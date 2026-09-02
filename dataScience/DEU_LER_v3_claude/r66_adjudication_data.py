"""OD0-R66 adjudication data: geometry freeze, regional adjudication,
scaling limit, inventory, M8 preregistration. (Claude Code.)"""

RUN_DATE = "2026-09-02"

G1 = {
 "status": "FROZEN",
 "statement": "GEOMETRY CANDIDATE (frozen): the record space R - the "
   "occupied nodes of the universal ternary word tree - with "
   "d(r, r') = 3^{-l(r, r')}, l the common prefix length, and "
   "d(r, r) = 0. Properties, all previously certified and carried: "
   "ultrametric without exception (R65: 7,971,964 triples, zero "
   "violations); full ternary at every realized depth (forced by the "
   "declared odometer order 3^D); volume-growth exponent delta = 1 "
   "exact and Gamma-independent; READABLE_FROM_S (R63 D7). "
   "BACK-ACTION INVARIANCE (R63 D8 carried to the tree, certified "
   "this round): an adjunction appends records and never erases or "
   "rewrites a prefix, so all distances among existing records are "
   "invariant under every act - the record geometry is immutable "
   "history; only new points are added. This is a geometry of what "
   "can be read, not of the object DAG.",
}

G2 = {
 "status": "PROVEN",
 "statement": "DEPTH-GRADING DUALITY (internal theorem). Both "
   "structures are graded by one depth index: at depth D the record "
   "tree has 3^D cylinders; the clock group is C_D = Z/(3^{D+1} Z) "
   "with embeddings i_D(q) = 3q (all declared, A13R/CD1I). "
   "(i) The inverse limit of the cylinder level sets under "
   "truncation is the space of infinite ternary words - the "
   "boundary of the tree - homeomorphic to the 3-adic integers Z_3 "
   "with the metric 3^{-(common prefix)}: compact, totally "
   "disconnected, carrying the uniform product (Haar) measure. "
   "(ii) The direct limit C_infty = varinjlim(C_d, i_d) is the "
   "group of all 3-power roots of unity via [d, q] -> "
   "exp(2 pi i q / 3^{d+1}) - the Prufer 3-group Z(3^infty) "
   "(mathematical identification, permitted per note 3). "
   "(iii) CHARACTER PAIRING: for an infinite word w with 3-adic "
   "truncations w^{(m)} = sum_{i<m} w_i 3^i, the pairing "
   "<[d, q], w> = exp(2 pi i q w^{(d+1)} / 3^{d+1}) is "
   "well-defined (embedding-consistent: certified exactly, 3,240 "
   "checks, zero failures), each w defines a continuous character, "
   "distinct words define distinct characters (243/243 at depth 4), "
   "and every character arises this way (Hom(Z(3^infty), T) = "
   "varprojlim Hom(Z/3^{m}, T) = varprojlim Z/3^{m} = Z_3). The "
   "characters of the clock are exactly the boundary points of the "
   "record tree: the clock and the record geometry are Pontryagin "
   "duals (identification cited as mathematics; no interpretation).",
}

R1 = {
 "verdict": "REQUIRES_PREMISE",
 "statement": "The standing token's region is NOT derivable "
   "(panel-verified, adversarial source search): (i) the "
   "common-prefix assignment is degenerate for literally every "
   "object (903/903 catalog graphs and 2304/2304 R19 edit sets "
   "map to ROOT - every graph carries a root-anchored edit), "
   "reproducing exactly the sole region the frozen executable "
   "ever stamps (service.py regional_sets default ()); (ii) the "
   "nondegenerate majority-cell functional is PARTIAL on the "
   "frozen catalogs themselves - object-pooled depth-1 majority "
   "ties on 486/2304 R19 edit sets and is undefined on 9 all-root "
   "profiles (zero ties but 9 undefined on the 903-catalog); "
   "per-factor majority never ties but is undefined on 288 factor "
   "slots and yields a cell PAIR, and pooled-vs-per-factor is "
   "itself an undeclared selection; depth-2 plurality is a third "
   "inequivalent choice-free functional; (iii) the sources "
   "everywhere take region_mu as GIVEN (A13R: 'its inherited "
   "structural region'; ticks are per-region fixtures looped over "
   "the 10-marker catalog; CD2's locality premise PRESUPPOSES mu; "
   "UEQ0 has no object concept; package-wide grep for home-region "
   "rules: zero hits). Multiple inequivalent choice-free "
   "candidates, none selected by source: a premise is required.",
 "candidate_premise": "TR1' (candidate, NOT adopted; emended by "
   "the panel to be total): the standing token of an object "
   "occupies the object's pooled depth-1 majority anchor cell; "
   "ties AND profiles with no depth >= 1 edits fall to the common "
   "prefix (ROOT). Binary, parameter-free, total on both frozen "
   "catalogs, schedule-invariant - and not adopted by any source; "
   "the inequivalent alternatives (depth-2 plurality, per-factor "
   "majority pair, cost-weighted variants) remain equally "
   "unselected.",
}

