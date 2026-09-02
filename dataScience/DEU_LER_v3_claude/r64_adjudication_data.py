"""OD0-R64 adjudication data: the locality premise class. (Claude Code.)
Six-referee adversarial panel + exact gated reachability; panel
corrections folded in and recorded in OD0_R64_COUNTEREXAMPLES.md."""

RUN_DATE = "2026-09-02"

# Per-gate table: C1 deadlock, C2 firing/growth, C3 rho/D3, C4 type,
# readability (READABLE = function of the fact graph S on recorded
# structure; CONSTRUCTOR_LEVEL otherwise).
TABLE = {
 "ALL": {"C1": "deadlock-free from genesis", "C2": "TG1 baseline; "
   "leaf fraction 1/3 (measured 0.33331-0.33366 at n = 2e5)",
   "C3": "rho = 8 exactly (frozen R63); all D1 structures as R63",
   "C4": "SMALL_WORLD", "read": "CONSTRUCTOR_LEVEL (trivial gate)"},
 "REL": {"C1": "genesis BLOCKED (a,b unrelated; deadlock at n = 2); "
   "sustains from the 3-object seed",
   "C2": "the REL tower is a random TREE with depth-preferential "
   "attachment (fire prob proportional to depth+2-fired: the coupon "
   "structure, panel-derived); |cone(z)| = depth(z)+3 exactly; depth "
   "= (2.0-2.5) ln n; ln chains = Theta(sqrt(log n)) with lineage "
   "constant pi/sqrt(3) = 1.814; cost per formation exp(Theta("
   "sqrt(log n))) = n^{o(1)} (BOTH the registered Theta(ln n) and "
   "the pre-run polynomial guess refuted); growth |X(T)| = "
   "T^{1-o(1)} quasi-linear",
   "C3": "diameter Theta(log n) => exponential balls, rho > 1; "
   "no stable exponent; d_J/d_U inherit tree degeneracies",
   "C4": "TREE_LIKE", "read": "READABLE (comparability is a "
   "function of recorded cones on X_rec)"},
 "UNREL": {"C1": "genesis fires once then PERMANENT DEADLOCK at "
   "n = 3 (both absent pairs related; exact witness, every Gamma); "
   "sustains only from a 7-object seed with incomparable pairs; "
   "then asymptotically inert (excluded related fraction "
   "Theta(n^{-1/2}))",
   "C2": "post-seed: near-ALL", "C3": "rho -> 8", "C4":
   "SMALL_WORLD (seeded)", "read": "READABLE"},
 "PC": {"C1": "genesis blocked; deadlock-free from the 3-object "
   "seed with #fireable = n - 1 EXACTLY (+2 per firing, -1 fired)",
   "C2": "eligible pairs E_n = Theta(n); growth sustained",
   "C3": "exponential balls, measured base 2.67-4.21 (tree with "
   "unbounded child accumulation); no stable exponent",
   "C4": "TREE_LIKE", "read": "READABLE on X_rec"},
 "NOT_PC": {"C1": "fires genesis but hits the n = 3 bottleneck "
   "(all absent pairs at n = 3 are parent-child); sustains from "
   "the 4-object seed", "C2": "excludes a Theta(1/n) fraction: "
   "asymptotically inert", "C3": "rho -> 8", "C4": "SMALL_WORLD",
   "read": "READABLE"},
 "GP": {"C1": "blocked to n <= 3; minimal sustaining seed n = 4 "
   "(panel: each firing creates the gated pair {middle parent, z})",
   "C2": "E_n/n -> 2.0-2.5", "C3": "exponential (ultrasmall: "
   "eccentricity 9 at n = 1e5)", "C4": "SMALL_WORLD",
   "read": "READABLE"},
 "NOT_GP": {"C1": "deadlock-free from genesis", "C2":
   "asymptotically inert", "C3": "rho -> 8", "C4": "SMALL_WORLD",
   "read": "READABLE"},
 "SIB": {"C1": "blocked to n <= 3; from the MINIMAL 4-object seed "
   "it sustains via a DETERMINISTIC FORCED CHAIN t_{k+1} = "
   "{t_{k-1}, t_k} with exactly ONE fireable pair at every step "
   "(panel theorem); from richer seeds E_n = Theta(n) and the "
   "process is mean-field",
   "C2": "SEED-DEPENDENT: minimal seed -> chain; rich seed -> "
   "exponential", "C3": "minimal seed: exponent 1 (chain); rich "
   "seed: exponential (measured base 3.58)",
   "C4": "CHAIN_LIKE (minimal seed) / TREE_LIKE (rich seed) - the "
   "only gate whose geometry class depends on the seed",
   "read": "READABLE"},
 "NOT_SIB": {"C1": "deadlock-free from genesis", "C2":
   "asymptotically inert", "C3": "rho -> 8", "C4": "SMALL_WORLD",
   "read": "READABLE"},
 "COUSIN1": {"C1": "blocked to n <= 5; sustains from the 7-object "
   "seed", "C2": "E_n/n growing (slope ~1.34: superlinear)",
   "C3": "exponential (eccentricity 8-10)", "C4": "SMALL_WORLD",
   "read": "READABLE"},
 "NOT_COUSIN1": {"C1": "deadlock-free from genesis", "C2":
   "asymptotically inert", "C3": "rho -> 8", "C4": "SMALL_WORLD",
   "read": "READABLE"},
 "LEAF1": {"C1": "deadlock-free from genesis", "C2": "the leaf "
   "count is pathwise NON-INCREASING and equals 1 forever past "
   "genesis (panel theorem; seeded relaxation L ~ n^{-1/2}, "
   "measured slope -0.486): deterministic self-organization to a "
   "single growing frontier plus one uniform long-range parent "
   "per birth; growth self-throttled",
   "C3": "rho = (5 + sqrt(41))/2 = 5.7016 by the two-type frozen "
   "operator (lambda A = 4(A+C), lambda C = 2A + C; the pre-run "
   "guess 4 refuted - chain links interact multiplicatively); "
   "measured shell ratios 4.02-4.07 at n = 1e7, above 4 and "
   "rising; no stable exponent",
   "C4": "SMALL_WORLD (chain + uniform bridges)",
   "read": "READABLE (leaf status = childlessness, in S)"},
 "LEAF2": {"C1": "PERMANENT DEADLOCK at n = 3 from genesis, and "
   "halts at finite n from EVERY finite seed (leaf count falls by "
   "exactly 1 per firing - panel strengthening)", "C2": "-",
   "C3": "-", "C4": "FINITE", "read": "READABLE"},
 "NOT_LEAF2": {"C1": "genesis blocked (both primitives childless); "
   "sustains from the 3-object seed",
   "C2": "leaf fraction converges to the exact fixed point "
   "sqrt(2) - 1 = 0.41421 (attracting; measured 0.41425 +/- "
   "0.00042 at n = 2e5, 4 seeds)", "C3": "rho -> 8 (two "
   "quasi-uniform parents)", "C4": "SMALL_WORLD",
   "read": "READABLE"},
 "REC2": {"C1": "genesis blocked; from ANY seed the recorded set "
   "is FROZEN (new objects are permanent leaves), the process "
   "fires exactly the absent pairs within the seed's recorded set "
   "R in any order to a UNIQUE final state of size n_seed + "
   "C(|R|,2) - #pre-existing R-pairs: a FINITE universe always "
   "(theorem; the engine's SUSTAINS at the n = 9 cap is the "
   "artifact of the cap, corrected here)", "C2": "-", "C3": "-",
   "C4": "FINITE", "read": "READABLE"},
 "MINCOST": {"C1": "inert at Gamma = 2; deadlock-free (any single "
   "served pair is minimal)",
   "C2": "REFUTES both the registered guess (rho decreasing) and "
   "the pre-run inertness guess: served-ensemble pair costs are "
   "BIRTH-DOMINATED (W(cone) ~ b ln b by prefix self-similarity; "
   "Theta(1) relative spread - the D9 late-pair concentration "
   "does not apply), so MINCOST persistently fires a noisy "
   "top-2-EARLIEST-BORN pair (fractions 0.60/0.50/0.43 at Gamma "
   "= 3/4/5, flat in n, vs nulls 1/3, 1/6, 1/10); leaf fraction "
   "0.4404 (Gamma=3) / 0.5697 (Gamma=5), matching the operator "
   "to 3 decimals",
   "C3": "idealized operator (parents = top-2 order statistics "
   "of Gamma Exp(1) types): rho = 2 M_h(1/2) = 48/5 = 9.6 "
   "(Gamma=3), 384/35 = 10.9714 (Gamma=4), 256/21 = 12.1905 "
   "(Gamma=5) - ABOVE 8, growing with Gamma; exact-cost runs "
   "drift upward (9.20 at Gamma=3, 11.47 at Gamma=5 by n=8000); "
   "d_J shifts by Theta(1) toward SMALLER overlap (0.627 -> "
   "0.70-0.76): more long-range, not less",
   "C4": "SMALL_WORLD (enhanced)", "read": "READABLE on X_rec "
   "(costs are functions of S) - realizing requires adjunction"},
 "NOT_MINCOST": {"C1": "inert at Gamma = 2 in the complementary "
   "sense (blocks the only pair: DEADLOCK at Gamma = 2); at "
   "Gamma >= 3 fires all but the minimal pair: near-ALL",
   "C2": "asymptotically inert (excludes one pair per burst)",
   "C3": "rho -> 8", "C4": "SMALL_WORLD", "read": "READABLE"},
 "DG2": {"C1": "blocked to n <= 3 (genesis d_G infinite; n = 3 "
   "pairs are at d_G = 1); minimal sustaining seed n = 4; "
   "deadlock-free (each firing creates the gated pair {w, z})",
   "C2": "eligible pairs superlinear (E_n/n: 5.9 -> 21); parent "
   "degree size-biased (mean deg sum at firing 28 vs population "
   "8 at n = 1e5)",
   "C3": "SMALL_WORLD by two-step preferential attachment: "
   "heavy-tailed degrees (deg_max ~ n^0.57, Hill alpha ~ 2.4), "
   "diameter ~ 1.2 ln n, exponential balls (effective base ~7, "
   "n-dependent; the rho = 8 operator's hypothesis formally "
   "fails - verdict from structure); every effective-delta "
   "estimator drifts +1.1 per decade: NO stable exponent; the "
   "collapse branch refuted (diameter grows, deg_max/n -> 0)",
   "C4": "SMALL_WORLD", "read": "MIXED (d_G = 2 through "
   "unrecorded leaves is invisible to S - R63 D7)"},
 "NOT_DG2": {"C1": "deadlock-free from genesis (d = infinity != "
   "2)", "C2": "asymptotically inert", "C3": "rho -> 8",
   "C4": "SMALL_WORLD", "read": "MIXED"},
 "DG3PLUS": {"C1": "fires genesis (d = infinity >= 3) but "
   "deadlocks by n <= 5 from small seeds; sustains from the "
   "7-object seed", "C2": "excludes a vanishing near-pair "
   "fraction: asymptotically inert", "C3": "rho -> 8",
   "C4": "SMALL_WORLD", "read": "MIXED"},
 "NOT_DG3PLUS": {"C1": "genesis blocked; sustains from the "
   "3-object seed (engine) / 4-object (panel, strict reading)",
   "C2": "same reinforcement mechanism as DG2",
   "C3": "SMALL_WORLD class of DG2 (deg_max ~ n^0.56, delta "
   "drifting 3.1 -> 4.7)", "C4": "SMALL_WORLD", "read": "MIXED"},
 "SIB_AND_LEAF1": {"C1": "blocked to n <= 3; sustains from the "
   "4-object seed", "C2": "chain-with-leaf-constraint: the "
   "forced-chain regime persists (the chain's frontier is the "
   "leaf)", "C3": "exponent 1 (chain) from the minimal seed",
   "C4": "CHAIN_LIKE", "read": "READABLE"},
 "REL_AND_MINCOST": {"C1": "as REL (genesis blocked; 3-object "
   "seed); inert selection at Gamma = 2",
   "C2": "REL tree with earliest-born preference among related "
   "served pairs: deepens the depth-preferential bias",
   "C3": "TREE_LIKE, exponential; no stable exponent",
   "C4": "TREE_LIKE", "read": "READABLE"},
 "UNREL_AND_MINCOST": {"C1": "as UNREL: deadlock at n = 3 from "
   "genesis; 7-object seed to sustain; then near-ALL with the "
   "MINCOST early-born bias", "C3": "rho >= 8 class",
   "C2": "seeded: near-MINCOST", "C4": "SMALL_WORLD",
   "read": "READABLE"},
 "DG2_AND_LEAF1": {"C1": "sustains from the 4-object seed (4/4 "
   "seeds, no deadlock)",
   "C2": "leaf starvation confines growth to a BALLISTIC FRONTIER "
   "FILAMENT of constant width ~18: valid candidates stay O(1) "
   "the whole run; leaf fraction -> < 1e-4",
   "C3": "CHAIN_LIKE, delta = 1 EXACTLY (diameter linear in n; "
   "deg_max ~ log n, no heavy tail): the only stable exponent in "
   "the DG2 trio, and it is the trivial one",
   "C4": "CHAIN_LIKE", "read": "MIXED"},
}

