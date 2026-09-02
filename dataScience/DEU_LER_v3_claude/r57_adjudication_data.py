"""OD0-R57 adjudication data: H2 extraction, mapping, sealed-rule verdict."""

RUN_DATE = "2026-09-02"

EXTRACTION = {
    "artifact": "Run3_Dijet (2).pdf, 8 pages, sha 16e9cfcd... (verified "
                "pre-opening); 'Pre-Registered Structural Predictions for "
                "LHC Run-3 Dijet Angular Distributions from a Discrete "
                "Emergent Universe Model' (July 2026)",
    "repo_pin": {
        "reference_verbatim": "https://github.com/jrmerwin/deu-run3, tags "
            "run3-protocol-v1 and run3-values-v1; Zenodo "
            "10.5281/zenodo.21464119 (locked predictions, checksums, "
            "ladder records) and 10.5281/zenodo.21464816 (state pickles, "
            "oversize enumeration tables); STATE_SHA256SUMS hash-lock",
        "status": "EXTERNAL - recorded verbatim, not fetched this round; "
                  "local raw backing = the R48-census-pinned Stage-K "
                  "artifacts (RMR_DEU/hadron_hunting: "
                  "stagek_k3_collision_toolkit_v0_4.py, "
                  "stagek_k7_k11_dijet_and_debris_v0_1.py, "
                  "deu_stageK_outputs incl. K11D3) - the engine and "
                  "campaign drivers the paper certifies against",
        "raw_backed_locally": "K3 engine source; K7-K11 drivers; StageK "
                              "output archives",
        "paper_only_locally": "run3 scaffold, frozen packet, prediction "
                              "card, ladder records (external repo/Zenodo)",
    },
    "engine_and_substrate": {
        "engine": "K3 v0.4 deterministic activation-foam engine; "
                  "collisions = driven contact cascades ('funnels') "
                  "between zero-anchor frontier structures, followed by "
                  "fracture into debris",
        "opportunity_law_verbatim": "engine rounds are 'the iterative "
            "ticks of the model's bandwidth scheduler' (paper Sec 8); "
            "contact/fracture eligibility computed from live "
            "shell-component adjacency (R48 census, Stage-K record); "
            "collision drives are EXTERNAL interventions on the substrate",
        "substrate": "archived foam lineage state at round 1,910,001 "
                     "('mature anchor'); single substrate for all scored "
                     "predictions; epoch analysis single-seed",
        "destruction_mechanism": "PRESENT IN THE COLLISION DRIVER ONLY "
            "(fracture into debris under driven cascades); NO "
            "substrate-aging removal is reported; age-axis availability "
            "is reported as growing (robust in aggregate)",
    },
    "stage_sequence_verbatim_age_axis": [
        "primordial composite-only era (no two-frontier family exists "
        "under any filter while composite families do)",
        "emergence of two-frontier channels (robust under every filter)",
        "growth of channel availability by three orders of magnitude",
        "mature substrate / modern epoch (the archived mature anchor; "
        "strain relaxed toward the anchor value)",
    ],
    "energy_axis_patterns": [
        "two-frontier family availability collapses monotonically with "
        "tier (290 -> ... -> 0)",
        "simultaneous extinction: concentrated channels vanish and peak "
        "completion fails together",
        "forbidden gap (no capacity combination sums to the target) and "
        "an isolated terminal line (the maximum attainable capacity sum)",
    ],
    "definitions": {
        "family": "a capacity decomposition of the collision target N0 "
                  "into frontier components from the candidate bank "
                  "(exact-capacity enumeration); 'two-frontier family' = "
                  "decomposition into exactly two frontier structures",
        "channel": "a driveable family (routing for a collision)",
        "composite_only": "no two-frontier family exists; collisions "
                          "route only through composite (multi-component) "
                          "decompositions",
        "filter_band": "six candidate-selection predicates spanning the "
                       "reconstruction uncertainty (the original filter "
                       "is UNDERIVED - the paper's own open gap, Sec 9.2)",
        "strain": "bridge chi per contact of the funnel drive (a "
                  "geometric foam-drive quantity)",
        "channel_availability": "count of two-frontier families at fixed "
                                "N0 on the substrate at a given age",
        "mature_anchor": "the archived substrate state; chi median 1.890 "
                         "at E30",
    },
    "pattern_classification": {
        "orderings": ["composite-only -> two-frontier emergence (robust "
                      "under all filters)"],
        "monotonicities": ["channel availability grows with age (robust "
                           "in aggregate; strict monotonicity "
                           "filter-sensitive - a 2M->4M dip appears only "
                           "under edge-thresholded filters and is "
                           "flagged by the paper as instrument "
                           "uncertainty)",
                           "strain relaxes with age toward the mature "
                           "anchor (regime-level at emergence: "
                           "family-sensitive)"],
        "freeze_saturation": ["none reported on the age axis"],
        "capacity_complexity": ["availability collapse with energy tier; "
                                "simultaneous extinction; forbidden gap "
                                "+ terminal line (hard capacity-sum "
                                "unreachability)"],
        "cross_substrate": ["N/A - single substrate, single-seed"],
        "rate_age_excluded": ["all engine-round counts (2.5e5, 5e5, 8e6, "
                              "1,910,001), 'three orders of magnitude' "
                              "as a rate, all TeV mappings and the "
                              "energy dictionary - recorded as "
                              "historical values, EXCLUDED from "
                              "comparison; the paper itself disclaims "
                              "linear calibration of rounds to physical "
                              "epochs"],
    },
}

