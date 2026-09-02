#!/usr/bin/env python3
"""OD0-R68 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r68_stamp.py <commitB_ref>"""
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
    "schema": "R68_PROVENANCE_STAMP_V1",
    "round": "OD0-R68",
    "verdict": "OD0_R68_PASS_TOKEN_REGION_CLASS_ADJUDICATED",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R68_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R68_OUTPUT_MANIFEST.json"),
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder "
                           "double-run)",
    "headline": {
        "premise": "TD1 (T-DEEP zero-clause form) UNIQUE_MINIMAL - "
                   "stated, not adopted; TR1' is its depth-1 "
                   "truncation (R66 record superseded, recorded)",
        "survivors": "T-DEEP > TR1' > plurality; T-LAST "
                     "schedule-dependent (rejected); "
                     "T-INHERIT/T-PROFILE degenerate",
        "region_set": "FIXED_MAP (finite inherited set; 10-marker "
                      "fixture; nearest-mapped-ancestor charging; "
                      "capacity constant - tower intact)",
        "fields": "charge-share theorem (q0; q1/3 + Q2/9; Q2/9); "
                  "two-phase lapse law: early share-ordered, "
                  "mature NINE-REGION EQUALIZATION at N = 9 Gamma "
                  "with ROOT permanently free; d* = log_3(N/Gamma); "
                  "density rho_rec(d) = N_{>=d}; per-region "
                  "duality proven",
        "r69": "preregister the H5 comparison protocol against "
               "the density and lapse fields; R70 opens H5 - the "
               "last sealed corpus"},
}
out = PKG / "R68_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R68_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
