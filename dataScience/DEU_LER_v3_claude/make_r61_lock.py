#!/usr/bin/env python3
"""OD0-R61 Commit A: input lock. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = json.loads((PKG / "R60_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
pkg_name = "OD0_CLAUDE_CODE_PACKAGE_R61_H3_H4_PREREGISTRATION_v0_1.md"
pkg_text = (PKG / pkg_name).read_text(encoding="utf-8")

m = re.search(r"(# 4\. Derived-side tables.*?)\n# 7\. Part 3",
              pkg_text, re.S)
sections_4_6 = m.group(1).strip()

manifest_ok = (stamp["output_manifest_sha256"] ==
               sha("R60_OUTPUT_MANIFEST.json"))
m7_ok = (stamp["M7_prediction_set_sha256"] ==
         sha("R60_M7_PREDICTION_SET.json"))

lock = {
    "schema": "R61_INPUT_LOCK_V1",
    "round": "OD0-R61",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r60_stamp_pin": {
        "stamp_sha256": sha("R60_PROVENANCE_STAMP.json"),
        "commit_A": stamp["commit_A_prereg"],
        "commit_B": stamp["commit_B_outputs"],
        "output_manifest_sha256": stamp["output_manifest_sha256"],
        "manifest_match_verified": manifest_ok,
        "M7_prediction_set_sha256": stamp["M7_prediction_set_sha256"],
        "M7_hash_match_verified": m7_ok},
    "r56_observable_freeze_pin": {
        "R56_H2_PREREGISTRATION_sha256": sha(
            "R56_H2_PREREGISTRATION.json"),
        "note": "O1 containment, O2 coembedding, O7 clock functionals "
                "used under their frozen verbatim definitions"},
    "sections_4_to_6_verbatim": sections_4_6,
    "seals": {"BELL2_opened": False,
              "H1": "spent (R54)", "H2": "spent (R57)",
              "H3": {"parsed": False}, "H4": {"parsed": False},
              "H5": {"parsed": False}},
    "declarations": [
        "Sections 4-6 frozen verbatim at Commit A; only the hashed "
        "Part 2 (C5_DERIVED) and Part 4 (G7_UPDATED_R61) appendices "
        "may be added, derived before any opening",
        "H3/H4 not opened; artifact pinning is by name and hash only, "
        "no scientific content parsed",
        "Tier D quantities, rates-versus-rounds, and spatial/regional "
        "claims excluded from both protocols by construction",
        "no external referent in any output",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R61_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("manifest_match_verified:", manifest_ok)
print("M7_hash_match_verified:", m7_ok)
print("lock sha256:", sha("R61_INPUT_LOCK.json"))