NO_GO = {
 "verdict": "PROVEN (E-level, with the corrected route recorded)",
 "statement": "For every deadlock-free gate in G, the mature ideal "
   "has no stable finite volume-growth exponent greater than 1: "
   "either balls grow exponentially (rho > 1) or the structure is "
   "chain-like with exponent exactly 1 (SIB from its minimal seed; "
   "SIB_AND_LEAF1; DG2_AND_LEAF1).",
 "route": {
  "i_corrected": "The frozen route (i) is sound as a kernel "
    "comparison but wrong quantitatively: a uniform-parent term of "
    "coefficient c gives rho >= 4c (Krein-Rutman comparison; K_1 "
    "e^{x/2} = 4 e^{x/2} - 2), which proves rho > 1 only for c > "
    "1/4. The conclusion survives for every c bounded below via "
    "BRIDGING: each gated birth drops a length-2 bridge with a "
    "uniform endpoint, so |B_{r+1}| >= (1 + Theta(c))|B_r| while "
    "|B_r| = o(n): rho >= max(4c, 1 + kappa c) > 1 (measured base "
    "2.13 at c = 0.1 where 4c = 0.4; 1.39 at c = 0.02). The "
    "hypothesis is strengthened to 'uniform over all objects or a "
    "time-representative set'.",
  "ii_corrected": "THE ELIGIBLE-PAIR DRIFT DICHOTOMY (the no-go's "
    "engine): every newly eligible pair involves the newborn "
    "(relations between old pairs never change - each new edge is "
    "incident to the newborn), so E_{n+1} - E_n = C_n - 1 with "
    "C_n = eligible pairs created at the newborn. Trichotomy: "
    "E[C] - 1 > 0 => E_n = Theta(n) or more => mean-field site "
    "choice => rho > 1; C = 1 deterministically => E_n = Theta(1) "
    "=> forced chain, exponent 1; E[C] = 1 with variance => E_n "
    "hits 0 a.s. (extinction). E_n = Theta(n^alpha) with 0 < "
    "alpha < 1 is UNATTAINABLE STABLY in the class: the "
    "intermediate-dimension window is structurally closed. "
    "Measured per gate: PC E_n = n + 8 exactly; GP 2.0-2.5 n; "
    "SIB (rich seed) ~5n; COUSIN1 superlinear; DG2 5.9-21 n; "
    "SIB (minimal seed) and DG2_AND_LEAF1: C = 1 / O(1) - the "
    "chains.",
  "iii_corrected": "MINCOST: the registered route stands in "
    "conclusion (rho > 1) but the mechanism is the opposite of "
    "both guesses: birth-dominated cost spread makes the gate "
    "persistently select earliest-born parents, RAISING rho above "
    "8 (exact operator values 48/5, 384/35, 256/21 for Gamma = "
    "3, 4, 5) and shifting d_J toward smaller overlap."},
 "negative_result": "No parameter-free binary internal gate on "
   "pair formation yields a stable finite volume-growth exponent "
   "greater than 1. Locality cannot be bought with a gate: the "
   "class offers exponential worlds (with computable bases 8, "
   "5.7016, 9.6+, trees, small worlds) or one-dimensional chains, "
   "nothing between. Recorded at equal prominence.",
 "honest_gaps": "E-level proof (locally-tree-like path counts, "
   "as the frozen rho = 8 convention); the strengthened route-(i) "
   "hypothesis leaves a theoretical evasion (a time-skewed "
   "Theta(n) parent set plus a protected appendage) that no "
   "relational gate in G realizes (appendage vertices generically "
   "acquire degree >= 3 and become bridge targets); DG2's verdict "
   "is structural-plus-simulation (no finite-dimensional operator "
   "constructed).",
}

