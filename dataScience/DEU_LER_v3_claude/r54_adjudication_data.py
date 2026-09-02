"""OD0-R54 adjudication data: H1 extraction, mapping by definition, and the
frozen-rule adjudication. (Claude Code executor, package v0.1.)"""

RUN_DATE = "2026-09-02"

EXTRACTION = {
    "primary_artifacts": {
        "paper_notes": "RMR_utility/dag_char/dag_time.ipynb cell 89 - the "
                       "embedded 'Distinction engine paper notes' document "
                       "(the missing distinction_engine_paper_notes.md, "
                       "recovered inside the notebook), plus analysis "
                       "cells 40/50; RMR_utility/apr_17_progress.md "
                       "(session notes, structural theorems and "
                       "corrections)",
        "model_family": "the synchronous full-saturation distinction "
                        "engine - 'at each step, every previously unused "
                        "unordered pair generates a new composite object' "
                        "(verbatim) - i.e. exactly the T_sat law - with "
                        "the regime analysis performed STATICALLY on the "
                        "dag_size foliation of the fixed completed "
                        "universe G_6 (2,598,062 objects). R48 census "
                        "family: the recursive DAG-7 registry constructor "
                        "line / structural pipeline (analytic registry + "
                        "audit notebooks). Not reclassified.",
        "supporting_negatives": [
            "DEU_unification task2 REGISTRY_FACTORIZATION_AUDIT.md: the "
            "432/27/2-9 factorization claims FAIL against the frozen "
            "registry (historical program's own negative result)",
            "DEU_bridge/CARRIER_HUB_NULL.md: the foam does not natively "
            "generate the registry's degree structure (structural null)",
        ],
    },
    "historical_regime_sequence_verbatim": [
        {"label": "registry formation / global illumination",
         "coordinate": "dag layers 7-8",
         "report": "137-object DAG-7 registry closes; 'by DAG-8, all "
                   "registry nodes are already present in higher-layer "
                   "exposure' - the first lights-on result"},
        {"label": "broadening", "coordinate": "roughly DAG-9 to DAG-12",
         "report": "support grows, visibility rises, effective support "
                   "increases - more spatial interaction modes active"},
        {"label": "freeze-out onset", "coordinate": "DAG-12 to DAG-13",
         "report": "support breadth contracts, effective pair diversity "
                   "falls, but total pair weight continues to rise - "
                   "concentrating interactions into fewer channels"},
        {"label": "support locking", "coordinate": "DAG-13 to DAG-14",
         "report": "the support set remains the same, but the surviving "
                   "channels intensify - frozen in topology, not in "
                   "weight"},
        {"label": "late concentration", "coordinate": "DAG-14 to DAG-15",
         "report": "support shrinks a little further, concentration rises "
                   "further; the 95th-percentile weighted persistent "
                   "backbone collapses exactly onto the 9-node spatial "
                   "bedrock (K9)"},
    ],
    "coordinate_note": "The historical regimes are reported along the "
        "dag_size LAYER coordinate of a fixed synchronous universe (a "
        "foliation of a completed object), not along engine steps; the "
        "source itself stresses that step and dag_size are different "
        "quantities and flags the late layers as truncation-mixed. "
        "Historical numeric layer boundaries (9-12, 12-13, 13-14, 14-15) "
        "and the K9/80-percent figures are recorded as historical values "
        "only, playing no role.",
    "historical_observables": [
        {"name": "exposure / containment",
         "definition": "for each registry object w and layer d: the "
                       "number of dag-size-d objects containing w as a "
                       "complete ancestral sub-DAG",
         "direction": "rising through broadening (illumination by DAG-8)"},
        {"name": "pair co-embedding",
         "definition": "number of registry pairs co-embedded in the same "
                       "host object, per layer",
         "direction": "broadens in later layers; coembedding clock "
                      "advances fastest (R3 ~ 1.42 > 1)"},
        {"name": "support size (nonzero spatial pairs)",
         "definition": "count of spatial-81 pairs with nonzero "
                       "co-embedding weight at layer d",
         "direction": "up in broadening, contracts at freeze-out, "
                      "constant in locking, slightly down in "
                      "concentration"},
        {"name": "visibility / entropy-effective support / participation "
                 "ratio",
         "definition": "diversity measures of the spatial-pair weight "
                       "distribution at layer d",
         "direction": "up in broadening; down from freeze-out on"},
        {"name": "concentration measures / weighted backbone",
         "definition": "high-percentile thresholding of persistent pair "
                       "weights across layers 13-15; the surviving clique",
         "direction": "rising late; collapses onto the 9 spatial "
                      "degree-136 bedrock nodes"},
        {"name": "global dilution",
         "definition": "81 / |V_d| across layers",
         "direction": "monotone decreasing"},
        {"name": "mean parent-child degree",
         "definition": "2|E|/|V| of the full parent-child graph",
         "direction": "rises 2.40 -> 4.00 and saturates at 4"},
        {"name": "total directed paths (global clock candidate)",
         "definition": "total root-to-node directed paths in G_s; "
                       "tau ~ log log(total paths)",
         "direction": "increasing (clock candidate; compressed)"},
        {"name": "registry containment / coembedding clocks",
         "definition": "log log of registry containments / pair "
                       "coembeddings",
         "direction": "increasing; faster than the global clock (R2 < 1)"},
        {"name": "shell / two-epoch stratification",
         "definition": "step-s objects have degree exactly 2 (no "
                       "children); step-<s objects saturated - the shell "
                       "is the childless population",
         "direction": "shell dominates as s grows"},
        {"name": "dag_size layer populations",
         "definition": "count of objects at each dag_size",
         "direction": "each layer count nondecreasing in time; the "
                      "unimodal G_6 profile is flagged by the source as "
                      "truncation-mixed"},
        {"name": "foam hub degree distribution (CARRIER_HUB_NULL)",
         "definition": "degree distribution of the DEU foam carrier "
                       "supergraph",
         "direction": "power-law; historically shown NOT to match the "
                      "registry (negative result)"},
        {"name": "sector condensation dynamics (HetSim)",
         "definition": "Metropolis dynamics on the co-embedding lattice "
                       "with interface-mediated condensation",
         "direction": "matter-like condensation requires the interface "
                      "sector"},
    ],
}

