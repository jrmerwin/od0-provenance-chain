#!/usr/bin/env python3
"""OD0-R64 provenance stamp (Commit C). All hashes in-process.
Usage: python make_r64_stamp.py <commitB_ref>"""
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
    "schema": "R64_PROVENANCE_STAMP_V1",
    "round": "OD0-R64",
    "verdict": "OD0_R64_PASS_LOCALITY_CLASS_CLASSIFIED",
    "primary": "NO_GO_G = PROVEN",
    "commit_A_prereg": rev(B_REF + "~1"),
    "commit_B_outputs": rev(B_REF),
    "input_lock_sha256": sha("R64_INPUT_LOCK.json"),
    "output_manifest_sha256": sha("R64_OUTPUT_MANIFEST.json"),
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5_parsed": False},
    "deterministic_rerun": "byte-identical (engine + builder "
                           "double-run)",
    "headline": {
        "no_go": "no parameter-free binary internal gate yields a "
                 "stable exponent > 1: exponential worlds or chains, "
                 "nothing between (eligible-pair drift dichotomy: "
                 "E_{n+1} - E_n = C_n - 1; Theta(n)/Theta(1)/"
                 "extinction trichotomy closes the window)",
        "bases": "ALL 8; LEAF1 (5+sqrt(41))/2 = 5.7016; MINCOST "
                 "48/5, 384/35, 256/21 (Gamma = 3,4,5) - above 8, "
                 "rising; DG2 small-world, delta drifting",
        "chains": "SIB (minimal seed, deterministic forced chain), "
                  "SIB_AND_LEAF1, DG2_AND_LEAF1 (ballistic "
                  "filament) - exponent exactly 1",
        "rel_tower": "ln chains = Theta(sqrt(log n)), kappa = "
                     "pi/sqrt(3); cost n^{o(1)}; growth T^{1-o(1)}",
        "fixed_points": "leaf fractions: ALL 1/3; NOT_LEAF2 "
                        "sqrt(2)-1; LEAF1 exactly one leaf; "
                        "MINCOST 0.4404/0.5697 (Gamma = 3/5)",
        "r65": "three-branch fork, no selection; branch (c) = the "
               "CD1I prefix-cylinder region tree (ultrametric, "
               "base 3)"},
}
out = PKG / "R64_PROVENANCE_STAMP.json"
out.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("stamp sha256:", sha("R64_PROVENANCE_STAMP.json"))
print("A:", stamp["commit_A_prereg"])
print("B:", stamp["commit_B_outputs"])
print("manifest:", stamp["output_manifest_sha256"])
