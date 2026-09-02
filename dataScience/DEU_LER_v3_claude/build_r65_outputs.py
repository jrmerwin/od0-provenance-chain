#!/usr/bin/env python3
"""OD0-R65 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r65_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


certs = json.loads((PKG / "R65_EXACT_CERTIFICATES.json").read_text(
    encoding="utf-8"))
raw = json.loads((PKG / "R65_EXTRACTION_RAW.json").read_text(
    encoding="utf-8"))

src = {
    "schema": "R65_CYLINDER_SOURCE_AND_RECORD_SPACE_V1",
    "P1_cylinder_source_structure": A.P1,
    "P2_record_space_distance": A.P2,
    "certificates": {
        "P2_ultrametric": certs["P2_ultrametric_certificate"]},
    "extraction_and_panel_raw": raw,
}
dump(PKG / "R65_CYLINDER_SOURCE_AND_RECORD_SPACE.json", src)

grow = {
    "schema": "R65_OCCUPIED_GROWTH_AND_MEASURES_V1",
    "P3_occupied_growth": A.P3,
    "P4_canonical_measures": A.P4,
    "panel_verdicts": A.PANEL,
    "certificates": {
        "P3_marker_orbit_arithmetic": certs["P3_marker_orbit"],
        "P3_chain_prefix_trajectories_labeled":
            certs["P3_chain_prefix_trajectories_labeled"],
        "P4_terminal_cells": certs["P4_terminal_cells"]},
}
dump(PKG / "R65_OCCUPIED_GROWTH_AND_MEASURES.json", grow)

results = {
    "schema": "OD0_R65_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "primary": A.VERDICTS["primary"],
    "components": A.VERDICTS["components"],
    "targets_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R65_INPUT_LOCK.json"),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r66_recommendation": A.VERDICTS["r66_recommendation"],
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5": {"parsed": False}},
}
dump(PKG / "OD0_R65_RESULTS.json", results)

cx = """# OD0-R65 Counterexamples and corrections (append-only)

## CX-R65-1: the reduced-word exponent log_3 2 REFUTED
The registered branching-2 law rested on the A13R 10-marker catalog;
the panel proved the catalog is a HARDCODED S_3 orbit of the
arbitrarily preregistered seed (0,1) ('fixed without inspecting a
response'), that repeat-digit markers are legal, that the no-repeat
condition is not gauge-invariant under CD1I's per-frame cyclic
origins, and that the declared odometer order 3^D forces a single
cycle through ALL words. The record tree is the full ternary tree:
delta = 1 exactly, STABLE. The package-carried 'branching at most 2
by the two-parent structure' does not apply to the word tree.

## CX-R65-2: registered DISJOINT_UNION refuted
The source record identity carries no event index; equal prefix
symbols use the same record state (LERF2). The record space is ONE
exact ultrametric tree (certified: 7,971,964 triples, zero
violations). The event-indexed disjoint union is the round-level
counting picture (R50), recorded as such.

## CX-R65-3: registered 'no canonical object transport' refuted
Every A12 edit carries a content-determined anchor region; the
object-to-region-multiset profile is a frozen-data lookup, verified
schedule-invariant on all 903 catalog graphs. What fails is a single
canonical cylinder per object, not the transport.

## CX-R65-4: package-carried source premises corrected (three)
(i) 'why 8': no 8-region enumeration exists in the frozen package -
the A13R catalog has 10 hardcoded markers and the A12 anchors span
40 regions (all prefixes to depth 3, including repeat cells);
(ii) the Prufer-3-group / Pontryagin-dual FOOTNOTE is absent from
source (the direct-limit structure itself is declared exactly as
carried);
(iii) per-region five-integer ledgers and per-region clocks are
DECLARED at UEQ0 spec level with a product master kernel - the R52
JOINT_ONLY designation describes the frozen catalog's
ROOT-instantiation, not the spec.
"""
(PKG / "OD0_R65_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

report = f"""# OD0-R65 Report: Branch (c) - The Prefix-Cylinder Tree

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.
Primary: **{A.VERDICTS["primary"]}**.

## Position
R64 stamp pinned and verified. Targets P1-P4 and the branch record
frozen verbatim at Commit A. Source extraction by a five-agent
workflow with file+line citations; derivations verified by a
two-referee adversarial panel that REFUTED the registered exponent
before it could freeze.

## P1 - cylinder source structure
Region definition: {A.P1["region_definition"]}

Why 8 (corrected): {A.P1["why_8"]}

Regional ledgers (finding): {A.P1["regional_ledgers"]}

Maps: {json.dumps(A.P1["maps"], indent=1)[1:-1]}

Letter semantics: {A.P1["letter_semantics"]}

Clock tower: {A.P1["prufer_note"]}

## P2 - record-space distance
{A.P2["structure"]}

{A.P2["round_level_note"]}

Readability: {A.P2["readability"]}

## P3 - occupied growth and the exponent
{A.P3["law"]}

Exponent: {A.P3["exponent"]}

Two trees: {A.P3["two_trees_note"]}

## P4 - canonical measures and the trichotomy
W: {A.P4["W_list"]}

Transport: {A.P4["transport"]}

Trichotomy: {A.P4["trichotomy"]}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R65_RESULTS.json).

## R66
{A.VERDICTS["r66_recommendation"]}
"""
(PKG / "OD0_R65_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R65_REPORT.md", "OD0_R65_RESULTS.json",
         "OD0_R65_COUNTEREXAMPLES.md", "R65_INPUT_LOCK.json",
         "R65_CYLINDER_SOURCE_AND_RECORD_SPACE.json",
         "R65_OCCUPIED_GROWTH_AND_MEASURES.json",
         "R65_EXACT_CERTIFICATES.json", "R65_EXTRACTION_RAW.json",
         "r65_exact.py", "r65_adjudication_data.py",
         "build_r65_outputs.py", "make_r65_lock.py"]
manifest = {"schema": "R65_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R65_OUTPUT_MANIFEST.json", manifest)
print("primary:", A.VERDICTS["primary"])
print("manifest sha256:", sha(PKG / "R65_OUTPUT_MANIFEST.json"))
