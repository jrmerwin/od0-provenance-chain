"""OD0-R52 adjudication data (Claude Code executor, package v0.1)."""

RUN_DATE = "2026-09-02"

REGIONS = {
    "definition": {
        "classification": "CANONICAL_DERIVED (frozen declaration)",
        "statement": "A structural region is an element of the inherited "
                     "prefix-region set R, declared IMMUTABLE in the UEQ0 "
                     "master transition ('R is the immutable structural "
                     "prefix map'); the registered OD0 instance has the "
                     "eight factor-prefix regions (R28). The number of "
                     "regions is FIXED under the growing DAG - no source "
                     "refines regions with depth.",
    },
    "assignment": {
        "classification": "CANONICAL_DERIVED (A12 axiom wording)",
        "statement": "A new object/edit is charged to its SMALLEST "
                     "INHERITED PREFIX REGION (A12: 'one integer forced "
                     "request in its smallest inherited prefix region'). "
                     "At constructor level every composite's closed "
                     "ancestry contains both primitives, so every "
                     "composite is charged to the shared joint region; "
                     "only the two primitive tokens occupy proper factor "
                     "regions (R51 S5).",
    },
    "gamma_per_region": {
        "classification": "CANONICAL_DERIVED",
        "statement": "The frozen ledger is per region (UEQ0: L_mu per "
                     "region mu; kernel applied regionally), so Gamma is "
                     "per region. With the region count fixed, CAPACITY_"
                     "TOTAL = (number of regions) x Gamma is CONSTANT - "
                     "no state dependence.",
    },
    "records_charged": {
        "classification": "CANONICAL_DERIVED",
        "statement": "A record on lineage w and its A12 requests are "
                     "charged to w's region by the same smallest-inherited-"
                     "prefix rule; at constructor level this is the joint "
                     "region for all composite lineages.",
    },
    "verdict": "REGIONS = FIXED(n inherited; effective single active joint "
               "region at constructor level); CAPACITY_TOTAL = constant",
}

RECORD_SCOPE = {
    "verdict": "THROUGH_OWN_LETTER",
    "statement": "The frozen R49 RO-D rule sets ell(lambda, e) = max{k : "
                 "lambda[k] in closed_anc(z)} for a parent z of e; closed "
                 "ancestry includes z itself, so when e uses x_j directly, "
                 "ell = j and the recorded prefix lambda[0..j] INCLUDES "
                 "x_j's own creation letter. Consequence: the first use of "
                 "an object records its whole ancestry cone (the recorded-"
                 "cone invariant), so between global steps the unresolved "
                 "sector is exactly the shell objects' own letters, each "
                 "an independent single-letter append - a PRODUCT state.",
    "sibling_entanglement": "Present WITHIN a step only: same-step sibling "
        "events recording the same prefix share one classical copy "
        "(perfect correlation, the m-party equality structure realized as "
        "same-step record agreement); between steps no unresolved letter "
        "is shared. The registered prediction guessed BEFORE_OWN_LETTER "
        "with persistent m-party equality states - CORRECTED by the frozen "
        "rule.",
    "cluster_theorem": "PASS in the strong product form, conditional on "
        "TG1: between-step clusters are singletons (max size 1); within-"
        "step sibling groups are bounded by Gamma-1 children of one parent "
        "(batch pairs from <= Gamma served objects), so the transient "
        "within-step cluster has size <= Gamma. The two-to-many gap is "
        "closed for the throttled process; every record outcome is a "
        "bounded (single-letter / same-step-correlated) computation.",
    "max_cluster_size": "1 between steps; <= Gamma within a step",
}

INFLOW = {
    "c_first": {
        "value": "11..13 per Q1-type history; 22..26 per Q2-type "
                 "(sibling-shared) history - frozen ranges; exact per-type "
                 "constants live in the frozen F3R history-graph catalog "
                 "(903 graphs, 8 primitive edit types; CD2R A12 audit) and "
                 "are not re-derived here",
        "classification": "FROZEN_RANGE",
    },
    "c_repeat": {
        "value": 2,
        "statement": "A repeated use of an already-recorded prefix "
                     "generates exactly the query token and the temporal "
                     "provenance edge (CD2 population/relief: "
                     "TEMPORAL_PROVENANCE_EDGE is one canonical A12 edit; "
                     "a new query event is a new history node), and NO "
                     "unresolved-cell token (the cell is recorded; CD1I "
                     "Sec 9: stable deeper records append rather than "
                     "rewrite - the A10 write is idempotent on the "
                     "recorded prefix).",
        "classification": "DERIVED",
    },
    "sampled_law": "c_first = 11 (frozen minimum) per newly recorded "
                   "prefix, c_repeat = 2 per repeat record - the declared "
                   "lower-bound load, recorded before the readout",
}

