# OD0-R56 CLAUDE CODE PACKAGE v0.1

## Target-Blind Freeze for H2: Provenance-Disclosed Observables, the Availability Prediction Set, the H2 Comparison Protocol, and the M5 Label-Reachability Opening

### Position

R55 is frozen: commits `b57f3fb` (A) / `c399d05` (B) / `443d942` (C-stamp), output manifest `8765f837…` (full hash in R55_PROVENANCE_STAMP.json). Verdict `OD0_R55_PASS_LATE_REGIME_TARGETS_ADJUDICATED`. Frozen support PROVEN: P(pair available at D ever forms) ≤ φ(Γ,m,D) = Γ(Γ−1)·[1/(Γ−m) + 2Γ²/(Γ−m)²]/(D−1), via the exact co-service identity n(n−1)/((F+D)(F+D−1)) and a drain/band occupation bound (the package's telescoping route had a gap at quiet steps; repaired argument on record). Termination SCOPED (conditional on superlinear burst-cost growth). Rate: |X_k| ≤ C·k/log log k. Run3_Dijet paper pinned into H2 (`16e9cfcd…`, sealed). H1 spent; H2–H5 sealed.

### Adjudication notes to carry

1. **Scale.** The registered domain (Γ ≤ 5, |X| ~ 50–130 at 10⁴ steps) is exactness-scale, not universe-scale. Theorem-grade statements carry; readout-grade statements are shape checks only, and the H2 protocol weights them accordingly.
2. **Reparametrization.** Historical rounds are policy indices (R49, R54). Any H2 comparison may use only shapes invariant under a monotone reparametrization of time: orderings, monotonicity, freezing, capacity thresholds, cross-run randomness. Growth *rates* are not comparable and are excluded from the protocol.
3. **Central open problem, queued (not in R56):** typical burst-cost growth of the random DAG built by the process; it controls both the rate exponent and the unconditional termination claim. Gets its own round.

---

# 0. Governing question

Before H2 is opened, freeze — target-blind with disclosed provenance — (i) the nine H1-provenance observables as exact functions on 𝔷⁺, (ii) the derived availability prediction set with evidential classes, (iii) the H2 comparison protocol with its pass/fail rule; and open M5 by classifying the exact semantic label alphabet by minimal service configuration, giving each label a capacity threshold, a state condition, and a first-appearance law on the realized random ideal.

Zero new premises. H2 is not opened. No particle, collision, or physical claim.

---

# 1. Locks (minimal)

Pin R55 stamp. Clean worktree at start and end. `BELL2_opened = false`. H2–H5 sentinels `parsed = false` at start and end; the H2 PDF hash re-verified and untouched. Exact arithmetic; readouts labeled and seeded. Hash hygiene; stamp commit at the end.

# 2. Commits

Commit A: this package verbatim; lock verification; Sections 4, 5, 6 (observables, prediction set, protocol) recorded as frozen. Commit B: M5 classification and outputs. Commit C: stamp.

---

# 3. Frozen inputs

The conditional stack; R52 cluster theorem (same-step sibling groups ≤ Γ−1; between-step shell); R52 c_first typing (Q1 / Q2); R47 CCP1_EXACT_SPARSE (356 labels, 178/178 by factor; chains of consecutive actual appearances by occurrence rank; no absent-rank stage); R50 registry arrow; R54 H1 extraction (definitions only, for provenance disclosure); R55 φ and its proof.

---

# 4. Part 1 — Provenance-disclosed observable freeze (record at Commit A)

Each entry: exact definition as a function on 𝔷⁺; H1 provenance disclosed; evidential class of its monotonicity under the throttled process (THEOREM / READOUT / NONE). These are frozen for H2–H5 only; H1 is spent.

1. **containment(w)** = #objects whose closed ancestry contains w. Monotone nondecreasing — THEOREM (objects never destroyed; ancestry fixed at formation).
2. **co-embedding(w₁,w₂)** = #objects whose closed ancestry contains both. Nondecreasing — THEOREM.
3. **support size** = #realized objects of a fixed reference set (default: the 173 registry objects; also per grade). Nondecreasing — THEOREM; eventually frozen with positive probability for each grade — THEOREM (R55).
4. **participation ratio** of containment weights = (Σ_w c_w)² / Σ_w c_w². Class: READOUT.
5. **concentration / backbone** = the set of objects carrying the top-quantile chain-through weight (chains passing through w; define exactly: total chains of descendants of w that pass through w), with the quantile fixed at 0.95 as the *historical* convention, disclosed. Class: READOUT.
6. **dilution** = (#objects with dag_size ≤ 7)/|X|. → 0 as |X| → ∞ — THEOREM (numerator ≤ 173); stepwise monotonicity NONE.
7. **containment clock** and **co-embedding clock** = the historical clock functionals of (1) and (2), extracted verbatim from R54_H1_EXTRACTION (log or normalized forms as historically defined); class inherits from (1),(2).
8. **parent–child diameter** of the composite graph. Nondecreasing — prove or classify (adding objects can only add paths; diameter may still drop if a shorter path appears — state exactly).
9. **early-layer count** = #objects with dag_size ≤ 7 (the numerator of 6). Nondecreasing, bounded by 173 — THEOREM.

Nothing may be added after Commit A.

---

# 5. Part 2 — Derived availability prediction set (record at Commit A)

Statements about "availability of fixed structures at maturity," each with class, each reparametrization-invariant:

- **P1 (monotone availability).** Any fixed structure, once realized, remains; availability is nondecreasing in process time. THEOREM. (Weak; included for completeness.)
- **P2 (inclusion decay).** For a fixed structure available when the universe has D objects, realization probability is bounded by φ ∝ 1/(D−1): earlier-available structures are realized with higher probability. THEOREM (bound).
- **P3 (freeze order).** The eventual support of lower grades freezes before that of higher grades: the probability that a grade's realized set still changes after a given process time decreases with the grade's availability size. THEOREM for the bound; READOUT for the observed order at Γ ≤ 5.
- **P4 (configuration ordering).** Structures whose formation requires k same-step co-served tokens are reachable only for Γ ≥ k (from the cluster structure); families ordered by minimal configuration become reachable in that order as capacity rises, and at fixed Γ families above the threshold never appear. THEOREM (to be established in Part 4).
- **P5 (frozen-random subset).** Independent realizations of the process at equal parameters realize different eventual supports; presence of a fixed late-available structure varies across runs. THEOREM. Testable against H2 only if H2 reports multiple independent substrates at equal age; else N/A.
- **P6 (cost-ordered persistence).** Structures with larger chain multiplicity impose larger rendering cost when built upon (cost law) and are, per unit availability, realized later. THEOREM for the cost law; READOUT for the ordering.

Excluded by construction: any statement about growth rates, round counts, or absolute ages.

---

# 6. Part 3 — H2 comparison protocol (record at Commit A; executed in a later round)

1. **What will be compared.** The reported H2 patterns that are invariant under monotone reparametrization of rounds — orderings of family emergence, monotonicity of availability, freezing/saturation of any family, dependence on substrate capacity or on family complexity, and cross-substrate variability if reported — against P1–P6 and the Part 1 observables, mapped **by definition** at opening (R54 rule: names, words, counts are not maps). H2's "strain" and "channel" notions map only if their extracted definitions coincide with a frozen function on 𝔷⁺; otherwise `UNMAPPED_COMPUTABLE` / `UNMAPPED_INAPPLICABLE`.
2. **Rule.** PASS iff every mapped, reparametrization-invariant H2 pattern is consistent with the corresponding THEOREM-grade prediction and no such pattern contradicts one; PARTIAL if consistent but a stage-defining H2 observable is unmapped or matches only at READOUT grade; FAIL if a THEOREM-grade prediction is contradicted by a reparametrization-invariant H2 pattern. Mismatches at equal prominence.
3. **Forbidden.** Round-number alignment; rate comparison; any prediction added, criterion moved, or observable renamed after opening; any repair of the tower in the opening round.
4. **Model-family caveat, mandatory.** The H2 engine's opportunity law and substrate (from the R48 census and the sealed repository commit) are stated at opening; a mismatch may reflect them.

---

# 7. Part 4 — M5 opening: label reachability by minimal configuration

## 7.1 Alphabet scope audit (first)

State exactly which record events the global process fires and how each is typed into the frozen history/label alphabets: single-use records (Q1 typing), same-step sibling pairs (Q2 typing), and same-step sibling groups of size ≥ 3 (which arise for Γ ≥ 4). For groups ≥ 3: report how R52–R55 typed and costed them; classify that rule as `FROZEN_ALPHABET_COVERS` / `PAIRWISE_REDUCTION_CONVENTION` / `AD_HOC`. If not covered by frozen source, scope every downstream statement to Γ ≤ 3 (groups ≤ 2) until an m-sibling alphabet is derived, and record the gap.

## 7.2 Classification (theorem)

For each exact semantic label e in the frozen alphabet (356 for the two-factor system; plus the Q1 labels if distinct), derive:
- its **minimal service configuration**: the smallest number of co-served tokens and the parent-sharing pattern required for a record event that emits e;
- its **capacity threshold** Γ_min(e);
- its **state condition** (which objects must exist and which must be shell vs recorded for the emitting event to be a first use vs a repeat);
- whether e is emitted on first use only, on repeat use only (query token, provenance edge), or both.

Prove P4 from this classification.

## 7.3 First-appearance and recurrence laws

- τ_e = first process time at which e appears; give the exact law where computable (K_max points) and bounds otherwise; classify labels reachable at each registered Γ.
- **Recurrence.** Under CCP1_EXACT_SPARSE, the carrier chain of e is its sequence of actual appearances. Prove or bound: P(e appears infinitely often | e appears once), and the growth of the chain length with process time. Registered target: for repeat-use labels, each object is used again as a parent infinitely often a.s. (per-burst reuse probability ~ Γ/D against D growing at most linearly in bursts — harmonic divergence), so chains are unbounded with logarithmically sparse recurrence; state exactly what is proven.
- **No particle promotion.** Labels stay exact semantic A12 objects (CCE4). Nothing here is a species.

## 7.4 Readout (labeled)

On the existing seeded trajectories: per-label first-appearance times, reachable-label counts by Γ, chain-length growth; per-Γ ordering of label families by first appearance. Readouts define nothing.

---

# 8. Hostile controls (8)

1. anything added to Sections 4–6 after Commit A;
2. any H2 content read; sentinels not `false`;
3. any rate or round-number statement in the prediction set or protocol;
4. any ≥3-sibling convention presented as frozen source without the 7.1 audit;
5. any label promoted to a particle, species, or channel;
6. any use of H1 beyond disclosed provenance;
7. modification of TG1, the cost law, the filtration, or frozen roots; BELL2 opened;
8. any hand-produced hash; any placeholder.

---

# 9. Outputs (7 + stamp)

```text
OD0_R56_REPORT.md
OD0_R56_RESULTS.json
OD0_R56_COUNTEREXAMPLES.md                    (append-only)
R56_INPUT_LOCK.json                           (Sections 4–6 verbatim, frozen)
R56_H2_PREREGISTRATION.json                   (observables + prediction set + protocol, one sealed object with hash)
R56_M5_LABEL_REACHABILITY.json                (Part 4: audit, classification, laws, readouts)
R56_OUTPUT_MANIFEST.json
R56_PROVENANCE_STAMP.json                     (commit C)
```

Deterministic rerun: byte-identical JSON.

---

# 10. Verdict tree

Always, if Sections 4–6 were frozen at Commit A and H2 remained sealed:

```text
OD0_R56_PASS_H2_PREREGISTERED_AND_M5_OPENED
```

Components:
- `ALPHABET_SCOPE = {COVERS | PAIRWISE_CONVENTION(scoped Γ ≤ 3) | AD_HOC(scoped)}`
- `P4_CONFIGURATION_ORDERING = {PROVEN | REFUTED(witness) | SCOPED}`
- `RECURRENCE = {PROVEN(law) | SCOPED(gap)}`
- `REACHABLE_LABELS_BY_Γ = {counts}`; `H2_PREREG_HASH = {…}`

## R57 rule

- If `ALPHABET_SCOPE = COVERS` or scoped cleanly, and P4 PROVEN → R57 opens H2 under the sealed protocol, one comparison, no repair (mirroring R54).
- If the alphabet audit exposes an ad hoc convention that affected R52–R55 costs at Γ ≥ 4 → R57 first re-scopes or rederives those results (m-sibling alphabet from the incidence structure), and H2 waits.
- The random-DAG cost problem remains queued; it is opened as its own round after H2, unless the H2 result makes it the immediate dependency.

---

# 11. Compact terminal return

```text
OD0-R56 OVERALL VERDICT:
COMMITS (A / B / C-stamp):
R55 STAMP PIN / WORKTREE / BELL2 / H2–H5 SENTINELS / H2 PDF HASH / HAND HASHES:
SECTIONS 4–6 FROZEN AT COMMIT A (yes/no); H2_PREREG_HASH:
OBSERVABLES (9): definitions frozen; monotonicity classes:
PREDICTION SET (P1–P6): classes:
ALPHABET SCOPE AUDIT: single / pair / ≥3-group typing; convention class; scoped Γ:
LABEL CLASSIFICATION: labels by minimal configuration; Γ_min histogram; first-use vs repeat-use:
P4 STATUS:
FIRST-APPEARANCE LAWS: exact points / bounds; reachable labels by Γ:
RECURRENCE: proven law or gap:
READOUT SUMMARY (labeled):
HOSTILE CONTROLS: N/8:
DETERMINISTIC RERUN:
OUTPUT MANIFEST SHA-256 (in stamp):
RECOMMENDED SINGLE R57 MOVE:
```

---

# Adjudicator's registered prediction (Claude, pre-run)

Alphabet audit: ≥3-sibling groups were costed by a pairwise reduction convention, not frozen source → M5 statements scoped to Γ ≤ 3 until an m-sibling alphabet is derived; R52–R55 *theorems* unaffected (they use bounds on cost, not its exact typing), readouts at Γ ≥ 4 flagged. Labels split into single-use (Γ_min = 2) and sibling-pair (Γ_min = 3) classes, with repeat-use labels (query token, provenance edge) reachable at Γ = 2; P4 PROVEN. Recurrence: each object is reused as a parent infinitely often a.s. with reuse probability per burst ~ Γ/D, so repeat-use chains are unbounded and logarithmically sparse; first-use chains for a fixed label grow with the number of distinct objects of the emitting type. H2 preregistration sealed with P2–P4 as the load-bearing theorem-grade predictions. This prediction constrains nothing in the run.
