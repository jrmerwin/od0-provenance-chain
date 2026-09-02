"""OD0-R51 adjudication data (Claude Code executor, package v0.1)."""

RUN_DATE = "2026-09-02"

SELECTOR_STATUS = {
    "S1_per_token_identity": {
        "classification": "DERIVED_GIVEN_TOKEN_DISTINGUISHABILITY",
        "statement": "CD2R's regional B/M/J/V/capacity/P/H objects are "
                     "content-addressed finite sets of IDENTIFIED tokens "
                     "(service.py builds token(name, region, index, ...) "
                     "elements; the matching groupoid is transitive under "
                     "S_(F+D) x S_n with the uniform invariant measure over "
                     "complete matchings of identified requests to slots). "
                     "Only the hypergeometric PUSHFORWARD forgets identity "
                     "to counts. Hence the realization sigma retains which "
                     "vacuum tokens were served, given the frozen "
                     "type-blind distinguishability of the minimal service "
                     "representation axiom; the served vacuum subset is "
                     "uniform over size-S^V subsets.",
        "cite": "CD2_SERVICE_GROUPOID_AND_HYPERGEOMETRIC_PROOF.md; "
                "cd2r/src/service.py:35,46,81",
    },
    "S2_vacuum_token_semantics": {
        "classification": "NEW_IDENTIFICATION (manuscript-adjacent)",
        "statement": "No active source states what V is a set OF beyond "
                     "'vacuum-maintenance requests' per region (UEQ0/A13); "
                     "the reading 'maintenance of existing structure' is "
                     "manuscript-level. The identification V ~ X (one "
                     "standing token per existing object, D = |X|, "
                     "regionally partitioned by prefix region) is therefore "
                     "a NEW_IDENTIFICATION carried INSIDE the candidate "
                     "premise, not source semantics.",
        "d_constancy_note": "R50's finding that D is kernel-constant is a "
                            "property of the frozen kernel MAP (it copies D "
                            "into the successor); it is SILENT on "
                            "re-parameterizing D between applications. "
                            "Overriding the carried D with |X_k| is an "
                            "explicit extension recorded in every V-"
                            "candidate's C5 footprint.",
    },
    "S3_rrp1_scope": {
        "classification": "NO_VACUUM_MARK_IN_SOURCE",
        "statement": "RRP1 (R41) marks served A12 FORCED requests only; no "
                     "active source assigns any persistent mark to served "
                     "vacuum tokens. A vacuum mark is a new persistent "
                     "field; exactly the M=P candidates require it.",
    },
    "S4_genesis_service": {
        "classification": "DETERMINISTIC_ALL_VACUUM_FOR_m_0",
        "statement": "At step 0 with X0={a,b} and V~X: D0=2 (the primitives "
                     "are objects, hence tokens). With m=0: F0=0, n0 = "
                     "min(Gamma,2), and every draw is vacuum - S^V = n0 "
                     "deterministically; for Gamma >= 2 both primitive "
                     "tokens are served with probability 1. With m > 0 the "
                     "chronic load competes and the exact hypergeometric "
                     "table is emitted (genesis_service_table).",
    },
    "S5_regionality": {
        "classification": "TRIVIAL_JOINT_REGION_AT_CONSTRUCTOR_LEVEL",
        "statement": "Tokens belong to the object's smallest inherited "
                     "prefix region (A12 rule). For constructor objects, "
                     "every composite's closed ancestry contains BOTH "
                     "primitives (any composite of dag_size >= 3 descends "
                     "from {a,b}), so the smallest inherited prefix region "
                     "of every composite is the shared joint region; only "
                     "the two primitive tokens sit in proper factor "
                     "regions. The regional pool partition of D under V~X "
                     "is therefore {a-region: 1, b-region: 1, joint: "
                     "|X|-2}. The registered eight-factor-prefix instance "
                     "is an OD0-side refinement, not a constructor-level "
                     "structure.",
    },
}

