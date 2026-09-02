#!/usr/bin/env python3
"""OD0-R64 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r64_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


certs = json.loads((PKG / "R64_EXACT_CERTIFICATES.json").read_text(
    encoding="utf-8"))

gates = {
    "schema": "R64_GATE_CLASSIFICATION_V1",
    "per_gate_table": A.TABLE,
    "certificates": certs,
    "notes": [
        "The engine's reachability SUSTAINS entries are exhaustive to "
        "the n = 9 cap; REC2's entry is superseded by the exact "
        "finite-universe theorem (recorded in the table).",
        "One exploratory referee conjunction outside G was excluded "
        "from the class and the verdict (HC1)."],
}
dump(PKG / "R64_GATE_CLASSIFICATION.json", gates)

nogo = {
    "schema": "R64_NO_GO_AND_COROLLARIES_V1",
    "no_go": A.NO_GO,
    "ancestry_gated_corollary": A.COROLLARY_REL,
    "readable_vs_constructor_note": "Every gate in G except the "
        "graph-distance family is READABLE (a function of the fact "
        "graph S on recorded structure): the locality class is, "
        "almost entirely, a class of statements about what the "
        "recorded universe can see; the d_G-family gates are MIXED "
        "because leaf shortcuts are invisible to S (R63 D7). "
        "Recorded, not interpreted.",
}
dump(PKG / "R64_NO_GO_AND_COROLLARIES.json", nogo)

results = {
    "schema": "OD0_R64_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "primary": A.VERDICTS["primary"],
    "components": A.VERDICTS["components"],
    "G_and_no_go_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R64_INPUT_LOCK.json"),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r65_recommendation": A.VERDICTS["r65_recommendation"],
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5": {"parsed": False}},
}
dump(PKG / "OD0_R64_RESULTS.json", results)

cx = """# OD0-R64 Counterexamples and corrections (append-only)

## CX-R64-1: registered gate-class guesses refuted (four)
(i) UNREL does not resemble ALL from genesis: exact witness -
permanent deadlock at n = 3 (both absent pairs are related through
ab); it sustains only from a 7-object seed with incomparable pairs.
(ii) LEAF1's spectral base is (5 + sqrt(41))/2 = 5.7016 (two-type
operator: lambda A = 4(A+C), lambda C = 2A + C), not 4: chain links
interact multiplicatively with the uniform bridges (measured shell
ratios 4.02-4.07 at n = 1e7, above 4 and rising). Stronger: the
leaf count is pathwise non-increasing and equals exactly 1 past
genesis.
(iii) MINCOST at Gamma >= 3 is exponentially ENHANCED, not
clustered-drifting: pair costs on the served ensemble are
birth-dominated (Theta(1) relative spread - the D9 late-pair
concentration does not transfer), the gate persistently fires
top-2-earliest-born pairs (0.60/0.50/0.43 at Gamma = 3/4/5, flat),
and the exact operator gives rho = 48/5, 384/35, 256/21 - above 8,
growing in Gamma; d_J shifts toward SMALLER overlap (0.627 ->
0.70-0.76).
(iv) PC/GP/COUSIN1/DG2 are exponential small worlds, not uniformly
'tree-like or chain-like'; the class's true chains are SIB from
its minimal seed, SIB_AND_LEAF1, and DG2_AND_LEAF1.

## CX-R64-2: the ancestry-gated cost law is neither of the two
## candidates
The package-carried Theta(ln n) AND the pre-run polynomial guess
are both refuted: under REL, ln chains = Theta(sqrt(log n)) with
lineage fixed point kappa = pi/sqrt(3) = 1.814 (local exponents
decline as a/(2 sqrt(ln n)), matching measurement across four
runs); cost = exp(Theta(sqrt(log n))) = n^{o(1)} but
omega(polylog); growth |X(T)| = T^{1-o(1)}.

## CX-R64-3: the frozen no-go route (i) corrected
'One parent uniform over Theta(n) with probability >= c' gives
rho >= 4c by kernel comparison - proving rho > 1 only for
c > 1/4. The conclusion holds for every c bounded below via the
bridging bound rho >= 1 + Theta(c) (measured base 2.13 at
c = 0.1, 1.39 at c = 0.02), with the hypothesis strengthened to
uniformity over all objects (or a time-representative set).

## CX-R64-4: a seed-dependent geometry class
SIB is the class's only gate whose structure type depends on the
seed: from its minimal 4-object seed it is a DETERMINISTIC forced
chain t_{k+1} = {t_{k-1}, t_k} with exactly one fireable pair at
every step (exponent 1); from richer seeds the eligible-pair
count is Theta(n) and the process is an exponential tree.
Recorded as a finding about gate/seed coupling.
"""
(PKG / "OD0_R64_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

vt = A.VERDICTS["components"]
report = f"""# OD0-R64 Report: The Locality Premise Class

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.
Primary: **{A.VERDICTS["primary"]}**.

## Position
Both R63 stamps pinned and verified. The gate class G (25 members)
and the no-go statement frozen verbatim at Commit A. Six-referee
adversarial panel + exhaustive gated reachability before freezing.

## The no-go theorem
{A.NO_GO["statement"]}

Route (i), corrected: {A.NO_GO["route"]["i_corrected"]}

Route (ii), the engine of the proof: {A.NO_GO["route"]["ii_corrected"]}

Route (iii): {A.NO_GO["route"]["iii_corrected"]}

**The negative result (equal prominence).** {A.NO_GO["negative_result"]}

Honest gaps: {A.NO_GO["honest_gaps"]}

## Per-gate table
{json.dumps(A.TABLE, indent=1)}

## The ancestry-gated tower (corollary, not adopted)
{A.COROLLARY_REL["laws"]}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R64_RESULTS.json).

## R65
{A.VERDICTS["r65_recommendation"]}
"""
(PKG / "OD0_R64_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R64_REPORT.md", "OD0_R64_RESULTS.json",
         "OD0_R64_COUNTEREXAMPLES.md", "R64_INPUT_LOCK.json",
         "R64_GATE_CLASSIFICATION.json",
         "R64_NO_GO_AND_COROLLARIES.json",
         "R64_EXACT_CERTIFICATES.json", "r64_exact.py",
         "r64_adjudication_data.py", "build_r64_outputs.py",
         "make_r64_lock.py"]
manifest = {"schema": "R64_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R64_OUTPUT_MANIFEST.json", manifest)
print("primary:", A.VERDICTS["primary"])
print("manifest sha256:", sha(PKG / "R64_OUTPUT_MANIFEST.json"))