COROLLARY_REL = {
 "id": "ANCESTRY_GATED_TOWER (corollary, not adopted)",
 "laws": "Genesis blocked; from the 3-object seed the REL tower is "
   "a random tree with depth-preferential attachment (coupon law: "
   "fire probability proportional to depth + 2 - fired). Cones: "
   "|cone(z)| = depth(z) + 3 exactly; depth = (2.0-2.5) ln n "
   "(uniform-v model: 1.0 ln n). Chains: ln ch = Theta(sqrt("
   "log n)), lineage fixed point kappa = pi/sqrt(3) = 1.814 "
   "(local exponents decline as a/(2 sqrt(ln n)), matching "
   "measurement); cost per formation = exp(Theta(sqrt(log n))) = "
   "n^{o(1)} but omega(polylog) - the registered Theta(ln n) and "
   "the polynomial guess BOTH refuted. Growth: |X(T)| = "
   "T e^{-Theta(sqrt(log T))} = T^{1-o(1)} (quasi-linear). "
   "Lapse/clock (replacing R60 at corollary level): the balance "
   "band runs at x* ~ e^{-Theta(sqrt(log n))} - the lapse decays "
   "slower than any power of n; the three ages compress toward "
   "each other (k = n^{1+o(1)}). Recorded, not adopted.",
}