CANDIDATES = {
    "ADJ-V-S": {
        "premise_a13r0": "Serviced vacuum maintenance of an object is "
                         "enablement-active, same-step: an enabled "
                         "adjunction y={u,v} fires at step k+1 iff the "
                         "standing vacuum tokens of BOTH u and v were "
                         "served at step k. Inert alternative: service has "
                         "no enablement effect (B0).",
        "modifies": "the opportunity law only (which enabled events fire); "
                    "En(X), RO-D, RRP1 untouched; V~X identification and "
                    "per-step D-override carried inside the premise",
        "C1": ["PASS_SCOPED", "deadlock-free on registered Gamma in 2..5 "
               "(genesis: both primitives served w.p. 1 at m=0, positive "
               "probability for all m; drain lemma gives recurrent "
               "vacuum service, |X| >= 5 reached a.s.); DEADLOCKED for "
               "Gamma <= 1: n <= 1 serves at most one token per step and "
               "the same-step gate needs two - exact witness, X = {a,b} "
               "forever"],
        "C2": ["LINEAR", "per-step increment <= C(S^V,2) <= C(Gamma,2), a "
               "constant bound in Gamma alone"],
        "C3": ["PASS", "self-limiting burst-drain cycle: forced inflow per "
               "new object (records x 11..13 requests, >= 22 for a "
               "composite-parent event) exceeds Gamma <= 5, so bursts "
               "starve vacuum (P(S^V=0) rises), growth halts, backlog "
               "drains at rate n per step, vacuum service resumes, growth "
               "restarts; long-run P(S^V=0) is bounded away from 1 (drain "
               "phases recur) and from 0 for m>0-free points; exact "
               "trajectories in the readout"],
        "C4": ["PASS", "lifetime > 1 with probability 1/3 already at "
               "(Gamma=2, m=0, H=0), exact witness in certificates"],
        "C5": ["MINIMAL", "footprint = {opportunity law, V~X "
               "identification, D-override}; En/RO-D/RRP1 untouched; R50 "
               "envelope survives verbatim (record poset, fixed-setting "
               "outcome law, entry point)"],
        "C6": [0, "no persistent field (same-step gate reads sigma_k only)"],
        "C7": [0, "no parameters"],
        "C8": ["DIRECT", "the same-step condition references the step "
               "quotient directly; the R50 envelope says the record poset "
               "and fixed-setting outcome law still survive because RO-D "
               "is untouched"],
        "survivor": True,
    },
    "ADJ-V-P": {
        "premise_a13r0": "Serviced vacuum maintenance of an object is "
                         "enablement-active, persistent: an enabled "
                         "adjunction fires at step k+1 iff both parents "
                         "carry the (new) served-vacuum mark by step k.",
        "modifies": "opportunity law + a NEW persistent vacuum-mark field "
                    "(S3: absent from source) + V~X + D-override",
        "C1": ["PASS_SCOPED", "deadlock-free on registered Gamma in 1..5 "
               "(marks accumulate; both primitives marked a.s.); "
               "DEADLOCKED at Gamma = 0 (no service ever)"],
        "C2": ["POLYNOMIAL", "exact bound: |M_k| <= 2 + Gamma*k marked "
               "objects, and |X_k| <= C(|M_k|,2) + 2 <= C(2+Gamma*k,2)+2 - "
               "quadratic in k. (Corrects the registered prediction's "
               "EXPONENTIAL guess with an exact quadratic upper bound.)"],
        "C3": ["PASS", "same burst-drain mechanism; marks only accumulate, "
               "service competition unchanged"],
        "C4": ["PASS", "same witness shape (a marked pair may already be "
               "exhausted; new objects wait for marks)"],
        "C5": ["MINIMAL_PLUS_FIELD", "as ADJ-V-S plus the vacuum-mark "
               "persistent field (an RRP1-style extension to vacuum "
               "tokens); envelope survives (RO-D untouched)"],
        "C6": [1, "the vacuum mark"],
        "C7": [0, "no parameters"],
        "C8": ["INDIRECT", "gate reads cumulative marks, not the step "
               "index; weaker quotient reference than same-step"],
        "survivor": True,
    },
    "ADJ-F-S": {
        "premise_a13r0": "(stated for completeness) an adjunction fires iff "
                         "a forced A12 request derived from a record on "
                         "each parent's lineage was served same-step.",
        "modifies": "opportunity law + forced-service gating",
        "C1": ["FAIL_ALL_GAMMA", "circular deadlock at step 1, exact: a "
               "forced request exists only after an A12 compile of a "
               "record; a record (RO-D) fires only on a downstream USE; a "
               "use is a fired adjunction; and every adjunction is gated "
               "on a served forced request. At genesis there are no "
               "records, hence no forced requests, hence no serveable "
               "gate token, hence no adjunction ever fires."],
        "C2": ["NOT_REACHED", "deadlocked"], "C3": ["NOT_REACHED", ""],
        "C4": ["NOT_REACHED", ""],
        "C5": ["N/A", ""], "C6": [0, ""], "C7": [0, ""], "C8": ["DIRECT", ""],
        "survivor": False,
    },
    "ADJ-F-P": {
        "premise_a13r0": "(as ADJ-F-S with persistent marks)",
        "modifies": "opportunity law + forced gating + mark",
        "C1": ["FAIL_ALL_GAMMA", "same circular witness: persistence does "
               "not help because no forced request is ever generated"],
        "C2": ["NOT_REACHED", ""], "C3": ["NOT_REACHED", ""],
        "C4": ["NOT_REACHED", ""],
        "C5": ["N/A", ""], "C6": [1, ""], "C7": [0, ""], "C8": ["INDIRECT", ""],
        "survivor": False,
    },
    "REC-V-S": {
        "premise_a13r0": "(stated) an RO-D record fires iff the recorded "
                         "child's vacuum token was served same-step; "
                         "adjunctions free (CO1).",
        "modifies": "RO-D itself (records become conditional on service)",
        "C1": ["PASS", "adjunctions unthrottled - the process leaves "
               "genesis"],
        "C2": ["SUPER_EXPONENTIAL", "adjunction layer is B0/T_sat: "
               "|X_{k+1}| = C(|X_k|,2)+2 - the R50 saturation applies "
               "verbatim (kappa=2)"],
        "C3": ["FAIL", "R50 scan: forced pool exceeds every registered "
               "Gamma by k=2; P(S^V=0) -> 1; degenerate"],
        "C4": ["PASS", ""],
        "C5": ["FORFEITS_ENVELOPE", "modifies RO-D (DERIVED_GIVEN_RO1): "
               "the R50 record-poset invariance and fixed-setting outcome "
               "law no longer hold verbatim (criterion from adjudication "
               "note 1)"],
        "C6": [0, ""], "C7": [0, ""], "C8": ["DIRECT", ""],
        "survivor": False,
    },
    "REC-V-P": {
        "premise_a13r0": "(as REC-V-S, persistent)",
        "modifies": "RO-D + a vacuum mark",
        "C1": ["PASS", ""],
        "C2": ["SUPER_EXPONENTIAL", "same as REC-V-S"],
        "C3": ["FAIL", "same"], "C4": ["PASS", ""],
        "C5": ["FORFEITS_ENVELOPE", "same"], "C6": [1, ""], "C7": [0, ""],
        "C8": ["INDIRECT", ""],
        "survivor": False,
    },
    "REC-F-S": {
        "premise_a13r0": "(stated) a record fires iff a forced request from "
                         "the same lineage was served same-step.",
        "modifies": "RO-D + forced gating",
        "C1": ["FAIL_RECORD_LAYER", "records circularly deadlocked (first "
               "record needs a served forced request, which needs a "
               "record); adjunctions explode ungated - the record layer "
               "never starts, so the process never generates load and "
               "never renders: the record poset is empty forever"],
        "C2": ["SUPER_EXPONENTIAL", "ungated adjunctions"],
        "C3": ["FAIL", "no forced pool at all (no records): lapse "
               "identically 1 where D>0 - degenerate at the opposite pole"],
        "C4": ["PASS", ""], "C5": ["FORFEITS_ENVELOPE", ""], "C6": [0, ""],
        "C7": [0, ""], "C8": ["DIRECT", ""],
        "survivor": False,
    },
    "REC-F-P": {
        "premise_a13r0": "(as REC-F-S, persistent)",
        "modifies": "RO-D + forced gating + mark",
        "C1": ["FAIL_RECORD_LAYER", "same circular witness"],
        "C2": ["SUPER_EXPONENTIAL", ""], "C3": ["FAIL", ""], "C4": ["PASS", ""],
        "C5": ["FORFEITS_ENVELOPE", ""], "C6": [1, ""], "C7": [0, ""],
        "C8": ["INDIRECT", ""],
        "survivor": False,
    },
    "B0": {
        "premise_a13r0": "CO1 alone (control): all enabled adjunctions fire.",
        "modifies": "nothing beyond CO1",
        "C1": ["PASS", "leaves genesis deterministically"],
        "C2": ["SUPER_EXPONENTIAL", "R50: |X_{k+1}| = C(|X_k|,2)+2"],
        "C3": ["FAIL", "R50 saturation: kappa=2 at all 1296 registered "
               "points; P(S^V=0) -> 1; degenerate"],
        "C4": ["FAIL", "R50: lifetime == 1 for every object"],
        "C5": ["NONE", "no modification"], "C6": [0, ""], "C7": [0, ""],
        "C8": ["N/A", ""],
        "survivor": False,
    },
}

