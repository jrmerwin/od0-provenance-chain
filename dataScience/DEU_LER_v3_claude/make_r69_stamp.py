#!/usr/bin/env python3
"""OD0-R69 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r69_stamp.py <commitB_ref>"""
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
    "schema": "R69_PROVENANCE_STAMP_V1",
    "round": "OD0-R69",
    "verdict": "OD0_R69_PASS_H5_PREREGISTERED",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R69_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R69_OUTPUT_MANIFEST.json"),
    "H5_prereg_sha256": sha("R69_H5_PREREGISTRATION.json"),
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent",
              "H5": "SEALED (parsed=false); opens R70 under the "
                    "sealed protocol"},
    "deterministic_rerun": "byte-identical (pins + builder "
                           "double-run)",
    "headline": {
        "derived_side": "Q1-Q8 frozen (density, critical density, "
                        "boundary motion, two-phase lapse, ratios, "
                        "tick field, duality, dark fraction); Q8 "
                        "NOT COMPARED (R66 seal recorded)",
        "protocol": "sealed with the advance rule, state-class "
                    "rule, Tier D exclusions, pre-committed "
                    "classifications, and three pre-committed FAIL "
                    "diagnoses",
        "artifacts": "H5 14/14 pinned unchanged; not PAPER_ONLY; "
                     "the de Sitter-closure computation still "
                     "missing (manuscript-only family)",
        "r70": "open H5 - the LAST sealed corpus; after it, the "
               "proto-paper and the queued theorems"},
}
out = PKG / "R69_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R69_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
