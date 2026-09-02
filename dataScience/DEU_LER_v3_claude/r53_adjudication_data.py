"""OD0-R53 adjudication data (Claude Code executor, package v0.1)."""

RUN_DATE = "2026-09-02"

COST_THEOREM = {
    "chains_recurrence": {
        "statement": "chains(primitive) = 1; chains({u,v}) = chains(u) + "
                     "chains(v). Proof: a complete immediate-parent chain "
                     "to {u,v} ends with a step from exactly one of the "
                     "two parents, and its initial segment is a complete "
                     "chain to that parent; the correspondence is a "
                     "bijection. No orientation correction is needed for "
                     "counting (the orientation double cover doubles "
                     "frames, not chains).",
    },
    "paths_recurrence": {
        "statement": "paths_to(primitive) = 0; paths_to({u,v}) = "
                     "(paths_to(u)+1) + (paths_to(v)+1) - all immediate-"
                     "parent paths of length >= 1 ending at the object, "
                     "from any starting vertex. The frozen record identity "
                     "(R50 prefix-canonical) counts PATHS, not only "
                     "primitive-rooted complete chains: every path ending "
                     "in the used parent's ancestry cone is a distinct "
                     "recorded prefix. The cost law is therefore stated in "
                     "paths, with chains as the primitive-rooted subfamily "
                     "(recorded as an exact refinement of the package's "
                     "sketch).",
    },
    "first_use_cost": {
        "statement": "At the first use of x (given the recorded-cone "
                     "invariant: x's creation recorded Anc(x)\\{x}), the "
                     "new prefixes are exactly the paths ending AT x - "
                     "count paths_to(x) - and every deeper cone path is a "
                     "repeat. c(x) = c_first * paths_to(x) + c_repeat * "
                     "sum over w in (Anc(x)\\{x} and X) of paths_to(w), "
                     "with c_first in the frozen ranges (11..13 Q1, "
                     "22..26 Q2; 11 used as the declared lower bound) and "
                     "c_repeat = 2 exactly (R52 Part 1.4).",
    },
    "depth_bounds": {
        "upper": "chains(x) <= 2^depth(x) (induction: chains(u)+chains(v) "
                 "<= 2*2^(depth-1)); certified with 0 failures on O_<=7",
        "lower_fibonacci": "along the maximal-chain family x_k = "
                           "{x_{k-1}, x_{k-2}}: chains(x_k) = Fib(k+2) "
                           "(1,1,2,3,5,8,13,21 - engine-certified); "
                           "general lower bound: chains(x) >= depth(x)+1",
        "paths_lower": "paths_to(x) >= 2*depth(x) (each step adds >= 2)",
    },
    "c_min_monotonicity": {
        "statement": "NOT monotone in general: pair costs are state-"
                     "dependent only through the recorded set, and newly "
                     "created shallow objects introduce new enabled pairs "
                     "that can be cheaper than the surviving enabled "
                     "pairs; moreover repeat-only pairs (both cones fully "
                     "recorded) cost 2*|cone paths|, which can undercut "
                     "first-use pairs. The engine's exact witness (or its "
                     "absence over the searched range) is recorded in the "
                     "certificates; the package's trailing-clause claim "
                     "is adjudicated by that search.",
    },
}

