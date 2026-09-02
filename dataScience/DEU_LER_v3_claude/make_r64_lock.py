#!/usr/bin/env python3
"""OD0-R64 Commit A: input lock. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


base = json.loads((PKG / "R63_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
add = json.loads((PKG / "R63_ADDENDUM_STAMP.json").read_text(
    encoding="utf-8"))
pkg_name = "OD0_CLAUDE_CODE_PACKAGE_R64_LOCALITY_PREMISE_CLASS_v0_1.md"
pkg_text = (PKG / pkg_name).read_text(encoding="utf-8")
mg = re.search(r"(# 4\. Part 1.*?)\n-{3,}\s*\n+# 5\.", pkg_text, re.S)
mn = re.search(r"(# 6\. Part 3.*?)\n-{3,}\s*\n+# 7\.", pkg_text, re.S)
gates_verbatim = mg.group(1).strip()
nogo_verbatim = mn.group(1).strip()

GATE_LIST = [
    "ALL", "REL", "UNREL", "PC", "NOT_PC", "GP", "NOT_GP", "SIB",
    "NOT_SIB", "COUSIN1", "NOT_COUSIN1", "LEAF1", "LEAF2",
    "NOT_LEAF2", "REC2", "MINCOST", "NOT_MINCOST", "DG2", "NOT_DG2",
    "DG3PLUS", "NOT_DG3PLUS", "SIB_AND_LEAF1", "REL_AND_MINCOST",
    "UNREL_AND_MINCOST", "DG2_AND_LEAF1"]

lock = {
    "schema": "R64_INPUT_LOCK_V1",
    "round": "OD0-R64",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r63_base_stamp_pin": {
        "stamp_sha256": sha("R63_PROVENANCE_STAMP.json"),
        "manifest_match": base["output_manifest_sha256"] ==
                          sha("R63_OUTPUT_MANIFEST.json")},
    "r63_addendum_stamp_pin": {
        "stamp_sha256": sha("R63_ADDENDUM_STAMP.json"),
        "manifest_match": add["addendum_manifest_sha256"] ==
                          sha("R63_ADDENDUM_MANIFEST.json")},
    "gate_class_verbatim": gates_verbatim,
    "gate_enumeration": {
        "members": GATE_LIST, "count": len(GATE_LIST),
        "notes": [
            "complement identities: NOT_REL = UNREL and NOT_UNREL = "
            "REL (not double-counted); NOT_LEAF1 = REC2 exactly (by "
            "the R63 leaf theorem: recorded iff has a child) - "
            "listed once as REC2; NOT_REC2 = LEAF1 likewise",
            "NOT_DG3PLUS = {d_G <= 2} = PC-edge union DG2, distinct "
            "from DG2 alone",
            "MINCOST is inert at Gamma = 2 (a single new pair is "
            "always minimal)"]},
    "no_go_statement_verbatim": nogo_verbatim,
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5": {"parsed": False}},
    "declarations": [
        "gates tested as candidates, never adopted as laws this round",
        "service kernel untouched; frozen tower untouched",
        "no threshold, weight, or length; no external referent; "
        "'dimension' only as the D3 exponent",
        "no exponent or spectral radius fitted from readouts",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R64_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("base pin:", lock["r63_base_stamp_pin"]["manifest_match"],
      "| addendum pin:",
      lock["r63_addendum_stamp_pin"]["manifest_match"])
print("|G| =", len(GATE_LIST))
print("lock sha256:", sha("R64_INPUT_LOCK.json"))
