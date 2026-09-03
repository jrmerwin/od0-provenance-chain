# OD0-R61 Report: H3/H4 Preregistration, Clock Functionals,
# and the Relief-Band Line

Run date: 2026-09-02. Verdict: **OD0_R61_PASS_H3_H4_PREREGISTERED**.

## Position
R60 stamp and the M7 prediction hash pinned and verified. Sections 4-6
frozen verbatim at Commit A. H3-H5 sentinels parsed=false at start and
end; artifact pinning touched byte hashes and filenames only.

## The two sealed preregistrations
- **H3 (load maturation)**: derived-side table G1-G8 (6 THEOREM-grade
  rows) + G7_UPDATED_R61; sealed sha256 = ede9c8f75e17211f72c4374f5562b914aee58ea6cce0841d8aafc737c15624a8
- **H4 (clocks)**: derived-side table C1-C6 + C5_DERIVED appendix;
  sealed sha256 = 2916ddb0af1ba67e5c77d84727cf99111afdbced623de678a2e32fccc4cf6649

Both exclude, by construction: Tier D quantities, rates versus rounds,
spatial/regional claims (UNMAPPED_INAPPLICABLE), calibrated
dictionaries. Mapping is by definition at opening; the model-family
caveat (R48 F5) is mandatory.

## Part 2 - C5_DERIVED (appendix sha256 = aa1c6fb2db05c154a42e1b3262562c9436a005ba9965eac5776cf164f67eddcd)
TC(n) = sum_w containment(w) = sum_o (|closed_anc(o)| - 1) by pair double-counting. Exact per-step recursion: Delta TC = |cone(new)| (certified exhaustively at n <= 9 against the R59 cone table, and bit-exactly on trajectories). Order: E[TC(n)] = Theta(n^{3/2}) two-sided THEOREM at E-level via the R59 proven cone order. CONSTANT (panel correction, recorded as a forward erratum to R59 T3): the descendant chain d_j is a rate-2 Yule process in log-time, so phi_j(n) -> n W/(n W + j^2) with W ~ Exp(1) RANDOM, and the cone constant carries E[sqrt(W)] = sqrt(pi)/2: E|cone(new at n)| = (3/8) pi^{3/2} sqrt(n) (1+o(1)) ~ 2.0881 sqrt(n), NOT (3 pi/4) sqrt(n); hence E[TC(n)] = (pi^{3/2}/4) n^{3/2} ~ 1.3921 n^{3/2}. Three concordant checks: DAG simulation to n = 30000 (TC/n^{3/2} -> 1.3873, 17+ SE below pi/2); exact-marginal chains of the certified per-state law (E|cone|/sqrt(n) = 2.0936 +/- 0.0075 at n = 16000, 35 SE below 3 pi/4); the exhaustive n = 9 value 6.165 vs 6.26 predicted vs 7.07 mean-field. Constant grade: branching-limit derivation at the same rigor level as the mean-field it corrects (order THEOREM; sharp constant at that level).

TCo(n) = sum_{pairs} coembedding = sum_o C(|closed_anc(o)|, 2); Delta TCo = C(A, 2), A = |closed_anc(new)|. Bounds: E[C(A,2)] >= (E[A]^2 - E[A])/2 = Theta(k) (Jensen); E[A^2] = sum_{i,j} P(i,j both ancestors) <= 2 sum_j j a_j(k) = Theta(k ln k). Hence c1 n^2 <= E[TCo(n)] <= c2 n^2 ln n - two-sided THEOREM at E-level; sharp order n^2 CONJECTURE (trajectories: TCo/n^2 = 1.26-1.62, stable; TCo/(n^2 ln n) falling - labeled).

tau_C = ln ln TC = ln ln n + ln(3/2) + o(1); tau_Co = ln ln TCo = ln ln n + ln 2 + o(1) (the log-band on TCo perturbs by O(ln ln n / ln n); the ln ln form absorbs all Theta-constants, so the corrected TC constant does not move these). MUTUAL RELATION: both clocks run at the same ln ln order (ratio -> 1); the CO-EMBEDDING clock runs AHEAD by the additive constant ln 2 - ln(3/2) = ln(4/3) = 0.2877 asymptotically. Labeled: tau_Co - tau_C = 0.265-0.276 at n ~ 50-80 (round trajectories) and 0.2729 -> 0.2765 at n = 2000 -> 30000 (panel), tracking the finite-n prediction with corrected constants (0.2723 -> 0.2763) toward ln(4/3). Grade: orders THEOREM (E-level, with the TCo log band); the ln(4/3) offset BOUND (exact under the sharp-n^2 conjecture, [ln(4/3), ln(4/3) + O(lnln/ln)] under the band).

N_V = O(n^{3/2} sqrt(ln n)) (R60): TC and N_V share the n^{3/2} scale up to sqrt(ln n) - the containment clock total and the tick count are polynomially locked (exponent 3/2 in maturity), while TCo runs at exponent 2, the same as process time k up to logs. Clock-vs-clock and clock-vs-object-count relations comparable; anything vs process steps recorded but excluded from the protocols.

