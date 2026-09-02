"""OD0-R55 adjudication data: late-regime theorems. (Claude Code executor.)

Frozen targets are adjudicated as PROVEN / SCOPED with explicit proofs,
constants, and named gaps. Corrections to the registered prediction are
recorded, not softened.
"""

RUN_DATE = "2026-09-02"

FROZEN_SUPPORT = {
    "verdict": "PROVEN (a, c, d fully; b proven with a two-stage explicit "
               "bound, uniform-form scoped to D_tau above the bite "
               "threshold)",
    "lemma_1_pair_service_identity": {
        "statement": "At any state with pool F, tokens D, draws n = "
                     "min(Gamma, F+D): the probability that two specific "
                     "vacuum tokens are both served is EXACTLY "
                     "n(n-1)/((F+D)(F+D-1)).",
        "proof": "The service realization draws n of the F+D identified "
                 "requests uniformly (matching groupoid, R52 S1-derived "
                 "identity); both specified tokens drawn with probability "
                 "C(F+D-2, n-2)/C(F+D, n) = n(n-1)/((F+D)(F+D-1)).",
        "certified": "engine check at every evolved state (0 failures "
                     "expected; see certificates)",
    },
    "lemma_2_occupation_bound": {
        "statement": "For m < Gamma and any E1 start (D_tau > Gamma), "
                     "E[sum_k 1/(R_k(R_k-1))] <= "
                     "[1/(Gamma-m) + 1/p0(Gamma,m)] / (D_tau - 1), where "
                     "R_k = F_k + D_k and p0(Gamma,m) = "
                     "((Gamma-m)/Gamma)^2 / 2 is a band burst-probability "
                     "lower bound.",
        "proof_outline": [
            "Split steps into drain steps (F above the band mD/(Gamma-m)) "
            "and band steps.",
            "Drain: F decreases in expectation by at least Gamma-m per "
            "step there (R53 drift), so the expected number of steps with "
            "R in [r, r+1) is <= 1/(Gamma-m); summing "
            "1/(r(r-1)) over r >= D_tau gives <= "
            "1/((Gamma-m)(D_tau-1)).",
            "Band: x >= (Gamma-m)/Gamma exactly (R53), so P(S^V >= 2) >= "
            "x^2-type bound and a burst occurs per band step with "
            "probability >= p0; hence expected band steps at each D-level "
            "j is <= 1/p0, and D-levels advance with each burst: "
            "sum_j (1/p0)/((D_tau+j)(D_tau+j-1)) telescopes to "
            "1/(p0 (D_tau-1)).",
        ],
        "note": "This REPAIRS the packaged proof route: the route's "
                "step-3 telescoping bounds only burst-step co-services; "
                "quiet-step co-services are controlled by Lemma 1's "
                "F-dependence (theta_k <= Gamma(Gamma-1)/(R_k(R_k-1))) "
                "plus this occupation split. The frozen TARGETS are "
                "unchanged; the route correction is recorded in the "
                "counterexamples file.",
    },
    "a_finite_co_service": {
        "status": "PROVEN",
        "bound": "E[# co-service steps of (u,v) from tau] <= "
                 "Gamma(Gamma-1) * [1/(Gamma-m) + 2Gamma^2/(Gamma-m)^2] "
                 "/ (D_tau - 1) =: phi(Gamma, m, D_tau)",
    },
    "b_positive_non_formation": {
        "status": "PROVEN (two-stage bound)",
        "bound": "For D_tau above the bite threshold: P(never) >= "
                 "1 - phi > 0. For Gamma < D_tau <= bite: there is a "
                 "positive explicit constant - the probability of a "
                 "finite explicit path (other pairs forming, (u,v) never "
                 "co-served) that raises D above the bite, times the "
                 "1 - phi bound there; every step of the path has "
                 "positive rational probability, so the constant is "
                 "computable from (Gamma, m, D_tau). The single-formula "
                 "uniform bound is scoped to the bite region and reported "
                 "exactly.",
    },
    "c_inclusion_decay": {
        "status": "PROVEN",
        "phi": "phi(Gamma, m, D_tau) = Gamma(Gamma-1)[1/(Gamma-m) + "
               "2Gamma^2/(Gamma-m)^2]/(D_tau-1) -> 0 as D_tau -> "
               "infinity; O(Gamma^4/((Gamma-m)^2 D)) - coarser in the "
               "constant than the O(Gamma^2/D) target but of the "
               "targeted 1/D order (the target asked for the sharpest "
               "the argument yields; this is it)",
    },
    "d_nondegenerate_support": {
        "status": "PROVEN",
        "statement": "Any available-but-unformed pair at an E1 state "
                     "forms with positive probability (Lemma 1 gives a "
                     "positive per-step co-service probability) and "
                     "never forms with positive probability (b); hence "
                     "S_inf intersect M is nondegenerate for any fixed "
                     "finite M containing such an element. The registry "
                     "(the 173 T_dag^5 objects, R50 exact arrow) is an "
                     "instance whenever some registry pair is unformed "
                     "in E1 - which the exact evolutions show has "
                     "probability 1 from every registered start.",
    },
    "corollaries": {
        "bite": "phi < 1 iff D_tau > 1 + Gamma(Gamma-1)[1/(Gamma-m) + "
                "2Gamma^2/(Gamma-m)^2]; per-(Gamma,m) thresholds in the "
                "certificates; vacuous below (stated exactly, as the "
                "target requires)",
        "vanishing_fraction": "At a state with D objects there are "
                              "C(D,2)-(D-2) available pairs, each with "
                              "P(ever form) <= phi ~ 1/D; the expected "
                              "fraction ever realized tends to 0: the "
                              "universe realizes a vanishing, RANDOM "
                              "fraction of the universal DAG.",
        "random_ideal": "The realized universe is a random ideal of the "
                        "universal DAG; the eventual support of every "
                        "fixed grade is a nondegenerate random subset.",
    },
}

