"""OD0-R65 adjudication data: branch (c), the prefix-cylinder tree.
(Claude Code.) Source extraction by 5-agent workflow (file+line
citations in R65_CYLINDER_SOURCE_AND_RECORD_SPACE.json); derivations
panel-verified before freezing."""

RUN_DATE = "2026-09-02"

P1 = {
 "region_definition": "A structural region is an inherited ternary "
   "PREFIX - a tuple over {0,1,2} of arbitrary finite depth, root = "
   "() - forming 'the finite inherited prefix-region set R' (UEQ0 "
   "master spec; compiler regex local_([0-2](?:_[0-2])*)_ell\\d+). "
   "UEQ0 fixes no cardinality and no maximum depth.",
 "why_8": "CORRECTED BY SOURCE: no 8-region enumeration exists "
   "anywhere in the frozen package. The A13R marker_region_catalog "
   "declares TEN regions: [(), (0,), (1,), (2,), (0,1), (1,2), "
   "(2,0), (0,2), (1,0), (2,1)] - root + 3 depth-1 + the 6 "
   "no-repeat depth-2 words (repeated-digit words absent; generated "
   "as the symmetry orbit of the inherited markers; no exclusion "
   "rule stated as a sentence). The package-carried 'why 8' "
   "premise is a round-level gloss, not a source fact; recorded as "
   "a correction.",
 "regional_ledgers": "DECLARED (a finding beyond the round-carried "
   "picture): each region carries its OWN complete five-integer "
   "ledger L_mu = (B, D, Gamma, P, H) and its own persistent clock "
   "Q_mu; the UEQ0 master kernel is the PRODUCT of independent "
   "per-region hypergeometric/relief kernels. The R52 JOINT_ONLY "
   "designation is the frozen catalog's instantiation at the "
   "single ROOT region (service_catalog invokes regional_sets with "
   "the default region ()); the spec-level structure is regional. "
   "Both statements recorded with citations; no round result is "
   "affected (the catalog instantiation is what the tower used).",
 "maps": {
  "records": "DECLARED - a record is the prefix symbol pi_ell(m) of "
    "a frontier-mode address m in Z_3^D, written by a relational "
    "interaction of resolution ell; it corresponds to exactly one "
    "length-ell prefix cylinder (global query); equal symbols use "
    "the SAME record state (LERF2). The R50 round-level identity "
    "(event, lambda[0..ell]) is the tower's counting identity over "
    "the object DAG; the source record identity carries NO event "
    "index - both recorded.",
  "requests": "DECLARED - every A12 primitive edit is one forced "
    "request charged to the smallest inherited prefix region "
    "containing its structural/provenance anchors (compiler "
    "_intrinsic_anchor + neighbor inheritance + ROOT fallback).",
  "tokens": "DECLARED per region at ambient depth for CLOCK ticks "
    "(A13R marked-cylinder operator T_{d,mu}; 'only region_mu, "
    "service_depth, and the inherited regional orientation enter "
    "the clock map'); UNDECLARED for the V ~ X standing object "
    "token (UEQ0 has no object concept at all).",
  "objects": "UNDECLARED for a cylinder; DERIVABLE for a region "
    "PROFILE: an object's A12 edit graph inherits a multiset of "
    "anchor regions through the frozen charging rules - a "
    "choice-free object-to-region-profile map exists, but no "
    "single canonical cylinder per object.",
 },
 "letter_semantics": "ROLES_ONLY, in the strongest form: the "
   "alphabet is the three-role local incidence frame {IN, CO, NEW} "
   "per lineage step; a chain does not HAVE a word - it indexes a "
   "depth-D word SPACE W_D^lambda, and after the cyclic-origin "
   "gauge every depth-D lineage shares the identical canonical "
   "address set {0,1,2}^D ('the physical construction must be "
   "independent of those representative origins'; addresses(depth) "
   "takes no lineage argument; 1326 distinct chains share one word "
   "tree). The chain-to-word map is not merely non-injective - it "
   "is not defined.",
 "prufer_note": "The clock tower C_infty = varinjlim(Z/3^{d+1}Z, "
   "q -> 3q) is DECLARED (A13R section 4); the names 'Prufer "
   "3-group' and the Pontryagin-dual footnote are NOT_FOUND "
   "anywhere in the frozen package - the package position's "
   "attribution is corrected; the structure itself is exactly as "
   "carried. Clock depth and cylinder depth share one grading "
   "(DECLARED, A13R sections 4-11).",
}

