"""OD0-R49 adjudication data (Claude Code executor, package v0.1).

Pure data consumed by build_r49_outputs.py together with
R49_EXACT_CERTIFICATES.json. Every claim cites its exact source.
"""

RUN_DATE = "2026-09-01"

CITES = {
    "NATIVE_PY": "DEU_LER_v0_1_Codex_Package/.../deu_combinatorial_descent_cd0/src/native.py",
    "CATEGORY_PY": "DEU_LER_v0_1_Codex_Package/.../deu_combinatorial_descent_cd0/src/category.py",
    "CD0_REPORT": ".../deu_combinatorial_descent_cd0/CD0_DISTINCTION_EVENT_CATEGORY_REPORT.md",
    "CD1I_SPEC": ".../deu_combinatorial_descent_cd1_incidence/SPEC_CD1I_INCIDENCE_ODOMETER_DESCENT_v0_2.md",
    "CD2_SERVICE": ".../deu_combinatorial_descent_cd2r/CD2_SERVICE_GROUPOID_AND_HYPERGEOMETRIC_PROOF.md",
    "CD2_A12": ".../deu_combinatorial_descent_cd2r/CD2_A12_ATOMIC_EDIT_DESCENT.md",
    "CD2_POP": ".../deu_combinatorial_descent_cd2r/CD2_POPULATION_AND_RELIEF_DESCENT.md",
    "A13R0": ".../deu_a13r_scale_natural_clock_service_v0_1/UEQ0_A13R_CANDIDATE_AMENDMENT.md:8",
    "R28_SPEC": "DEU_LER_v2_codex/.../od0_r28_source_action_reconciliation_v0_1/OD0_R28_SPEC_v0_1.md",
    "UEQ0_MASTER": ".../deu_unified_equations_v1_0/UEQ0_MASTER_TRANSITION_THEOREM.md",
    "R12_REPORT": "DEU_LER_v2_codex/.../r12_bell0_d1_cluster_quotient (two-lineage shared-ancestor machinery)",
    "R16": "DEU_LER_v2_codex/.../r16_general_depth_theorem",
    "CERTS": "DEU_LER_v3_claude/R49_EXACT_CERTIFICATES.json",
}

# ---------------------------------------------------------------------------
# Part 1 - source extraction (Section 4.1) with file/line cites
# ---------------------------------------------------------------------------
SOURCE_EXTRACTION = {
    "object_rule": {
        "statement": "A nonprimitive object is frozenset({left, right}) of two "
                     "DISTINCT previously constructible objects; a candidate "
                     "is admitted at enumeration stage `size` exactly when "
                     "len(closed_ancestors(candidate)) == size.",
        "cite": "native.py:109-122 (build_universe); distinctness by "
                "iteration over current[i+1:] (line 115-116)",
    },
    "gradings": [
        {"name": "dag_size (a.k.a. level)",
         "definition": "dag_size(x) = |closed_ancestors(x)| where "
                       "closed_ancestors includes x itself (native.py:25-31); "
                       "recorded per object (native.py:78, field dag_size); "
                       "used to stratify the enumeration loop "
                       "(native.py:112, for size in range(2, max_dag+1)).",
         "is_stratification_grading": True},
        {"name": "multiplicity",
         "definition": "shape-labelling count (native.py:53-63)",
         "is_stratification_grading": False,
         "reason": "attribute only; never indexes a construction stage"},
        {"name": "parent_overlap",
         "definition": "|closed_anc(parent1) & closed_anc(parent2)| "
                       "(native.py:130)",
         "is_stratification_grading": False,
         "reason": "attribute only; never indexes a construction stage"},
        {"name": "shape / sector / degree",
         "definition": "categorical or level-7-only attributes "
                       "(native.py:34-38, 133-134, adjacency)",
         "is_stratification_grading": False,
         "reason": "non-numeric or scope-restricted; never a stage index"},
    ],
    "transition_vs_grading": {
        "statement": "No step/round/layer is defined as a transition anywhere "
                     "in the executed CD0 source. native.py's size loop is a "
                     "stratified ENUMERATION of a static universe; "
                     "category.py defines ConstructionState.add (single "
                     "adjunction arrows of the derived category, "
                     "category.py:34-37) with no step law, and "
                     "enumerate_ideals is an audit enumeration "
                     "(category.py:40-50). The CD0 report states the "
                     "successor is independent of enumeration or allocation "
                     "identity.",
        "cite": "native.py:112; category.py:34-50; CD0_REPORT (State and "
                "adjunction)",
    },
    "level7_stop_reason": {
        "classification": "CUTOFF_PARAMETER",
        "statement": "build_universe(max_dag: int = 7) - an explicit default "
                     "parameter (native.py:109); the loop stops at max_dag "
                     "(native.py:112). The constructor rule itself is "
                     "unbounded; 173 objects is the size of the frozen "
                     "REGISTERED universe, not a rule restriction. CD0 spec "
                     "Section 1 freezes O_<=7 as 'the exact source-generated "
                     "recursive object universe through DAG level 7'.",
        "cite": "native.py:109,112; CD0 SPEC Sec 1",
    },
}

