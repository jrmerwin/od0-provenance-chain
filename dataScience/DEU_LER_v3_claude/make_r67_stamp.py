#!/usr/bin/env python3
"""OD0-R67 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r67_stamp.py <commitB_ref>"""
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
    "schema": "R67_PROVENANCE_STAMP_V1",
    "round": "OD0-R67",
    "verdict": "OD0_R67_PASS_M8_COMPARISON_EXECUTED_AND_BRANCH_D_"
               "ADJUDICATED",
    "M8_BELL": "PASS (no contradiction)",
    "BRANCH_D": "CONDITIONAL_ARROW(S-e, m = 4)",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R67_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R67_OUTPUT_MANIFEST.json"),
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder "
                           "double-run)",
    "headline": {
        "A1": "CGLMP: EXACT_AGREEMENT by algebraic equality - "
              "independent Born computation = 4/3 + (8/9) sqrt(3) "
              "in Q(sqrt 3); local bound exactly 2",
        "A2": "CHSH: EXACT_AGREEMENT - independent supremum "
              "2.517939955996... to all frozen digits; the frozen "
              "quintic identified as the stationarity polynomial "
              "in c = cos(2 pi phi/3); S's own minimal polynomial "
              "the 27^4 quartic (precision recorded)",
        "A4_A5": "RESTRICTION on the non-maximal ceiling exactly "
                 "as declared; heralded-state existence agreement; "
                 "native value left open (BELL3 recorded)",
        "branch_d": "the closure-amplitude Gram IS the 4-sibling "
                    "exchange sector: rho = 1/3, rank 3, spectrum "
                    "{0, 4/3 x3} - conditional on Gamma >= 5; "
                    "m = 4 is a capacity condition, not a constant",
        "one_thirds": "alphabet-dark: one p = 2 theorem; simplex: "
                      "conditional on the 4-sibling event",
        "milestone": "first external comparison of the tower: the "
                     "quantum-side scaffold PASSES"},
}
out = PKG / "R67_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R67_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