P2 = {
 "structure": "ULTRAMETRIC (single tree) - correcting the "
   "registered DISJOINT_UNION: the source record space is the "
   "rooted ternary prefix tree R_D = union of Z_3^ell with "
   "append-only extension and the 0/1 equality kernel; equal "
   "prefix symbols are IDENTIFIED ('Different record symbols "
   "occupy orthogonal record states. Equal symbols use the same "
   "record state.'), and no event index exists in the source "
   "identity. With d(r, r') = 3^{-(common prefix length)} and "
   "d(r, r) = 0, the strong triangle inequality holds on all of "
   "R: certified exhaustively (364 nodes to depth 5, 7,971,964 "
   "triples, ZERO violations) and by the standard common-prefix "
   "argument (common(r,t) >= min(common(r,s), common(s,t))).",
 "round_level_note": "The tower's R50 counting identity (event, "
   "lambda[0..ell]) is event-indexed: under it the record "
   "OCCURRENCES form a disjoint union of per-event copies "
   "embedding in the one source tree; records of different events "
   "with equal prefixes sit at symbol-distance 0 and are the same "
   "record STATE (source) while remaining distinct counting "
   "events (round). Both structures recorded; the geometry lives "
   "on the source tree.",
 "readability": "READABLE_FROM_S by construction (records ARE the "
   "fact graph's content).",
}

P3 = {
 "law": "PANEL-REFUTED CANDIDATE, CORRECTED LAW: the reduced-word "
   "hypothesis (N(ell) = 3*2^(ell-1), delta = log_3 2) is REFUTED "
   "as a source law - the 10-marker catalog is HARDCODED (the S_3 "
   "orbit of the arbitrarily preregistered seed (0,1), 'fixed "
   "without inspecting a response'; Marker((0,0)) is legal; "
   "events.py:99-106); the no-repeat condition is not even "
   "gauge-invariant under CD1I's per-frame cyclic origins; and "
   "the CD1I odometer REQUIRES ord(tau_D) = 3^D - a single cycle "
   "through ALL of {0,1,2}^D including repeat-digit words, "
   "positively incompatible with a reduced-word substrate. The "
   "SOURCE law: the record word space is the FULL ternary tree, "
   "fully swept by the odometer; occupancy at frozen-catalog "
   "level: the 903-graph A12 catalog anchors into all 40 ternary "
   "prefixes of depth <= 3 INCLUDING repeat cells ('00','11',"
   "'22': 96 edits each); the R19 356-catalog occupies only root "
   "+ the three depth-1 cells; the A13R marker set is a 10-cell "
   "bounded fixture.",
 "exponent": "delta = 1 EXACTLY, STABLE (D3 sense), on the source "
   "record tree: with full ternary occupancy V(3^{-ell}) = "
   "3^{-ell} of the total - the one-dimensional 3-adic ball law, "
   "forced by the declared odometer order 3^D. Gamma-independent. "
   "The registered delta = log_3 2 (and the package-carried "
   "'branching at most 2 by the two-parent structure', which "
   "does not apply to the word tree at all) are refuted and "
   "recorded.",
 "grade": "STABLE(1) - source-exact via ord(tau_D) = 3^D; the "
   "bounded-depth catalogs carry no asymptotic exponent of their "
   "own (recorded)",
 "two_trees_note": "The round-level chain-prefix tree (directed "
   "recorded chains of the object DAG) is a DIFFERENT structure: "
   "its per-level branching decays through 1 (trajectory readout: "
   "4.5 -> 0.73 by depth 8, labeled) - drifting, not stable. The "
   "stable exponent belongs to the source word tree, not to the "
   "object DAG's chain tree; this sharpens where the geometry "
   "lives: in the record algebra (the readable universe), exactly "
   "as branch (c) proposed.",
 "bedrock_halo": "The word tree is common to all lineages (gauge "
   "independence): the exponent carries no bedrock/halo "
   "distinction at source level; the round-level chain trees "
   "differ (labeled readout), but no cylinder exponent attaches "
   "to them.",
}