MINIMALITY = {
    "survivors": ["ADJ-V-S", "ADJ-V-P"],
    "order_rule": "(C5 footprint, C6 fields, C8 dependence) lexicographic "
                  "(frozen at Commit A)",
    "comparison": "C5: ADJ-V-S = {opportunity, V~X, D-override} strictly "
                  "contained in ADJ-V-P's footprint (which adds the "
                  "vacuum-mark field); C6: 0 < 1. The order is decided at "
                  "C5/C6; C8 (DIRECT vs INDIRECT, favoring P) is never "
                  "reached in the lexicographic comparison - recorded, not "
                  "suppressed. Scope difference recorded: ADJ-V-P covers "
                  "Gamma=1 where ADJ-V-S is deadlocked; this is scope, not "
                  "a selection criterion (frozen survivor rule).",
    "unique_minimum": "ADJ-V-S",
    "premise_statement": "TG1 (throttle gating, stated not adopted): "
        "Serviced vacuum maintenance of an object is enablement-active, "
        "same-step - an enabled adjunction y={u,v} fires at step k+1 iff "
        "the standing vacuum tokens of both u and v were served in the "
        "step-k service realization; under the identification V ~ X (one "
        "standing vacuum token per existing object, D_k = |X_k|, "
        "regionally partitioned by smallest inherited prefix region). "
        "Inert alternative: service has no enablement effect.",
    "scope": "registered Gamma in 2..5; Gamma <= 1 deadlocked (exact "
             "witness); the identification V ~ X is a NEW_IDENTIFICATION "
             "carried inside the premise (S2)",
}

