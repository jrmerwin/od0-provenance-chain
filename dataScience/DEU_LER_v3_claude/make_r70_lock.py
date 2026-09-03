#!/usr/bin/env python3
"""OD0-R70 Commit A: input lock. Verifies the sealed H5 protocol and
every H5 artifact hash BEFORE any content is read. Hashes in-process."""
import hashlib
import json
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


def fsha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


stamp = json.loads((PKG / "R69_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
protocol = json.loads((PKG / "R69_H5_PREREGISTRATION.json").read_text(
    encoding="utf-8"))
pins = json.loads((PKG / "R69_ARTIFACT_PINS.json").read_text(
    encoding="utf-8"))
pkg_name = "OD0_CLAUDE_CODE_PACKAGE_R70_OPEN_H5_UNDER_SEALED_PROTOCOL_v0_1.md"

sealed = "160775e68feaecbcaa081a77e96ba8640def57d14693a3d6fb69fc2767d26c94"
now = sha("R69_H5_PREREGISTRATION.json")

rows = []
ok = bad = 0
for it in pins["H5"]["items"]:
    p = Path(it["path"])
    cur = fsha(p) if p.is_file() else "MISSING"
    match = cur == it.get("current_sha256")
    rows.append({"path": it["path"], "hash_match": match})
    ok += 1 if match else 0
    bad += 0 if match else 1

lock = {
    "schema": "R70_INPUT_LOCK_V1",
    "round": "OD0-R70",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r69_stamp_pin": {
        "stamp_sha256": sha("R69_PROVENANCE_STAMP.json"),
        "manifest_match": stamp["output_manifest_sha256"] ==
                          sha("R69_OUTPUT_MANIFEST.json"),
        "protocol_hash_in_stamp": stamp["H5_prereg_sha256"]},
    "protocol_verification": {
        "sealed_hash": sealed, "hash_now": now,
        "UNCHANGED": now == sealed == stamp["H5_prereg_sha256"]},
    "protocol_verbatim": protocol,
    "artifact_hash_verification_before_reading": {
        "verified": ok, "failed": bad, "rows": rows},
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent, not consulted"},
    "declarations": [
        "H5 opened under the sealed protocol only; one comparison, "
        "no repair",
        "pre-committed classifications applied at extraction before "
        "adjudication",
        "Q8 (the dark fraction) is not compared; any fraction-of-"
        "total quantity is recorded and left uncompared",
        "the de Sitter-closure family is MANUSCRIPT_ONLY at equal "
        "prominence",
        "Part 4 readouts are archive-only and enter no verdict",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R70_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("protocol UNCHANGED:",
      lock["protocol_verification"]["UNCHANGED"])
print("artifacts verified:", ok, "failed:", bad)
print("lock sha256:", sha("R70_INPUT_LOCK.json"))
