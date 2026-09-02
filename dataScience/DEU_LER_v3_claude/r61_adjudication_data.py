"""OD0-R61 adjudication data: H3/H4 preregistration round. (Claude Code.)

Part 2 and Part 4 derivations adversarially panel-verified before
freezing (three referees, instructed to refute).
"""

RUN_DATE = "2026-09-02"

# ---------------------------------------------------------------- Part 2
C5_DERIVED = {
 "id": "C5_DERIVED",
 "status": "derived in R61 before opening",
 "definitions_frozen_R56": {
  "containment": "containment(w) = #{o in X : w in closed_anc(o), "
                 "o != w} (strict descendant count)",
  "coembedding": "coembedding(w1,w2) = #{o in X : {w1,w2} subset "
                 "closed_anc(o)} (common-descendant count)",
  "clock_functionals": "tau = log-compressed totals, verbatim "
                       "historical forms (tau ~ ln ln of the "
                       "respective totals)"},
 "derivation": {
  "total_containment": "TC(n) = sum_w containment(w) = sum_o "
    "(|closed_anc(o)| - 1) by pair double-counting. Exact per-step "
    "recursion: Delta TC = |cone(new)| (certified exhaustively at "
    "n <= 9 against the R59 cone table, and bit-exactly on "
    "trajectories). Order: E[TC(n)] = Theta(n^{3/2}) two-sided "
    "THEOREM at E-level via the R59 proven cone order. CONSTANT "
    "(panel correction, recorded as a forward erratum to R59 T3): "
    "the descendant chain d_j is a rate-2 Yule process in log-time, "
    "so phi_j(n) -> n W/(n W + j^2) with W ~ Exp(1) RANDOM, and the "
    "cone constant carries E[sqrt(W)] = sqrt(pi)/2: E|cone(new at "
    "n)| = (3/8) pi^{3/2} sqrt(n) (1+o(1)) ~ 2.0881 sqrt(n), NOT "
    "(3 pi/4) sqrt(n); hence E[TC(n)] = (pi^{3/2}/4) n^{3/2} ~ "
    "1.3921 n^{3/2}. Three concordant checks: DAG simulation to "
    "n = 30000 (TC/n^{3/2} -> 1.3873, 17+ SE below pi/2); "
    "exact-marginal chains of the certified per-state law "
    "(E|cone|/sqrt(n) = 2.0936 +/- 0.0075 at n = 16000, 35 SE "
    "below 3 pi/4); the exhaustive n = 9 value 6.165 vs 6.26 "
    "predicted vs 7.07 mean-field. Constant grade: branching-limit "
    "derivation at the same rigor level as the mean-field it "
    "corrects (order THEOREM; sharp constant at that level).",
  "total_coembedding": "TCo(n) = sum_{pairs} coembedding = sum_o "
    "C(|closed_anc(o)|, 2); Delta TCo = C(A, 2), A = "
    "|closed_anc(new)|. Bounds: E[C(A,2)] >= (E[A]^2 - E[A])/2 = "
    "Theta(k) (Jensen); E[A^2] = sum_{i,j} P(i,j both ancestors) <= "
    "2 sum_j j a_j(k) = Theta(k ln k). Hence c1 n^2 <= E[TCo(n)] <= "
    "c2 n^2 ln n - two-sided THEOREM at E-level; sharp order n^2 "
    "CONJECTURE (trajectories: TCo/n^2 = 1.26-1.62, stable; "
    "TCo/(n^2 ln n) falling - labeled).",
  "clock_functionals": "tau_C = ln ln TC = ln ln n + ln(3/2) + o(1); "
    "tau_Co = ln ln TCo = ln ln n + ln 2 + o(1) (the log-band on TCo "
    "perturbs by O(ln ln n / ln n); the ln ln form absorbs all "
    "Theta-constants, so the corrected TC constant does not move "
    "these). MUTUAL RELATION: both clocks run at the same ln ln "
    "order (ratio -> 1); the CO-EMBEDDING clock runs AHEAD by the "
    "additive constant ln 2 - ln(3/2) = ln(4/3) = 0.2877 "
    "asymptotically. Labeled: tau_Co - tau_C = 0.265-0.276 at "
    "n ~ 50-80 (round trajectories) and 0.2729 -> 0.2765 at "
    "n = 2000 -> 30000 (panel), tracking the finite-n prediction "
    "with corrected constants (0.2723 -> 0.2763) toward ln(4/3). "
    "Grade: orders THEOREM (E-level, with the TCo log band); the "
    "ln(4/3) offset BOUND (exact under the sharp-n^2 conjecture, "
    "[ln(4/3), ln(4/3) + O(lnln/ln)] under the band).",
  "vs_tick_count": "N_V = O(n^{3/2} sqrt(ln n)) (R60): TC and N_V "
    "share the n^{3/2} scale up to sqrt(ln n) - the containment "
    "clock total and the tick count are polynomially locked "
    "(exponent 3/2 in maturity), while TCo runs at exponent 2, the "
    "same as process time k up to logs. Clock-vs-clock and "
    "clock-vs-object-count relations comparable; anything vs "
    "process steps recorded but excluded from the protocols.",
  "correction_to_registered": "The registered prediction guessed "
    "both totals at n^{3/2} with containment ahead. Outcome: TCo "
    "is n^2-scale (each new object contributes C(A,2) ~ A^2/2 "
    "pairs, not A), and the co-embedding clock is AHEAD by "
    "ln(4/3). Additionally the panel corrected the cone constant "
    "itself (forward erratum to R59 T3, see "
    "OD0_R61_COUNTEREXAMPLES.md). Recorded as corrections."},
}

