# OD0-R55 CLAUDE CODE PACKAGE v0.1

## Late-Regime Theorems of the Throttled Process: Frozen-Support Law, Termination Dichotomy in Persistent Load, and Growth-Rate Bounds

### Position

R54 is frozen: commits `bd21aca` (stamps) / `45eb08c` (A) / `67991bf` (B) / `e0f70c9` (C-stamp), output manifest `88c5b963…` (full hash in R54_PROVENANCE_STAMP.json). Verdict `OD0_R54_PASS_H1_OPENED_UNDER_FROZEN_PROTOCOL`, `H1_COMPARISON = PARTIAL`: sequence coarsens with no reversal; 4 mapped observables match (3 theorem-grade, 1 readout-grade); 9 `UNMAPPED_COMPUTABLE`, 2 `UNMAPPED_INAPPLICABLE`. H1 is now **spent**: nothing may be validated against it again. H2–H5 sealed (`parsed = false`).

### Adjudication notes to carry

1. **Historical engine identified.** The H1 engine is T_sat verbatim; its regimes are read along the dag_size foliation of a completed static universe. Historical "epochs" are grade strata of the universal DAG, not process time. The derived process reads that foliation out slowly and randomly in process time; the R54 coarsening reflects that.
2. **Cross-validations on record:** grade-8 count 945; growth sequence 5, 12, 68, 2280, 2598062 = C(n,2)+2; mean degree 4(n−2)/n exact on any ideal. The sealed enumerations and the blind tower agree on every shared number.
3. **Inventory gap, not contradiction.** The 9 unmapped-computable observables (containment, co-embedding, support size, participation, concentration/backbone, dilution, containment/co-embedding clocks, diameter) are functions on 𝔷⁺. They are *not* frozen in R55; per the R54 rule they are frozen in R56 with H1 provenance disclosed, after the theorems below.
4. **Provenance stamps** are now standing convention; no report placeholders.

---

# 0. Governing question

Three exact statements about the late regime of the throttled process, in priority order: (1) the eventual support of any fixed finite set of target objects is a nondegenerate random subset, with explicit inclusion-probability bounds — provable by burst counting without a growth rate; (2) growth terminates almost surely when persistent load exceeds capacity plus relief, giving a sharp dichotomy in m; (3) improved exact bounds on the growth exponent for m < Γ.

Zero new premises. No external referents. No thresholds. H1 provenance of the *questions* (support locking prompted question 1) is disclosed; the theorems are about the frozen process and use no historical content.

---

# 1. Locks (minimal)

Pin R54 stamp (manifest hash, commits). Clean worktree at start and end. `BELL2_opened = false`. H2–H5 sentinels `parsed = false` at start and end. Exact arithmetic for theorems; sampled readouts labeled and seeded. Hash hygiene; stamp commit at the end.

# 2. Commits

Commit A: this package verbatim; lock verification; the theorem statements of Sections 4–6 as *targets* (frozen wording, so the run proves or refutes fixed statements). Commit B: proofs/certificates/readouts. Commit C: stamp.

---

# 3. Frozen inputs

The conditional stack over the frozen local laws; R52 identities (uniform served subset; growth identity; P(S^V ≥ 2) bound); R53 (cost law; renewal theorem; U-growth for m < Γ via drift band + Borel–Cantelli; relief boundary note m < Γ + H); R50 registry arrow (exact identity of the 173 T_dag⁵ objects); R54 map table (for provenance disclosure only).

---

# 4. Part 1 — Frozen-support theorem (primary)

## 4.1 Target statement (frozen)

Let m < Γ and let τ be a step at which the process is in E1 with D_τ = |X_τ| > Γ. Let y = {u, v} be any composite not in X_τ whose parents u, v ∈ X_τ. Then:

(a) **Finite co-service.** The expected number of steps k ≥ τ at which both u and v are vacuum-served is finite, with an explicit bound depending only on (Γ, D_τ).

(b) **Positive non-formation.** P(y never forms | 𝔷⁺_τ) > 0, with an explicit lower bound depending only on (Γ, D_τ).

(c) **Inclusion decay.** P(y ever forms | 𝔷⁺_τ) ≤ φ(Γ, D_τ) with φ(Γ, D) → 0 as D → ∞; obtain the sharpest explicit φ the argument yields (target: φ = O(Γ²/D)).

(d) **Nondegenerate eventual support.** For any fixed finite set M of composites, the eventual support S_∞ ∩ M is a nondegenerate random variable whenever M contains an element unavailable or unformed at some E1 state; the registry set (173 objects) is a specific instance.

## 4.2 Proof route (to be executed exactly)

