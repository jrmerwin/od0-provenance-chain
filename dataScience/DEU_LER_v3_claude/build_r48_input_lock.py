#!/usr/bin/env python3
"""Assemble R48_INPUT_LOCK.json (Commit A preregistration record).

Pulls verified hashes from R48_CHAIN_VERIFICATION.json; records the R47 pin
block and its on-disk verification, the Section-3 frozen prior inputs, the
source-root list (verbatim supply + recorded interpretation), the frozen
GM/LG/CCE criteria reference, and the worktree state at start.
"""
import json
import hashlib
import subprocess
from pathlib import Path

PKG = Path(__file__).resolve().parent

chain = json.loads((PKG / "R48_CHAIN_VERIFICATION.json").read_text(encoding="utf-8"))
files = {f["path"].replace("\\", "/").split("/")[-1]: f
         for f in chain["package"]["files"]}

head = subprocess.run(["git", "rev-parse", "HEAD"],
                      capture_output=True, text=True, cwd=PKG).stdout.strip()
branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                        capture_output=True, text=True, cwd=PKG).stdout.strip()

lock = {
    "schema": "OD0_R48_INPUT_LOCK_V1",
    "campaign": "OD0-R48",
    "package": {
        "path": "dataScience/DEU_LER_v3_claude/"
                "OD0_CLAUDE_CODE_PACKAGE_R48_MATURATION_SOURCE_BOUNDARY_v0_2.md",
        "sha256": files["OD0_CLAUDE_CODE_PACKAGE_R48_MATURATION_SOURCE_BOUNDARY_v0_2.md"]["sha256"],
        "bytes": files["OD0_CLAUDE_CODE_PACKAGE_R48_MATURATION_SOURCE_BOUNDARY_v0_2.md"]["bytes"],
        "executor": "Claude Code (Fable 5)",
    },
    "r47_pin_block": {
        "result_digest_pin":
            "382a2cc975a194a1ef45b7aabd553d732811f084120bab3b1fafd7834e6c5c14",
        "output_manifest_sha256_pin":
            "d4eeb49ea1274619eca5ff99182b61e54a7e46aadce075593ba0279585d62fbb",
        "execution_commit_pin":
            "2b7ae30fe23b0ccffe31f2ffbba6ae2de2318a21",
        "on_disk_verification": {
            "manifest_path": chain["r47_top_pins"]["manifest_path"],
            "manifest_sha256_match": chain["r47_top_pins"]["manifest_match"],
            "result_digest_match": chain["r47_top_pins"]["result_digest_match"],
            "execution_commit_locally_resolvable": False,
            "execution_commit_note": (
                "The pinned commit is not an object in the local "
                "home-directory repository; the R30-R47 chain was executed in "
                "a separate (Codex) environment and its git objects were not "
                "transferred. Reachability of every inherited artifact is "
                "instead established by the on-disk hash chain recorded in "
                "R48_CHAIN_VERIFICATION.json (R47->R30, all links VERIFIED)."),
            "chain_walk_status": chain["status"],
            "chain_walk_artifact":
                "dataScience/DEU_LER_v3_claude/R48_CHAIN_VERIFICATION.json",
        },
    },
    "frozen_prior_inputs": {
        "R30_no_opportunity": {
            "artifact_root": "dataScience/DEU_LER_v2_codex/"
                             "deu_od0_exact_observables_v0_1/"
                             "od0_r30_outer_policy_audit_v0_1",
            "reachable_through_pinned_chain": True,
            "role": ("GM4 answer for family F0: no active source supplies "
                     "occurrence opportunity, control selection, physical "
                     "timing, or next-record lifecycle for the OD0 family."),
        },
        "CD0_constructor_category": {
            "artifact_root": "dataScience/DEU_LER_v0_1_Codex_Package/"
                             "deu_ler_v0_1/deu_unified_equations_v1_0/"
                             "deu_combinatorial_descent_cd0",
            "file_pins": ("39 files hash-pinned in "
                          "R48_CHAIN_VERIFICATION.json (cd0 section)"),
            "role": ("ancestry-closed construction states; legal adjunction "
                     "events with exact independence diamond; one trace class "
                     "per comparable state pair; genesis state = primitives "
                     "{a,b}. Settles GM1-GM3 candidacy for F1 up to "
                     "persistence and closure checks."),
        },
        "descent_paper_ledgers": {
            "MODEL_GENEALOGY.md": {
                "sha256": files["MODEL_GENEALOGY.md"]["sha256"],
                "bytes": files["MODEL_GENEALOGY.md"]["bytes"]},
            "MISSING_PROVENANCE.md": {
                "sha256": files["MISSING_PROVENANCE.md"]["sha256"],
                "bytes": files["MISSING_PROVENANCE.md"]["bytes"]},
            "role": ("census starting inventory; R48 verifies and formalizes "
                     "their family list."),
        },
        "R47_boundary": {
            "role": ("event-local coproduct source category; zero "
                     "cross-occurrence and cross-factor source arrows; CCP1 "
                     "conditional and not source-derived."),
            "mandatory_reproduction_facts_asserted": {
                "dependency_quiver_objects_arrows": [356, 448],
                "Q_cons": "Z^844",
                "P4_histories": 2304,
                "service_templates": 41472,
                "CCP1_winner": ("K2 exact-semantic sparse continuation; "
                                "carrier labels 356, ranks 178/178"),
                "absent_ranks": ("no carrier stage; cross-anchor repair "
                                 "forbidden; no strict connection; "
                                 "no holonomy"),
            },
        },
        "codex_r48_to_r53_outputs_not_used": (
            "Directories od0_r48_* .. od0_r53_* exist in the v2_codex tree "
            "from the Codex line. They are NOT among the Section-3 frozen "
            "inputs of this v0.2 package; their verdicts and contents are "
            "not read in this run. They are hash-pinned in the census as "
            "artifacts only."),
    },
    "supporting_manuscripts_hash_pinned_not_committed": [
        {"path": "dataScience/DEU_LER_v3_claude/unified_deu_eq.pdf",
         "sha256": files["unified_deu_eq.pdf"]["sha256"],
         "bytes": files["unified_deu_eq.pdf"]["bytes"],
         "access_rule": ("headings/structure only; no numerical maturation "
                         "content parsed")},
        {"path": "dataScience/DEU_LER_v3_claude/unified_deu_eq (1).pdf",
         "sha256": files["unified_deu_eq (1).pdf"]["sha256"],
         "bytes": files["unified_deu_eq (1).pdf"]["bytes"],
         "access_rule": ("headings/structure only; no numerical maturation "
                         "content parsed")},
    ],
    "source_roots": {
        "supplied_by_jason_verbatim": (
            "Please work exclusively inside the directory DEU_LER_v3_claude. "
            "In there you will find supporting materials and the current "
            "package R48 that you are to follow and execute the "
            "instructions. If any files are missing let me know and I will "
            "find them for you."),
        "recorded_interpretation": (
            "Write scope is exclusively dataScience/DEU_LER_v3_claude (all "
            "outputs, scripts, and both commits). The package Section-1 lock "
            "verification and Section-6 census require read-only access to "
            "the pinned chain and the historical source roots, which live in "
            "sibling directories; these are enumerated below, opened "
            "read-only, and never modified."),
        "read_write_root": "dataScience/DEU_LER_v3_claude",
        "read_only_census_root_rule": (
            "every top-level directory of dataScience matching DEU_* / "
            "deu_* / RMR_* (case-insensitive), plus "
            "four_forces_simulation_reference, derivation_table, "
            "simulation_meets_derivations, unified_solution_audit, "
            "ringdown_pdf_text, and the loose file GR_QM.pdf; deduplicated "
            "by resolved path"),
        "read_only_census_roots": sorted([
            "DEU_LER_v0_1_Codex_Package", "DEU_LER_v2_codex", "DEU_LHC3",
            "DEU_SR", "DEU_bridge", "DEU_holo",
            "DEU_holo_full_mac_transfer", "DEU_unification", "DEU_voids",
            "RMR_137_sim", "RMR_DEU", "RMR_GR", "RMR_G_const",
            "RMR_applications", "RMR_doomsday", "RMR_logical_seed",
            "RMR_masses", "RMR_origin_and_fate", "RMR_signal_pairs",
            "RMR_utility", "RMR_willow", "deu_equations",
            "four_forces_simulation_reference", "derivation_table",
            "simulation_meets_derivations", "unified_solution_audit",
            "ringdown_pdf_text", "GR_QM.pdf",
        ]),
    },
    "criteria_frozen": {
        "GM": "GM1-GM12 exactly as Section 5.2 of the committed package",
        "LG": "LG1-LG12 exactly as Section 7 of the committed package",
        "CCE": "CCE1-CCE5 exactly as Section 9 of the committed package",
        "map_classification": ("Section 5.3 seven-way classification, "
                               "exactly one per proposed map"),
        "verdict_tree": "Section 14 of the committed package",
        "frozen_by": "package sha256 above; committed verbatim in Commit A",
    },
    "declarations": {
        "new_premises": 0,
        "historical_numerical_content_parsed": False,
        "BELL2_scientific_content_opened": False,
        "BELL2_location_sealed": (
            "dataScience/DEU_LER_v2_codex/"
            "DEU_BELL2_Final_and_Math_First_Transition_Package_v0_2 "
            "(directory recorded; contents not opened)"),
        "no_policy_time_gravity_threshold_particle_or_age_selected": True,
        "adjudicator_registered_prediction": (
            "committed verbatim inside the package file; constrains nothing"),
    },
    "worktree_state_at_start": {
        "repository_root": ("C:/Users/merwijas (home-directory repo; only "
                            "dataScience/DEU_voids is tracked; dataScience/* "
                            "otherwise gitignored)"),
        "HEAD": head,
        "branch": branch,
        "pre_existing_deltas": (
            "36 unstaged deletions + 59 untracked paths, all confined to "
            "dataScience/DEU_voids, plus one untracked root .gitignore; none "
            "touch the pinned chain roots (DEU_LER_v2_codex, "
            "DEU_LER_v0_1_Codex_Package) or any RMR/DEU census root"),
        "frozen_root_modification_check_at_start":
            "CLEAN under all pinned and census roots",
    },
}

out = PKG / "R48_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("wrote", out.name, hashlib.sha256(out.read_bytes()).hexdigest())
