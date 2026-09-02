"""OD0-R60 adjudication data: M7 lapse/clock epoch laws. (Claude Code.)

Every L4-L7 derivation below was independently adversarially verified
(five-referee panel, each instructed to refute; exact DP / Monte-Carlo
cross-checks) before freezing; corrections from that panel are folded in
and recorded in OD0_R60_COUNTEREXAMPLES.md.
"""

RUN_DATE = "2026-09-02"

L = {
 "L1": {"verdict": "PROVEN",
  "statement": "In E0 = {F + D <= Gamma}: n_slots = min(Gamma, F+D) = "
    "F + D, so every token is served: S^V = D, S^F = F, V0 = min(Gamma, "
    "D) = D, hence Phi^2 = D/D = 1 exactly and the tick rate equals D "
    "(rising as D grows within E0). E0 is nonempty at genesis iff "
    "m + 2 <= Gamma (genesis F = m, D = 2); for m + 2 > Gamma the "
    "process starts in the middle case {D <= Gamma < F + D} and E0 has "
    "duration 0. E0 exit is permanent at D > Gamma (R53). Exact E0 and "
    "middle-case duration distributions per registered (Gamma, m) are "
    "certified by exact distribution evolution (finite horizon, "
    "entered-probability and residual recorded) in "
    "R60_EXACT_CERTIFICATES.json."},
 "L2": {"verdict": "PROVEN",
  "statement": "Complete case table, certified exactly (3840 states, "
    "zero failures). (i) F + D <= Gamma: all served, Phi = 1, S^V = D. "
    "(ii) D > Gamma (E1): V0 = Gamma, S^V ~ Hypergeometric(F+D, D, "
    "Gamma); Phi^2 = S^V/Gamma pathwise, so the tick rate and the "
    "lapse are the SAME observable: S^V = Gamma Phi^2 exactly; "
    "E[Phi^2 | state] = D/(F+D) = x; P(Phi = 1) = P(S^V = Gamma) = "
    "C(D,Gamma)/C(F+D,Gamma); full distribution P(S^V = s) = "
    "C(D,s) C(F,Gamma-s)/C(F+D,Gamma). (iii) middle case D <= Gamma < "
    "F + D: V0 = D, E[Phi^2 | state] = Gamma/(F+D), P(Phi = 1) = "
    "C(F, Gamma-D)/C(F+D, Gamma)."},
 "L3": {"verdict": "PROVEN",
  "statement": "At the first step with D > Gamma the lapse moves from "
    "the E0/middle value to the E1 hypergeometric value with "
    "E[Phi^2] = D/(F+D), F carrying the just-fired burst costs. The "
    "exact E1-entry distribution of Phi^2 per registered (Gamma, m) - "
    "a finite mixture of hypergeometrics over entry states - and the "
    "conditional drop magnitude are certified exactly in "
    "R60_EXACT_CERTIFICATES.json. Notable exact feature: at Gamma = 2, "
    "m = 0 the entry burst is the genesis pair, whose cost is 0, so "
    "entry occurs with F = 0 and Phi = 1 exactly - the drop is "
    "deferred one step. At all other registered points the entry drop "
    "is strict (e.g. Gamma = 3, m = 0: E[Phi^2 at entry] = 0.1613; "
    "Gamma = 5, m = 3: 0.0377; exact rationals in the certificates)."},
 "L4": {"verdict": "PROVEN (cycle-average form corrected; mid-drain "
                   "burst count corrected; relief saturation derived)",
  "statement": "PURE-DRAIN CYCLE (cost C injected at object count D, "
    "m = 0, drain to renewal). (i) EXACT pathwise identity: over the "
    "cycle sum S^F = C and S^V = Gamma - S^F per E1 step, so "
    "<Phi^2>_cycle = 1 - C/(Gamma tau); in expectation (renewal-"
    "reward) <Phi^2> = 1 - C/(Gamma E[tau]). (ii) E[tau] = "
    "(C + D H_C)/Gamma (1 + O(Gamma/D)) with H_C the C-th harmonic "
    "number: expected occupation of forced level F is (F+D)/(Gamma F) "
    "(exact at Gamma = 1; level-skipping correction < 0.3% at D = 200, "
    "Gamma = 2, certified by exact backward induction: E[tau] ratio "
    "1.0004). (iii) Hence <Phi^2>_cycle = D H_C/(C + D H_C) (1+o(1)); "
    "certified exactly: D = 150, C = 4 D ln D: exact 0.29956 vs "
    "formula 0.29993 vs the constant-rate form 0.15202 - the carried "
    "form <Phi^2> = (D/C) ln(1+C/D) ~ ln(1+4 ln n)/(4 ln n) is "
    "REFUTED: it ignores the hypergeometric slowdown (the chain spends "
    "Theta(D ln C) steps at low F where Phi^2 ~ 1). (iv) With "
    "C = c D ln D the cycle-average tends to 1/(1+c) > 0 - the "
    "average lapse over a completed drain does NOT vanish with "
    "maturity (convergence is O(ln ln D / ln D)-slow; the usable "
    "finite-n law is D H_C/(C + D H_C)). (v) MID-DRAIN BURSTS: "
    "expected S^V >= 2 trigger events per full drain = "
    "(1/Gamma) D (ln D + gamma_E) + Theta(D) - Theta(D log D), NOT "
    "O(1); the carried O(1)-per-cycle note is REFUTED for the late "
    "regime (exact induction: 414 triggers at D = 150, Gamma = 2; "
    "P(uninterrupted full drain) = exp(-Theta(D log D)), e.g. "
    "ln P = -520.7 at D = 500). The general-Gamma prefactor is "
    "1/Gamma (the dominant region F <= D has x ~ 1 where "
    "P(S^V >= 2) -> 1); C(Gamma,2)/Gamma is correct only at "
    "Gamma = 2 where the two coincide. (vi) RELIEF: the relief "
    "subsystem has the deterministic attracting fixed point "
    "P* = 10 Gamma - 6 with quota exactly 2 Gamma, period 1; the "
    "long-run voiding rate is v* = H for H <= 2 Gamma - 1 and "
    "v* = 2 Gamma (1 - x) for H >= 2 Gamma (certified exactly for "
    "all Gamma in 2..5, H in 0..8; stochastic subsystem to <0.03%). "
    "Effective late drain rate r = Gamma (1 - x) + v* - m ~ "
    "Gamma + min(H, 2 Gamma) - m. This retro-explains the R59 "
    "labeled growth-table saturation at H ~ 2 Gamma (capped law "
    "obs/pred = 0.978 +/- 0.063 vs uncapped 0.866 +/- 0.097)."},
 "L5": {"verdict": "PROVEN at mean-square E-level (upper for the mean "
                   "THEOREM; matching mean lower and pointwise "
                   "concentration CONJECTURE); recurrence stratified",
  "statement": "The carried Theta(ln ln n / ln n) decay is REPLACED by "
    "the BALANCE-BAND LAW. (i) Exact burst-count identity (Doob): "
    "E[b_k] = E[sum_t P(burst | state_t)], with exact two-sided "
    "bounds (1/2)(1 - 2/n) x^2 <= P(S^V >= 2 and pair absent | "
    "state) <= C(Gamma,2) x^2 (the upper holds with NO epsilon at "
    "every state; certified on an exact hypergeometric grid). "
    "(ii) Bursts create 1..C(Gamma,2) objects: (n-2)/C(Gamma,2) <= "
    "b <= n - 2, and at Gamma = 2, b = n - 2 EXACTLY. (iii) With "
    "k(n) = sum_j c_j / r (R59 cost theorem, r = Gamma + min(H, "
    "2 Gamma) - m): the run-averaged mean-square vacuum fraction is "
    "(1/k) sum_t x_t^2 = Theta(r/(2 C(Gamma,2) n ln n)) and the "
    "maturity-n instantaneous mean-square is x*^2 = r/(4 C(Gamma,2) "
    "n ln n) (1+o(1)) (the factor 2 is the early-history integral; "
    "verified decisively: late-window ratio 1.098 +/- 0.051 against "
    "the alternative constant reading 2.0). (iv) Time-averaged "
    "lapse^2 = <x> <= sqrt(<x^2>) = O(sqrt(r/(2 C(Gamma,2))) "
    "(n ln n)^{-1/2}) - THEOREM at E-level by Cauchy-Schwarz; the "
    "matching lower bound for <x> is CONJECTURE (x is a sawtooth "
    "with relative amplitude ~ 2 sqrt(r ln n / n); it does NOT "
    "concentrate pointwise at accessible n - only the mean-square "
    "law is theorem-grade). Tick rate: E[S^V] = Gamma <x>, same "
    "bounds times Gamma. (v) FULL-LAPSE RECURRENCE IS "
    "Gamma-STRATIFIED: at Gamma = 2, S^V = 2 = Gamma at every "
    "burst, so every burst is a Phi = 1 step - full lapse recurs "
    "i.o. a.s. (THEOREM, via R53 U-growth: bursts recur a.s. for "
    "m < Gamma). For Gamma >= 3, P(Phi = 1 | state) = "
    "C(D,Gamma)/C(F+D,Gamma) ~ x^Gamma; under the band law "
    "sum_t x_t^Gamma = integral (4 n ln n / r) x*^Gamma dn "
    "diverges for Gamma <= 4 (as n^{1/2}/sqrt(ln n) at Gamma = 3, "
    "as ln ln n at Gamma = 4) and CONVERGES for Gamma = 5: "
    "conditional Borel-Cantelli gives Phi = 1 i.o. for Gamma <= 4 "
    "and only finitely many full-lapse steps for Gamma = 5 "
    "(CONJECTURE grade for Gamma >= 3: rests on the band law's "
    "conjectural side). (vi) Renewals (F = 0, m = 0): the renewal "
    "event at F = 0 is exact (R53); per-cycle probability of an "
    "uninterrupted drain is exp(-Theta(D log D)) (L4), so the "
    "renewal duty cycle vanishes super-polynomially (BOUND); "
    "whether F = 0 recurs a.s. infinitely often in the late regime "
    "is OPEN (R53 established the renewal mechanism and early-"
    "regime recurrence, not late-regime i.o. recurrence). When a "
    "renewal or a Gamma = 2 burst occurs the spike amplitude is "
    "exactly 1 while the drain floor -> 0: fixed amplitude, "
    "vanishing duty cycle."},
 "L6": {"verdict": "THEOREM/BOUND (k-n two-sided; b exact bounds; N_V "
                   "upper THEOREM, matching lower CONJECTURE)",
  "statement": "Three ages plus burst count, all E-level with explicit "
    "constants. (i) k(n) = sum_{j<n} c_j / r = (2/r) n^2 ln n "
    "(1 + o(1)) two-sided via the R59 paths-form band [2,8] j ln j "
    "and r = Gamma + min(H, 2 Gamma) - m (second-order term -n^2/r; "
    "~5% at n ~ 10^3). (ii) b in [(n-2)/C(Gamma,2), n-2] pathwise "
    "THEOREM; b = n - 2 exactly at Gamma = 2. (iii) N_V = "
    "sum_t S^V = Gamma sum_t x_t <= Gamma k sqrt(<x^2>) = "
    "O(Gamma sqrt(2/(C(Gamma,2) r)) n^{3/2} sqrt(ln n)) - upper "
    "THEOREM at E-level; the matching-order lower bound is "
    "CONJECTURE (band law). The carried registered form "
    "N_V ~ Gamma n^2 ln ln n/(2(Gamma+H-m)) is REFUTED (it "
    "presupposed the ln ln n/ln n lapse decay); the corrected "
    "scale is n^{3/2} sqrt(ln n). (iv) dN_V/dk = Gamma <x> = "
    "O((n ln n)^{-1/2}) - supersedes the carried "
    "Gamma ln ln n/(4 ln n). (v) INVARIANT ORDERING: the four ages "
    "are polynomially separated, b ~ n << N_V ~ n^{3/2} sqrt(ln n) "
    "<< k ~ n^2 ln n - exponents (1, 3/2, 2) up to logarithmic "
    "factors (upper THEOREM / lower-matching BOUND-CONJECTURE as "
    "in (iii))."},
 "L7": {"verdict": "BOUNDED (refinement law exact; depth band "
                   "corrected to [1, 2e] in ln-units); "
                   "REGIONS = JOINT_ONLY",
  "statement": "(i) AMBIENT DEPTH DEFINED FROM SOURCE: D_ambient := "
    "the region word depth = max over present objects of birth depth "
    "(A13R: a tick born at depth b reads epsilon 3^{D-b} at ambient "
    "depth D; the region's word depth is the maximal constructor "
    "word length = max object depth). (ii) MAX-DEPTH LAW (uniform "
    "two-parent attachment, R59 T1): E-level band ln n (1 - o(1)) "
    "<= E[M_n] <= 2e ln n (1 + o(1)). Upper: P(w in parent pair) <= "
    "2/(n-2) exactly, so E[N_d(n+1)] <= E[N_d(n)] + (2/(n-2)) "
    "E[N_{d-1}(n)], giving E[N_d(n)] <= (2 H_{n-3} + 2)^d / d! and "
    "the 2e constant by Poisson-tail summation (certified: the "
    "bound holds at every exhaustively enumerated point n <= 10). "
    "Lower: max >= average and the average-depth recursion "
    "E[depth(new) | state] >= 1 + T-linear form with summable "
    "exclusion bias => E[avg depth] >= H_n - O(1). Pathwise exact: "
    "chains(x) <= 2^{depth(x)} (induction; 173/173 on the frozen "
    "universe). Labeled readout: M_n / ln n ~ 3.6-4.3 at n = "
    "10^3..10^6, inside the band; the earlier registered guess "
    "[1, 2] is REFUTED (readout 3.58 at n = 10^3, 40/40 seeds). "
    "(iii) REFINEMENT LAW (exact): the direct-limit reading "
    "R = sum_v epsilon 3^{M - b(v)} multiplies every existing "
    "contribution by exactly 3 at each unit increment of the "
    "region word depth; R >= N_V always, and the reading is "
    "dominated by the shallowest-born ticks (readout: "
    "R/3^{M} tabulated, labeled). No interpretation of the "
    "reading is offered. (iv) REGIONS: JOINT_ONLY - R52 Section "
    "4.1 fixes regions by the inherited prefix map with the joint "
    "region effective at the constructor level; no source-declared "
    "per-region ledger split exists in the frozen UEQ0/CD2R "
    "sources; whether x can differ across regions is therefore not "
    "derivable (recorded, no claim)."},
 "L8": {"verdict": "PROVEN",
  "statement": "F >= m at every step (m is injected before service; "
    "costs and backlog only add), so at drained states (B = 0, no "
    "fresh burst) F = m and E[Phi^2 | drained, D] = D/(m + D) = "
    "1 - m/(m + D) -> 1 as D grows: the persistent-load lapse "
    "deficit at drained states is exactly m/(m + D) <= m/D, fading "
    "with maturity - while the drain-rate effect of m persists "
    "undiminished (r = Gamma + min(H, 2 Gamma) - m at every "
    "maturity). Exact statement and bound; no numeric threshold. "
    "Band Gamma <= m <= Gamma + H: OPEN, recorded, no claim."},
}

