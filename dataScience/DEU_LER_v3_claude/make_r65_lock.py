#!/usr/bin/env python3
"""OD0-R65 Commit A: input lock. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = json.loads((PKG / "R64_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
pkg_name = "OD0_CLAUDE_CODE_PACKAGE_R65_PREFIX_CYLINDER_BRANCH_C_v0_1.md"
pkg_text = (PKG / pkg_name).read_text(encoding="utf-8")
mt = re.search(r"(# 4\. Targets.*?)\n-{3,}\s*\n+# 5\.", pkg_text, re.S)
mb = re.search(r"(# 7\. Branch record.*?)\n-{3,}\s*\n+# 8\.", pkg_text,
               re.S)

lock = {
    "schema": "R65_INPUT_LOCK_V1",
    "round": "OD0-R65",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r64_stamp_pin": {
        "stamp_sha256": sha("R64_PROVENANCE_STAMP.json"),
        "commit_A": stamp["commit_A_prereg"],
        "commit_B": stamp["commit_B_outputs"],
        "manifest_match": stamp["output_manifest_sha256"] ==
                          sha("R64_OUTPUT_MANIFEST.json")},
    "targets_P1_P4_verbatim": mt.group(1).strip(),
    "branch_record_verbatim": mb.group(1).strip(),
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5": {"parsed": False}},
    "declarations": [
        "zero premises adopted; base 3 is the alphabet, not a choice",
        "no object-to-cylinder assignment invented - extraction only",
        "no measure adopted as a law; only choice-free measures "
        "admitted to W",
        "no external referent; 'dimension' only in the D3 sense",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R65_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("manifest_match:", lock["r64_stamp_pin"]["manifest_match"])
print("lock sha256:", sha("R65_INPUT_LOCK.json"))
