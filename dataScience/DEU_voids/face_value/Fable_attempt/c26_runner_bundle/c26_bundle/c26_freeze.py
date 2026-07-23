#!/usr/bin/env python3
# C26 freeze tool. Run ONCE, after all [FREEZE-POINT] values are ratified and the
# certified formation adapter is installed. Produces:
#   c26_seeds.json      ordered reserve seed list (deterministic from prereg hash)
#   FREEZE_MANIFEST.json  SHA-256 of prereg + every bundle file + config,
#                         wc -l counts, timestamp
# After this, the driver runs in FROZEN mode and refuses tampered files.
# Usage: python3 c26_freeze.py <prereg.md> [--force]
import hashlib, json, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = ["make_v21i4_c26.py", "c26_formation_adapter.py", "c26_worker.py",
          "c26_firewall.py", "c26_select.py", "c26_adjudicate.py", "c26_driver.py",
          "c26_config.json"]

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    prereg = Path(sys.argv[1])
    force = "--force" in sys.argv
    man = HERE / "FREEZE_MANIFEST.json"
    if man.exists() and not force:
        sys.exit("FREEZE ABORT: manifest already exists (freeze is once)")
    cfg = json.loads((HERE / "c26_config.json").read_text(encoding="utf-8"))
    if cfg.get("formation_label", "").startswith("NATIVE_FALLBACK") and not force:
        sys.exit("FREEZE ABORT: config still uses the uncertified fallback "
                 "formation adapter (prereg section 3)")
    h = sha(prereg)
    rng_stream = int(h[:16], 16)
    n_reserve, lo, hi = cfg["reserve_size"], 100000, 999999
    seeds, x = [], rng_stream
    while len(seeds) < n_reserve:
        x = (6364136223846793005 * x + 1442695040888963407) % (1 << 64)  # LCG64
        s = lo + (x >> 16) % (hi - lo)
        if s not in seeds: seeds.append(s)
    cohort = seeds[:cfg["cohort_size"]]
    (HERE / "c26_seeds.json").write_text(json.dumps(
        dict(source_prereg_sha256=h, reserve=seeds, cohort=cohort,
             note="cohort split: list-position even->discovery, odd->validation"),
        indent=1), encoding="utf-8", newline="\n")
    rec = dict(round="C26", frozen_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               prereg=dict(file=prereg.name, sha256=h),
               files={f: sha(HERE / f) for f in BUNDLE},
               seeds_sha256=sha(HERE / "c26_seeds.json"),
               wc_l={f: len((HERE / f).read_text(encoding="utf-8").splitlines())
                     for f in BUNDLE + ["c26_seeds.json"]})
    man.write_text(json.dumps(rec, indent=1), encoding="utf-8", newline="\n")
    print(json.dumps(rec, indent=1))
    print("\nFROZEN. Commit c26_seeds.json + FREEZE_MANIFEST.json + prereg together.")

if __name__ == "__main__":
    main()