# ---------------------------------------------------------------- Part 4
G7_UPDATED_R61 = {
 "id": "G7_UPDATED_R61",
 "status": "derived in R61 before opening; supersedes the R59/R53 "
           "band statement",
 "statement": "TERMINATION DICHOTOMY AT THE LINE m_c = Gamma + "
   "min(H, 2 Gamma) (stated for the frozen kernel at all parameter "
   "values; registered points have m <= 3): (a) m > m_c: the number "
   "of bursts is finite a.s. - cumulative outflow <= Gamma k + "
   "min(H k, P_0 + 2 sum S^F) <= (Gamma + min(H, 2 Gamma)) k + P_0 "
   "(the P-ledger caps voiding pathwise), so F >= C_k + eps k with "
   "eps = m - m_c > 0; on {infinitely many bursts} the R59 chains "
   "lemma gives per-burst cost -> infinity, so x -> 0 and b_t = "
   "o(t) (Cesaro + martingale SLLN), the conditional burst "
   "intensity obeys <= c (b_t/t)^2, and conditional Borel-Cantelli "
   "plus the discrete Gronwall telescope 1/S_{k-1} - 1/S_k <= "
   "4c/k^2 (equivalently a monotone coupling to a pure-birth chain "
   "killed by Levy's 0-1 law) arrests b at a finite value - "
   "contradiction. STRENGTHENS R59 (m > Gamma + H) whenever "
   "H > 2 Gamma. Panel-verified, including from adversarially "
   "matured states (m switched above the line at n ~ 130: bursts "
   "arrest, hazard sum converges). (b) m < m_c: unbounded growth "
   "a.s. - for F large, voiding runs at v* = min(H, 2 Gamma (1-x)) "
   "(H >= 2 Gamma: the attracting orbit P* = 10 Gamma - 6; H <= "
   "2 Gamma - 1: the P-ledger diverges and v = H every step, gate "
   "trivially open), so the non-burst drift m - Gamma(1-x) - v* "
   "-> m - m_c < 0 as x -> 0; with F_0(n) = Theta(n^{3/2} "
   "sqrt(log n)) (genuinely required: the burst-injection term "
   "C(Gamma,2) x^2 c_n is o(1) only there, and drift is positive "
   "at moderate x), F returns below F_0(n) i.o. (block "
   "supermartingale; the one-step P-dip after a quota-2 void is "
   "absorbed in 2-step blocks); below F_0(n), x >= p(n) > 0 and a "
   "burst occurs within geometric time (absent pairs exist at "
   "every n) - the R53 drift-band pattern extended through the "
   "relief band (renewals F = 0 never occur for m >= Gamma and "
   "are not needed). (c) THE LINE m = m_c: OPEN - the leading "
   "drift cancels and the residual drift is +Gamma x (H <= "
   "2 Gamma - 1) or +3 Gamma x (H >= 2 Gamma), giving F ~ "
   "sqrt(2 Gamma D t) resp. sqrt(6 Gamma D t) and log-divergent "
   "burst sums: genuinely critical, slow i.o. bursts not "
   "excluded. Labeled illustration (Gamma=2, H=8, m_c=6, 30000 "
   "steps): m=3,4,5 grow throughout; m=6: F = 830 ~ sqrt(24 t) "
   "(the sqrt-critical signature; expected bursts by this horizon "
   "~0.5, observed 0); m=7,8: F = 30119/60056 (linear), zero "
   "bursts. Gamma=3, H=2 (m_c=5): m=3,4 grow; m=5 log-slow "
   "sporadic growth then quiet; m=6: growth freezes a.s. (the "
   "process does not halt; bursts stop).",
}

RELIEF_LINE = {
 "a_termination": "PROVEN (a.s.) for m > Gamma + min(H, 2 Gamma)",
 "b_persistence": "PROVEN (a.s.) for m < Gamma + min(H, 2 Gamma)",
 "c_line": "OPEN (critical: residual +3 Gamma x drift, sqrt-t "
           "forced-pool growth, log-divergent burst sums)",
}

