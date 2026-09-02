#!/usr/bin/env python3
"""OD0-R60 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r60_stamp.py <commitB_ref>"""
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


results = json.loads((PKG / "OD0_R60_RESULTS.json").read_text(
    encoding="utf-8"))

stamp = {
    "schema": "R60_PROVENANCE_STAMP_V1",
    "round": "OD0-R60",
    "verdict": "OD0_R60_PASS_M7_LAPSE_CLOCK_EPOCH_LAWS_FROZEN",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R60_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R60_OUTPUT_MANIFEST.json"),
    "results_sha256": sha("OD0_R60_RESULTS.json"),
    "report_sha256": sha("OD0_R60_REPORT.md"),
    "M7_prediction_set_sha256": results["M7_prediction_set_sha256"],
    "seals": {"BELL2_opened": False, "H1": "spent", "H2": "spent",
              "H3_parsed": False, "H4_parsed": False,
              "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder "
                           "double-run)",
    "headline": {
        "E1_identity": "tick rate = Gamma Phi^2 pathwise; "
                       "E[Phi^2|state] = D/(F+D)",
        "cycle_law": "<Phi^2>_cycle = 1 - C/(Gamma E[tau]) -> "
                     "1/(1+c) for C = c D ln D (constant-rate form "
                     "refuted)",
        "middrain": "Theta(D log D) bursts per full drain; "
                    "renewals die out as exp(-Theta(D log D))",
        "balance_band": "mean-square vacuum fraction x*^2 = "
                        "r/(4 C(Gamma,2) n ln n), r = Gamma + "
                        "min(H, 2 Gamma) - m",
        "relief": "v* = min(H, 2 Gamma (1-x)); P* = 10 Gamma - 6",
        "full_lapse": "Gamma-stratified recurrence (every Gamma=2 "
                      "burst is a Phi=1 step)",
        "ages": "b ~ n; N_V = O(n^{3/2} sqrt(ln n)); "
                "k ~ (2/r) n^2 ln n",
        "depth": "word depth in [ln n, 2e ln n] E-level; reading "
                 "x3 per depth increment"},
}
out = PKG / "R60_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R60_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
print("M7 set:", stamp["M7_prediction_set_sha256"])
