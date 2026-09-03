# OD0-R51 Report - Minimal Throttle Premise Class

## Answer to the governing question

**The survivor is unique under the frozen minimality order: ADJ-V-S**, stated as premise TG1 (serviced vacuum maintenance is enablement-active, same-step, on both parents), with exact scope Gamma in 2..5. All four forced-token candidates deadlock at step 1 by an exact circularity (request needs record needs use needs enablement needs served request). Both record-gated candidates keep the unthrottled adjunction layer (SUPER_EXPONENTIAL, R50 saturation) and forfeit the envelope by modifying RO-D. ADJ-V-P survives with one extra persistent field (a vacuum mark absent from all source) and POLYNOMIAL growth - an exact quadratic bound correcting the prediction's EXPONENTIAL guess - and covers Gamma = 1; the frozen lexicographic order (C5, C6, C8) still gives the unique minimum to ADJ-V-S. Under TG1 the dynamics are LINEAR-bounded, non-degenerate (burst-drain: forced inflow of >= 22 requests per new object against Gamma <= 5 starves vacuum service, growth halts, backlog drains, service resumes), and coherence lifetime > 1 appears with probability 1/3 already at the smallest deadlock-free point. The R50 envelope survives verbatim for both survivors.

## Verdicts

- OD0_R51_PASS_THROTTLE_CLASS_FROZEN_AND_ADJUDICATED
- PRIMARY: THROTTLE_UNIQUE_MINIMAL(ADJ-V-S, TG1, scope Gamma 2..5)
- DEADLOCK_WITNESSES: all four T=F candidates: exact circularity (request needs record needs use needs enablement needs served request); ADJ-V-S at Gamma<=1: one token per step vs two-token same-step gate; ADJ-V-P at Gamma=0
- GROWTH_CLASSES: ADJ-V-S LINEAR (<= C(Gamma,2)/step); ADJ-V-P POLYNOMIAL (<= C(2+Gamma*k,2)+2, exact quadratic bound - corrects the prediction's EXPONENTIAL); REC-* and B0 SUPER_EXPONENTIAL
- SELECTOR_IDENTITY: DERIVED_GIVEN_TOKEN_DISTINGUISHABILITY
- V_IDENTIFICATION: NEW_IDENTIFICATION (carried inside the premise)

## Prediction vs outcome

Confirmed: S1 derived; S2 new identification; S3 no vacuum mark; S4 deterministic all-vacuum genesis (m=0); T=F circular deadlock; ADJ-V-S deadlock-free exactly for Gamma >= 2 with LINEAR growth, burst-drain non-degeneracy, lifetime witness probability 1/3; envelope survives for ADJ-*; verdict THROTTLE_UNIQUE_MINIMAL(ADJ-V-S). Corrected: ADJ-V-P's growth class is POLYNOMIAL (exact quadratic bound), not EXPONENTIAL; and K_max is resource-bounded per point (exact expansion budget) rather than uniformly >= 10 - per-point K_max and reasons are reported in the readout. The prediction constrained nothing.

## Compact terminal return

```text
OD0-R51 OVERALL VERDICT: OD0_R51_PASS_THROTTLE_CLASS_FROZEN_AND_ADJUDICATED + THROTTLE_UNIQUE_MINIMAL(ADJ-V-S, TG1, scope Gamma 2..5)
COMMITS (A / B): 28f50e5 / FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE
R50 PIN / WORKTREE / BELL2 / VALUES PARSED / HAND HASHES: PASS / CLEAN / false / 0 / 0
SELECTOR STATUS S1-S5: S1 DERIVED_GIVEN_TOKEN_DISTINGUISHABILITY; S2 V~X = NEW_IDENTIFICATION (kernel D-constancy silent on it); S3 no vacuum mark in source; S4 deterministic all-vacuum genesis at m=0 (exact table for all Gamma, m); S5 trivial joint region at constructor level ({a}:1, {b}:1, joint:|X|-2)
CANDIDATE CLASS (9): ADJ-V-S SURVIVOR(scope G>=2); ADJ-V-P SURVIVOR(+1 field, G>=1, POLYNOMIAL); ADJ-F-S/P DEADLOCK(circular); REC-V-S/P C2+C3 FAIL + envelope forfeited; REC-F-S/P record-layer deadlock; B0 control degenerate (R50)
DEADLOCK WITNESSES: T=F circularity exact; ADJ-V-S Gamma<=1 (one token/step vs two-token same-step gate); ADJ-V-P Gamma=0
GROWTH CLASSES: ADJ-V-S LINEAR (<=C(Gamma,2)/step); ADJ-V-P POLYNOMIAL (<=C(2+Gamma*k,2)+2); REC-*/B0 SUPER_EXPONENTIAL
LEDGER NON-DEGENERACY: burst-drain cycle; forced inflow >= 2 records x 11 = 22 per composite-parent event vs Gamma <= 5; P(S^V=0) rises then dips within K_max (exemplar G=2,m=0,H=0: 0, 154/325, ~0.62, ~0.657, ~0.656); long-run drain lemma stated
COHERENCE LIFETIME > 1: YES - probability exactly 1/3 at (Gamma=2, m=0, H=0), path witness recorded
FOOTPRINT / FIELDS / QUOTIENT DEP: ADJ-V-S {opportunity, V~X, D-override} / 0 / DIRECT; ADJ-V-P +vacuum-mark / 1 / INDIRECT; envelope survives for both
SURVIVORS AND MINIMALITY: {ADJ-V-S, ADJ-V-P}; (C5,C6,C8)-lex unique minimum = ADJ-V-S
SURVIVOR PREMISE (TG1): TG1 (throttle gating, stated not adopted): Serviced vacuum maintenance of an object is enablement-active, same-step - an enabled adjunction y={u,v} fires at step k+1 iff the standing vacuum tokens of both u and v were served in the step-k service realization; under the identification V ~ X (one standing vacuum token per existing object, D_k = |X_k|, regionally partitioned by smallest inherited prefix region). Inert alternative: service has no enablement effect.
K_MAX AND READOUT: per-point exact-enumeration bound; ADJ-V-S K_max 3-5 over 144 points, ADJ-V-P K_max 3-7 over 180 points; full exact trajectories (E|X|, P(S^V=0), shell, backlog) in R51_SURVIVOR_DYNAMICS_READOUT.json
HOSTILE CONTROLS: 8/8
DETERMINISTIC RERUN: IDENTICAL_BYTE_FOR_BYTE
OUTPUT MANIFEST SHA-256: FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE
RECOMMENDED SINGLE R52 MOVE: Per the verdict tree: R52 derives the intrinsic epoch-observable algebra on the exact throttled process, conditional on the stated premises (CO1, RO1, TG1, V~X), on state-defined observables only - the R50 envelope delimits the quotient-invariant domain; the natural first objects are the unresolved-shell trajectory, the burst-drain cycle structure of P(S^V=0), the marked/served filtration, and the lapse process - with no threshold, label, or historical comparison. This is where the maturation filtration (M2-M3) begins.
```