MAP_TABLE = [
    {"h2": "channel availability (count of two-frontier families over "
           "realized components)",
     "derived": "UNMAPPED_COMPUTABLE - a pair-count over realized objects "
                "with a capacity predicate is well-defined on z+ but is "
                "not one of the nine frozen observables (O3 counts "
                "members of a fixed set, not configurations)",
     "status": "UNMAPPED_COMPUTABLE"},
    {"h2": "two-frontier (exactly-2-component capacity decomposition)",
     "derived": "P4-question adjudicated BY DEFINITION: this is an "
                "assembly configuration over the candidate bank, NOT a "
                "co-served-token count of a record event - a different "
                "function on a different domain; the P4 mapping is "
                "DECLINED (no name-resonance mapping). The ordering "
                "content is carried instead at pattern-class level by "
                "P3/P6 (small/cheap structures realized before "
                "large/complex ones).",
     "status": "UNMAPPED_COMPUTABLE (configuration-count analog)"},
    {"h2": "composite-only era",
     "derived": "as above - the small-component-routes-only regime; "
                "pattern-class counterpart P3/P6 (availability of small "
                "structures precedes large)",
     "status": "UNMAPPED_COMPUTABLE (analog)"},
    {"h2": "strain (bridge chi per contact)",
     "derived": "UNMAPPED_INAPPLICABLE - a funnel/bridge geometric "
                "quantity of the foam drive; the foam family has no "
                "exact arrow into z+ (R48 NO_MAP); not a load ratio by "
                "definition",
     "status": "UNMAPPED_INAPPLICABLE"},
    {"h2": "candidate filter band",
     "derived": "UNMAPPED_INAPPLICABLE - an instrument-reconstruction "
                "convention over foam component properties",
     "status": "UNMAPPED_INAPPLICABLE"},
    {"h2": "mature anchor",
     "derived": "a state designation, not an observable; no mapping "
                "required",
     "status": "N/A"},
    {"h2": "availability growth with age (pattern class: nondecreasing "
           "availability of realized configurations)",
     "derived": "consistent with P1 (THEOREM: realized structures "
                "persist, so configuration counts over persistent "
                "components are nondecreasing) - the pattern CLASS "
                "matches a theorem-grade prediction; the specific "
                "counting function remains unmapped",
     "status": "PATTERN_CONSISTENT_P1"},
    {"h2": "composite-only -> two-frontier ordering",
     "derived": "consistent with P3 (freeze/availability order; THEOREM "
                "bound, READOUT order) and P6 (cost-ordered persistence; "
                "READOUT order) at pattern-class level",
     "status": "PATTERN_CONSISTENT_P3_P6_READOUT"},
    {"h2": "energy-axis collapse / forbidden gap / terminal line",
     "derived": "capacity/complexity dependence: hard capacity-sum "
                "unreachability over a fixed bank - the same pattern "
                "CLASS as P4's hard service-capacity bound (forbidden "
                "configurations above capacity), and P2-consistent "
                "(larger demands, fewer realizations); functions differ "
                "by definition; no contradiction",
     "status": "PATTERN_CONSISTENT_P2_P4_CLASS"},
    {"h2": "strain relaxation with age",
     "derived": "no frozen counterpart (strain inapplicable); recorded, "
                "not compared",
     "status": "NOT_COMPARED"},
]

