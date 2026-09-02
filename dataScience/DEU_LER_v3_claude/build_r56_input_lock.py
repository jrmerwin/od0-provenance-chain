#!/usr/bin/env python3
"""Assemble R56_INPUT_LOCK.json + the sealed R56_H2_PREREGISTRATION.json
(Commit A). All hashes computed in-process. H2 PDF re-verified untouched."""
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


stamp = json.loads((PKG / "R55_PROVENANCE_STAMP.json").read_text(encoding="utf-8"))
r55_lock = json.loads((PKG / "R55_INPUT_LOCK.json").read_text(encoding="utf-8"))
dijet_now = sha256_file(PKG / "Run3_Dijet (2).pdf")
dijet_pin = r55_lock["h2_supplement_pin"]["sha256"]

OBSERVABLES = [
    {"id": "O1_containment",
     "definition": "containment(w) = #{o in X : w in closed_anc(o), o != w}",
     "h1_provenance": "H1 exposure/containment counts (dag_time.ipynb)",
     "class": "THEOREM: nondecreasing (objects never destroyed; ancestry "
              "fixed at formation)"},
    {"id": "O2_coembedding",
     "definition": "coembedding(w1,w2) = #{o in X : {w1,w2} subset "
                   "closed_anc(o)}",
     "h1_provenance": "H1 pair co-embedding", "class": "THEOREM: "
     "nondecreasing"},
    {"id": "O3_support_size",
     "definition": "support(M) = |X intersect M| for a fixed reference set "
                   "M (default: the 173 registry objects; also per grade)",
     "h1_provenance": "H1 support size on the spatial 81",
     "class": "THEOREM: nondecreasing; eventually frozen with positive "
              "probability per grade (R55)"},
    {"id": "O4_participation_ratio",
     "definition": "PR = (sum_w c_w)^2 / sum_w c_w^2 over containment "
                   "weights c_w",
     "h1_provenance": "H1 participation ratio", "class": "READOUT"},
    {"id": "O5_concentration_backbone",
     "definition": "backbone_q = {w : through(w) >= q-quantile}, "
                   "through(w) = total chains of descendants of w passing "
                   "through w; q = 0.95 as the HISTORICAL convention, "
                   "disclosed",
     "h1_provenance": "H1 weighted K9 backbone", "class": "READOUT"},
    {"id": "O6_dilution",
     "definition": "dilution = #{o : dag_size(o) <= 7}/|X|",
     "h1_provenance": "H1 global dilution 81/|V_d|",
     "class": "THEOREM: -> 0 as |X| -> infinity (numerator <= 173); "
              "stepwise monotonicity NONE"},
    {"id": "O7_clocks",
     "definition": "containment clock = log-compressed total containment; "
                   "co-embedding clock = log-compressed total "
                   "co-embedding, in the verbatim historical functional "
                   "forms of R54_H1_EXTRACTION (tau ~ log log of the "
                   "respective totals)",
     "h1_provenance": "H1 clock candidates",
     "class": "inherits THEOREM monotonicity from O1/O2"},
    {"id": "O8_diameter",
     "definition": "diameter of the parent-child composite graph on X",
     "h1_provenance": "H1 diameter invariance",
     "class": "NONE proven: adding objects adds vertices at distance via "
              "parents and can also CREATE shortcuts, so neither "
              "monotonicity direction is a theorem; classified NONE with "
              "the exact reason; readout only"},
    {"id": "O9_early_layer_count",
     "definition": "#{o in X : dag_size(o) <= 7}",
     "h1_provenance": "numerator of O6",
     "class": "THEOREM: nondecreasing, bounded by 173"},
]

PREDICTIONS = [
    {"id": "P1", "statement": "Monotone availability: any fixed structure, "
     "once realized, remains; availability nondecreasing in process time.",
     "class": "THEOREM (weak; completeness)"},
    {"id": "P2", "statement": "Inclusion decay: a fixed structure available "
     "at universe size D is realized with probability <= phi ~ 1/(D-1); "
     "earlier-available structures realize with higher probability bound.",
     "class": "THEOREM (bound; R55 phi)"},
    {"id": "P3", "statement": "Freeze order: lower grades freeze before "
     "higher grades; P(a grade's realized set still changes after a given "
     "process time) decreases with the grade's availability size.",
     "class": "THEOREM (bound) / READOUT (observed order at Gamma <= 5)"},
    {"id": "P4", "statement": "Configuration ordering: structures requiring "
     "k same-step co-served tokens are reachable only for Gamma >= k; "
     "families ordered by minimal configuration become reachable in that "
     "order as capacity rises; above-threshold families never appear at "
     "fixed Gamma.", "class": "THEOREM (established in R56 Part 4)"},
    {"id": "P5", "statement": "Frozen-random subset: independent "
     "realizations at equal parameters realize different eventual "
     "supports; presence of late-available structures varies across runs.",
     "class": "THEOREM; testable against H2 only if it reports multiple "
              "independent substrates at equal age, else N/A"},
    {"id": "P6", "statement": "Cost-ordered persistence: larger "
     "chain-multiplicity structures impose larger rendering cost when "
     "built upon and are, per unit availability, realized later.",
     "class": "THEOREM (cost law) / READOUT (ordering)"},
]

