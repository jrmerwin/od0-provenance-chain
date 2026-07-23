# B0 Instrument Specification — Depth-Contrast Boundary Demand: Stock vs. Rate

**Status:** DRAFT FOR REGISTRATION. Read-only instrument round. Items marked **[FREEZE-POINT]** require PI ratification before the spec is hashed.

**Campaign:** DEU Work–Energy, compiler track. Designation B0 (first boundary-demand round), parallel to C26 and independent of its outcome.

---

## 1. Question

Does the depth-contrast boundary of a legally formed, topologically pinned refined pocket generate a **serviceable metric load rate** — persistent served work per epoch above vacuum baseline — or only a **standing stock** of frustrated demand that pools without conversion to service?

Equivalently: is the demand-trap structure a candidate λ_X source, or is it (as the gravity campaign's boundary-freezing results would permit) a pure sink whose demand never clears the scheduler?

This round answers the stock/rate question only. It does not certify a compiler.

## 2. Motivation and candidate logic

The compiler eligibility criteria require λ_X to be derived from an exact native unsatisfied constraint with: vacuum zero, refinement covariance, persistence, additivity, and no tunable amplitude. The depth-contrast boundary is the strongest untested candidate because:

- The equal-depth flip restriction makes a refined pocket's interface flip-frozen: degree regulation cannot rewire across the depth mismatch, so frustration generated at the interface cannot be relieved by the vacuum's ordinary channel.
- The boundary-freezing results (matter pocket as combinatorial demand trap, independently confirmed three ways in the gravity campaign) establish that demand pools inward at such interfaces.
- The pocket is produced legally by the certified C13–C15 formation instrument; nothing about the candidate is inserted by hand.

The known risk, stated up front: pooled demand may be *unserviceable*. A standing stock with zero service is a real structure but fails the rate requirement — λ is an extensive input/served rate (per the C-campaign's stock/rate/field distinction), not a pool. Both branches of this round are informative; neither is a failure of the instrument.

## 3. Object definitions

### 3.1 Pocket

The refined region produced by the certified formation protocol (C13–C15: equal-metric burst, action 0.50, N = 240 subdivision, source-off clearance certified per C15). The pocket face set at epoch t is defined by refinement depth: all faces with depth k ≥ k_vac + **[FREEZE-POINT: 2]**, where k_vac is the modal vacuum depth at the same metric radius, restricted to the connected component containing the burst locus.

### 3.2 Boundary set B(t)

The depth-contrast interface: every face f such that f shares an edge with a face g where |k_f − k_g| ≥ 1 and exactly one of {f, g} belongs to the pocket set. B(t) is recomputed each epoch from topology and depth alone (whitelist-clean; no demand fields enter the definition).

### 3.3 Vacuum baseline region V(t)

A matched control annulus in a **separate, pocket-free foam** from the same seed family: same metric radial band as B(t)'s shell occupancy, same epoch, formation replaced by the certified 30-way relief-free control schedule (C13). Matching is on metric radius and epoch only — fixed before any demand field is read.

## 4. Instrument requirements

- **Pure reads only.** The B0 variant adds no dynamics, no random draws, no state. It logs per-epoch, per-face-set aggregates defined in §5.
- **Certification:** before any B0 data are used, the variant must reproduce, bit-exactly, the standing certification panel (ten archived runs spanning load regimes, outcome classes, and capacity-lottery extremes, across all shared scalar observables), per the instruments-are-engines rule. Certification scope is scalar pipeline observables; geometry-sector claims are out of scope for this variant.
- **Exact algebra:** all metric-weighted sums use the C18 exact representation (A + B√3)/3^N. Floating mirrors are logged for cross-check at the certified ~10⁻¹³ agreement level but are non-primary.
- **Timing declaration (binding):** demand is read **pre-service** (the declared-measure rule; the C17/C16 proxy failure and the Section-6.1 instrument-timing failure of the unification paper are the controlling precedents). Service is attributed at execution. Epoch-end state is logged separately and never substituted for either.

## 5. Observables (per epoch, per region R ∈ {B, V})

1. **D_R(t)** — exact standing frustrated demand: sum of exact face-scale weights of frustrated faces in R at pre-service timing.
2. **S_R(t)** — exact served work: sum of exact weights of operations executed in R during epoch t, by kind (split / flip / relief-voided), attributed at execution.
3. **A_R(t)** — exact metric area of R (normalization; also the refinement-covariance check denominator).
4. **N_R(t)** — face count of R (diagnostic only; never a primary variable, per C0).
5. **Persistence trace** — B(t) nonempty flag and exact metric extent of the pocket, per epoch.

Derived (analysis stage, definitions frozen here):
- Demand density d_R(t) = D_R(t)/A_R(t); service density s_R(t) = S_R(t)/A_R(t).
- Boundary excesses ΔD(t) = d_B(t) − d_V(t), ΔS(t) = s_B(t) − s_V(t).

## 6. Run plan

- **Seeds:** **[FREEZE-POINT: 10]** fresh seeds (disjoint from C26's reserve list and from all prior C-campaign cohorts), ordered reserve of **[FREEZE-POINT: 20]**, replacement only for clearance failure or engine fault.
- **Window:** formation + clearance, then a quiet source-off observation window of **[FREEZE-POINT: 480]** epochs (double the C15-certified 240, to power the stationarity split below).
- **Analysis windows:** early half W₁ and late half W₂ of the observation window, fixed here.

## 7. Decision rules

All gates evaluate the late window W₂ unless stated; stationarity compares W₁ vs W₂.

- **G0 (excess demand exists):** median over seeds of time-mean ΔD > 0 with **[FREEZE-POINT: ≥ 8/10]** seeds individually positive. If G0 fails → NULL branch.
- **G1 (persistence):** pocket and boundary persist (nonempty B(t)) through W₂ in ≥ 8/10 seeds.
- **G2 (rate):** median time-mean ΔS > 0 with ≥ **[FREEZE-POINT: 7/10]** seeds individually positive.
- **G3 (stationarity):** per-seed |mean_{W₂}(ΔS) − mean_{W₁}(ΔS)| / mean_{W₁∪W₂}(ΔS) ≤ **[FREEZE-POINT: 0.5]** in the seeds counted for G2, and the W₂ trend slope of ΔS is not significantly negative at the registered level **[FREEZE-POINT: one-sided 0.05, run-level bootstrap, 2000 resamples, fixed rng seed]**.
- **G4 (stock discrimination):** the demand stock behavior is classified per seed: POOLING if ΔD has significantly positive W₂ slope; STEADY if slope indistinguishable from zero; DRAINING if negative. Recorded regardless of branch.

## 8. Registered classifications (exactly one fires)

- `B0_BOUNDARY_RATE_CERTIFIED__COMPILER_CANDIDATE_OPEN` — G0, G1, G2, G3 all pass. The boundary generates a persistent, stationary, served metric load above vacuum baseline. λ_dress := time-mean ΔS·A_B (exact units) becomes the registered candidate rate for the next round. **This does not certify a compiler**; it licenses B1 (additivity + vacuum-zero formalization + refinement-covariance audit) and, conditional on B1, the C9 same-object field composition test Ω_scar(r) = λ_dress/C1(r).
- `B0_BOUNDARY_STOCK_ONLY__RATE_ABSENT` — G0 and G1 pass, G2 or G3 fails. The boundary is a demand trap: real standing stock, no serviceable rate. The depth-contrast boundary is closed **as a λ_X source under this formation mechanism and observable set**; the null scope is exactly that. The stock result is retained as a positive structural finding consistent with the demand-sink picture.
- `B0_NO_BOUNDARY_EXCESS` — G0 fails. The flip-frozen interface does not even carry excess standing demand; the candidate's motivating premise fails in the source-off state. Closed at that scope.
- `B0_POCKET_NOT_PERSISTENT` — G1 fails. The formation product does not survive as a pinned structure over the window; the candidate is not testable by this instrument and the failure is a formation finding, not a demand finding.

## 9. Eligibility mapping (for the compiler criteria — recorded, not gated here)

| Criterion | Where addressed |
|---|---|
| Vacuum zero | ΔD, ΔS are baseline-subtracted by construction; formal vacuum-zero proof deferred to B1 |
| Refinement covariance | Exact face-scale algebra + area normalization; covariance audit (representation-only subdivision test) deferred to B1 |
| Persistence | G1 + G3 |
| Additivity | Not tested in B0 (single pocket); two-pocket additivity is B1 |
| No tunable amplitude | The definition contains no gain: B(t) from topology, weights from depth, rates from the ledger |

## 10. What this round does not do

- Does not modify engine dynamics or the random stream.
- Does not read or touch any C26 cohort or observable.
- Does not open the C9 field pipeline for this object.
- Does not assign physical units; no physics referents in any claim.
- A RATE result is not a mass, an energy, or a particle; it is an internal candidate rate pending B1.

## 11. Amendment policy

Standard campaign rule: pre-adjudication only, prior failure + diagnosis on record. The classification set in §8 may not be extended after data exist.

---

*Registration checklist: ratify [FREEZE-POINT] values, commit seed lists, hash spec + instrument-variant patcher + certification panel manifest, record timestamp. Certification (10/10 bit-exact) must complete before the first B0 observation run.*