GROWTH_LAW = {
    "case_split": "by external load m vs per-region capacity Gamma "
                  "(capacity total constant, carry-forward)",
    "U_theorem_m_lt_Gamma": {
        "verdict": "U - unbounded growth a.s., PROVEN for all registered "
                   "points with m < Gamma (117 of 144)",
        "proof_outline": [
            "1. Quiet-step drift: E[Delta F | F, D, quiet] = m - "
            "min(Gamma,F+D)*F/(F+D) <= m - Gamma*F/(F+D) < 0 exactly "
            "whenever F > m*D/(Gamma-m); jumps are bounded on quiet steps "
            "(service <= Gamma, relief <= H), so F returns a.s. to the "
            "band F <= m*D/(Gamma-m) (drift-recurrence).",
            "2. In the band, x = D/(F+D) >= (Gamma-m)/Gamma exactly.",
            "3. P(S^V >= 2 | state) >= D(D-1)/((F+D)(F+D-1)) >= "
            "((Gamma-m)/Gamma)^2 * (D-1)/D-type positive bound in the "
            "band (R52 global bound); D >= 2 always.",
            "4. At a burst attempt, P(new object >= 1) >= "
            "1 - (n-2)/C(n,2) > 0 (R52 growth identity; absent pairs "
            "always exist - R49 lemma).",
            "5. Infinitely many band visits x positive burst probability "
            "bounded below along them => infinitely many new objects a.s. "
            "(conditional Borel-Cantelli).",
        ],
        "rate": "PARTIAL: upper bound |X_k| <= 2 + C(Gamma,2)*k (exact); "
                "no proven lower rate - the registered Theta(log k) "
                "target is NOT established. The gap is the cost-growth "
                "law of the random DAG: the c_min non-monotonicity blocks "
                "the geometric-burst-cost argument, and the depth "
                "profile of uniformly-served new pairs is not controlled "
                "by an exact theorem this round.",
    },
    "P_m_ge_Gamma": {
        "verdict": "P - not closed by exact argument (27 registered "
                   "points: Gamma=2 with m in {2,3}; Gamma=3 with m=3)",
        "exact_statements": [
            "Quiet-step drift >= m - Gamma >= 0: F is nondecreasing in "
            "expectation on quiet steps; with H = 0 and m > Gamma, "
            "F_{k+1} >= F_k + (m - Gamma) deterministically, so F >= "
            "(m-Gamma)*k -> infinity.",
            "Relief adds up to H per gated step to the drain; for m <= "
            "Gamma + H with recurrent gating the band argument can "
            "re-enter, but gating requires B >= Gamma and P >= 6, whose "
            "recurrence is not proven this round.",
            "Along any trajectory with F >= c*k and D = o(k), sum_k "
            "P(S^V >= 2) <= sum_k C(Gamma,2)*(D_k/(F_k))^2 converges, "
            "giving a.s. finitely many bursts (T-flavored); but D_k = "
            "o(k) is itself not proven unconditionally.",
        ],
        "gap": "whether D_k/F_k -> 0 along m >= Gamma trajectories; "
               "stated precisely, left open",
    },
    "sensitivity": {
        "relief": "shifts the drain capacity from Gamma to at most "
                  "Gamma + H per step, hence shifts the case boundary "
                  "toward m < Gamma + H (conditional on recurrent "
                  "gating); does not change the growth class within "
                  "m < Gamma (U-proof unaffected).",
        "population_factor": "enters only the relief quota timing (P "
                             "growth rate); with factor 1 the gate P >= 6 "
                             "arrives later but recurs identically; "
                             "growth class unchanged.",
    },
}

RENEWAL = {
    "theorem": "At drained states (F = 0): n = min(Gamma, F+D) = "
               "min(Gamma, D) and every draw is vacuum - S^V = "
               "min(Gamma, D) deterministically; the next burst is "
               "determined by the served subset alone (uniform "
               "min(Gamma,D)-subset of X). The process regenerates at "
               "drained states modulo the DAG: conditional on X, the "
               "cycle (burst size, burst cost, drain excursion of F "
               "from 0) is an exact function of the served subsets and "
               "service realizations within the cycle.",
    "burst_size_law": "at a drained state, new-object count distribution "
                      "= the R52 Part 4.3 law with s = min(Gamma, D): "
                      "P(new = j) from the uniform s-subset against the "
                      "composite graph's present pairs; mean "
                      "C(s,2)*(1-(n-2)/C(n,2)).",
    "drain_scaling": "after a burst of cost C at a drained state with "
                     "load m: per quiet step the backlog decreases by "
                     "S^F - m + voided, with S^F <= Gamma and voided <= "
                     "H; exact bounds: drain length L >= "
                     "(C - Gamma)/(Gamma + H - m) and E[L] <= "
                     "C/(Gamma*x_band - m) + O(band width) where x_band "
                     "is the band lower bound of the U-proof; stated as "
                     "two-sided exact inequalities, constants explicit "
                     "per point. Geometric growth of successive cycle "
                     "lengths is CONJECTURE (tied to the unproven cost-"
                     "growth rate).",
}

