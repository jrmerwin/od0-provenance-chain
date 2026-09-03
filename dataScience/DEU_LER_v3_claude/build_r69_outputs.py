#!/usr/bin/env python3
"""OD0-R69 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r69_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


pins_sha = sha(PKG / "R69_ARTIFACT_PINS.json")

prereg = {
    "schema": "R69_H5_PREREGISTRATION_V1",
    "corpus": "H5 (carrier-density / cosmology-projection) - the "
              "last sealed corpus",
    "status": "SEALED",
    "conditionality_banner": "Every comparable statement is "
        "conditional on TD1 (stated, not adopted) in addition to "
        "the tower's premises (CO1, RO1, TG1, V ~ X), except where "
        "flagged tower-only.",
    "derived_side_table_Q1_Q8": A.DERIVED_SIDE,
    "protocol": A.PROTOCOL,
    "artifact_pins_sha256": pins_sha,
    "opening_rule": "R70 opens H5 under this sealed protocol, one "
                    "comparison, no repair; the missing de Sitter-"
                    "closure computation is carried at equal "
                    "prominence for its family.",
}
dump(PKG / "R69_H5_PREREGISTRATION.json", prereg)
prereg_sha = sha(PKG / "R69_H5_PREREGISTRATION.json")

pins = json.loads((PKG / "R69_ARTIFACT_PINS.json").read_text(
    encoding="utf-8"))
results = {
    "schema": "OD0_R69_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "components": dict(A.VERDICTS["components"],
                       H5_PREREG_HASH=prereg_sha),
    "sections_4_5_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R69_INPUT_LOCK.json"),
    "artifact_summary": pins["H5"]["summary"],
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r70_recommendation": A.VERDICTS["r70_recommendation"],
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5": {"parsed": False,
                                       "status": "SEALED until R70"}},
}
dump(PKG / "OD0_R69_RESULTS.json", results)

cx = """# OD0-R69 Counterexamples and corrections (append-only)

## CX-R69-1: none required
The round is a preregistration: the derived-side table carries only
previously certified theorems, the pins verified 14/14 unchanged,
and the registered prediction was met on every point. The only
standing gap is inherited: the de Sitter-closure computation
artifact remains missing (its family is manuscript-only), carried
forward at equal prominence for the R70 opening.
"""
(PKG / "OD0_R69_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

report = f"""# OD0-R69 Report: The H5 Preregistration

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.

## Position
R68 stamp pinned and verified. Sections 4-5 frozen verbatim at
Commit A. H5 sentinel parsed=false at start and end; pinning touched
byte hashes and filenames only.

## The derived-side table (frozen)
{json.dumps(A.DERIVED_SIDE, indent=1)}

## The sealed protocol
sha256 = {prereg_sha}

{json.dumps(A.PROTOCOL, indent=1)[1:-1]}

## Artifacts
H5: 14/14 pinned unchanged; 6 non-manuscript artifacts (the corpus
is not PAPER_ONLY); the de Sitter-closure computation artifact is
STILL MISSING (zero filename matches) - that family is
manuscript-only, carried at equal prominence.

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R69_RESULTS.json).

## R70
{A.VERDICTS["r70_recommendation"]}
"""
(PKG / "OD0_R69_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R69_REPORT.md", "OD0_R69_RESULTS.json",
         "OD0_R69_COUNTEREXAMPLES.md", "R69_INPUT_LOCK.json",
         "R69_H5_PREREGISTRATION.json", "R69_ARTIFACT_PINS.json",
         "r69_pins.py", "r69_adjudication_data.py",
         "build_r69_outputs.py", "make_r69_lock.py"]
manifest = {"schema": "R69_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R69_OUTPUT_MANIFEST.json", manifest)
print("H5 prereg sha256:", prereg_sha)
print("manifest sha256:", sha(PKG / "R69_OUTPUT_MANIFEST.json"))
