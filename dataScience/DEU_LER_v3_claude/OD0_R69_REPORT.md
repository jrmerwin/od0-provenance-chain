# OD0-R69 Report: The H5 Preregistration

Run date: 2026-09-02. Verdict: **OD0_R69_PASS_H5_PREREGISTERED**.

## Position
R68 stamp pinned and verified. Sections 4-5 frozen verbatim at
Commit A. H5 sentinel parsed=false at start and end; pinning touched
byte hashes and filenames only.

## The derived-side table (frozen)
[
 {
  "id": "Q1",
  "statement": "Record density rho_rec(d) = N_{>=d}/3^d per cylinder at depth d; uniform across cylinders at each depth in expectation; NONDECREASING in maturity at every cylinder (records are never erased); decreasing across depths.",
  "class": "THEOREM (uniformity certified R68)",
  "conditionality": "tower (CO1, RO1, TG1, V ~ X); not TD1-dependent",
  "invariant": true,
  "fixture_specific": false
 },
 {
  "id": "Q2",
  "statement": "Critical density: a cylinder at depth d leaves the free regime when F_rho + D_rho > Gamma - its record density reaches rho_crit(d) = Gamma 3^d per unit measure (exact form through the charge-share theorem's shares).",
  "class": "THEOREM under TD1 + FIXED_MAP",
  "conditionality": "tower + TD1",
  "invariant": true,
  "fixture_specific": "only through k and the share family"
 },
 {
  "id": "Q3",
  "statement": "Boundary motion: d*(N) = log_3(N/Gamma); the congested set is a growing ball-complement in the record tree; increases logarithmically in N.",
  "class": "THEOREM (general-depth law)",
  "conditionality": "tower + TD1",
  "invariant": "as ordering and monotonicity; the rate is comparable only against internal counts, never rounds",
  "fixture_specific": false
 },
 {
  "id": "Q4",
  "statement": "Two-phase lapse field: early - lapse ordered by depth (deeper freer); mature - the nine non-root regions congest simultaneously at N = 9 Gamma and equalize by S_3 symmetry; the root never congests (Phi = 1, full tick rate, forever).",
  "class": "THEOREM under TD1 + the ten-marker fixture",
  "conditionality": "tower + TD1 + fixture",
  "invariant": true,
  "fixture_specific": "the free-root and equalization clauses; the early ordering is general"
 },
 {
  "id": "Q5",
  "statement": "Early/late density ratios: per cylinder >= 1 (THEOREM, from Q1 monotonicity), exact law from Q1; cross-depth ratios at fixed N from Q1. Specific numeric ratios compared only under state-class match.",
  "class": "THEOREM (direction); ratios gated by state class",
  "conditionality": "tower + TD1",
  "invariant": true,
  "fixture_specific": false
 },
 {
  "id": "Q6",
  "statement": "Tick-rate field: Gamma_rho Phi^2_rho per region; the root's tick rate maximal and constant at maturity; the nine cells' rates equal and decreasing with load.",
  "class": "THEOREM under TD1 + fixture",
  "conditionality": "tower + TD1 + fixture",
  "invariant": true,
  "fixture_specific": true
 },
 {
  "id": "Q7",
  "statement": "Per-region duality: each region's clock characters are the points of its own cylinder (a ball in Z_3).",
  "class": "THEOREM",
  "conditionality": "tower",
  "invariant": "internal only - NOT compared",
  "fixture_specific": false
 },
 {
  "id": "Q8",
  "statement": "Dark fraction E|U|/n -> 1/3.",
  "class": "THEOREM",
  "conditionality": "tower",
  "invariant": true,
  "fixture_specific": false,
  "NOT_COMPARED": "the R66 seal forbids comparison until a readable-structure dictionary is preregistered against a sealed corpus; H5's side is sealed, so no dictionary can exist yet; the prohibition stands through R70. Recorded here so the temptation cannot be reached for at opening."
 }
]

