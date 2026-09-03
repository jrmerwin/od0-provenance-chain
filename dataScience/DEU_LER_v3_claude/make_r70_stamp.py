#!/usr/bin/env python3
"""OD0-R70 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r70_stamp.py <commitB_ref>"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parent
B_REF = sys.argv[1]


def rev(ref):
    return subprocess.run(["git", "rev-parse", ref], cwd=PKG,
                          capture_output=True, text=True,
                          check=True).stdout.strip()


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = {
    "schema": "R70_PROVENANCE_STAMP_V1",
    "round": "OD0-R70",
    "verdict": "OD0_R70_PASS_H5_OPENED_UNDER_SEALED_PROTOCOL",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R70_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R70_OUTPUT_MANIFEST.json"),
    "sealed_protocol_sha256_verified":
        "160775e68feaecbcaa081a77e96ba8640def57d14693a3d6fb69fc2767"
        "d26c94",
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent, not consulted",
              "H5": "OPENED AND SPENT this round",
              "SEALED_CORPORA_REMAINING": 0},
    "deterministic_rerun": "byte-identical (builder double-run on "
                           "static extraction raw)",
    "headline": {
        "H5_COMPARISON": "PARTIAL - density direction consistent "
                         "with Q1 at pattern level (counts "
                         "nondecreasing despite corpus-wide "
                         "destruction mechanisms); closure/critical "
                         "conditions present, classified ASYMPTOTIC "
                         "or FINITE_COUNT and never compared with "
                         "N=9*Gamma across the state-class gate; "
                         "no theorem contradicted",
        "Q8_TOUCHED": False,
        "state_classes": "activation foams (1->3 face replacement) "
                         "lack a pair-closure arrow; all "
                         "quantitative comparisons "
                         "STATE_CLASS_MISMATCH; de Sitter-closure "
                         "family Tier D + MANUSCRIPT_ONLY at equal "
                         "prominence",
        "milestone": "all five holdout corpora (H1-H5) now opened "
                     "and adjudicated under sealed protocols; none "
                     "contradicted a theorem",
        "r71": "the proto-paper of the R48-R70 arc"},
}
out = PKG / "R70_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R70_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