VERDICTS = {
    "always": "OD0_R51_PASS_THROTTLE_CLASS_FROZEN_AND_ADJUDICATED",
    "primary": "THROTTLE_UNIQUE_MINIMAL(ADJ-V-S, TG1, scope Gamma 2..5)",
    "secondary": {
        "SELECTOR_IDENTITY": "DERIVED_GIVEN_TOKEN_DISTINGUISHABILITY",
        "V_IDENTIFICATION": "NEW_IDENTIFICATION (carried inside the premise)",
        "DEADLOCK_WITNESSES": "all four T=F candidates: exact circularity "
            "(request needs record needs use needs enablement needs served "
            "request); ADJ-V-S at Gamma<=1: one token per step vs two-token "
            "same-step gate; ADJ-V-P at Gamma=0",
        "GROWTH_CLASSES": "ADJ-V-S LINEAR (<= C(Gamma,2)/step); ADJ-V-P "
            "POLYNOMIAL (<= C(2+Gamma*k,2)+2, exact quadratic bound - "
            "corrects the prediction's EXPONENTIAL); REC-* and B0 "
            "SUPER_EXPONENTIAL",
    },
    "prediction_vs_outcome": "Confirmed: S1 derived; S2 new identification; "
        "S3 no vacuum mark; S4 deterministic all-vacuum genesis (m=0); T=F "
        "circular deadlock; ADJ-V-S deadlock-free exactly for Gamma >= 2 "
        "with LINEAR growth, burst-drain non-degeneracy, lifetime witness "
        "probability 1/3; envelope survives for ADJ-*; verdict "
        "THROTTLE_UNIQUE_MINIMAL(ADJ-V-S). Corrected: ADJ-V-P's growth "
        "class is POLYNOMIAL (exact quadratic bound), not EXPONENTIAL; and "
        "K_max is resource-bounded per point (exact expansion budget) "
        "rather than uniformly >= 10 - per-point K_max and reasons are "
        "reported in the readout. The prediction constrained nothing.",
    "r52_recommendation": "Per the verdict tree: R52 derives the intrinsic "
        "epoch-observable algebra on the exact throttled process, "
        "conditional on the stated premises (CO1, RO1, TG1, V~X), on "
        "state-defined observables only - the R50 envelope delimits the "
        "quotient-invariant domain; the natural first objects are the "
        "unresolved-shell trajectory, the burst-drain cycle structure of "
        "P(S^V=0), the marked/served filtration, and the lapse process - "
        "with no threshold, label, or historical comparison. This is where "
        "the maturation filtration (M2-M3) begins.",
}

HOSTILE_CONTROLS = [
    ["HC1", "selecting by preference or dynamics readout", "REJECTED",
     "Survivorship and minimality are decided solely by the frozen C1-C8 "
     "rule and (C5,C6,C8) order; the dynamics readout is Part 4 output, "
     "not a criterion."],
    ["HC2", "tuning or singling out Gamma; Gamma>=2 as physical claim",
     "REJECTED", "The full registered Gamma range is scanned; Gamma>=2 is "
     "reported as exact scope with its witness, explicitly not a physical "
     "claim."],
    ["HC3", "external referent in outputs", "REJECTED",
     "No cosmology, particle, inflation, or time referent appears in any "
     "R51 output."],
    ["HC4", "historical rounds = steps; historical numerics", "REJECTED",
     "No identification made; all numerics are this round's own exact "
     "computations or frozen structural constants."],
    ["HC5", "hidden parameters", "REJECTED",
     "All nine candidates are binary and parameter-free by construction "
     "(C7=0 verified per candidate); the load convention (11/record) is a "
     "frozen lower bound, not a tunable."],
    ["HC6", "readouts defining an epoch or basin", "REJECTED",
     "No epoch, basin, regime label, or threshold is defined; shell size "
     "and burst structure are reported as raw trajectories."],
    ["HC7", "frozen-root modification; BELL2", "REJECTED",
     "Read-only access; worktree clean at start and end; BELL2 unopened."],
    ["HC8", "hand-produced hash", "REJECTED",
     "All hashes computed in-process at recording time."],
]