# ---------------------------------------------------------------------------
# Part 1 - candidate adjudication (Section 4.2-4.4)
# ---------------------------------------------------------------------------
ADJUNCTION_CLASSIFICATION = {
    "candidates": {
        "T_sat": {
            "law": "X -> X union En(X)",
            "determinism": "PASS (set-valued function of X)",
            "order_freeness": "PASS: any batch of enabled events is a union "
                              "of monotone attachments; pairwise diamonds "
                              "exact (CD0); enabledness persists inside the "
                              "batch (certificate: 0 persistence failures "
                              "over the 82-state exhaustive domain)",
            "covariance": "PASS: En(sigma X) = sigma En(X) for primitive "
                          "exchange, verified on all 82 exhaustive states "
                          "(0 failures); C2 is the full constructor-"
                          "preserving automorphism group (CD0 Symmetry)",
            "genesis_compatibility": "PASS: defined at {a,b}; "
                                     "En({a,b}) = {{a,b}} nonempty",
            "unbounded_well_definedness": "PASS: En(X) finite for finite X "
                                          "(bounded by C(|X|,2)); lemma: "
                                          "En(X) is nonempty for every "
                                          "finite construction state under "
                                          "the unbounded rule (a finite X "
                                          "cannot contain all its own "
                                          "pairs); within the frozen "
                                          "universe En(X) is empty only at "
                                          "the complete state",
            "verdict": "CANONICAL",
        },
        "T_dag": {
            "law": "X -> X union {y in En(X) : dag_size(y) minimal}; the "
                   "unique T_g instance (dag_size is the only source "
                   "stratification grading)",
            "determinism": "PASS",
            "order_freeness": "PASS: min-grade batch is cascade-free (an "
                              "added object can only enable objects of "
                              "strictly larger dag_size, since parents are "
                              "proper ancestors); union order-free as above",
            "covariance": "PASS: dag_size is exchange-invariant (verified, "
                          "0 failures; also asserted native.py:209-211)",
            "genesis_compatibility": "PASS",
            "unbounded_well_definedness": "PASS: min over a finite nonempty "
                                          "set",
            "verdict": "CANONICAL",
            "trajectory_fact": "its genesis trajectory is exactly the "
                               "level-completion sequence of the frozen "
                               "universe (sizes 2,3,5,11,36,173) - i.e. the "
                               "source enumeration loop realizes T_dag's "
                               "orbit as a GRADING, not as a transition",
        },
        "T_id": {
            "law": "X -> X",
            "verdict": "CANONICAL_BUT_INERT; no source-backed premise "
                       "excludes it (CD0 disclaims scheduling; frozen R30 "
                       "supplies no opportunity) -> CO1 stated",
        },
        "T_mult, T_povl (attribute-graded variants)": {
            "verdict": "EXCLUDED_FROM_FROZEN_CLASS: multiplicity and "
                       "parent_overlap are source attributes, not "
                       "stratification gradings (never index a construction "
                       "stage); the frozen class instantiates T_g only for "
                       "source gradings in the stage sense. Recorded so the "
                       "exclusion is explicit, not silent.",
        },
    },
    "t_sat_equals_t_g": {
        "answer": "NO - proven with exhaustive smallest witnesses",
        "smallest_states": "the two 4-object ancestry-closed states "
                           "{a,b,{a,b},{a,{a,b}}} and {a,b,{a,b},{b,{a,b}}} "
                           "(a primitive-exchange pair); mixed enabled "
                           "grades {4,5}; T_sat adds 4 events, T_dag adds 1. "
                           "80 of the 82 exhaustive size<=5 ideals have "
                           "mixed enabled grades; only {a,b} and "
                           "{a,b,{a,b}} do not.",
        "genesis_divergence": "first divergence at step k=3: |X3_sat|=12 vs "
                              "|X3_dag|=11; the deferred object is "
                              "{{a,{a,b}},{b,{a,b}}} (dag_size 6)",
    },
    "CO1": {
        "statement": "at each global step, enabled adjunctions occur "
                     "(rather than none)",
        "type": "A13R0-pattern binary activity premise",
        "consequence": "excludes T_id only; does NOT select between T_sat "
                       "and T_dag",
    },
    "asynchronous_laws": {
        "classification": "PREMISE_REQUIRING_SELECTION",
        "selector_constraints_enumerated": [
            "covariance under primitive exchange (else two selectors per "
            "orbit are distinguishable with no source distinction)",
            "fairness/exhaustiveness (every enabled event eventually fires, "
            "else reachability of the trace category is violated)",
            "no dependence on unretained order (CD0 Thm 1: construction "
            "order is not a record)",
        ],
        "selected": "NONE",
        "historical_rounds_note": "historical engine 'rounds' (rung/foam "
                                  "epochs) are asynchronous-policy indices, "
                                  "not saturation layers; no identification "
                                  "between round counts and layers is "
                                  "licensed (hostile controls 3/4)",
    },
    "part1_verdict": "NONUNIQUE_CANONICAL_GIVEN_CO1: the choice-free class "
                     "given CO1 contains exactly two inequivalent canonical "
                     "laws {T_sat, T_dag}",
}

