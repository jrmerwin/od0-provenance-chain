"""OD0-R56 adjudication data: alphabet audit, M5 classification, P4,
recurrence. (Claude Code executor.)"""

RUN_DATE = "2026-09-02"

ALPHABET_AUDIT = {
    "record_event_typing_in_frozen_source": {
        "single_use": "Q1-typed histories, c_first in 11..13 (R52 Part "
                      "1.4 frozen range)",
        "same_step_sibling_pairs": "Q2-typed sibling-shared histories, "
                                   "c_first in 22..26 (R52); the "
                                   "within-step sibling correlation of "
                                   "the R52 cluster theorem",
        "sibling_groups_ge_3": "NOT separately typed in any frozen "
                               "source; they arise only for Gamma >= 4 "
                               "(group size <= Gamma - 1, R52)",
    },
    "what_r50_r55_actually_did": "Every engine costed every record at the "
        "uniform Q1-minimum lower-bound load (11 per newly recorded "
        "prefix, 2 per repeat), declared in advance at the R50/R51 Commit "
        "A locks; Q2 typing was never applied and sibling groups of any "
        "size were costed as independent records. This is a coarser "
        "convention than pairwise reduction and was recorded as a "
        "lower-bound convention throughout.",
    "classification": "PAIRWISE_REDUCTION_CONVENTION (scoped Gamma <= 3) "
        "- the nearest frozen class, with the exact description above "
        "recorded verbatim; NOT AD_HOC (declared in advance, direction-"
        "consistent) and NOT FROZEN_ALPHABET_COVERS (>= 3 groups have no "
        "frozen typing)",
    "impact": {
        "theorems": "UNAFFECTED - every R52-R55 theorem uses cost LOWER "
                    "bounds (c >= 11*paths_to), which the convention "
                    "under-approximates consistently: phi, the cost-"
                    "budget identity, the k/loglog k bound, and the "
                    "termination statements all survive verbatim",
        "readouts": "ALL sampled readouts (R50-R55, every Gamma) are "
                    "lower-bound-load readouts - already labeled as such "
                    "at their Commit A locks; at Gamma >= 4 they "
                    "additionally omit any >= 3-group typing surcharge - "
                    "flagged",
        "scope": "exact label-EMISSION statements are scoped to Gamma <= "
                 "3 (sibling groups <= 2, covered by the frozen Q1/Q2 "
                 "alphabet) until an m-sibling alphabet is derived from "
                 "the incidence structure - the recorded gap for R57+",
    },
}

CLASSIFICATION = {
    "universal_floor": "Every record event is fired by an adjunction, "
        "which requires 2 co-served tokens (TG1); hence Gamma_min >= 2 "
        "for every label - and E0 (where nothing fires distinctions "
        "under congestion-free service) emits nothing beyond the first "
        "pair.",
    "classes": [
        {"class": "REPEAT_USE labels (query token, temporal provenance "
                  "edge)",
         "minimal_configuration": "2 co-served tokens forming one "
                                  "adjunction whose composite cone is "
                                  "fully recorded",
         "Gamma_min": 2,
         "state_condition": "both parents exist; every composite in the "
                            "union of their ancestry cones is recorded "
                            "(used before)",
         "emission": "repeat use only"},
        {"class": "SINGLE_FIRST_USE labels (Q1-typed unresolved-cell "
                  "content)",
         "minimal_configuration": "2 co-served tokens; the used composite "
                                  "parent (or a cone member) is in the "
                                  "shell (unrecorded)",
         "Gamma_min": 2,
         "state_condition": "a shell composite in the fired event's "
                            "ancestry cone",
         "emission": "first use only"},
        {"class": "SIBLING_PAIR labels (Q2-typed sibling-shared "
                  "histories; the two-factor 356 catalog's correlated "
                  "content)",
         "minimal_configuration": "3 co-served tokens sharing one parent: "
                                  "events {u,v1}, {u,v2} in one step "
                                  "record the same prefix",
         "Gamma_min": 3,
         "state_condition": "u and two partners co-served; both pairs "
                            "absent",
         "emission": "first use (correlated pair); repeats also possible"},
        {"class": "SIBLING_GROUP >= 3 (m-sibling content, m >= 3)",
         "minimal_configuration": "m+1 co-served tokens sharing one "
                                  "parent",
         "Gamma_min": "m+1 >= 4",
         "state_condition": "scoped - no frozen typing (alphabet audit)",
         "emission": "SCOPED to the m-sibling alphabet derivation"},
    ],
    "per_label_note": "The 356 catalog labels split between the Q1-typed "
        "and Q2-typed classes per the frozen R47/R52 typing; per-label "
        "enumeration requires the registered instrument instance and is "
        "recorded at type-class level here (the class-level Gamma_min "
        "histogram is exact; the instance-level split is carried by the "
        "frozen catalog).",
    "P4": {
        "verdict": "PROVEN",
        "proof": "The service realization draws n = min(Gamma, F+D) <= "
                 "Gamma tokens, so at most Gamma tokens are co-served in "
                 "any step - a HARD bound, not probabilistic. A "
                 "configuration requiring k co-served tokens is therefore "
                 "impossible at Gamma < k, possible (and by Lemma-1 "
                 "positivity, eventually realized with positive "
                 "probability) at Gamma >= k. Families ordered by minimal "
                 "configuration become reachable exactly in that order as "
                 "capacity rises; at fixed Gamma, families above the "
                 "threshold never appear. Engine confirmation: "
                 "SIBLING_GROUP_GE3 never occurs at Gamma <= 3 in any "
                 "exact evolution or sampled trajectory.",
    },
}

