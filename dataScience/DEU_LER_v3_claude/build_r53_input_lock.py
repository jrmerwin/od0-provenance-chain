#!/usr/bin/env python3
"""Assemble R53_INPUT_LOCK.json (Commit A). All hashes computed in-process."""
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


on_disk = sha256_file(PKG / "R52_OUTPUT_MANIFEST.json")

lock = {
    "schema": "OD0_R53_INPUT_LOCK_V1",
    "campaign": "OD0-R53",
    "run_date": "2026-09-02",
    "package": {
        "path": "dataScience/DEU_LER_v3_claude/"
                "OD0_CLAUDE_CODE_PACKAGE_R53_COST_GROWTH_FILTRATION_v0_1.md",
        "sha256": sha256_file(
            PKG / "OD0_CLAUDE_CODE_PACKAGE_R53_COST_GROWTH_FILTRATION_v0_1.md"),
        "executor": "Claude Code (Fable 5)",
    },
    "r52_pin_block": {
        "output_manifest_sha256_on_disk": on_disk,
        "prefix_match_2203c9bc": on_disk.startswith("2203c9bc"),
        "commit_A_resolved": git("rev-parse", "44f2197"),
        "commit_B_resolved": git("rev-parse", "3e55670"),
        "transitive": "R51..R47 via the pinned chain of input locks",
    },
    "declarations": {
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "exact_arithmetic_for_theorems": True,
        "sampled_readouts_labeled_seeded_never_proof": True,
        "zero_new_premises": True,
        "no_numeric_thresholds_in_criteria": True,
        "conditional_stack": ["CO1", "RO1", "TG1", "V~X identification",
                              "SV-pool", "frozen local laws"],
        "hash_hygiene_in_force": True,
    },
    "r52_sec_4_1_carry_forward_verbatim": {
        "regions": "FIXED (inherited immutable prefix map - UEQ0: 'R is "
                   "the immutable structural prefix map'; effective single "
                   "active joint region at constructor level, since every "
                   "composite's closed ancestry contains both primitives)",
        "per_region_Gamma": "Gamma is per region (frozen per-region ledger "
                            "kernel)",
        "capacity_total": "CONSTANT (fixed region count x per-region "
                          "Gamma); NOT state-dependent - all Parts 2-3 "
                          "theorems run under the single constant-capacity "
                          "reading",
    },
    "frozen_filtration_criteria_sec_6": {
        "E0_free": "F + D <= Gamma (every token served every step); to "
                   "prove: exited permanently once D > Gamma (D "
                   "non-decreasing); exact exit-step distribution at each "
                   "registered point",
        "E1_congested": "D > Gamma; to prove forward-invariant",
        "renewal_decomposition": "within E1: drained (F=0) vs draining "
                                 "(F>0); burst steps (>=1 new object) vs "
                                 "quiet steps",
        "cost_strata": "strata of c_min(z+) relative to capacity by state "
                       "relations only ({c_min <= Gamma}, ...); prove "
                       "which are forward-invariant; report exactly if "
                       "{c_min <= Gamma} is empty at every registered "
                       "point",
        "asymptotic_regime": "late regime defined by the Part-2 growth "
                             "law, not a threshold; if no exact state "
                             "relation exists, state plainly that no "
                             "threshold-free basin beyond E1 exists and "
                             "maturity is the asymptotic law alone",
        "no_historical_labels": True,
    },
    "frozen_r54_comparison_protocol_sec_8": {
        "1_what_compared": "the derived regime sequence (E0 -> E1 -> "
            "renewal/asymptotic) and the derived monotone observables "
            "(|X|, shell fraction u, chain-multiplicity distribution, "
            "cycle-length growth) against the historical SEQUENCE of "
            "qualitative regimes and the historical observables they were "
            "reported on - sequence and monotonicity only, no numerical "
            "thresholds, no round-number alignment (historical rounds are "
            "policy indices; R49)",
        "2_pass_fail_declared_in_advance": "PASS if the historical "
            "sequence of regimes is a coarsening of the derived filtration "
            "order and each historical observable maps to a frozen "
            "R52/R53 observable with the same reported monotonicity; "
            "PARTIAL if the sequence matches but an observable does not; "
            "FAIL if the order is contradicted. Any mismatch is reported "
            "at equal prominence.",
        "3_what_may_not_happen": "no observable added, no criterion moved, "
            "no stratum renamed after opening",
        "frozen_at_commit_A": True,
    },
    "sampling_protocol_frozen": {
        "seed_scheme": "random.Random(1000000*Gamma + 10000*m + 100*H + "
                       "trajectory_index)",
        "trajectories_per_point": 50,
        "steps_per_trajectory": 10000,
        "checkpoints": [100, 1000, 3000, 10000],
        "scope_note": "trajectory count recorded before any readout "
                      "(exact-resource scope, uniform across points, "
                      "R51/R52 precedent); sensitivity variants at the "
                      "two deterministic rule points as in R52",
    },
    "worktree_state_at_start": {
        "pre_existing_deltas": "36 unstaged deletions + 60 untracked "
                               "paths (DEU_voids + root .gitignore), "
                               "unchanged; none touch pinned roots",
        "frozen_root_modification_check_at_start": "CLEAN",
    },
}

out = PKG / "R53_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("R52 manifest prefix match:", lock["r52_pin_block"]["prefix_match_2203c9bc"])
print("commits:", lock["r52_pin_block"]["commit_A_resolved"][:12],
      lock["r52_pin_block"]["commit_B_resolved"][:12])
print("wrote", out.name, sha256_file(out))
