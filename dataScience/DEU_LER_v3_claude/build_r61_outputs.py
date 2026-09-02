#!/usr/bin/env python3
"""OD0-R61 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r61_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


lock = json.loads((PKG / "R61_INPUT_LOCK.json").read_text(encoding="utf-8"))
certs = json.loads((PKG / "R61_EXACT_CERTIFICATES.json").read_text(
    encoding="utf-8"))
pins_sha = sha(PKG / "R61_ARTIFACT_PINS.json")

# ------------------------------------------- clock/relief derivations
claws = {
    "schema": "R61_CLOCK_FUNCTIONALS_AND_RELIEF_LINE_V1",
    "part2_C5_DERIVED": A.C5_DERIVED,
    "part4_G7_UPDATED_R61": A.G7_UPDATED_R61,
    "part4_relief_line": A.RELIEF_LINE,
    "certificates": certs,
    "adversarial_verification_note":
        "Part 2 and Part 4 derivations verified by a three-referee "
        "adversarial panel (independent derivation + simulation) "
        "before freezing; see OD0_R61_RESULTS.json for verdicts.",
}
dump(PKG / "R61_CLOCK_FUNCTIONALS_AND_RELIEF_LINE.json", claws)
c5_sha = hashlib.sha256(json.dumps(
    A.C5_DERIVED, indent=2, sort_keys=True).encode()).hexdigest()
g7_sha = hashlib.sha256(json.dumps(
    A.G7_UPDATED_R61, indent=2, sort_keys=True).encode()).hexdigest()

# ------------------------------------------- the two sealed protocols
h3 = {
    "schema": "R61_H3_PREREGISTRATION_V1",
    "corpus": "H3 (load-maturation projection family)",
    "status": "SEALED",
    "model_family": "R48 F5 (cosmology-projection): state field / "
                    "derived observable / external calibration / "
                    "phenomenological projection / fixed bridge "
                    "assumption / manuscript-only",
    "derived_side_table_G1_G8": [
        {"id": g[0], "statement": g[1], "class": g[2]}
        for g in A.H3_TABLE],
    "G7_UPDATED_R61": A.G7_UPDATED_R61,
    "G7_appendix_sha256": g7_sha,
    "protocol": A.PROTOCOL_RULE,
    "excluded_by_construction": A.EXCLUSIONS,
    "artifact_pins_sha256": pins_sha,
    "opening_rule": "R62 opens H3 under this sealed protocol, one "
                    "comparison, no repair; the v31o gap and the "
                    "DEU_voids SOURCE_CONFLICT carried at equal "
                    "prominence.",
}
dump(PKG / "R61_H3_PREREGISTRATION.json", h3)
h3_sha = sha(PKG / "R61_H3_PREREGISTRATION.json")

h4 = {
    "schema": "R61_H4_PREREGISTRATION_V1",
    "corpus": "H4 (clock-projection family)",
    "status": "SEALED",
    "model_family": "R48 F5 (cosmology-projection): state field / "
                    "derived observable / external calibration / "
                    "phenomenological projection / fixed bridge "
                    "assumption / manuscript-only",
    "derived_side_table_C1_C6": [
        {"id": c[0], "statement": c[1], "class": c[2]}
        for c in A.H4_TABLE],
    "C5_DERIVED": A.C5_DERIVED,
    "C5_appendix_sha256": c5_sha,
    "protocol": A.PROTOCOL_RULE,
    "excluded_by_construction": A.EXCLUSIONS,
    "artifact_pins_sha256": pins_sha,
    "opening_rule": "R62 opens H4 under this sealed protocol, one "
                    "comparison, no repair.",
}
dump(PKG / "R61_H4_PREREGISTRATION.json", h4)
h4_sha = sha(PKG / "R61_H4_PREREGISTRATION.json")

# ------------------------------------------------------------- results
pins = json.loads((PKG / "R61_ARTIFACT_PINS.json").read_text(
    encoding="utf-8"))
results = {
    "schema": "OD0_R61_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "components": dict(A.VERDICTS["components"],
                       H3_PREREG_HASH=h3_sha, H4_PREREG_HASH=h4_sha,
                       C5_appendix_sha256=c5_sha,
                       G7_appendix_sha256=g7_sha),
    "sections_4_to_6_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R61_INPUT_LOCK.json"),
    "artifact_summary": {
        "H3": pins["H3"]["summary"], "H4": pins["H4"]["summary"],
        "deu_voids_commit":
            pins["deu_voids_source_line"][
                "last_commit_touching_DEU_voids"],
        "v31": {k: v["status"]
                for k, v in pins["v31_generating_sources"].items()}},
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r62_recommendation": A.VERDICTS["r62_recommendation"],
    "seals": {"BELL2_opened": False,
              "H1": "spent (R54)", "H2": "spent (R57)",
              "H3": {"parsed": False}, "H4": {"parsed": False},
              "H5": {"parsed": False}},
    "panel_verdicts": A.PANEL_VERDICTS,
}
dump(PKG / "OD0_R61_RESULTS.json", results)

cx = """# OD0-R61 Counterexamples and corrections (append-only)

