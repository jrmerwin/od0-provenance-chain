# OD0-R54 CLAUDE CODE PACKAGE v0.1

## Opening the H1 Structural-Epoch Holdout under the Frozen R53 Protocol — One Comparison, No Repair

### Position

R53 is frozen: commits `33c1782` (A) / `8c1a470` (B), output manifest `c985a7ca…` (full hash from R53_OUTPUT_MANIFEST.json). Verdict `OD0_R53_PASS_MATURATION_FILTRATION_DEFINED_TARGET_BLIND`. The maturation filtration (E0 = {F+D ≤ Γ}, permanent exit at D > Γ; E1 = {D > Γ} forward-invariant; drained/draining and burst/quiet decompositions; {c_min ≤ Γ} transient and nonempty) is target-blind. U-growth proven a.s. for m < Γ; rate open (≤ linear; readouts consistent with a √k-type law, never proof); m ≥ Γ partial with the gap stated. The R54 comparison protocol is frozen in R53_INPUT_LOCK.json.

R54 executes that protocol and nothing else. It adds no observable, moves no criterion, renames no stratum, and repairs nothing.

### Housekeeping (before Commit A)

**Provenance stamp commit.** Write `R52_PROVENANCE_STAMP.json` and `R53_PROVENANCE_STAMP.json`, each recording that round's commit B hash and output manifest hash (copied from tool output), in one commit. Adopt as standing convention: every round ends with a stamp commit; reports never carry placeholders again.

**H2 pin (if artifacts were supplied).** If the Run3_Dijet paper and/or result archives have been placed in the holdout directory, hash-pin them into the H2 entry of the holdout manifest with `scientific_values_parsed = false`. Do not open them. If not supplied, record H2 still incomplete.

---

# 0. Governing instruction

Open H1 only. Verify every H1 artifact's hash against the R48 holdout manifest before reading any content. H2–H5 remain sealed; their sentinels must read `parsed = false` at start and end.

The frozen protocol (R53_INPUT_LOCK.json, hash-verified and copied verbatim into R54_INPUT_LOCK.json):

1. **Compared:** the derived regime sequence and derived monotone observables vs. the historical *qualitative regime sequence* and the observables it was reported on — sequence and monotonicity only. No numeric thresholds. No alignment of historical round numbers with derived steps (historical rounds are policy indices; R49).
2. **Rule:** PASS iff the historical sequence is a coarsening of the derived filtration order and each historical observable maps to a frozen R52/R53 observable with the same reported monotonicity; PARTIAL if the sequence matches but an observable does not map or does not match; FAIL if the order is contradicted. Mismatches at equal prominence.
3. **Forbidden:** any observable added, criterion moved, or stratum renamed after opening.

---

# 1. Locks (minimal)

Pin R53 output manifest hash and commits (transitively R52–R47). Pin the R48 holdout manifest hash. Clean worktree at start and end. `BELL2_opened = false`. Hash hygiene in force.

# 2. Commits

Commit A (before any H1 content is read): this package verbatim; the protocol copied verbatim from R53_INPUT_LOCK.json with hash match recorded; the **derived-side table** of Section 3 frozen. Commit B: extraction, mapping, adjudication, outputs. Commit C: stamp.

---

# 3. Derived-side table (freeze at Commit A, from R52/R53 outputs only)

Record, before opening, each derived item with its evidential class:

**Derived filtration order:**
- E0 (free) → E1 (congested), exact, permanent exit at D > Γ — THEOREM.
- Within E1: {c_min ≤ Γ} transient (last exit is a finite random step) — THEOREM; drained/draining alternation (renewal at F = 0) — THEOREM; burst/quiet — exact decomposition.
- Asymptotic regime: |X| → ∞ a.s. for m < Γ — THEOREM; rate ≤ linear — THEOREM; √k-type curve — READOUT.