# ---------------------------------------------------------------------------
# Part 2 - record opportunity (Section 5)
# ---------------------------------------------------------------------------
RECORD_CLASSIFICATION = {
    "RO_A": {
        "verdict": "REFUTED",
        "witness": "CD1I SPEC Sec 5 (lines 203-225): the unresolved append "
                   "J_D is the UNIQUE local-C3-invariant isometry appending "
                   "the uniform |u>, with 'no retained distinction among the "
                   "new three incidence roles' as a frozen uniqueness "
                   "condition. An A10 record is the write "
                   "|w>|0> -> |w>|pi_l(w)> (Sec 9, lines 406-414), which "
                   "retains distinction. An adjunction acting as a record on "
                   "the lineage it extends would retain distinction among "
                   "its own new roles, contradicting the frozen uniqueness "
                   "of J_D. RO-A is closed.",
        "consistency_note": "RO-D does not contradict the append: the "
                            "recording event acts on PREVIOUSLY appended "
                            "letters of other lineages; its own new letter "
                            "remains the J_D-invariant append.",
    },
    "RO_D": {
        "verdict": "UNIQUE_GIVEN_RO1 (with the setting residual classified)",
        "assignment": "ell(lambda, e) = the maximal ancestry position k such "
                      "that lambda's member x_k lies in the closed ancestry "
                      "of a parent of e (maximal supported scope). The "
                      "recorded act is the A10 prefix write pi_ell on "
                      "lambda's frontier word.",
        "certificates_D_le_3": {
            "record_uses_enumerated": 74,
            "multi_touch_uses": 32,
            "multi_touch_resolution": "when both parents of e touch lambda "
                                      "at distinct positions, the maximal "
                                      "position is the unique assignment "
                                      "satisfying the scope lemma upper "
                                      "bound and completeness (any smaller "
                                      "ell under-records a structurally "
                                      "supported position); no free "
                                      "parameter remains",
            "scope_lemma": "0 failures: every frame at positions <= ell lies "
                           "inside the closed ancestry of the touching "
                           "parent (frame members are ancestors), so the "
                           "prefix copy distinguishes nothing the event does "
                           "not structurally contain",
            "no_over_recording": "0 failures: the (ell+1) frame's NEW member "
                                 "is never inside the event's scope (by "
                                 "maximality), so recording deeper than ell "
                                 "is never licensed",
            "exchange_covariance": "0 failures over all enumerated uses",
            "reflection_cyclic_gauge": "the assignment uses only unoriented "
                                       "ancestry positions and role-free "
                                       "scope containment; it is manifestly "
                                       "independent of cyclic origin labels "
                                       "and reflection (no gauge symbol "
                                       "appears in the rule)",
        },
        "a10_compatibility": "the induced act is exactly the frozen A10 form "
                             "|w>|0> -> |w>|pi_l(w)>; deeper stable records "
                             "append rather than rewrite (CD1I Sec 9 "
                             "functoriality conditions)",
    },
    "setting_component": {
        "question": "does the downstream event determine the clock setting "
                    "(odometer residue) of the full control, or only the "
                    "query?",
        "answer": "ONLY_THE_QUERY. The full control is "
                  "gamma=(q_A,q_B,n,m) with settings in Z_9 (R28: "
                  "8x8x9x9=5184). The event determines the recorded prefix "
                  "and hence the cylinder-algebra query component (at the "
                  "registered depth-1 instance these are the eight "
                  "source-declared local queries per factor); no structural "
                  "datum of the event determines an odometer residue.",
        "residual_classification": "FORCED_BY_STATE_GIVEN_A13R, not free: "
                                   "the lineage's inherited direct-limit "
                                   "clock residue (A13R; advanced per "
                                   "A13R0 by serviced vacuum events) is "
                                   "state data supplying the setting; the "
                                   "residual is a function of the global "
                                   "state, not a new premise and not an "
                                   "event datum",
    },
    "RO_0_and_RO1": {
        "RO_0_excluded_by_source": "NO - no source statement forces records "
                                   "(CD1I derives record REPRESENTATIONS, "
                                   "not record occurrence; R30 frozen)",
        "RO1": "a distinction event whose parent set includes a lineage "
               "object with an unresolved incidence frontier acts "
               "nontrivially (as an A10 prefix record) on that frontier",
        "RO1_type": "A13R0-pattern binary activity premise",
        "CO1_RO1_relation": "NOT one statement: CO1 excludes only T_id "
                            "(adjunction activity); RO1 excludes only RO-0 "
                            "(record activity of occurring adjunctions). "
                            "Independent axes of the same A13R0 template "
                            "type; a model can satisfy CO1 with RO-0 "
                            "(active but coherent) or vacuously satisfy RO1 "
                            "under T_id. Both are kept.",
    },
    "RO_X_status": "remains the status quo fallback; not selected; it is "
                   "the only candidate compatible with rejecting both CO1 "
                   "and RO1, and keeps OD0 an externally controlled cocycle",
    "hostile_compliance": "no ell tuning against N/S restriction; no A12 "
                          "counts or service outcomes used to pick the "
                          "record rule; no external query alphabet imported "
                          "(the cylinder algebra is CD1I-native)",
}

