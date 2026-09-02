"""OD0-R50 adjudication data (Claude Code executor, package v0.1).

Pure data consumed by build_r50_outputs.py together with
R50_EXACT_CERTIFICATES.json.
"""

RUN_DATE = "2026-09-02"

ENVELOPE = {
    "L1_object_layer": {
        "class": "INVARIANT_ALL_QUOTIENTS",
        "statement": "The universal DAG (all composites under the unbounded "
                     "rule) and its ancestry order are defined by the "
                     "constructor alone; a step quotient only assigns steps "
                     "and cannot alter objects or ancestry. Definitional "
                     "theorem; no witness needed.",
    },
    "L2_record_poset": {
        "class": "INVARIANT_ALL_QUOTIENTS",
        "statement": "A record event is canonically the pair (using event y, "
                     "recorded prefix path lam[0..ell]) with ell the "
                     "maximal-supported-scope position (R49 RO-D). The "
                     "prefix path lies inside closed_anc(z) for the touching "
                     "parent z of y, and every member of Anc(z) is formed "
                     "before y under EVERY ancestry-compatible quotient "
                     "(q(parent) < q(child) implies ancestors precede). "
                     "Hence the record set attached to y, and the induced "
                     "causal order (records of y precede records of y's "
                     "descendants), depend only on the universal DAG.",
        "canonicalization_required": "The naive identity (full lineage, ell) "
                                     "is NOT invariant: suffix extensions of "
                                     "a lineage that exist only in the "
                                     "later-firing trajectory duplicate the "
                                     "same physical record (9 common events "
                                     "witnessed the failure before "
                                     "canonicalization; 0 after). The A10 "
                                     "write copies pi_ell, so all suffix "
                                     "extensions share one record. Recorded "
                                     "as a refuted naive identification.",
        "verified": "identical (prefix, ell) record sets for all 9 events "
                    "common to both members' k<=3/k<=5 trajectories",
    },
    "L3_record_outcome_law_fixed_settings": {
        "class": "INVARIANT_ALL_QUOTIENTS",
        "statement": "Prefix records are copy maps diagonal in the word "
                     "basis: |w>|0> -> |w>|pi_l(w)>. Any two such maps on "
                     "the same word space commute (both diagonal in one "
                     "basis; the deeper copy refines the shallower), and "
                     "records on disjoint letter sets commute trivially. "
                     "Therefore the joint outcome distribution over any "
                     "finite record set is independent of ordering and "
                     "bundling - quotient-invariant WHEN SETTINGS ARE HELD "
                     "FIXED. Algebraic theorem on the frozen CD1I forms.",
    },
    "L4_settings": {
        "class": "QUOTIENT_DEPENDENT",
        "entry_chain": "quotient -> per-step pool -> service realization "
                       "S^V -> A13R clock advance (A13R0: serviced vacuum "
                       "events act by the least generator) -> odometer "
                       "residue -> setting component of the control -> "
                       "outcome law",
        "only_entry_point_certificate": "Layers 2 and 3 are proven "
                                        "quotient-invariant, and the only "
                                        "quotient-sensitive input remaining "
                                        "in a record's outcome law is its "
                                        "setting (clock residue); the "
                                        "cumulative-ledger witness shows "
                                        "service realizations differ across "
                                        "quotients. This is the sole entry "
                                        "point on the record side.",
    },
    "L5_request_layer": {
        "class_per_record": "INVARIANT_ALL_QUOTIENTS",
        "class_per_step_pool": "QUOTIENT_DEPENDENT",
        "statement": "The A12 request multiset per record is a function of "
                     "the record alone (CD2R Thm 3 compile: additive, "
                     "cardinality-exact, region-covariant). The per-step "
                     "pool is the union over the step's records and differs "
                     "between members from step 3 on (distinct-record "
                     "counts 46 vs 36 at step 3; lower-bound pools 506 vs "
                     "396).",
    },
    "L6_ledger": {
        "class_per_step_conservation": "INVARIANT_ALL_QUOTIENTS",
        "class_cumulative": "QUOTIENT_DEPENDENT",
        "statement": "Per-step conservation (backlog balance, population "
                     "balance, service split) holds for every kernel "
                     "application under any quotient (frozen kernel "
                     "identities, ledger.py conservation()). No cumulative "
                     "horizon quantity beyond them is invariant: the exact "
                     "witness pools the same two unit requests in one step "
                     "vs two steps at the registered point "
                     "(B=0,D=1,Gamma=1,P=0,H=0,m=0) and the total-served-"
                     "forced distributions differ (certificates: "
                     "cumulative_ledger_witness).",
    },
    "L7_marks_interval": {
        "class_realized": "QUOTIENT_DEPENDENT",
        "class_support_envelope": "INVARIANT_CANONICAL_PAIR",
        "statement": "Which requests are served (RRP1 marks) is realization- "
                     "and quotient-dependent. The SUPPORT of achievable "
                     "cumulative served sets is equal for the two members "
                     "at the witness configuration (verified exactly), and "
                     "each individual request admits a positive-probability "
                     "serving realization under both members whenever draws "
                     ">= 1 (positive hypergeometric mass), so the interval "
                     "envelope over all realizations - intersection of "
                     "G- = Int(R) and union of G+ = Cl(R) over achievable R "
                     "- agrees at the witness. Full-generality support "
                     "equality beyond the witness is stated as "
                     "verified-at-witness, not claimed generally.",
    },
    "L8_coherence_lifetime": {
        "class": "INVARIANT_CANONICAL_PAIR",
        "statement": "Lifetime = 1 for every object under BOTH members "
                     "(verified exhaustively at k<=3 (T_sat) / k<=4 "
                     "(T_dag)): the object z0 = {y, p} for p a parent of y "
                     "has depth(z0) = depth(y)+1 and dag_size(z0) = "
                     "dag_size(y)+1, so z0 fires at the very next step in "
                     "both gradings and uses y at its full word depth. "
                     "General theorem: for a quotient q, lifetime(y) = "
                     "min over z with y in Par(z) of q(z) - q(y); lifetime "
                     "== 1 for all y iff every object has a child in the "
                     "immediately next step (both graded members satisfy "
                     "via z0); quotients admitting lifetime > 1 are exactly "
                     "those deferring EVERY child of some y past step "
                     "q(y)+1 - ancestry-compatibility permits arbitrary "
                     "deferral, so such quotients exist (witness: defer z0 "
                     "of any y by one step).",
        "frozen_cap_boundary": "Within the frozen universe O_<=7 the 137 "
                               "level-7 objects are never used as parents "
                               "(exact count), so their words are never "
                               "recorded: the registry shell remains "
                               "permanently coherent inside the frozen "
                               "scope. Under the unbounded rule no such "
                               "boundary exists.",
    },
}

