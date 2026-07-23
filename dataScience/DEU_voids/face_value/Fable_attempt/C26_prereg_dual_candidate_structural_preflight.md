# C26 Preregistration — Dual-Candidate Structural Preflight (Relief-Scar Family Adjudication)

**Status:** DRAFT FOR FREEZE. This document becomes binding when committed with a SHA-256 hash and timestamp. Items marked **[FREEZE-POINT]** require numeric ratification by the PI before hashing; every other clause is proposed as final.

**Campaign:** DEU Work–Energy, round C26 (successor to C25).

**Rule inheritance:** This round operates under the standing methodology of the C-campaign: frozen preregistration before any run; amendments only with the prior failure and its diagnosis on record, and only pre-adjudication; equal-prominence reporting; instruments are engines (any instrumented variant must pass the bit-exact certification panel before its data are used); null scope is exact.

---

## 1. Question

Can either of two structurally distinct relief-scar candidates — neither of which is the closed C24 first-relief-survivor candidate — be **supported, matched, and cleanly controlled** on fresh foams, without reading any demand, service, or work outcome?

This is a preflight. It measures structural eligibility only. No effect is opened.

## 2. Why this round exists

C24–C25 closed the candidate "first relief survivor + d/ℓ\* < 16 + burst-minus-fine contrast" under its frozen definition. The C25 record explicitly requires that future work use a structurally distinct candidate rather than relaxed gates. This round adjudicates the two registered distinct candidates and carries the family-level stopping rule (§9): if both fail structurally, the relief-scar family closes permanently.

## 3. Formation protocol (frozen by reference)

Formation uses the certified C13–C15 instrument without modification:

- Equal-metric burst at total action 0.50, temporal subdivision at the certified relief-separation boundary N = 240, followed by source-off evolution.
- Source-off clearance certification per C15: all backlogs must reach the registered zero-hold (128 epochs) before the preflight observation window opens; seeds failing clearance are recorded and replaced from the ordered reserve (§5), with the replacement logged.
- Exact face-scale metric per C18: all metric-weighted quantities in this round use the exact algebraic representation (A + B√3)/3^N; floor-quantized values are diagnostic only.

No engine dynamics are modified for this round. Any instrumentation added to log lineage identity is pure reads and must pass the ten-run bit-exact certification panel before its output is used.

## 4. Candidate definitions

Both candidates are defined over the **formation phase**: the interval from burst onset to the completion of source-off clearance certification.

### Candidate A — Final-relief survivor

Let R₁, …, R_K be the relief events executed during the formation phase, in engine order. Candidate A is the material lineage that survives the **final** relief event R_K:

1. Enumerate the faces removed by R_K and the faces incident to the collapse locus that persist immediately after R_K executes.
2. The candidate lineage is the persistent material lineage (per the C19 lineage-tracking definition) containing those surviving incident faces.
3. If R_K leaves more than one disjoint surviving lineage at its locus, apply tie-breaks (§4.3).
4. If K = 0 (a seed whose formation produces no relief), Candidate A is undefined for that seed; the seed is recorded as `A_UNDEFINED_NO_RELIEF` and counts against Candidate A's support denominator (it is not replaced).

### Candidate B — Maximum-reuse lineage

Over the same formation phase, for every persistent material lineage created by a relief event, count its **relief participation**: the number of distinct later relief events R_j (j > creation event) whose executed collapse set intersects the lineage. Candidate B is the lineage with the maximum relief participation count.

If the maximum participation count is 0 in a given seed (no lineage is ever reused), Candidate B is undefined for that seed; recorded as `B_UNDEFINED_NO_REUSE`, counted against B's support denominator, not replaced.

A and B may coincide in a given seed. Coincidence is recorded per seed and does not disqualify either candidate; if both classes pass their gates only through seeds where A = B, the classification must state that the two classes were not structurally separated on this cohort (§8, outcome `...NOT_SEPARATED`).

### 4.3 Deterministic tie-breaks (both candidates)

Applied in order until unique; all inputs are pre-outcome fields:

1. Larger exact metric extent of the lineage at the tie-evaluation epoch (sum of exact face-scale weights of member faces).
2. Earlier lineage creation epoch.
3. Greater maximum refinement depth among member faces.
4. Lowest immutable token/lineage identifier (engine creation order).

Tie-break 4 is total; the selection is therefore deterministic given a seed.

## 5. Cohorts and seed policy

- **Fresh seeds only.** The C24 cohort (and any seed used in C13–C25 effect or support rounds) is excluded.
- **Ordered reserve policy** per the C23 template: a frozen ordered list of **[FREEZE-POINT: 30]** candidate seeds is committed with this document. Seeds are consumed in order. A seed is replaced (next in reserve) only for registered pre-outcome disqualifications: clearance-certification failure (§3) or engine fault. Candidate-undefined seeds (§4) are **not** replaced.
- Target cohort: **[FREEZE-POINT: 10]** seeds completing formation + clearance, split by frozen assignment into **discovery (5)** and **validation (5)** before any preflight observable is computed. The split is by seed-list position (odd positions discovery, even validation), fixed here.

