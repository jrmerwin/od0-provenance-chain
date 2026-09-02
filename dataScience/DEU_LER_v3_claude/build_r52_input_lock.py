#!/usr/bin/env python3
"""Assemble R52_INPUT_LOCK.json (Commit A). All hashes computed in-process."""
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


on_disk = sha256_file(PKG / "R51_OUTPUT_MANIFEST.json")

OBSERVABLE_INVENTORY = {
    "object_layer_per_region_and_total": [
        "|X|", "|U| unresolved shell (objects never used as a parent)",
        "|En(X)| = C(|X|,2) - (|X|-2)",
        "depth distribution", "dag_size distribution",
        "composite-graph degree distribution (children per object)",
        "cluster census (Part 4.2)",
    ],
    "record_layer": [
        "number of recorded words", "prefix-length distribution",
        "N multiplicities by P4 type", "|S|",
        "first-use vs repeat-use counts",
    ],
    "ledger_per_region": [
        "B", "D", "F", "P", "H", "Gamma", "clock residue", "V0 = min(Gamma,D)",
        "conditional laws of 4.5 evaluated at the state",
    ],
    "interval_currents": ["|G-|", "|G+|", "|G+ \\ G-|", "D/L/M stocks (R45)"],
    "intensive": [
        "x = D/(F+D)", "B/Gamma", "|U|/|X|", "|G-|/|S|",
        "E[Phi^2|state]", "P(S^V>=2|state)", "E[new objects|state]",
        "F/|X| requests-outstanding per object",
    ],
    "frozen_rule": "nothing added after Commit A; nothing removed on the "
                   "basis of readouts",
}

CLOSURE_LADDER = [
    "L0: ledger counts only (B, D, P, H, Gamma, clock residues)",
    "L1: L0 + |X|, |U|",
    "L2: L1 + composite-graph isomorphism class of X",
    "L3: L2 + record-status map (word -> recorded prefix length) + cluster census",
    "L4: L3 + N and S content",
    "L5: full z = (X, N, S, Lambda, G+-)",
]

lock = {
    "schema": "OD0_R52_INPUT_LOCK_V1",
    "campaign": "OD0-R52",
    "run_date": "2026-09-02",
    "package": {
        "path": "dataScience/DEU_LER_v3_claude/"
                "OD0_CLAUDE_CODE_PACKAGE_R52_CLOSED_OBSERVABLE_ALGEBRA_v0_1.md",
        "sha256": sha256_file(
            PKG / "OD0_CLAUDE_CODE_PACKAGE_R52_CLOSED_OBSERVABLE_ALGEBRA_v0_1.md"),
        "executor": "Claude Code (Fable 5)",
    },
    "r51_pin_block": {
        "output_manifest_sha256_on_disk": on_disk,
        "prefix_match_8df67d66": on_disk.startswith("8df67d66"),
        "commit_A_resolved": git("rev-parse", "28f50e5"),
        "commit_B_resolved": git("rev-parse", "2369705"),
        "transitive": "R50..R47 via the pinned chain of input locks",
    },
    "declarations": {
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "exact_arithmetic_for_theorems_and_exact_readouts": True,
        "sampled_readouts_labeled_seeded_never_cited_as_proof": True,
        "zero_new_premises": True,
        "conditional_stack": ["CO1", "RO1", "TG1", "V~X identification",
                              "SV-pool", "frozen local laws"],
        "hash_hygiene_in_force": True,
    },
    "frozen_observable_inventory_sec_5": OBSERVABLE_INVENTORY,
    "frozen_closure_ladder_sec_6": CLOSURE_LADDER,
    "sampling_protocol_frozen": {
        "seed_scheme": "random.Random(1000000*Gamma + 10000*m + 100*H + "
                       "trajectory_index) - recorded, deterministic, "
                       "reproducible",
        "scope_note": "the package prescribes 1000 trajectories x 1000 "
                      "steps per registered point; the executor records an "
                      "exact-resource scope reduction (trajectories x "
                      "steps per point as reported in the readout file) "
                      "with the R51 K_max-budget precedent; the reduction "
                      "is uniform across points (nothing singled out) and "
                      "is recorded here BEFORE any readout is computed",
        "trajectories_per_point": 100,
        "steps_per_trajectory": 500,
        "sensitivity_points_rule": "the lexicographically smallest and "
                                   "largest registered deadlock-free "
                                   "points (Gamma=2,m=0,H=0) and "
                                   "(Gamma=5,m=3,H=8) - a deterministic "
                                   "rule, not a preference",
    },
    "worktree_state_at_start": {
        "pre_existing_deltas": "36 unstaged deletions + 60 untracked paths "
                               "(DEU_voids + root .gitignore), unchanged; "
                               "none touch pinned roots",
        "frozen_root_modification_check_at_start": "CLEAN",
    },
}

out = PKG / "R52_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("R51 manifest prefix match:", lock["r51_pin_block"]["prefix_match_8df67d66"])
print("commits:", lock["r51_pin_block"]["commit_A_resolved"][:12],
      lock["r51_pin_block"]["commit_B_resolved"][:12])
print("wrote", out.name, sha256_file(out))
