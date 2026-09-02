#!/usr/bin/env python3
"""OD0-R63 Commit A: input lock. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = json.loads((PKG / "R62_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
pkg_name = "OD0_CLAUDE_CODE_PACKAGE_R63_GEOMETRY_STAGE_OPENING_v0_1.md"
pkg_text = (PKG / pkg_name).read_text(encoding="utf-8")
m = re.search(r"(# 4\. Targets \(frozen at Commit A\).*?)\n# 5\. Readouts",
              pkg_text, re.S)
targets = m.group(1).strip()

manifest_ok = (stamp["output_manifest_sha256"] ==
               sha("R62_OUTPUT_MANIFEST.json"))

lock = {
    "schema": "R63_INPUT_LOCK_V1",
    "round": "OD0-R63",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r62_stamp_pin": {
        "stamp_sha256": sha("R62_PROVENANCE_STAMP.json"),
        "commit_A": stamp["commit_A_prereg"],
        "commit_B": stamp["commit_B_outputs"],
        "output_manifest_sha256": stamp["output_manifest_sha256"],
        "manifest_match_verified": manifest_ok},
    "targets_D1_D6_verbatim": targets,
    "seals": {"BELL2_opened": False,
              "H1_H4": "spent, not consulted (provenance of diameter/"
                       "containment observables disclosed, nothing "
                       "more)",
              "H5": {"parsed": False}},
    "declarations": [
        "D1 inventory and D2-D6 targets frozen verbatim before any "
        "computation",
        "R47 boundary retained: no connection, no holonomy, no strict "
        "identity transport",
        "no external geometric referent, named space, or literature "
        "estimator in any output; 'dimension' only in the D3 internal "
        "sense",
        "no exponent or law fitted from readouts; asymptotics carry "
        "finite-n bounds or CONJECTURE",
        "no locality introduced into the pairing law this round",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R63_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("manifest_match_verified:", manifest_ok)
print("lock sha256:", sha("R63_INPUT_LOCK.json"))
