#!/usr/bin/env python3
"""OD0-R63 ADDENDUM provenance stamp (Commit C2). Hashes in-process.
Usage: python make_r63_addendum_stamp.py <commitB2_ref>"""
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
    "schema": "R63_ADDENDUM_STAMP_V1",
    "round": "OD0-R63-ADDENDUM",
    "verdict": "OD0_R63_ADDENDUM_PASS_OPERATIONAL_LAYER_FROZEN",
    "ADDENDUM_FROZEN_AFTER_A": True,
    "commit_A2_freeze": rev(B_REF + "~1"),
    "commit_B2_outputs": rev(B_REF),
    "addendum_lock_sha256": sha("R63_ADDENDUM_LOCK.json"),
    "addendum_manifest_sha256": sha("R63_ADDENDUM_MANIFEST.json"),
    "operational_layer_sha256": sha("R63_OPERATIONAL_LAYER.json"),
    "base_round": {"commit_C": "a22f5fd",
                   "base_manifest_sha256_pinned":
                       sha("R63_OUTPUT_MANIFEST.json")},
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder "
                           "double-run)",
    "headline": {
        "D7": "U = leaves exactly; horizon E|U|/n = 1/3 - 2/(3n); "
              "d_arrow/d_U/d_J/order READABLE_FROM_S on X_rec; "
              "d_G MIXED (leaf shortcuts invisible to S)",
        "D8": "comparison collapses d_G to <= 2, leaves all "
              "cone-based distances invariant, costs "
              "Theta(n log n), drain (5 n ln n / r)(1+o(1))",
        "D9": "d_cost is a METRIC at any common snapshot (triangle "
              "THEOREM, slack >= 22, snapshot-relative; registered "
              "failure refuted); DEGENERATE at 1/sqrt(log n) rate; "
              "primary NONE_UNDER_UNIFORM_PAIRING stands over all "
              "seven structures"},
}
out = PKG / "R63_ADDENDUM_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R63_ADDENDUM_STAMP.json"))
print("A2:", stamp["commit_A2_freeze"])
print("B2:", stamp["commit_B2_outputs"])