ADJUDICATION = {
    "ordering_test": "The single age-axis ordering (composite-only -> "
        "two-frontier) is consistent with P3/P6 at READOUT grade "
        "(pattern-class placement; the P4 definitional mapping is "
        "declined, not contradicted). No reported ordering contradicts "
        "any THEOREM-grade prediction.",
    "monotonicity_test": "Availability-with-age is nondecreasing in the "
        "paper's robust aggregate - consistent with P1 (THEOREM) at "
        "pattern-class level. The filter-sensitive 2M->4M dip is flagged "
        "by the source itself as inside instrument uncertainty and is "
        "therefore not an established reparametrization-invariant "
        "pattern; recorded at equal prominence, contradicting nothing.",
    "freeze_test": "No age-axis saturation/locking reported; N/A.",
    "capacity_complexity_test": "The energy-axis collapse, simultaneous "
        "extinction, and forbidden-gap/terminal-line structure are "
        "capacity-dependence patterns consistent at pattern-class level "
        "with P2/P4's hard-threshold shape; the discrete forbidden gap "
        "is the H2 engine's own expression of a hard capacity spectrum. "
        "No contradiction.",
    "cross_substrate_test": "N/A (single substrate, single seed) - P5 "
        "untestable, as the registered prediction anticipated.",
    "excluded": "every engine-round count, the energy dictionary, and "
        "all growth-rate magnitudes - listed in the extraction and "
        "excluded; the paper's own refusal to calibrate rounds to "
        "physical time is noted as convergent with the protocol's "
        "reparametrization rule",
    "verdict": "PARTIAL",
    "verdict_reason": "Per the sealed rule: every mapped, "
        "reparametrization-invariant H2 pattern is consistent with the "
        "corresponding predictions and none contradicts a THEOREM-grade "
        "prediction - but the stage-defining H2 observables (channel "
        "availability, two-frontier/composite-only configuration counts) "
        "are UNMAPPED_COMPUTABLE, strain and the filter band are "
        "UNMAPPED_INAPPLICABLE, and the ordering matches only at "
        "READOUT/pattern-class grade. 'PARTIAL if consistent but a "
        "stage-defining H2 observable is unmapped or matches only at "
        "READOUT grade.' The registered prediction (PARTIAL, with "
        "exactly this decomposition) is CONFIRMED on every point, "
        "including the declined P4 name-mapping and the P5 N/A.",
    "p1_fail_path": "NOT INVOKED - no availability-decreasing-with-age "
        "pattern exists at established grade; the substrate has no "
        "aging-removal mechanism (fracture is collision-driven only).",
    "model_family_caveat": "The H2 engine (K3 v0.4) is a deterministic "
        "activation-foam with bandwidth-scheduler rounds and externally "
        "driven collision cascades - neither T_sat nor TG1; it belongs "
        "to the R48 collision-substrate family F4 with NO_MAP into the "
        "active chain. Its 'families' are assembly configurations over a "
        "candidate bank, not record-event configurations. Every "
        "unmapped item and every pattern-class-only match may reflect "
        "this model-family difference rather than the constructor. The "
        "caveat does not soften the verdict.",
}

HOSTILE_CONTROLS = [
    ["HC1", "sealed prereg altered; derived-side additions", "REJECTED",
     "Preregistration verified byte-unchanged at Commit A; the "
     "adjudication uses only its items; the quarantined analog was NOT "
     "added to the derived side."],
    ["HC2", "round alignment; rate comparison", "REJECTED",
     "All round counts and rates recorded and excluded; no alignment "
     "anywhere."],
    ["HC3", "mapping by name/word/count", "REJECTED",
     "The tempting 'two-frontier ~ two co-served tokens' name-map was "
     "explicitly DECLINED by definition; all matches are "
     "pattern-class-level and labeled."],
    ["HC4", "H3-H5 read; H1 consulted", "REJECTED",
     "Sentinels parsed=false at start and end; H1 not consulted (its "
     "definitions were not needed)."],
    ["HC5", "Part 4 in the verdict", "REJECTED",
     "The quarantined analog lives in its own file; the adjudication "
     "text references none of its values."],
    ["HC6", "TG1/cost law/filtration/alphabet/frozen roots modified",
     "REJECTED", "Nothing modified; worktree clean."],
    ["HC7", "BELL2 opened", "REJECTED", "Unopened."],
    ["HC8", "hand hash; placeholder", "REJECTED",
     "All hashes in-process; stamp closes the round."],
]

VERDICTS = {
    "always": "OD0_R57_PASS_H2_OPENED_UNDER_SEALED_PROTOCOL",
    "primary": "H2_COMPARISON = PARTIAL",
    "secondary": {
        "MAP_TABLE": "mapped(pattern-class): 3, unmapped_computable: 3, "
                     "unmapped_inapplicable: 2, n/a: 2",
        "RAW_BACKING": "engine + campaign drivers + StageK archives "
                       "locally pinned (R48); run3 scaffold external "
                       "(GitHub/Zenodo, recorded verbatim, not fetched)",
        "H2_ENGINE_LAW": "bandwidth-scheduler ticks + externally driven "
                         "contact cascades (verbatim references recorded)",
        "DESTRUCTION_MECHANISM": "collision-driven fracture only; no "
                                 "substrate-aging removal",
        "SENTINELS_H3_H5": "parsed=false",
    },
    "r58_recommendation": "PARTIAL, so per the R58 rule: derive the "
        "m-sibling alphabet from the incidence structure (the "
        "m-descendant equality composite, its record algebra, A11R "
        "histories, and A12 counts, extending BELL0/R19 from two factors "
        "to m), closing the R56 scoping gap; R59 then takes the "
        "random-DAG cost theorem. H2 is spent after this round.",
}
