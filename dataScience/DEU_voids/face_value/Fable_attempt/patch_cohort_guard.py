#!/usr/bin/env python3
# COHORT-GUARD PATCH (2026-07-22) -- closes the partial-cohort gap: a budget
# interrupt in the run stage previously fell through to selection/adjudication,
# scoring registered gates against an incomplete cohort. Two defenses, both
# bundles:
#   1. Drivers: an incomplete run stage halts the pipeline in 'all' mode.
#   2. Adjudicators: verify every cohort seed is present and ABORT if any are
#      missing, so a standalone adjudicate call can never score a partial cohort.
# Usage: python3 patch_cohort_guard.py [b0_dir] [c26_dir]
# APPLY BEFORE (RE-)FREEZING so manifests capture the patched files.
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

B0_DRIVER = [
("""    if stage in ("run", "all"):
        seeds = json.loads((HERE / cfg["seeds_file"]).read_text(encoding="utf-8"))["cohort"]
        t0, done = time.time(), 0
        for s in seeds:
            if budget and time.time() - t0 > budget:
                print(f"budget reached after {done}/{len(seeds)} seeds; rerun to resume")
                break
            sh([sys.executable, HERE / "b0_worker.py", s, cfgp,
                cfg["cache_dir"], cfg["engine_dir"]])
            done += 1
    if stage in ("adjudicate", "all"):
        sh([sys.executable, HERE / "b0_adjudicate.py", cfgp, cfg["cache_dir"],
            HERE / "b0_decision.json"])""",
 """    run_complete = True
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
            HERE / cfg["seeds_file"], HERE / "b0_decision.json"])"""),
]

B0_ADJ = [
("""def main(cfgp, cache_dir, outp):
    full = json.loads(Path(cfgp).read_text(encoding="utf-8"))""",
 """def main(cfgp, cache_dir, seedsp, outp):
    cohort = json.loads(Path(seedsp).read_text(encoding="utf-8"))["cohort"]
    full = json.loads(Path(cfgp).read_text(encoding="utf-8"))"""),
("""    val = [s for s in seeds if s["clearance_ok"]]""",
 """    present = {s["seed"] for s in seeds}
    missing = [s for s in cohort if s not in present]
    if missing:
        sys.exit(f"ADJUDICATE ABORT: cohort incomplete -- missing seeds {missing}. "
                 "Rerun the run stage to resume; adjudication requires the full cohort.")
    val = [s for s in seeds if s["clearance_ok"]]"""),
("""    main(*sys.argv[1:4])""",
 """    main(*sys.argv[1:5])"""),
]

C26_DRIVER = [
("""        sh([sys.executable, HERE / "c26_worker.py", s, HERE / "c26_config.json",
            cfg["cache_dir"], cfg["engine_dir"]])
        done += 1""",
 """        sh([sys.executable, HERE / "c26_worker.py", s, HERE / "c26_config.json",
            cfg["cache_dir"], cfg["engine_dir"]])
        done += 1
    return True"""),
("""            print(f"budget reached after {done}/{len(seeds)} seeds; rerun to resume")
            return""",
 """            print(f"budget reached after {done}/{len(seeds)} seeds; rerun to resume")
            return False"""),
("""    if stage in ("run", "all"):     stage2(cfg, budget)
    if stage in ("select", "all"):  stage3(cfg)
    if stage in ("adjudicate", "all"): stage4(cfg)""",
 """    complete = True
    if stage in ("run", "all"):     complete = stage2(cfg, budget)
    if not complete and stage == "all":
        print("SELECT/ADJUDICATE SKIPPED: run stage incomplete (budget); "
              "rerun to resume.")
        return
    if stage in ("select", "all"):  stage3(cfg)
    if stage in ("adjudicate", "all"): stage4(cfg)"""),
]

C26_ADJ = [
("""    rows = [r for r in rows if r["seed"] in pos]""",
 """    rows = [r for r in rows if r["seed"] in pos]
    missing = [s for s in order if s not in {r["seed"] for r in rows}]
    if missing:
        sys.exit(f"ADJUDICATE ABORT: cohort incomplete -- missing seeds {missing}. "
                 "Rerun run+select stages; adjudication requires the full cohort.")"""),
]

def main():
    b0 = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("b0_bundle")
    c26 = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("c26_bundle")
    any_ok = False
    any_ok |= apply(b0 / "b0_driver.py", B0_DRIVER)
    any_ok |= apply(b0 / "b0_adjudicate.py", B0_ADJ)
    any_ok |= apply(c26 / "c26_driver.py", C26_DRIVER)
    any_ok |= apply(c26 / "c26_adjudicate.py", C26_ADJ)
    if not any_ok:
        sys.exit("PATCH ABORT: no bundle directories found")
    print("\nDONE. Note new wc -l counts for the manifests before (re-)freezing.")

if __name__ == "__main__":
    main()