# ------------------------------------------------- derived-side tables
H3_TABLE = [
 ["G1", "E0: Phi = 1 identically; no load effect", "THEOREM"],
 ["G2", "E1 entry: sharp lapse drop with an exact per-point law "
  "(deferred one step only at the zero-cost entry point Gamma=2, "
  "m=0)", "THEOREM"],
 ["G3", "Late regime: band-average lapse^2 decreases with object "
  "count, O((n ln n)^{-1/2})", "THEOREM (upper) / BOUND"],
 ["G4", "Fixed amplitude (Phi = 1 at bursts) with vanishing duty "
  "cycle", "THEOREM at Gamma=2; Gamma-stratified recurrence at "
  "Gamma >= 3 CONJECTURE"],
 ["G5", "Persistent load: drained-state lapse deficit exactly "
  "m/(m+D), fading; drain-rate effect persists", "THEOREM"],
 ["G6", "Relief: attracting fixed point P* = 10 Gamma - 6; voiding "
  "rate capped at 2 Gamma", "THEOREM"],
 ["G7", "Termination dichotomy in m at the line m_c = Gamma + "
  "min(H, 2 Gamma); line itself open (G7_UPDATED_R61)", "THEOREM "
  "(both sides of the line; line OPEN)"],
 ["G8", "No spatial variation derivable (JOINT_ONLY)", "DECLARED"],
]

H4_TABLE = [
 ["C1", "Tick rate = Gamma Phi^2 in E1; = D in E0 (clock and lapse "
  "are one observable)", "THEOREM"],
 ["C2", "Tick rate maximal in E0, decreasing in the band",
  "THEOREM/BOUND"],
 ["C3", "Three ages: exponent ordering objects (1) < ticks (3/2) < "
  "process steps (2), up to logs; N_V vs n comparable; anything vs "
  "rounds excluded", "BOUND"],
 ["C4", "Direct-limit reading: x3 per depth increment; depth in "
  "[ln n, 2e ln n]", "THEOREM (band)"],
 ["C5", "Containment and co-embedding clocks nondecreasing "
  "(THEOREM); growth orders and mutual relation per C5_DERIVED: "
  "TC ~ (pi^{3/2}/4) n^{3/2}; TCo in [c1 n^2, c2 n^2 ln n]; both "
  "clocks ~ ln ln n with the co-embedding clock ahead by ln(4/3)",
  "THEOREM (orders, E-level) / BOUND (offset)"],
 ["C6", "Gamma-stratified recurrence of full tick rate", "THEOREM "
  "at Gamma=2; CONJECTURE otherwise"],
]

EXCLUSIONS = [
 "All Tier D quantities: dimensionful or empirically calibrated "
 "values (growth-of-structure parameters, expansion-rate values, "
 "registry factors used as calibration, SI dictionaries) - recorded "
 "as historical values, excluded from comparison",
 "All rates versus rounds (rounds are policy indices; monotone "
 "reparametrization invariance required)",
 "All spatial/regional variation claims - declared "
 "UNMAPPED_INAPPLICABLE now, before opening (regions JOINT_ONLY)",
 "Any calibrated dictionary",
]

PROTOCOL_RULE = {
 "compared": "Reported patterns invariant under monotone "
   "reparametrization of rounds - onset of the load effect, "
   "direction and monotonicity of its change with maturity, "
   "saturation or persistence of oscillation, dependence on "
   "capacity or persistent load, clock-versus-clock and "
   "clock-versus-object-count relations, early-versus-late clock "
   "behavior - against the derived-side table and the frozen R56 "
   "observables, mapped BY DEFINITION at opening. Names, words, "
   "counts are not maps.",
 "rule": "PASS iff every mapped reparametrization-invariant pattern "
   "is consistent with the corresponding THEOREM-grade statement "
   "and none contradicts one; PARTIAL if consistent but a "
   "stage-defining historical observable is unmapped or matches "
   "only at BOUND/READOUT/CONJECTURE grade; FAIL if a THEOREM-grade "
   "statement is contradicted. Mismatches at equal prominence.",
 "forbidden": "Round-number alignment; any statement added, "
   "criterion moved, observable renamed, or tower repaired in the "
   "opening round.",
 "model_family_caveat": "MANDATORY at opening: the projection "
   "family's derivation chain (which parts are state fields, which "
   "are calibrations) from the R48 F5 classification (state field / "
   "derived observable / external calibration / phenomenological "
   "projection / fixed bridge assumption / manuscript-only).",
}

