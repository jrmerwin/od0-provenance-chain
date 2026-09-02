"""OD0-R62 adjudication data: H3 and H4 opened under sealed protocols.
(Claude Code.) Two separate adjudications; no cross-use."""

RUN_DATE = "2026-09-02"

# ===================================================================== H3
H3_STATE_CLASSES = {
 "SCHEDULER_FOAM": ["rung2_v30_conscription.py", "TRACKB_C1_DESIGN.md",
                    "grav_geometry.pdf", "grav_geometry.txt",
                    "rung2_v31l/m/n (all five pinned sources)",
                    "deu_vacuum_paper_reproduce.py"],
 "PROJECTION_ONLY": ["registry.py", "DE_gravity_obs (1).pdf",
                     "g_const_search.ipynb",
                     "deu_dynamic_g_s8_manuscript.tex",
                     "deu_dynamic_g_omega_profile.py",
                     "deu_growth_locked_normalization_test.py",
                     "E6_S1_pipeline.ipynb"],
 "OTHER": ["OD0_CODEX_PACKAGE_R48 (protocol document)",
           "E6_A1_preregistration.md (prereg text)",
           "analysis_ready_stacked_voids.csv (observational table)",
           "rmr_gravity_extended.py (integer-lattice engine, not a "
           "pair-closure structure)"],
 "RANDOM_IDEAL": [],
}

H3_MAP_TABLE = [
 {"notion": "load proxy (backlog / pressure_w on the foam; standing "
   "vacuum demand)", "definition": "unserved forced demand + standing "
   "frustrated-face vacuum demand per window",
  "state_class": "SCHEDULER_FOAM",
  "map": "definitional counterpart of the ledger backlog/forced pool "
         "F and standing vacuum demand D (both are unserved-demand "
         "pools competing for capacity)",
  "state_class_mismatch": True,
  "reason": "no exact arrow foam -> random ideal; direction-level "
            "patterns only"},
 {"notion": "gravity-strength proxy mu(a) = 120/D_G(a), D_G: 124->120",
  "definition": "calibrated registry-count ratio in a growth-equation "
                "pipeline",
  "state_class": "PROJECTION_ONLY",
  "map": "UNMAPPED_INAPPLICABLE as a function (external-calibration "
         "projection, R48 F5); its reparametrization-invariant PATTERN "
         "(a small early deficit fading monotonically to zero with "
         "maturity) is compared at pattern level",
  "state_class_mismatch": False,
  "reason": "the pattern class (direction/monotonicity of load effect "
            "with maturity) is protocol-comparable; the function is "
            "not"},
 {"notion": "registry-maturation measure (D_G denominator; A_CMB = "
   "124; f_top hub condensation)", "definition": "counts of active/"
   "condensed registry elements; foam hub-degree fraction f_top = "
   "1 - 1/dmax",
  "state_class": "PROJECTION_ONLY / SCHEDULER_FOAM",
  "map": "support-measure family (R56 O3 support) at definition "
         "level; f_top itself UNMAPPED_COMPUTABLE (computed in Part "
         "4, quarantined)",
  "state_class_mismatch": True,
  "reason": "registry factors used as calibration are Tier D; the "
            "foam condensation fraction has no exact arrow"},
 {"notion": "Omega(r) radial demand profile; corridor census; E6 void-"
   "boundary age step; lattice 1/r field",
  "definition": "spatial/radial profiles and regional contrasts",
  "state_class": "SCHEDULER_FOAM / PROJECTION_ONLY / OTHER",
  "map": "UNMAPPED_INAPPLICABLE (G8: regions JOINT_ONLY; declared "
         "before opening)", "state_class_mismatch": False,
  "reason": "spatial claims excluded by construction"},
 {"notion": "relief valve / edge-collapse surgery; three-flow limit "
   "cycle R = 2(F+V)", "definition": "threshold-gated removal of "
   "standing demand; stationary type-fraction cycle",
  "state_class": "SCHEDULER_FOAM",
  "map": "definitional counterpart of the CD2R relief channel "
         "(threshold-gated voiding of standing demand) -> G6",
  "state_class_mismatch": True,
  "reason": "mechanism-level match; quantitative fixed points not "
            "comparable across state classes"},
 {"notion": "critical load m* in (16, 26) separating stable window "
   "from runaway inflation (TRACKB C1)",
  "definition": "phase structure in persistent load m at fixed "
                "geometry",
  "state_class": "SCHEDULER_FOAM",
  "map": "definitional counterpart of the G7 critical line m_c = "
         "Gamma + min(H, 2 Gamma) (existence of a load threshold "
         "separating bounded from runaway forced-pool behavior)",
  "state_class_mismatch": True,
  "reason": "existence + direction comparable; the numeric threshold "
            "is not"},
 {"notion": "Tier D set (S8, sigma8, Omega_m, H0, G values, 365 ppm, "
   "registry factors 124/120/137 as calibrations, z-limits)",
  "definition": "calibrated cosmological/laboratory quantities",
  "state_class": "PROJECTION_ONLY",
  "map": "recorded as historical values, EXCLUDED from comparison",
  "state_class_mismatch": False, "reason": "Tier D by construction"},
]

