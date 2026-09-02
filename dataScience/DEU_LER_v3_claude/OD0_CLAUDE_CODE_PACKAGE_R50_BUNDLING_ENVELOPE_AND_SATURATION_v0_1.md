# OD0-R50 CLAUDE CODE PACKAGE v0.1

## Bundling-Invariant Envelope over {T_sat, T_dag}, Synchronous-Family Saturation Readout, and Capacity / Genesis-Ledger Source Status

### Position

R49 is frozen: commits `4946e4e` (A) / `2feccb7` (B), output manifest `53002a42f0a253b8d05f32cac196e3fa3d3dee7ab5ecd99925066e223a33486a`. Verdict `OPP_NONUNIQUE_CANONICAL`. Record law RO-D unique given RO1 (maximal-supported-scope prefix; setting forced by the lineage's A13R clock state). SV-pool unique (interleaving refuted by the 2/3-vs-1/2 witness). Adjunction law: T_sat and T_dag both canonical, distinct (4-object witnesses, divergence at k = 3). Λ₀ undeclared in source. Two-to-many shared-ancestor cluster generalization: gap stated. R48 hash erratum recorded forward in R49_INPUT_LOCK.json; R48 unchanged.

### Adjudication notes to carry into R50

1. **Family identification.** T_sat is the depth filtration of the universal DAG (prove in Part 1: under full saturation, formation step = nesting depth); T_dag is the dag_size filtration. The two-member family is exactly {depth-graded, dag_size-graded} saturating transitions. Both step quotients are local (the step of y is a canonical function of y alone).
2. **Registry arrow.** T_dag⁵(genesis) has 173 objects with a 137-object grade-5 shell. If its object set equals the CD0 registered DAG-7 / 137-registry object set exactly, record an exact *object-set* arrow from the historical registry family into the constructor family (dynamics not identified). Verify in Part 5.
3. **Erratum policy.** Frozen rounds are never rewritten; errata are recorded forward. Hash hygiene rule added below.

---

# 0. Governing question

What structure of the global process is invariant under the step quotient, what is the exact quotient-sensitive residue, and is either canonical member non-degenerate under the frozen ledger — does any developmental regime exist in the synchronous family, or does the forced pool saturate every source-admissible capacity within k ≤ K_max?

Zero-premise round. CO1, RO1, SV-pool are carried as declared conditionals; nothing new is introduced. No member of {T_sat, T_dag} is selected. No throttle, capacity law, physical time, or maturity threshold is selected.

---

# 1. Locks (minimal)

Pin R49 output manifest hash and commits (R48/R47 transitively). Clean worktree at start and end. `BELL2_opened = false`. Historical numerical content never parsed. Exact arithmetic only.

**Hash hygiene (new, permanent):** no hash is typed, expanded, or reconstructed by hand. Every commit hash is copied verbatim from `git rev-parse` output and every file hash from `sha256sum` output, at the moment of recording. Short hashes are recorded as short; full hashes only when produced by the tool.

# 2. Commits

Commit A: this package verbatim; lock verification; the frozen candidate lists of Sections 4.2 and 6.3 recorded before any readout. Commit B: everything else.

---

# 3. Frozen inputs

CD0 (constructor, Thm 1); CD1I (append, prefix records, clock tower); CD2R (A12 additivity, finite-set ledger representation, service-equivalence premise, hypergeometric kernel, population/relief rules); A13R (scale-natural clock action); UEQ0 (master transition, ledger updates, lapse); R40–R45 (service composition, RRP1 marks, interval, currents); R49 (RO-D record law with its D ≤ 3 certificates; SV-pool; the T_sat/T_dag classification and witnesses).

---

# 4. Part 1 — Bundling-invariant envelope (theorem)

## 4.1 Definitions

A **step quotient** is a surjection q from the universal event set (all composites) onto ℕ that is ancestry-compatible: q(parent) < q(child). A **graded quotient** is q = g for a canonical grading g. T_sat and T_dag are the graded quotients for g = depth and g = dag_size (prove both identities exactly; give the smallest object where depth ≠ dag_size).

## 4.2 Frozen layer list

Classify each layer as `INVARIANT_ALL_QUOTIENTS`, `INVARIANT_CANONICAL_PAIR`, or `QUOTIENT_DEPENDENT` (with the first exact divergence witness):

1. **Object layer** — the universal DAG and its ancestry order.
2. **Record poset** — the set of RO-D record events (downstream use → recorded prefix) with induced causal order. Prove or refute: the record attached to use (y, x_j) depends only on y and x_j, hence on no quotient.
3. **Record outcome law at fixed settings** — prove that prefix records are diagonal in the word basis and commute, so the joint outcome distribution over any finite set of records is quotient-invariant *when settings are held fixed*.
4. **Settings** — the setting of each record is forced by the lineage's A13R clock state, which advances with serviced vacuum maintenance. Mark exactly where quotient dependence enters: quotient → per-step pool → service realization → clock residue → setting → outcome law. Certify this is the *only* entry point on the record side.
5. **Request layer** — A12 request multiset per record (invariant) vs per-step pool (dependent).
6. **Ledger** — per-step conservation identities hold under any quotient; determine whether any *cumulative* ledger quantity over a horizon (total served forced, total served vacuum, total relief, final backlog, clock residue) is quotient-invariant. Expected: none beyond the conservation identities, by non-compositionality of the pooled kernel; give the witness.
7. **Marks and interval G±** — RRP1 marks depend on which requests are served (dependent); determine whether the *support* of possible mark sets, and the interval envelope (G⁻, G⁺) taken over all realizations, is quotient-invariant.
8. **Coherence lifetime** — for each object, the number of steps between its formation and the full RO-D record of its word. Prove or refute: under both T_sat and T_dag the lifetime is exactly 1 for every object (every object is used as a parent at the step after its formation). State the general theorem: for which quotients is lifetime ≡ 1, and characterize quotients admitting lifetime > 1.

## 4.3 Output

The maximal quotient-invariant structure, stated as a theorem, plus the exact residue. This envelope is the candidate domain for any later maturation observable; nothing quotient-dependent may define an epoch without first selecting a quotient by theorem or declared premise.

---

# 5. Part 2 — No-choice test (do not select)

Test whether any *source-backed* condition separates T_sat from T_dag:

- **(a) Locality of the quotient** — step of y a function of y's own ancestry. Expected: both satisfy.
- **(b) Naturality w.r.t. the frozen representation's grading** — the clock tower C_d, frontier H_D, and append J_D are depth-indexed. State whether "the global step must be natural w.r.t. depth" is a source theorem or a premise; if premise, do not apply.
- **(c) Selector-freeness** — the fired set is the full enabled set with no comparison function among enabled events. T_sat qualifies; T_dag fires the min-grade subset. Classify this as a definition distinguishing a `PRIORITY_FREE` law from a `GRADED` law; do not promote it to a selection principle.
- **(d) Service non-compositionality** — does the pooled kernel impose any constraint on admissible quotients beyond ancestry-compatibility? Expected: none.

Verdict: `SELECTED_BY_SOURCE_THEOREM(member, witness)` or `NOT_SEPARATED_BY_SOURCE(premise_class = {PRIORITY_FREE, GRADED})`.

---

# 6. Part 3 — Synchronous-family saturation readout (exact, both members, k ≤ K_max)

## 6.1 Growth (closed form or exact recurrence)

|X_k| and |En(X_k)| for both laws for every k the theorem permits: T_sat via depth-count recurrence, T_dag via dag_size counts. Exact integers.

## 6.2 Load lower bounds

Using the frozen per-record request counts (Q1: 11–13; Q2 histories: 22–26) and the RO-D record count per step, give exact lower bounds on the forced pool F_k for k ≤ 6 under both laws, independent of any Λ₀ choice.

## 6.3 Ledger scan (not a selection)

Λ₀ is undeclared. Run the frozen ledger with genesis parameters (Γ, D, m, H) ranging over the *complete registered CD2R/UEQ0 domain* — every registered value, no value singled out — and report for each: the smallest k with F_k > Γ; the exact probability that S^V_k = 0 (no vacuum served) at each k ≤ K_max; backlog B_k; lapse Φ_k distribution; direct-limit clock increments. Report identically for T_sat and T_dag.

Verdict: `SYNCHRONOUS_FAMILY_LEDGER_SATURATES_BY_k=κ_FOR_ALL_REGISTERED_Γ` or `DEVELOPMENTAL_REGIME_EXISTS_FOR(Γ range, k range)` or `NOT_REACHED(reason)`. κ is a readout, not a threshold, and defines nothing.

---

# 7. Part 4 — Capacity, vacuum demand, and enablement: source status (zero premise)

Frozen candidate list (record at Commit A, before Part 3 results are read):

Classify each of Γ (capacity), D (vacuum demand), m (persistent load), H (relief candidates) at genesis and under update as `EXTERNAL_CONSTANT` / `STATE_FUNCTION(formula, source file)` / `UNDECLARED`, across UEQ0, the CD2R finite-set representation, A13R, and R40–R45. Specifically answer:

1. Does any active source define Γ or D as a function of rendered structure (marks, G±, |X|, served history)?
2. Does any active source gate adjunction enablement on realization — i.e., require Par(y) ⊆ (rendered set) rather than Par(y) ⊆ X?
3. If both answers are no, record the minimal premise class for a throttled opportunity law, listing without selecting: **RG1** rendered-parent gating (with the premise-invariant G⁻/G⁺ envelope from R44 giving lower/upper enabled sets); state-scaled Γ; state-scaled D. Record for each: what it would make quotient-dependent, whether it introduces a parameter, and whether it is binary.

This is a census. No candidate is tested dynamically in R50.

---

# 8. Part 5 — Registry identification

Compare the T_dag⁵(genesis) object set (as unordered recursive sets, canonical form) with the CD0 registered DAG-7 object set. Exact set equality → record `EXACT_OBJECT_SET_ARROW(registry → constructor, dynamics not identified)` in the genealogy; otherwise the first differing object.

---

# 9. Hostile controls (8)

1. selecting T_sat or T_dag by preference or by the saturation readout;
2. using the saturation readout to introduce or justify a throttle premise within this round;
3. singling out a Λ₀ scan value as physical;
4. step = time; historical rounds = steps;
5. κ or coherence lifetime used as a maturity threshold;
6. any historical numeric;
7. modification of frozen roots; BELL2 opened;
8. any hand-produced hash.

Each rejection carries its first exact obstruction.

---

# 10. Outputs (8)

```text
OD0_R50_REPORT.md
OD0_R50_RESULTS.json
OD0_R50_COUNTEREXAMPLES.md                    (append-only)
R50_INPUT_LOCK.json
R50_BUNDLING_INVARIANT_ENVELOPE.json          (Part 1: per-layer classification + witnesses + lifetime theorem)
R50_NO_CHOICE_TEST.json                       (Part 2)
R50_SATURATION_READOUT.json                   (Part 3: growth, load bounds, full Λ₀ scan, both members)
R50_CAPACITY_ENABLEMENT_SOURCE_STATUS.json    (Parts 4–5)
R50_OUTPUT_MANIFEST.json
```

Deterministic rerun: byte-identical JSON.

---

# 11. Verdict tree

Always, if the layer list and candidate lists were frozen at Commit A:

```text
OD0_R50_PASS_BUNDLING_ENVELOPE_AND_SYNCHRONOUS_FAMILY_CHARACTERIZED
```

Components: `ENVELOPE = {per-layer classification}`; `LIFETIME = {≡1 for both | witness otherwise}`; `NO_CHOICE = {SELECTED(member) | NOT_SEPARATED(premise class)}`; `SATURATION = {SATURATES_BY_κ | DEVELOPMENTAL_REGIME_EXISTS | NOT_REACHED}`; `CAPACITY_SOURCE = {Γ, D, m, H status; enablement gating status; minimal throttle class if undeclared}`; `REGISTRY_ARROW = {EXACT | witness}`.

## R51 rule

- If `SATURATION = SATURATES_BY_κ` and enablement/capacity are `UNDECLARED` → R51 classifies the minimal throttle premise class (RG1 with the G⁻/G⁺ envelope as the leading candidate), by the A13R/RO1 binary-premise template; it does not add physical time.
- If `DEVELOPMENTAL_REGIME_EXISTS` in the synchronous family → R51 derives epoch observables on the quotient-invariant envelope, comparing members only through invariants.
- If `NO_CHOICE = SELECTED` → R51 derives epoch observables on the selected member.
- If a source already couples capacity or enablement to rendered structure → R51 rederives the opportunity family with that coupling before anything else.

---

# 12. Compact terminal return

```text
OD0-R50 OVERALL VERDICT:
COMMITS (A / B):
R49 PIN / WORKTREE / BELL2 / VALUES PARSED / HAND HASHES:
FAMILY IDENTIFICATION: T_sat = depth filtration? T_dag = dag_size filtration? smallest depth≠dag_size object:
ENVELOPE (per layer, 1–8): 
COHERENCE LIFETIME: T_sat / T_dag / general theorem:
QUOTIENT-DEPENDENCE ENTRY POINT (record side):
NO-CHOICE TEST (a)–(d):
GROWTH |X_k|, |En(X_k)| both members (k ≤ …):
LOAD LOWER BOUNDS F_k (k ≤ 6):
Λ₀ SCAN: registered domain size / smallest k with F_k > Γ / P(S^V_k = 0) trajectory / lapse:
SATURATION VERDICT:
CAPACITY SOURCE: Γ / D / m / H status; enablement gating status; minimal throttle class:
REGISTRY ARROW:
HOSTILE CONTROLS: N/8:
DETERMINISTIC RERUN:
OUTPUT MANIFEST SHA-256:
RECOMMENDED SINGLE R51 MOVE:
```

---

# Adjudicator's registered prediction (Claude, pre-run)

Part 1: object layer and record poset invariant under all quotients; record outcome law invariant at fixed settings; quotient dependence enters only through the clock setting via service; A12 multisets invariant, pools dependent; no cumulative ledger invariant beyond conservation; coherence lifetime ≡ 1 for both members. Part 2: `NOT_SEPARATED_BY_SOURCE`, premise class {PRIORITY_FREE, GRADED}; (a) both pass, (b) is a premise, (c) is a definition, (d) no constraint. Part 3: F_k exceeds every registered Γ by k ≤ 3 for both members; P(S^V = 0) → 1 by k ≤ 4; `SATURATES_BY_κ` with κ ≤ 3. Part 4: Γ, D, m EXTERNAL or UNDECLARED as state functions; no source gates enablement on rendering; RG1 recorded as the leading binary candidate. Part 5: exact object-set equality with the registry. This prediction constrains nothing in the run.
