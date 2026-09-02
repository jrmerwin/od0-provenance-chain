#!/usr/bin/env python3
"""OD0-R63 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r63_stamp.py <commitB_ref>"""
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
    "schema": "R63_PROVENANCE_STAMP_V1",
    "round": "OD0-R63",
    "verdict": "OD0_R63_PASS_GEOMETRY_STRUCTURES_CLASSIFIED_AND_SCALED",
    "primary": "NONE_UNDER_UNIFORM_PAIRING",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R63_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R63_OUTPUT_MANIFEST.json"),
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder "
                           "double-run)",
    "headline": {
        "classification": "dG metric; darrow extended quasimetric; "
                          "dU NONE (both triangle forms fail, exact "
                          "witnesses); dJ metric (closed cones)",
        "diameter": "Theta(log n) two-sided; ball base exactly 8 "
                    "(spectral radius); depth constants = roots of "
                    "c(1 + ln 2 - ln c) = 1: 0.3734 / 4.3111",
        "jaccard": "d_J late-pair law nondegenerate; ratio-of-means "
                   "22/35 exactly (E[sqrt(W)] cancels); D3 "
                   "trichotomy incomplete",
        "order": "unrelated fraction 1 - (pi^{3/2}/2) n^{-1/2}; "
                 "beta ~ n^{2/3}; interval threshold n^{1/4}; "
                 "f(I) ~ s^{-1/2}",
        "bedrock": "sparse self-similar (near-total order refuted); "
                   "Theta(log n) access (O(1) refuted)",
        "locality": "D4/D5 PROVEN - no locality from pairing or "
                    "service; any locality must be emergent",
        "primary": "NONE_UNDER_UNIFORM_PAIRING -> R64 = locality "
                   "premise class (TG1 template)"},
}
out = PKG / "R63_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R63_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