H3_SATURATION = {
 "FINITE_EPOCH_DIFFERENCE": [
  "124 -> 120 condensation (early epoch vs a = 1 today)",
  "reverse-flow fraction flat over a 16x horizon (grav_geometry)",
  "arrest basins at dose saturation (late dose > 0.5 criterion)",
  "E6 S3 persistence 'for the remainder of the run'",
  "mu(z=0) = 1 vs mu(z >> 1) = 120/124"],
 "ASYMPTOTIC_CLAIM": [
  "three-flow fixed point / limit cycle R = 2(F+V) (foam "
  "stationarity; STATE_CLASS_MISMATCH for quantitative use)",
  "vacuum-paper mature A = 120 at dmax -> infinity",
  "lattice steady-state after warmup (rmr_gravity_extended)",
  "grav_geometry overlap asymptote 6.4-7.3%"],
 "routing": "Per the pre-committed path, FINITE_EPOCH_DIFFERENCE "
            "items are not comparable to G3; the ASYMPTOTIC items "
            "are on foam/lattice state classes, so their quantita"
            "tive content is STATE_CLASS_MISMATCH; none asserts a "
            "non-decaying band-average lapse, so none contradicts "
            "G3."}

H3_TESTS = {
 "G1_G2_onset": "No historical claim asserts load effects inside the "
   "pre-capacity regime or denies a sharp onset; the conscription "
   "phase structure (stable window at small m) and grav_geometry's "
   "threshold/bistability onsets are direction-consistent with a "
   "sharp entry into the loaded regime. CONSISTENT (direction level; "
   "foam state).",
 "G3_late_decay": "All extracted saturation claims route to "
   "FINITE_EPOCH_DIFFERENCE or to foam-stationarity ASYMPTOTIC "
   "claims about type fractions (not lapse): G3 is neither "
   "contradicted nor quantitatively tested. NOT CONTRADICTED; "
   "stage-defining quantitative test unavailable (state class).",
 "G4_oscillation": "Persistent oscillation with relaxation "
   "(fluctuating swollen window m ~ 8-16; three-flow limit cycle) "
   "is direction-consistent with fixed-amplitude persistent "
   "oscillation. CONSISTENT (direction level).",
 "G5_persistent_load_fading": "The central H3 pattern - a small "
   "early gravity-strength deficit fading monotonically to unity "
   "with maturity (mu: 120/124 -> 1; 'percent-level early "
   "suppression'; 'progressively condensing operator') - matches "
   "the G5 THEOREM pattern (drained-state lapse deficit m/(m+D) "
   "-> 0, fading with maturity, while the rate effect persists) in "
   "direction and monotonicity. CONSISTENT at pattern level; the "
   "proxy itself is a projection (caveat).",
 "G6_relief": "Relief-valve mechanics (threshold-gated removal of "
   "standing demand; stability requires load-proportional dilation; "
   "fixed-gain instability) are mechanism-consistent with the "
   "attracting capped relief fixed point. CONSISTENT (mechanism "
   "level; foam state).",
 "G7_termination_line": "The reported critical load m* in (16, 26) "
   "separating a stable window from runaway inflation matches G7's "
   "critical line in existence and direction (excess persistent "
   "load over capacity + relief -> runaway). CONSISTENT (existence/"
   "direction; numeric threshold not comparable).",
 "G8_spatial": "All spatial claims (Omega(r) profiles, corridor "
   "census, E6 void-boundary steps, lattice fields, S8 maps) "
   "declared UNMAPPED_INAPPLICABLE as sealed.",
}

