#!/usr/bin/env python3
"""OD0-R63 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
from pathlib import Path

import r63_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


certs = json.loads((PKG / "R63_EXACT_CERTIFICATES.json").read_text(
    encoding="utf-8"))

structures = {
    "schema": "R63_DISTANCE_STRUCTURES_V1",
    "D1_classification": A.D1,
    "D4_locality_theorem": A.D4,
    "D5_carrier_support_locality": A.D5,
    "D6_bedrock": A.D6,
    "certificates": {
        "D1_witnesses": certs["D1_witnesses"],
        "D1_jaccard_triangle": certs["D1_jaccard_triangle_certificate"]},
    "adversarial_verification": A.PANEL,
}
dump(PKG / "R63_DISTANCE_STRUCTURES.json", structures)

scaling = {
    "schema": "R63_SCALING_AND_DIMENSION_V1",
    "D2_laws": A.D2,
    "D3_verdicts": A.D3,
    "primary": A.VERDICTS["primary"],
    "negative_result": A.VERDICTS["negative_result"],
    "readouts_labeled": certs["trajectory_geometry_labeled"],
    "Tdag_illustration": certs["Tdag_illustration"],
}
dump(PKG / "R63_SCALING_AND_DIMENSION.json", scaling)

results = {
    "schema": "OD0_R63_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "primary": A.VERDICTS["primary"],
    "components": A.VERDICTS["components"],
    "targets_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R63_INPUT_LOCK.json"),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "panel": A.PANEL,
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r64_recommendation": A.VERDICTS["r64_recommendation"],
    "seals": {"BELL2_opened": False, "H1_H4": "spent, not consulted",
              "H5": {"parsed": False}},
}
dump(PKG / "OD0_R63_RESULTS.json", results)

cx = """# OD0-R63 Counterexamples and corrections (append-only)

## CX-R63-1: the ultrametric inequality FAILS on pair-closure ideals
Witness (n = 8, exact): p = {a,ab}, q = {b,ab}, x = {a,p}, z = {b,q},
y = {p,q}. beta(x,y) = 3, beta(y,z) = 4, beta(x,z) = 2 (only {a,b,ab}
shared): d(x,z) = 6 > max(d(x,y), d(y,z)) = 5. Sharing breaks the
tree ultrametric. Both birth-index and depth variants fail.

## CX-R63-2: d_U fails even the ORDINARY triangle inequality
Witness (n = 13, exact): with p = {a,{a,ab}}, q = {b,{b,ab}} born
after half-time (births 8, 9): d(x,z) = 11 > 9 = d(x,y) + d(y,z).
d_U is classified NONE (a symmetric premetric).

## CX-R63-3: registered bedrock claims REFUTED (two)
(i) 'The bedrock is nearly totally ordered' - refuted: by exact
self-similarity its internal related fraction is (pi^{3/2}/2) m^{-1/2}
= Theta(n^{-1/4}) -> 0 (sparse self-similar partial order).
(ii) 'Every late object is within O(1) graph distance of the bedrock'
- refuted: the distance is Theta(log n) (greedy earlier-parent rate
exactly 3/2 log-units/step gives (1/3) ln n; BFS measured 0.289 ln n
at n = 1e7; lower bound from the base-8 volume law).

## CX-R63-4: the D3 trichotomy is INCOMPLETE
d_J between typical late objects realizes a fourth outcome: a
NONDEGENERATE bounded limit law (ratio-of-means 22/35 exactly, the
E[sqrt(W)] factor canceling; measured mean -> 0.627 at n = 2e5, sd
flattening at ~0.055, component fluctuation |cone|/sqrt(n) with limit
sd ~ 0.75). Not STABLE, not DRIFTING, not DEGENERATE. The registered
prediction (dJ DEGENERATE) is refuted; the frozen trichotomy is
refuted as exhaustive.

## CX-R63-5: pre-run constants corrected by the adversarial panel
(i) The cone-overlap integral is 13pi/32 = 1.2763, not 9pi/16 (my
pre-run slip); c_cap = 13 pi^{3/2}/64 = 1.1311; d_J ratio-of-means
= 1 - 13/35 = 22/35. (ii) The latest-common-ancestor scale is
n^{2/3}, not sqrt(n) (E[W^2] = 2 doubles the pair-ancestor density;
median beta/n^{2/3} ~ 1.0 stable across n = 1e3..1e5). (iii) The
interval bedrock-domination threshold is j = O(n^{1/4}), not
O(sqrt n). (iv) The greedy-descent constant to the bedrock is 1/3
ln n (2/3 ln n is the route to the primitives). (v) The max-depth
constant sharpens to c_max = 4.3111 (the frozen 2e ln n outer bound
holds), and the directed lower constant is c_min = 0.373365 - the
two roots of c(1 + ln 2 - ln c) = 1.
"""
(PKG / "OD0_R63_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

vt = A.VERDICTS["components"]
report = f"""# OD0-R63 Report: Geometry Stage Opening

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.
Primary: **GEOMETRY = {A.VERDICTS["primary"]}**.

## Position
R62 stamp pinned (verified). D1 inventory and D2-D6 frozen verbatim
at Commit A. R47 boundary retained. H5 sentinel parsed=false. Every
scaling derivation passed a three-referee adversarial panel before
freezing; five panel corrections recorded in the counterexamples.

## D1 - the canonical structures
- d_G: {A.D1["a_dG"]["class"]}. {A.D1["a_dG"]["statement"]}
- d_arrow: {A.D1["b_darrow"]["class"]}. {A.D1["b_darrow"]["statement"]}
- d_U: {A.D1["c_dU"]["class"]}. {A.D1["c_dU"]["statement"]}
- d_J: {A.D1["d_dJ"]["class"]}. {A.D1["d_dJ"]["statement"]}
- causal: {A.D1["e_causal"]["statement"]}
- R38: {A.D1["f_R38"]["statement"]}

## D2 - scaling laws
Diameters: {A.D2["diameters"]}

Ball volumes: {A.D2["ball_volume"]}

Intervals and ordering: {A.D2["intervals"]}

Unrelated fraction: {A.D2["unrelated_fraction"]}

Height structure: {A.D2["beta_law"]}

## D3 - the dimension question
- d_G: {A.D3["dG"]}
- d_arrow: {A.D3["darrow"]}
- d_U: {A.D3["dU"]}
- d_J: {A.D3["dJ"]}
- causal: {A.D3["causal"]}

## D4 - locality theorem: {A.D4["verdict"]}
{A.D4["statement"]}

## D5 - carrier-support locality: {A.D5["verdict"]}
{A.D5["statement"]}

## D6 - bedrock geometry: {A.D6["verdict"]}
{A.D6["statement"]}

## The negative result (equal prominence)
{A.VERDICTS["negative_result"]}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R63_RESULTS.json).

## R64
{A.VERDICTS["r64_recommendation"]}
"""
(PKG / "OD0_R63_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R63_REPORT.md", "OD0_R63_RESULTS.json",
         "OD0_R63_COUNTEREXAMPLES.md", "R63_INPUT_LOCK.json",
         "R63_DISTANCE_STRUCTURES.json",
         "R63_SCALING_AND_DIMENSION.json",
         "R63_EXACT_CERTIFICATES.json", "r63_exact.py",
         "r63_adjudication_data.py", "build_r63_outputs.py",
         "make_r63_lock.py"]
manifest = {"schema": "R63_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R63_OUTPUT_MANIFEST.json", manifest)
print("primary:", A.VERDICTS["primary"])
print("manifest sha256:", sha(PKG / "R63_OUTPUT_MANIFEST.json"))
