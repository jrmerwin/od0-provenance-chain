# OD0-R51 CLAUDE CODE PACKAGE v0.1

## Minimal Throttle Premise Class: Candidate Freeze, Deadlock / Growth / Degeneracy Adjudication, and Source Status of the Service Selector

### Position

R50 is frozen: commits `09d446d` (A) / `4fa6555` (B), output manifest `c6a6917f…` (full hash from R50_OUTPUT_MANIFEST.json, never retyped). Verdict `OD0_R50_PASS_BUNDLING_ENVELOPE_AND_SYNCHRONOUS_FAMILY_CHARACTERIZED`: T_sat = depth filtration, T_dag = dag_size filtration; record poset invariant under prefix-canonical identity `(event, λ[0..ℓ])`; sole quotient-dependence entry point quotient → pool → service → A13R clock → setting; cumulative ledger not invariant; lifetime ≡ 1; `NOT_SEPARATED_BY_SOURCE`; saturation κ = 2 at all 1,296 registered genesis points, both members (F₂ ≥ 44 > Γ_max = 5); registry arrow exact (173/173, 137/137); Γ, D, H genesis-undeclared and kernel-constant; m external; no source couples capacity or enablement to rendered structure.

### Adjudication notes to carry

1. **Envelope carry-over.** Any throttle gating *adjunction* leaves RO-D untouched, so the R50 envelope (record poset, fixed-setting outcome law, entry point) holds verbatim. Any throttle gating *records* modifies RO-D and forfeits the envelope. Record this distinction as criterion C5 below.
2. **The selector.** The frozen system contains exactly one source-defined random selector: the service realization σ (uniform over complete request–slot matchings, CD2R). A throttle is an opportunity law whose selector is σ. This makes the candidate class enumerable rather than open.
3. **Frontier shell.** Under a throttle, the R50 "shell coherent at the cap" corollary becomes dynamical: the unresolved sector is the set of objects not yet used as parents. Report it as a readout; it defines nothing.

---

# 0. Governing question

Among opportunity laws whose only selector is the frozen service realization, which gate an event class on a served token, are binary and parameter-free, and are stated as one A13R0/RO1-style activity premise: which are deadlock-free from genesis, non-explosive, and non-degenerate over the registered ledger domain — and is the survivor unique under minimality of frozen-structure footprint?

Zero-or-one-premise round. The survivor's premise is *stated* as a conditional (like RO1); it is not adopted as source law. No physical time, no maturity threshold, no cosmology or particle referent.

---

# 1. Locks (minimal)

Pin R50 output manifest hash and commits (transitively R49/R48/R47). Clean worktree at start and end. `BELL2_opened = false`. Historical numerical content never parsed. Exact arithmetic. Hash hygiene rule in force: every hash copied from tool output.

# 2. Commits

Commit A: this package verbatim; lock verification; the candidate class of Section 5 and the criteria of Section 6 recorded before any test. Commit B: everything else.

---

# 3. Frozen inputs

CD0 (En(X) = {y : Par(y) ⊆ X}, Thm 1); CD1I (append, records, clock); CD2R (finite-set ledger V/C/M/J/P/H, service-equivalence premise, matching groupoid and its uniform invariant measure, hypergeometric pushforward, population/relief rules); A13R and A13R0; UEQ0 (n = min(Γ, F + D), S^F/S^V, lapse Φ² = S^V/V⁰); R41 RRP1; R44 (G⁻, G⁺); R49 (RO1/RO-D, CO1, SV-pool); R50 (envelope, saturation scan, registry arrow, capacity census).

---

# 4. Part 1 — Source status of the selector ingredients (zero premise)

Classify each from source, before any candidate is tested:

- **S1 per-token service identity.** The CD2R matching groupoid is uniform over complete matchings of *identified* requests to slots. Does the frozen realization σ retain which vacuum tokens were served (identity), or only the count S^V? If the groupoid identifies tokens and only the kernel forgets them, classify per-token identity as `DERIVED_GIVEN_TOKEN_DISTINGUISHABILITY`; otherwise `UNDECLARED`.
- **S2 vacuum-token semantics.** Does any active source state what the vacuum set V is a set *of* — existing objects, regions, abstract maintenance units? Classify the identification V ≅ X (one standing token per existing object, D = |X|, regionally partitioned by prefix region) as `SOURCE_SEMANTICS`, `MANUSCRIPT_ONLY`, or `NEW_IDENTIFICATION`. The R50 finding that D is kernel-constant is a fixed-region property; state whether it forbids or is silent on D = |X|.
- **S3 RRP1 scope.** RRP1 marks served *A12 forced* requests. Do served vacuum tokens receive any persistent mark in any active source? Expected: no. A vacuum mark is then a new persistent field; note which candidates need it.
- **S4 genesis service.** At step 0 with X₀ = {a, b}: are the primitives tokens (D₀ = 2), and with F₀ = 0 is n₀ = min(Γ, 2) served deterministically all-vacuum? State exactly.
- **S5 regionality.** Tokens of an object belong to its prefix region; state the regional pool partition of D under V ≅ X.