NO_CHOICE = {
    "a_locality": {
        "T_sat": "PASS: step(y) = depth(y), a function of y alone",
        "T_dag": "PASS: step(y) = dag_size(y) - 2, a function of y alone",
    },
    "b_naturality_wrt_representation_grading": {
        "status": "PREMISE_NOT_SOURCE_THEOREM",
        "statement": "The CD1I clock tower C_d, frontier H_D, and append "
                     "J_D are depth-indexed, but no source theorem states "
                     "that the GLOBAL step must be natural with respect to "
                     "representation depth. If assumed it would select "
                     "T_sat (whose step IS depth); it is a premise and is "
                     "NOT applied.",
    },
    "c_selector_freeness": {
        "status": "DEFINITION_NOT_SELECTION_PRINCIPLE",
        "statement": "T_sat fires the full enabled set with no comparison "
                     "function (PRIORITY_FREE); T_dag fires the min-grade "
                     "subset (GRADED). This distinguishes the two laws by "
                     "definition; promoting selector-freeness to a "
                     "selection principle would itself be a premise. Not "
                     "promoted.",
    },
    "d_service_non_compositionality_constraint": {
        "status": "NO_CONSTRAINT",
        "statement": "The frozen kernel is total on every (F, D, n) with "
                     "n = min(Gamma, F+D): it accepts any per-step pool, so "
                     "non-compositionality constrains OUTCOMES across "
                     "bundlings but imposes no admissibility condition on "
                     "quotients beyond ancestry compatibility.",
    },
    "verdict": "NOT_SEPARATED_BY_SOURCE(premise_class = {PRIORITY_FREE, "
               "GRADED})",
}

