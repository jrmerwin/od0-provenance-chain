#!/usr/bin/env python3
"""OD0-R67 Commit A: input lock. Verifies the sealed M8 protocol
unchanged BEFORE any Part A work. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = json.loads((PKG / "R66_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
protocol = json.loads((PKG / "R66_M8_COMPARISON_PREREGISTRATION.json"
                       ).read_text(encoding="utf-8"))
pkg_name = "OD0_CLAUDE_CODE_PACKAGE_R67_M8_EXECUTION_AND_BRANCH_D_v0_1.md"
pkg_text = (PKG / pkg_name).read_text(encoding="utf-8")
mi = re.search(r"(## 5\.1 Structure inventory.*?)\n## 5\.2", pkg_text,
               re.S)

protocol_hash_now = sha("R66_M8_COMPARISON_PREREGISTRATION.json")
sealed_hash = "e0a94da19ad542d9658098b98f8dc38e2b66b58894c7ad65f6033fd712621da7"

lock = {
    "schema": "R67_INPUT_LOCK_V1",
    "round": "OD0-R67",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r66_stamp_pin": {
        "stamp_sha256": sha("R66_PROVENANCE_STAMP.json"),
        "manifest_match": stamp["output_manifest_sha256"] ==
                          sha("R66_OUTPUT_MANIFEST.json"),
        "M8_protocol_hash_in_stamp": stamp["M8_prereg_sha256"]},
    "m8_protocol_verification": {
        "sealed_hash_carried_by_package": sealed_hash,
        "hash_now": protocol_hash_now,
        "UNCHANGED": protocol_hash_now == sealed_hash ==
                     stamp["M8_prereg_sha256"]},
    "m8_protocol_verbatim": protocol,
    "part_b_inventory_5_1_verbatim": mi.group(1).strip(),
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5": {"parsed": False}},
    "declarations": [
        "Part A values computed independently (exact algebra), never "
        "copied from the frozen Bell report",
        "no new Bell computation (A5's native value stays open; "
        "BELL3 recorded)",
        "no structure added to 5.1 after Commit A; no invariant "
        "inner product chosen where a family exists; no m chosen",
        "closure-amplitude values are the match target only; no "
        "derivation imported",
        "TR1' untouched (R68 per the R66 rule)",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R67_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("protocol UNCHANGED:",
      lock["m8_protocol_verification"]["UNCHANGED"])
print("manifest match:", lock["r66_stamp_pin"]["manifest_match"])
print("lock sha256:", sha("R67_INPUT_LOCK.json"))
