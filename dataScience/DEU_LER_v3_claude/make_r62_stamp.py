#!/usr/bin/env python3
"""OD0-R62 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r62_stamp.py <commitB_ref>"""
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
    "schema": "R62_PROVENANCE_STAMP_V1",
    "round": "OD0-R62",
    "verdict": "OD0_R62_PASS_H3_H4_OPENED_UNDER_SEALED_PROTOCOLS",
    "H3_COMPARISON": "PARTIAL",
    "H4_COMPARISON": "PARTIAL",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R62_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R62_OUTPUT_MANIFEST.json"),
    "seals": {"BELL2_opened": False, "H1": "spent", "H2": "spent",
              "H3": "OPENED AND SPENT (R62)",
              "H4": "OPENED AND SPENT (R62)",
              "H5_parsed": False},
    "deterministic_rerun": "byte-identical (part4 + builder "
                           "double-run)",
    "headline": {
        "H3": "PARTIAL - fading-deficit pattern matches G5; critical "
              "load line matches G7 in existence/direction; mu(a) a "
              "calibrated projection; spatial claims inapplicable; "
              "no theorem contradicted",
        "H4": "PARTIAL - clock functionals definitionally IDENTICAL "
              "to R56 O1/O2/O7 incl. lnln normalization; ln(4/3) "
              "offset STATE_CLASS_MISMATCH; definition-invariant "
              "ordering consistent; capacity-clock claims direction-"
              "consistent with C1/C2; no theorem contradicted",
        "milestone": "All four spent holdouts (H1-H4) met without "
                     "contradiction; geometry stage (roadmap 7) "
                     "unblocked for R63"},
}
out = PKG / "R62_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R62_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