**Derived monotone observables (direction, class):**
- |X|: nondecreasing — THEOREM.
- recorded-cone mask: nondecreasing — THEOREM.
- shell fraction u = |U|/|X|: direction as reported in R53 readouts — READOUT (state it).
- chain-multiplicity distribution: mean nondecreasing in |X| — THEOREM (parent-sum recurrence); tail shape — READOUT.
- cycle length / drain length: two-sided bounds growing with burst cost — THEOREM; geometric growth — CONJECTURE.
- full-drain frequency: decreasing in readouts — READOUT.
- burst cost: c_min not monotone — THEOREM (witness); typical burst cost increasing — READOUT.

Nothing may be added to this table after Commit A.

---

# 4. Part 1 — H1 extraction

For each H1 artifact (from the R48 manifest: the registry-persistence/structural-epochs paper and its result archives; any notes files present), extract and record:

- model family and evidential status (from the R48 census; do not reclassify);
- the reported regime sequence, verbatim labels, in reported order;
- for each regime: the observable(s) it was defined or detected on, with the artifact's *definition* of each observable (what it computes on what state), and the reported direction/monotonicity of each observable within and across regimes;
- the reported transition markers between regimes (qualitative), and any numeric thresholds — recorded as historical values only, playing no role.

Record definitions precisely enough that a later round could freeze them target-blind for H2–H5 comparisons.

---

# 5. Part 2 — Mapping by definition

For each historical observable, decide whether its definition, applied to the derived state 𝔷⁺ (a pair-closure DAG with used/served markings and ledger), coincides with a frozen R52/R53 observable **as a function**. Names, words, and counts are not maps (R48 rule). Record:

```text
historical observable | definition | derived counterpart (frozen id) or UNMAPPED | reason
```

Historical observables that are well-defined on 𝔷⁺ but not in the frozen inventory are `UNMAPPED_COMPUTABLE`; those not well-defined on 𝔷⁺ (e.g., requiring a registry-embedding layer or a foam) are `UNMAPPED_INAPPLICABLE`.

---

# 6. Part 3 — Adjudication (frozen rule, operationalized)

**Coarsening test.** The derived order is the chain of exact strata E0 < E1, refined by the transient stratum {c_min ≤ Γ} (early E1) and its complement (late E1), with the renewal alternation inside and the asymptotic regime as the limit. A historical sequence S1 < … < Sn *coarsens* this order iff there is an order-preserving assignment of each Si to a derived stratum or to a derived monotone-observable regime such that no historical transition reverses a derived one. Give the explicit assignment, or the explicit obstruction (the first historical transition that cannot be placed).

**Monotonicity test.** For each mapped observable, compare the historical reported direction with the derived direction and its class (THEOREM/READOUT/CONJECTURE). A match against a READOUT-class derived direction is a match of readouts, and is labeled so.

**Verdict:** PASS / PARTIAL / FAIL exactly per the frozen rule, with every mismatch and every UNMAPPED item listed at equal prominence.

**Model-family caveat (mandatory section):** state which opportunity/scheduling law the historical engine used (from its source, per the R48 census) versus the derived throttled law (TG1), and that any mismatch may reflect that difference rather than the constructor. Do not use this caveat to soften the verdict.

---

# 7. Part 4 — Quarantined post-opening readout (optional, not adjudication)

For each `UNMAPPED_COMPUTABLE` historical observable, compute its definition on the R53 sampled derived trajectories and report its direction. Label the section `POST_OPENING_READOUT_NOT_ADJUDICATION`. Nothing in it enters the verdict. Its only permitted future use: candidates for target-blind freezing before any H2–H5 comparison.

---

# 8. Hostile controls (8)

1. any observable, criterion, or stratum changed after Commit A; any derived-side item added after opening;
2. any historical round number aligned with a derived step;
3. any mapping by name, word, or count;
4. any content of H2–H5 read; sentinels must remain `parsed = false`;
5. Part 4 content leaking into the verdict;
6. any modification of TG1, the cost law, or the filtration in response to the result;
7. modification of frozen roots; BELL2 opened;
8. any hand-produced hash; any placeholder left in a report.