TERMINATION = {
    "verdict": "SCOPED (corrects the registered prediction, which "
               "expected PROVEN)",
    "a_supercritical": {
        "status": "SCOPED - conditional theorem + named unconditional gap",
        "proven_exact": [
            "For m > Gamma + H: B_k >= B_0 + (m-Gamma-H)k deterministically "
            "(service <= Gamma, relief <= H per step), so F_k >= "
            "(m-Gamma-H)k + 22*N_k (each burst's cheapest object injects "
            ">= 22 requests) - the pool grows at least linearly forever.",
            "x_k <= (2 + C(Gamma,2)N_k)/((m-Gamma-H)k + 22N_k + D_k): the "
            "process is permanently load-dominated with x bounded away "
            "from 1 by C(Gamma,2)/22 asymptotically.",
            "CONDITIONAL TERMINATION: if cumulative burst cost grows "
            "superlinearly in the burst count (cost_N / N -> infinity), "
            "then on {N_inf = infinity} the burst probabilities satisfy "
            "sum_k p_k < infinity, contradicting Levy's conditional "
            "Borel-Cantelli; hence N_inf < infinity a.s. under that "
            "condition.",
        ],
        "gap": "UNCONDITIONALLY OPEN: a linear-bursting regime (N_k ~ k, "
               "D_k ~ k, x stabilized near C(Gamma,2)/22-scale) is "
               "self-consistent under the load argument alone; excluding "
               "it requires a lower bound on the typical burst cost of "
               "the random DAG - the same named obstruction as the "
               "growth rate. The frozen target (a) is therefore NOT "
               "proven this round; what is proven is the conditional "
               "theorem and the exact load-domination bounds.",
    },
    "b_persistence": {
        "status": "m < Gamma PROVEN (R53, carried). Extension to m < "
                  "Gamma + H: exact statement - when the relief gate "
                  "(B >= Gamma and P >= 6) holds, the per-step drain "
                  "capacity is Gamma + voided <= Gamma + H; the drift "
                  "band argument extends verbatim IF gating recurs; "
                  "gating recurrence (P staying >= 6 against relief's own "
                  "subtraction) is the exact unproven lemma, stated and "
                  "left open (consistent with R53's boundary note).",
    },
    "c_critical_line": {
        "status": "The entire band Gamma <= m <= Gamma + H is OPEN: "
                  "below it persistence is proven, above it only "
                  "conditional termination; on the line m = Gamma + H "
                  "nothing is claimed. Stated in model-internal terms "
                  "only.",
    },
    "registered_points": "27 points have m >= Gamma; exactly the "
                         "H = 0 subset with m > Gamma (Gamma=2, m=3, "
                         "H=0) is supercritical m > Gamma+H (1 point); "
                         "the rest lie in the open band or on the line - "
                         "per-point table in the certificates.",
}

RATE = {
    "verdict": "UPPER BOUND IMPROVED (k/loglog k form); beta < 1 target "
               "NOT met; lower bound alpha > 0 NOT obtained; obstruction "
               "named on both sides",
    "cost_budget_identity": {
        "statement": "EXACT: at every transition B' - B = m + requests - "
                     "S^F - voided; hence cumulative injected cost "
                     "sum_j c(y_j) = B_k + cumServed + cumVoided - m*k "
                     "<= B_k + (Gamma + H - m)k + const. "
                     "Engine-certified at every evolved transition.",
    },
    "upper_bound_theorem": {
        "statement": "For m < Gamma, on the event that B_k/k -> 0 (the "
                     "recurrent-drain regime), |X_k| <= C(Gamma,m,H) * "
                     "k / log log k eventually. Proof: (i) the cost "
                     "budget gives sum of first-use costs <= "
                     "(Gamma+H)k + B_k; (ii) c(y) >= 11 * paths_to(y) "
                     ">= 22 * depth(y); (iii) the universal DAG's "
                     "cumulative depth-census T(d) satisfies T(d+1) = "
                     "C(T(d),2) + 2 (doubly exponential), so any ideal "
                     "of size N contains at least N - T(d) objects of "
                     "depth > d; choosing d with T(d) ~ N/2 gives total "
                     "first-use cost >= c * N * d(N) with d(N) ~ "
                     "log log N. Combining: N * log log N <= C * k.",
        "class": "THEOREM (with the B_k/k -> 0 hypothesis stated; "
                 "unconditional for the m=0 points where drains recur "
                 "by R53's renewal theorem)",
    },
    "beta_lt_1_obstruction": "The universal DAG is doubly-exponentially "
        "wide: objects of depth d number T(d+1)-T(d), so cheap objects "
        "(cost ~ 22d) are too plentiful for the budget argument to force "
        "any polynomial gap - k/loglog k is the exact limit of this "
        "route. Named obstruction: cheap-object abundance.",
    "alpha_gt_0_obstruction": "A positive growth exponent needs an UPPER "
        "bound on typical burst cost (to bound cycle lengths); typical "
        "served pairs are recent objects whose paths_to is uncontrolled "
        "from above. Named obstruction: uncontrolled typical burst cost "
        "- the same quantity, from the other side.",
}