## Part 3 - Artifacts
H3: 17/17 present, hashes unchanged, 9 non-manuscript artifacts (not
PAPER_ONLY). H4: 26/26 present, unchanged, 20 non-manuscript (not
PAPER_ONLY). DEU_voids source line pinned at commit
3537e7c74f641870cbcdc2dcca110ac74b286560
(SOURCE_CONFLICT recorded). v31l/m/n FOUND (correcting the carried
missing-list); v31o MISSING.

## Part 4 - The relief-band line (appendix sha256 = e2f781147700fe8db1f34a78f2074301a59d578acf0adb91c31ab3cb144ef072)
TERMINATION DICHOTOMY AT THE LINE m_c = Gamma + min(H, 2 Gamma) (stated for the frozen kernel at all parameter values; registered points have m <= 3): (a) m > m_c: the number of bursts is finite a.s. - cumulative outflow <= Gamma k + min(H k, P_0 + 2 sum S^F) <= (Gamma + min(H, 2 Gamma)) k + P_0 (the P-ledger caps voiding pathwise), so F >= C_k + eps k with eps = m - m_c > 0; on {infinitely many bursts} the R59 chains lemma gives per-burst cost -> infinity, so x -> 0 and b_t = o(t) (Cesaro + martingale SLLN), the conditional burst intensity obeys <= c (b_t/t)^2, and conditional Borel-Cantelli plus the discrete Gronwall telescope 1/S_{k-1} - 1/S_k <= 4c/k^2 (equivalently a monotone coupling to a pure-birth chain killed by Levy's 0-1 law) arrests b at a finite value - contradiction. STRENGTHENS R59 (m > Gamma + H) whenever H > 2 Gamma. Panel-verified, including from adversarially matured states (m switched above the line at n ~ 130: bursts arrest, hazard sum converges). (b) m < m_c: unbounded growth a.s. - for F large, voiding runs at v* = min(H, 2 Gamma (1-x)) (H >= 2 Gamma: the attracting orbit P* = 10 Gamma - 6; H <= 2 Gamma - 1: the P-ledger diverges and v = H every step, gate trivially open), so the non-burst drift m - Gamma(1-x) - v* -> m - m_c < 0 as x -> 0; with F_0(n) = Theta(n^{3/2} sqrt(log n)) (genuinely required: the burst-injection term C(Gamma,2) x^2 c_n is o(1) only there, and drift is positive at moderate x), F returns below F_0(n) i.o. (block supermartingale; the one-step P-dip after a quota-2 void is absorbed in 2-step blocks); below F_0(n), x >= p(n) > 0 and a burst occurs within geometric time (absent pairs exist at every n) - the R53 drift-band pattern extended through the relief band (renewals F = 0 never occur for m >= Gamma and are not needed). (c) THE LINE m = m_c: OPEN - the leading drift cancels and the residual drift is +Gamma x (H <= 2 Gamma - 1) or +3 Gamma x (H >= 2 Gamma), giving F ~ sqrt(2 Gamma D t) resp. sqrt(6 Gamma D t) and log-divergent burst sums: genuinely critical, slow i.o. bursts not excluded. Labeled illustration (Gamma=2, H=8, m_c=6, 30000 steps): m=3,4,5 grow throughout; m=6: F = 830 ~ sqrt(24 t) (the sqrt-critical signature; expected bursts by this horizon ~0.5, observed 0); m=7,8: F = 30119/60056 (linear), zero bursts. Gamma=3, H=2 (m_c=5): m=3,4 grow; m=5 log-slow sporadic growth then quiet; m=6: growth freezes a.s. (the process does not halt; bursts stop).

## Prediction vs outcome
Both preregistrations sealed - as registered. C5: registered both totals at n^{3/2} with the containment clock ahead - CORRECTED twice: TCo is n^2-scale (each new object contributes C(A,2) pairs) with the CO-EMBEDDING clock ahead by ln(4/3); and the panel found the cone/TC constant itself is the Yule-limit value (forward erratum to R59 T3: (3/8) pi^{3/2}, not 3 pi/4). Relief line: (a) and (b) PROVEN as registered; (c) open as registered, with the sharper critical picture (residual +Gamma x / +3 Gamma x drift, F ~ sqrt(t)). Artifacts: registered 'H4 at least partly PAPER_ONLY; v31l-v31o missing unless supplied' - outcome better: both corpora carry non-manuscript artifacts (no PAPER_ONLY), and v31l/m/n were located (only v31o missing). The prediction constrained nothing.

## Hostile controls
All 8 REJECTED (see OD0_R61_RESULTS.json).

## R62
Both preregistrations sealed with L-grade tables and hashed appendices, so per the R62 rule: R62 opens H3 and H4 under their sealed protocols, one comparison each, no repair, in one round - two separate adjudications, two separate verdicts, one report, mirroring R54/R57 exactly. The v31o gap and the DEU_voids SOURCE_CONFLICT are carried into the H3 opening at equal prominence. H5 remains sealed until a derived density observable exists.
