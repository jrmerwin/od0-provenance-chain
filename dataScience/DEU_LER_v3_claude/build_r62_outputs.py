#!/usr/bin/env python3
"""OD0-R62 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r62_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


raw = json.loads((PKG / "R62_EXTRACTION_RAW.json").read_text(
    encoding="utf-8"))
part4_sha = sha(PKG / "R62_PART4_READOUTS.json")

h3 = {
    "schema": "R62_H3_EXTRACTION_MAP_ADJUDICATION_V1",
    "corpus": "H3 (load maturation)",
    "part1_extraction": raw["H3"],
    "part2_state_classes": A.H3_STATE_CLASSES,
    "part2_map_table": A.H3_MAP_TABLE,
    "part2_saturation_classification": A.H3_SATURATION,
    "part3_tests_G1_G8": A.H3_TESTS,
    "part3_verdict": A.H3_VERDICT,
    "part4_quarantined_key": {
        "present": True, "file": "R62_PART4_READOUTS.json",
        "sha256": part4_sha,
        "label": "POST_OPENING_READOUT_NOT_ADJUDICATION"},
}
dump(PKG / "R62_H3_EXTRACTION_MAP_ADJUDICATION.json", h3)

h4 = {
    "schema": "R62_H4_EXTRACTION_MAP_ADJUDICATION_V1",
    "corpus": "H4 (clock projections)",
    "part1_extraction": raw["H4"],
    "part2_state_classes": A.H4_STATE_CLASSES,
    "part2_clock_functional_identity": A.H4_CLOCK_IDENTITY,
    "part2_map_table": A.H4_MAP_TABLE,
    "part3_tests_C1_C6": A.H4_TESTS,
    "part3_verdict": A.H4_VERDICT,
    "part4_quarantined_key": {
        "present": True, "file": "R62_PART4_READOUTS.json",
        "sha256": part4_sha,
        "label": "POST_OPENING_READOUT_NOT_ADJUDICATION"},
}
dump(PKG / "R62_H4_EXTRACTION_MAP_ADJUDICATION.json", h4)

results = {
    "schema": "OD0_R62_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "H3_COMPARISON": A.VERDICTS["H3_COMPARISON"],
    "H4_COMPARISON": A.VERDICTS["H4_COMPARISON"],
    "input_lock_sha256": sha(PKG / "R62_INPUT_LOCK.json"),
    "state_class_rule_recorded_at_commit_A": True,
    "clock_offset_adjudicated":
        A.H4_VERDICT["clock_offset_adjudicated"],
    "H3_map_counts": {
        "mapped_pattern_level": 4, "unmapped_inapplicable": 2,
        "unmapped_computable": 1, "state_class_mismatch": 4,
        "tierD_recorded_excluded": 1},
    "H4_map_counts": {
        "mapped": 4, "unmapped_inapplicable": 1,
        "excluded_rounds_or_tierD": 3, "state_class_mismatch": 5},
    "v31o": "missing; grav_geometry confirmation-round claims "
            "recorded as manuscript-only at equal prominence",
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r63_recommendation": A.VERDICTS["r63_recommendation"],
    "seals": {"BELL2_opened": False,
              "H1": "spent, not consulted", "H2": "spent, not "
              "consulted", "H3": "OPENED AND SPENT this round",
              "H4": "OPENED AND SPENT this round",
              "H5": {"parsed": False}},
}
dump(PKG / "OD0_R62_RESULTS.json", results)

cx = """# OD0-R62 Counterexamples and corrections (append-only)

## CX-R62-1: registered state-class guess for H3 registry inputs
The registered prediction expected the H3 registry-side inputs at
state class UNIVERSAL_IDEAL_BY_LEVEL; extraction shows them at
PROJECTION_ONLY (registry.py, the mu(a) pipelines) and
SCHEDULER_FOAM (the condensation foam). No adjudication consequence
(the mismatch handling is identical); recorded as a prediction
correction.

## CX-R62-2: one H3 saturation family classified ASYMPTOTIC
The registered prediction expected all H3 saturation claims to
classify FINITE_EPOCH_DIFFERENCE; the foam three-flow fixed-point /
limit-cycle family and the vacuum-paper dmax -> infinity maturity
claim classify ASYMPTOTIC_CLAIM by their stated definitions. They
sit on foam state classes (quantitative use blocked) and none
asserts a non-decaying lapse average, so G3 is untouched; recorded.
"""
(PKG / "OD0_R62_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

report = f"""# OD0-R62 Report: H3 and H4 Opened under Their Sealed
# Protocols

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.
Two comparisons, adjudicated separately, no repair.

## Gate discipline
Both protocol hashes and all 43 artifact hashes verified in-process
BEFORE any content was read (R62_INPUT_LOCK.json, Commit A). H5
sentinel parsed=false at start and end; H1/H2 not consulted.

## H3 (load maturation): **{A.VERDICTS["H3_COMPARISON"]}**

State classes: scheduler foams (conscription/v31 line, condensation
foam, grav_geometry engine), projections (registry bookkeeping,
mu(a)/S8/G pipelines, E6 statistical arm), and one non-DAG lattice
engine. No random-ideal state class appears.

{A.H3_VERDICT["basis"]}

Tests: {json.dumps(A.H3_TESTS, indent=1)[1:-1]}

Saturation routing: {A.H3_SATURATION["routing"]}

**Model-family caveat (mandatory).** {A.H3_VERDICT["model_family_caveat"]}

**v31o.** {A.H3_VERDICT["v31o_note"]}

## H4 (clock projections): **{A.VERDICTS["H4_COMPARISON"]}**

State classes: one universal-ideal-by-level engine (epoch_time.py -
the containment/co-embedding/clock computer), scheduler foams
(GR_QM engine and instrumentation), and projection pipelines
(41/40, spectral clock, Hubble screens, LIGO suite).

CLOCK FUNCTIONAL IDENTITY: {A.H4_CLOCK_IDENTITY["normalization"]}

{A.H4_VERDICT["basis"]}

Tests: {json.dumps(A.H4_TESTS, indent=1)[1:-1]}

**Model-family caveat (mandatory).** {A.H4_VERDICT["model_family_caveat"]}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R62_RESULTS.json).

## R63
{A.VERDICTS["r63_recommendation"]}
"""
(PKG / "OD0_R62_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R62_REPORT.md", "OD0_R62_RESULTS.json",
         "OD0_R62_COUNTEREXAMPLES.md", "R62_INPUT_LOCK.json",
         "R62_H3_EXTRACTION_MAP_ADJUDICATION.json",
         "R62_H4_EXTRACTION_MAP_ADJUDICATION.json",
         "R62_EXTRACTION_RAW.json", "R62_PART4_READOUTS.json",
         "r62_part4_readouts.py", "r62_adjudication_data.py",
         "build_r62_outputs.py", "make_r62_lock.py"]
manifest = {"schema": "R62_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R62_OUTPUT_MANIFEST.json", manifest)
print("H3:", A.VERDICTS["H3_COMPARISON"],
      "| H4:", A.VERDICTS["H4_COMPARISON"])
print("manifest sha256:", sha(PKG / "R62_OUTPUT_MANIFEST.json"))