HOSTILE_CONTROLS = [
    ["HC1", "theorem statement altered after Commit A", "REJECTED",
     "Targets adjudicated verbatim as frozen; the route repair is "
     "recorded separately and changes no statement."],
    ["HC2", "H1 content used beyond disclosed provenance; renewed H1 "
     "comparison", "REJECTED", "No H1 artifact opened; the registry "
     "readout uses the R50-derived object identity only and is labeled "
     "non-comparison."],
    ["HC3", "H2-H5 content read", "REJECTED",
     "The supplied Run3_Dijet paper was hashed (bytes only) and pinned "
     "sealed; sentinels parsed=false at start and end."],
    ["HC4", "readouts cited as proof; exponent asserted from readouts",
     "REJECTED", "All verdict components rest on the proofs above; the "
     "sqrt-k comparison stays labeled."],
    ["HC5", "threshold or external referent", "REJECTED", "None appears."],
    ["HC6", "modification of TG1/cost law/filtration/frozen roots",
     "REJECTED", "Nothing modified; worktree clean."],
    ["HC7", "BELL2 opened", "REJECTED", "Unopened."],
    ["HC8", "hand hash; placeholder", "REJECTED",
     "All hashes in-process; stamp commit closes the round."],
]

VERDICTS = {
    "always": "OD0_R55_PASS_LATE_REGIME_TARGETS_ADJUDICATED",
    "components": {
        "FROZEN_SUPPORT": "PROVEN(phi = Gamma(Gamma-1)[1/(Gamma-m) + "
                          "2Gamma^2/(Gamma-m)^2]/(D_tau-1); (b) "
                          "two-stage)",
        "TERMINATION": "SCOPED(conditional theorem; unconditional gap = "
                       "typical burst-cost growth)",
        "PERSISTENCE_EXTENSION": "m < Gamma proven (carried); m < "
                                 "Gamma+H gap = relief-gating recurrence "
                                 "lemma",
        "CRITICAL_LINE": "band Gamma <= m <= Gamma+H open; stated "
                         "model-internally",
        "RATE": "UPPER k/loglog k (theorem, hypothesis stated); beta<1 "
                "and alpha>0 blocked by the named two-sided cost "
                "obstruction",
    },
    "prediction_vs_outcome": "Frozen support: PROVEN as predicted, with "
        "phi of the predicted 1/D order (constant coarser: Gamma^4/"
        "(Gamma-m)^2 rather than 2Gamma(Gamma-1)); the packaged proof "
        "route needed repair (quiet-step co-services; occupation split) "
        "- recorded. Termination: CORRECTED - predicted PROVEN, "
        "adjudicated SCOPED: the load argument alone cannot exclude a "
        "self-consistent linear-bursting regime; termination is proven "
        "only conditionally on superlinear burst-cost growth. "
        "Persistence extension: gap as predicted. Rate: the k/loglog k "
        "upper bound is NEW (the prediction expected beta < 1 or "
        "obstruction; the outcome is between - a genuine improvement "
        "that still misses the beta < 1 form); the obstruction is named "
        "on both sides as predicted (drained-state frequency was the "
        "predicted obstruction; the actual named obstruction is "
        "cheap-object abundance / uncontrolled typical burst cost). "
        "The prediction constrained nothing.",
    "r56_recommendation": "FROZEN_SUPPORT = PROVEN, so per the R56 rule: "
        "freeze, target-blind for H2-H5, (i) the nine H1-provenance "
        "observables as exact functions on z+ (provenance disclosed), "
        "and (ii) the inclusion-probability law phi as the derived "
        "availability prediction; preregister the H2 comparison "
        "protocol (availability of fixed structures at maturity as a "
        "frozen random subset - shape and monotonicity only; the "
        "Run3_Dijet paper is now pinned sealed and waiting); open the "
        "M5 question (which repeated exact semantic labels become "
        "reachable in the realized random ideal). The termination "
        "result is queued for M7 and compared with nothing in R56.",
}
