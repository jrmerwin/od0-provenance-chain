# OD0-R52 CLAUDE CODE PACKAGE v0.1

## Exact Closed Observable Algebra, Frontier-Cluster Theorem, and Intensive Dynamics of the Throttled Global Process

### Position

R51 is frozen: commits `28f50e5` (A) / `2369705` (B), output manifest `8df67d66…` (full hash from R51_OUTPUT_MANIFEST.json). Verdict `THROTTLE_UNIQUE_MINIMAL(ADJ-V-S, TG1, scope Γ 2..5)`. TG1 stated, not adopted: serviced vacuum maintenance of an object is enablement-active, same-step — an enabled adjunction fires iff both parents' standing vacuum tokens were served in the previous service realization — under V ≅ X (`NEW_IDENTIFICATION`). Per-token service identity `DERIVED` from the matching groupoid. Growth LINEAR (≤ C(Γ,2) per step); envelope survives verbatim; exact burst-drain cycle at registered points; coherence lifetime > 1 with probability 1/3 at the smallest deadlock-free point.

The global process is now fully specified conditional on (CO1, RO1, TG1, V ≅ X) and the frozen local laws. All R52 statements are conditional on that stack and inherit its evidential classes.

### Adjudication notes to carry

1. **Regime of validity.** Scope Γ ∈ 2..5 is the registered domain, not a physical restriction. Nothing in R52 extrapolates Γ.
2. **Frozen constitutive rules now do quantitative work.** Population factor two and six-based relief (FROZEN_MODEL_RULE, possible foam artifacts) enter the ledger dynamics. R52 carries them unchanged and adds one sensitivity *readout* (Part 5), not a modification.
3. **Regional structure** must be extracted from source before any global count is interpreted: whether regions are fixed in number under the growing DAG, how a new object's region is assigned, and whether Γ is per region.

---

# 0. Governing question

What is the exact minimal set of state-derived observables of the throttled global process that is closed under its transition (the global operator system), what exact conditional identities govern its intensive variables, and does the frontier's unresolved sector decompose into bounded clusters so that exact computation scales?

Zero new premises. No epoch labels, no thresholds, no historical numerics, no external referents. Readouts are readouts.

---

# 1. Locks (minimal)

Pin R51 output manifest hash and commits (transitively R50–R47). Clean worktree at start and end. `BELL2_opened = false`. Historical numerical content never parsed. Exact arithmetic for every theorem and every exact readout; sampled readouts (Part 5) are explicitly labeled, seeded, and never cited as proof.

# 2. Commits

Commit A: this package verbatim; lock verification; the observable inventory of Section 5 and the quotient ladder of Section 6 recorded before any closure test or readout. Commit B: everything else.

---

# 3. Frozen inputs

The full conditional stack: CD0, CD1I, CD2R, A13R/A13R0, UEQ0, R28/R30, R41 RRP1, R44 interval, R45 currents, R49 (RO1/RO-D, CO1, SV-pool), R50 envelope, R51 (TG1, V ≅ X, per-token identity, dynamics readouts, K_max budget).

---

# 4. Part 1 — Structural prerequisites (theorems)

## 4.1 Regional structure under the global DAG

From source: the definition of a structural region for an object of the global DAG (prefix cylinder at what depth?); whether the number of regions is fixed or refines with depth; whether Γ, D, H, P, B are per region; how V ≅ X partitions tokens by region; whether a record on lineage w and its A12 requests are charged to w's region. Classify each as `CANONICAL_DERIVED` / `DERIVED_GIVEN_CDA1` / `UNDECLARED`. If refinement of regions with depth would change total capacity, state it exactly and do not adopt either reading without source.

## 4.2 Record scope and the frontier-cluster theorem

State exactly what RO-D records when a downstream adjunction uses ancestor x_j: the prefix through x_j's own letter, or the prefix before it. Then prove or refute:

**Cluster theorem (conditional on TG1).** At every reachable state, the unresolved sector of the global frontier decomposes into disjoint clusters, each consisting of the unresolved letters of one object and of its children, and no unresolved letter is shared across clusters. Give the exact cluster state: if the parent's own letter is unresolved and shared by m children, the m-party equality state 3^{-1/2} Σ_r |r⟩^{⊗m} (source-derived as the linearized diagonal Δ_I on m descendants, generalizing BELL0's m = 2); if the parent's letter is recorded, a product of independent single-letter appends. Certify at every reachable state for k ≤ K_max at all registered points; prove for general k from RO-D + TG1 or give the first counterexample.

If the theorem holds, the two-to-many gap is closed *for the throttled process* and every record outcome is a bounded-cluster computation. Report the maximum cluster size reachable as a function of Γ.

## 4.3 Exact growth identity

Prove: given the service realization serves s vacuum tokens at a state with |X| = n, the served objects are a uniform s-subset of X (from uniform matchings + token identity), and

E[new objects | s, X] = C(s,2) · (1 − (n−2)/C(n,2)),

using that every composite is exactly one parent pair, so X contains exactly n − 2 existing pairs. State the exact distribution's dependence on the composite graph (vertices = objects, edges = parent pairs) and give the smallest pair of states with equal (n, s) but different growth distributions.

## 4.4 Exact forced-inflow identity

From RO-D + A11R + A12, determine exactly the request count generated by (i) the first use of an object (full maximal-scope record; Q1-type vs sibling-shared Q2-type history), and (ii) a repeated use of an already-recorded object (idempotent A10 write: which A12 edit types, if any, are still generated — query token, provenance edge, unresolved-cell token). Report the exact per-use request constants c_first (by type) and c_repeat.

## 4.5 Exact ledger identities

With F forced pool, D = |X| (regional), n = min(Γ, F + D), V⁰ = min(Γ, D):
- E[S^V | state] = n·D/(F + D) (hypergeometric mean);
- E[Φ² | state] = D/(F + D) whenever Γ ≤ D; give the other cases exactly;
- P(S^V ≥ 2 | state) in closed form (growth-possible probability);
- E[new objects | state] by composing 4.3 with the hypergeometric law;
- exact relief term v as a function of (B, P, H, Γ) from the frozen controller.

Certify each identity against the R51 exact distribution evolution at all 324 registered points.

---

# 5. Part 2 — Frozen observable inventory (target-blind; record at Commit A)

Every entry is a function of the global state 𝔷 = (X, N, S, Λ, G±) only.

**Object layer (per region and total):** |X|; |U| unresolved shell (objects never used as a parent); |En(X)| = C(|X|,2) − (|X|−2); depth and dag_size distributions; composite-graph degree distribution (children per object); cluster census from 4.2 (number and sizes).

**Record layer:** number of recorded words; prefix-length distribution; N multiplicities by P4 type; |S|; first-use vs repeat-use counts.

**Ledger (per region):** B, D, F, P, H, Γ; clock residue; V⁰; the conditional laws of 4.5 evaluated at the state.

**Interval / currents:** |G⁻|, |G⁺|, |G⁺ ∖ G⁻|; D/L/M stocks (R45).

**Intensive:** x = D/(F + D); B/Γ; |U|/|X|; |G⁻|/|S|; E[Φ² | state]; P(S^V ≥ 2 | state); E[new objects | state]; requests-outstanding per object F/|X|.

Nothing is added after Commit A. Nothing is removed on the basis of readouts.

---

# 6. Part 3 — Closure (lumpability) audit

On the exact reachable state set for k ≤ K_max at each registered point, construct the exact transition and test each candidate quotient for exact lumpability (block-constant transition probabilities), in this frozen ladder:

