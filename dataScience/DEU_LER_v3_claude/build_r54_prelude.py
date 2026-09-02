#!/usr/bin/env python3
"""R54 prelude: provenance stamps (R52/R53), H2 supply check, H1 hash
verification against the R48 holdout manifest, and R54_INPUT_LOCK.json
assembly. All hashes computed in-process (hash hygiene).

No H1 content is read here: files are hashed (bytes -> sha256) only.
"""
import hashlib
import json
import subprocess
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          cwd=PKG).stdout.strip()


# ---- provenance stamps (standing convention from R54 on) ----
for rnd, commitB in (("R52", "3e55670"), ("R53", "8c1a470")):
    stamp = {
        "schema": f"OD0_{rnd}_PROVENANCE_STAMP_V1",
        "campaign": f"OD0-{rnd}",
        "commit_B_resolved": git("rev-parse", commitB),
        "output_manifest_path": f"{rnd}_OUTPUT_MANIFEST.json",
        "output_manifest_sha256": sha256_file(
            PKG / f"{rnd}_OUTPUT_MANIFEST.json"),
        "convention": "every round ends with a stamp commit; reports never "
                      "carry placeholders again (R54 housekeeping rule, "
                      "standing)",
    }
    (PKG / f"{rnd}_PROVENANCE_STAMP.json").write_text(
        json.dumps(stamp, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print(f"{rnd} stamp:", stamp["commit_B_resolved"][:12],
          stamp["output_manifest_sha256"][:12])

# ---- R53 pin ----
r53_manifest_sha = sha256_file(PKG / "R53_OUTPUT_MANIFEST.json")

# ---- R48 holdout manifest pin (cross-checked against frozen R48 manifest) ----
r48_out = json.loads((PKG / "R48_OUTPUT_MANIFEST.json").read_text(encoding="utf-8"))
holdout_entry = next(e for e in r48_out["files"]
                     if e["path"] == "R48_HOLDOUT_MANIFEST.json")
holdout_on_disk = sha256_file(PKG / "R48_HOLDOUT_MANIFEST.json")
holdout_match = holdout_on_disk == holdout_entry["sha256"]
print("R48 holdout manifest pin match:", holdout_match)

# ---- H1 hash verification (bytes only; no content read) ----
holdout = json.loads((PKG / "R48_HOLDOUT_MANIFEST.json").read_text(encoding="utf-8"))
h1_items = holdout["items_by_tag"].get("H1", [])
verified, mismatched, missing, unhashable = [], [], [], []
for item in h1_items:
    p = Path(item["path"])
    rec = {"path": item["path"], "pinned_sha256": item.get("sha256")}
    if not p.exists() or not p.is_file():
        if p.exists() and p.is_dir():
            rec["status"] = "DIRECTORY_PIN"
            unhashable.append(rec)
        else:
            rec["status"] = "MISSING"
            missing.append(rec)
        continue
    now = sha256_file(p)
    rec["sha256_now"] = now
    pin = item.get("sha256")
    if pin in (None, "SKIPPED_OVER_50MB",
               "DIRECTORY_PIN_MEMBERS_LISTED_IN_CENSUS",
               "PATH_NOT_A_FILE_AT_PIPELINE_TIME"):
        rec["status"] = "HASHED_NOW_NO_BYTE_PIN"
        unhashable.append(rec)
    elif now == pin:
        rec["status"] = "VERIFIED"
        verified.append(rec)
    else:
        rec["status"] = "HASH_MISMATCH"
        mismatched.append(rec)
print(f"H1: {len(h1_items)} items; verified {len(verified)}, "
      f"mismatched {len(mismatched)}, missing {len(missing)}, "
      f"no-byte-pin {len(unhashable)}")

# ---- H2 supply check (Run3_Dijet placed in the working directory?) ----
h2_candidates = sorted(str(p.name) for p in PKG.glob("*un3*")) + \
    sorted(str(p.name) for p in PKG.glob("*ijet*"))
h2_status = ("PINNED" if h2_candidates else
             "INCOMPLETE - no Run3_Dijet artifacts supplied to the "
             "holdout directory; H2 sentinel remains parsed=false")
print("H2:", h2_status, h2_candidates)

# ---- sentinels ----
sentinels = {tag: "parsed=false (sealed; not opened in R54)"
             for tag in ("H2", "H3", "H4", "H5")}

# ---- protocol copied verbatim from R53_INPUT_LOCK.json ----
r53_lock = json.loads((PKG / "R53_INPUT_LOCK.json").read_text(encoding="utf-8"))
protocol = r53_lock["frozen_r54_comparison_protocol_sec_8"]
r53_lock_sha = sha256_file(PKG / "R53_INPUT_LOCK.json")

# ---- derived-side table (Section 3, frozen; from R52/R53 outputs only) ----
DERIVED_TABLE = {
    "filtration_order": [
        {"item": "E0 (free) -> E1 (congested), permanent exit at D > Gamma",
         "class": "THEOREM"},
        {"item": "within E1: {c_min <= Gamma} transient (last exit a "
                 "finite random step)", "class": "THEOREM"},
        {"item": "within E1: drained/draining alternation (renewal at F=0)",
         "class": "THEOREM"},
        {"item": "within E1: burst/quiet decomposition",
         "class": "EXACT_DECOMPOSITION"},
        {"item": "asymptotic: |X| -> infinity a.s. for m < Gamma",
         "class": "THEOREM"},
        {"item": "asymptotic rate <= linear", "class": "THEOREM"},
        {"item": "asymptotic sqrt-k-type curve", "class": "READOUT"},
    ],
    "monotone_observables": [
        {"observable": "|X|", "direction": "nondecreasing",
         "class": "THEOREM"},
        {"observable": "recorded-cone mask", "direction": "nondecreasing",
         "class": "THEOREM"},
        {"observable": "shell fraction u = |U|/|X|",
         "direction": "slowly increasing in R53 readouts at registered "
                      "points (shell mean grows with |X|; fraction "
                      "drifts up mildly)", "class": "READOUT"},
        {"observable": "chain-multiplicity distribution",
         "direction": "mean nondecreasing in |X| (parent-sum recurrence); "
                      "tail shape from readouts", "class":
         "THEOREM(mean)/READOUT(tail)"},
        {"observable": "cycle length / drain length",
         "direction": "two-sided bounds growing with burst cost "
                      "(THEOREM); geometric growth (CONJECTURE)",
         "class": "THEOREM(bounds)/CONJECTURE(geometric)"},
        {"observable": "full-drain frequency",
         "direction": "decreasing in readouts", "class": "READOUT"},
        {"observable": "burst cost",
         "direction": "c_min not monotone (THEOREM witness); typical "
                      "burst cost increasing", "class":
         "THEOREM(c_min)/READOUT(typical)"},
    ],
    "frozen_rule": "nothing added after Commit A",
}

lock = {
    "schema": "OD0_R54_INPUT_LOCK_V1",
    "campaign": "OD0-R54",
    "run_date": "2026-09-02",
    "package": {
        "path": "dataScience/DEU_LER_v3_claude/"
                "OD0_CLAUDE_CODE_PACKAGE_R54_OPEN_H1_UNDER_FROZEN_PROTOCOL_v0_1.md",
        "sha256": sha256_file(
            PKG / "OD0_CLAUDE_CODE_PACKAGE_R54_OPEN_H1_UNDER_FROZEN_PROTOCOL_v0_1.md"),
        "executor": "Claude Code (Fable 5)",
    },
    "r53_pin_block": {
        "output_manifest_sha256_on_disk": r53_manifest_sha,
        "prefix_match_c985a7ca": r53_manifest_sha.startswith("c985a7ca"),
        "commit_A_resolved": git("rev-parse", "33c1782"),
        "commit_B_resolved": git("rev-parse", "8c1a470"),
        "transitive": "R52..R47 via the pinned chain of input locks",
    },
    "r48_holdout_manifest_pin": {
        "sha256_on_disk": holdout_on_disk,
        "sha256_in_frozen_r48_manifest": holdout_entry["sha256"],
        "match": holdout_match,
    },
    "protocol_verbatim_from_r53_lock": protocol,
    "r53_input_lock_sha256": r53_lock_sha,
    "derived_side_table_frozen": DERIVED_TABLE,
    "h1_hash_verification": {
        "items": len(h1_items),
        "verified": verified,
        "mismatched": mismatched,
        "missing": missing,
        "no_byte_pin_hashed_now": unhashable,
    },
    "h1_extraction_scope_note": "The extraction targets the registry-"
        "persistence/structural-epochs paper family and its result "
        "archives and notes (per Section 4). H1-tagged items that are "
        "Codex-side od0_r48..r50 round directories are OUT OF EXTRACTION "
        "SCOPE: they are neither the paper nor its archives, and reading "
        "a parallel executor's boundary analyses would contaminate the "
        "comparison. Recorded here before opening.",
    "h2_pin_status": {"status": h2_status, "candidates": h2_candidates},
    "sentinels_h2_h5": sentinels,
    "declarations": {
        "BELL2_opened": False,
        "hand_produced_hashes": 0,
        "hash_hygiene_in_force": True,
        "nothing_added_moved_renamed_after_commit_A": True,
    },
    "worktree_state_at_start": {
        "pre_existing_deltas": "36 unstaged deletions + 60 untracked "
                               "paths (DEU_voids + root .gitignore), "
                               "unchanged; none touch pinned roots",
        "frozen_root_modification_check_at_start": "CLEAN",
    },
}

out = PKG / "R54_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("wrote", out.name, sha256_file(out))
