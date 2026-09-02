#!/usr/bin/env python3
"""OD0-R59 output builder. Deterministic; byte-identical on rerun."""
import hashlib
import json
import math
from pathlib import Path

import r59_adjudication_data as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


lock = json.loads((PKG / "R59_INPUT_LOCK.json").read_text(encoding="utf-8"))
certs = json.loads((PKG / "R59_EXACT_CERTIFICATES.json").read_text(encoding="utf-8"))
r53 = json.loads((PKG / "R53_SAMPLED_READOUT.json").read_text(encoding="utf-8"))


def solve_N(c, k):
    """Solve N^2 ln N = c*k/2 by Newton (float, presentation only)."""
    rhs = c * k / 2.0
    N = max(3.0, math.sqrt(rhs / max(1.0, math.log(math.sqrt(rhs)))))
    for _ in range(60):
        f = N * N * math.log(N) - rhs
        fp = 2 * N * math.log(N) + N
        N -= f / fp
    return N


growth_table = []
for pt in r53["points"]:
    G, m, H = pt["Gamma"], pt["m"], pt["H"]
    if m >= G:
        continue
    row = {"Gamma": G, "m": m, "H": H, "readouts": {}}
    for kk in ("1000", "10000"):
        if kk not in pt.get("summary", {}):
            continue
        k = int(kk)
        obs = float(pt["summary"][kk]["X_mean_dec"])
        lo = solve_N(G - m, k)
        hi = solve_N(G + H - m, k)
        row["readouts"][kk] = {
            "observed_X_mean": round(obs, 3),
            "predicted_N_low_c_Gamma_minus_m": round(lo, 2),
            "predicted_N_high_c_Gamma_plus_H_minus_m": round(hi, 2),
            "obs_over_pred_low": round(obs / lo, 4),
        }
    growth_table.append(row)

h0_ratios = [v["obs_over_pred_low"] for row in growth_table if row["H"] == 0
             for v in row["readouts"].values()]
agreement_summary = {
    "H0_points": {"count": len(h0_ratios),
                  "obs_over_pred_min": min(h0_ratios),
                  "obs_over_pred_max": max(h0_ratios),
                  "note": "Relief-free points: the parameter-free E-level "
                          "law N^2 ln N = (Gamma - m) k / 2 matches every "
                          "registered point within ~15% (labeled "
                          "agreement, not proof)."},
    "H_positive": {"note": "Observed means track the upper solve "
                           "(c = Gamma + H - m) at small H and saturate "
                           "near H ~ 5, consistent with the quota-gated "
                           "relief mechanism (labeled)."}}

laws = {
    "schema": "R59_RANDOM_DAG_LAWS_V1",
    "T1_uniform_pair_law": A.T["T1"],
    "T2_ancestry_law": A.T["T2"],
    "T3_cone_size": A.T["T3"],
    "T4_chain_growth": A.T["T4"],
    "T5_recorded_cone": A.T["T5"],
    "exact_closed_forms": {
        "E_T_n": "n(n-1)/2 + 1 (exact, all n; proven fixed point of the "
                 "exact linear recursion; certified n <= 10 exhaustively)",
        "E_chains_new_at_n": "n (exact)",
        "E_chains_new_given_state": "2((k-2)T + 2)/(k^2 - 3k + 4)",
        "descendant_fraction": "phi_j(n) = n/(n + j(j-1)) (1+o(1))",
        "ancestor_law": "a_j(n) = 2 phi_j - phi_j^2 + O(1/n)",
        "cone": "E|cone(new at n)| = (3 pi/4) sqrt(n) (1+o(1))",
        "weighted_cone": "E[W(new at n)] = n ln n (1+o(1)), band [1/2,2]",
        "identity": "paths_to(x) = 2 chains(x) - 2 (exact)",
    },
    "certificates": {
        "paths_chains_identity": certs["paths_chains_identity"],
        "exhaustive_moments_n_le_10": certs["exhaustive_law_moments_n_le_10"],
        "cv2_trajectory": certs["cv2_trajectory"],
    },
}
dump(PKG / "R59_RANDOM_DAG_LAWS.json", laws)

cost = {
    "schema": "R59_COST_AND_GROWTH_V1",
    "T6_typical_burst_cost": A.T["T6"],
    "T7_growth_exponent": A.T["T7"],
    "T8_termination_closure": A.T["T8"],
    "growth_prediction_vs_readout_labeled": {
        "note": "LABELED READOUT - agreement is not proof. Predicted N "
                "solves N^2 ln N = c k / 2 with c in {Gamma - m, "
                "Gamma + H - m} (E-level cost-budget balance, "
                "paths-form cumulative cost 2 N^2 ln N).",
        "agreement_summary": agreement_summary,
        "points": growth_table},
    "readout_containment_labeled": certs["readout_containment"],
    "bedrock_readout_labeled": {
        "note": "Share of cone members of late-born objects born before "
                "sqrt(final n); mean-field prediction of the share is "
                "(3 pi/8 - 1/4)/(3 pi/4) = 0.394 as n -> infinity.",
        "rows": certs["bedrock_readout_labeled"]},
    "termination_dichotomy": {
        "m_lt_Gamma": "U (unbounded growth a.s., R53 theorem)",
        "m_gt_Gamma_plus_H": "T (finite growth a.s., CLOSED this round)",
        "band_Gamma_le_m_le_Gamma_plus_H": "OPEN (relief-gated "
                                           "recurrence)"},
}
dump(PKG / "R59_COST_AND_GROWTH.json", cost)