# ---------------------------------------------------------------------------
# Part 3 - service opportunity (Section 6)
# ---------------------------------------------------------------------------
SERVICE_CLASSIFICATION = {
    "SV_pool": {
        "verdict": "UNIQUE_ORDER_FREE_CANDIDATE",
        "form": "one kernel application per global step on the pooled "
                "forced set: the frozen UEQ0 form F_t = B_t + m_t + C_b "
                "with C_b the disjoint union of J_h over the step's record "
                "outcomes (UEQ0 master equation shape "
                "Pr=p(b) prod_mu K_led(s|L,m+C))",
        "order_freeness_proof": "A12 additivity across a step is frozen "
                                "(CD2R Thm 3: |Compile(J_b)|=|J_b|, "
                                "additive, regional sums agree; simultaneous "
                                "tokens injective); the pooled request "
                                "multiset is therefore a function of the "
                                "step's record-outcome SET, which is "
                                "order-free by CD0 Thm 1 (appends commute; "
                                "records on distinct letters commute)",
        "regional_partition": "via the ancestry/prefix regions of X "
                              "(the eight factor-prefix regions of the "
                              "registered instance; R28 spec line 24)",
    },
    "SV_int": {
        "verdict": "PREMISE_REQUIRING_SELECTION",
        "witness": "exact counterexample (R49_EXACT_CERTIFICATES part3): "
                   "two record-induced forced requests, one vacuum token, "
                   "one draw: pooled P(S^F=1)=2/3; interleaving with the "
                   "draw in the first sub-application gives 1/2. The "
                   "interleaved distribution depends on the split/order of "
                   "kernel applications, which CD0 Thm 1 proves is not "
                   "retained state; selecting a split is therefore a new "
                   "selection premise.",
    },
    "m_external": "persistent load m remains an external input (UEQ0 master "
                  "theorem: the only declared external input); recorded",
    "service_axiom_note": "the hypergeometric kernel itself stands on the "
                          "frozen MINIMAL_SERVICE_REPRESENTATION_AXIOM "
                          "(type-blind slot relation) with the unique "
                          "invariant uniform measure (CD2 service groupoid); "
                          "reused, not rederived; population/relief remain "
                          "FROZEN_MODEL_RULE (CD2 population/relief)",
}

