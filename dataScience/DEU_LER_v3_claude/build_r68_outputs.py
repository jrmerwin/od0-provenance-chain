#!/usr/bin/env python3
"""OD0-R68 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r68_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


certs = json.loads((PKG / "R68_EXACT_CERTIFICATES.json").read_text(
    encoding="utf-8"))
workers = json.loads((PKG / "R68_WORKERS_RAW.json").read_text(
    encoding="utf-8"))

dump(PKG / "R68_ASSIGNMENT_CLASS.json", {
    "schema": "R68_ASSIGNMENT_CLASS_V1",
    "part1_table": A.PART1,
    "workers_raw": [w for w in workers
                    if w["worker"] == "Y1_candidates"]})

dump(PKG / "R68_REGION_SET_AND_PROCESS.json", {
    "schema": "R68_REGION_SET_AND_PROCESS_V1",
    "RS1_RS3": A.RS,
    "certificates": {"RS2": certs["RS2_product_kernel"]}})

dump(PKG / "R68_FIELDS_ON_THE_TREE.json", {
    "schema": "R68_FIELDS_ON_THE_TREE_V1",
    "F1_F5": A.FIELDS,
    "certificates": {
        "F4": certs["F4_per_region_duality"],
        "F1_F3_occupancy": certs["F1_F3_occupancy"]},
    "workers_raw": [w for w in workers if w["worker"] == "Y2_fields"]})

dump(PKG / "R68_PREMISE_AND_H5_CANDIDATES.json", {
    "schema": "R68_PREMISE_AND_H5_CANDIDATES_V1",
    "premise": A.PREMISE})

results = {
    "schema": "OD0_R68_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "components": A.VERDICTS["components"],
    "targets_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R68_INPUT_LOCK.json"),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r69_recommendation": A.VERDICTS["r69_recommendation"],
    "seals": {"BELL2_scientific_content_reopened": False,
              "H1_H4": "spent", "H5": {"parsed": False}},
}
dump(PKG / "OD0_R68_RESULTS.json", results)

cx = """# OD0-R68 Counterexamples and corrections (append-only)

## CX-R68-1: the R66-recorded TR1' is not the minimal premise
The frozen minimality order (readability, covariance, #tie-break
clauses) selects T-DEEP in its uniform zero-clause form
T(x) = common_prefix(argmax-depth anchor cells): readability and
covariance tie across survivors, and the clause count is 0 (T-DEEP)
< 1 (plurality) < 2 (TR1'). TR1' is exactly T-DEEP's depth-1
truncation on the whole 903-catalog (894/894 both-localized; T-DEEP
strictly deeper on 624). The registered prediction (TR1'
UNIQUE_MINIMAL, coinciding with R66) is corrected.

## CX-R68-2: the registered 'no other candidate' is false
Full-anchor-multiset plurality (strict-max cell; tie -> ROOT) is a
third total, choice-free, covariant, schedule-invariant,
non-degenerate candidate (non-ROOT 0.538 / 0.375 on the two
catalogs). It ranks third. T-LAST is rejected outright: the
catalogs freeze no occurrence order (hash-sorted lists; compilation
conventions), and re-serialization moves it on 154/903 and
1058/2304 objects.

## CX-R68-3: two field-side slips caught by the referee
(i) The in-prompt congestion composite '9 Gamma / (min share)'
double-applies the 9: the correct threshold is N > Gamma/s_rho,
giving full-fixture congestion at 9 Gamma in the mature limit.
(ii) 'Root gets depth-0 symbols + ...' overstated: s_ROOT = q0
exactly - no deeper cylinder charges past its depth-1 ancestor.
Consequence, missed by the registered picture: at maturity the
fixture EQUALIZES the nine non-root regions (simultaneous
congestion at N = 9 Gamma) and leaves ROOT permanently free.
"""
(PKG / "OD0_R68_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

report = f"""# OD0-R68 Report: The Token-Region Premise Round

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.

## Position
R67 stamp pinned and verified. TR1' copied verbatim; the class T and
all targets frozen at Commit A. Candidate tests and field laws
referee-computed on the frozen catalogs (exact; raw in
R68_WORKERS_RAW.json).

## Part 1 - the assignment class
{json.dumps(A.PART1, indent=1)[1:-1]}

## Part 2 - region set and process
{json.dumps(A.RS, indent=1)[1:-1]}

## Part 3 - fields on the record tree
{json.dumps(A.FIELDS, indent=1)[1:-1]}

## Part 4 - the premise
{A.PREMISE["statement_A13R0_form"]}

Coincides with the R66 record: {A.PREMISE["coincides_with_R66_record"]}

H5 derived-side candidates (target-blind):
{json.dumps(A.PREMISE["H5_derived_side_candidates"], indent=1)}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R68_RESULTS.json).

## R69
{A.VERDICTS["r69_recommendation"]}
"""
(PKG / "OD0_R68_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R68_REPORT.md", "OD0_R68_RESULTS.json",
         "OD0_R68_COUNTEREXAMPLES.md", "R68_INPUT_LOCK.json",
         "R68_ASSIGNMENT_CLASS.json",
         "R68_REGION_SET_AND_PROCESS.json",
         "R68_FIELDS_ON_THE_TREE.json",
         "R68_PREMISE_AND_H5_CANDIDATES.json",
         "R68_EXACT_CERTIFICATES.json", "R68_WORKERS_RAW.json",
         "r68_exact.py", "r68_adjudication_data.py",
         "build_r68_outputs.py", "make_r68_lock.py"]
manifest = {"schema": "R68_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R68_OUTPUT_MANIFEST.json", manifest)
print("premise:", A.VERDICTS["components"]["TR1_PRIME_STATUS"][:50])
print("manifest sha256:", sha(PKG / "R68_OUTPUT_MANIFEST.json"))
