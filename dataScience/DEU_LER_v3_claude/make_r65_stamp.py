#!/usr/bin/env python3
"""OD0-R65 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r65_stamp.py <commitB_ref>"""
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
    "schema": "R65_PROVENANCE_STAMP_V1",
    "round": "OD0-R65",
    "verdict": "OD0_R65_PASS_BRANCH_C_DERIVED",
    "primary": "BRANCH_C = RECORD_SPACE_EXPONENT(delta = 1)",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R65_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R65_OUTPUT_MANIFEST.json"),
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder "
                           "double-run)",
    "headline": {
        "record_space": "ONE exact ultrametric tree (equal symbols "
                        "identified at source; 7.97M triples, zero "
                        "violations); READABLE_FROM_S",
        "exponent": "delta = 1 exactly, STABLE - the full ternary "
                    "tree, forced by the declared odometer order "
                    "3^D; log_3 2 refuted (hardcoded seed orbit)",
        "letters": "ROLES_ONLY; the chain-to-word map is not "
                   "defined; one universal address tree",
        "regions": "10-marker A13R fixture vs 40 A12 anchor "
                   "regions vs unbounded UEQ0 prefix concept; "
                   "per-region ledgers DECLARED at spec level",
        "transport": "choice-free object region-profile exists "
                     "(903/903 schedule-invariant)",
        "trichotomy": "EXTENDS to bounded-depth hierarchical "
                      "measures (E-level; gap named; boundary "
                      "conditional on unbounded refinement)",
        "r66": "freeze the geometry candidate (ultrametric record "
               "space, delta = 1); open M8 step 1 - scaling limit "
               "+ dimensionless-invariant inventory"},
}
out = PKG / "R65_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R65_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