P4 = {
 "W_list": "The hierarchical-uniform family is the only choice-free "
   "measure class surfaced: on any FIXED bounded-depth region tree, "
   "every choice-free hierarchical measure has all its mass on "
   "cells of fixed positive fraction (pigeonhole over <= 40 cells; "
   "the S_3 orbit ties are EXACT - 43/43/43 per factor in the R19 "
   "catalog - so no cardinality-based rule can select an o(n) "
   "cell; refine-until-small terminates at depth 1 on the R19 "
   "catalog since its depth-2 cells are empty).",
 "transport": "EXISTS and is CHOICE-FREE (correcting the registered "
   "'no canonical transport'): every A12 edit carries a "
   "content-determined anchor region (compiler.py:41-52, 88-98); "
   "the object-to-region-multiset profile is a frozen-data lookup, "
   "verified schedule-invariant on all 903 catalog graphs "
   "(reversed order and Jacobi vs Gauss-Seidel: zero differences). "
   "The anchor set is NOT the A13R marker set (40 anchor regions "
   "incl. repeats vs the 10 hardcoded markers; the marker depth-2 "
   "cells receive zero R19 edits) - the two region catalogs are "
   "distinct fixtures, both recorded.",
 "trichotomy": "EXTENDS (E-level) to all bounded-depth hierarchical "
   "measures: Theta(n) terminal cells + the R64 bridging bound "
   "give rho >= 1 + Theta(c) - exponential balls; NAMED GAP: the "
   "bridging bound as frozen requires time-representative cells; "
   "marker cells are S_3-equivariant (exchangeable in "
   "distribution) but not pathwise-certified; adversarial toy "
   "cells (deliberately birth-localized, MSD assignment) still "
   "give base 6.4-8.6 exponential growth - the gap does not "
   "change the outcome at any tested scale (labeled). BOUNDARY "
   "(honest, conditional): under UNBOUNDED refinement, "
   "refine-until-small cells become O(1) and the bounded-cell "
   "argument no longer applies; the frozen catalogs do not "
   "provide unbounded refinement, so this conditions on an "
   "instantiation outside the frozen sources; even the toy "
   "unbounded-tree illustration stays exponential (base near 8).",
}

PANEL = {
 "W1_reduced_words": "REFUTED - the no-repeat law is seed-artifact, "
   "not source law; odometer ord = 3^D forces the full tree; "
   "delta = log_3 2 has no source support (grep: zero "
   "occurrences); the corrected exponent is delta = 1 on the full "
   "ternary record tree.",
 "W2_transport": "CORRECTED - transport choice-free and verified; "
   "region catalogs split (40-region A12 anchors vs 10-marker "
   "A13R vs 4-region R19 slice); trichotomy EXTENDS at E-level "
   "with the time-representativeness gap named; boundary "
   "conditional on unbounded refinement.",
}

HC = [
 ["HC1", "target altered; depth/base/weight chosen", "REJECTED",
  "P1-P4 adjudicated verbatim; base 3 is the alphabet; no depth "
  "chosen (the catalog's depth-2 instantiation is a source fact)."],
 ["HC2", "external referent; 'dimension' outside D3", "REJECTED",
  "Internal vocabulary; the Prufer/Pontryagin NAMES were found "
  "absent from source and are not used in any claim."],
 ["HC3", "object-to-cylinder assignment invented", "REJECTED",
  "Objects adjudicated UNDECLARED for cylinders; the region "
  "PROFILE is extracted from the frozen charging rules, not "
  "invented, and yields no single cylinder."],
 ["HC4", "a measure adopted; a non-choice-free measure admitted",
  "REJECTED", "W examined as candidates only; the profile "
  "transport is recorded with its choice-freedom status."],
 ["HC5", "readouts cited as proof", "REJECTED",
  "The ultrametric and orbit certificates are exact; trajectory "
  "chain-prefix tables are labeled."],
 ["HC6", "H5 read; H1-H4 pattern used", "REJECTED",
  "Sentinels parsed=false; extraction touched only the frozen "
  "descent package."],
 ["HC7", "frozen tower modified; BELL2 opened", "REJECTED",
  "Nothing modified; unopened."],
 ["HC8", "hand hash; placeholder", "REJECTED",
  "All hashes in-process."],
]