- **L0:** ledger counts only (B, D, P, H, Γ, clock residues).
- **L1:** L0 + |X|, |U|.
- **L2:** L1 + composite-graph isomorphism class of X.
- **L3:** L2 + record-status map (word → recorded prefix length) + cluster census.
- **L4:** L3 + N and S content.
- **L5:** full 𝔷.

Report the coarsest exactly lumpable level, the first witness pair against each coarser level (R2 style), and the dimension/description of the closed system at that level. Then test **intensive closure**: whether the intensive variables of Section 5 are exactly closed at any level, and if not, the smallest witness. State plainly whether epoch observables can be defined on an exactly closed quotient or only on the full state.

---

# 7. Part 4 — Intensive dynamics: exact identities, registered conjecture, and bounds

## 7.1 Exact

Prove whatever exact statements about the long-run process follow from Part 1 identities without a limit argument: e.g., that P(S^V ≥ 2 | state) is bounded below by a positive function of (Γ, x) so vacuum service never vanishes identically once x is bounded below; that x is bounded below along any trajectory once |X| exceeds a Γ-dependent constant; monotonicity or conservation identities for cumulative counts.

## 7.2 Registered conjecture (mean-field fixed-point map)

Write, as a conjecture, the one-step map on (x, u = |U|/|X|, g) obtained by replacing each random increment by its exact conditional expectation from Part 1 (ΔD = g; ΔF = c·g − E[S^F] − v; …), and its fixed-point conditions. Label `MEAN_FIELD_CONJECTURE`. Do not fit anything. Do not claim convergence.

## 7.3 Sampled readout of the frozen law (evidence, not proof)

For each registered point with Γ ∈ 2..5: 1,000 trajectories × 1,000 steps of the exact throttled law, sampled with recorded seeds, computing only the Section 5 observables. Report per-step means and exact-fraction quantiles of x, u, g, E[Φ²|state], cluster sizes, B/Γ. State whether the sampled x, u, g settle, oscillate, or drift, and compare with the 7.2 fixed point — as a readout. Any regime boundary visible in these plots is a readout, not a definition.

---

# 8. Part 5 — Constitutive-rule sensitivity readout

Repeat 7.3 at two registered points with (a) relief disabled, (b) population factor set to one, each labeled `SENSITIVITY_READOUT_NOT_A_MODEL`. Report only whether the qualitative structure of x, u, g changes. This informs whether the frozen foam-family rules are load-bearing for maturation; it selects nothing.

---

# 9. Hostile controls (9)

1. any observable added or dropped after Commit A;
2. any epoch label, threshold, or basin defined from readouts;
3. sampled results cited as theorems or used to choose a quotient level;
4. mean-field map presented as more than a registered conjecture;
5. Γ extrapolated beyond 2..5, or regions refined without source;
6. any external referent (cosmology, particles, time, inflation);
7. any historical numeric; historical rounds identified with steps;
8. modification of frozen roots; BELL2 opened;
9. any hand-produced hash.

---

# 10. Outputs (9)

```text
OD0_R52_REPORT.md
OD0_R52_RESULTS.json
OD0_R52_COUNTEREXAMPLES.md                    (append-only)
R52_INPUT_LOCK.json
R52_STRUCTURAL_THEOREMS.json                  (Part 1: regions, record scope, cluster theorem, identities + certificates)
R52_OBSERVABLE_INVENTORY.json                 (Part 2, frozen at Commit A)
R52_CLOSURE_LADDER.json                       (Part 3: per level, lumpability, witnesses, closed-system description)
R52_INTENSIVE_DYNAMICS.json                   (Part 4–5: exact statements, conjecture map, seeded readouts, sensitivity)
R52_OUTPUT_MANIFEST.json
```

Deterministic rerun: byte-identical JSON (sampled readouts reproduce under recorded seeds).

---

# 11. Verdict tree

Always, if the inventory and ladder were frozen at Commit A:

```text
OD0_R52_PASS_GLOBAL_OBSERVABLE_ALGEBRA_AUDITED
```