CAPACITY_SOURCE = {
    "Gamma_capacity": {
        "genesis": "UNDECLARED",
        "under_update": "EXTERNAL_CONSTANT (copied verbatim into every "
                        "successor: UEQ0 src/ledger.py:69-75)",
        "state_function": "NO source formula found in UEQ0, CD2R, A13R, "
                          "R40-R45",
    },
    "D_vacuum_demand": {
        "genesis": "UNDECLARED",
        "under_update": "EXTERNAL_CONSTANT (copied verbatim, ledger.py:71)",
        "state_function": "NO source formula found",
    },
    "m_persistent_load": {
        "genesis": "EXTERNAL (declared external input, UEQ0 master theorem)",
        "under_update": "EXTERNAL per-step input (ledger_kernel argument "
                        "chronic, ledger.py:55)",
        "state_function": "NO - explicitly external",
    },
    "H_relief_candidates": {
        "genesis": "UNDECLARED",
        "under_update": "EXTERNAL_CONSTANT (copied verbatim, ledger.py:74)",
        "state_function": "NO source formula found",
    },
    "q1_gamma_d_from_rendered_structure": "NO. No active source defines "
        "Gamma or D as a function of marks, G+-, |X|, or served history. "
        "(The v30 conscription engine scales a service region with demand, "
        "but it belongs to the F3 scheduler family with NO_MAP into the "
        "active chain - precedent, not source.)",
    "q2_enablement_gated_on_realization": "NO. Enablement is "
        "Par(y) subset X (CD0 category.py:28-32,35); no active source "
        "requires Par(y) subset rendered set.",
    "q3_minimal_throttle_premise_class": [
        {"name": "RG1 rendered-parent gating",
         "form": "an adjunction is opportunity-bearing only if its parents "
                 "are rendered; with the R44 premise-invariant envelope, "
                 "G- gives the lower enabled set and G+ the upper enabled "
                 "set (En(rendered-) subset En_eff subset En(rendered+))",
         "quotient_effect": "makes enablement - hence every layer - depend "
                            "on service realization, coupling the object "
                            "layer to the ledger",
         "parameter": "NONE (binary; A13R0/RO1 template)",
         "binary": True},
        {"name": "state-scaled Gamma",
         "form": "Gamma as a declared function of state (e.g. of |X| or "
                 "served history)",
         "quotient_effect": "capacity trajectory becomes quotient-dependent",
         "parameter": "YES (a function/scale must be chosen)",
         "binary": False},
        {"name": "state-scaled D",
         "form": "D as a declared function of state",
         "quotient_effect": "vacuum pool becomes quotient-dependent",
         "parameter": "YES",
         "binary": False},
    ],
    "census_only": "No candidate is tested dynamically in R50.",
}