---

# 5. Part 2 — Frozen throttle candidate class

Every candidate is an opportunity law "events of class G fire at step k+1 iff their gating condition, evaluated on the frozen service realization σ_k (and, for persistent variants, on a mark set), holds." Enumerate the class by three binary axes and freeze all eight plus the baseline:

- **Gate G ∈ {ADJ, REC}:** ADJ gates the adjunction y = {u, v}; REC gates the RO-D record fired by a downstream use (adjunction free).
- **Token T ∈ {V, F}:** V = the object's own standing vacuum token; F = a forced A12 request derived from a record on the object's lineage.
- **Timing M ∈ {S, P}:** S = same-step (gate holds iff the token was served at step k; no persistent field); P = persistent (gate holds iff the token has been served at any step ≤ k; requires a mark).

For ADJ candidates the condition applies to *both* parents u and v (ADJ-V-S: both tokens served at step k; ADJ-V-P: both marked). For REC candidates it applies to the *child* whose downstream use would fire the record.

Baseline **B0**: CO1 alone (T_sat/T_dag), rejected by R50 as degenerate; retained as control.

Write each candidate's premise statement in A13R0 form ("serviced vacuum maintenance of an object is enablement-active: …"), its inert alternative, and the exact frozen object it modifies.

---

# 6. Part 3 — Frozen adjudication criteria

- **C1 deadlock-freedom.** From genesis, over every registered (Γ, D₀, m, H) point: does the process leave X₀ with positive probability, and does it reach |X| ≥ 5 with probability 1 in finitely many steps? Report the smallest Γ for which each candidate is deadlock-free. Expected: all T = F candidates deadlock at step 1 (record needs use, use needs enablement, enablement needs a served forced request, which needs a record); give the circular witness exactly.
- **C2 growth class.** Exact recurrence bounds on |X_{k+1}| − |X_k| in terms of S^V_k, Γ, |X_k|: classify as SUPER_EXPONENTIAL / EXPONENTIAL / POLYNOMIAL / LINEAR (per-step increment bounded by a function of Γ alone).
- **C3 ledger non-degeneracy.** Over the registered domain and k ≤ K_max: is P(S^V_k = 0) bounded away from 1 in the long run, i.e., is lapse not identically 0 (nor identically 1)? Exact finite-state analysis for small Γ; report the forced-inflow-per-new-object constant (records per adjunction × requests per record) against Γ.
- **C4 unresolved persistence.** Is coherence lifetime > 1 achievable (an object can remain un-built-upon for several steps)? Exact for small Γ.
- **C5 frozen-structure footprint.** Which frozen objects does the candidate modify or extend: En(X) (CD0, DIRECT_NATIVE), RO-D (DERIVED_GIVEN_RO1), RRP1 (premise), D's kernel constancy (fixed-region), V-identification (S2 result)? Whether the R50 envelope survives verbatim.
- **C6 new persistent fields.** Count (0 for S variants if S1 is derived; ≥ 1 for P variants).
- **C7 parameters.** Must be 0.
- **C8 quotient dependence.** Whether the gate references the step quotient directly (same-step conditions do) and what the R50 envelope says survives.

A candidate is a **survivor** iff it passes C1 on some registered Γ range, is not SUPER_EXPONENTIAL under C2, passes C3 and C4, and has C7 = 0. Scope restrictions from C1 (e.g., deadlock-free only for Γ ≥ 2) are reported as scope, not as failure, with the exact witness.

---

# 7. Part 4 — Exact small-Γ dynamics of survivors (readout only)

For each survivor and each registered genesis point with Γ ≤ 5, compute exactly for k ≤ K_max: |X_k|; S^V_k, S^F_k distributions; backlog B_k; lapse Φ_k support and mean; unresolved-shell size (objects never yet used as parents); records and requests per step; coherence-lifetime distribution; regional split. Report K_max and its reason — expected far beyond 3 since growth is bounded. No epoch label, no threshold.

---

# 8. Part 5 — Minimality and uniqueness

Among survivors, order by (C5 footprint, C6 fields, C8 dependence). If a unique minimum exists, return it with its premise statement in A13R0 form. If two survivors differ only in gated sector (ADJ vs REC), return the two-member class and the exact structure invariant across both (the record poset survives in one and not the other; state what still does). Select nothing beyond the ordering.

---

# 9. Hostile controls (8)