H3_VERDICT = {
 "verdict": "PARTIAL",
 "basis": "Every mapped reparametrization-invariant pattern is "
   "consistent with the corresponding sealed statement and none "
   "contradicts a THEOREM-grade statement. PARTIAL (not PASS) "
   "because: (i) the load/gravity-strength proxy mu(a) is a "
   "calibrated projection - UNMAPPED_INAPPLICABLE as a function; "
   "(ii) the stage-defining quantitative observables (Omega(r), "
   "f_top condensation, foam fixed points) are UNMAPPED "
   "(spatial-inapplicable, computable-quarantined, or "
   "STATE_CLASS_MISMATCH); (iii) the consistent matches (G5 "
   "pattern, G7 existence, G4/G6 direction) hold at pattern/"
   "direction level, not at exact-arrow level.",
 "model_family_caveat": "R48 F5 chain as pinned: state fields = "
   "scheduler-foam engines (conscription/v31 line; their own "
   "state, not the throttled process); derived observables = "
   "backlog/pressure/corridor/Omega(r) reads; external "
   "calibrations = registry factors (124/120, 137), S8/H0/G "
   "targets, z-limits; phenomenological projections = mu(a) "
   "growth pipeline, 365 ppm G-deficit, E6/A1 astronomical arm; "
   "fixed bridge assumptions = Omega(r) = r_s/r import (made "
   "internal by C1), 137 pressure-gate dictionary import "
   "(declared in-source); manuscript-only = grav_geometry "
   "narrative claims whose late-round generating source (v31o) "
   "is missing.",
 "v31o_note": "The grav_geometry confirmation-round claims (second "
   "gate firing rho = -0.667; legible Dres(r) profile) belong to "
   "the round sequence whose final generating source v31o remains "
   "missing; those specific claims cannot be tied to a pinned "
   "source and are recorded at equal prominence as "
   "manuscript-only.",
}

# ===================================================================== H4
H4_STATE_CLASSES = {
 "UNIVERSAL_IDEAL_BY_LEVEL": ["epoch_time.py (containment/"
   "co-embedding/clock engine on DAG-7 layers)"],
 "SCHEDULER_FOAM": ["GR_QM.pdf engine", "U1_metamorphic_causal_speed",
                    "vacuum_density_clock.py", "instrumented_foam.py",
                    "clock_law_lock.json candidates",
                    "ROUND23_PREREGISTRATION.md",
                    "DEU_SR_Worldline_Clock_Audit.ipynb (foam sample)"],
 "PROJECTION_ONLY": ["41/40 suite (report, tex, clock.py, hubble.py, "
                     "two_clocks tex)", "06_spectral_clock.tex",
                     "coherent_clock_bridge.py",
                     "coherent_decay_clock.py", "U0", "LIGO suite",
                     "candidate3", "rmr_cosmology_locked_candidate_v4",
                     ],
 "OTHER": ["R39/R40 output manifests"],
 "RANDOM_IDEAL": [],
}