M7_PREDICTIONS = [
 {"id": "M7-1", "class": "THEOREM",
  "statement": "In E0 the lapse is identically 1 and the tick rate "
   "equals the object count, rising; E0 is nonempty at genesis iff "
   "m + 2 <= Gamma and its exit at D > Gamma is permanent."},
 {"id": "M7-2", "class": "THEOREM",
  "statement": "In E1 the tick rate and the lapse are the same "
   "observable: S^V = Gamma Phi^2 pathwise, E[Phi^2 | state] = "
   "D/(F+D), P(Phi = 1) = C(D,Gamma)/C(F+D,Gamma); the full "
   "hypergeometric case table holds exactly in all three regimes."},
 {"id": "M7-3", "class": "THEOREM",
  "statement": "At E1 entry the expected lapse drops strictly below 1 "
   "at every registered point except where the entry burst has zero "
   "cost (Gamma = 2, m = 0), where the drop is deferred exactly one "
   "step; the entry distribution is a finite mixture of "
   "hypergeometrics, exact per point."},
 {"id": "M7-4", "class": "THEOREM",
  "statement": "Over a completed pure-drain cycle of injected cost C "
   "at maturity D, the cycle-averaged lapse^2 equals 1 - "
   "C/(Gamma E[tau]) with E[tau] = (C + D H_C)/Gamma (1 + "
   "O(Gamma/D)); for C = c D ln D it tends to the positive constant "
   "1/(1+c): the average lapse over a completed drain does not "
   "vanish with maturity."},
 {"id": "M7-5", "class": "THEOREM",
  "statement": "Uninterrupted full drains die out with maturity: the "
   "expected number of mid-drain burst triggers per full drain is "
   "(1/Gamma) D ln D (1+o(1)) and the probability of completing a "
   "drain without a burst is exp(-Theta(D log D))."},
 {"id": "M7-6", "class": "THEOREM (mean-square, E-level); upper bound "
   "for the mean",
  "statement": "In the late regime the mean-square vacuum-service "
   "fraction at maturity n is x*^2 = r/(4 C(Gamma,2) n ln n) "
   "(1+o(1)) with r = Gamma + min(H, 2 Gamma) - m (run-average "
   "twice that); hence the maturity-indexed time-averaged lapse^2 "
   "is at most sqrt(r/(2 C(Gamma,2))) (n ln n)^{-1/2} (1+o(1)), "
   "and the tick rate is Gamma times the lapse^2 average."},
 {"id": "M7-7", "class": "BOUND",
  "statement": "Relief saturates: the long-run voiding rate is "
   "exactly H for H <= 2 Gamma - 1 and 2 Gamma (1 - x) for H >= "
   "2 Gamma (attracting fixed point P* = 10 Gamma - 6, quota "
   "2 Gamma); adding relief capacity beyond 2 Gamma changes "
   "nothing in the late regime."},
 {"id": "M7-8", "class": "THEOREM at Gamma = 2; CONJECTURE for "
   "Gamma >= 3",
  "statement": "Full-lapse recurrence is Gamma-stratified: at "
   "Gamma = 2 every burst is a Phi = 1 step, so full lapse recurs "
   "unboundedly often; for Gamma = 3, 4 the conditional-probability "
   "sum diverges (recurrence expected i.o.), for Gamma = 5 it "
   "converges (finitely many full-lapse steps expected). The "
   "recurring spike amplitude is exactly 1 while the drain floor "
   "tends to 0: fixed amplitude, vanishing duty cycle."},
 {"id": "M7-9", "class": "THEOREM (b, k two-sided; N_V upper); "
   "CONJECTURE (N_V matching lower)",
  "statement": "The process's ages are polynomially separated: "
   "burst count b in [(n-2)/C(Gamma,2), n-2] (exactly n-2 at "
   "Gamma = 2); process time k = (2/r) n^2 ln n (1+o(1)) "
   "two-sided; cumulative tick count N_V = "
   "O(Gamma sqrt(2/(C(Gamma,2) r)) n^{3/2} sqrt(ln n)) - "
   "exponents (1, 3/2, 2) in maturity up to logarithmic factors."},
 {"id": "M7-10", "class": "THEOREM",
  "statement": "Persistent-load dependence fades from the lapse but "
   "not from the drain: the drained-state lapse deficit is exactly "
   "m/(m+D) -> 0 with maturity, while the drain rate carries -m "
   "undiminished at every maturity."},
 {"id": "M7-11", "class": "THEOREM (refinement exact; depth band "
   "E-level)",
  "statement": "The direct-limit clock reading multiplies every "
   "existing contribution by exactly 3 at each unit increment of "
   "the region word depth; the word depth grows logarithmically in "
   "maturity with E-level band [ln n (1-o(1)), 2e ln n (1+o(1))], "
   "and chains(x) <= 2^{depth(x)} pathwise."},
 {"id": "M7-12", "class": "RECORD",
  "statement": "REGIONS = JOINT_ONLY: no source-declared per-region "
   "ledger split exists; regional load inhomogeneity of x is not "
   "derivable and no claim is made."},
]