MAP_TABLE = [
    {"historical": "mean parent-child degree",
     "derived": "composite-graph degree distribution (frozen R52 "
                "inventory); mean degree = 4(n-2)/n EXACTLY on any "
                "ideal (every composite contributes exactly two parent "
                "edges) - law-independent",
     "status": "MAPPED",
     "monotonicity": "historical: rising to 4 and saturating; derived: "
                     "4(n-2)/n strictly increasing to 4 in |X| - THEOREM. "
                     "MATCH (theorem-grade)."},
    {"historical": "total directed paths (global clock)",
     "derived": "chain-multiplicity distribution total (frozen R52/R53 "
                "observable; sum functional)",
     "status": "MAPPED",
     "monotonicity": "historical: increasing; derived: total chains "
                     "nondecreasing - THEOREM. MATCH. (log log is a "
                     "reparameterization, not a separate observable.)"},
    {"historical": "dag_size layer populations",
     "derived": "dag_size distribution (frozen R52 inventory)",
     "status": "MAPPED",
     "monotonicity": "historical: layer counts nondecreasing in time "
                     "(profile shape flagged truncation-mixed by the "
                     "source); derived: per-level counts nondecreasing - "
                     "THEOREM. MATCH on the clean monotone claim."},
    {"historical": "shell / two-epoch stratification",
     "derived": "unresolved shell |U| and fraction u = |U|/|X| (frozen "
                "R52 inventory) - identical function: the childless "
                "population",
     "status": "MAPPED",
     "monotonicity": "historical: shell dominates under synchronous "
                     "growth; derived: u slowly increasing - READOUT. "
                     "MATCH at readout level (labeled)."},
    {"historical": "exposure / containment",
     "derived": "UNMAPPED_COMPUTABLE - containment counts are "
                "well-defined on z+ (number of objects whose closed "
                "ancestry contains w) but are NOT in the frozen R52 "
                "inventory (which carries chains ending at an object, "
                "not hosts containing it)",
     "status": "UNMAPPED_COMPUTABLE", "monotonicity": "n/a"},
    {"historical": "pair co-embedding",
     "derived": "UNMAPPED_COMPUTABLE (same reason)",
     "status": "UNMAPPED_COMPUTABLE", "monotonicity": "n/a"},
    {"historical": "support size (spatial pairs)",
     "derived": "UNMAPPED_COMPUTABLE (well-defined once the registry "
                "objects exist in X; the R50 registry arrow gives exact "
                "object identity)",
     "status": "UNMAPPED_COMPUTABLE", "monotonicity": "n/a"},
    {"historical": "visibility / effective support / participation ratio",
     "derived": "UNMAPPED_COMPUTABLE", "status": "UNMAPPED_COMPUTABLE",
     "monotonicity": "n/a"},
    {"historical": "concentration / K9 weighted backbone",
     "derived": "UNMAPPED_COMPUTABLE (persistent cross-layer weighted "
                "supports; computable in principle on states containing "
                "the deep layers)",
     "status": "UNMAPPED_COMPUTABLE", "monotonicity": "n/a"},
    {"historical": "global dilution 81/|V_d|",
     "derived": "UNMAPPED_COMPUTABLE (early-layer fraction of X)",
     "status": "UNMAPPED_COMPUTABLE", "monotonicity": "n/a"},
    {"historical": "registry containment/coembedding clocks",
     "derived": "UNMAPPED_COMPUTABLE (functions of the two unmapped "
                "count families)",
     "status": "UNMAPPED_COMPUTABLE", "monotonicity": "n/a"},
    {"historical": "parent-child diameter",
     "derived": "UNMAPPED_COMPUTABLE (graph functional of X; not in "
                "frozen inventory)",
     "status": "UNMAPPED_COMPUTABLE", "monotonicity": "n/a"},
    {"historical": "foam hub degree distribution",
     "derived": "UNMAPPED_INAPPLICABLE (requires the foam family; no "
                "exact arrow into z+ - R48 NO_MAP)",
     "status": "UNMAPPED_INAPPLICABLE", "monotonicity": "n/a"},
    {"historical": "HetSim sector condensation dynamics",
     "derived": "UNMAPPED_INAPPLICABLE (requires the HetSim Metropolis "
                "family on the co-embedding lattice; externally supplied "
                "dynamics, R48 census)",
     "status": "UNMAPPED_INAPPLICABLE", "monotonicity": "n/a"},
]