## CX-R61-1: registered co-embedding total order CORRECTED
The registered prediction placed both clock totals at n^{3/2} with the
containment clock ahead. Each new object contributes C(A,2) ~ A^2/2
co-embedding pairs (not A), so TCo(n) is n^2-scale (proven band
[c1 n^2, c2 n^2 ln n]) while TC(n) = (pi/2) n^{3/2} (1+o(1)); under
the frozen ln ln functionals the CO-EMBEDDING clock runs ahead, by
the additive constant ln(4/3) = 0.2877. Labeled witness: tau_Co -
tau_C = 0.265-0.276 at n ~ 50-80.

## CX-R61-2: R48 missing-artifact list partially stale
v31l, v31m, v31n generating sources were located on this machine
(DEU_voids sol_effort/face_value bundles; filenames pinned in
R61_ARTIFACT_PINS.json); only v31o remains missing. Recorded as a
correction to the carried missing-list; no content parsed.

## CX-R61-3: FORWARD ERRATUM to R59 T3 (and the R60 stamp headline)
The cone constant 3 pi/4 in R59 T3 is a mean-field artifact. The
descendant chain d_j is a rate-2 Yule process in log-time, so the
descendant fraction converges to n W/(n W + j^2) with W ~ Exp(1)
RANDOM; summing the ancestor law over j then carries the factor
E[sqrt(W)] = sqrt(pi)/2: E|cone(new at n)| = (3/8) pi^{3/2} sqrt(n)
(1+o(1)) ~ 2.0881 sqrt(n). Witnesses: exact-marginal chains of the
certified per-state law give E|cone|/sqrt(n) = 2.0936 +/- 0.0075 at
n = 16000 (35 SE below 3 pi/4 = 2.3562); the R59 exhaustive n = 9
value 6.165 vs 6.26 predicted vs 7.07 mean-field; DAG simulation
TC/n^{3/2} -> 1.3873 at n = 30000 (pi^{3/2}/4 = 1.3921, pi/2 =
1.5708). The Theta(sqrt n) ORDER of R59 T3 stands; only the sharp
constant is corrected. R59/R60 stay frozen; correction recorded
forward here (same convention as the R48 hash erratum). Secondary:
R59 T2's stated recursion omits composite j's own parent pair from
the non-descendant existing-pair count (+1; O(1/k^2) effect,
asymptotics unaffected; the fixed form reproduces R59's own
certified exact values 8/29 and 109/319 at n = 9).
"""
(PKG / "OD0_R61_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

report = f"""# OD0-R61 Report: H3/H4 Preregistration, Clock Functionals,
# and the Relief-Band Line

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.

## Position
R60 stamp and the M7 prediction hash pinned and verified. Sections 4-6
frozen verbatim at Commit A. H3-H5 sentinels parsed=false at start and
end; artifact pinning touched byte hashes and filenames only.

## The two sealed preregistrations
- **H3 (load maturation)**: derived-side table G1-G8 (6 THEOREM-grade
  rows) + G7_UPDATED_R61; sealed sha256 = {h3_sha}
- **H4 (clocks)**: derived-side table C1-C6 + C5_DERIVED appendix;
  sealed sha256 = {h4_sha}

Both exclude, by construction: Tier D quantities, rates versus rounds,
spatial/regional claims (UNMAPPED_INAPPLICABLE), calibrated
dictionaries. Mapping is by definition at opening; the model-family
caveat (R48 F5) is mandatory.

## Part 2 - C5_DERIVED (appendix sha256 = {c5_sha})
{A.C5_DERIVED["derivation"]["total_containment"]}

{A.C5_DERIVED["derivation"]["total_coembedding"]}

{A.C5_DERIVED["derivation"]["clock_functionals"]}

{A.C5_DERIVED["derivation"]["vs_tick_count"]}

## Part 3 - Artifacts
H3: 17/17 present, hashes unchanged, 9 non-manuscript artifacts (not
PAPER_ONLY). H4: 26/26 present, unchanged, 20 non-manuscript (not
PAPER_ONLY). DEU_voids source line pinned at commit
{results["artifact_summary"]["deu_voids_commit"]}
(SOURCE_CONFLICT recorded). v31l/m/n FOUND (correcting the carried
missing-list); v31o MISSING.

## Part 4 - The relief-band line (appendix sha256 = {g7_sha})
{A.G7_UPDATED_R61["statement"]}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R61_RESULTS.json).

## R62
{A.VERDICTS["r62_recommendation"]}
"""
(PKG / "OD0_R61_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R61_REPORT.md", "OD0_R61_RESULTS.json",
         "OD0_R61_COUNTEREXAMPLES.md", "R61_INPUT_LOCK.json",
         "R61_H3_PREREGISTRATION.json", "R61_H4_PREREGISTRATION.json",
         "R61_CLOCK_FUNCTIONALS_AND_RELIEF_LINE.json",
         "R61_ARTIFACT_PINS.json", "R61_EXACT_CERTIFICATES.json",
         "r61_exact.py", "r61_pins.py", "r61_adjudication_data.py",
         "build_r61_outputs.py", "make_r61_lock.py"]
manifest = {"schema": "R61_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R61_OUTPUT_MANIFEST.json", manifest)
print("H3 prereg sha256:", h3_sha)
print("H4 prereg sha256:", h4_sha)
print("C5 appendix sha256:", c5_sha)
print("G7 appendix sha256:", g7_sha)
print("manifest sha256:", sha(PKG / "R61_OUTPUT_MANIFEST.json"))