R2R3 = {"status": "NOT_RUN (per the package rule: R1 is not "
                  "DERIVABLE, so the regional process and the "
                  "lapse/density fields wait for the premise round)"}

S1 = {
 "tuple": {
  "space": "EXACT: the 3-adic word space Z_3 (G2(i)) - the inverse "
           "limit of the record tree.",
  "measure": "EXACT: the uniform product (Haar) measure - the limit "
             "of the uniform cylinder measures.",
  "occupancy": "LAW WITH BOUNDS: at frozen-catalog level the "
    "occupied cylinders are the 40 A12 anchor regions (depth <= 3) "
    "and the odometer sweeps the full tree at every realized depth; "
    "the asymptotic occupancy of the full tree is exact "
    "(odometer-forced), the catalog occupancy is a bounded-depth "
    "fixture (both recorded; no interpolating law is frozen).",
  "fields": "CONDITIONAL: the lapse and tick-rate fields on "
    "cylinders await the regional premise (R1 REQUIRES_PREMISE); "
    "only the ROOT-instantiation values (the R60 laws) exist "
    "unconditionally - they are the depth-0 field values.",
  "clock": "EXACT: the character structure of G2 - the clock's "
    "dual IS the boundary of the record space.",
 },
 "exactness_summary": "space and measure and duality EXACT; "
   "occupancy a two-regime law (catalog fixture + odometer "
   "asymptotic); fields conditional on the regional premise.",
}

S2 = {
 "scope": "The limit contains NO length, NO Euclidean or manifold "
   "structure, NO spatial dimension, NO metric on objects "
   "(R63-R65 theorems). It is: an ultrametric boundary space with "
   "Haar measure, its exact clock dual, and depth-graded fields "
   "awaiting the regional premise. Standing scope of the geometry; "
   "any bridge beyond it requires a preregistered dictionary.",
}

