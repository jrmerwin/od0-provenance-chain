"""OD0-R67 adjudication data: M8 execution + branch (d). (Claude Code.)
Part A values computed independently (exact algebra; the A1
computation additionally cross-checked by an independent worker);
never copied from the frozen Bell reports."""

RUN_DATE = "2026-09-02"

PART_A = {
 "A1_CGLMP": {
  "derived_frozen": "I_3,infinity = 4/3 + 8 sqrt(3)/9 (BELL1)",
  "independent_standard": "Born rule on |psi> = (|00>+|11>+|22>)/"
    "sqrt(3) with the dictionary's two-setting Fourier family; "
    "joint law P(k,l) = sin^2(pi s)/(27 sin^2(pi s/3)), s = "
    "(k-l) + alpha - beta; exact Q(sqrt 3) evaluation at the "
    "family's maximizing phases (twelfth-grid point (-1/4, 1/4; "
    "-1/2, 0), a common-offset gauge of the textbook choice): "
    "I_3 = 4/3 + (8/9) sqrt(3) EXACTLY; maximality grid-certified "
    "(4000-point random grid <= the exact value); the identities "
    "(12 + 8 sqrt 3)/9 = 4/(6 sqrt 3 - 9) = 4/3 + 8 sqrt(3)/9 "
    "verified in Q(sqrt 3).",
  "comparison": "ALGEBRAIC EQUALITY in Q(sqrt 3)",
  "verdict": "EXACT_AGREEMENT"},
 "A2_CHSH": {
  "derived_frozen": "S_infinity = 2.5179399560, characterized by "
    "16 c^5 - 16 c^3 + 2 c^2 + 2 c - 1 = 0 (BELL1)",
  "independent_standard": "The frozen dichotomic readout extracted "
    "from the BELL1 spec ((-1, -1, +1) outcome map, cited with "
    "file+line by the worker); applied to the Born correlations of "
    "the dictionary's state and family and maximized over phases: "
    "S* = 2.517939955996527777... - agreement with the frozen "
    "value to ALL ten frozen digits. Algebraic identification: the "
    "frozen quintic is EXACTLY the independent stationarity "
    "polynomial through the substitution c = cos(2 pi phi*/3) at "
    "the optimal phase (dS/dc = -(96/27)(16 c^5 - 16 c^3 + 2 c^2 "
    "+ 2 c - 1); relevant root c* = 0.8889129786801, a root of "
    "the irreducible quartic factor 8c^4 - 4c^3 - 6c^2 + 4c - 1).",
  "comparison": "NUMERIC to all frozen digits + algebraic "
    "identification of the frozen polynomial as the optimum's "
    "stationarity equation in c. Wording precision recorded (a "
    "clarification, not a disagreement): S itself is not a root "
    "of the quintic - its own minimal polynomial is the quartic "
    "531441 S^4 - 1574640 S^3 + 624024 S^2 - 25920 S - 115568 "
    "(531441 = 27^4), unique real root > 2; the frozen phrase "
    "'the root of' reads correctly as 'the value at the "
    "stationary point characterized by'. Also S* < 2 sqrt(2), "
    "consistent with the frozen supraquantum gate.",
  "verdict": "EXACT_AGREEMENT"},
 "A3_local_bounds": {
  "derived_frozen": "I_3 <= 2 and S <= 2 (BELL1 enumerations)",
  "independent_standard": "exhaustive enumeration of all 81 "
    "deterministic assignments of the corrected standard I_3 form: "
    "maximum exactly 2; CHSH deterministic maximum exactly 2 "
    "(standard, re-verified by the A2 worker's readout).",
  "comparison": "EXACT",
  "verdict": "EXACT_AGREEMENT"},
 "A4_nonmaximal_ceiling": {
  "external_value_named": "1 + sqrt(11/3) (the known CGLMP-3 "
    "maximum over the same family attained by a non-maximally "
    "entangled two-qutrit state; named here under the sealed "
    "protocol, as pre-authorized by its quarantined citation in "
    "the frozen Bell report)",
  "derived_side": "BELL2 direct-source rigidity: the constructor's "
    "autonomous source is Schmidt-uniform (maximally entangled); "
    "the frozen ceiling theorem covers the direct source and the "
    "full-rank canonical class.",
  "verdict": "RESTRICTION - the constructor's direct source cannot "
    "reach the non-maximal ceiling; standard theory contains it "
    "with a different preparation. A claim about what the "
    "constructor prepares, not a contradiction (exactly the "
    "declared expected pattern)."},
 "A5_heralded_branch": {
  "derived_frozen": "the legal event-ready word P_{0,1} F_3 P_{0,1} "
    "prepares Schmidt squares (3/4, 1/4, 0) with success "
    "probability 4/9 (BELL2)",
  "comparison": "state existence: standard theory contains this "
    "state.",
  "verdict": "EXACT_AGREEMENT (existence)",
  "value_not_computed": "its Bell value under the native family "
    "remains open (BELL2) and is NOT computed here; recorded as "
    "the BELL3 candidate round outside the OD0 tower."},
 "non_comparisons": "Recorded verbatim from the sealed protocol: "
   "TIME / CAPACITY / GEOMETRY dictionary classes not compared "
   "(no dictionaries exist); the dark fraction 1/3 comparison "
   "FORBIDDEN until a readable-structure dictionary is "
   "preregistered against a sealed corpus.",
 "overall": "M8_BELL = PASS - A1, A2, A3 EXACT_AGREEMENT (A1 by "
   "algebraic equality in Q(sqrt 3), independently cross-checked "
   "by a second worker under the textbook phase gauge; A2 numeric "
   "to all frozen digits with the algebraic identification; A3 "
   "exact enumerations), A4 RESTRICTION exactly as declared in "
   "the sealed expected pattern, A5 EXACT_AGREEMENT (existence). "
   "NO CONTRADICTION: the quantum-side scaffold stands.",
}

