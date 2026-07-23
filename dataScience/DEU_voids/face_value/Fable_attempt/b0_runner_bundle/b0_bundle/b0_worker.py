#!/usr/bin/env python3
# B0 per-seed worker: TWO ARMS per seed on the same random stream.
#   pocket arm : formation burst (adapter schedule) -> source-off quiet window
#   control arm: identical run with the burst withheld (pulse_size=0) --
#                the C13-style relief-free vacuum baseline
# Run-validity: C15 zero-hold clearance on the pocket arm.
# Atomic gzip-pickle caches, resumable. No selection, no firewall: B0 is a
# registered read-only instrument round; demand/service ARE the observables.
# Usage: python3 b0_worker.py <seed> <config.json> <cache_dir> [engine_dir]
import gzip, hashlib, json, os, pickle, sys, time
from pathlib import Path

def load_engine(engine_dir):
    eng = Path(engine_dir)
    src = (eng / "rung1_v21i5_b0.py").read_text(encoding="utf-8")
    ns = {}; cwd = os.getcwd(); os.chdir(eng)
    try: exec(compile(src, "rung1_v21i5_b0", "exec"), ns)
    finally: os.chdir(cwd)
    return ns["grow_native"]

def zero_hold(epoch_log, start, hold):
    el = epoch_log[epoch_log.epoch >= start]; run = 0
    for ep, b in zip(el.epoch, el.backlog):
        run = run + 1 if b == 0 else 0
        if run >= hold: return int(ep)
    return None

def run_seed(seed, cfg, cache_dir, engine_dir):
    cache_dir = Path(cache_dir); cache_dir.mkdir(parents=True, exist_ok=True)
    cfgh = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode("utf-8")).hexdigest()[:8]
    out = cache_dir / f"b0_seed{seed}_cfg{cfgh}.pkl.gz"
    if out.exists():
        try:
            with gzip.open(out, "rb") as f: pickle.load(f)
            print(f"seed {seed}: cache exists, skip"); return 0
        except Exception:
            print(f"seed {seed}: corrupt cache, rerun"); out.unlink()
    grow = load_engine(engine_dir)
    fe = int(cfg["formation_end"])
    final = fe + int(cfg["clearance_hold"]) + int(cfg["clearance_scan_extra"]) \
               + int(cfg["observation_epochs"])
    base = dict(seed=int(seed), final_epoch=final,
                defect_inject_epoch=int(cfg["defect_inject_epoch"]),
                r_core=float(cfg["r_core"]), b0_log=True,
                b0_rmax=float(cfg["b0_rmax"]), b0_kpocket=int(cfg["b0_kpocket"]),
                b0_shellw=float(cfg["b0_shellw"]))
    t0 = time.time()
    rp = grow(**base, pulse_size=int(cfg["pulse_size"]),
              pulse_every=int(cfg["pulse_every"]),
              pulse_start=int(cfg["pulse_start"]), n_pulses=int(cfg["n_pulses"]))
    rc = grow(**base, pulse_size=0, pulse_every=0,
              pulse_start=int(cfg["pulse_start"]), n_pulses=0)
    clr = zero_hold(rp.epoch_log, fe, int(cfg["clearance_hold"]))
    payload = dict(schema="b0_cache_v1", seed=int(seed), config=dict(cfg),
                   cfg_hash=cfgh,
                   final_epoch=final, formation_end=fe,
                   clearance_epoch=clr, clearance_ok=clr is not None,
                   obs_start=final - int(cfg["observation_epochs"]),
                   pocket_log=rp.stats["b0"]["log"],
                   control_log=rc.stats["b0"]["log"],
                   wall_seconds=round(time.time() - t0, 1))
    tmp = out.with_suffix(".tmp")
    with gzip.open(tmp, "wb") as f: pickle.dump(payload, f, protocol=4)
    os.replace(tmp, out)
    print(f"seed {seed}: done in {payload['wall_seconds']}s, "
          f"clearance={'OK@'+str(clr) if clr else 'FAILED'}, cache={out.name}")
    return 0

if __name__ == "__main__":
    seed, cfgp, cache = sys.argv[1], sys.argv[2], sys.argv[3]
    engd = sys.argv[4] if len(sys.argv) > 4 else "../generative-ledger/engines"
    cfg = json.loads(Path(cfgp).read_text(encoding="utf-8"))
    sys.exit(run_seed(int(seed), cfg, cache, engd))