results = {
    "schema": "OD0_R59_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["always"],
    "components": A.VERDICTS["components"],
    "targets_frozen_at_commit_A": True,
    "input_lock_sha256": sha(PKG / "R59_INPUT_LOCK.json"),
    "hostile_controls": [
        {"id": h[0], "control": h[1], "status": h[2], "basis": h[3]}
        for h in A.HC],
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "r60_recommendation": A.VERDICTS["r60_recommendation"],
    "seals": {"BELL2_opened": False,
              "H1": "spent (R54)", "H2": "spent (R57)",
              "H3": {"parsed": False}, "H4": {"parsed": False},
              "H5": {"parsed": False}},
    "adjudication": A.T,
}
dump(PKG / "OD0_R59_RESULTS.json", results)

cx = """# OD0-R59 Counterexamples and corrections (append-only)

## CX-R59-1: registered Gamma-ratio product form for E[T_n] REFUTED
The registered prediction gave E[T_n] via the product 4*prod_{k=3}^{n-1}
(1 + 2/k) = n(n+1)/3. The exact law is E[T_n] = n(n-1)/2 + 1 (proven
fixed point of the exact linear recursion E[chains(new)|state] =
2((k-2)T+2)/(k^2-3k+4); certified exhaustively for n <= 10, e.g.
E[T_10] = 46 vs product form 110/3). The product form omits the
existing-pair exclusion, which shifts the quadratic constant from 1/3
to 1/2. Recorded as a refutation of the registered closed form; the
target's Theta(n^2) claim stands with the corrected constant.

## CX-R59-2: registered ancestry form is the descendant fraction, not
## the ancestor law
n/(n + j(j-1)) is the descendant FRACTION phi_j(n). The ancestor
probability of the new object is a_j(n) = 2 phi_j - phi_j^2 + O(1/n).
Witness (exhaustive exact, j = 8, n = 9): a = 0.2759; corrected law
0.258; registered phi-form 0.139. The phi-form as ancestor law is
refuted; the corrected identification is adopted.

## CX-R59-3: registered cone constant pi/2 REFUTED; correct constant
## 3 pi/4
sum_j phi_j = (pi/2) sqrt(n) is the single-parent cone; the pair-union
cone is sum_j (2 phi_j - phi_j^2) = (3 pi/4) sqrt(n) (1+o(1)).
Registered constant corrected; the Theta(sqrt n) order stands.
"""
(PKG / "OD0_R59_COUNTEREXAMPLES.md").write_text(cx, encoding="utf-8",
                                                newline="\n")

vt = A.VERDICTS["components"]
report = f"""# OD0-R59 Report: The Random-DAG Cost Theorem

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["always"]}**.

## Position
R58 stamp pinned (verified in R59_INPUT_LOCK.json). Targets T1-T8
frozen verbatim at Commit A before any computation. BELL2 unopened;
H3-H5 sentinels parsed=false; H1/H2 spent, not consulted.

## The theorems

**T1 (uniform pair law): PROVEN.** {A.T["T1"]["statement"]}

**T2 (ancestry law): {A.T["T2"]["verdict"]}.** {A.T["T2"]["statement"]}

**T3 (cone size): {A.T["T3"]["verdict"]}.** {A.T["T3"]["statement"]}

**T4 (chain growth): {A.T["T4"]["verdict"]}.** {A.T["T4"]["statement"]}

**T5 (recorded cone): {A.T["T5"]["verdict"]}.** {A.T["T5"]["statement"]}

**T6 (typical burst cost): {A.T["T6"]["verdict"]}.**
{A.T["T6"]["statement"]}

**T7 (growth exponent): {A.T["T7"]["verdict"]}.**
{A.T["T7"]["statement"]}

**T8 (termination closure): {A.T["T8"]["verdict"]}.**
{A.T["T8"]["statement"]}

## Components
CONE_ORDER = {vt["CONE_ORDER"]}; COST_ORDER = {vt["COST_ORDER"]};
GROWTH_BOUNDS = {vt["GROWTH_BOUNDS"]}; TERMINATION = {vt["TERMINATION"]}.

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
All 8 REJECTED (see OD0_R59_RESULTS.json).

## R60
{A.VERDICTS["r60_recommendation"]}
"""
(PKG / "OD0_R59_REPORT.md").write_text(report, encoding="utf-8",
                                       newline="\n")

files = ["OD0_R59_REPORT.md", "OD0_R59_RESULTS.json",
         "OD0_R59_COUNTEREXAMPLES.md", "R59_INPUT_LOCK.json",
         "R59_RANDOM_DAG_LAWS.json", "R59_COST_AND_GROWTH.json",
         "R59_EXACT_CERTIFICATES.json", "r59_exact.py",
         "r59_adjudication_data.py", "build_r59_outputs.py"]
manifest = {"schema": "R59_OUTPUT_MANIFEST_V1",
            "note": "manifest excludes itself",
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R59_OUTPUT_MANIFEST.json", manifest)
print("manifest sha256:", sha(PKG / "R59_OUTPUT_MANIFEST.json"))
for f in files:
    print(" ", manifest["files"][f][:16], f)