# ---------------------------------------------------------------------------
# Part 4 - obstruction (nonunique family) + verdicts
# ---------------------------------------------------------------------------
OBSTRUCTION = {
    "trigger": "Part 1 yields TWO inequivalent canonical adjunction laws; "
               "Section 7's uniqueness condition fails; the family and its "
               "smallest distinguishing states are emitted instead "
               "(package Sec 7: 'If nonunique: emit the family and the "
               "smallest state distinguishing its members.')",
    "family": {
        "members": ["T_sat-composite", "T_dag-composite"],
        "shared_structure": [
            "genesis z_0 = ({a,b}, 0, empty, Lambda_0, empty) with Lambda_0 "
            "UNDECLARED_IN_SOURCE (reported as required)",
            "identical record layer: RO-D maximal-position prefix records "
            "given RO1",
            "identical service layer: SV-pool hypergeometric form given the "
            "frozen service axiom; m external",
            "identical trace category: both laws' full histories are legal "
            "histories of the SAME ancestry poset (CD0 Thm 1); the "
            "difference is a step-quotient (bundling) choice",
            "shared trajectory through k<=2 (verified exactly; divergence "
            "first at k=3)",
        ],
        "physical_difference": "step bundling is NOT gauge: pooled "
                               "hypergeometric service is non-compositional "
                               "across pools (Part 3 counterexample), so "
                               "the two members generate different "
                               "Lambda/clock trajectories from the same "
                               "record events. Adjunction-law nonuniqueness "
                               "therefore propagates to the service side "
                               "and cannot be quotiented away by Thm 1.",
    },
    "second_blocker": "Lambda_0 UNDECLARED_IN_SOURCE: even given a unique "
                      "law, the trajectory-level ledger is not "
                      "source-determined (reported per Sec 7).",
    "K_max": 3,
    "commuting_diagram": "NOT_REACHED (nonunique adjunction layer + "
                         "undeclared Lambda_0); shared-trajectory "
                         "normalization/covariance facts at k<=2 recorded "
                         "as family-characterization data",
    "cluster_gap": "the frozen shared-ancestor machinery covers Q1 isolated "
                   "lineages and Q2 two-lineage shared-ancestor pairs "
                   "(R12/R16); at k>=1 the global frontier is ONE "
                   "multi-lineage shared-ancestor cluster (census: single "
                   "component at k=1..3 for both members); the "
                   "generalization from two lineages to many is NOT frozen "
                   "- exact gap stated; no factorization assumed "
                   "(hostile control 10)",
}

