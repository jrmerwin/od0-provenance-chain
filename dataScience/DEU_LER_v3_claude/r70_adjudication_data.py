"""OD0-R70 adjudication data: H5 opened under the sealed protocol.
(Claude Code.) Extraction by 5-agent workflow (raw in
R70_EXTRACTION_RAW.json); mapping and adjudication per the sealed
R69 rule, exactly as frozen."""

RUN_DATE = "2026-09-02"

STATE_CLASSES = {
 "note": "Extractor state-class tags are raw data; the MAPPING "
   "re-adjudicates for arrow purposes. The derived state is the "
   "pair-closure random ideal under TD1. The H5 foam substrates "
   "(foam.py, run_100M, ledger, deu_reduced, the DE_foam substrate) "
   "are 1 -> 3 face-replacement activation foams with face "
   "consumption and no pair-closure/two-parent structure: NO exact "
   "arrow exists, whatever the growth stochasticity - adjudicated "
   "SCHEDULER_FOAM-family for the state-class rule. "
   "equation_unification: SCHEDULER_FOAM (its own two-queue "
   "scheduler). run_500k/README: OTHER (K5 integer-fission "
   "lattice). U5b, tests.md, locked ledger: PROJECTION_ONLY. "
   "Bridge/prereg documents: manuscript/planning.",
 "consequence": "Every quantitative H5 comparison is "
   "STATE_CLASS_MISMATCH; only definition-invariant patterns "
   "(existence, direction, monotonicity) are comparable, exactly "
   "as the sealed protocol provides.",
}

CLASSIFICATIONS = {
 "closures": {
  "fhub_to_1_hub_closure": "ASYMPTOTIC (f_hub = 1 - 1/d_max -> 1 "
    "only as d_max -> infinity; the DE_foam 'closure target' is a "
    "limit) - per pre-committed diagnosis (iii), NEVER compared "
    "with the finite-count N = 9 Gamma result.",
  "de_sitter_residual_lock": "FINITE_COUNT by its own definition "
    "(a specific product (124/120)(1 + rho_C) tested against "
    "F_req = 1.052718776) - BUT from the MANUSCRIPT_ONLY family "
    "(its computation artifact is missing) and calibration-facing "
    "(lambda_observed): Tier D; recorded at equal prominence, not "
    "compared quantitatively. Its FORM - the existence of a "
    "finite-count closure condition - is the comparable pattern.",
  "collapse_threshold_x50": "FINITE_COUNT (backlog-overwhelms-"
    "capacity at a specific load fraction; the substrate's own "
    "load-versus-capacity condition).",
  "registry_capacity_conditions": "FINITE_COUNT (cap = 137 "
    "fission trigger; md = 137 window; the N* = 137 question, "
    "answered 'no' by the corpus itself).",
  "d_inf_dimension_estimates": "ASYMPTOTIC (N -> infinity limits "
    "of saturating fits) - recorded.",
 },
 "factors": {
  "F_registry_f_hub_124_120_family": "computed on the un-driven "
    "foam checkpoint state (no arrow) AND used inside a "
    "calibration comparison (lambda residuals vs "
    "lambda_observed): STATE_CLASS_MISMATCH + Tier D - not "
    "compared, exactly as registered.",
  "internal_ratios": "the valve quantum 2 and gain 1/6 (derived "
    "internally per the corpus's own audit), the shield channel "
    "count 40 x 3 = 120: INTERNAL_RATIO, recorded.",
 },
 "destruction_mechanism": "YES, corpus-wide in the substrate "
   "family: face consumption with ancestry dropping (foam.py "
   "verbatim: 'the dense, ancestry-dropping storage path'); "
   "grammar-level face replacement (DE_foam); edge severing in "
   "forced fission (run_500k); identity-collapse merging "
   "(horizon proposal); relief-valve voiding "
   "(equation_unification). AND YET no density decrease with "
   "maturity is reported anywhere: all cumulative counts are "
   "nondecreasing, rho_C is reported stationary, f_hub "
   "increasing. The registered branch 'present with density "
   "still reported nondecreasing' is the outcome.",
}

