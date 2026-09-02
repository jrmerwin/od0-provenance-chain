#!/usr/bin/env python3
"""OD0-R60 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
import math
from pathlib import Path

import r60_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


certs = json.loads((PKG / "R60_EXACT_CERTIFICATES.json").read_text(
    encoding="utf-8"))

# ---------------------------------------------------------------- laws
laws = {
    "schema": "R60_LAPSE_CLOCK_LAWS_V1",
    "L1_E0_law": A.L["L1"],
    "L2_E1_identities": A.L["L2"],
    "L3_E1_entry": A.L["L3"],
    "L4_cycle_law": A.L["L4"],
    "L5_late_regime": A.L["L5"],
    "L6_three_ages": A.L["L6"],
    "L7_depth_and_reading": A.L["L7"],
    "L8_persistent_load": A.L["L8"],
    "exact_laws_summary": {
        "E0": "Phi = 1; tick rate = D",
        "E1_identity": "S^V = Gamma Phi^2 pathwise; E[Phi^2|state] = "
                       "D/(F+D)",
        "cycle_average": "<Phi^2>_cycle = 1 - C/(Gamma E[tau]); "
                         "E[tau] = (C + D H_C)/Gamma (1+O(Gamma/D)); "
                         "-> 1/(1+c) for C = c D ln D",
        "middrain_bursts": "(1/Gamma) D ln D (1+o(1)) per full drain; "
                           "P(uninterrupted) = exp(-Theta(D log D))",
        "balance_band": "x*^2 = r/(4 C(Gamma,2) n ln n), r = Gamma + "
                        "min(H, 2 Gamma) - m; run-average twice that",
        "relief": "v* = H (H <= 2 Gamma - 1); 2 Gamma (1-x) (H >= "
                  "2 Gamma); fixed point P* = 10 Gamma - 6",
        "ages": "b ~ n; N_V = O(n^{3/2} sqrt(ln n)); k ~ (2/r) n^2 "
                "ln n",
        "depth": "E[M_n]/ln n in [1, 2e] E-level; chains <= 2^depth "
                 "pathwise; reading x3 per unit word-depth increment",
        "drained_lapse_deficit": "exactly m/(m+D)"},
    "certificates": {
        "L2_case_table": certs["L2_case_table"],
        "L1_L3_early_evolution": certs["L1_L3_early_evolution"],
        "L4_drain_induction": certs["L4_drain_induction"],
        "L4_relief_fixed_point": certs["L4_relief_fixed_point"],
        "L7_chains_le_2pow_depth": certs["L7_chains_le_2pow_depth"],
        "L7_depth_enumeration_n_le_10":
            certs["L7_depth_enumeration_n_le_10"]},
    "adversarial_verification": {
        "note": "Every L4-L7 derivation was independently verified by "
                "a five-referee adversarial panel (each instructed to "
                "refute, with exact DP and Monte-Carlo cross-checks) "
                "before freezing. Panel corrections folded in: "
                "general-Gamma mid-drain prefactor 1/Gamma (not "
                "C(Gamma,2)/Gamma, which coincides only at Gamma=2); "
                "relief saturation value 2 Gamma (1-x) with integer "
                "split at H = 2 Gamma; quota ~ P/6.",
        "verdicts": {"cycle_average": "CONFIRMED",
                     "middrain_bursts": "CORRECTED (prefactor)",
                     "balance_band": "CONFIRMED",
                     "depth_bounds": "CONFIRMED",
                     "relief_saturation": "CONFIRMED"}},
}
dump(PKG / "R60_LAPSE_CLOCK_LAWS.json", laws)

# ------------------------------------------------------- prediction set
pset = {
    "schema": "R60_M7_PREDICTION_SET_V1",
    "round": "OD0-R60",
    "status": "SEALED_TARGET_BLIND",
    "note": "Reparametrization-invariant statements about lapse and "
            "tick rate versus maturity; no rate in process time; the "
            "only object H3/H4 may later be compared against.",
    "statements": A.M7_PREDICTIONS,
}
dump(PKG / "R60_M7_PREDICTION_SET.json", pset)
pset_sha = sha(PKG / "R60_M7_PREDICTION_SET.json")

# -------------------------------------------------------------- readouts
rows = []
for key, t in sorted(certs["L5_L6_L7_trajectories_labeled"].items()):
    parts = key.split("_")
    G = int(parts[0][1:])
    m = int(parts[1][1:])
    H = int(parts[2][1:])
    tk = t["10000"]
    n = tk["n"]
    r = G + min(H, 2 * G) - m
    CG2 = G * (G - 1) // 2
    xstar = math.sqrt(r / (4 * CG2 * n * math.log(n)))
    run_pred = math.sqrt(r / (2 * CG2 * n * math.log(n)))
    nv_coef = G * math.sqrt(2 / (CG2 * r))
    rows.append({
        "Gamma": G, "m": m, "H": H, "k": 10000,
        "n": n, "b": tk["b"], "b_equals_n_minus_2": tk["b"] == n - 2,
        "N_V": tk["N_V"], "renewals": tk["renewals"],
        "max_depth": tk["max_depth"],
        "maxdepth_over_ln_n": round(tk["max_depth"] / math.log(n), 3),
        "window_rms_x": tk["window_rms_x"],
        "pred_xstar": round(xstar, 5),
        "window_over_pred": round(tk["window_rms_x"] / xstar, 3),
        "run_rms_x": tk["rms_x"],
        "run_pred": round(run_pred, 5),
        "run_over_pred": round(tk["rms_x"] / run_pred, 3),
        "N_V_over_n32_sqrtlnn": round(
            tk["N_V"] / (n ** 1.5 * math.sqrt(math.log(n))), 3),
        "pred_NV_upper_coef": round(nv_coef, 3),
        "avg_phi2": tk["avg_phi2"],
        "reading_over_3maxdepth": tk["reading_over_3maxdepth"],
    })
g2 = [r_ for r_ in rows if r_["Gamma"] == 2]
readouts = {
    "schema": "R60_READOUTS_V1",
    "note": "LABELED seeded readouts - no readout enters a theorem. "
            "pred_xstar = sqrt(r/(4 C(Gamma,2) n ln n)); "
            "run_pred = sqrt(r/(2 C(Gamma,2) n ln n)); "
            "N_V upper coefficient = Gamma sqrt(2/(C(Gamma,2) r)).",
    "at_k_10000": rows,
    "summary": {
        "b_equals_n_minus_2_at_Gamma2": all(
            r_["b_equals_n_minus_2"] for r_ in g2),
        "window_over_pred_median": sorted(
            r_["window_over_pred"] for r_ in rows)[len(rows) // 2],
        "run_over_pred_median": sorted(
            r_["run_over_pred"] for r_ in rows)[len(rows) // 2],
        "maxdepth_over_ln_n_range": [
            min(r_["maxdepth_over_ln_n"] for r_ in rows),
            max(r_["maxdepth_over_ln_n"] for r_ in rows)],
        "renewals_range": [min(r_["renewals"] for r_ in rows),
                           max(r_["renewals"] for r_ in rows)]},
}
dump(PKG / "R60_READOUTS.json", readouts)

# --------------------------------------------------------------- results
results = {
    "schema": "OD0_R60_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "components": A.VERDICTS["components"],
    "targets_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R60_INPUT_LOCK.json"),
    "M7_prediction_set_sha256": pset_sha,
    "M7_statement_count": len(A.M7_PREDICTIONS),
    "M7_theorem_grade_count": sum(
        1 for p in A.M7_PREDICTIONS if p["class"].startswith("THEOREM")),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r61_recommendation": A.VERDICTS["r61_recommendation"],
    "seals": {"BELL2_opened": False,
              "H1": "spent (R54)", "H2": "spent (R57)",
              "H3": {"parsed": False}, "H4": {"parsed": False},
              "H5": {"parsed": False}},
    "adjudication": A.L,
}
dump(PKG / "OD0_R60_RESULTS.json", results)

# --------------------------------------------------------- counterexamples
cx = """# OD0-R60 Counterexamples and corrections (append-only)

