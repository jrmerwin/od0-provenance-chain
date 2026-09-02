#!/usr/bin/env python3
"""OD0-R59 provenance stamp (Commit C). All hashes in-process."""
import hashlib
import json
import subprocess
from pathlib import Path

PKG = Path(__file__).resolve().parent


def rev(ref):
    return subprocess.run(["git", "rev-parse", ref], cwd=PKG,
                          capture_output=True, text=True,
                          check=True).stdout.strip()


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = {
    "schema": "R59_PROVENANCE_STAMP_V1",
    "round": "OD0-R59",
    "verdict": "OD0_R59_PASS_RANDOM_DAG_COST_TARGETS_ADJUDICATED",
    "commit_A_prereg": rev("98b5d52~1"),
    "commit_B_outputs": rev("98b5d52"),
    "input_lock_sha256": sha("R59_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R59_OUTPUT_MANIFEST.json"),
    "results_sha256": sha("OD0_R59_RESULTS.json"),
    "report_sha256": sha("OD0_R59_REPORT.md"),
    "seals": {"BELL2_opened": False, "H1": "spent", "H2": "spent",
              "H3_parsed": False, "H4_parsed": False, "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder double-run)",
    "headline": {
        "exact_closed_form": "E[T_n] = n(n-1)/2 + 1 (exact, all n)",
        "identity": "paths_to = 2 chains - 2 (exact, 173/173)",
        "ancestor_law": "a_j(n) = 2 phi_j - phi_j^2, "
                        "phi_j(n) = n/(n+j(j-1))",
        "cone": "(3 pi/4) sqrt(n)",
        "cost": "Theta(n log n), paths-form 4 n ln n leading",
        "growth": "N^2 ln N = (Gamma+H-m) k / 2 (E-level two-sided)",
        "termination": "CLOSED for m > Gamma + H "
                       "(low-chain population lemma)"},
}
out = PKG / "R59_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R59_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