MAP_TABLE = [
 {"notion": "rho_C = carriers/boundary (carrier density)",
  "definition": "carrier-signature faces as a FRACTION of live "
                "boundary faces",
  "class": "fraction_of_total",
  "map": "NOT Q1 by definition (Q1 is records per fixed cylinder "
         "measure; rho_C is a fraction of a growing total) and "
         "NEVER read toward Q8 (fraction-of-total rule): recorded, "
         "uncompared. Reported stationary ~0.019 - no decrease.",
  "mismatch": "n/a (uncompared by rule)"},
 {"notion": "cumulative counts (boundary faces, nodes, active_C, "
   "records of the ledger)", "definition": "raw growing counts",
  "class": "density_maturity_direction",
  "map": "Q1 at PATTERN level: existence and direction of "
         "densities/counts changing with maturity - all "
         "nondecreasing: CONSISTENT with Q1 (THEOREM); no "
         "contradiction despite the present destruction "
         "mechanisms.", "mismatch": "numbers blocked (foam state)"},
 {"notion": "f_hub = 1 - 1/d_max (hub-condensation progress)",
  "definition": "saturation fraction of the maximal hub",
  "class": "ASYMPTOTIC closure variable",
  "map": "direction (increasing with maturity) recorded; its "
         "closure target is ASYMPTOTIC - never compared with "
         "N = 9 Gamma (pre-committed diagnosis iii).",
  "mismatch": "yes for numbers"},
 {"notion": "collapse/relief thresholds (x50 = 1.30 / relieved "
   "~3.5; forced-resolution trigger)",
  "definition": "load-versus-free-capacity conditions on the "
                "scheduler substrate",
  "class": "FINITE_COUNT critical condition",
  "map": "Q2 BY DEFINITION (a load-versus-capacity condition on a "
         "region): the H5 corpus's own critical density is "
         "finite-count and load-typed - existence and form "
         "CONSISTENT with Q2 (THEOREM under TD1+FIXED_MAP); the "
         "numeric thresholds are STATE_CLASS_MISMATCH.",
  "mismatch": "yes for numbers"},
 {"notion": "de Sitter residual closure (124/120)(1 + rho_C) vs "
   "F_req", "definition": "finite-count product lock against a "
   "calibrated cosmological residual",
  "class": "FINITE_COUNT + Tier D + MANUSCRIPT_ONLY",
  "map": "existence-of-finite-count-closure pattern consistent "
         "with Q2's form; the quantitative lock is Tier D "
         "calibration from the family whose computation artifact "
         "is missing - recorded at equal prominence, not "
         "compared.", "mismatch": "Tier D + manuscript-only"},
 {"notion": "sector structures (carrier/feeder/post 81/40/16; "
   "(k,m) valleys; registry sectors)",
  "definition": "registry-content partitions and grammar ridges",
  "class": "distinguished_sector / sector_ordering",
  "map": "UNMAPPED_INAPPLICABLE to the cylinder tree: no "
         "definitional map from any H5 sector structure to "
         "ternary prefix regions exists - the Q4/Q6 fixture "
         "clauses (free root, nine-equal, N = 9 Gamma) are NOT "
         "adjudicated (pre-committed diagnosis ii).",
  "mismatch": "no map"},
 {"notion": "the protected registry (RegistryAnchor, "
   "registry_intact; shielded, never destroyed while the foam "
   "churns)", "definition": "a protected subgraph exempted from "
   "the substrate's destruction",
  "class": "distinguished_sector",
  "map": "the PATTERN 'a distinguished sector that does not "
         "participate' is present in H5 and direction-consistent "
         "with Q4's free-root clause - but the definitional "
         "region map is absent (protected-subgraph != "
         "cylinder-region; intactness != load-freedom): NOT "
         "adjudicated; the echo is recorded in the caveat only.",
  "mismatch": "no definitional map"},
 {"notion": "open-to-mature registry factor family (124/120, "
   "137/124, F_registry_f_hub)", "definition": "state-computed "
   "factors used in calibration screens",
  "class": "early_late_ratio / Tier D",
  "map": "STATE_CLASS_MISMATCH (computed on foam/registry states) "
         "and calibration-facing: not compared (Q5's gate).",
  "mismatch": "yes"},
 {"notion": "fraction-of-total inventory (rho_C, churn 0.478, "
   "hit fractions 20/21, md/N windows, coverage fractions)",
  "definition": "various fractions of totals",
  "class": "fraction_of_total",
  "map": "ALL recorded and left uncompared with Q8, whatever "
         "their values. Q8_TOUCHED = false.",
  "mismatch": "n/a (sealed rule)"},
 {"notion": "rate-vs-rounds items (100M-round schedules, "
   "convergence-in-N predictions, checkpoint laws)",
  "definition": "quantities indexed by engine rounds",
  "class": "rate_vs_rounds", "map": "EXCLUDED (rounds are policy "
  "indices).", "mismatch": "n/a"},
]