ADJUDICATION = {
    "coarsening_assignment": [
        {"historical": "registry formation / global illumination",
         "derived_placement": "E0 -> early E1, the transient "
                              "{c_min <= Gamma} stratum: the era in which "
                              "the cheap (registry-level) pairs are still "
                              "enabled and forming; its last exit is the "
                              "derived sharp event (THEOREM stratum)"},
        {"historical": "broadening",
         "derived_placement": "early E1 renewal-rich regime: bursts "
                              "frequent, |X|/recorded-cone/total-chains "
                              "all rising (THEOREM-class monotone "
                              "observables)"},
        {"historical": "freeze-out onset",
         "derived_placement": "late E1 regime by frozen monotone "
                              "observables: full-drain frequency "
                              "decreasing (READOUT) and typical burst "
                              "cost increasing (READOUT); growth "
                              "decelerating (READOUT sqrt-k-type)"},
        {"historical": "support locking",
         "derived_placement": "asymptotic regime (same placement class as "
                              "freeze-out continuation; no frozen "
                              "observable separates locking from "
                              "concentration - placed weakly "
                              "order-preservingly, no reversal)"},
        {"historical": "late concentration",
         "derived_placement": "asymptotic regime (as above)"},
    ],
    "no_reversal": "No historical transition maps against the derived "
                   "order: the assignment is monotone from the historical "
                   "ladder into E0 < early-E1 < late-E1 <= asymptotic. "
                   "The coarsening test PASSES with the last two "
                   "historical stages sharing one derived placement.",
    "monotonicity_results": {
        "matches_theorem_grade": ["mean parent-child degree",
                                  "total directed paths / chains",
                                  "dag_size layer populations"],
        "matches_readout_grade": ["shell fraction (labeled: match of "
                                  "readouts)"],
        "not_mapped": "9 UNMAPPED_COMPUTABLE + 2 UNMAPPED_INAPPLICABLE",
    },
    "verdict": "PARTIAL",
    "verdict_reason": "Per the frozen rule: the historical sequence "
        "coarsens the derived filtration order (explicit assignment, no "
        "reversal), and every MAPPED observable matches with its class "
        "stated - but the stage-DEFINING observables of freeze-out, "
        "locking, and concentration (support size, visibility/"
        "participation, concentration/K9 backbone) and the containment/"
        "coembedding clocks are UNMAPPED_COMPUTABLE: their definitions "
        "are well-formed on z+ but absent from the frozen R52/R53 "
        "inventory. 'PARTIAL if the sequence matches but an observable "
        "does not map.' The registered prediction (PARTIAL; through-path/"
        "hub measures unmapped; concentration resting on them; no "
        "contradiction of the derived order) is CONFIRMED on every "
        "point.",
    "model_family_caveat": "The historical engine's opportunity law is "
        "synchronous full saturation - verbatim 'at each step, every "
        "previously unused unordered pair generates a new composite "
        "object' - i.e. exactly T_sat (B0/CO1 alone), the law R50 proved "
        "SATURATES every registered ledger by step 2; and the historical "
        "regimes are read on the dag_size foliation of a completed "
        "static universe, not on process time. The derived side is the "
        "throttled TG1 law on process time. Any mismatch may reflect "
        "this model-family/coordinate difference rather than the "
        "constructor. This caveat does not soften the verdict.",
    "cross_validations_noted": [
        "the historical level-8 count 945 equals the R50 exact level-8 "
        "computation (independent)",
        "the historical growth sequence 5, 12, 68, 2280, 2598062 equals "
        "the R50 T_sat closed recurrence |X_{k+1}| = C(|X_k|,2)+2 "
        "(independent)",
        "the historical shell decomposition (degree-2 childless shell) "
        "is the derived |U| shell under T_sat",
    ],
}