VERDICTS = {
    "always": "OD0_R49_PASS_OPPORTUNITY_CANDIDATE_CLASS_FROZEN_AND_CLASSIFIED",
    "primary": "OPP_NONUNIQUE_CANONICAL",
    "primary_justification": "The frozen choice-free class given CO1 "
        "contains exactly two inequivalent canonical laws (T_sat, T_dag), "
        "with exhaustive smallest distinguishing states (two 4-object "
        "ideals) and genesis-trajectory divergence at k=3. The record and "
        "service layers are each unique (RO-D given RO1; SV-pool), so the "
        "entire residual nonuniqueness of the global transition is the "
        "adjunction step-quotient - and it is physical, because pooled "
        "service is non-compositional across pools.",
    "secondary": {
        "RECORD_RULE": "RO-A refuted; RO-D unique (residual: setting - "
                       "FORCED_BY_STATE_GIVEN_A13R, not free; query "
                       "determined); RO-0 not excluded -> RO1 stated",
        "SERVICE_RULE": "SV-pool unique; SV-int PREMISE_REQUIRING_SELECTION "
                        "(exact 2/3 vs 1/2 witness)",
        "COMMUTING_DIAGRAM": "NOT_REACHED (nonunique + Lambda_0 undeclared)",
    },
    "prediction_vs_outcome": "The registered prediction (T_sat unique "
        "nontrivial choice-free law; overall OPP_ONE_PREMISE; closure at "
        "K_max=3) is CORRECTED: T_dag (next-grade saturation under the "
        "single source stratification grading dag_size) satisfies every "
        "frozen canonicity criterion and provably differs from T_sat, so "
        "the adjunction layer is nonunique and the primary verdict is "
        "OPP_NONUNIQUE_CANONICAL. The prediction's record-layer and "
        "service-layer expectations (RO-A refuted; RO-D query-not-setting; "
        "SV-pool unique; K_max=3; single coherence cluster at small k) are "
        "all CONFIRMED. The prediction constrained nothing.",
    "r50_recommendation": "Per the verdict tree: R50 = premise-invariant "
        "envelope / no-choice theorem over the two-member family. Exact "
        "shape sharpened by this round: the members share genesis, trace "
        "category, record law, and service form, and differ only in the "
        "step quotient; pooled service makes the quotient physical. R50 "
        "should (i) derive the maximal premise-invariant common structure "
        "(trajectory observables invariant across bundling, e.g. the "
        "record-event partial order and per-event marks), and (ii) test "
        "the one candidate no-choice principle available at source level: "
        "whether service non-compositionality plus a source covariance/"
        "locality condition on step quotients excludes one member exactly "
        "- before considering any new premise.",
}