1. Per step, given the state, the served vacuum set is a uniform s-subset of X with s = S^V (R52); P({u,v} ⊆ served | s) = s(s−1)/(D(D−1)); E[S^V(S^V−1)] ≤ Γ(Γ−1)·P(S^V ≥ 2).
2. Given S^V ≥ 2, a burst occurs with probability ≥ 1 − 2(D−2)/(D(D−1)) ≥ 1/2 for D ≥ 4 (a specific pair among the served is new with at least that probability).
3. Hence E[# co-service steps] ≤ 2Γ(Γ−1)·E[Σ_{bursts b ≥ τ} 1/(D_b(D_b−1))], and D_b ≥ D_τ + (number of bursts since τ) since every burst adds ≥ 1 object; the sum telescopes: Σ_{j≥0} 1/((D_τ+j)(D_τ+j−1)) = 1/(D_τ−1).
4. (b) from (a) by the conditional product/supermartingale argument: P(never) = E[Π_k (1 − p_k(state))] with Σ p_k finite and each p_k < 1 in E1.
5. (c) by Markov/union on the co-service count; (d) as a corollary.

Certify (a)–(c) numerically against the exact distribution evolutions (K_max points) where the exact P(y forms by step K) is computable, and against the 10⁴-step sampled trajectories as a labeled readout.

## 4.3 Corollaries to state

- Early-available pairs (D_τ small) form with probability near 1; the bound is vacuous for D_τ ≤ Γ+1 — state exactly where it bites.
- The expected fraction of currently available pairs that ever form tends to 0 as D grows; the universe realizes a vanishing fraction of the universal DAG, randomly.
- The realized universe is a random ideal of the universal DAG whose law is determined by the process; the eventual support of each fixed grade is random.

---

# 5. Part 2 — Termination dichotomy in persistent load

## 5.1 Target statement (frozen)

Let H be the relief-candidate count and let the relief controller be active in the congested regime (its conditions P ≥ 6, B ≥ Γ hold eventually; prove or scope). Then:

(a) **Supercritical termination.** If m > Γ + H, the number of bursts is finite almost surely: growth terminates at a finite random size.

(b) **Subcritical persistence** (R53, carried): if m < Γ, growth is unbounded a.s.; extend to m < Γ + H under the relief conditions or state the exact gap.

(c) **Critical line.** m = Γ + H (and the band Γ ≤ m ≤ Γ + H if (b) does not extend): state precisely what is proven and what is open.

## 5.2 Proof route for (a)

1. Forced outflow per step ≤ Γ (service) + H (relief), inflow ≥ m; hence B_k ≥ B_0 + (m − Γ − H)k → ∞ linearly, regardless of D.
2. x_k = D_k/(F_k + D_k) ≤ D_k/((m − Γ − H)k − const).
3. Suppose infinitely many bursts. Then D_k → ∞, and the cost law makes forced inflow from bursts unbounded, so F_k grows faster than any linear function of D_k; combine with P(burst at k | state) ≤ Γ(Γ−1)x_k² to show Σ_k P(burst at k) < ∞ on every trajectory with infinitely many bursts — a contradiction by the conditional Borel–Cantelli lemma (Lévy's extension). Handle the two cases N_k sublinear (direct) and N_k linear (cost-driven) explicitly.
4. Conclude N_∞ < ∞ a.s.; derive any bound on E[terminal size] the argument yields.

Certify against exact distribution evolutions at the 27 registered m ≥ Γ points (which side of the line each lies on, given its H) and against seeded 10⁴-step readouts (terminal-size histograms, labeled).

## 5.3 Statement discipline

The dichotomy is stated in model-internal terms only: regions whose persistent load exceeds service-plus-relief capacity stop generating new distinctions after a finite random time; regions below the line never stop.

---

# 6. Part 3 — Growth-rate bounds for m < Γ (bounded effort)

Attempt to sharpen the R53 rate statement using the cost law and the renewal structure: prove any exact upper bound of the form |X_k| ≤ C·k^β with β < 1, and any lower bound of the form |X_k| ≥ c·k^α with α > 0, for m < Γ. If neither is obtainable within the round, record the precise obstruction (which quantity's growth is uncontrolled) and stop. Readout comparison with the √k-type curve remains labeled.

---

# 7. Part 4 — Registry-inclusion readout (labeled; provenance disclosed)

Using the R50 exact identity of the 173 T_dag⁵ objects and the existing seeded 10⁴-step trajectories at all registered points: per-object inclusion frequency at k ∈ {10², 10³, 10⁴}; fraction of the registry present, by grade; whether inclusion frequency at k = 10⁴ is still changing between 10³ and 10⁴ (an empirical stand-in for "frozen"). This is a readout of the Part 1 theorem on a specific derived set; the question's H1 provenance is disclosed; it is not an H1 comparison (H1 is spent) and it defines nothing. Its role is to characterize the prediction shape for the sealed H2 comparison.

---

# 8. Hostile controls (8)

1. any theorem statement altered after Commit A (targets are frozen; the run proves, refutes, or scopes them);
2. any use of H1 content beyond the disclosed provenance of a question; any renewed H1 comparison;
3. any content of H2–H5 read;
4. readouts cited as proof; the rate exponent asserted from readouts;
5. any threshold or external referent;
6. modification of TG1, the cost law, the filtration, or frozen roots;
7. BELL2 opened;
8. any hand-produced hash; any placeholder.

---

# 9. Outputs (7 + stamp)

```text
OD0_R55_REPORT.md
OD0_R55_RESULTS.json
OD0_R55_COUNTEREXAMPLES.md                    (append-only)
R55_INPUT_LOCK.json                           (frozen theorem targets verbatim)
R55_FROZEN_SUPPORT_THEOREM.json               (Part 1: proof, bounds, certificates)
R55_TERMINATION_DICHOTOMY.json                (Part 2: proof or scoped gap; per-point side of the line; certificates)
R55_RATE_BOUNDS_AND_REGISTRY_READOUT.json     (Parts 3–4)
R55_OUTPUT_MANIFEST.json
R55_PROVENANCE_STAMP.json                     (commit C)
```

Deterministic rerun: byte-identical JSON.

---

# 10. Verdict tree

Always, if the targets were frozen at Commit A:

```text
OD0_R55_PASS_LATE_REGIME_TARGETS_ADJUDICATED
```

Components:
- `FROZEN_SUPPORT = {PROVEN(φ) | REFUTED(witness) | SCOPED(gap)}`
- `TERMINATION = {PROVEN_SUPERCRITICAL(m > Γ+H) | SCOPED(band)}`; `PERSISTENCE_EXTENSION = {m < Γ+H proven | gap}`; `CRITICAL_LINE = {statement}`
- `RATE = {UPPER(β) / LOWER(α) | OBSTRUCTION(named)}`
- `REGISTRY_READOUT = {fraction present by grade at 10⁴; still changing yes/no}`

## R56 rule

- If `FROZEN_SUPPORT = PROVEN`: R56 freezes, target-blind for H2–H5, (i) the nine H1-provenance observables as exact functions on 𝔷⁺ (provenance disclosed), and (ii) the inclusion-probability law as the derived availability prediction; then preregisters the H2 comparison protocol (availability of fixed structures at maturity as a frozen random subset — shape and monotonicity only), and opens the M5 question: which repeated exact semantic labels (CCP1) become reachable in the realized random ideal.
- If `FROZEN_SUPPORT = REFUTED`: R56 diagnoses the failing step of the proof route first; nothing is frozen for H2 until the support law is settled.
- The termination result, either way, is queued for M7 (persistent-load regions) and is not compared with anything in R56.

---

# 11. Compact terminal return

```text
OD0-R55 OVERALL VERDICT:
COMMITS (A / B / C-stamp):
R54 STAMP PIN / WORKTREE / BELL2 / H2–H5 SENTINELS / HAND HASHES:
THEOREM TARGETS FROZEN AT COMMIT A (yes/no):
FROZEN SUPPORT: (a) bound / (b) bound / (c) φ(Γ,D) / (d) — PROVEN / REFUTED / SCOPED; certification (exact points, readout):
WHERE THE BOUND BITES (smallest D_τ):
TERMINATION: supercritical proof status; persistence extension; critical line; per-point side (27 m ≥ Γ points); terminal-size readout:
RATE BOUNDS: upper β / lower α / obstruction:
REGISTRY READOUT: fraction present by grade at 10²/10³/10⁴; still changing:
HOSTILE CONTROLS: N/8:
DETERMINISTIC RERUN:
OUTPUT MANIFEST SHA-256 (in stamp):
RECOMMENDED SINGLE R56 MOVE:
```

---

# Adjudicator's registered prediction (Claude, pre-run)

Frozen support PROVEN with φ(Γ, D) = 2Γ(Γ−1)/(D−1) or sharper; the bound bites for D_τ > 2Γ(Γ−1)+1 and is vacuous below; early registry grades present with frequency near 1 at 10⁴, late-available structures with frequency decreasing in their availability size; inclusion frequencies essentially unchanged between 10³ and 10⁴ for early grades. Termination PROVEN for m > Γ + H; persistence extends to m < Γ + H under the relief conditions; the line m = Γ + H stays open. Rate: an upper bound with β < 1 obtainable from the cost law (cost ≥ linear in D forces sublinear growth); a lower bound with α ≥ 1/3 plausible; if only one side closes, the obstruction is the drained-state frequency. This prediction constrains nothing in the run.