FILTRATION = {
    "E0": {
        "definition": "F + D <= Gamma (every token served every step)",
        "exit_theorem": "PERMANENT exit once D > Gamma: D = |X| is "
                        "nondecreasing, so F + D >= D > Gamma forever. "
                        "(E0 can also fail transiently through F while "
                        "D <= Gamma; the permanent-exit criterion is "
                        "D > Gamma.) Exact exit/entry distributions per "
                        "registered point in the certificates.",
        "forward_invariant": False,
    },
    "E1": {
        "definition": "D > Gamma",
        "forward_invariant": True,
        "proof": "D nondecreasing (objects never destroyed).",
    },
    "renewal_decomposition": "within E1: drained (F=0) vs draining (F>0); "
                             "burst steps (>=1 new object) vs quiet steps "
                             "- all exact state/step relations.",
    "cost_strata": {
        "statement": "{c_min <= Gamma} is NOT empty everywhere (corrects "
                     "the registered prediction): (i) at genesis the pair "
                     "{a,b} has cost 0 (empty ancestry cone - the first "
                     "record count is 0, R50); (ii) repeat-only pairs "
                     "(both members' cones fully recorded) cost "
                     "2*|cone paths|, e.g. an unformed {a,c} with c "
                     "already used costs exactly 4 <= Gamma at Gamma in "
                     "{4,5}. The stratum is transient, not forward-"
                     "invariant (it empties when its cheap pairs form and "
                     "can be re-entered when new repeat-only pairs "
                     "arise); exact per-point per-step mass in the "
                     "certificates.",
        "forward_invariant": False,
    },
    "basin_beyond_E1": {
        "verdict": "NOT DEFINABLE without a numeric choice",
        "statement": "The package's candidate relation ('expected "
                     "next-burst cost exceeds expected drain capacity "
                     "over any fixed horizon') requires a horizon "
                     "parameter; every variant we can state either "
                     "introduces a numeric threshold or reduces to E1. "
                     "Maturity beyond E1 is therefore characterized by "
                     "the asymptotic law alone (growth class U with "
                     "rate gap; renewal scaling), exactly as the "
                     "adjudication-note-2 framing anticipates.",
    },
    "historical_style_notions": "A 'basin' in the historical sense is "
        "definable only as E1 (capacity congestion, forward-invariant) "
        "or by a numeric choice, which is forbidden here; the derived "
        "regime sequence is E0 -> E1 -> (renewal cycles with growing "
        "structure), and no stratum carries a historical label.",
}

HOSTILE_CONTROLS = [
    ["HC1", "numeric threshold; criterion not in state fields", "REJECTED",
     "Every filtration criterion is a state relation (F+D<=Gamma, "
     "D>Gamma, F=0, batch nonempty, c_min<=Gamma); no numeric constant "
     "beyond frozen state fields appears."],
    ["HC2", "historical label on a stratum; historical numeric", "REJECTED",
     "Strata are named E0/E1/drained/draining/burst/quiet only."],
    ["HC3", "log-growth stated as theorem; U/T by readout", "REJECTED",
     "The Theta(log k) target is explicitly NOT established; U is proven "
     "for m < Gamma by the drift/Borel-Cantelli argument, not by "
     "readouts; m >= Gamma left as P with the precise gap."],
    ["HC4", "modification of cost law, record scope, or TG1", "REJECTED",
     "All carried verbatim; the paths-vs-chains refinement is an exact "
     "restatement of the frozen R50 record identity, recorded as such."],
    ["HC5", "capacity extrapolated; regions refined", "REJECTED",
     "Carry-forward verbatim: regions fixed, capacity total constant; "
     "all statements at registered Gamma."],
    ["HC6", "R54 protocol altered after Commit A", "REJECTED",
     "Frozen in R53_INPUT_LOCK.json at Commit A; emitted unchanged."],
    ["HC7", "external referent", "REJECTED", "None appears."],
    ["HC8", "frozen roots; BELL2", "REJECTED",
     "Read-only; worktree clean at start and end; BELL2 unopened."],
    ["HC9", "hand-produced hash", "REJECTED",
     "All hashes computed in-process."],
]

VERDICTS = {
    "always": "OD0_R53_PASS_MATURATION_FILTRATION_DEFINED_TARGET_BLIND",
    "components_static": {
        "CAPACITY_TOTAL": "constant (carry-forward)",
        "GROWTH_LAW": "U(m < Gamma: proven, rate PARTIAL [<= linear; "
                      "log-target unproven]) / P(m >= Gamma: precise gap "
                      "stated)",
        "RENEWAL": "theorem at F=0; drain bounds two-sided; geometric "
                   "cycle growth CONJECTURE",
        "BASIN_BEYOND_E1": "not definable without numeric choice",
        "R54_PROTOCOL": "FROZEN",
    },
    "prediction_vs_outcome": "Confirmed: chains recurrence exact with "
        "1,326 certification; Fibonacci lower bound; renewal at F=0; E1 "
        "forward-invariant; no basin beyond E1 without a numeric choice; "
        "R54 protocol frozen. Corrected: (i) the growth law splits by m "
        "vs Gamma - U is proven only for m < Gamma, and the registered "
        "Theta(log k) rate is NOT established (the cost-growth argument "
        "fails against the c_min non-monotonicity); (ii) the stratum "
        "{c_min <= Gamma} is NOT empty everywhere - genesis cost 0 and "
        "repeat-only pairs of cost 4 defeat the c_first > 5 argument at "
        "Gamma in {4,5}. The prediction constrained nothing.",
    "r54_recommendation": "Open H1 under the frozen protocol - one "
        "comparison, no repair: derived sequence (E0 -> E1 -> renewal "
        "cycles with growing structure, U-growth for m < Gamma with rate "
        "gap reported at equal prominence) and derived monotone "
        "observables (|X|, shell fraction, chain-multiplicity "
        "distribution, cycle-length growth) against the historical "
        "qualitative regime sequence and observables, sequence and "
        "monotonicity only.",
}
