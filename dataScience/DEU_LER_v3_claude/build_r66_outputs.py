#!/usr/bin/env python3
"""OD0-R66 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r66_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


certs = json.loads((PKG / "R66_EXACT_CERTIFICATES.json").read_text(
    encoding="utf-8"))

geo = {
    "schema": "R66_GEOMETRY_FREEZE_AND_DUALITY_V1",
    "G1_geometry_candidate": A.G1,
    "G2_duality": A.G2,
    "certificates": certs,
}
dump(PKG / "R66_GEOMETRY_FREEZE_AND_DUALITY.json", geo)

reg = {
    "schema": "R66_REGIONAL_INSTANTIATION_AND_FIELDS_V1",
    "R1_token_region": A.R1,
    "R2_R3": A.R2R3,
    "verdict": "REGIONAL_REQUIRES_PREMISE",
}
dump(PKG / "R66_REGIONAL_INSTANTIATION_AND_FIELDS.json", reg)

sl = {
    "schema": "R66_SCALING_LIMIT_AND_INVENTORY_V1",
    "S1_scaling_limit": A.S1,
    "S2_scope": A.S2,
    "I1_inventory": A.I1,
}
dump(PKG / "R66_SCALING_LIMIT_AND_INVENTORY.json", sl)

prereg = {
    "schema": "R66_M8_COMPARISON_PREREGISTRATION_V1",
    "status": "SEALED",
    "protocol": A.M8_PROTOCOL,
}
dump(PKG / "R66_M8_COMPARISON_PREREGISTRATION.json", prereg)
m8_sha = sha(PKG / "R66_M8_COMPARISON_PREREGISTRATION.json")

results = {
    "schema": "OD0_R66_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "components": dict(A.VERDICTS["components"],
                       M8_PREREG_HASH=m8_sha),
    "targets_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R66_INPUT_LOCK.json"),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r67_recommendation": A.VERDICTS["r67_recommendation"],
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5": {"parsed": False}},
}
dump(PKG / "OD0_R66_RESULTS.json", results)

cx = """# OD0-R66 Counterexamples and corrections (append-only)

## CX-R66-1: registered R1 DERIVABLE refuted
The registered prediction expected the token-region map derivable
via the smallest-prefix anchor of the formation record. Panel-exact
outcome: the common-prefix assignment is degenerate for every
object in both frozen catalogs (903/903 and 2304/2304 map to ROOT),
the nondegenerate majority functional is PARTIAL on the frozen
catalogs themselves (486/2304 pooled ties; 9 undefined all-root
profiles; per-factor variant undefined on 288 slots and
pair-valued), and the sources take region_mu as given everywhere
(zero home-region rules package-wide). R1 = REQUIRES_PREMISE; the
emended total candidate TR1' is recorded, not adopted; R2/R3 wait.

## CX-R66-2: R19 profile-shape claim corrected
The R65-carried description 'per factor root x2 + one depth-1 digit
x9-or-11' holds for 1296/2304 edit sets only; 1008 contain a
degenerate factor ({root:10, digit x1} or {root:11, no depth-1
edit}). Recorded; affects only the wording of the profile law, not
the choice-freedom of the profile lookup.
"""
(PKG / "OD0_R66_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

inv_counts = {}
for it in A.I1:
    c = it["cls"].split(" ")[0]
    inv_counts[c] = inv_counts.get(c, 0) + 1

report = f"""# OD0-R66 Report: Geometry Freeze and the M8 Preregistration

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.

## Position
R65 stamp pinned and verified. Targets and the protocol skeleton
frozen verbatim at Commit A. No comparison performed this round;
external values appear only as *names to be compared in R67* inside
the sealed protocol.

## G1 - the geometry candidate (frozen)
{A.G1["statement"]}

## G2 - the depth-grading duality (proven)
{A.G2["statement"]}

## R1 - token-region derivability: {A.R1["verdict"]}
{A.R1["statement"]}

Candidate premise (recorded, not adopted): {A.R1["candidate_premise"]}

R2/R3: {A.R2R3["status"]}

## S1 - the scaling-limit object
{json.dumps(A.S1["tuple"], indent=1)[1:-1]}

Exactness: {A.S1["exactness_summary"]}

## S2 - scope
{A.S2["scope"]}

## I1 - inventory ({len(A.I1)} entries)
Counts by bridge class: {json.dumps(inv_counts)}

{json.dumps(A.I1, indent=1)}

## The sealed M8 protocol
sha256 = {m8_sha}
Dictionary fixed (settings only); expected pattern declared
(EXACT_AGREEMENT on maximally entangled CGLMP/CHSH and local
bounds; RESTRICTION on the non-maximal ceiling); all other bridge
classes declared non-comparisons; the dark fraction FORBIDDEN
until its dictionary is preregistered.

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R66_RESULTS.json).

## R67
{A.VERDICTS["r67_recommendation"]}
"""
(PKG / "OD0_R66_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R66_REPORT.md", "OD0_R66_RESULTS.json",
         "OD0_R66_COUNTEREXAMPLES.md", "R66_INPUT_LOCK.json",
         "R66_GEOMETRY_FREEZE_AND_DUALITY.json",
         "R66_REGIONAL_INSTANTIATION_AND_FIELDS.json",
         "R66_SCALING_LIMIT_AND_INVENTORY.json",
         "R66_M8_COMPARISON_PREREGISTRATION.json",
         "R66_EXACT_CERTIFICATES.json", "r66_exact.py",
         "r66_adjudication_data.py", "build_r66_outputs.py",
         "make_r66_lock.py"]
manifest = {"schema": "R66_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R66_OUTPUT_MANIFEST.json", manifest)
print("M8 prereg sha256:", m8_sha)
print("manifest sha256:", sha(PKG / "R66_OUTPUT_MANIFEST.json"))
