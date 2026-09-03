# OD0-R49 CLAUDE CODE PACKAGE v0.1

## Minimum Global Opportunity Law: Candidate Freeze and Forced / One-Premise / Choice Classification

### Position

R48 is frozen: commits `244e61a` (A) / `36d38b1` (B), output manifest `ea354c9ca639b236c0e1a5377ac61d32e5d13ad681abef43a5fd968ea84cd5ef`. Verdict: hybrid B/C. Per-component OD0 restriction: x PARTIAL (CD1I) | N FAIL (trace theorem) | S FAIL | Λ FAIL | G± FAIL. GM first failure for the native constructor F1 is GM4 only. Holdout PARTIAL (4 named-missing artifacts); values parsed = 0.

### Correction to the R48-recommended move

R48 recommended testing whether the A12 compiler is derivable from the CD1I record algebra. That is already frozen: CD2R Theorem 3 classifies A12 as CANONICAL_DERIVED, the cardinality functor on atomic generators of the A11R fact-event category. R49 does not reopen it. The correct reading of R48's "A12 is the first non-derived layer" is that A12's domain (fact edits J_h) is empty in the bare constructor because the constructor contains no record events. The obstruction is upstream of A12: record-event opportunity. R49 targets opportunity.

### Structural corollary of R48 (record as theorem, not premise)

Z splits into a state-derived part, x (a representation of the incidence structure of X), and a history-accumulated part, (N, S, Λ, G±) (functions of which events occurred). By CD0 Theorem 1 no state that forgets occurrence determines the latter. Therefore any global maturation model must carry an occurrence/record layer — the global state is necessarily Z-shaped:

𝔷 = (X, N, S, Λ, G⁻, G⁺).

Record this as `OCCURRENCE_LAYER_NECESSITY` (derived from R48 + CD0 Thm 1). R49 works with this shape throughout.

---

# 0. Governing question

For the Z-shaped global state, what is the smallest set of source-derivable properties that determine at each global step (i) which enabled adjunctions occur, (ii) whether and which A10 records occur, (iii) when service rounds occur — and is the resulting global transition 𝕋 unique with zero premises, unique given one binary activity premise, a nonunique canonical family, or premise-requiring?

Zero-or-one-premise round. Template for any premise: A13R0 (an inert option not excluded by source, a unique law given the binary activity statement). No policy weights, no physical time, no thresholds, no historical numerics, no geometry/particle/gravity/SI claims.

---

# 1. Locks (minimal)

Pin the R48 output manifest hash and commits; R47 digest transitively. Verify clean worktree at start and end. `BELL2_opened = false`. Historical numerical content is never parsed. Exact arithmetic only.

# 2. Commits

Commit A: this package verbatim + lock verification + the frozen candidate classes of Sections 4.2, 5.0, 6 recorded as frozen before any test. Commit B: everything else.

---

# 3. Frozen inputs (cite, do not rediscover)

- **CD0:** constructor, enabled events, exact diamond, Thm 1 (legal sequences X→Y are the linear extensions of the ancestry order on Y∖X; one trace class per comparable pair).
- **CD1I §5.4:** the unresolved append J_D — the adjunction acts on the frontier as the *invariant, non-recording* isometry. **§5.6:** the A10 prefix-record write |w⟩|0⟩ ↦ |w⟩|π_ℓ(w)⟩ and the induced block dephasing.
- **CD2R Thm 3:** A12 cardinality functor (additive, region-covariant) — closed. Service-equivalence principle (frozen premise) and hypergeometric kernel. Population/relief frozen rules.
- **A13R / A13R0:** clock action; the binary-activity-premise template.
- **R28:** 5,184 full controls = query × setting. **R30:** no active source supplies opportunity.
- **R48:** obstruction theorem, per-component restriction, 31-field inventory, genealogy.

---

# 4. Part 1 — Adjunction opportunity

## 4.1 Source extraction

From CD0 source, extract exactly: the object rule; every source-defined grading g (depth, leaf-size, DAG-size, "level") with its definition; whether any step/round/layer is defined as a *transition* or only as a grading of a static DAG; the exact reason the registered DAG stops at level 7 / 173 objects (cutoff parameter, grading bound, or rule restriction). Report each with file and line. Do not assume the seed's summary rule is the executed rule.

## 4.2 Frozen choice-free candidate class

- **T_sat:** X ↦ X ∪ En(X), En(X) = all enabled composites.
- **T_g** for each source grading g: X ↦ X ∪ {y ∈ En(X) : g(y) = min_{En(X)} g} (next-grade saturation).
- **T_id:** X ↦ X (inert).

For each, prove or refute: determinism; order-freeness (via Thm 1); covariance under primitive exchange and every CD0 source automorphism; genesis compatibility; well-definedness under unbounded growth; whether T_sat = T_g for a given g (prove, or give the smallest X where they differ).

## 4.3 Classification

State exactly which candidates are canonical. If no source-backed premise excludes T_id, state

**CO1 (constructor activity):** at each global step, enabled adjunctions occur (rather than none),

and derive the unique law given CO1 within the choice-free class.