I1 = [
 {"inv": "CGLMP supremum 4/3 + 8 sqrt(3)/9 (maximally entangled "
         "two-qutrit, native family)", "src": "BELL1/BELL2 frozen "
         "reports", "cls": "SETTING_DICTIONARY_ONLY",
  "dict": "settings/preparations identification - EXISTS (Section "
          "8)"},
 {"inv": "CHSH supremum under the frozen dichotomic readout",
  "src": "BELL frozen reports", "cls": "SETTING_DICTIONARY_ONLY",
  "dict": "settings - EXISTS"},
 {"inv": "local bounds (frozen)", "src": "BELL frozen reports",
  "cls": "SETTING_DICTIONARY_ONLY", "dict": "settings - EXISTS"},
 {"inv": "direct-source Schmidt rigidity (uniform Schmidt spectrum)",
  "src": "BELL0/R58", "cls": "SETTING_DICTIONARY_ONLY",
  "dict": "settings - EXISTS"},
 {"inv": "heralded branch (3/4, 1/4, 0)", "src": "BELL frozen "
  "reports", "cls": "SETTING_DICTIONARY_ONLY",
  "dict": "settings - EXISTS"},
 {"inv": "age-exponent ladder (1, 3/2, 2) up to logs", "src": "R60",
  "cls": "TIME_DICTIONARY_REQUIRED", "dict": "a time dictionary - "
  "NONE exists"},
 {"inv": "ln(4/3) clock offset (co-embedding vs containment)",
  "src": "R61", "cls": "TIME_DICTIONARY_REQUIRED", "dict": "time - "
  "NONE"},
 {"inv": "lapse laws (E0 Phi=1; E1 x = D/(F+D); band x*^2 = "
         "r/(4 C(Gamma,2) n ln n))", "src": "R60",
  "cls": "TIME_DICTIONARY_REQUIRED", "dict": "time - NONE"},
 {"inv": "three ages k ~ (2/r) n^2 ln n; N_V = O(n^{3/2} "
         "sqrt(ln n)); b ~ n", "src": "R60",
  "cls": "TIME_DICTIONARY_REQUIRED", "dict": "time - NONE"},
 {"inv": "capacity spectrum (Gamma >= k hard ladder)", "src":
  "R56 M5", "cls": "CAPACITY_DICTIONARY_REQUIRED",
  "dict": "capacity - NONE"},
 {"inv": "critical line m_c = Gamma + min(H, 2 Gamma)", "src":
  "R61/R64", "cls": "CAPACITY_DICTIONARY_REQUIRED",
  "dict": "capacity - NONE"},
 {"inv": "relief fixed point P* = 10 Gamma - 6; cap 2 Gamma",
  "src": "R60", "cls": "CAPACITY_DICTIONARY_REQUIRED",
  "dict": "capacity - NONE"},
 {"inv": "MINCOST base family 48/5, 384/35, 256/21", "src": "R64",
  "cls": "CAPACITY_DICTIONARY_REQUIRED", "dict": "capacity - NONE"},
 {"inv": "ball-growth base 8 (spectral radius, exact)", "src":
  "R63", "cls": "GEOMETRY_DICTIONARY_REQUIRED", "dict":
  "geometry - NONE"},
 {"inv": "Jaccard ratio-of-means 22/35", "src": "R63",
  "cls": "GEOMETRY_DICTIONARY_REQUIRED", "dict": "geometry - NONE"},
 {"inv": "LEAF1 base (5 + sqrt(41))/2", "src": "R64",
  "cls": "GEOMETRY_DICTIONARY_REQUIRED", "dict": "geometry - NONE"},
 {"inv": "NOT_LEAF2 leaf fixed point sqrt(2) - 1", "src": "R64",
  "cls": "GEOMETRY_DICTIONARY_REQUIRED", "dict": "geometry - NONE"},
 {"inv": "depth constants 4.311070 / 0.373365 (roots of "
         "c(1 + ln 2 - ln c) = 1)", "src": "R63",
  "cls": "GEOMETRY_DICTIONARY_REQUIRED", "dict": "geometry - NONE"},
 {"inv": "delta = 1 (record-space 3-adic exponent) and the 3-adic "
         "structure itself", "src": "R65",
  "cls": "GEOMETRY_DICTIONARY_REQUIRED", "dict": "geometry - NONE"},
 {"inv": "REL-tower lineage constant pi/sqrt(3)", "src": "R64",
  "cls": "INTERNAL_ONLY (conditional tower, not adopted)",
  "dict": "n/a"},
 {"inv": "readable fraction 2/3 / dark fraction 1/3", "src":
  "R63 addendum D7", "cls": "STRUCTURE_FRACTION",
  "dict": "NONE - and comparison FORBIDDEN until a 'readable "
  "structure' dictionary is preregistered against a sealed "
  "corpus. Recorded note: the value is the integral of t^2 from "
  "the two-parent childlessness law - a combinatorial fact about "
  "recording, not a census of anything external."},
 {"inv": "cone constant (3/8) pi^{3/2}; TC constant pi^{3/2}/4; "
         "unrelated-fraction constant pi^{3/2}/2; beta scale "
         "n^{2/3}; interval threshold n^{1/4}", "src": "R61/R63",
  "cls": "INTERNAL_ONLY", "dict": "n/a"},
 {"inv": "1/3 leaf fraction (ALL); horizon law E|U| = (n-2)/3",
  "src": "R63 addendum / R64", "cls": "INTERNAL_ONLY",
  "dict": "n/a"},
]

M8_PROTOCOL = {
 "scope": "SETTING_DICTIONARY_ONLY invariants only.",
 "dictionary": {
  "source": "the DEU direct equality source <-> the maximally "
            "entangled two-qutrit state",
  "settings": "the DEU native setting family (clock translation + "
              "reverse character transform + native three-outcome "
              "PVM) <-> the standard two-setting qutrit measurement "
              "family of the CGLMP construction",
  "readout": "the frozen dichotomic readout <-> the same map "
             "applied in the standard setting",
  "closure": "No other identification."},
 "external_values_to_name_in_R67": [
  "the standard two-qutrit CGLMP-3 maximum over the dictionary's "
  "measurement family for the maximally entangled state",
  "the CHSH value under the same dictionary",
  "the known qutrit ceiling attained by a non-maximally entangled "
  "state (already cited in the frozen Bell report as a quarantined "
  "external benchmark)",
  "the local bounds"],
 "rule": "Per invariant: EXACT_AGREEMENT (derived = theory under "
   "the dictionary - a consistency theorem, since the same "
   "mathematics was derived) / RESTRICTION (the derived family "
   "cannot reach a theory value a broader family can - a claim "
   "about what the constructor prepares, not a contradiction) / "
   "CONTRADICTION (a derived value exceeds a theory bound or "
   "disagrees where the dictionary identifies the same object - a "
   "FAIL of the quantum-side scaffold, reported at equal "
   "prominence).",
 "declared_expected_pattern": "EXACT_AGREEMENT on the maximally "
   "entangled CGLMP and CHSH values and on the local bounds; "
   "RESTRICTION on the non-maximal ceiling.",
 "declared_non_comparisons": "TIME_DICTIONARY_REQUIRED, "
   "CAPACITY_DICTIONARY_REQUIRED, GEOMETRY_DICTIONARY_REQUIRED "
   "classes: not compared - their dictionaries do not exist. "
   "STRUCTURE_FRACTION (the 1/3 dark fraction): comparison "
   "FORBIDDEN until a readable-structure dictionary is "
   "preregistered against a sealed corpus.",
 "standing_prediction_untestable_now": "Autonomous shared-source "
   "states are Schmidt-uniform among same-step siblings (R58 "
   "T2/T3): natural entanglement in the throttled universe is "
   "always maximal and phase-erased at the record; multi-setting "
   "correlation structure is instrument-level only. Recorded for "
   "a future instrument dictionary; not compared.",
 "execution": "R67, one round, no repair.",
}