1. selecting a candidate by preference or by dynamics readout rather than by C1–C8;
2. tuning or singling out Γ; treating a Γ ≥ 2 scope condition as a physical claim;
3. any external referent (cosmology, particles, inflation, time) in any output;
4. historical rounds identified with steps; any historical numeric;
5. a candidate with a hidden parameter (weights, thresholds, rates);
6. dynamics readouts used to define an epoch or basin;
7. modification of frozen roots; BELL2 opened;
8. any hand-produced hash.

---

# 10. Outputs (8)

```text
OD0_R51_REPORT.md
OD0_R51_RESULTS.json
OD0_R51_COUNTEREXAMPLES.md                    (append-only; deadlock witnesses, explosion witnesses)
R51_INPUT_LOCK.json
R51_SELECTOR_SOURCE_STATUS.json               (Part 1, S1–S5)
R51_THROTTLE_CLASS_ADJUDICATION.json          (Parts 2–3: 9 candidates × C1–C8, witnesses)
R51_SURVIVOR_DYNAMICS_READOUT.json            (Part 4)
R51_OUTPUT_MANIFEST.json
```

Deterministic rerun: byte-identical JSON.

---

# 11. Verdict tree

Always, if the class and criteria were frozen at Commit A:

```text
OD0_R51_PASS_THROTTLE_CLASS_FROZEN_AND_ADJUDICATED
```

Primary (one):

- `THROTTLE_UNIQUE_MINIMAL(candidate, premise, scope)` — R52 derives the intrinsic epoch-observable algebra on the exact throttled process, conditional on the stated premise; this is where the maturation filtration (M2–M3) begins, on state-defined observables only.
- `THROTTLE_TWO_MEMBER_CLASS(ADJ-*, REC-*)` — R52 derives the premise-invariant envelope across both before any epoch work.
- `THROTTLE_NO_SURVIVOR` — R52 widens the class by exactly one axis (e.g., gates on relief or on clock residue), never by a parameter.

Secondary: `SELECTOR_IDENTITY = {DERIVED | UNDECLARED}`; `V_IDENTIFICATION = {SOURCE | MANUSCRIPT | NEW}`; `DEADLOCK_WITNESSES = {…}`; `GROWTH_CLASSES = {…}`; `K_MAX`.

---

# 12. Compact terminal return

```text
OD0-R51 OVERALL VERDICT:
COMMITS (A / B):
R50 PIN / WORKTREE / BELL2 / VALUES PARSED / HAND HASHES:
SELECTOR STATUS S1–S5:
CANDIDATE CLASS FROZEN (9) — per candidate C1..C8 summary:
DEADLOCK WITNESSES (T=F circularity; ADJ-V-S Γ=1 if present):
GROWTH CLASSES:
LEDGER NON-DEGENERACY (per survivor: long-run P(S^V=0) range, forced-inflow constant vs Γ):
COHERENCE LIFETIME > 1 ACHIEVABLE:
FOOTPRINT / NEW FIELDS / QUOTIENT DEPENDENCE per survivor:
SURVIVORS AND MINIMALITY ORDER:
SURVIVOR PREMISE STATEMENT (A13R0 form) AND SCOPE:
K_MAX AND DYNAMICS READOUT SUMMARY (|X_k|, lapse, shell size):
HOSTILE CONTROLS: N/8:
DETERMINISTIC RERUN:
OUTPUT MANIFEST SHA-256:
RECOMMENDED SINGLE R52 MOVE:
```

---

# Adjudicator's registered prediction (Claude, pre-run)

S1 derived from the matching groupoid; S2 `MANUSCRIPT_ONLY` for "maintenance of existing structure," so V ≅ X is a new identification carried inside the premise; S3 no vacuum mark exists; S4 deterministic all-vacuum genesis service for Γ ≥ 2. All four T = F candidates deadlock at step 1 with the circular witness. ADJ-V-S: deadlock-free for Γ ≥ 2, deadlocked at Γ = 1 (a distinction needs two served tokens in one step); growth LINEAR (increment ≤ C(S^V, 2) ≤ C(Γ, 2)); non-degenerate with self-limiting bursts — forced inflow ≈ 24 requests per new object against Γ ≤ 5 starves vacuum, backlog drains, growth resumes; lifetime > 1 achievable; footprint = opportunity only, RO-D untouched, envelope survives; 0 new fields; quotient-dependent. ADJ-V-P: deadlock-free for Γ ≥ 1; EXPONENTIAL; needs a vacuum mark. REC-V-*: adjunction stays SUPER_EXPONENTIAL; envelope forfeited. Verdict `THROTTLE_UNIQUE_MINIMAL(ADJ-V-S, scope Γ ≥ 2)`, K_max ≥ 10. This prediction constrains nothing in the run.