HC = [
 ["HC1", "target altered after Commit A / prediction added after "
  "readouts", "REJECTED", "Targets adjudicated verbatim; the M7 set "
  "was derived from the L1-L8 derivations, panel-verified, and "
  "sealed at Commit B before any holdout contact."],
 ["HC2", "external referent; H3-H5 consulted/named/described",
  "REJECTED", "Package vocabulary only; sentinels parsed=false."],
 ["HC3", "rate-in-process-time statement in the prediction set",
  "REJECTED", "Every sealed statement is maturity-indexed, pathwise, "
  "or a cross-age relation of the process's own clocks; no "
  "per-step-policy rate is compared to anything external."],
 ["HC4", "reinterpretation of Phi or the clock", "REJECTED",
  "Phi^2 = S^V/V0 and the A13R tick action used verbatim; the "
  "reading is computed, not interpreted."],
 ["HC5", "readouts cited as proof; unlabeled asymptotics", "REJECTED",
  "Every asymptotic clause carries finite-n bounds or CONJECTURE; "
  "readout tables labeled; the depth and RMS readouts inform no "
  "verdict class."],
 ["HC6", "TG1/cost law/filtration/A13R modified", "REJECTED",
  "All used verbatim; the corrections target the package's CARRIED "
  "approximations (constant-rate drain, O(1) mid-drain bursts, "
  "ln ln n/ln n decay, N_V form, depth band), not frozen laws."],
 ["HC7", "BELL2 opened", "REJECTED", "Unopened."],
 ["HC8", "hand hash; placeholder", "REJECTED",
  "All hashes in-process; no placeholders in sealed outputs."],
]

