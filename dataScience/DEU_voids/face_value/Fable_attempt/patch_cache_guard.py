#!/usr/bin/env python3
# CACHE-GUARD PATCH (2026-07-22) -- closes the stale-cache gap found in the
# void B0 freeze: resumable workers skipped existing caches without checking
# that they were produced under the CURRENT config, and analyzers ingested
# whatever matched the glob. Two defenses, both bundles:
#   1. Cache filenames embed an 8-hex SHA-256 of the full config, so a config
#      change can never be satisfied by an old cache (worker re-runs).
#   2. Analyzers/selectors verify the config hash stored INSIDE each cache and
#      ABORT (not skip) on mismatch, with an instruction to clear stale caches.
# Run from a directory containing b0_bundle/ and/or c26_bundle/, or point it:
#   python3 patch_cache_guard.py [b0_dir] [c26_dir]
# Anchored exact-string edits; aborts if any anchor is not found exactly once.
# APPLY BEFORE (RE-)FREEZING so the manifests capture the patched files.
import sys
from pathlib import Path

def apply(path, edits):
    p = Path(path)
    if not p.exists():
        print(f"skip {p} (not found)"); return False
    src = p.read_text(encoding="utf-8")
    for i, (old, new) in enumerate(edits):
        n = src.count(old)
        if n != 1:
            sys.exit(f"PATCH ABORT: {p.name} edit {i} anchor occurs {n} times")
        src = src.replace(old, new)
    p.write_text(src, encoding="utf-8", newline="\n")
    print(f"patched {p}")
    return True

B0_WORKER = [
("import gzip, json, os, pickle, sys, time",
 "import gzip, hashlib, json, os, pickle, sys, time"),
("""    cache_dir = Path(cache_dir); cache_dir.mkdir(parents=True, exist_ok=True)
    out = cache_dir / f"b0_seed{seed}.pkl.gz\"""",
 """    cache_dir = Path(cache_dir); cache_dir.mkdir(parents=True, exist_ok=True)
    cfgh = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode("utf-8")).hexdigest()[:8]
    out = cache_dir / f"b0_seed{seed}_cfg{cfgh}.pkl.gz\""""),
("""    payload = dict(schema="b0_cache_v1", seed=int(seed), config=dict(cfg),""",
 """    payload = dict(schema="b0_cache_v1", seed=int(seed), config=dict(cfg),
                   cfg_hash=cfgh,"""),
]

B0_ADJ = [
("""import gzip, json, pickle, sys""",
 """import gzip, hashlib, json, pickle, sys"""),
("""    cfg = json.loads(Path(cfgp).read_text(encoding="utf-8"))["gates_b0"]
    seeds = []
    for p in sorted(Path(cache_dir).glob("b0_seed*.pkl.gz")):
        with gzip.open(p, "rb") as f: rec = pickle.load(f)""",
 """    full = json.loads(Path(cfgp).read_text(encoding="utf-8"))
    cfg = full["gates_b0"]
    cfgh = hashlib.sha256(json.dumps(full, sort_keys=True).encode("utf-8")).hexdigest()[:8]
    seeds = []
    for p in sorted(Path(cache_dir).glob("b0_seed*.pkl.gz")):
        with gzip.open(p, "rb") as f: rec = pickle.load(f)
        if rec.get("cfg_hash") != cfgh:
            sys.exit(f"ADJUDICATE ABORT: {p.name} was produced under a different "
                     f"config (cache {rec.get('cfg_hash')} vs current {cfgh}). "
                     "Clear stale caches from the cache_dir and rerun the run stage.")"""),
]

C26_WORKER = [
("import gzip, json, os, pickle, sys, time",
 "import gzip, hashlib, json, os, pickle, sys, time"),
("""    cache_dir = Path(cache_dir); cache_dir.mkdir(parents=True, exist_ok=True)
    out = cache_dir / f"c26_seed{seed}.pkl.gz\"""",
 """    cache_dir = Path(cache_dir); cache_dir.mkdir(parents=True, exist_ok=True)
    cfgh = hashlib.sha256(json.dumps(cfg, sort_keys=True).encode("utf-8")).hexdigest()[:8]
    out = cache_dir / f"c26_seed{seed}_cfg{cfgh}.pkl.gz\""""),
("""    payload = dict(
        schema="c26_cache_v1", seed=int(seed), config=dict(cfg),""",
 """    payload = dict(
        schema="c26_cache_v1", seed=int(seed), config=dict(cfg), cfg_hash=cfgh,"""),
]

C26_FIREWALL = [
("""WHITELIST_TOP = ("schema", "seed", "config", "final_epoch", "formation_end",""",
 """WHITELIST_TOP = ("schema", "seed", "config", "cfg_hash", "final_epoch", "formation_end","""),
]

C26_SELECT = [
("""import heapq, itertools, json, sys""",
 """import hashlib, heapq, itertools, json, sys"""),
("""def main(cfgp, cache_dir, outp):
    cfg = json.loads(Path(cfgp).read_text(encoding="utf-8"))["selection"]
    rows = []
    for p in sorted(Path(cache_dir).glob("c26_seed*.pkl.gz")):
        rows.append(preflight_seed(load_whitelisted(p), cfg))""",
 """def main(cfgp, cache_dir, outp):
    full = json.loads(Path(cfgp).read_text(encoding="utf-8"))
    cfg = full["selection"]
    cfgh = hashlib.sha256(json.dumps(full, sort_keys=True).encode("utf-8")).hexdigest()[:8]
    rows = []
    for p in sorted(Path(cache_dir).glob("c26_seed*.pkl.gz")):
        view = load_whitelisted(p)
        if view.get("cfg_hash") != cfgh:
            sys.exit(f"SELECT ABORT: {p.name} was produced under a different "
                     f"config (cache {view.get('cfg_hash')} vs current {cfgh}). "
                     "Clear stale caches from the cache_dir and rerun the run stage.")
        rows.append(preflight_seed(view, cfg))"""),
]

def main():
    b0 = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("b0_bundle")
    c26 = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("c26_bundle")
    any_ok = False
    any_ok |= apply(b0 / "b0_worker.py", B0_WORKER)
    any_ok |= apply(b0 / "b0_adjudicate.py", B0_ADJ)
    any_ok |= apply(c26 / "c26_worker.py", C26_WORKER)
    any_ok |= apply(c26 / "c26_firewall.py", C26_FIREWALL)
    any_ok |= apply(c26 / "c26_select.py", C26_SELECT)
    if not any_ok:
        sys.exit("PATCH ABORT: no bundle directories found")
    print("\nDONE. Delete all existing *_seed*.pkl.gz caches now, then (re-)freeze "
          "so the manifests capture the patched files.")

if __name__ == "__main__":
    main()
