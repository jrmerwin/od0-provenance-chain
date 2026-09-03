#!/usr/bin/env python3
"""OD0-R69 Commit A: input lock. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = json.loads((PKG / "R68_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
pkg_name = "OD0_CLAUDE_CODE_PACKAGE_R69_H5_PREREGISTRATION_v0_1.md"
pkg_text = (PKG / pkg_name).read_text(encoding="utf-8")
mt = re.search(r"(# 4\. Derived-side table.*?)\n-{3,}\s*\n+# 6\.",
               pkg_text, re.S)

lock = {
    "schema": "R69_INPUT_LOCK_V1",
    "round": "OD0-R69",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r68_stamp_pin": {
        "stamp_sha256": sha("R68_PROVENANCE_STAMP.json"),
        "commit_A": stamp["commit_A_prereg"],
        "commit_B": stamp["commit_B_outputs"],
        "manifest_match": stamp["output_manifest_sha256"] ==
                          sha("R68_OUTPUT_MANIFEST.json")},
    "sections_4_5_verbatim": mt.group(1).strip(),
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5": {"parsed": False}},
    "declarations": [
        "H5 not opened; artifact pinning by name and byte hash only",
        "the derived side is conditional on TD1 (+ CO1, RO1, TG1, "
        "V ~ X) - every comparable statement carries that "
        "conditionality",
        "the dark fraction (Q8) is NOT compared - the R66 seal "
        "stands through R70; recorded here so the temptation "
        "cannot be reached for at opening",
        "state-class rule (R62) in force; fixture-specific clauses "
        "compared only under a definitional region-structure map",
        "nothing added to Sections 4-5 after Commit A",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R69_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("manifest_match:", lock["r68_stamp_pin"]["manifest_match"])
print("lock sha256:", sha("R69_INPUT_LOCK.json"))