TERMINAL_STATIC = {
    "R48_PIN": "PASS (manifest sha256 exact; commits resolve; erratum on "
               "R48's fabricated full-hash expansion recorded in "
               "R49_INPUT_LOCK.json)",
    "STEP_SEMANTICS": "no source-defined transition (enumeration only, "
                      "native.py:112 / category.py:40-50); gradings: "
                      "dag_size only (stratification); level-7 stop = "
                      "explicit cutoff parameter max_dag=7 (native.py:109), "
                      "rule unbounded",
    "ADJUNCTION_LINE": "T_sat CANONICAL; T_dag CANONICAL; T_sat != T_dag "
                       "(smallest witnesses: two 4-object ideals; genesis "
                       "divergence k=3); T_id not excluded by source; CO1 "
                       "stated",
    "RECORD_LINE": "RO-A REFUTED (frozen append); RO-D UNIQUE given RO1 "
                   "(74 uses, 32 multi-touch, 0 scope/over-record/"
                   "covariance failures at D<=3); setting residual "
                   "FORCED_BY_STATE_GIVEN_A13R; RO-0 not excluded; RO1 "
                   "stated",
    "SERVICE_LINE": "SV-pool unique order-free (A12 additivity + Thm 1); "
                    "SV-int PREMISE_REQUIRING_SELECTION (2/3 vs 1/2 exact "
                    "witness); order-free parts: appends + request pools; "
                    "order-sensitive part: interleaved ledger updates",
    "GLOBAL_TRANSITION": "two-member canonical family {T_sat-composite, "
                         "T_dag-composite} given (CO1, RO1) + frozen "
                         "premises (service axiom, A13R0, RRP1); smallest "
                         "distinguishing state: 4-object ideal "
                         "{a,b,{a,b},{a,{a,b}}} (and its exchange image)",
    "CLUSTER_LINE": "single shared-ancestor coherence cluster at k=1..3 "
                    "(both members); two-to-many lineage generalization "
                    "NOT frozen - exact gap stated; no factorization "
                    "assumed",
}

HOSTILE_CONTROLS = [
    ["HC1", "enumeration order = step", "REJECTED",
     "native.py's loop is stratified enumeration; CD0 report: successor "
     "independent of enumeration; no output identifies enumeration order "
     "with a step."],
    ["HC2", "DAG size or grading = step unless proved for a T_g", "SCOPED_EXACTLY",
     "T_dag's genesis trajectory IS the level-completion sequence - proved "
     "as a property of that candidate law only; no identification asserted "
     "outside the T_dag member, and the law itself remains one member of a "
     "nonunique family."],
    ["HC3", "asynchronous selection presented as canonical", "REJECTED",
     "all one-event/bounded-batch selector laws classified "
     "PREMISE_REQUIRING_SELECTION; selector constraints enumerated; none "
     "selected."],
    ["HC4", "historical rounds identified with saturation layers", "REJECTED",
     "recorded explicitly: engine rounds are asynchronous-policy indices; "
     "no round-to-layer identification appears in any output."],
    ["HC5", "records assumed active without stating RO1", "REJECTED",
     "RO-0 not excluded by source; RO1 stated as an explicit A13R0-pattern "
     "premise; nothing downstream assumes record activity without it."],
    ["HC6", "record rule tuned so N/S restrict", "REJECTED",
     "the RO-D assignment is fixed by the maximal-supported-scope rule with "
     "zero free parameters BEFORE any restriction question; no N/S "
     "restriction test fed back into the rule (the commuting diagram was "
     "not even reached)."],
    ["HC7", "A12 derivation reopened", "REJECTED",
     "CD2R Thm 3 cited as closed (A12_CANONICAL_DERIVED_EVENT_COUNT); the "
     "R48 recommendation's error on this point is corrected in the package "
     "and honored here."],
    ["HC8", "local depth = epoch, or cluster fraction = epoch by threshold", "REJECTED",
     "no epoch is defined anywhere in this round; cluster censuses are "
     "emitted as raw counts with no threshold."],
    ["HC9", "historical numeric or fitted threshold", "REJECTED",
     "no historical numerics parsed; all computed quantities are exact "
     "integers/rationals generated by this round's own small-k enumeration."],
    ["HC10", "frozen-root modification; BELL2 opened; frontier factorization assumed", "REJECTED",
     "worktree clean under frozen roots at start and end; BELL2 unopened; "
     "the many-lineage frontier treated as one shared-ancestor cluster "
     "system with the two-to-many generalization gap stated explicitly."],
]