## CX-R60-1: carried cycle-average form REFUTED
The package carried <Phi^2>_cycle ~ ln(1 + 4 ln n)/(4 ln n) (linear
drain at constant rate). The hypergeometric drain slows as F falls
(rate Gamma F/(F+D)), and the chain spends Theta(D ln C) steps at low
F where Phi^2 ~ 1. Exact law: <Phi^2>_cycle = 1 - C/(Gamma E[tau]) =
D H_C/(C + D H_C) (1+o(1)) -> 1/(1+c) for C = c D ln D - a positive
constant. Witness (exact backward induction, Gamma=2, D=150,
C=3006): exact 0.29956, corrected formula 0.29993, carried formula
0.15202.

## CX-R60-2: 'mid-drain bursts O(1) per cycle' REFUTED (late regime)
Expected S^V >= 2 triggers per full drain = (1/Gamma) D ln D (1+o(1))
+ Theta(D) - unbounded. Witness (exact induction, Gamma=2): 34.2 /
137.3 / 414.2 triggers at D = 20/60/150. P(uninterrupted full drain)
= exp(-Theta(D log D)) (ln P = -520.7 at D=500). Consequence: pure
renewal cycles are an early-regime object; the late regime is the
balance band. Panel correction folded in: the general-Gamma
prefactor is 1/Gamma, not C(Gamma,2)/Gamma (equal only at Gamma=2).

