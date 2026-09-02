#!/usr/bin/env python3
"""Assemble R51_INPUT_LOCK.json (Commit A). All hashes computed in-process."""
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


R50_MANIFEST_PIN = None  # copied from disk below (hash hygiene: tool output only)

on_disk = sha256_file(PKG / "R50_OUTPUT_MANIFEST.json")

lock = {
    "schema": "OD0_R51_INPUT_LOCK_V1",
    "campaign": "OD0-R51",
    "run_date": "2026-09-02",
    "package": {
        "path": "dataScience/DEU_LER_v3_claude/"
                "OD0_CLAUDE_CODE_PACKAGE_R51_THROTTLE_PREMISE_CLASS_v0_1.md",
        "sha256": sha256_file(
            PKG / "OD0_CLAUDE_CODE_PACKAGE_R51_THROTTLE_PREMISE_CLASS_v0_1.md"),
        "executor": "Claude Code (Fable 5)",
    },
    "r50_pin_block": {
        "output_manifest_sha256_on_disk": on_disk,
        "package_pin_note": "the R51 package pins the R50 manifest by prefix "
                            "c6a6917f... and full-hash-from-file rule; the "
                            "on-disk value above is the binding pin",
        "prefix_match_c6a6917f": on_disk.startswith("c6a6917f"),
        "commit_A_resolved": git("rev-parse", "09d446d"),
        "commit_B_resolved": git("rev-parse", "4fa6555"),
        "transitive": "R49/R48/R47 via the pinned chain of input locks",
    },
    "declarations": {
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "exact_arithmetic_only": True,
        "hash_hygiene_in_force": True,
        "zero_or_one_premise_round": True,
        "survivor_premise_stated_not_adopted": True,
        "no_physical_time_no_maturity_threshold_no_external_referent": True,
    },
    "frozen_candidate_class_sec_5": {
        "axes": {
            "G_gate": ["ADJ (gates the adjunction y={u,v}; condition on "
                       "BOTH parents)",
                       "REC (gates the RO-D record fired by a downstream "
                       "use; adjunction free)"],
            "T_token": ["V (the object's own standing vacuum token)",
                        "F (a forced A12 request derived from a record on "
                        "the object's lineage)"],
            "M_timing": ["S (same-step: token served at step k; no "
                         "persistent field)",
                         "P (persistent: token served at any step <= k; "
                         "requires a mark)"],
        },
        "candidates": ["ADJ-V-S", "ADJ-V-P", "ADJ-F-S", "ADJ-F-P",
                       "REC-V-S", "REC-V-P", "REC-F-S", "REC-F-P",
                       "B0 (CO1 alone; R50-degenerate control)"],
        "selector": "the frozen service realization sigma (uniform over "
                    "complete request-slot matchings, CD2R) - the only "
                    "source-defined random selector",
    },
    "frozen_criteria_sec_6": {
        "C1": "deadlock-freedom from genesis over every registered "
              "(Gamma, D0, m, H); smallest deadlock-free Gamma per candidate",
        "C2": "growth class from exact recurrence bounds "
              "(SUPER_EXPONENTIAL / EXPONENTIAL / POLYNOMIAL / LINEAR)",
        "C3": "ledger non-degeneracy: long-run P(S^V=0) not identically "
              "0/1; forced-inflow constant vs Gamma",
        "C4": "coherence lifetime > 1 achievable (exact witness, small Gamma)",
        "C5": "frozen-structure footprint; whether the R50 envelope "
              "survives verbatim",
        "C6": "count of new persistent fields",
        "C7": "parameters (must be 0)",
        "C8": "quotient dependence of the gate",
        "survivor_rule": "passes C1 on some registered Gamma range, not "
                         "SUPER_EXPONENTIAL under C2, passes C3 and C4, "
                         "C7 = 0; C1 scope restrictions reported as scope "
                         "with exact witness, not failure",
        "minimality_order": "(C5 footprint, C6 fields, C8 dependence) "
                            "lexicographic; select nothing beyond the "
                            "ordering",
    },
    "part1_selector_questions_frozen": ["S1 per-token service identity",
                                        "S2 vacuum-token semantics / V ~ X",
                                        "S3 RRP1 scope for vacuum tokens",
                                        "S4 genesis service",
                                        "S5 regionality under V ~ X"],
    "worktree_state_at_start": {
        "pre_existing_deltas": "36 unstaged deletions + 60 untracked paths "
                               "(DEU_voids + root .gitignore), unchanged "
                               "from prior rounds; none touch pinned roots",
        "frozen_root_modification_check_at_start": "CLEAN",
    },
}

out = PKG / "R51_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("R50 manifest prefix match:", lock["r50_pin_block"]["prefix_match_c6a6917f"])
print("commits:", lock["r50_pin_block"]["commit_A_resolved"][:12],
      lock["r50_pin_block"]["commit_B_resolved"][:12])
print("wrote", out.name, sha256_file(out))
