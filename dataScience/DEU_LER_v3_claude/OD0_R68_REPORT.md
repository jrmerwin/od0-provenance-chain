# OD0-R68 Report: The Token-Region Premise Round

Run date: 2026-09-02. Verdict: **OD0_R68_PASS_TOKEN_REGION_CLASS_ADJUDICATED**.

## Position
R67 stamp pinned and verified. TR1' copied verbatim; the class T and
all targets frozen at Commit A. Candidate tests and field laws
referee-computed on the frozen catalogs (exact; raw in
R68_WORKERS_RAW.json).

## Part 1 - the assignment class

 "T0": "inert baseline (all ROOT) - the current tower.",
 "TR1_prime": "TOTAL; READABLE (the A12 anchors are content-determined from recorded propositions - a function of S); S3-COVARIANT (0 mismatches, 6 permutations x both catalogs); SCHEDULE-INVARIANT (anchors recomputed under reversed and Jacobi orders: 0/903 mismatches; serialization permutations: 0 changes); NON-DEGENERATE: non-ROOT fraction 894/903 = 0.990 (903-catalog; 0 ties, 9 all-root) and 1809/2304 = 0.785 (R19; 486 two-way ties, 9 all-root). Tie-break clauses: TWO (majority tie -> ROOT; no depth >= 1 edits -> ROOT - semantically distinct, neither absorbable).",
 "T_DEEP": "TOTAL in the uniform ZERO-CLAUSE form T(x) = common_prefix(argmax-depth anchor cells) - the empty/all-root case is subsumed (the max-depth set of an all-root profile is {ROOT}); extensionally identical to the itemized one-clause form on both catalogs. READABLE; COVARIANT (0 mismatches); SCHEDULE-INVARIANT (0 mismatches). NON-DEGENERATE: 894/903 = 0.990 non-ROOT with assigned depths {1: 270, 2: 282, 3: 342}; R19: 945/2304 = 0.410 (1350 distinct-cell ties -> ROOT). RELATION TO TR1': TR1' is exactly T-DEEP's depth-1 truncation on the whole 903-catalog (894/894 both-localized agree at depth 1; T-DEEP strictly deeper on 624); wherever T-DEEP localizes on R19 it coincides with TR1' (945/945).",
 "T_LAST": "REJECTED: schedule-dependent. The catalogs freeze NO canonical occurrence order (R19 edit lists are content-hash-sorted 2304/2304; the 903 order is a compilation convention); one random re-serialization changes the assignment on 154/903 and 1058/2304 objects (TR1'/T-DEEP: 0 changes).",
 "T_INHERIT": "REJECTED: ROOT-degenerate by induction from genesis (primitives ROOT; deeper-of(ROOT, ROOT) ties to ROOT).",
 "T_PROFILE": "REJECTED: degenerate (the profile's common prefix is ROOT for 903/903 and 2304/2304 - every object has a root-anchored edit).",
 "PLURALITY": "FOUND (the executor-search clause is non-empty, correcting the registered 'none'): full-anchor-multiset plurality (strict-max cell; tie -> ROOT) is a THIRD total, choice-free, covariant, schedule-invariant, non-degenerate candidate (non-ROOT 486/903 = 0.538 and 864/2304 = 0.375). Ranks third: its tie clause is a hard reset, not a refinement, and it conflates root-anchored bookkeeping edits with localization.",
 "survivors": [
  "T_DEEP",
  "TR1_prime",
  "PLURALITY"
 ],
 "minimality": "By the frozen order (readability, covariance, #tie-break clauses): readability and covariance TIE across the three survivors (all functions of S; all covariant); clause count decides: T-DEEP 0 (uniform form) < PLURALITY 1 < TR1' 2. UNIQUE MINIMUM: T-DEEP."


## Part 2 - region set and process

 "RS1": "FIXED_MAP. The spec declares 'the finite inherited prefix-region set R' (R65 P1, verbatim-cited); the frozen fixture is the 10-marker A13R catalog (root + 3 depth-1 + 6 no-repeat depth-2); records/requests/tokens in unmapped cylinders charge to the NEAREST MAPPED ANCESTOR (the smallest inherited region containing the anchor - the frozen compiler rule). Capacity total = k Gamma, CONSTANT: the maturation tower is intact; the ALL_OCCUPIED reading is not source-supported (finiteness is declared) and was not run.",
 "RS2": "Well-defined: the joint state (per-region five-integer ledgers + exchange-canonical ideal + region labels) carries the PRODUCT master kernel of per-region hypergeometric/relief kernels (UEQ0 spec form); normalization certified exactly on a joint-state grid (zero failures); Markov closure inherited from the frozen per-region kernels and the assignment's determinism; the ROOT instantiation is the k = 1 special case; pairing stays uniform over the union of served objects - the R64 no-go is untouched.",
 "RS3": "FIXED_MAP: the global balance-band law (R60) is UNCHANGED IN FORM with r_total = sum of per-region drain constants; per-region bands differ by charge share (see F2). No CAPACITY_GROWING_READING exists to label."


