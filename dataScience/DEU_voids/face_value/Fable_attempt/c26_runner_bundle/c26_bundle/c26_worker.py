#!/usr/bin/env python3
# C26 per-seed worker.
# Runs one seed through: formation (adapter schedule) -> source-off clearance
# certification (C15 rule: 128-epoch backlog zero-hold) -> observation window.
# Writes an atomic gzip-pickle cache. Resumable: an existing valid cache is kept.
#
# The worker performs RUN-VALIDITY checks only (clearance). It performs no
# candidate selection and reads no effect. Selection happens behind the firewall.
#
# Usage: python3 c26_worker.py <seed> <config.json> <cache_dir> [engine_dir]
import gzip, hashlib, json, os, pickle, sys, time
from pathlib import Path

def load_engine(engine_dir):
    eng = Path(engine_dir)
    src = (eng / "rung1_v21i4_c26.py").read_text(encoding="utf-8")
    ns = {}
    cwd = os.getcwd()
    os.chdir(eng)  # engine exec's its deps by relative path
    try:
        exec(compile(src, "rung1_v21i4_c26", "exec"), ns)
    finally:
        os.chdir(cwd)
    return ns["grow_native"]

def zero_hold_clearance(epoch_log, formation_end, hold=128):
    """C15 rule: first epoch >= formation_end after which backlog==0 for `hold`
    consecutive epochs. Returns clearance_epoch (end of hold) or None."""
    el = epoch_log[epoch_log.epoch >= formation_end]
    run = 0
    for ep, b in zip(el.epoch, el.backlog):
        run = run + 1 if b == 0 else 0
        if run >= hold:
            return int(ep)
    return None

def run_seed(seed, cfg, cache_dir, engine_dir):
    cache_dir = Path(cache_dir); cache_dir.mkdir(parents=True, exist_ok=True)
    cfgh = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode("utf-8")).hexdigest()[:8]
    out = cache_dir / f"c26_seed{seed}_cfg{cfgh}.pkl.gz"
    if out.exists():
        try:
            with gzip.open(out, "rb") as f:
                pickle.load(f)
            print(f"seed {seed}: cache exists, skip"); return 0
        except Exception:
            print(f"seed {seed}: corrupt cache, rerun"); out.unlink()

    grow = load_engine(engine_dir)
    fe = int(cfg["formation_end"])
    final = fe + int(cfg["clearance_hold"]) + int(cfg["clearance_scan_extra"]) \
               + int(cfg["observation_epochs"])
    t0 = time.time()
    r = grow(seed=int(seed), final_epoch=final,
             defect_inject_epoch=int(cfg["defect_inject_epoch"]),
             r_core=float(cfg["r_core"]),
             snap_every=int(cfg["snap_every"]), snap_relief=True,
             pulse_size=int(cfg["pulse_size"]), pulse_every=int(cfg["pulse_every"]),
             pulse_start=int(cfg["pulse_start"]), n_pulses=int(cfg["n_pulses"]))
    clearance = zero_hold_clearance(r.epoch_log, fe, int(cfg["clearance_hold"]))
    c26 = r.stats["c26"]
    snaps = {ep: dict(active_faces=sorted(s.active_faces),
                      face_nodes={int(f): sorted(n) for f, n in s.face_nodes.items()
                                  if f in s.active_faces},
                      face_types={int(f): s.face_types[f] for f in s.active_faces},
                      face_depth={int(f): int(s.face_depth[f]) for f in s.active_faces},
                      face_defect={int(f): bool(s.face_defect[f]) for f in s.active_faces})
             for ep, s in r.spatial_snapshots.items()}
    payload = dict(
        schema="c26_cache_v1", seed=int(seed), config=dict(cfg), cfg_hash=cfgh,
        final_epoch=final, formation_end=fe,
        clearance_epoch=clearance, clearance_ok=clearance is not None,
        relief_log=c26["relief_log"], frus_log=c26["frus_log"],
        lineage_snaps=c26["lineage_snaps"], snapshots=snaps,
        epoch_log=r.epoch_log,   # raw archive; firewall strips this for selection
        wall_seconds=round(time.time() - t0, 1))
    tmp = out.with_suffix(".tmp")
    with gzip.open(tmp, "wb") as f:
        pickle.dump(payload, f, protocol=4)
    os.replace(tmp, out)
    print(f"seed {seed}: done in {payload['wall_seconds']}s, "
          f"clearance={'OK@'+str(clearance) if clearance else 'FAILED'}, "
          f"events={len(payload['relief_log'])}, cache={out.name}")
    return 0

if __name__ == "__main__":
    seed, cfgp, cache = sys.argv[1], sys.argv[2], sys.argv[3]
    engd = sys.argv[4] if len(sys.argv) > 4 else "../generative-ledger/engines"
    cfg = json.loads(Path(cfgp).read_text(encoding="utf-8"))
    sys.exit(run_seed(int(seed), cfg, cache, engd))