H4_CLOCK_IDENTITY = {
 "containment": "epoch_time.py registry_containments = per-object "
   "descendant-containment counts over the DAG-7 registry - the SAME "
   "definition as R56 O1 (containment(w) = #{o : w in closed_anc(o), "
   "o != w}); R56 froze O1 verbatim from this lineage (h1_provenance: "
   "dag_time.ipynb).",
 "coembedding": "registry_pair_coembeddings = common-descendant pair "
   "counts = R56 O2 verbatim.",
 "normalization": "safe_loglog = the ln ln compression = exactly the "
   "R56 O7 clock functional form (tau ~ ln ln of the respective "
   "totals). DEFINITION AND NORMALIZATION IDENTITY: CONFIRMED.",
 "state_class": "UNIVERSAL_IDEAL_BY_LEVEL (deterministic universal "
   "pair-closure DAG, fixed dag_size layers) - no exact arrow to "
   "the random ideal of the throttled process.",
}

H4_MAP_TABLE = [
 {"notion": "containment clock / co-embedding clock (epoch_time)",
  "definition": "ln ln of total containment / total co-embedding "
                "(identical to R56 O1/O2/O7)",
  "state_class": "UNIVERSAL_IDEAL_BY_LEVEL",
  "map": "C5: definitions coincide with the frozen observables; "
         "quantitative offset -> STATE_CLASS_MISMATCH; "
         "definition-invariant ordering adjudicated (see tests)",
  "state_class_mismatch": True,
  "reason": "universal-by-level vs random ideal"},
 {"notion": "Phi^2 capacity-clock law (GR_QM: gamma = 1/Phi; "
   "dtau/dt = sqrt(1 - r_s/r); horizon = saturation surface)",
  "definition": "clock rate = remaining internal update capacity "
                "fraction; frozen at saturation",
  "state_class": "SCHEDULER_FOAM",
  "map": "definitional ancestor of the frozen Phi^2 = S^V/V0 (same "
         "symbol lineage through UEQ0) -> C1/C2 at direction level",
  "state_class_mismatch": True,
  "reason": "foam state; direction/monotonicity comparable, numbers "
            "not"},
 {"notion": "epoch dilation (time_dilation_factor: burden/growth "
   "ratio per step)", "definition": "clock versus process rounds",
  "state_class": "UNIVERSAL_IDEAL_BY_LEVEL",
  "map": "EXCLUDED (rate versus rounds)", "state_class_mismatch": False,
  "reason": "rounds are policy indices"},
 {"notion": "tick vs sweep clocks (instrumented_foam: d(sweep) = "
   "dt/N_F is the scale-free clock)",
  "definition": "global step clock vs per-face proper-time clock",
  "state_class": "SCHEDULER_FOAM",
  "map": "C3 at ordinal level (global process clock runs ahead of "
         "per-object clocks)", "state_class_mismatch": True,
  "reason": "ordinal direction comparable"},
 {"notion": "path-total clock vs object count (epoch_time "
   "total_root_to_node_paths)",
  "definition": "total root-to-node path count vs dag_size/count",
  "state_class": "UNIVERSAL_IDEAL_BY_LEVEL",
  "map": "C3 ordinal (path/chain-mass clocks run polynomially ahead "
         "of the object count; cf. frozen T_n and TC orders)",
  "state_class_mismatch": True,
  "reason": "ordinal only across state classes"},
 {"notion": "index architecture 41/40 (A_G graph index); q_CMB = "
   "137/124; depth constant 122; eta = 40/41",
  "definition": "amplitude/branch indices in likelihood pipelines",
  "state_class": "PROJECTION_ONLY",
  "map": "UNMAPPED_INAPPLICABLE (calibration/branch identification "
         "per the corpus's own statement: 'A formal topological "
         "derivation of 41/40 remains the step required'); recorded "
         "Tier D", "state_class_mismatch": False,
  "reason": "not a definable function on the frozen structure"},
 {"notion": "spectral clock; positronium lifetimes; H0_clocked; "
   "two-clocks Hubble screens; LIGO ringdown compression",
  "definition": "SI-calibrated projection screens",
  "state_class": "PROJECTION_ONLY",
  "map": "Tier D - recorded, excluded", "state_class_mismatch": False,
  "reason": "calibrated dictionaries"},
 {"notion": "native clock-law candidates (clock_law_lock: "
   "C01_BACKLOG_LINEAR ... C06) with status UNDERDETERMINED",
  "definition": "candidate clock increments on scheduler metrology",
  "state_class": "SCHEDULER_FOAM",
  "map": "recorded: the historical family left its native clock law "
         "UNDERDETERMINED with holdouts unopened; no comparison "
         "(their own status)", "state_class_mismatch": True,
  "reason": "no adjudicable claim"},
]

