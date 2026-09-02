#!/usr/bin/env python3
"""OD0-R67 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r67_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


certs = json.loads((PKG / "R67_EXACT_CERTIFICATES.json").read_text(
    encoding="utf-8"))
workers = json.loads((PKG / "R67_WORKERS_RAW.json").read_text(
    encoding="utf-8"))

pa = {
    "schema": "R67_M8_COMPARISON_EXECUTION_V1",
    "protocol_hash_verified":
        "e0a94da19ad542d9658098b98f8dc38e2b66b58894c7ad65f6033fd712"
        "621da7",
    "part_A": A.PART_A,
    "in_round_certificates": {
        "A1": certs["partA_A1_cglmp"],
        "A2_quintic_roots": certs["partA_A2_quintic_roots"]},
    "independent_workers_raw": workers,
}
dump(PKG / "R67_M8_COMPARISON_EXECUTION.json", pa)

pb = {
    "schema": "R67_BRANCH_D_INTERFACE_V1",
    "part_B": A.PART_B,
    "certificates": {
        "gram_sectors": certs["partB_gram_sectors"],
        "m4_exact_check": certs["partB_m4_check"],
        "one_thirds": certs["partB_one_thirds"]},
}
dump(PKG / "R67_BRANCH_D_INTERFACE.json", pb)

results = {
    "schema": "OD0_R67_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "M8_BELL": A.VERDICTS["M8_BELL"],
    "BRANCH_D": A.VERDICTS["BRANCH_D"],
    "ONE_THIRD": A.VERDICTS["ONE_THIRD"],
    "targets_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R67_INPUT_LOCK.json"),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r68_recommendation": A.VERDICTS["r68_recommendation"],
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5": {"parsed": False}},
}
dump(PKG / "OD0_R67_RESULTS.json", results)

cx = """# OD0-R67 Counterexamples and corrections (append-only)

## CX-R67-1: in-round A1 assembly errors caught by the exactness
## discipline
The first in-round CGLMP assembly carried two index errors (a
plus-term at the wrong outcome difference; one enumeration
condition). The exact machinery itself exposed them BEFORE any
comparison: the deterministic local bound computed as 3 (impossible
for the standard form, whose bound is 2) and the value was
non-stationary. Corrected, the in-round computation gives
I_3 = 4/3 + (8/9) sqrt(3) exactly, and an independent worker
confirmed the identical value under the textbook phase gauge
((0, 1/2; 1/4, -1/4) with the CGLMP sign convention). Recorded as
a working note: the local bound is an effective checksum.

## CX-R67-2: precision of the frozen A2 phrasing
BELL1's 'S_infinity = the root of 16c^5 - 16c^3 + 2c^2 + 2c - 1'
is precisified: the quintic is the optimum's STATIONARITY
polynomial in c = cos(2 pi phi/3) (dS/dc = -(96/27) x quintic;
relevant root c* = 0.8889129786801, from the irreducible quartic
factor 8c^4 - 4c^3 - 6c^2 + 4c - 1); S itself satisfies the
irreducible quartic 531441 S^4 - 1574640 S^3 + 624024 S^2 -
25920 S - 115568 = 0 (531441 = 27^4), unique real root > 2. The
numeric value agrees to all frozen digits; no verdict affected.
"""
(PKG / "OD0_R67_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

report = f"""# OD0-R67 Report: The Sealed Comparison and Branch (d)

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.
M8_BELL: **{A.VERDICTS["M8_BELL"]}**.
BRANCH_D: **{A.VERDICTS["BRANCH_D"]}**.

## Gate discipline
The sealed M8 protocol was verified byte-unchanged before any Part A
work (hash in R67_INPUT_LOCK.json). Every Part A value was computed
independently - exact algebra in Q(sqrt 3), exhaustive enumerations,
and an extracted-readout re-derivation - never copied from the
frozen Bell reports.

## Part A - the five sealed items
A1 CGLMP: {A.PART_A["A1_CGLMP"]["verdict"]}.
{A.PART_A["A1_CGLMP"]["independent_standard"]}

A2 CHSH: {A.PART_A["A2_CHSH"]["verdict"]}.
{A.PART_A["A2_CHSH"]["independent_standard"]}
{A.PART_A["A2_CHSH"]["comparison"]}

A3 local bounds: {A.PART_A["A3_local_bounds"]["verdict"]}.

A4 non-maximal ceiling: {A.PART_A["A4_nonmaximal_ceiling"]["verdict"]}

A5 heralded branch: {A.PART_A["A5_heralded_branch"]["verdict"]}.
{A.PART_A["A5_heralded_branch"]["value_not_computed"]}

Non-comparisons: {A.PART_A["non_comparisons"]}

**Overall.** {A.PART_A["overall"]}

## Part B - the interface theorem
{json.dumps(A.PART_B["gram_sectors"], indent=1)[1:-1]}

**Verdict.** {A.PART_B["verdict_statement"]}

## The three appearances of 1/3
{json.dumps(A.PART_B["one_thirds"], indent=1)[1:-1]}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R67_RESULTS.json).

## R68
{A.VERDICTS["r68_recommendation"]}
"""
(PKG / "OD0_R67_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R67_REPORT.md", "OD0_R67_RESULTS.json",
         "OD0_R67_COUNTEREXAMPLES.md", "R67_INPUT_LOCK.json",
         "R67_M8_COMPARISON_EXECUTION.json",
         "R67_BRANCH_D_INTERFACE.json",
         "R67_EXACT_CERTIFICATES.json", "R67_WORKERS_RAW.json",
         "r67_exact.py", "r67_adjudication_data.py",
         "build_r67_outputs.py", "make_r67_lock.py"]
manifest = {"schema": "R67_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R67_OUTPUT_MANIFEST.json", manifest)
print("M8_BELL:", A.VERDICTS["M8_BELL"][:40])
print("manifest sha256:", sha(PKG / "R67_OUTPUT_MANIFEST.json"))