TESTS = {
 "Q1_density_direction": "CONSISTENT (THEOREM untouched): every "
   "reported count/density direction is nondecreasing or "
   "stationary with maturity; no decrease anywhere - the FAIL "
   "diagnosis (i) is not triggered even though the substrate HAS "
   "destruction mechanisms (they consume faces/edges, never the "
   "cumulative records the counts track). Pattern-level "
   "agreement; numerics blocked by state class.",
 "Q2_critical_density": "CONSISTENT at the level the protocol "
   "permits: the corpus's own critical conditions are FINITE_COUNT "
   "load-versus-capacity thresholds - the same FORM as Q2; "
   "thresholds not compared (state class).",
 "Q3_boundary_motion": "NOT TESTED: no H5 pattern maps by "
   "definition to depth-graded congestion on a prefix tree; no "
   "contradiction possible and none found.",
 "Q4_Q6_fixture_clauses": "NOT ADJUDICATED (pre-committed "
   "diagnosis ii): no definitional map from any H5 region/sector "
   "structure to the ten-marker fixture; the free-root and "
   "nine-equal signatures untested; the protected-registry echo "
   "recorded in the caveat only.",
 "Q5_ratios": "Directions only: early-to-late count ratios >= 1 "
   "throughout - consistent; every specific factor (124/120 "
   "family) blocked (state class + Tier D).",
 "Q7": "internal only - not compared, per the table.",
 "Q8": "NOT TOUCHED. All fraction-of-total items recorded "
   "uncompared.",
}

VERDICT = {
 "H5_COMPARISON": "PARTIAL",
 "basis": "Every mapped reparametrization-invariant pattern is "
   "consistent with its THEOREM-grade counterpart and none "
   "contradicts one (Q1 direction; Q2 form; Q5 directions). "
   "PARTIAL (not PASS) because the stage-defining H5 observables "
   "are unmapped or gated: rho_C is fraction-of-total "
   "(uncompared by rule); the hub closure is ASYMPTOTIC (never "
   "compared with N = 9 Gamma); the de Sitter lock is Tier D + "
   "MANUSCRIPT_ONLY; the sector structures are "
   "UNMAPPED_INAPPLICABLE; every quantitative ratio is "
   "STATE_CLASS_MISMATCH; the fixture signatures are not "
   "adjudicated for lack of a definitional region map. No FAIL "
   "diagnosis was triggered.",
 "model_family_caveat": "R48 F5 chains as pinned: state fields = "
   "the activation-foam engines (foam.py, run_100M/ledger, "
   "deu_reduced, the DE_foam substrate; 1 -> 3 replacement "
   "grammars with face consumption - destruction present) and "
   "the K5 fission lattice; derived observables = rho_C, d_max, "
   "f_hub, shell censuses, eigenvalue ratios; external "
   "calibrations = lambda_observed, alpha^-1, Planck peak "
   "ratios, H0 anchors, the 6.14 TeV collider anchor; "
   "phenomenological projections = the lambda residual screens, "
   "CMB/BAO/H0 ledgers; fixed bridge assumptions = registry_"
   "factor/carrier_factor bridges, the action-quantum "
   "assignment; manuscript-only = the de Sitter-closure "
   "computation family (artifact missing, carried at equal "
   "prominence). The protected-registry echo of the free-root "
   "pattern is a caveat-level observation, not an adjudicated "
   "comparison. DESTRUCTION_MECHANISM = YES with all counts "
   "nondecreasing.",
}