HC = [
 ["HC1", "gate added; threshold/weight smuggled; service kernel "
  "modified", "REJECTED", "G = the 25 frozen members, adjudicated "
  "verbatim; one exploratory referee conjunction (PC-and-SIB) was "
  "NOT admitted into the class or the verdict; the kernel is "
  "untouched."],
 ["HC2", "external referent; 'dimension' outside D3", "REJECTED",
  "Internal vocabulary only; structure-type names are the "
  "package's own."],
 ["HC3", "exponent/spectral radius fitted from readouts",
  "REJECTED", "Every base traces to an operator computation "
  "(8, 4, 5.7016 = (5+sqrt(41))/2, 9.6 = 48/5, 384/35, 256/21) "
  "or an exact structure theorem (chains); readouts labeled as "
  "checks."],
 ["HC4", "a gate adopted as a law", "REJECTED",
  "All gates tested as candidates; the REL corollary is recorded, "
  "not adopted."],
 ["HC5", "H5 read; H1-H4 pattern used to choose a gate",
  "REJECTED", "The class was frozen at Commit A from the package "
  "text; sentinels parsed=false."],
 ["HC6", "frozen tower modified; BELL2 opened", "REJECTED",
  "Untouched; unopened."],
 ["HC7", "readouts cited as proof", "REJECTED",
  "Verdicts rest on exact reachability, operator computations, "
  "and panel-verified derivations."],
 ["HC8", "hand hash; placeholder", "REJECTED",
  "All hashes in-process."],
]

