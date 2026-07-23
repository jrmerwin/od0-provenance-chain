#!/usr/bin/env python3
# C26 staged driver.
#   Stage 0  preflight   mandatory wc -l manifest check (shadow-cache dragon)
#   Stage 1  certify     base 10/10, variant 10/10, instruments-ON identity gate
#   Stage 2  run         per-seed workers (subprocess, resumable, budgeted)
#   Stage 3  select      firewall-loaded candidate selection
#   Stage 4  adjudicate  gates + registered classification
# Usage: python3 c26_driver.py <stage|all> <config.json> [budget_seconds]
# Frozen runs additionally require FREEZE_MANIFEST.json and a formation schedule
# with certified_for_freeze=True; otherwise the driver runs in SMOKE mode and
# says so loudly.
import hashlib, json, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = ["make_v21i4_c26.py", "c26_formation_adapter.py", "c26_worker.py",
          "c26_firewall.py", "c26_select.py", "c26_adjudicate.py", "c26_driver.py"]

def sh(cmd, timeout=None):
    print("+", " ".join(map(str, cmd)))
    r = subprocess.run(list(map(str, cmd)), timeout=timeout)
    if r.returncode != 0:
        sys.exit(f"DRIVER ABORT: {' '.join(map(str,cmd))} rc={r.returncode}")

def stage0(cfg):
    man = HERE / "FREEZE_MANIFEST.json"
    counts = {f: len((HERE / f).read_text(encoding="utf-8").splitlines())
              for f in BUNDLE}
    print("wc -l:", counts)
    for f in BUNDLE:
        if counts[f] < 10:
            sys.exit(f"DRIVER ABORT: {f} suspiciously short -- shadow-cache path failure?")
    if man.exists():
        rec = json.loads(man.read_text(encoding="utf-8"))
        for f, n in rec["wc_l"].items():
            if counts.get(f) != n:
                sys.exit(f"DRIVER ABORT: {f} line count {counts.get(f)} != frozen {n}")
        print("FROZEN mode: manifest verified")
        return True
    print("SMOKE mode: no FREEZE_MANIFEST.json -- results are NOT registerable")
    return False

def stage1(cfg, frozen):
    eng = Path(cfg["engine_dir"]).resolve()
    cert = eng.parent / "certification" / "certify.py"
    if not (eng / "rung1_v21i4_c26.py").exists():
        sh([sys.executable, HERE / "make_v21i4_c26.py"])
    sh([sys.executable, cert], timeout=600)                       # base
    sh([sys.executable, cert, eng / "rung1_v21i4_c26.py"], timeout=600)  # variant
    # instruments-ON shared-column identity gate (the round's keystone gate)
    code = f"""
import os, numpy as np
os.chdir({str(eng)!r})
nsb, nsv = {{}}, {{}}
exec(open('rung1_v21_zeno.py').read(), nsb)
exec(open('rung1_v21i4_c26.py').read(), nsv)
kw = dict(seed=110, final_epoch=100, defect_inject_epoch=50, r_core=0.06,
          pulse_size=104, pulse_every=4, pulse_start=55, n_pulses=11)
eb = nsb['grow_native'](**kw).epoch_log
ev = nsv['grow_native'](**kw, snap_every=10, snap_relief=True).epoch_log
shared = [c for c in eb.columns if c in ev.columns]
assert all((eb[c].values == ev[c].values).all() for c in shared), 'IDENTITY FAIL'
print(f'identity gate: PASS ({{len(shared)}} shared columns bit-identical)')
"""
    sh([sys.executable, "-c", code], timeout=300)

def stage2(cfg, budget):
    seeds = json.loads((HERE / cfg["seeds_file"]).read_text(encoding="utf-8"))["cohort"]
    t0, done = time.time(), 0
    for s in seeds:
        if budget and time.time() - t0 > budget:
            print(f"budget reached after {done}/{len(seeds)} seeds; rerun to resume")
            return False
        sh([sys.executable, HERE / "c26_worker.py", s, HERE / "c26_config.json",
            cfg["cache_dir"], cfg["engine_dir"]])
        done += 1
    return True

def stage3(cfg):
    sh([sys.executable, HERE / "c26_select.py", HERE / "c26_config.json",
        cfg["cache_dir"], HERE / "c26_selection.json"])

def stage4(cfg):
    sh([sys.executable, HERE / "c26_adjudicate.py", HERE / "c26_config.json",
        HERE / "c26_selection.json", HERE / cfg["seeds_file"],
        HERE / "c26_decision.json"])

def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    cfgp = sys.argv[2] if len(sys.argv) > 2 else HERE / "c26_config.json"
    budget = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    cfg = json.loads(Path(cfgp).read_text(encoding="utf-8"))
    frozen = stage0(cfg)
    if frozen:
        import c26_formation_adapter as fa  # noqa
        # frozen runs must not use the fallback schedule
        if cfg.get("formation_label", "").startswith("NATIVE_FALLBACK"):
            sys.exit("DRIVER ABORT: frozen run with fallback formation adapter")
    if stage in ("certify", "all"): stage1(cfg, frozen)
    complete = True
    if stage in ("run", "all"):     complete = stage2(cfg, budget)
    if not complete and stage == "all":
        print("SELECT/ADJUDICATE SKIPPED: run stage incomplete (budget); "
              "rerun to resume.")
        return
    if stage in ("select", "all"):  stage3(cfg)
    if stage in ("adjudicate", "all"): stage4(cfg)

if __name__ == "__main__":
    main()
