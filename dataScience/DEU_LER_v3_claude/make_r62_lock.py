#!/usr/bin/env python3
"""OD0-R62 Commit A: input lock. Verifies every H3/H4 artifact hash and
both protocol hashes BEFORE any content is read. All hashes in-process."""
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


stamp = json.loads((PKG / "R61_PROVENANCE_STAMP.json").read_text(
    encoding="utf-8"))
pins = json.loads((PKG / "R61_ARTIFACT_PINS.json").read_text(
    encoding="utf-8"))
h3_protocol = json.loads((PKG / "R61_H3_PREREGISTRATION.json").read_text(
    encoding="utf-8"))
h4_protocol = json.loads((PKG / "R61_H4_PREREGISTRATION.json").read_text(
    encoding="utf-8"))
pkg_name = ("OD0_CLAUDE_CODE_PACKAGE_R62_OPEN_H3_H4_UNDER_SEALED_"
            "PROTOCOLS_v0_1.md")

checks = {
    "r61_manifest_match": stamp["output_manifest_sha256"] ==
                          sha("R61_OUTPUT_MANIFEST.json"),
    "h3_protocol_hash_match": stamp["H3_prereg_sha256"] ==
                              sha("R61_H3_PREREGISTRATION.json"),
    "h4_protocol_hash_match": stamp["H4_prereg_sha256"] ==
                              sha("R61_H4_PREREGISTRATION.json"),
}

artifact_verification = {}
for tag in ("H3", "H4"):
    ok = bad = 0
    rows = []
    for it in pins[tag]["items"]:
        p = Path(it["path"])
        cur = fsha(p) if p.is_file() else "MISSING_OR_DIR"
        match = (cur == it.get("current_sha256"))
        rows.append({"path": it["path"], "hash_match": match})
        ok += 1 if match else 0
        bad += 0 if match else 1
    artifact_verification[tag] = {"verified": ok, "failed": bad,
                                  "rows": rows}

lock = {
    "schema": "R62_INPUT_LOCK_V1",
    "round": "OD0-R62",
    "package": pkg_name,
    "package_sha256": sha(pkg_name),
    "r61_stamp_pin": {
        "stamp_sha256": sha("R61_PROVENANCE_STAMP.json"),
        "commit_A": stamp["commit_A_prereg"],
        "commit_B": stamp["commit_B_outputs"],
        "checks": checks},
    "h3_protocol_verbatim": h3_protocol,
    "h4_protocol_verbatim": h4_protocol,
    "h3_protocol_sha256": stamp["H3_prereg_sha256"],
    "h4_protocol_sha256": stamp["H4_prereg_sha256"],
    "artifact_hash_verification_before_reading": artifact_verification,
    "state_class_rule": {
        "classes": ["UNIVERSAL_IDEAL_BY_LEVEL", "SCHEDULER_FOAM",
                    "RANDOM_IDEAL", "PROJECTION_ONLY", "OTHER"],
        "rule": "Quantitative clock-versus-clock or load-versus-count "
                "comparisons are adjudicated only when the tagged "
                "class has an exact arrow to the derived state class "
                "(random ideal of the throttled process). Otherwise "
                "STATE_CLASS_MISMATCH - neither contradiction nor "
                "confirmation; only definition-invariant properties "
                "(holding on every pair-closure ideal, derived from "
                "frozen theorems) may still be compared."},
    "diagnosis_paths": {
        "H3_saturation": "Any reported saturation of the load effect "
            "is classified at extraction, by definition, as "
            "ASYMPTOTIC_CLAIM (comparable to G3) or "
            "FINITE_EPOCH_DIFFERENCE (not comparable) before "
            "adjudication.",
        "H4_clock_ordering": "Any reported clock ordering opposite to "
            "C5 is first checked for normalization or functional "
            "differences (a mapping failure -> UNMAPPED) before it "
            "can count against C5."},
    "seals": {"BELL2_opened": False,
              "H1": "spent, not consulted", "H2": "spent, not "
              "consulted", "H5": {"parsed": False}},
    "declarations": [
        "no pattern from one corpus is used in the other's "
        "adjudication",
        "Tier D quantities, rates-versus-rounds, spatial claims "
        "excluded as sealed",
        "no round-number alignment; nothing added, moved, renamed, "
        "or repaired",
        "Part 4 readouts quarantined, never in a verdict",
        "hash hygiene: all hashes in-process"],
}
out = PKG / "R62_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("checks:", checks)
for tag in ("H3", "H4"):
    v = artifact_verification[tag]
    print(tag, "verified:", v["verified"], "failed:", v["failed"])
print("lock sha256:", sha("R62_INPUT_LOCK.json"))