VERDICTS = {
 "always": "OD0_R60_PASS_M7_LAPSE_CLOCK_EPOCH_LAWS_FROZEN",
 "components": {
  "L1": "PROVEN", "L2": "PROVEN", "L3": "PROVEN",
  "L4": "PROVEN(corrected: cycle-average D H_C/(C + D H_C) -> "
        "1/(1+c) constant, NOT ln(1+4 ln n)/(4 ln n); mid-drain "
        "bursts Theta(D log D), NOT O(1); relief v* = min(H, "
        "2 Gamma))",
  "L5": "PROVEN at mean-square E-level (balance-band law replaces "
        "Theta(ln ln n/ln n); mean lower + concentration "
        "CONJECTURE; full-lapse recurrence Gamma-stratified)",
  "L6": "THEOREM/BOUND (k, b two-sided; N_V = O(n^{3/2} "
        "sqrt(ln n)) upper, corrected from n^2 ln ln n; matching "
        "lower CONJECTURE)",
  "L7": "BOUNDED (depth band [1, 2e] ln n, corrected from [1,2]; "
        "refinement law exact); REGIONS = JOINT_ONLY",
  "L8": "PROVEN",
  "LATE_DECAY": "mean-square (n ln n)^{-1/2} scale proven E-level; "
                "ln ln n/ln n REFUTED",
  "THREE_AGES": "b ~ n; N_V ~ n^{3/2} sqrt(ln n) (upper); "
                "k ~ (2/r) n^2 ln n; exponents (1, 3/2, 2)",
  "REGIONS": "JOINT_ONLY",
 },
 "prediction_vs_outcome": "Registered: L1-L3 PROVEN exactly - "
  "outcome: yes. L4 registered the linear-drain constant "
  "ln(1 + 4 ln n)/(4 ln n) - REFUTED by the exact drain induction; "
  "the correct cycle law is 1 - C/(Gamma E[tau]) = D H_C/(C + D "
  "H_C) -> 1/(1+c), and the O(1) mid-drain-burst note fails "
  "(Theta(D log D)). L5 registered Theta(ln ln n/ln n) BOUNDED - "
  "REPLACED: the balance-band mean-square law (n ln n)^{-1/2} "
  "scale, upper THEOREM. L6 registered N_V ~ Gamma n^2 ln ln n/"
  "(2(Gamma+H-m)) - REFUTED; corrected to O(n^{3/2} sqrt(ln n)). "
  "L7 registered depth constant in [1, 2] - REFUTED (readout 3.6+; "
  "proven band [1, 2e]); regions JOINT_ONLY as registered. L8 "
  "PROVEN as registered. Prediction set sealed with 12 statements, "
  "7 carrying THEOREM grade (>= 5 required). The registered "
  "prediction constrained nothing.",
 "r61_recommendation": "L1-L4 and L6 close at THEOREM/BOUND grade "
  "and the M7 set is sealed, so per the R60 rule: R61 preregisters "
  "the H3 and H4 comparison protocols (mirroring R56: extraction by "
  "definition at opening; reparametrization-invariant shapes only; "
  "advance PASS/PARTIAL/FAIL rule; mandatory model-family caveat), "
  "and pins any still-missing H3/H4 artifacts (R48: v31l-v31o "
  "sources; DEU_voids G2c line in SOURCE_CONFLICT). R62 opens H3 "
  "and H4 under the sealed protocols, one comparison each, no "
  "repair. H5 stays sealed pending a derived density observable.",
}