VERDICTS = {
 "always": "OD0_R64_PASS_LOCALITY_CLASS_CLASSIFIED",
 "primary": "NO_GO_G = PROVEN",
 "components": {
  "gate_count": 25,
  "deadlocked_permanently": ["LEAF2 (every seed)",
                             "REC2 (finite universe theorem)"],
  "genesis_blocked_but_seedable": ["REL", "PC", "GP", "SIB",
      "COUSIN1", "NOT_PC", "NOT_LEAF2", "REC2", "DG2",
      "NOT_DG3PLUS", "UNREL (7-object seed)", "DG3PLUS (7-object)",
      "SIB_AND_LEAF1", "REL_AND_MINCOST", "UNREL_AND_MINCOST",
      "DG2_AND_LEAF1"],
  "asymptotically_inert": ["UNREL(seeded)", "NOT_PC", "NOT_GP",
      "NOT_SIB", "NOT_COUSIN1", "NOT_DG2", "DG3PLUS(seeded)",
      "NOT_MINCOST(Gamma>=3)"],
  "exponential_bases": {"ALL": 8, "LEAF1": "(5+sqrt(41))/2 = "
      "5.7016", "MINCOST": "48/5, 384/35, 256/21 for Gamma=3,4,5",
      "NOT_LEAF2": "-> 8", "DG2/NOT_DG3PLUS": "small-world, "
      "effective ~7, drifting", "PC": "2.7-4.2 measured tree"},
  "chains_exponent_1": ["SIB (minimal seed, deterministic forced "
      "chain)", "SIB_AND_LEAF1", "DG2_AND_LEAF1 (ballistic "
      "filament, width ~18)"],
  "CLUSTERING_UNDER_MINCOST": "d_J late-pair mean shifts 0.627 -> "
      "0.70 (Gamma=3) / 0.76 (Gamma=5) - toward SMALLER overlap; "
      "rho above 8 and increasing in Gamma (both the registered "
      "'rho decreases' and the pre-run 'asymptotically inert' "
      "guesses refuted)",
  "ANCESTRY_GATED_TOWER": "cones (2.0-2.5) ln n; ln chains "
      "Theta(sqrt(log n)) with kappa = pi/sqrt(3); cost "
      "exp(Theta(sqrt(log n))); growth T^{1-o(1)}; lapse "
      "e^{-Theta(sqrt(log n))}",
 },
 "prediction_vs_outcome": "No-go PROVEN - as registered, though by "
  "corrected routes. Registered errors, all caught by the "
  "engine/panel: (i) UNREL does not behave like ALL from genesis - "
  "it deadlocks permanently at n = 3 (it needs a 7-object seed, "
  "and only then is it asymptotically inert); (ii) LEAF1's base is "
  "(5+sqrt(41))/2 = 5.7016, not 'between 4 and 8' vaguely - and "
  "the leaf count is exactly 1 pathwise, a deterministic chain-"
  "plus-bridges; (iii) MINCOST at Gamma >= 3 is not "
  "CLUSTERED_DRIFTING with decreasing rho - it is exponentially "
  "ENHANCED (rho = 48/5... rising in Gamma) and shifts d_J toward "
  "smaller overlap; (iv) the REL corollary's registered cost "
  "Theta(ln n) is refuted - the true class is exp(Theta(sqrt("
  "log n))) with lineage constant pi/sqrt(3); (v) PC/GP/SIB/"
  "COUSIN1/DG2 are not 'tree-like or chain-like' uniformly - "
  "most are exponential small worlds; the true chains are SIB-"
  "from-minimal-seed (a deterministic forced chain), "
  "SIB_AND_LEAF1, and DG2_AND_LEAF1. The prediction constrained "
  "nothing.",
 "r65_recommendation": "NO_GO_G = PROVEN, so per the R65 rule: R65 "
  "classifies what a geometry premise must add beyond G, as the "
  "declared three-branch fork with no selection: (a) a "
  "length-scale parameter (non-minimal; recorded only); (b) a new "
  "constitutive primitive (this round's no-go is the required "
  "failure record); (c) the parameter-free structure the "
  "constructor already carries: the CD1I prefix-cylinder region "
  "tree (exactly ultrametric by construction, base 3 like the "
  "clock) - R65 derives its source status (how objects and "
  "records are assigned to cylinders; whether region-level "
  "locality is definable without a parameter) and, if definable, "
  "its ball-growth base by the same spectral method; (a) and (b) "
  "recorded as alternatives.",
}