## Part 3 - fields on the record tree

 "F1": "Occupancy: E[records of resolution >= d in a given depth-d cylinder] = N_{>=d}/3^d exactly (uniform symbols, T3). CHARGE-SHARE THEOREM (referee-exact, one-parameter family in the resolution profile (q0, q1, Q2)): s_ROOT = q0 exactly (root receives ONLY resolution-0 records - nothing charges past its depth-1 ancestor); s_depth-1 cell = q1/3 + Q2/9 each; s_mapped depth-2 cell = Q2/9 each; sums to 1 identically. Uniform-depth regime: (1/3; 4/27 x3; 1/27 x6) (round engine, exact + simulated). MATURE LIMIT (Q2 -> 1): (0; 1/9 x3; 1/9 x6) - the fixture EQUALIZES the nine non-root regions and STARVES root.",
 "F2": "Lapse/tick fields: region rho congests when s_rho N > Gamma (threshold Gamma/s_rho). TWO-PHASE VARIATION LAW (VARIATION_DERIVED): early (q0, q1 > 0) the lapse is ordered by charge share - Phi(mapped depth-2) >= Phi(depth-1), root most congested when q0 dominates; at maturity the nine non-root regions congest SIMULTANEOUSLY at N = 9 Gamma (exact equalization by S3 symmetry + share equality) while ROOT NEVER CONGESTS (s_ROOT -> 0): the root region becomes the permanently free region, Phi_ROOT = 1 with full tick rate. d*(N) = log_3(N/Gamma) confirmed as the general-depth boundary law (exact at N/Gamma = 3^d); the frozen depth-<=2 map saturates once d* > 2 (honest fixture caveat).",
 "F3": "Density: rho_rec(depth-d cylinder) = N_{>=d} in expectation - uniform across cylinders at each depth (exact; simulated chi2(8) = 16.4 at N = 9 x 10^4), decreasing in depth until records reach that depth (two-regime form under the bounded-resolution fixture; e.g. profile (1/4, 1/4, 1/2): rho/N = 1, 3/4, 1/2, 0 at depths 0..3, matched by simulation).",
 "F4": "Per-region duality PROVEN: on a depth-d0 cylinder the G2 pairing factors EXACTLY into the prefix phase times the tail pairing (14,661 exact checks, zero failures): the region clock's characters are the points of the region's 3-adic ball.",
 "F5": "Readability: record occupancy and record density fully readable (functions of S); token fields readable because the surviving assignments are (Y1: the anchor inputs are recorded propositions)."


## Part 4 - the premise
TD1 (the surviving premise; stated, NOT adopted): the standing vacuum token of an object is enablement-served in the region common_prefix(argmax-depth anchor cells of the object's formation edits), rather than in ROOT. Inert alternative T0: every token in ROOT (the current tower). Binary, parameter-free, internal, zero tie-break clauses, readable, covariant, schedule-invariant, non-degenerate (0.990 non-ROOT on the 903-catalog).

Coincides with the R66 record: NO - the R66-recorded TR1' is T-DEEP's depth-1 truncation (exact on the whole 903-catalog); the class enumeration this round found the deeper zero-clause form and the frozen minimality order selects it. Recorded as a correction of the registered prediction.

H5 derived-side candidates (target-blind):
[
 "the record-density field rho_rec(d) = N_{>=d} and its two-regime maturation law (class: derived, readable)",
 "the charge-share family (q0; q1/3 + Q2/9; Q2/9) and its mature limit (0; 1/9; 1/9) (class: exact theorem)",
 "the free/congested boundary d*(N) = log_3(N/Gamma) and its outward logarithmic motion (class: exact at powers of 3)",
 "the mature equalization-plus-free-root signature: nine equal-lapse regions and one permanently free region (class: derived; the fixture's sharpest qualitative signature)",
 "early-to-late density ratios per cylinder (class: derived dimensionless; depends only on the resolution profile)"
]

## Prediction vs outcome
Registered: at least three total candidates, T-PROFILE partial, T-DEEP and TR1' coincide or differ on ties, survivors readable/covariant/non-degenerate - outcome: three survivors confirmed, but the registered 'none' for the search clause is CORRECTED (plurality exists), T-LAST is rejected on schedule grounds, and T-DEEP vs TR1' differ systematically (T-DEEP strictly deeper on 624/894; TR1' is its depth-1 truncation). Registered FIXED_MAP with constant capacity and unchanged band law - as registered. Registered VARIATION_DERIVED depth-graded with d* = log_3(N/Gamma) - as registered at general depth, SHARPENED by the referee: the mature fixture EQUALIZES the nine non-root regions (N = 9 Gamma simultaneous congestion) and leaves root permanently free - a two-phase law the registered picture missed; my in-prompt congestion composite carried a x9 slip (corrected, CX-R68-3). Registered TR1' UNIQUE_MINIMAL coinciding with R66 - CORRECTED: the unique minimum is T-DEEP's zero-clause form; TR1' ranks second as its truncation. The prediction constrained nothing.

## Hostile controls
All 8 REJECTED (see OD0_R68_RESULTS.json).

## R69
UNIQUE_MINIMAL with VARIATION_DERIVED, so per the R69 rule: R69 preregisters the H5 comparison protocol against the density and lapse fields (R56/R61 mirror: definitions extracted at opening; reparametrization-invariant shapes only - depth ordering, boundary motion, monotonicities, the equalization-plus-free-root signature; Tier D excluded; state-class rule; advance PASS/PARTIAL/FAIL rule), and pins any missing H5 artifacts. R70 opens H5 - the LAST sealed corpus.