LEDGER_IDENTITIES = [
    "E[S^V | state] = n*D/(F+D), n = min(Gamma, F+D)  [hypergeometric mean]",
    "E[Phi^2 | state] = D/(F+D) when Gamma <= D and F+D >= Gamma "
    "(V0 = Gamma = n); = E[S^V]/D = 1 when F = 0 (all-vacuum); general "
    "case E[Phi^2] = n*D/((F+D)*min(Gamma,D)) exactly",
    "P(S^V >= 2 | state) = 1 - [C(F,n) + C(F,n-1)*C(D,1)]/C(F+D,n) "
    "(closed form; support-clipped)",
    "E[new objects | state] = sum_s P(S^V = s) * C(s,2)*(1-(n_obj-2)/"
    "C(n_obj,2)) with n_obj = |X|  [composition of 4.3 with the law]",
    "relief v = min(2*ceil(max(1, floor((P+2*S^F)/6))/2)_even, H, B-, P-) "
    "when B- >= Gamma and P- >= 6, else 0  [frozen controller verbatim]",
]

LONG_RUN_EXACT = [
    "P(S^V >= 2 | state) >= D(D-1)/((F+D)(F+D-1)) > 0 at every state "
    "(D = |X| >= 2 always): vacuum-pair service never vanishes; no "
    "absorbing stall exists at any finite state (growth is possible from "
    "every reachable state).",
    "D = |X| is nondecreasing along every trajectory (objects are never "
    "destroyed).",
    "Per-step conservation identities of the frozen kernel hold at every "
    "transition (backlog, population, service split).",
    "The recorded-cone mask is monotone nondecreasing (records are never "
    "erased), so the shell is the exact unresolved sector at every step.",
]

MEAN_FIELD = {
    "label": "MEAN_FIELD_CONJECTURE - registered as a conjecture; nothing "
             "fitted; no convergence claim",
    "variables": "x = D/(F+D); u = |U|/|X|; g = E[new objects per step]",
    "one_step_map": [
        "D' = D + g",
        "F' = F + m + c_eff*g - Gamma*(1-x) - v   (c_eff = requests per new "
        "object = records-per-new-object x c_first/c_repeat mix; NOT a "
        "constant - it grows with ancestry-cone path counts, see caveat)",
        "g' = E[C(S^V,2)]*(1-(D'-2)/C(D',2)) with S^V ~ Hypergeom(F',D',n')",
    ],
    "fixed_point_conditions": [
        "inflow = outflow: m + c_eff*g* = Gamma*(1-x*) + v*",
        "g* = E[C(S^V,2) | x*]*(1 - (D-2)/C(D,2)) evaluated at the "
        "stationary x*",
    ],
    "caveat": "The Part 1 identities make c_eff STATE-DEPENDENT and "
              "unbounded: the record count of a use equals the number of "
              "ancestry-cone paths, which grows with DAG depth. A "
              "stationary (x*, u*, g*) with constant c_eff therefore "
              "presupposes bounded-depth growth; the sampled readout tests "
              "exactly this. The conjecture is recorded with this caveat "
              "rather than repaired.",
}

HOSTILE_CONTROLS = [
    ["HC1", "observable added/dropped after Commit A", "REJECTED",
     "The Section-5 inventory was frozen in R52_INPUT_LOCK.json at Commit "
     "A and is emitted unchanged; readouts removed nothing."],
    ["HC2", "epoch label, threshold, or basin from readouts", "REJECTED",
     "No label, threshold, or basin appears anywhere; settle/drift "
     "language in the readout summary describes sampled curves only."],
    ["HC3", "sampled results cited as theorems or used to choose a "
     "quotient level", "REJECTED",
     "The closure ladder was adjudicated purely on the exact transition "
     "systems; the sampled file carries a NEVER-PROOF label."],
    ["HC4", "mean-field map presented as more than a conjecture",
     "REJECTED", "Labeled MEAN_FIELD_CONJECTURE with an explicit validity "
     "caveat; no convergence claim; nothing fitted."],
    ["HC5", "Gamma extrapolated; regions refined without source",
     "REJECTED", "All dynamics at registered Gamma 2..5; regions declared "
     "FIXED per the frozen UEQ0 declaration."],
    ["HC6", "external referent", "REJECTED", "None appears."],
    ["HC7", "historical numeric; rounds=steps", "REJECTED",
     "All numerics generated in-round or frozen structural constants."],
    ["HC8", "frozen-root modification; BELL2", "REJECTED",
     "Read-only; worktree clean at start and end; BELL2 unopened."],
    ["HC9", "hand-produced hash", "REJECTED",
     "All hashes computed in-process."],
]

VERDICTS = {
    "always": "OD0_R52_PASS_GLOBAL_OBSERVABLE_ALGEBRA_AUDITED",
    "components_static": {
        "RECORD_SCOPE": "THROUGH_OWN_LETTER (sibling correlation "
                        "within-step only)",
        "CLUSTER_THEOREM": "PASS (product form; max cluster 1 between "
                           "steps, <= Gamma within a step)",
        "REGIONS": "FIXED (inherited immutable prefix map); "
                   "CAPACITY_TOTAL constant",
        "MEAN_FIELD_CONJECTURE": "recorded with state-dependent c_eff "
                                 "caveat",
    },
    "r53_recommendation_template": "Filled by the pipeline from the "
        "closure and readout results.",
}
