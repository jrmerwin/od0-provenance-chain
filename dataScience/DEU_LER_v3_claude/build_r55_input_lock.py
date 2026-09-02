#!/usr/bin/env python3
"""Assemble R55_INPUT_LOCK.json (Commit A). All hashes computed in-process.
Also pins the newly supplied Run3_Dijet paper into H2 (bytes hashed only;
scientific_values_parsed = false; NOT opened)."""
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


stamp = json.loads((PKG / "R54_PROVENANCE_STAMP.json").read_text(encoding="utf-8"))
stamp_sha = sha256_file(PKG / "R54_PROVENANCE_STAMP.json")
manifest_on_disk = sha256_file(PKG / "R54_OUTPUT_MANIFEST.json")

dijet = PKG / "Run3_Dijet (2).pdf"
h2_pin = {
    "path": "dataScience/DEU_LER_v3_claude/Run3_Dijet (2).pdf",
    "bytes": dijet.stat().st_size,
    "sha256": sha256_file(dijet),
    "scientific_values_parsed": False,
    "status": "PINNED_SEALED - supplied by Jason 2026-09-02; hashed only, "
              "never opened; supplements the R48 H2 entry (the frozen R48 "
              "manifest itself is not modified); remains sealed until an "
              "H2 round opens it under a frozen protocol",
}

TARGETS = {
    "part1_frozen_support_sec_4_1": {
        "setting": "m < Gamma; tau a step with the process in E1, "
                   "D_tau = |X_tau| > Gamma; y = {u,v} a composite not in "
                   "X_tau with parents u, v in X_tau",
        "a": "Finite co-service: E[# steps k >= tau at which both u and v "
             "are vacuum-served] is finite, with an explicit bound "
             "depending only on (Gamma, D_tau).",
        "b": "Positive non-formation: P(y never forms | z+_tau) > 0, with "
             "an explicit lower bound depending only on (Gamma, D_tau).",
        "c": "Inclusion decay: P(y ever forms | z+_tau) <= phi(Gamma, "
             "D_tau) with phi -> 0 as D -> infinity; sharpest explicit "
             "phi the argument yields (target: phi = O(Gamma^2/D)).",
        "d": "Nondegenerate eventual support: for any fixed finite set M "
             "of composites, S_inf intersect M is a nondegenerate random "
             "variable whenever M contains an element unavailable or "
             "unformed at some E1 state; the registry set (173 objects) "
             "is a specific instance.",
    },
    "part2_termination_sec_5_1": {
        "a": "Supercritical termination: if m > Gamma + H, the number of "
             "bursts is finite almost surely: growth terminates at a "
             "finite random size.",
        "b": "Subcritical persistence (R53, carried): if m < Gamma, "
             "growth is unbounded a.s.; extend to m < Gamma + H under "
             "the relief conditions or state the exact gap.",
        "c": "Critical line: m = Gamma + H (and the band Gamma <= m <= "
             "Gamma + H if (b) does not extend): state precisely what is "
             "proven and what is open.",
    },
    "part3_rate_sec_6": "prove any exact upper bound |X_k| <= C*k^beta "
                        "with beta < 1 and any lower bound |X_k| >= "
                        "c*k^alpha with alpha > 0, for m < Gamma; if "
                        "neither is obtainable, record the precise "
                        "obstruction and stop",
    "note": "targets frozen verbatim; the run proves, refutes, or scopes "
            "them; the Section 4.2 proof route is guidance, not a frozen "
            "statement",
}

lock = {
    "schema": "OD0_R55_INPUT_LOCK_V1",
    "campaign": "OD0-R55",
    "run_date": "2026-09-02",
    "package": {
        "path": "dataScience/DEU_LER_v3_claude/"
                "OD0_CLAUDE_CODE_PACKAGE_R55_LATE_REGIME_THEOREMS_v0_1.md",
        "sha256": sha256_file(
            PKG / "OD0_CLAUDE_CODE_PACKAGE_R55_LATE_REGIME_THEOREMS_v0_1.md"),
        "executor": "Claude Code (Fable 5)",
    },
    "r54_pin_block": {
        "stamp_sha256": stamp_sha,
        "stamp_commit_B": stamp["commit_B_resolved"],
        "manifest_sha256_in_stamp": stamp["output_manifest_sha256"],
        "manifest_sha256_on_disk": manifest_on_disk,
        "match": manifest_on_disk == stamp["output_manifest_sha256"],
    },
    "h1_status": "SPENT - nothing may be validated against H1 again",
    "h2_supplement_pin": h2_pin,
    "sentinels_h2_h5": {t: "parsed=false" for t in
                        ("H2", "H3", "H4", "H5")},
    "frozen_theorem_targets": TARGETS,
    "registry_readout_scope": {
        "trajectories_per_point": 5,
        "steps": 10000,
        "checkpoints": [100, 1000, 10000],
        "seed_scheme": "random.Random(1000000*Gamma + 10000*m + 100*H + t)",
        "note": "recorded before any readout; uniform across all 144 "
                "registered points; objects tracked with exact recursive "
                "identity for registry membership (R50 arrow)",
    },
    "declarations": {
        "BELL2_opened": False,
        "zero_new_premises": True,
        "no_thresholds_no_external_referents": True,
        "hash_hygiene_in_force": True,
        "h1_provenance_of_questions_disclosed": "the support-locking "
            "stage of H1 prompted target 1; the theorems use no "
            "historical content",
    },
    "worktree_state_at_start": {
        "pre_existing_deltas": "36 unstaged deletions + 60 untracked "
                               "paths (DEU_voids + root .gitignore), "
                               "unchanged; none touch pinned roots",
        "frozen_root_modification_check_at_start": "CLEAN",
    },
}

out = PKG / "R55_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("R54 stamp/manifest match:", lock["r54_pin_block"]["match"])
print("H2 dijet pinned:", h2_pin["sha256"][:16], h2_pin["bytes"], "bytes")
print("wrote", out.name, sha256_file(out))
