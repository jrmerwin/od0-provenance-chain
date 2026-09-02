#!/usr/bin/env python3
"""OD0-R66 Commit A: input lock. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = json.loads((PKG / "R65_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
pkg_name = ("OD0_CLAUDE_CODE_PACKAGE_R66_GEOMETRY_FREEZE_REGIONAL_M8_"
            "PREREG_v0_1.md")
pkg_text = (PKG / pkg_name).read_text(encoding="utf-8")
mt = re.search(r"(# 4\. Part 1.*?)\n-{3,}\s*\n+# 9\.", pkg_text, re.S)
targets = mt.group(1).strip()

lock = {
    "schema": "R66_INPUT_LOCK_V1",
    "round": "OD0-R66",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r65_stamp_pin": {
        "stamp_sha256": sha("R65_PROVENANCE_STAMP.json"),
        "commit_A": stamp["commit_A_prereg"],
        "commit_B": stamp["commit_B_outputs"],
        "manifest_match": stamp["output_manifest_sha256"] ==
                          sha("R65_OUTPUT_MANIFEST.json")},
    "targets_G_R_S_I_and_protocol_skeleton_verbatim": targets,
    "seals": {"BELL2_opened": False,
              "BELL2_note": "frozen verdicts citable; scientific "
                            "content not reopened",
              "H1_H4": "spent", "H5": {"parsed": False}},
    "declarations": [
        "zero premises adopted; external values named only inside "
        "the Section 8 sealed protocol; no comparison this round",
        "mathematical identifications permitted per note 3; no "
        "physical referent outside the sealed protocol",
        "no regional instantiation without R1 DERIVABLE; no "
        "token-region map invented",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R66_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("manifest_match:", lock["r65_stamp_pin"]["manifest_match"])
print("lock sha256:", sha("R66_INPUT_LOCK.json"))
