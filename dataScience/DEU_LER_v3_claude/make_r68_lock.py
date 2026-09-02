#!/usr/bin/env python3
"""OD0-R68 Commit A: input lock. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = json.loads((PKG / "R67_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
r66_reg = json.loads((PKG / "R66_REGIONAL_INSTANTIATION_AND_FIELDS."
                      "json").read_text(encoding="utf-8"))
pkg_name = "OD0_CLAUDE_CODE_PACKAGE_R68_TR1_PRIME_PREMISE_ROUND_v0_1.md"
pkg_text = (PKG / pkg_name).read_text(encoding="utf-8")
mt = re.search(r"(# 4\. Part 1.*?)\n-{3,}\s*\n+# 8\.", pkg_text, re.S)

lock = {
    "schema": "R68_INPUT_LOCK_V1",
    "round": "OD0-R68",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r67_stamp_pin": {
        "stamp_sha256": sha("R67_PROVENANCE_STAMP.json"),
        "manifest_match": stamp["output_manifest_sha256"] ==
                          sha("R67_OUTPUT_MANIFEST.json")},
    "TR1_prime_verbatim_from_R66":
        r66_reg["R1_token_region"]["candidate_premise"],
    "class_T_and_targets_verbatim": mt.group(1).strip(),
    "class_T_enumeration": ["T0 (inert: all ROOT)", "TR1_prime",
                            "T_DEEP", "T_LAST", "T_INHERIT",
                            "T_PROFILE", "plus any found"],
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5": {"parsed": False}},
    "declarations": [
        "zero premises adopted beyond stating a survivor as "
        "conditional; the survivor is stated, never asserted as "
        "source",
        "pairing, TG1, RO-D, the cost law, and G1/G2 untouched; "
        "the R64 no-go stands",
        "region reading settled by source extraction before "
        "instantiation; ALL_OCCUPIED results, if any, labeled",
        "no candidate added after Commit A; no parameterized "
        "tie-break",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R68_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("manifest_match:", lock["r67_stamp_pin"]["manifest_match"])
print("lock sha256:", sha("R68_INPUT_LOCK.json"))