H4_TESTS = {
 "C1_C2_tick_rate": "The GR_QM capacity-clock claims (clock rate = "
   "remaining update capacity; monotone suppression under load; "
   "frozen clock at the saturation surface; 'dead zone below "
   "threshold, graded burst above') are direction-consistent with "
   "C1/C2 (tick rate = Gamma Phi^2; maximal in E0; decreasing in "
   "the band). CONSISTENT (direction; foam state).",
 "C3_three_ages": "Ordinal claims (sweep/proper clock slower than "
   "tick clock; path-total clock ahead of object count; 'growth "
   "monotonic but mild' for the depth clock) are consistent with "
   "the exponent ordering objects < ticks < steps. CONSISTENT "
   "(ordinal).",
 "C4_depth_refinement": "The historical metrology is natively "
   "base-3 (1->3 refinement; 3^{-depth} area weights; the factor 3 "
   "in 3 log10(1+z) 'graph-volume-per-comoving-volume') - "
   "definitionally consonant with the x3-per-depth-increment "
   "refinement law. No depth-band claim to compare. CONSISTENT "
   "(definitional; no contradiction).",
 "C5_clocks": "Definitions and ln ln normalization IDENTICAL to "
   "R56 O1/O2/O7 (confirmed; R56 froze them from this lineage). "
   "Quantitative offset ln(4/3): STATE_CLASS_MISMATCH "
   "(UNIVERSAL_IDEAL_BY_LEVEL has no exact arrow to the random "
   "ideal) - NOT adjudicated. Definition-invariant ordering: "
   "TCo >= TC pathwise on EVERY pair-closure ideal (C(A,2) >= "
   "A - 1 per object), so the co-embedding clock never lags the "
   "containment clock on any state class - the historical corpus "
   "contains no claim of the opposite ordering; CONSISTENT "
   "(adjudicated at definition-invariant level). Monotonicity "
   "(both nondecreasing): THEOREM, consistent.",
 "C6_full_rate_recurrence": "No historical claim addresses full-"
   "tick-rate recurrence; not tested; CONJECTURE grade untouched.",
}

H4_VERDICT = {
 "verdict": "PARTIAL",
 "basis": "No THEOREM-grade statement is contradicted; the clock-"
   "functional definitions and normalization are identical to the "
   "frozen R56 observables; direction/ordinal/definition-invariant "
   "comparisons are consistent throughout. PARTIAL (not PASS) "
   "because: (i) the stage-defining quantitative comparison (the "
   "ln(4/3) clock offset) is STATE_CLASS_MISMATCH and not "
   "adjudicated; (ii) the index architecture (41/40) is "
   "UNMAPPED_INAPPLICABLE (calibration by the corpus's own "
   "admission); (iii) the Hubble/positronium/LIGO screens are "
   "Tier D; (iv) epoch-dilation claims are rate-versus-rounds, "
   "excluded.",
 "clock_offset_adjudicated": "STATE_CLASS_MISMATCH (offset); "
   "ordering adjudicated definition-invariantly: CONSISTENT",
 "model_family_caveat": "R48 F5 chain as pinned: state fields = "
   "the universal DAG-7 layer engine (epoch_time) and scheduler "
   "foams (GR_QM, instrumented_foam, vacuum_density_clock); "
   "derived observables = containment/co-embedding totals, "
   "path-total clocks, tick/sweep clocks; external calibrations = "
   "A_G = 41/40, q_CMB = 137/124, depth constant 122, eta = "
   "40/41, H0/SH0ES anchors, SI spectral units; phenomenological "
   "projections = Hubble/CMB/BAO/SN/LIGO screens; fixed bridge "
   "assumptions = one-motif-per-spectral-tick (declared "
   "'assumed_for_development' in-source), D(N) = log2 N and "
   "3 log10(1+z) maps; manuscript-only = two-clocks narrative "
   "sections. The corpus's own artifacts repeatedly mark the "
   "calibration boundary explicitly ('branch identification "
   "only', 'calibration unless predicted independently', "
   "'UNDERDETERMINED').",
}