HC = [
 ["HC1", "sections 4.1/4.2/5 altered after Commit A beyond the "
  "hashed Part 2/Part 4 appendices", "REJECTED",
  "Tables and protocols frozen in R61_INPUT_LOCK.json verbatim; "
  "C5_DERIVED and G7_UPDATED_R61 are the two permitted hashed "
  "appendices, derived before any opening."],
 ["HC2", "H3/H4 content read; sentinels not false", "REJECTED",
  "Pinning is byte-hash and filename only; sentinels parsed=false "
  "at start and end."],
 ["HC3", "Tier D quantity, rate-versus-rounds, or spatial claim in "
  "a protocol", "REJECTED", "Excluded by construction in both "
  "sealed objects."],
 ["HC4", "external referent", "REJECTED", "None appears."],
 ["HC5", "TG1/cost law/filtration/A13R modified", "REJECTED",
  "All used verbatim."],
 ["HC6", "readouts cited as proof", "REJECTED",
  "Clock-functional and relief-line trajectory tables are labeled; "
  "verdict classes rest on derivations, panel-verified."],
 ["HC7", "BELL2 opened", "REJECTED", "Unopened."],
 ["HC8", "hand hash; placeholder", "REJECTED",
  "All hashes in-process; no placeholders."],
]

PANEL_VERDICTS = {
 "note": "Three-referee adversarial panel (independent derivation + "
         "simulation, instructed to refute) on the Part 2 / Part 4 "
         "derivations before freezing.",
 "V1_clock_totals": "CORRECTED - the cone/TC constant is the "
   "Yule-limit value (3/8) pi^{3/2} resp. pi^{3/2}/4 (E[sqrt(W)] = "
   "sqrt(pi)/2 factor, W ~ Exp(1)); forward erratum to R59 T3 "
   "recorded; TCo band and the ln(4/3) offset confirmed; sharp "
   "TCo = Theta(n^2) supported (E[A^2]/E[A]^2 -> ~1.13)",
 "V2_line_termination": "CONFIRMED (proof completion: conditional "
   "Borel-Cantelli + discrete Gronwall, or monotone pure-birth "
   "coupling + Levy 0-1; verified from matured states)",
 "V3_band_persistence": "CONFIRMED (regime-split relief behavior; "
   "F_0(n) = Theta(n^{3/2} sqrt(log n)); 2-step block "
   "supermartingale; zero gate closures in ~10^6 large-F steps; "
   "cost-throughput identity matches in every in-band run)",
}

VERDICTS = {
 "always": "OD0_R61_PASS_H3_H4_PREREGISTERED",
 "components": {
  "C5_DERIVED": "TC ~ (pi^{3/2}/4) n^{3/2} (order THEOREM; "
                "Yule-corrected constant); TCo in [c1 n^2, "
                "c2 n^2 ln n] THEOREM (sharp n^2 CONJECTURE); "
                "co-embedding clock ahead by ln(4/3); both ~ ln ln n",
  "RELIEF_LINE": "CLOSED to the line m_c = Gamma + min(H, 2 Gamma) "
                 "(both sides PROVEN a.s.); the line itself OPEN "
                 "(sqrt-critical)",
  "ARTIFACTS": "H3: 17/17 pinned unchanged, 9 non-manuscript, not "
               "PAPER_ONLY; H4: 26/26 pinned unchanged, 20 "
               "non-manuscript, not PAPER_ONLY; DEU_voids line "
               "pinned (SOURCE_CONFLICT recorded); v31l/m/n FOUND "
               "(newly located), v31o MISSING",
 },
 "prediction_vs_outcome": "Both preregistrations sealed - as "
  "registered. C5: registered both totals at n^{3/2} with the "
  "containment clock ahead - CORRECTED twice: TCo is n^2-scale "
  "(each new object contributes C(A,2) pairs) with the "
  "CO-EMBEDDING clock ahead by ln(4/3); and the panel found the "
  "cone/TC constant itself is the Yule-limit value (forward "
  "erratum to R59 T3: (3/8) pi^{3/2}, not 3 pi/4). Relief line: "
  "(a) and (b) PROVEN as registered; (c) open as registered, with "
  "the sharper critical picture (residual +Gamma x / +3 Gamma x "
  "drift, F ~ sqrt(t)). Artifacts: registered 'H4 at least partly "
  "PAPER_ONLY; v31l-v31o missing unless supplied' - outcome "
  "better: both corpora carry non-manuscript artifacts (no "
  "PAPER_ONLY), and v31l/m/n were located (only v31o missing). "
  "The prediction constrained nothing.",
 "r62_recommendation": "Both preregistrations sealed with L-grade "
  "tables and hashed appendices, so per the R62 rule: R62 opens H3 "
  "and H4 under their sealed protocols, one comparison each, no "
  "repair, in one round - two separate adjudications, two separate "
  "verdicts, one report, mirroring R54/R57 exactly. The v31o gap "
  "and the DEU_voids SOURCE_CONFLICT are carried into the H3 "
  "opening at equal prominence. H5 remains sealed until a derived "
  "density observable exists.",
}