PART_B = {
 "gram_sectors": {
  "S_a": "incidence frame, m = 3: invariant form on V_rot unique "
         "up to scale; rho = 1/2, spectrum {0, 3/2, 3/2} - the "
         "m = 3 simplex; NOT the target.",
  "S_b_S_c": "m = 2 pairs (typing; orientation): rho = 1 "
             "(antipodal); not the target.",
  "S_d": "the four oriented typed frames, Klein Z2 x Z2 acting "
         "regularly: the invariant forms on the regular "
         "representation carry one coefficient per nontrivial "
         "character - a 3-parameter family; equal overlaps are "
         "NOT forced; no canonical rho. Does not produce the "
         "target despite realizing m = 4 = 2p.",
  "S_e": "the m-sibling exchange sector: S_m symmetry alone forces "
         "the traceless (uniform-mode-kernel) Gram to (1 + rho) I "
         "- rho J with rho = 1/(m-1) - the invariant form family "
         "span{I, J} restricts to a single ray on the standard "
         "representation. At m = 4: rho = 1/3, rank 3, spectrum "
         "{0, 4/3, 4/3, 4/3} - ALL FOUR frozen closure-amplitude "
         "values reproduced exactly (certified). Exists iff a "
         "4-sibling event occurs: Gamma >= 5 by the frozen P4 "
         "hard ladder.",
  "S_f": "the alphabet with null: S_3 fixing bot - not transitive "
         "(orbits 3 + 1); no single canonical Gram.",
  "S_g": "no further canonical finite symmetric structure with a "
         "transitive frozen action found in CD0/CD1I/R58 (the "
         "10-marker catalog is S_3-symmetric but splits into "
         "orbits 1 + 3 + 6).",
 },
 "verdict": "CONDITIONAL_ARROW(S-e, m = 4)",
 "verdict_statement": "The closure-amplitude family's m = 4 Gram "
   "values are exactly the 4-sibling sibling-exchange sector of "
   "the frozen equality state - an arrow that exists conditional "
   "on a 4-sibling event (Gamma >= 5). The family's m = 4 is "
   "thereby explained as a CAPACITY CONDITION, not a constant of "
   "the tower: no unconditional canonical structure forces it "
   "(S-d realizes m = 4 without forcing the Gram; nothing else "
   "reaches m = 4). The 'path-count matrices' of the family's "
   "Gate 2b are NOT identified with any frozen OD0 object "
   "(NO_MAP on that sub-question stands); only the GRAM SECTOR "
   "acquires the arrow.",
 "one_thirds": {
  "alphabet": "1/3 = 1/(p + 1), p = 2 parents (the frame is two "
              "parents plus the new object) - exact.",
  "dark": "1/3 = integral_0^1 t^p dt = 1/(p + 1), p = 2 "
          "(childlessness exponent = the two-parent constant) - "
          "exact (R63 D7).",
  "alphabet_dark": "SHARED_MECHANISM (theorem): both equal "
                   "1/(p + 1) with the SAME p = 2 - the two-parent "
                   "constant of CD0. One mechanism, two theorems.",
  "simplex": "CONDITIONAL(4-sibling event): rho = 1/(m - 1) = 1/3 "
             "iff m = 4 = 2p. The only canonical structure with "
             "m = 4 AND forced equal overlaps is S-e at m = 4, "
             "which is capacity-gated (Gamma >= 5), not forced; "
             "S-d realizes m = 2p canonically (typing x sheet) "
             "but its Klein action leaves three independent "
             "overlap parameters. The simplex 1/3 is therefore "
             "NOT a third face of the p = 2 mechanism: it is "
             "conditional structure, sharing the numeral only "
             "through m = 2p at a gated event.",
 },
}

