#!/usr/bin/env python3
# B0 freeze tool: run ONCE after ratified values are written into the B0 spec
# and the certified metric adapter is installed. Deterministic seed list from
# the spec hash (LCG64, disjoint from C26's stream by construction: different
# document, different hash). Writes b0_seeds.json + B0_FREEZE_MANIFEST.json.
# Usage: python3 b0_freeze.py <B0_spec.md> [--force]
import hashlib, json, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = ["make_v21i5_b0.py", "b0_worker.py", "b0_adjudicate.py",
          "b0_driver.py", "b0_formation_adapter.py", "b0_config.json"]

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    spec = Path(sys.argv[1]); force = "--force" in sys.argv
    man = HERE / "B0_FREEZE_MANIFEST.json"
    if man.exists() and not force:
        sys.exit("FREEZE ABORT: manifest already exists (freeze is once)")
    cfg = json.loads((HERE / "b0_config.json").read_text(encoding="utf-8"))
    if cfg.get("formation_label", "").startswith("NATIVE_FALLBACK") and not force:
        sys.exit("FREEZE ABORT: config still uses the uncertified fallback adapter")
    h = sha(spec); x = int(h[:16], 16)
    seeds, lo, hi = [], 100000, 999999
    while len(seeds) < cfg.get("reserve_size", 20):
        x = (6364136223846793005 * x + 1442695040888963407) % (1 << 64)
        s = lo + (x >> 16) % (hi - lo)
        if s not in seeds: seeds.append(s)
    cohort = seeds[:cfg.get("cohort_size", 10)]
    (HERE / "b0_seeds.json").write_text(json.dumps(
        dict(source_spec_sha256=h, reserve=seeds, cohort=cohort)),
        encoding="utf-8", newline="\n")
    rec = dict(round="B0",
               frozen_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               spec=dict(file=spec.name, sha256=h),
               files={f: sha(HERE / f) for f in BUNDLE},
               seeds_sha256=sha(HERE / "b0_seeds.json"),
               wc_l={f: len((HERE / f).read_text(encoding="utf-8").splitlines())
                     for f in BUNDLE})
    man.write_text(json.dumps(rec, indent=1), encoding="utf-8", newline="\n")
    print(json.dumps(rec, indent=1))
    print("\nFROZEN. Commit b0_seeds.json + B0_FREEZE_MANIFEST.json + spec together.")

if __name__ == "__main__":
    main()