VERDICTS = {
    "always": "OD0_R50_PASS_BUNDLING_ENVELOPE_AND_SYNCHRONOUS_FAMILY_CHARACTERIZED",
    "components": {
        "ENVELOPE": "L1 INV_ALL; L2 INV_ALL (prefix-canonical identity); "
                    "L3 INV_ALL (fixed settings); L4 QUOTIENT_DEPENDENT "
                    "(sole entry point, chain certified); L5 per-record "
                    "INV_ALL / pool DEPENDENT; L6 conservation INV_ALL / "
                    "cumulative DEPENDENT; L7 realized DEPENDENT / "
                    "support-envelope INV_PAIR (witness-verified); L8 "
                    "lifetime INV_PAIR (==1 both)",
        "LIFETIME": "==1 for both members; general characterization given; "
                    "frozen-cap boundary: 137 shell objects never recorded",
        "NO_CHOICE": "NOT_SEPARATED_BY_SOURCE(premise_class = "
                     "{PRIORITY_FREE, GRADED})",
        "SATURATION": "SYNCHRONOUS_FAMILY_LEDGER_SATURATES_BY_k=2_FOR_ALL_"
                      "REGISTERED_GAMMA (kappa = 2; 1296 registered points; "
                      "both members; no developmental regime in the "
                      "synchronous family on the registered domain)",
        "CAPACITY_SOURCE": "Gamma/D/H genesis-UNDECLARED and constant under "
                           "update; m external; no rendered-structure "
                           "coupling; no realization gating; minimal "
                           "throttle class recorded (RG1 leading, binary)",
        "REGISTRY_ARROW": "EXACT_OBJECT_SET_ARROW(registry -> constructor, "
                          "dynamics not identified): T_dag^5(genesis) = "
                          "CD0 registered universe exactly (173/173 "
                          "objects; level-7 shell 137/137)",
    },
    "prediction_vs_outcome": "The registered prediction is confirmed on "
        "every tested point, with two sharpenings: (i) record-poset "
        "invariance holds only under the prefix-canonical record identity "
        "(the naive full-lineage identity fails on 9 witnessed events - "
        "the canonicalization is itself a new exact theorem of this "
        "round); (ii) saturation is stronger than predicted: kappa = 2 "
        "(prediction allowed <= 3), with F_2 >= 44 > Gamma_max = 5 at "
        "every registered point for both members. The prediction "
        "constrained nothing.",
    "r51_recommendation": "Per the R51 rule (SATURATES + capacity/"
        "enablement UNDECLARED): classify the minimal throttle premise "
        "class by the A13R/RO1 binary-premise template, with RG1 "
        "rendered-parent gating as the leading candidate (binary, "
        "parameter-free, and the only candidate that couples opportunity "
        "to already-frozen structure - the R44 G-/G+ envelope supplies "
        "its premise-invariant lower/upper enabled sets). Do not add "
        "physical time. Note for R51 scope: under RG1 the quotient-"
        "dependence entry point (L4 chain) feeds back into enablement, so "
        "the envelope theorem of this round delimits exactly what remains "
        "comparable across members.",
}

HOSTILE_CONTROLS = [
    ["HC1", "selecting T_sat or T_dag by preference or saturation readout",
     "REJECTED", "No selection anywhere; the no-choice verdict is "
     "NOT_SEPARATED_BY_SOURCE; the saturation readout is identical in kind "
     "for both members and selects nothing."],
    ["HC2", "using the saturation readout to justify a throttle premise "
     "in-round", "REJECTED", "Part 4 is a census recorded at Commit A "
     "before Part 3 results; RG1 is recorded, not selected, not tested "
     "dynamically."],
    ["HC3", "singling out a Lambda_0 scan value as physical", "REJECTED",
     "All 1296 registered points reported identically; kappa is the max "
     "over the whole domain; no point is distinguished."],
    ["HC4", "step = time; historical rounds = steps", "REJECTED",
     "Steps are quotient indices only; no duration or physical time "
     "appears; historical engine rounds nowhere identified with steps."],
    ["HC5", "kappa or coherence lifetime used as a maturity threshold",
     "REJECTED", "kappa and lifetime are readouts; no epoch, regime label, "
     "or threshold is defined from them."],
    ["HC6", "any historical numeric", "REJECTED",
     "All numbers are generated by this round's own exact computation or "
     "are frozen structural constants (11/13/22/26 request bounds, "
     "registered ranges) cited from frozen sources."],
    ["HC7", "modification of frozen roots; BELL2 opened", "REJECTED",
     "Bytecode writing disabled before importing frozen CD0 source; "
     "worktree clean at start and end; BELL2 unopened."],
    ["HC8", "any hand-produced hash", "REJECTED",
     "Every hash in R50 outputs is computed in-process (hashlib / git "
     "rev-parse) at recording time; the input lock records the rule as "
     "permanent."],
]