HC = [
 ["HC1", "Part A value copied; comparison outside the five items; "
  "dictionary beyond settings", "REJECTED", "A1/A3 computed from "
  "the Born rule and enumerations in-round (exact algebra); A2 by "
  "an independent worker from the extracted readout definition; "
  "A4's external value named under the sealed authorization; five "
  "items only."],
 ["HC2", "new Bell computation; BELL2 reopened", "REJECTED",
  "A5's native value left open (BELL3 recorded); only frozen "
  "verdicts cited."],
 ["HC3", "structure added to 5.1; closure-amplitude derivation "
  "imported", "REJECTED", "Inventory adjudicated verbatim; the "
  "family's values used as match targets only."],
 ["HC4", "inner product chosen where a family exists; m chosen",
  "REJECTED", "S-d and S-f adjudicated as non-canonical "
  "families/non-transitive; no selection made; m = 4 enters only "
  "as the capacity-gated condition."],
 ["HC5", "physical referent outside Part A", "REJECTED",
  "Part B is pure representation theory of frozen structures."],
 ["HC6", "H5 read; TR1' touched", "REJECTED",
  "Sentinel parsed=false; the premise round is R68."],
 ["HC7", "frozen tower modified", "REJECTED", "Nothing modified."],
 ["HC8", "hand hash; placeholder", "REJECTED",
  "All hashes in-process."],
]

VERDICTS = {
 "always": "OD0_R67_PASS_M8_COMPARISON_EXECUTED_AND_BRANCH_D_"
           "ADJUDICATED",
 "M8_BELL": "PASS (A1/A2/A3 EXACT_AGREEMENT; A4 RESTRICTION as "
            "declared; A5 existence agreement; no CONTRADICTION)",
 "BRANCH_D": "CONDITIONAL_ARROW(S-e, m = 4)",
 "ONE_THIRD": "alphabet-dark: SHARED_MECHANISM (p = 2 theorem); "
              "simplex: CONDITIONAL (4-sibling event; m = 2p "
              "unforced)",
 "prediction_vs_outcome": "Registered: A1-A3 EXACT_AGREEMENT with "
  "algebraic equality, A4 RESTRICTION, A5 existence, M8_BELL PASS "
  "- outcome exactly as registered, with two workman's notes: my "
  "in-round A1 assembly initially carried index errors that the "
  "exact machinery itself exposed (local bound 3 and a "
  "non-stationary value flagged the bug before any comparison "
  "was made; corrected and then independently confirmed under "
  "the textbook gauge), and the frozen A2 phrasing 'root of the "
  "quintic' is precisified (the quintic is the optimum's "
  "stationarity polynomial in c = cos(2 pi phi/3); S's own "
  "minimal polynomial is the 27^4 quartic). Registered Part B: "
  "CONDITIONAL_ARROW(S-e, m = 4), S-a rho = 1/2, S-d not "
  "forcing, S-f not transitive, no S-g - all exactly as "
  "registered; the three 1/3s adjudicated as registered "
  "(alphabet-dark SHARED_MECHANISM; simplex CONDITIONAL). The "
  "prediction constrained nothing.",
 "r68_recommendation": "R68 is the TR1' premise round (per the R66 "
  "rule): preregister the total parameter-free token-region "
  "premise with its inert alternative, the regional throttled "
  "process, and the lapse and density fields (R66 R2-R3 as "
  "targets) by the TG1 template; the pairing no-go is unaffected. "
  "The amplitude-space geometry (the rank-3 Euclidean sector of "
  "the 4-sibling exchange) is recorded as a second, conditional "
  "geometry candidate alongside G1; its relation to the record-"
  "space 3-adic geometry is queued after R68. H5's derived side "
  "follows from the density field.",
}
