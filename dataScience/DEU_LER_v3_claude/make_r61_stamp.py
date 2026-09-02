#!/usr/bin/env python3
"""OD0-R61 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r61_stamp.py <commitB_ref>"""
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


results = json.loads((PKG / "OD0_R61_RESULTS.json").read_text(
    encoding="utf-8"))

stamp = {
    "schema": "R61_PROVENANCE_STAMP_V1",
    "round": "OD0-R61",
    "verdict": "OD0_R61_PASS_H3_H4_PREREGISTERED",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R61_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R61_OUTPUT_MANIFEST.json"),
    "H3_prereg_sha256": sha("R61_H3_PREREGISTRATION.json"),
    "H4_prereg_sha256": sha("R61_H4_PREREGISTRATION.json"),
    "C5_appendix_sha256": results["components"]["C5_appendix_sha256"],
    "G7_appendix_sha256": results["components"]["G7_appendix_sha256"],
    "seals": {"BELL2_opened": False, "H1": "spent", "H2": "spent",
              "H3_parsed": False, "H4_parsed": False,
              "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + pins + builder "
                           "double-run)",
    "headline": {
        "preregistrations": "H3 and H4 sealed; opening at R62, one "
                            "comparison each, no repair",
        "clock_functionals": "TC ~ (pi^{3/2}/4) n^{3/2}; TCo ~ n^2 "
                             "band; co-embedding clock ahead by "
                             "ln(4/3)",
        "relief_line": "band collapsed to m_c = Gamma + "
                       "min(H, 2 Gamma); both sides proven a.s.; "
                       "line critical, open",
        "erratum": "R59 T3 cone constant corrected forward to "
                   "(3/8) pi^{3/2} (Yule-limit factor sqrt(pi)/2)",
        "artifacts": "H3 17/17, H4 26/26 pinned unchanged; no "
                     "PAPER_ONLY; v31l/m/n found, v31o missing"},
}
out = PKG / "R61_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R61_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