Components:
- `CLUSTER_THEOREM = {PASS(max cluster size f(Γ), m-sibling state) | FAIL(witness) | PARTIAL}`
- `RECORD_SCOPE = {THROUGH_OWN_LETTER | BEFORE_OWN_LETTER}` (sibling entanglement present/absent)
- `REGIONS = {FIXED(n) | REFINING | UNDECLARED}`; `CAPACITY_TOTAL = {constant | state-dependent}`
- `CLOSURE = {EXACT_CLOSED_AT(Lj, description) | FULL_STATE_REQUIRED}`; `INTENSIVE_CLOSURE = {EXACT | NOT_EXACT(witness)}`
- `IDENTITIES = {certified list}`; `LONG_RUN_EXACT = {list}`; `MEAN_FIELD_CONJECTURE = {map, fixed point}`
- `READOUT = {settle | oscillate | drift, per Γ}`; `SENSITIVITY = {structure unchanged | changed, which rule}`

## R53 rule

- If an exactly closed quotient exists → R53 (M3) defines the maturation filtration by exact state criteria on that quotient (regimes of x, u, and P(S^V ≥ 2 | state); recurrence structure), proves what can be proven about the late regime, and writes the candidate mature-basin definition as fixed-point/invariance conditions — target-blind. R54 then opens H1 non-adaptively.
- If only the full state closes → R53 seeks the minimal exact extension of the intensive set that closes, or an exact limit theorem, before any filtration.
- If the cluster theorem fails → R53 addresses the failure witness first; exact computation cannot scale without it.

---

# 12. Compact terminal return

```text
OD0-R52 OVERALL VERDICT:
COMMITS (A / B):
R51 PIN / WORKTREE / BELL2 / VALUES PARSED / HAND HASHES:
REGIONS / CAPACITY TOTAL:
RECORD SCOPE / CLUSTER THEOREM (max size, state form, certification range, general proof or witness):
GROWTH IDENTITY (certified?) / SMALLEST (n,s)-EQUAL GROWTH-DIFFERENT WITNESS:
FORCED-INFLOW CONSTANTS c_first (by type) / c_repeat:
LEDGER IDENTITIES CERTIFIED (list):
CLOSURE LADDER: coarsest lumpable level, witnesses per level, closed-system description:
INTENSIVE CLOSURE:
LONG-RUN EXACT STATEMENTS:
MEAN-FIELD FIXED POINT (x*, u*, g*) per Γ — CONJECTURE:
SAMPLED READOUT SUMMARY per Γ (settle/oscillate/drift; x, u, g at k=1000):
SENSITIVITY READOUT:
HOSTILE CONTROLS: N/9:
DETERMINISTIC RERUN:
OUTPUT MANIFEST SHA-256:
RECOMMENDED SINGLE R53 MOVE:
```

---

# Adjudicator's registered prediction (Claude, pre-run)

Regions fixed in number under the global DAG (prefix cylinders at the frozen depth), Γ per region, capacity total constant. Record scope BEFORE_OWN_LETTER, so siblings share the parent's unresolved role and the cluster theorem passes with the m-sibling equality state, max cluster size ≤ 1 + C(Γ,2)+1. Growth identity certified; L0–L2 nonlumpable (composite-graph witness at L1, record-status witness at L2); exact closure first at L3 or L4; intensive set not exactly closed at finite k. E[Φ² | state] = D/(F+D) certified for Γ ≤ D. c_first ∈ {11,13} (Q1) / {22..26} (Q2), c_repeat small but nonzero (query token + provenance edge). Sampled readouts: x settles with damped oscillation to a Γ-dependent value near the mean-field fixed point; u settles; g settles near Γ(1−x*)/c. Sensitivity: relief changes x* quantitatively, not the qualitative settle/oscillate structure; population factor is not load-bearing. This prediction constrains nothing in the run.
