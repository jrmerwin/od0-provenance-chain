#!/usr/bin/env python3
"""OD0-R63 ADDENDUM Commit A2: hashed appendix freezing D7-D9 before
any D7-D9 computation. All hashes in-process."""
import hashlib
import json
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


addendum_name = ("OD0_CLAUDE_CODE_PACKAGE_R63_ADDENDUM_OPERATIONAL_"
                 "LAYER_v0_1 (1).md")
stamp = json.loads((PKG / "R63_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))

lock = {
    "schema": "R63_ADDENDUM_LOCK_V1",
    "round": "OD0-R63-ADDENDUM",
    "addendum_package": addendum_name,
    "addendum_sha256": sha(addendum_name),
    "ADDENDUM_FROZEN_AFTER_A": True,
    "base_round_status": "R63 base is FULLY FROZEN (commits A=3364ea4 "
        "B=fe44b89 C=a22f5fd; stamp verified below). The addendum "
        "arrived after Commit C; D7-D9 are frozen here in a hashed "
        "appendix BEFORE any D7-D9 computation, per the addendum's "
        "own rule. Base outputs are not modified; the operational "
        "layer is appended via its own manifest and stamp. The "
        "addendum's 'include its hash in the manifest' instruction "
        "is honored by R63_ADDENDUM_MANIFEST.json, which pins the "
        "frozen base manifest (deviation recorded: the base "
        "manifest itself is immutable).",
    "r63_base_pin": {
        "stamp_sha256": sha("R63_PROVENANCE_STAMP.json"),
        "base_manifest_sha256": stamp["output_manifest_sha256"],
        "base_manifest_match": stamp["output_manifest_sha256"] ==
                               sha("R63_OUTPUT_MANIFEST.json")},
    "targets_D7_D9_verbatim": (PKG / addendum_name).read_text(
        encoding="utf-8"),
    "seals": {"BELL2_opened": False, "H1_H4": "spent", "H5":
              {"parsed": False}},
    "declarations": [
        "zero new premises; same locks, controls, vocabulary as base",
        "hostile control 9: no operational claim beyond D7-D9; no "
        "observer, agent, or protocol posited; 'readable' means 'a "
        "function of S', nothing more",
        "the base counterexample file's hash is frozen in the base "
        "manifest; addendum corrections are recorded inside the "
        "addendum outputs instead (convention conflict resolved in "
        "favor of manifest integrity, recorded)",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R63_ADDENDUM_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("base manifest match:",
      lock["r63_base_pin"]["base_manifest_match"])
print("addendum lock sha256:", sha("R63_ADDENDUM_LOCK.json"))
