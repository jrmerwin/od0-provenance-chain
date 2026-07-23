#!/usr/bin/env python3
# B0 staged driver: preflight (wc -l) -> certify -> run -> adjudicate.
# Frozen mode requires B0_FREEZE_MANIFEST.json (written by b0_freeze.py).
# Usage: python3 b0_driver.py <stage|all> <config.json> [budget_seconds]
import json, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = ["make_v21i5_b0.py", "b0_worker.py", "b0_adjudicate.py", "b0_driver.py"]

IDENTITY_GATE = """
import os, numpy as np
os.chdir({eng!r})
nsb, nsv = {{}}, {{}}
exec(open('rung1_v21_zeno.py').read(), nsb)
exec(open('rung1_v21i5_b0.py').read(), nsv)
kw = dict(seed=110, final_epoch=100, defect_inject_epoch=50, r_core=0.06,
          pulse_size=104, pulse_every=4, pulse_start=55, n_pulses=11)
eb = nsb['grow_native'](**kw).epoch_log
ev = nsv['grow_native'](**kw, b0_log=True).epoch_log
shared = [c for c in eb.columns if c in ev.columns]
ok = all((eb[c].values == ev[c].values).all() for c in shared)
print('identity gate (b0_log=True):', 'PASS' if ok else '*** GATE VIOLATION ***',
      '(%d shared columns)' % len(shared))
raise SystemExit(0 if ok else 1)
"""

def sh(cmd, timeout=None, label=None):
    print("+", label or " ".join(map(str, cmd)))
    r = subprocess.run(list(map(str, cmd)), timeout=timeout)
    if r.returncode != 0:
        sys.exit(f"DRIVER ABORT: rc={r.returncode}")

def stage0():
    counts = {f: len((HERE / f).read_text(encoding="utf-8").splitlines())
              for f in BUNDLE}
    print("wc -l:", counts)
    for f, n in counts.items():
        if n < 10:
            sys.exit(f"DRIVER ABORT: {f} suspiciously short")
    man = HERE / "B0_FREEZE_MANIFEST.json"
    if man.exists():
        rec = json.loads(man.read_text(encoding="utf-8"))
        for f, n in rec["wc_l"].items():
            if f in counts and counts[f] != n:
                sys.exit(f"DRIVER ABORT: {f} line count {counts[f]} != frozen {n}")
        print("FROZEN mode: manifest verified"); return True
    print("SMOKE mode: no B0_FREEZE_MANIFEST.json -- results are NOT registerable")
    return False

def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    cfgp = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "b0_config.json"
    budget = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    cfg = json.loads(cfgp.read_text(encoding="utf-8"))
    frozen = stage0()
    if frozen and cfg.get("formation_label", "").startswith("NATIVE_FALLBACK"):
        sys.exit("DRIVER ABORT: frozen run with fallback formation adapter")
    eng = Path(cfg["engine_dir"]).resolve()
    if stage in ("certify", "all"):
        cert = eng.parent / "certification" / "certify.py"
        if not (eng / "rung1_v21i5_b0.py").exists():
            sh([sys.executable, HERE / "make_v21i5_b0.py"])
        sh([sys.executable, cert, eng / "rung1_v21i5_b0.py"], timeout=600)
        sh([sys.executable, "-c", IDENTITY_GATE.format(eng=str(eng))],
           timeout=300, label="[shared-column identity gate, b0_log=True]")
    run_complete = True
    if stage in ("run", "all"):
        seeds = json.loads((HERE / cfg["seeds_file"]).read_text(encoding="utf-8"))["cohort"]
        t0, done = time.time(), 0
        for s in seeds:
            if budget and time.time() - t0 > budget:
                print(f"budget reached after {done}/{len(seeds)} seeds; rerun to resume")
                run_complete = False
                break
            sh([sys.executable, HERE / "b0_worker.py", s, cfgp,
                cfg["cache_dir"], cfg["engine_dir"]])
            done += 1
    if stage in ("adjudicate", "all"):
        if not run_complete:
            print("ADJUDICATION SKIPPED: run stage incomplete (budget). "
                  "Rerun the run stage to resume; adjudication requires the full cohort.")
            return
        sh([sys.executable, HERE / "b0_adjudicate.py", cfgp, cfg["cache_dir"],
            HERE / cfg["seeds_file"], HERE / "b0_decision.json"])

if __name__ == "__main__":
    main()