HC = [
 ["HC1", "target altered; external value named outside Section 8; "
  "comparison performed", "REJECTED", "Targets verbatim; the only "
  "external names appear inside the sealed protocol as *to be "
  "named in R67*; no comparison performed."],
 ["HC2", "physical referent outside the sealed protocol",
  "REJECTED", "Mathematical identifications only (Z_3, Prufer "
  "3-group, Pontryagin duality), per note 3."],
 ["HC3", "regional instantiation without R1 DERIVABLE; token map "
  "invented", "REJECTED", "R1 adjudicated REQUIRES_PREMISE; TR1 "
  "recorded as a candidate, not adopted; R2-R3 not run."],
 ["HC4", "dictionary beyond settings; dark fraction/exponents/"
  "geometry in the protocol", "REJECTED", "The protocol's scope "
  "is the five setting-class invariants; all other classes are "
  "declared non-comparisons."],
 ["HC5", "readouts as proof; unlabeled asymptotics", "REJECTED",
  "This round's certificates are exact; the occupancy two-regime "
  "statement is labeled by regime."],
 ["HC6", "H5 read; BELL2 scientific content reopened", "REJECTED",
  "Sentinel parsed=false; only frozen Bell verdict VALUES are "
  "cited, from the frozen reports."],
 ["HC7", "frozen tower modified", "REJECTED", "Nothing modified."],
 ["HC8", "hand hash; placeholder", "REJECTED",
  "All hashes in-process."],
]

VERDICTS = {
 "always": "OD0_R66_PASS_GEOMETRY_FROZEN_AND_M8_PREREGISTERED",
 "components": {
  "G1": "FROZEN (back-action invariance certified)",
  "G2": "PROVEN (pairing exact; 3,240 embedding checks, 243/243 "
        "characters)",
  "R1": "REQUIRES_PREMISE (TR1 candidate recorded, not adopted)",
  "R2_R3": "not run (per rule)",
  "S1_S2": "stated (space/measure/duality exact; fields "
           "conditional)",
  "I1": "23 invariant entries: 5 SETTING_DICTIONARY_ONLY, 4 TIME, "
        "4 CAPACITY, 6 GEOMETRY, 1 STRUCTURE_FRACTION (forbidden "
        "note recorded), 3 INTERNAL_ONLY",
 },
 "prediction_vs_outcome": "Registered: G1 frozen, G2 PROVEN with "
  "the explicit pairing - as registered (panel: the flagged "
  "well-definedness step is exactly right; two wording "
  "clarifications folded in: the inverse limit is of the level "
  "sets, giving the boundary; 'continuous' is redundant on a "
  "discrete group). Registered R1 DERIVABLE via the "
  "smallest-prefix anchor - REFUTED: the common-prefix assignment "
  "is degenerate for every single object, the majority functional "
  "is partial on the frozen catalogs (486 ties + 9 undefined), "
  "and the sources take region_mu as given everywhere; R1 = "
  "REQUIRES_PREMISE with the emended TR1' recorded. Consequently "
  "the registered R2/R3 predictions (capacity scaling, occupancy "
  "uniformity, VARIATION_DERIVED) were not adjudicated - not run "
  "per the rule. S1/S2 as registered with the fields marked "
  "conditional. I1 as registered (geometry/internal majority; "
  "exactly the five Bell values in SETTING_DICTIONARY_ONLY). "
  "Protocol sealed with the declared pattern. The prediction "
  "constrained nothing.",
 "r67_recommendation": "Execute the sealed Section 8 comparison - "
  "one round, no repair - reporting EXACT_AGREEMENT / RESTRICTION "
  "/ CONTRADICTION per invariant; then open the branch (d) "
  "interface theorem (the rank-(m-1) Gram structure with pairwise "
  "overlap -1/(m-1) in R58's m-sibling composite, certified at "
  "m = 4 against the frozen closure-amplitude values) so the "
  "three appearances of 1/3 get their coincidence-or-theorem "
  "adjudication. The regional premise TR1 is preregistered as its "
  "own round before any regional law is used; H5 waits for the "
  "regional density field.",
}