PROTOCOL = {
    "compared": "only H2 patterns invariant under monotone "
        "reparametrization of rounds - orderings of family emergence, "
        "monotonicity of availability, freezing/saturation, dependence on "
        "substrate capacity or family complexity, cross-substrate "
        "variability if reported - against P1-P6 and O1-O9, mapped BY "
        "DEFINITION at opening (names, words, counts are not maps); "
        "'strain'/'channel' map only if their extracted definitions "
        "coincide with a frozen function on z+, else "
        "UNMAPPED_COMPUTABLE/UNMAPPED_INAPPLICABLE",
    "rule": "PASS iff every mapped reparametrization-invariant H2 pattern "
        "is consistent with the corresponding THEOREM-grade prediction "
        "and none contradicts one; PARTIAL if consistent but a "
        "stage-defining H2 observable is unmapped or matches only at "
        "READOUT grade; FAIL if a THEOREM-grade prediction is "
        "contradicted by a reparametrization-invariant pattern; "
        "mismatches at equal prominence",
    "forbidden": "round-number alignment; rate comparison; any prediction "
        "added, criterion moved, or observable renamed after opening; any "
        "repair of the tower in the opening round",
    "model_family_caveat": "the H2 engine's opportunity law and substrate "
        "(R48 census + sealed repository commit) are stated at opening; "
        "mismatches may reflect them",
}

prereg = {
    "schema": "R56_H2_PREREGISTRATION_V1",
    "run_date": "2026-09-02",
    "frozen_at_commit_A": True,
    "h2_sealed_target": {"path": "Run3_Dijet (2).pdf",
                         "sha256": dijet_now,
                         "matches_r55_pin": dijet_now == dijet_pin,
                         "opened": False},
    "observables": OBSERVABLES,
    "prediction_set": PREDICTIONS,
    "protocol": PROTOCOL,
    "h1_status": "SPENT (provenance disclosure only)",
}
(PKG / "R56_H2_PREREGISTRATION.json").write_text(
    json.dumps(prereg, indent=2, sort_keys=True) + "\n",
    encoding="utf-8", newline="\n")
prereg_sha = sha256_file(PKG / "R56_H2_PREREGISTRATION.json")

lock = {
    "schema": "OD0_R56_INPUT_LOCK_V1",
    "campaign": "OD0-R56",
    "run_date": "2026-09-02",
    "package": {
        "path": "dataScience/DEU_LER_v3_claude/"
                "OD0_CLAUDE_CODE_PACKAGE_R56_H2_PREREG_AND_M5_OPENING_v0_1.md",
        "sha256": sha256_file(
            PKG / "OD0_CLAUDE_CODE_PACKAGE_R56_H2_PREREG_AND_M5_OPENING_v0_1.md"),
        "executor": "Claude Code (Fable 5)",
    },
    "r55_pin_block": {
        "stamp_sha256": sha256_file(PKG / "R55_PROVENANCE_STAMP.json"),
        "commit_B_resolved": stamp["commit_B_resolved"],
        "manifest_sha256_in_stamp": stamp["output_manifest_sha256"],
        "manifest_sha256_on_disk": sha256_file(PKG / "R55_OUTPUT_MANIFEST.json"),
        "match": sha256_file(PKG / "R55_OUTPUT_MANIFEST.json")
                 == stamp["output_manifest_sha256"],
    },
    "h2_pdf_reverified": {"sha256_now": dijet_now,
                          "matches_r55_pin": dijet_now == dijet_pin,
                          "untouched_and_sealed": True},
    "sentinels_h2_h5": {t: "parsed=false" for t in ("H2", "H3", "H4", "H5")},
    "h2_preregistration": {"path": "R56_H2_PREREGISTRATION.json",
                           "sha256": prereg_sha},
    "declarations": {
        "BELL2_opened": False,
        "zero_new_premises": True,
        "h2_not_opened_this_round": True,
        "no_particle_collision_or_physical_claim": True,
        "hash_hygiene_in_force": True,
    },
    "m5_readout_scope": {
        "trajectories_per_point": 3, "steps": 10000,
        "seed_scheme": "random.Random(1000000*Gamma + 10000*m + 100*H + t)",
        "note": "recorded before any readout; uniform across points",
    },
    "worktree_state_at_start": {
        "pre_existing_deltas": "36 unstaged deletions + 60 untracked "
                               "paths (DEU_voids + root .gitignore), "
                               "unchanged; none touch pinned roots",
        "frozen_root_modification_check_at_start": "CLEAN",
    },
}
(PKG / "R56_INPUT_LOCK.json").write_text(
    json.dumps(lock, indent=2, sort_keys=True) + "\n",
    encoding="utf-8", newline="\n")
print("R55 pin match:", lock["r55_pin_block"]["match"])
print("H2 PDF untouched:", dijet_now == dijet_pin)
print("prereg sha:", prereg_sha)
print("wrote lock", sha256_file(PKG / "R56_INPUT_LOCK.json"))
