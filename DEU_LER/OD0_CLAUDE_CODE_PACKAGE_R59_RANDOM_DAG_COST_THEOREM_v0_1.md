# OD0-R59 CLAUDE CODE PACKAGE v0.1

## The Random-DAG Cost Theorem: Ancestry Law, Chain Growth, Cone Size, Typical Burst Cost, Growth Exponent, and Termination Closure

### Position

R58 is frozen: commits `61480f9` (A) / `1f0440d` (B) / `8b01a9f` (C-stamp), output manifest `d1219fac…` (full hash in R58_PROVENANCE_STAMP.json). Verdict `OD0_R58_PASS_M_SIBLING_TARGETS_ADJUDICATED`, `ALPHABET_SCOPE = COVERS_ALL_Γ`: m-sibling composite unique; outcome law perfectly correlated and setting-independent; alphabet = m factor copies, A12 additive; recost band [1, 13/11], qualitative class unchanged. H1, H2 spent; H3–H5 sealed.

Open results this round targets: growth rate (R53 `PARTIAL`, R55 bound |X_k| ≤ Ck/log log k); termination for m > Γ + H (R55 `SCOPED`, conditional on superlinear burst-cost growth).

### Adjudication notes to carry

1. **The object.** Each burst adds new pairs among a uniform s-subset of X (R52); marginally, each new object's parent pair is uniform over non-existing pairs (to be proven as T1). The realized ideal is a uniform-attachment two-parent random recursive DAG with the exact pair-uniformity law.
2. **The cost law (R53, frozen):** c(x) = c_first·chains(x) + 2·(recorded cone of x), chains({u,v}) = chains(u) + chains(v), recorded cone = Σ_{y ≺ x} chains(y) under THROUGH_OWN_LETTER (verify this identification exactly in T5).
3. **Two exact identities available:** the co-service identity (R55) and the cost-budget identity (R55: cumulative injected cost = backlog + served + voided − m·k).

---

# 0. Governing question

Derive exact expectation recursions and concentration bounds for the ancestry structure, chain counts, cone sizes, and first-use cost of a new object in the realized random DAG as functions of |X| = n; convert them through the cost-budget identity into two-sided bounds on |X_k|; and close the termination claim for m > Γ + H if typical burst cost is superlinear.

Zero new premises. No exponent may be fitted from readouts; every asymptotic statement carries explicit finite-n two-sided bounds or is labeled `CONJECTURE`. No external referent.

---

# 1. Locks (minimal)

Pin R58 stamp. Clean worktree at start and end. `BELL2_opened = false`. H3–H5 sentinels `parsed = false`. Exact arithmetic for recursions and certificates; asymptotic bounds with explicit constants; readouts labeled and seeded. Hash hygiene; stamp commit.

# 2. Commits

Commit A: this package verbatim; lock verification; targets T1–T8 frozen in wording. Commit B: proofs, certificates, readouts. Commit C: stamp.

---

# 3. Frozen inputs

R52 (uniform served subset; growth identity; per-object pair count n−2); R53 (chain recurrence; cost law; renewal theorem; U-growth for m < Γ); R55 (co-service identity; cost-budget identity; drain/band occupation bound; conditional termination theorem and its exact hypothesis); R58 (exact typing; recost); the exact distribution evolutions at K_max points; the recosted seeded trajectories.

---

# 4. Targets (frozen at Commit A)

**T1 (uniform pair law).** Conditional on a burst at a state with |X| = n and served count s, the set of new objects is the set of non-existing pairs among a uniform s-subset of X; consequently each new object's parent pair is marginally uniform over the n(n−1)/2 − (n−2) non-existing pairs, and two new objects in the same burst are siblings (share a parent) with an explicit probability. State exactly.

**T2 (ancestry law).** Let a_j(n) = P(the object born when |X| = j is a strict ancestor of the object born when |X| = n). Derive the exact recursion for a_j(n) under T1; give a closed form or two-sided bounds; and prove the asymptotic form a_j(n) = n/(n + j(j−1)) · (1 + o(1)) uniformly in the regime stated, or the correct replacement. Certify the exact recursion against the exact distribution evolutions for n ≤ K_max-reachable sizes and against the seeded trajectories (labeled).

**T3 (cone size).** E|cone(new at size n)| = Σ_j a_j(n); prove Θ(√n) with explicit constants (registered constant π/2 asymptotically), or the correct order. Give the second moment and a concentration statement.