RECURRENCE = {
    "theorem": "For m < Gamma (U-growth): every object w is reused as a "
               "parent infinitely often, almost surely.",
    "proof": "Given a burst at universe size D_b, the formed pair is "
             "drawn from the served subset (uniform); P(w in a formed "
             "pair | burst) >= c(Gamma)/D_b for an explicit positive "
             "c(Gamma) once D_b exceeds w's formed-pair saturation "
             "(children(w) < D_b - 1, true forever since children grow "
             "at most Gamma-1 per step and D grows too). D_b <= D_tau + "
             "C(Gamma,2)*b, so the conditional probabilities sum as a "
             "harmonic series over bursts: sum_b c/D_b = infinity. "
             "U-growth gives infinitely many bursts a.s. (R53); Levy's "
             "conditional Borel-Cantelli (divergence half) gives reuse "
             "infinitely often a.s.",
    "chain_law": "Under CCP1_EXACT_SPARSE the carrier chain of a "
                 "repeat-use label is its sequence of actual appearances "
                 "(no absent-rank stage, R47). PROVEN: chains are "
                 "unbounded a.s.; E[chain length after N bursts] = "
                 "Theta(log N) (two-sided: sum of c/D_b ~ harmonic gives "
                 "both bounds with explicit constants c(Gamma)/C(Gamma,2) "
                 "and Gamma). Recurrence is logarithmically sparse in "
                 "burst count - exactly the registered target's form, "
                 "proven in expectation with a.s. unboundedness.",
    "first_use_chains": "For a fixed first-use label, appearances count "
                        "distinct emitting objects first-used; growth is "
                        "bounded by the realized-support law (R55 phi): "
                        "first-use chains freeze randomly with the "
                        "support.",
    "cce4": "No particle promotion: labels remain exact semantic A12 "
            "objects throughout (CCE4); nothing here is a species.",
}

HOSTILE_CONTROLS = [
    ["HC1", "additions to Sections 4-6 after Commit A", "REJECTED",
     "R56_H2_PREREGISTRATION.json is byte-identical to its Commit-A "
     "seal; the adjudication references it read-only."],
    ["HC2", "H2 content read; sentinels not false", "REJECTED",
     "The H2 PDF hash re-verified untouched at lock time; sentinels "
     "parsed=false at start and end."],
    ["HC3", "rate or round-number statement in prereg/protocol",
     "REJECTED", "Excluded by construction; the protocol compares only "
     "reparametrization-invariant shapes."],
    ["HC4", ">=3-sibling convention presented as frozen source",
     "REJECTED", "The 7.1 audit classifies it PAIRWISE_REDUCTION_"
     "CONVENTION with the exact engine behavior recorded; label-emission "
     "statements scoped to Gamma <= 3."],
    ["HC5", "label promoted to particle/species/channel", "REJECTED",
     "CCE4 restated; no species language anywhere."],
    ["HC6", "H1 used beyond disclosed provenance", "REJECTED",
     "Only definitional provenance disclosure; no H1 values used."],
    ["HC7", "TG1/cost law/filtration/frozen roots modified; BELL2",
     "REJECTED", "Nothing modified; worktree clean; BELL2 unopened."],
    ["HC8", "hand hash; placeholder", "REJECTED",
     "All hashes in-process; stamp commit closes the round."],
]

VERDICTS = {
    "always": "OD0_R56_PASS_H2_PREREGISTERED_AND_M5_OPENED",
    "components": {
        "ALPHABET_SCOPE": "PAIRWISE_CONVENTION(scoped Gamma <= 3); "
                          "theorems unaffected (lower-bound costing); "
                          "readouts flagged; m-sibling alphabet = "
                          "recorded gap",
        "P4_CONFIGURATION_ORDERING": "PROVEN (hard capacity bound "
                                     "n <= Gamma)",
        "RECURRENCE": "PROVEN (harmonic reuse law; chains unbounded "
                      "a.s.; Theta(log N) expected length; "
                      "logarithmically sparse)",
        "REACHABLE_LABELS_BY_GAMMA": "repeat-use and single-first-use "
                                     "classes at Gamma >= 2; "
                                     "sibling-pair class at Gamma >= 3; "
                                     ">= 3-groups only at Gamma >= 4 "
                                     "(scoped); engine counts in "
                                     "certificates",
    },
    "prediction_vs_outcome": "Confirmed on every point: the audit found "
        "the >= 3-group costing to be a declared lower-bound convention "
        "(classified PAIRWISE_REDUCTION_CONVENTION, scoped Gamma <= 3), "
        "with R52-R55 theorems unaffected and readouts flagged; labels "
        "split single-use Gamma_min=2 / sibling-pair Gamma_min=3, "
        "repeat-use reachable at Gamma=2; P4 proven; recurrence proven "
        "in the predicted harmonic/logarithmic form. One sharpening: the "
        "engines' actual convention is uniform-Q1-minimum, coarser than "
        "pairwise reduction - recorded verbatim. The prediction "
        "constrained nothing.",
    "r57_recommendation": "ALPHABET_SCOPE scoped cleanly and P4 PROVEN, "
        "so per the R57 rule: open H2 under the sealed protocol "
        "(R56_H2_PREREGISTRATION.json, hash-pinned) - one comparison, no "
        "repair, mirroring R54: verify the Run3_Dijet hash, extract "
        "definitions, map by definition, adjudicate PASS/PARTIAL/FAIL "
        "with the model-family caveat. Content at Gamma >= 4 label "
        "granularity is outside the sealed comparison (scoped); the "
        "random-DAG cost problem stays queued unless H2 makes it the "
        "immediate dependency.",
}