PART4 = {
 "label": "POST_OPENING_READOUT_NOT_ADJUDICATION_ARCHIVE_ONLY",
 "note": "TD1 places tokens; it does not alter the DAG growth, so "
   "the derived-trajectory values of the UNMAPPED_COMPUTABLE "
   "notions are those already computed in R62_PART4_READOUTS.json "
   "(cited by hash in that round's manifest), valid under TD1 "
   "verbatim.",
 "readouts": {
  "f_hub_analog": "1 - 1/(max containment) on seeded derived "
    "trajectories: 0.9796 / 0.9811 / 0.9885 (G2/G3/G4 points, "
    "n = 51-89) - direction INCREASING with maturity, matching "
    "the H5 f_hub direction (archive observation only).",
  "rho_C_analog": "UNMAPPED_INAPPLICABLE even for the archive: "
    "the carrier signature (0,1,2) is an activation-count "
    "property of the foam grammar with no pair-closure "
    "counterpart; no definition to compute.",
  "top_hub_share": "0.0688-0.0988 (R62 archive), direction "
    "decreasing with n - recorded.",
 },
}

HC = [
 ["HC1", "protocol/table altered; derived-side item added",
  "REJECTED", "Protocol byte-verified at Commit A and applied "
  "verbatim; Q-table untouched."],
 ["HC2", "round aligned; rate compared; Tier D adjudicated",
  "REJECTED", "All rate-vs-rounds and Tier D items excluded and "
  "listed."],
 ["HC3", "name-mapping; quantitative across mismatch; "
  "fraction-of-total vs Q8", "REJECTED", "All maps by definition; "
  "every quantitative item gated; Q8_TOUCHED = false."],
 ["HC4", "closure without classification; N = 9 Gamma vs "
  "ASYMPTOTIC or unfixtured", "REJECTED", "Every closure carries "
  "its pre-committed class; N = 9 Gamma compared with nothing."],
 ["HC5", "H1-H4 consulted; Part 4 in the verdict", "REJECTED",
  "Spent corpora untouched; Part 4 is archive-labeled and feeds "
  "no verdict."],
 ["HC6", "TD1/TG1/cost law/filtration/G1/G2/fields modified",
  "REJECTED", "All frozen."],
 ["HC7", "BELL2 reopened", "REJECTED", "Not reopened."],
 ["HC8", "hand hash; placeholder", "REJECTED",
  "All hashes in-process."],
]

VERDICTS = {
 "always": "OD0_R70_PASS_H5_OPENED_UNDER_SEALED_PROTOCOL",
 "H5_COMPARISON": "PARTIAL",
 "Q8_TOUCHED": False,
 "SEALED_CORPORA_REMAINING": 0,
 "prediction_vs_outcome": "The carried registered prediction is "
  "met on every point: PARTIAL; density direction consistent "
  "with Q1 at pattern level; closure conditions present and "
  "classified ASYMPTOTIC (f_hub) or Tier D/manuscript-only (de "
  "Sitter lock) - not compared with N = 9 Gamma; the "
  "open-to-mature factor STATE_CLASS_MISMATCH; the foam engines "
  "adjudicated to the scheduler-foam family with sector "
  "structure UNMAPPED_INAPPLICABLE; the free-root signature not "
  "adjudicated for lack of a definitional region map; the "
  "destruction mechanism PRESENT with density still reported "
  "nondecreasing (the prediction's second branch); no "
  "THEOREM-grade contradiction; Q8 untouched. One extraction-"
  "level note: the extractors tagged the foams RANDOM_IDEAL; "
  "the mapping re-adjudicated them (no pair-closure arrow) - "
  "recorded, since the raw tags and the mapping decision are "
  "both part of the record.",
 "r71_recommendation": "Every sealed corpus is now spent, with "
  "all five holdout comparisons closed and no theorem-grade "
  "contradiction across H1-H5. R71 is the PROTO-PAPER of the "
  "R48-R70 arc (maturation, geometry, duality, fields, the "
  "passed external comparison, the five holdout comparisons), "
  "in the style of the Bell and descent drafts: every claim "
  "scoped to its premise tower and evidential class; failures "
  "and corrected predictions in the results sections at equal "
  "prominence; the R64 no-go and the Tier D dictionary problem "
  "stated in the first paragraph as what is NOT shown; the "
  "counterexample files cited as part of the theorem record. "
  "Queued after the paper, in order: the relation between the "
  "two geometry candidates; the relief critical line; BELL3; "
  "the Tier D dictionary problem, stated as open.",
}