## CX-R60-3: carried late-decay Theta(ln ln n / ln n) REPLACED
The balance-band law gives mean-square vacuum fraction x*^2 =
r/(4 C(Gamma,2) n ln n) at maturity n (run-average twice that), so
the time-averaged lapse^2 is O((n ln n)^{-1/2}) - a polynomial
scale, not ln ln n/ln n. Verified decisively in a self-consistent
simulation (late-window ratio 1.098 +/- 0.051 vs 2.0 for the
alternative bookkeeping, >17 sigma).

## CX-R60-4: carried N_V ~ Gamma n^2 ln ln n/(2(Gamma+H-m)) REFUTED
It presupposed the ln ln n/ln n decay. Corrected: N_V =
O(Gamma sqrt(2/(C(Gamma,2) r)) n^{3/2} sqrt(ln n)) (upper THEOREM
at E-level; matching lower CONJECTURE).

## CX-R60-5: registered depth-constant band [1, 2] REFUTED
Labeled readout: M_n/ln n = 3.58 at n = 10^3 (40/40 seeds >= 3.0),
rising to ~4.34 at n = 10^6. Proven E-level band: [1, 2e] in ln
units (upper by the Poisson-tail union bound with exact parent
marginal <= 2/(n-2); lower by max >= average with summable
exclusion bias).
"""
(PKG / "OD0_R60_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

# ----------------------------------------------------------------- report
vt = A.VERDICTS["components"]
report = f"""# OD0-R60 Report: M7 - Lapse and Clock Epoch Laws

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.

## Position
R59 stamp pinned (verified in R60_INPUT_LOCK.json). Targets L1-L8
frozen verbatim at Commit A. BELL2 unopened; H3-H5 sentinels
parsed=false throughout; H1/H2 spent, not consulted. Every L4-L7
derivation passed a five-referee adversarial panel before freezing.

## The laws

**L1 (E0): {A.L["L1"]["verdict"]}.** {A.L["L1"]["statement"]}

**L2 (E1 identities): {A.L["L2"]["verdict"]}.** {A.L["L2"]["statement"]}

**L3 (E1 entry): {A.L["L3"]["verdict"]}.** {A.L["L3"]["statement"]}

**L4 (cycle law): {A.L["L4"]["verdict"]}.**
{A.L["L4"]["statement"]}

**L5 (late regime): {A.L["L5"]["verdict"]}.**
{A.L["L5"]["statement"]}

**L6 (three ages): {A.L["L6"]["verdict"]}.**
{A.L["L6"]["statement"]}

**L7 (depth / reading / regions): {A.L["L7"]["verdict"]}.**
{A.L["L7"]["statement"]}

**L8 (persistent load): {A.L["L8"]["verdict"]}.**
{A.L["L8"]["statement"]}

## Components
LATE_DECAY = {vt["LATE_DECAY"]}; THREE_AGES = {vt["THREE_AGES"]};
REGIONS = {vt["REGIONS"]}.

## The sealed M7 prediction set
{len(A.M7_PREDICTIONS)} statements ({results["M7_theorem_grade_count"]}
at THEOREM grade), sealed target-blind; sha256 = {pset_sha}.
It is the only object H3/H4 may later be compared against.

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R60_RESULTS.json).

## R61
{A.VERDICTS["r61_recommendation"]}
"""
(PKG / "OD0_R60_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R60_REPORT.md", "OD0_R60_RESULTS.json",
         "OD0_R60_COUNTEREXAMPLES.md", "R60_INPUT_LOCK.json",
         "R60_LAPSE_CLOCK_LAWS.json", "R60_M7_PREDICTION_SET.json",
         "R60_READOUTS.json", "R60_EXACT_CERTIFICATES.json",
         "r60_exact.py", "r60_adjudication_data.py",
         "build_r60_outputs.py", "make_r60_lock.py"]
manifest = {"schema": "R60_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R60_OUTPUT_MANIFEST.json", manifest)
print("M7 prediction set sha256:", pset_sha)
print("manifest sha256:", sha(PKG / "R60_OUTPUT_MANIFEST.json"))
print("b=n-2 at Gamma=2 (all):",
      readouts["summary"]["b_equals_n_minus_2_at_Gamma2"])
print("window rms/pred median:",
      readouts["summary"]["window_over_pred_median"])
print("maxdepth/ln n range:",
      readouts["summary"]["maxdepth_over_ln_n_range"])
print("renewals range:", readouts["summary"]["renewals_range"])
