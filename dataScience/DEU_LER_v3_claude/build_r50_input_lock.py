#!/usr/bin/env python3
"""Assemble R50_INPUT_LOCK.json (Commit A preregistration record).

Hash hygiene (R50 Section 1, permanent): every hash in this lock is computed
by this script at the moment of recording (hashlib for files, git rev-parse
for commits). No hash is typed, expanded, or reconstructed by hand.
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


R49_MANIFEST_PIN = "53002a42f0a253b8d05f32cac196e3fa3d3dee7ab5ecd99925066e223a33486a"

lock = {
    "schema": "OD0_R50_INPUT_LOCK_V1",
    "campaign": "OD0-R50",
    "run_date": "2026-09-02",
    "package": {
        "path": "dataScience/DEU_LER_v3_claude/"
                "OD0_CLAUDE_CODE_PACKAGE_R50_BUNDLING_ENVELOPE_AND_SATURATION_v0_1.md",
        "sha256": sha256_file(
            PKG / "OD0_CLAUDE_CODE_PACKAGE_R50_BUNDLING_ENVELOPE_AND_SATURATION_v0_1.md"),
        "executor": "Claude Code (Fable 5)",
    },
    "hash_hygiene": {
        "rule": "permanent from R50 on: no hash typed, expanded, or "
                "reconstructed by hand; commit hashes only from git "
                "rev-parse output, file hashes only from sha256 tool "
                "output, captured programmatically at recording time",
        "this_lock_compliant": True,
        "generator": "build_r50_input_lock.py (all values computed in-process)",
    },
    "r49_pin_block": {
        "output_manifest_sha256_pin": R49_MANIFEST_PIN,
        "output_manifest_sha256_on_disk": sha256_file(PKG / "R49_OUTPUT_MANIFEST.json"),
        "commit_A_resolved": git("rev-parse", "4946e4e"),
        "commit_B_resolved": git("rev-parse", "2feccb7"),
        "r48_r47_transitive": "via R49_INPUT_LOCK.json (pinned in the R49 "
                              "manifest) -> R48 manifest -> "
                              "R48_CHAIN_VERIFICATION.json -> R47..R30",
    },
    "declarations": {
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "exact_arithmetic_only": True,
        "zero_premise_round": True,
        "carried_declared_conditionals": ["CO1", "RO1", "SV-pool"],
        "no_member_selected": True,
        "no_throttle_capacity_law_time_or_threshold_selected": True,
    },
    "frozen_layer_list_sec_4_2": [
        "L1 object layer - universal DAG and ancestry order",
        "L2 record poset - RO-D record events with induced causal order",
        "L3 record outcome law at fixed settings - diagonality/commutation",
        "L4 settings - A13R clock state; locate the quotient-dependence entry chain",
        "L5 request layer - per-record A12 multiset vs per-step pool",
        "L6 ledger - per-step conservation vs cumulative horizon quantities",
        "L7 marks and interval G+- - realization dependence vs support/envelope",
        "L8 coherence lifetime - formation-to-full-record step count; general theorem",
    ],
    "frozen_layer_classes": ["INVARIANT_ALL_QUOTIENTS",
                             "INVARIANT_CANONICAL_PAIR",
                             "QUOTIENT_DEPENDENT"],
    "frozen_ledger_scan_design_sec_6_3": {
        "lambda0_status": "UNDECLARED_IN_SOURCE (R49); therefore scan, do not choose",
        "scan_domain": "genesis parameters (Gamma, D, m, H) over the COMPLETE "
                       "registered CD2R/UEQ0 catalog domain - every "
                       "registered value, none singled out",
        "reported_per_point": ["smallest k with F_k > Gamma",
                               "P(S^V_k = 0) exactly for each k <= K_max",
                               "backlog B_k", "lapse Phi_k distribution",
                               "direct-limit clock increments"],
        "both_members": True,
        "K_max": 3,
        "kappa_is_readout_not_threshold": True,
    },
    "frozen_part4_candidate_list_sec_7": {
        "classified_quantities": ["Gamma (capacity)", "D (vacuum demand)",
                                  "m (persistent load)", "H (relief candidates)"],
        "classes": ["EXTERNAL_CONSTANT", "STATE_FUNCTION(formula, source file)",
                    "UNDECLARED"],
        "sources_scanned": ["UEQ0", "CD2R finite-set representation", "A13R",
                            "R40-R45"],
        "questions": [
            "does any active source define Gamma or D as a function of "
            "rendered structure (marks, G+-, |X|, served history)?",
            "does any active source gate adjunction enablement on "
            "realization (Par(y) subset rendered set rather than subset X)?",
        ],
        "minimal_throttle_premise_class_recorded_not_selected": [
            "RG1 rendered-parent gating (with the premise-invariant "
            "G-/G+ envelope from R44 giving lower/upper enabled sets)",
            "state-scaled Gamma", "state-scaled D",
        ],
    },
    "frozen_inputs_cited": [
        "CD0 (constructor, Thm 1)", "CD1I (append, prefix records, clock tower)",
        "CD2R (A12 additivity, finite-set ledger representation, "
        "service-equivalence premise, hypergeometric kernel, "
        "population/relief rules)",
        "A13R (scale-natural clock action)",
        "UEQ0 (master transition, ledger updates, lapse)",
        "R40-R45 (service composition, RRP1 marks, interval, currents)",
        "R49 (RO-D record law + D<=3 certificates; SV-pool; T_sat/T_dag "
        "classification and witnesses)",
    ],
    "worktree_state_at_start": {
        "pre_existing_deltas": "36 unstaged deletions + 60 untracked paths "
                               "(59 DEU_voids + root .gitignore), unchanged "
                               "from R48/R49 start/end states; none touch "
                               "pinned roots",
        "frozen_root_modification_check_at_start": "CLEAN",
    },
}

out = PKG / "R50_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("R49 manifest match:",
      lock["r49_pin_block"]["output_manifest_sha256_on_disk"] == R49_MANIFEST_PIN)
print("commit A:", lock["r49_pin_block"]["commit_A_resolved"])
print("commit B:", lock["r49_pin_block"]["commit_B_resolved"])
print("wrote", out.name, sha256_file(out))
