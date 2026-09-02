#!/usr/bin/env python3
"""OD0-R66 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r66_stamp.py <commitB_ref>"""
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
    "schema": "R66_PROVENANCE_STAMP_V1",
    "round": "OD0-R66",
    "verdict": "OD0_R66_PASS_GEOMETRY_FROZEN_AND_M8_PREREGISTERED",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R66_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R66_OUTPUT_MANIFEST.json"),
    "M8_prereg_sha256": sha("R66_M8_COMPARISON_PREREGISTRATION.json"),
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder "
                           "double-run)",
    "headline": {
        "G1": "geometry candidate FROZEN: the ultrametric record "
              "tree, delta = 1, back-action invariant",
        "G2": "duality PROVEN: the clock's characters ARE the "
              "boundary of the record tree (explicit pairing, "
              "exact certificates)",
        "R1": "REQUIRES_PREMISE - the token-region map is not "
              "derivable (common-prefix degenerate 2304/2304; "
              "majority partial; sources take region_mu as given); "
              "TR1' recorded, not adopted",
        "S1_S2": "scaling limit stated (space/measure/duality "
                 "exact; fields conditional); scope: no length, no "
                 "manifold, no object metric",
        "I1": "23 invariants inventoried by bridge class; dark "
              "fraction comparison FORBIDDEN pending its "
              "dictionary",
        "M8": "first dimensionless-comparison protocol SEALED "
              "(settings dictionary only; expected pattern "
              "declared; execution R67, one round, no repair)"},
}
out = PKG / "R66_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R66_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
print("M8 prereg:", stamp["M8_prereg_sha256"])