---

# 9. Outputs (7 + stamp)

```text
OD0_R54_REPORT.md
OD0_R54_RESULTS.json
OD0_R54_COUNTEREXAMPLES.md                    (append-only; every mismatch and obstruction)
R54_INPUT_LOCK.json                           (protocol verbatim + hash; derived-side table; H1 hash verification; H2 pin status)
R54_H1_EXTRACTION.json                        (Part 1)
R54_MAP_TABLE_AND_ADJUDICATION.json           (Parts 2–3; Part 4 in a separate quarantined key)
R54_OUTPUT_MANIFEST.json
R54_PROVENANCE_STAMP.json                     (commit C)
```

Deterministic rerun: byte-identical JSON.

---

# 10. Verdict tree

Always, if the protocol and derived-side table were frozen at Commit A and all H1 hashes verified:

```text
OD0_R54_PASS_H1_OPENED_UNDER_FROZEN_PROTOCOL
```

Primary: `H1_COMPARISON = {PASS | PARTIAL(list) | FAIL(obstruction)}`.

Secondary: `MAP_TABLE = {mapped: n, unmapped_computable: n, unmapped_inapplicable: n}`; `H2_PIN = {pinned | incomplete}`; `SENTINELS_H2_H5 = false`.

## R55 rule

- PASS or PARTIAL → R55 returns to the queued theorems on the derived process before any further holdout: (i) the eventual-support law (which fixed finite motif sets appear a.s. versus with probability < 1 under U-growth with uniform pairing); (ii) the m ≥ Γ gap; (iii) the growth rate. Any `UNMAPPED_COMPUTABLE` observable may be frozen target-blind for H2–H5 only after being re-derived from the process, with its H1 provenance disclosed.
- FAIL → R55 diagnoses the contradicted transition: whether it is a model-family/opportunity-law artifact or a property of the constructor. The diagnosis goes on record at equal prominence. No premise is modified without the failure and its diagnosis recorded first (R48 discipline), and any modification is a new preregistered premise round.

---

# 11. Compact terminal return

```text
OD0-R54 OVERALL VERDICT:
COMMITS (A / B / C-stamp):
R53 PIN / R48 HOLDOUT MANIFEST PIN / WORKTREE / BELL2 / HAND HASHES:
R52/R53 STAMPS WRITTEN:
H1 ARTIFACTS: n pinned / n hash-verified / n missing:
H2 PIN STATUS (Run3_Dijet):
SENTINELS H2–H5 (must be false):
DERIVED-SIDE TABLE FROZEN AT COMMIT A (yes/no):
HISTORICAL SEQUENCE (verbatim labels, order, model family):
HISTORICAL OBSERVABLES EXTRACTED (n) WITH DEFINITIONS:
MAP TABLE (mapped / unmapped_computable / unmapped_inapplicable):
COARSENING ASSIGNMENT OR OBSTRUCTION:
MONOTONICITY MATCHES (per mapped observable, with derived class):
H1 COMPARISON VERDICT: PASS / PARTIAL / FAIL:
MODEL-FAMILY CAVEAT (historical opportunity law vs TG1):
POST-OPENING READOUT (quarantined; present yes/no):
HOSTILE CONTROLS: N/8:
DETERMINISTIC RERUN:
OUTPUT MANIFEST SHA-256 (in stamp):
RECOMMENDED SINGLE R55 MOVE:
```

---

# Adjudicator's registered prediction (Claude, pre-run)

PARTIAL. The first two historical stages coarsen the exact strata (E0 and early E1 with the transient {c_min ≤ Γ} stratum, whose last exit is the derived sharp event); the last two map to asymptotic readout-level regimes or are unmapped. At least one historical observable is `UNMAPPED_COMPUTABLE` — a through-path/hub-weight measure (the frozen inventory carries chains ending at an object, not chains passing through it) — and the concentration stage rests on it. No historical transition contradicts the derived order. The historical engine's opportunity law differs from TG1. This prediction constrains nothing in the run.