HC = [
 ["HC1", "protocol/table altered; derived-side item added",
  "REJECTED", "Both protocols verified by hash at Commit A and "
  "applied verbatim; tables untouched."],
 ["HC2", "round alignment; rate compared; Tier D or spatial "
  "adjudicated", "REJECTED", "Epoch-dilation and Hubble screens "
  "excluded; all Tier D recorded-only; spatial -> G8/inapplicable."],
 ["HC3", "mapping by name/word/count; quantitative comparison "
  "across STATE_CLASS_MISMATCH", "REJECTED", "All maps are by "
  "definition (formulas/code lines); every quantitative comparison "
  "across a mismatch was withheld (the ln(4/3) offset above all)."],
 ["HC4", "H5 read; H1/H2 consulted", "REJECTED",
  "H5 sentinel parsed=false at start and end; H1/H2 untouched."],
 ["HC5", "Part 4 content in a verdict; cross-corpus use",
  "REJECTED", "Part 4 file carries the quarantine label and feeds "
  "no verdict; H3 and H4 adjudicated separately."],
 ["HC6", "TG1/cost law/filtration/A13R/M7 modified", "REJECTED",
  "All frozen; comparisons only."],
 ["HC7", "BELL2 opened", "REJECTED", "Unopened."],
 ["HC8", "hand hash; placeholder", "REJECTED",
  "All hashes in-process."],
]

VERDICTS = {
 "always": "OD0_R62_PASS_H3_H4_OPENED_UNDER_SEALED_PROTOCOLS",
 "H3_COMPARISON": "PARTIAL",
 "H4_COMPARISON": "PARTIAL",
 "prediction_vs_outcome": "Registered: H3 PARTIAL with the load "
  "proxy a projection-chain calibration (UNMAPPED_INAPPLICABLE as "
  "a function), registry maturation mapping to support/containment, "
  "saturations FINITE_EPOCH_DIFFERENCE, spatial claims present and "
  "inapplicable, mixed state classes - outcome: as registered on "
  "every point except that the registry-side inputs were "
  "PROJECTION_ONLY/SCHEDULER_FOAM rather than "
  "UNIVERSAL_IDEAL_BY_LEVEL, and one saturation family (foam fixed "
  "points) classified ASYMPTOTIC. Registered: H4 PARTIAL with "
  "clock functionals coinciding with R56 up to normalization, "
  "state class UNIVERSAL_IDEAL_BY_LEVEL, ln(4/3) offset "
  "STATE_CLASS_MISMATCH, definition-invariant ordering consistent, "
  "clock-rate claims excluded as rounds-based, index architecture "
  "unmapped - outcome: exactly as registered (the identity holds "
  "including normalization, not just up to it). No THEOREM-grade "
  "statement contradicted in either corpus - as registered. The "
  "prediction constrained nothing.",
 "r63_recommendation": "Both comparisons PARTIAL, so all four "
  "spent holdouts (H1, H2, H3, H4) have now been met without "
  "contradiction of any theorem-grade statement. Per the R63 "
  "rule: R63 opens the geometry stage (roadmap stage 7, "
  "previously blocked) - derive an operational quasi-metric on "
  "the mature random ideal from frozen structure only (ancestry "
  "law, cone structure, containment, event-indexed reachability "
  "from R38), target-blind, with the R47 boundary (no holonomy, "
  "no strict connection) retained. H5 stays sealed until a "
  "derived density observable exists (the Part 4 quarantined "
  "readouts are candidate material for that freeze).",
}