**T4 (chain growth).** With T_n = Σ_{x ∈ X} chains(x): exact recursion for E[T_{n+1} | T_n, n] under T1 (the new object's chains are the sum of two marginally uniform draws, with the exact non-existing-pair correction); closed form for E[T_n] (Gamma-ratio or explicit product) and Θ(n²); E[chains(new at size n)] = Θ(n) with explicit constants; second moment and the growth of the coefficient of variation (registered: ~√log n).

**T5 (recorded cone).** Verify the identification recorded cone(x) = Σ_{y ≺ x} chains(y) against the frozen record identity (event, λ[0..ℓ]) exactly. Then E[recorded cone of new at size n] = Σ_j a_j(n)·E[chains(object born at j)] with the exact correlation correction stated; prove Θ(n log n) with explicit constants, or the correct order.

**T6 (typical burst cost).** E[c(new at size n)] = c_first·E[chains] + 2·E[recorded cone] = Θ(n log n) with explicit two-sided constants per (Γ, typing); variance bound; a statement of the form "the cost of the b-th burst exceeds κ·n_b log n_b for all sufficiently large b, almost surely" if obtainable (needed for T8), else the exact gap.

**T7 (growth exponent).** Using the cost-budget identity, the drain dynamics (forced service ≤ Γ + H per step; ≥ Γ(1 − D/(F+D)) when F > 0), mid-drain bursts, and T6: two-sided bounds c₁·√(k/log k) ≤ |X_k| ≤ c₂·√k (or the sharper form the argument yields) holding in expectation and with probability → 1, with explicit constants per registered point; supersede |X_k| ≤ Ck/log log k. If only one side closes, name the obstruction.

**T8 (termination closure).** State the exact hypothesis of the R55 conditional termination theorem; determine whether T6 (in its almost-sure form) satisfies it; if so, conclude: for m > Γ + H, the number of bursts is finite almost surely and give any bound on the terminal size; if not, state the precise remaining gap.

---

# 5. Certification

- T2, T4 recursions: exact match against the exact distribution evolutions at every K_max point (means and second moments), zero failures required.
- T3, T5, T6: exact recursions certified at small n; asymptotic bounds checked against recosted seeded trajectories at all registered points (labeled readout; a bound violation is a counterexample, a bound satisfied is not a proof).
- T7: the seeded |X_k| curves at 10², 10³, 10⁴ lie inside the two-sided bounds at every registered point (labeled).
- A readout table of a_j(n) from the trajectories (j × n grid) and the "bedrock fraction" (share of objects born before √n among ancestors of new objects), labeled.

---

# 6. Hostile controls (8)

1. any target altered after Commit A;
2. any exponent, constant, or order fitted from readouts; asymptotics without finite-n bounds not labeled `CONJECTURE`;
3. any modification of the cost law, record identity, TG1, or frozen roots;
4. any external referent;
5. any H1/H2 content used; any H3–H5 content read;
6. readouts cited as proof;
7. BELL2 opened;
8. any hand-produced hash; any placeholder.

---

# 7. Outputs (7 + stamp)

```text
OD0_R59_REPORT.md
OD0_R59_RESULTS.json
OD0_R59_COUNTEREXAMPLES.md                    (append-only)
R59_INPUT_LOCK.json                           (targets verbatim)
R59_RANDOM_DAG_LAWS.json                      (T1–T5: recursions, closed forms, bounds, certificates)
R59_COST_AND_GROWTH.json                      (T6–T8: cost bounds, growth bounds, termination status; readouts labeled)
R59_OUTPUT_MANIFEST.json
R59_PROVENANCE_STAMP.json                     (commit C)
```

Deterministic rerun: byte-identical JSON.

---

# 8. Verdict tree

Always, if targets were frozen at Commit A:

```text
OD0_R59_PASS_RANDOM_DAG_COST_TARGETS_ADJUDICATED
```

Components: `T1..T8 = {PROVEN | REFUTED(witness) | SCOPED(gap)}`; `CONE_ORDER = {√n | n | other}`; `COST_ORDER = {n log n | n² | other}`; `GROWTH_BOUNDS = {lower c₁·f(k); upper c₂·g(k)}`; `TERMINATION = {CLOSED | SCOPED}`.

## R60 rule

- T7 and T8 closed (or T7 two-sided) → R60 opens M7: the epoch dependence of lapse and clock rate in the throttled process — E[Φ² | state] = D/(F+D) as a function of maturity, the vacuum-service (clock-increment) rate per region, their behavior across E0 → E1 → asymptotic, with exact laws where the R59 orders give them (registered expectation: both decay logarithmically in |X| in the late regime) — frozen target-blind before any H3/H4 preregistration.
- CONE_ORDER = n (cost quadratic, exponent 1/3) → R60 still opens M7, on the corrected orders; the counterexample is recorded and the readout exponent is declared a transient.
- T2 REFUTED (the ancestry law fails) → R60 addresses the witness first; the DAG structure must be right before any lapse law is built on it.

---

# 9. Compact terminal return

```text
OD0-R59 OVERALL VERDICT:
COMMITS (A / B / C-stamp):
R58 STAMP PIN / WORKTREE / BELL2 / H3–H5 SENTINELS / HAND HASHES:
TARGETS FROZEN AT COMMIT A (yes/no):
T1 UNIFORM PAIR LAW (exact statement; sibling probability):
T2 ANCESTRY LAW (recursion; closed form/bounds; asymptotic form; certification):
T3 CONE SIZE (order; constant; concentration):
T4 CHAIN GROWTH (E[T_n] closed form; E[chains(new)] constants; CV growth):
T5 RECORDED CONE (identification verified; order; constants):
T6 TYPICAL COST (order; constants; a.s. form obtained?):
T7 GROWTH BOUNDS (lower; upper; constants per point; readouts inside?):
T8 TERMINATION (hypothesis stated; satisfied?; conclusion; terminal-size bound):
BEDROCK READOUT (labeled):
HOSTILE CONTROLS: N/8:
DETERMINISTIC RERUN:
OUTPUT MANIFEST SHA-256 (in stamp):
RECOMMENDED SINGLE R60 MOVE:
```

---

# Adjudicator's registered prediction (Claude, pre-run)

T1 PROVEN. T2: a_j(n) = n/(n + j(j−1))·(1+o(1)), from the logistic descendant-growth recursion k·φ′ = φ(1−φ) with φ(j) = 1/j; exact recursion certified. T3: cone Θ(√n), constant π/2. T4: E[T_n] ∝ n² (product Π(1 + 2/k) form), E[chains(new)] ≈ 2T_n/n = Θ(n), CV ~ √log n. T5: identification verified; recorded cone Θ(n log n) with constant ≈ C/2 from T4's C. T6: cost Θ(n log n); a.s. lower bound obtainable via concentration of the cone sum. T7: |X_k| = Θ(√(k/log k)) two-sided, readouts inside at all points; the earlier √k reading is the leading order. T8: hypothesis satisfied; termination CLOSED for m > Γ + H. This prediction constrains nothing in the run.