## 6. Firewall (C23 template)

The eligibility/selection function — including candidate identification, tie-breaks, and control matching — receives **only** the following whitelisted pre-outcome fields:

**Whitelist**
- Lineage identity, membership, creation epoch, and token identifiers
- Relief event log: epochs, loci, executed collapse sets (identity and timing only)
- Face types (S/I/G), refinement depths, exact face-scale weights
- Metric positions and distances (d/ℓ\* to any locus)
- Persistence flags (lineage existence at specified epochs)
- Relief participation counts (event-intersection counts, §4)
- Control-candidate availability: existence, type composition, depth composition, and timing of prospective pseudo-loci
- Cleanliness flags: presence/absence of relief events within a control's exclusion window
- Local support counts: number of frustrated-face epochs within the support radius of a locus (count of epochs on which ≥1 frustrated face lies in the support region — availability only, no demand magnitudes)

**Blacklist (hard, no code path)**
- Standing demand magnitudes (any timing)
- Served work, service rates, or per-face service histories
- Backlog magnitudes and relief output sizes n_voided
- Any field derived from the above
- Any observable of the C9 field pipeline (J_cut, Ω, C1 profiles)

The firewall is structural, not procedural: the selection code's input schema must contain no blacklisted column, mirroring the C23 implementation.

## 7. Preflight observables (per seed, per candidate)

All computed after selection is complete, from whitelisted fields only:

1. **P — Persistence.** Candidate lineage exists with ≥1 member face at the end of the observation window: formation completion + **[FREEZE-POINT: 240]** source-off epochs.
2. **U — Reuse.** Candidate's relief participation count over the formation phase (recorded; gated only for B by definition U ≥ 1).
3. **M — Exact-type control availability.** Within a forward search window of **[FREEZE-POINT: 240]** epochs, a pseudo-locus exists whose face-type composition matches the candidate's **exactly** (categorical, per the C20 lesson — no 80% gate) and whose depth composition matches within **[FREEZE-POINT: ±1 depth level per face, order-matched]**.
4. **S — Local support.** Both candidate locus and matched control satisfy ≥ **[FREEZE-POINT: 90]** frustrated-face epochs within the support radius **[FREEZE-POINT: d/ℓ\* < 16, retained from C24 for comparability — ratify or revise before freeze; post-hoc revision is prohibited]**.
5. **C — Cleanliness.** Matched control is relief-free within an exclusion window of **[FREEZE-POINT: ±64]** epochs around the alignment time.

## 8. Gates and registered classifications

A candidate class is **ELIGIBLE** iff, counting only seeds where the candidate is defined:

- **G1 (persistence):** P holds in ≥ **[FREEZE-POINT: 4/5]** discovery seeds AND ≥ **[FREEZE-POINT: 4/5]** validation seeds.
- **G2 (matched control):** M holds in ≥ 4/5 and ≥ 4/5.
- **G3 (support + cleanliness):** S and C jointly hold in ≥ **[FREEZE-POINT: 3/5]** and ≥ 3/5.
- **G4 (definedness):** the candidate is defined (§4) in ≥ **[FREEZE-POINT: 4/5]** of each cohort half.

Registered classifications (exactly one fires):

- `C26_PREFLIGHT_A_ELIGIBLE__B_INELIGIBLE`
- `C26_PREFLIGHT_B_ELIGIBLE__A_INELIGIBLE`
- `C26_PREFLIGHT_BOTH_ELIGIBLE`
- `C26_PREFLIGHT_BOTH_ELIGIBLE__NOT_SEPARATED` (both pass, but only via A=B seeds)
- `C26_PREFLIGHT_BOTH_INELIGIBLE__SCAR_FAMILY_CLOSED`

## 9. Stopping rule (binding)

If `C26_PREFLIGHT_BOTH_INELIGIBLE__SCAR_FAMILY_CLOSED` fires, the relief-scar candidate family is **permanently closed**: no further scar-lineage candidate (first-relief, final-relief, max-reuse, or any other lineage-defined scar object) may be proposed as a λ_X source without a new, independently motivated formation mechanism that is itself preregistered. No effect round in this family may be launched. The campaign pivots fully to the native constraint-to-load compiler track.

This clause may not be amended after data exist. It is the point of the round.

## 10. What this round does not do

- It does not open any demand, service, or work effect. A candidate passing all gates is *eligible for* a future effect round (which requires its own prereg, reachability audit, and outcome-blind cohorts); it is not thereby confirmed as a source.
- It does not revisit, extend, or reinterpret the closed C24 candidate.
- It does not test the boundary-demand compiler candidate (that is instrument B0, separately registered).
- No physics referents. All claims are internal to the DEU.

## 11. Amendment policy

Amendments are permitted only before adjudication, only with a registered failure and diagnosis on record, and never to §9. Threshold changes after seeing any preflight observable are prohibited.

---

*Freeze checklist for the PI: ratify all [FREEZE-POINT] values, commit the ordered seed list, hash this document + seed list + selection-code schema, record timestamp, then launch formation.*