HOSTILE_CONTROLS = [
    ["HC1", "observable/criterion/stratum changed after Commit A",
     "REJECTED", "The derived-side table is byte-identical to the Commit-A "
     "lock; the adjudication uses only its items; the repeat-record "
     "concentration analogy noticed during extraction was NOT added to "
     "the derived side (it appears nowhere in the adjudication)."],
    ["HC2", "historical round number aligned with a derived step",
     "REJECTED", "Historical layer boundaries (9-12 etc.) recorded as "
     "historical values only; no numeric alignment appears anywhere."],
    ["HC3", "mapping by name, word, or count", "REJECTED",
     "Every MAPPED row is a function-level identity (mean degree = "
     "4(n-2)/n; total chains; per-level counts; childless population); "
     "shared words (broadening, shell, clock) map nothing."],
    ["HC4", "H2-H5 content read", "REJECTED",
     "Only the 30 H1-manifest paths were opened; H2-H5 sentinels remain "
     "parsed=false at start and end."],
    ["HC5", "Part 4 leaking into the verdict", "REJECTED",
     "The quarantined readout lives in its own file and key; the "
     "adjudication text contains no reference to its values."],
    ["HC6", "TG1/cost law/filtration modified in response", "REJECTED",
     "Nothing modified; R55 queue unchanged."],
    ["HC7", "frozen roots; BELL2", "REJECTED",
     "Read-only; worktree clean at start and end; BELL2 unopened."],
    ["HC8", "hand hash; placeholder in a report", "REJECTED",
     "All hashes in-process; the stamp convention replaces every "
     "placeholder (commit C writes the R54 stamp)."],
]

VERDICTS = {
    "always": "OD0_R54_PASS_H1_OPENED_UNDER_FROZEN_PROTOCOL",
    "primary": "H1_COMPARISON = PARTIAL",
    "secondary": {
        "MAP_TABLE": "mapped: 4, unmapped_computable: 9, "
                     "unmapped_inapplicable: 2",
        "H2_PIN": "incomplete (no Run3_Dijet artifacts supplied)",
        "SENTINELS_H2_H5": "parsed=false at start and end",
    },
    "r55_recommendation": "PARTIAL -> per the R55 rule: return to the "
        "queued theorems on the derived process before any further "
        "holdout - (i) the eventual-support law (which fixed finite "
        "motif sets appear a.s. vs with probability < 1 under U-growth "
        "with uniform pairing); (ii) the m >= Gamma gap; (iii) the "
        "growth rate. The UNMAPPED_COMPUTABLE observables (containment, "
        "coembedding, support/participation, concentration backbone, "
        "dilution, diameter) may be frozen target-blind for H2-H5 only "
        "after being re-derived from the process with their H1 "
        "provenance disclosed.",
}
