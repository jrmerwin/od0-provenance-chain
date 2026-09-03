#!/usr/bin/env python3
"""OD0-R70 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r70_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


raw = json.loads((PKG / "R70_EXTRACTION_RAW.json").read_text(
    encoding="utf-8"))

ema = {
    "schema": "R70_H5_EXTRACTION_MAP_ADJUDICATION_V1",
    "part1_extraction_raw": raw,
    "part2_state_classes": A.STATE_CLASSES,
    "part2_pre_committed_classifications": A.CLASSIFICATIONS,
    "part2_map_table": A.MAP_TABLE,
    "part3_tests_Q1_Q8": A.TESTS,
    "part3_verdict": A.VERDICT,
    "part4_quarantined_archive_only": A.PART4,
}
dump(PKG / "R70_H5_EXTRACTION_MAP_ADJUDICATION.json", ema)

results = {
    "schema": "OD0_R70_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "H5_COMPARISON": A.VERDICTS["H5_COMPARISON"],
    "Q8_TOUCHED": A.VERDICTS["Q8_TOUCHED"],
    "SEALED_CORPORA_REMAINING": A.VERDICTS["SEALED_CORPORA_REMAINING"],
    "MAP_TABLE_counts": {
        "mapped_pattern_level": 3, "unmapped_inapplicable": 2,
        "fraction_of_total_recorded": 1, "tierD_manuscript_only": 1,
        "state_class_mismatch_quantitative": 3,
        "excluded_rounds": 1},
    "DESTRUCTION_MECHANISM": "yes (counts nondecreasing)",
    "input_lock_sha256": sha(PKG / "R70_INPUT_LOCK.json"),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r71_recommendation": A.VERDICTS["r71_recommendation"],
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5": "OPENED AND SPENT this round"},
}
dump(PKG / "OD0_R70_RESULTS.json", results)

cx = """# OD0-R70 Counterexamples and corrections (append-only)

## CX-R70-1: extraction-level state-class tags re-adjudicated
The extraction agents tagged the H5 activation-foam engines
RANDOM_IDEAL (they are stochastically grown). The mapping
re-adjudicated: a 1 -> 3 face-replacement grammar with face
consumption has no pair-closure/two-parent structure and hence no
exact arrow to the derived state (the pair-closure random ideal
under TD1); for the state-class rule they sit in the
scheduler-foam family. Both the raw tags and the mapping decision
are part of the record; no verdict was affected (the gate blocked
quantitative comparison either way).

## CX-R70-2: none further
The carried registered prediction was met on every point; no FAIL
diagnosis was triggered; Q8 was not touched. The standing gap is
inherited and carried at equal prominence: the de Sitter-closure
computation artifact remains missing (manuscript-only family).
"""
(PKG / "OD0_R70_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

report = f"""# OD0-R70 Report: The Last Seal

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.
H5_COMPARISON: **{A.VERDICTS["H5_COMPARISON"]}**.
Sealed corpora remaining: **0**.

## Gate discipline
The sealed R69 protocol was verified byte-unchanged and all 14
artifact hashes verified in-process BEFORE any content was read
(R70_INPUT_LOCK.json, Commit A). H1-H4 not consulted. Q8 not
touched.

## State classes
{A.STATE_CLASSES["note"]}

{A.STATE_CLASSES["consequence"]}

## Pre-committed classifications
{json.dumps(A.CLASSIFICATIONS, indent=1)[1:-1]}

## The map
{json.dumps(A.MAP_TABLE, indent=1)}

## Tests
{json.dumps(A.TESTS, indent=1)[1:-1]}

## Verdict
{A.VERDICT["basis"]}

**Model-family caveat (mandatory).** {A.VERDICT["model_family_caveat"]}

## Quarantined archive (not adjudication)
{json.dumps(A.PART4, indent=1)[1:-1]}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R70_RESULTS.json).

## R71
{A.VERDICTS["r71_recommendation"]}
"""
(PKG / "OD0_R70_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R70_REPORT.md", "OD0_R70_RESULTS.json",
         "OD0_R70_COUNTEREXAMPLES.md", "R70_INPUT_LOCK.json",
         "R70_H5_EXTRACTION_MAP_ADJUDICATION.json",
         "R70_EXTRACTION_RAW.json",
         "r70_adjudication_data.py", "build_r70_outputs.py",
         "make_r70_lock.py"]
manifest = {"schema": "R70_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R70_OUTPUT_MANIFEST.json", manifest)
print("H5_COMPARISON:", A.VERDICTS["H5_COMPARISON"],
      "| sealed remaining:", A.VERDICTS["SEALED_CORPORA_REMAINING"])
print("manifest sha256:", sha(PKG / "R70_OUTPUT_MANIFEST.json"))