VERDICTS = {
 "always": "OD0_R65_PASS_BRANCH_C_DERIVED",
 "primary": "BRANCH_C = RECORD_SPACE_EXPONENT(delta = 1)",
 "components": {
  "CYLINDER_MAP": "records DECLARED (one prefix cylinder per "
      "symbol); requests DECLARED (smallest-prefix anchors); "
      "tokens DECLARED per region for clock ticks / UNDECLARED "
      "for the V ~ X standing token; objects UNDECLARED for a "
      "cylinder, DERIVABLE for a region profile",
  "LETTER_SEMANTICS": "ROLES_ONLY (the chain-to-word map is not "
      "defined; one universal address tree)",
  "RECORD_SPACE": "ULTRAMETRIC (single tree; 7,971,964 triples, "
      "zero violations; equal symbols identified at source)",
  "OCCUPIED_EXPONENT": "STABLE(1) - the full ternary tree, "
      "odometer-forced; log_3 2 refuted",
  "W": "hierarchical-uniform family only; choice-free object "
      "transport via the frozen A12 region-profile lookup",
  "TRICHOTOMY_ON_W": "EXTENDS (E-level; time-representativeness "
      "gap named; boundary conditional on unbounded refinement)",
 },
 "prediction_vs_outcome": "Registered: records DECLARED, requests "
  "DERIVABLE, tokens/objects UNDECLARED, letters ROLES_ONLY - as "
  "registered except requests are fully DECLARED and the clock "
  "tick's regional indexing is DECLARED. Registered "
  "DISJOINT_UNION for the record space - REFUTED: the source "
  "identifies equal symbols (no event index in the source "
  "identity), giving a SINGLE exact ultrametric tree; the "
  "event-indexed disjoint union is the round-level counting "
  "picture only. Registered delta = log_3 2 with branching -> 2 "
  "- REFUTED by the panel: the no-repeat structure is a "
  "hardcoded seed orbit, the odometer forces the full ternary "
  "tree, and the true stable exponent is delta = 1. Registered "
  "'no canonical object transport' - REFUTED: the A12 "
  "region-profile lookup is choice-free (verified 903/903). "
  "Registered trichotomy EXTENDS - as registered (E-level, gap "
  "named). Registered primary RECORD_SPACE_EXPONENT - as "
  "registered, with the corrected exponent. Also corrected "
  "against the package position: the 'why 8' premise (source has "
  "a 10-marker catalog and 40 anchor regions; no 8 anywhere), "
  "the Prufer/Pontryagin footnote attribution (structure "
  "declared, names absent), and the per-region five-integer "
  "ledgers DECLARED at UEQ0 spec level (JOINT_ONLY is the "
  "catalog's ROOT instantiation). The prediction constrained "
  "nothing.",
 "r66_recommendation": "RECORD_SPACE_EXPONENT(1) with "
  "TRICHOTOMY_ON_W = EXTENDS, so per the R66 rule: the geometry "
  "of the recorded universe is an exact ultrametric with the "
  "stable 3-adic exponent delta = 1, and no object-level pairing "
  "geometry exists in the parameter-free classes. R66 freezes "
  "this as the geometry candidate (delta = 1 as a derived "
  "dimensionless invariant), records the internal theorem that "
  "the record tree and the clock tower C_infty = "
  "varinjlim(Z/3^{d+1}Z) share one declared depth grading (the "
  "duality NAMES are absent from source and are not asserted), "
  "and opens M8 step 1: the frozen scaling limit of the record "
  "space and the inventory of derived dimensionless invariants "
  "(base 8; 22/35; (5+sqrt(41))/2; sqrt(2)-1; delta = 1; "
  "pi/sqrt(3); the critical line m_c = Gamma + min(H, 2 Gamma); "
  "the MINCOST base family 48/5, 384/35, 256/21; the 1/3 "
  "horizon; the ln(4/3) clock offset; 4.311/0.373 depth "
  "constants) for the dimensionless-comparison protocol - where "
  "external formulas may first be named, under preregistration.",
}