## 4.4 Asynchronous laws

Laws firing one event or a bounded batch per step with a selector are classified `PREMISE_REQUIRING_SELECTION`. Enumerate the source-derivable selector constraints (covariance, fairness/exhaustiveness, no dependence on unretained order) but select none. Record explicitly: historical engine "rounds" are asynchronous-policy indices, not saturation layers; no identification between round counts and layers is licensed.

---

# 5. Part 2 — Record opportunity (the crux)

## 5.0 Frozen candidate class (freeze before testing)

- **RO-A** adjunction-as-record: the adjunction x = {p,q} is itself an A10 record on the lineage(s) of p and/or q.
- **RO-D** downstream-incidence record: a record on an unresolved lineage occurs when a later adjunction takes that lineage's object (or a descendant) as IN or CO; the recorded prefix is determined by the ancestry position used.
- **RO-X** external: records remain external controls only (status quo; OD0 stays a cocycle).
- **RO-0** record-inert: adjunctions never record; frontiers stay coherent.

## 5.1 RO-A vs the frozen append

Prove or refute that RO-A contradicts CD1I §5.4 (the frozen append retains no distinction among the new roles). If refuted, RO-A is closed with that witness.

## 5.2 RO-D uniqueness

For a lineage word w of depth D and a downstream event using ancestor x_j (depth j) in role r ∈ {IN, CO}: does the CD1I prefix-record algebra assign a unique (lineage, prefix length ℓ, query) — a unique element or unique subset of the 5,184 full controls — with no free parameter? Enumerate exactly at D ≤ 3. Certify uniqueness; covariance under reflection, cyclic-origin gauge, factor exchange; compatibility with the A10 write map; and no over-recording (the induced record never distinguishes more than the downstream event structurally distinguishes).

## 5.3 Setting component

Does the downstream event determine the clock setting (odometer residue) of the full control, or only the query? If only the query: classify the residual as forced by the lineage's own direct-limit clock residue (A13R) or free.

## 5.4 Inert exclusion

If no source-backed premise excludes RO-0, state

**RO1 (record activity):** a distinction event whose parent set includes a lineage object with an unresolved incidence frontier acts nontrivially (as an A10 prefix record) on that frontier,

and derive the unique induced record law given RO1. If CO1 and RO1 are provably one statement, say so and keep one.

Hostile: no tuning of ℓ so that N or S restricts; no use of A12 counts or service outcomes to pick the record rule; no external query alphabet imported.

---

# 6. Part 3 — Service opportunity

Frozen candidates: **SV-pool** (one kernel application per global step on the pooled forced set — the frozen UEQ0 form F_t = B_t + m_t + C_b, with C_b the disjoint union of J_h over all record outcomes in the step) vs **SV-int** (service interleaved between individual events within a step).

Prove: A12 additivity across a step (CD2R Thm 3); regional partition via the ancestry/prefix regions of X; the GM8 composition/order theorem for many local occurrences per global step — which parts are order-free (appends by Thm 1; request pools by additivity) and which are order-sensitive (ledger updates under SV-int). Expected classification: SV-pool the unique order-free candidate; SV-int `PREMISE_REQUIRING_SELECTION`. Persistent load m remains external; record it.

---

# 7. Part 4 — Global state and commuting diagram (conditional)

If Parts 1–3 yield a unique 𝕋 (zero premise, or given CO1/RO1):

- write 𝔷_k = (X_k, N_k, S_k, Λ_k, G±_k), genesis 𝔷_0 = ({a,b}, 0, ∅, Λ_0, ∅) with Λ_0 the source-declared empty ledger (report if undeclared);
- write 𝕋 explicitly as: saturation append → induced records (branch measure) → A12 pool → pooled service → RRP1 marks → interval update. RRP1 remains a frozen premise; reuse, do not rederive;
- verify exactly for k ≤ K_max: normalization; Markov closure; per-component restriction to OD0 (x via CD1I, N via induced records, S via A12, Λ via kernel, G± via RRP1); local-global probability and successor commutation for each induced local occurrence; factor/region covariance. K_max = largest k for which the joint record-frontier over all lineages is exactly enumerable; state it and the reason (expected K_max = 3);
- re-score GM1–GM12 for the composite; GM4 now reads `FORCED` or `DERIVED_GIVEN_(CO1, RO1)`.

If nonunique: emit the family and the smallest state distinguishing its members.

Note on the global frontier: every composite descends from {a,b}, so lineages share ancestors. Treat the joint frontier as one shared-ancestor cluster system (R12/R16 machinery generalized), not as a tensor product of independent Q1 lineages. If the generalization from two lineages to many is not already frozen, state the exact gap; do not assume factorization.

---

# 8. Part 5 — Target-blind field readouts (only if Part 4 closes; no thresholds, no labels)

Tabulate for k ≤ K_max:

- |X_k|, |En(X_k)|, induced-record count per step;
- coherence-cluster census of the global frontier: connected components under "share an unresolved letter," component sizes, fraction of resolved letters;
- ancestry-cluster type census (Q1-type isolated vs Q2-type shared-ancestor pairs by R12/R16 classification) — the candidate effective-quotient field, since the local quotient dimension is a function of cluster type not depth (R6/R16);
- legal control alphabet Γ(𝔷_k) ⊆ Γ_5184, cardinality and orbit decomposition;
- request pool size, F/(F+D), lapse Φ distribution, direct-limit clock increments;
- CCP1 first-appearance ranks τ_e where licensed (CCE1); absent-rank scope unchanged.

These are readouts for R50; no epoch is defined and no historical comparison is made.

---

# 9. Hostile controls (10)

1. enumeration order ≠ step;
2. DAG size or grading ≠ step unless proved for a T_g;
3. an asynchronous selection presented as canonical;
4. historical rounds identified with saturation layers;
5. records assumed active without stating RO1;
6. record rule tuned so N/S restrict;
7. A12 derivation reopened;
8. local depth = epoch, or cluster fraction = epoch by threshold;
9. any historical numeric or fitted threshold;
10. modification of frozen roots; BELL2 opened; global frontier assumed to factorize.

Each rejection carries its first exact obstruction.

---

# 10. Outputs (8 + optional)

```text
OD0_R49_REPORT.md
OD0_R49_RESULTS.json
OD0_R49_COUNTEREXAMPLES.md                          (append-only)
R49_INPUT_LOCK.json
R49_ADJUNCTION_OPPORTUNITY_CLASSIFICATION.json      (Part 1)
R49_RECORD_OPPORTUNITY_CLASSIFICATION.json          (Part 2 incl. D≤3 enumeration certificates)
R49_GLOBAL_TRANSITION_CANDIDATE.json                (Parts 3–4; or R49_OPPORTUNITY_OBSTRUCTION.json)
R49_OUTPUT_MANIFEST.json
optional: R49_FIELD_READOUTS.json                    (Part 5)
```

Deterministic rerun: byte-identical JSON (canonical serialization, sorted keys).

---

# 11. Verdict tree

Always, if the candidate classes were frozen before testing and every candidate adjudicated:

```text
OD0_R49_PASS_OPPORTUNITY_CANDIDATE_CLASS_FROZEN_AND_CLASSIFIED
```

Primary (exactly one):

- `OPP_FORCED` — unique zero-premise 𝕋 with induced records. R50 = intrinsic epoch-observable algebra.
- `OPP_ONE_PREMISE` — unique 𝕋 given CO1 and/or RO1. R50 = epoch-observable algebra conditional on them (A13R pattern).
- `OPP_NONUNIQUE_CANONICAL` — ≥2 inequivalent choice-free laws. R50 = premise-invariant envelope / no-choice theorem.
- `OPP_REQUIRES_SELECTION` — no choice-free record law; minimal premise class enumerated. R50 classifies.

Secondary: `RECORD_RULE = {RO-A refuted | RO-D unique | RO-D nonunique(residual: setting/prefix) | none}`; `SERVICE_RULE = {SV-pool unique | nonunique}`; `COMMUTING_DIAGRAM = {PASS k≤K_max | FAIL(component, witness) | NOT_REACHED}`.

---

# 12. Compact terminal return

```text
OD0-R49 OVERALL VERDICT:
COMMITS (A / B):
R48 PIN VERIFICATION / CLEAN WORKTREE / BELL2 / HISTORICAL VALUES PARSED:
CONSTRUCTOR STEP SEMANTICS (source-defined transition? gradings found? level-7 cutoff reason):
ADJUNCTION LAW: candidates canonical / T_sat = T_g? / T_id excluded by source? / CO1 stated?:
RECORD LAW: RO-A / RO-D uniqueness / setting residual / RO-0 excluded? / RO1 stated?:
SERVICE LAW: SV-pool / GM8 order theorem (order-free vs order-sensitive parts):
GLOBAL TRANSITION: unique / family / obstruction; premises used:
COMMUTING DIAGRAM: K_max, per-component restriction status (x / N / S / Λ / G±):
GM1–GM12 RESCORE (first failures if any):
GLOBAL FRONTIER CLUSTER STRUCTURE AT k ≤ K_max (components / resolved fraction):
FIELD READOUTS EMITTED (y/n):
HOSTILE CONTROLS: N/10:
DETERMINISTIC RERUN:
OUTPUT MANIFEST SHA-256:
RECOMMENDED SINGLE R50 MOVE:
```

---

# Adjudicator's registered prediction (Claude, pre-run)

Part 1: T_sat is the unique nontrivial choice-free law; T_id is not excluded by source → CO1 stated. Part 2: RO-A refuted by the frozen invariant append; RO-D determines the query (prefix = ancestry position used) but not the setting; RO-0 not excluded → RO1 stated. Overall `OPP_ONE_PREMISE` (CO1 and RO1 as two binary activity premises of one type, possibly collapsing to one). Part 3: SV-pool unique order-free. Part 4: closes exactly at K_max = 3, with the global frontier a single coherence cluster at k = 1–2 and first fragmentation at k = 3. This prediction constrains nothing in the run.