## The sealed protocol
sha256 = 160775e68feaecbcaa081a77e96ba8640def57d14693a3d6fb69fc2767d26c94


 "compared": "Reparametrization-invariant reported patterns - existence and direction of a density that changes with maturity; existence of a critical density or closure condition and whether it is finite-count or asymptotic; equalization or persistence of differences across regions or sectors; a distinguished region or sector that does not participate; ordering of sectors by depth or specificity; early-versus-late ratios as DIRECTIONS - against Q1-Q7, mapped BY DEFINITION at opening. Names, words, counts are not maps.",
 "rule": "PASS iff every mapped reparametrization-invariant pattern is consistent with the corresponding THEOREM-grade statement and none contradicts one; PARTIAL if consistent but a stage-defining H5 observable is unmapped, matches only at BOUND/READOUT/CONJECTURE grade, or is STATE_CLASS_MISMATCH; FAIL if a THEOREM-grade statement is contradicted by a reparametrization-invariant pattern under state-class match. Mismatches at equal prominence.",
 "excluded": "Tier D quantities; rates versus rounds; the dark fraction (Q8); any quantitative ratio without an exact state-class arrow; any mapping of rho_crit, 'closure', or 'density' by NAME.",
 "pre_committed_classifications": "Any reported closure or critical condition is classified FINITE_COUNT or ASYMPTOTIC by definition BEFORE adjudication; any reported open-to-mature factor is classified by the state it is computed on and by calibration-vs-internal-ratio status.",
 "pre_committed_FAIL_diagnoses": [
  "(i) A reported DECREASE of density with maturity contradicts Q1 (THEOREM); the diagnosis path is whether the H5 substrate has a destruction mechanism (record or structure removal), stated in the caveat, with nothing softening the verdict.",
  "(ii) A reported congestion of the distinguished region, or the absence of a distinguished free region, is compared only if H5's region structure maps to the ten-marker fixture by definition; otherwise STATE_CLASS_MISMATCH.",
  "(iii) A reported ASYMPTOTIC closure is not compared with the finite-count N = 9 Gamma result; recorded."
 ],
 "forbidden": "Round-number alignment; any statement added, criterion moved, observable renamed, or tower repaired in the opening round.",
 "model_family_caveat": "MANDATORY at opening: the projection family's derivation chain for each H5 artifact (state field / derived observable / external calibration / phenomenological projection / fixed bridge assumption / manuscript-only), from the R48 F5 classification and the pinned sources; the state class of each pattern.",
 "state_class_rule": "R62 verbatim: quantitative comparisons only under an exact arrow from the historical state class to the derived state (random ideal under TD1); otherwise STATE_CLASS_MISMATCH - neither contradiction nor confirmation.",
 "execution": "R70, one round, no repair - the LAST sealed corpus."


## Artifacts
H5: 14/14 pinned unchanged; 6 non-manuscript artifacts (the corpus
is not PAPER_ONLY); the de Sitter-closure computation artifact is
STILL MISSING (zero filename matches) - that family is
manuscript-only, carried at equal prominence.

## Prediction vs outcome
Registered: sealed with Q1-Q7 comparable and Q8 forbidden; artifacts pinned with the de Sitter-closure computation still missing - outcome exactly as registered (14/14 pinned unchanged; the closure-computation family manuscript-only). The R70 outcome prediction (PARTIAL with the enumerated pattern) is registered in the package and carried to the opening round; it constrains nothing.

## Hostile controls
All 8 REJECTED (see OD0_R69_RESULTS.json).

## R70
Open H5 under the sealed protocol - one comparison, no repair, mirroring R54/R57/R62: hash verification before reading; extraction with state-class tags and the pre-committed classifications; mapping by definition; adjudication; mandatory caveat; quarantined post-opening readout permitted (no future holdout remains - its only use is the record). After R70 every sealed corpus is spent; next is the maturation-and-geometry proto-paper (R48-R70), then the queued theorems: the two geometry candidates' relation, the relief critical line, BELL3, and the Tier D dictionary problem - the true bridge, open, to be stated as such.
