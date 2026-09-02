# OD0-R49 Report - Minimum Global Opportunity Law: Candidate Freeze and Forced / One-Premise / Choice Classification

## Governing question and answer

> What is the smallest set of source-derivable properties that determine, at each global step, which enabled adjunctions occur, whether and which A10 records occur, and when service rounds occur - and is the resulting global transition unique?

**The record and service layers close; the adjunction layer is nonunique-canonical - and the nonuniqueness is physical.** Given the two A13R0-pattern activity premises (CO1, RO1), the record law is uniquely RO-D (maximal-supported-scope prefix records; RO-A is refuted by the frozen invariant append; the setting residual is forced by the lineage's A13R clock state, not free), and the service law is uniquely SV-pool (interleaving is order-sensitive by an exact 2/3-vs-1/2 witness). But the frozen choice-free class contains TWO canonical adjunction laws - full saturation T_sat and next-grade saturation T_dag under the single source stratification grading dag_size - which provably differ (smallest witnesses: two 4-object states; genesis divergence at k=3). Because pooled service is non-compositional across pools, the step-bundling difference propagates to the ledger/clock trajectories: it is not a gauge choice. A second independent blocker is recorded: Lambda_0 is undeclared in source.

## Verdicts

- OD0_R49_PASS_OPPORTUNITY_CANDIDATE_CLASS_FROZEN_AND_CLASSIFIED
- PRIMARY: OPP_NONUNIQUE_CANONICAL
- COMMUTING_DIAGRAM: NOT_REACHED (nonunique + Lambda_0 undeclared)
- RECORD_RULE: RO-A refuted; RO-D unique (residual: setting - FORCED_BY_STATE_GIVEN_A13R, not free; query determined); RO-0 not excluded -> RO1 stated
- SERVICE_RULE: SV-pool unique; SV-int PREMISE_REQUIRING_SELECTION (exact 2/3 vs 1/2 witness)

Justification: The frozen choice-free class given CO1 contains exactly two inequivalent canonical laws (T_sat, T_dag), with exhaustive smallest distinguishing states (two 4-object ideals) and genesis-trajectory divergence at k=3. The record and service layers are each unique (RO-D given RO1; SV-pool), so the entire residual nonuniqueness of the global transition is the adjunction step-quotient - and it is physical, because pooled service is non-compositional across pools.

## Registered prediction vs outcome

The registered prediction (T_sat unique nontrivial choice-free law; overall OPP_ONE_PREMISE; closure at K_max=3) is CORRECTED: T_dag (next-grade saturation under the single source stratification grading dag_size) satisfies every frozen canonicity criterion and provably differs from T_sat, so the adjunction layer is nonunique and the primary verdict is OPP_NONUNIQUE_CANONICAL. The prediction's record-layer and service-layer expectations (RO-A refuted; RO-D query-not-setting; SV-pool unique; K_max=3; single coherence cluster at small k) are all CONFIRMED. The prediction constrained nothing.

## Compact terminal return

```text
OD0-R49 OVERALL VERDICT: OD0_R49_PASS_OPPORTUNITY_CANDIDATE_CLASS_FROZEN_AND_CLASSIFIED + PRIMARY OPP_NONUNIQUE_CANONICAL
COMMITS (A / B): 4946e4e / FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE
R48 PIN VERIFICATION / CLEAN WORKTREE / BELL2 / HISTORICAL VALUES PARSED: PASS (manifest sha256 exact; commits resolve; erratum on R48's fabricated full-hash expansion recorded in R49_INPUT_LOCK.json) / CLEAN (pre-existing DEU_voids deltas unchanged) / false / 0
CONSTRUCTOR STEP SEMANTICS: no source-defined transition (enumeration only, native.py:112 / category.py:40-50); gradings: dag_size only (stratification); level-7 stop = explicit cutoff parameter max_dag=7 (native.py:109), rule unbounded
ADJUNCTION LAW: T_sat CANONICAL; T_dag CANONICAL; T_sat != T_dag (smallest witnesses: two 4-object ideals; genesis divergence k=3); T_id not excluded by source; CO1 stated
RECORD LAW: RO-A REFUTED (frozen append); RO-D UNIQUE given RO1 (74 uses, 32 multi-touch, 0 scope/over-record/covariance failures at D<=3); setting residual FORCED_BY_STATE_GIVEN_A13R; RO-0 not excluded; RO1 stated
SERVICE LAW: SV-pool unique order-free (A12 additivity + Thm 1); SV-int PREMISE_REQUIRING_SELECTION (2/3 vs 1/2 exact witness); order-free parts: appends + request pools; order-sensitive part: interleaved ledger updates
GLOBAL TRANSITION: two-member canonical family {T_sat-composite, T_dag-composite} given (CO1, RO1) + frozen premises (service axiom, A13R0, RRP1); smallest distinguishing state: 4-object ideal {a,b,{a,b},{a,{a,b}}} (and its exchange image)
COMMUTING DIAGRAM: NOT_REACHED; K_max=3; per-component restriction unchanged from R48 (x PARTIAL(CD1I) | N via induced records CONDITIONAL(RO1) | S via A12 CONDITIONAL(RO1+CO1) | Lambda blocked (Lambda_0 undeclared) | G+- RRP1 not exercised)
GM1-GM12 RESCORE: NOT_PERFORMED (Sec 7 conditional not met; nonunique family)
GLOBAL FRONTIER CLUSTER STRUCTURE AT k <= 3: single shared-ancestor coherence cluster at k=1..3 (both members); two-to-many lineage generalization NOT frozen - exact gap stated; no factorization assumed
FIELD READOUTS EMITTED: n (Part 5 conditional not met)
HOSTILE CONTROLS: 10/10
DETERMINISTIC RERUN: IDENTICAL_BYTE_FOR_BYTE
OUTPUT MANIFEST SHA-256: FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE
RECOMMENDED SINGLE R50 MOVE: Per the verdict tree: R50 = premise-invariant envelope / no-choice theorem over the two-member family. Exact shape sharpened by this round: the members share genesis, trace category, record law, and service form, and differ only in the step quotient; pooled service makes the quotient physical. R50 should (i) derive the maximal premise-invariant common structure (trajectory observables invariant across bundling, e.g. the record-event partial order and per-event marks), and (ii) test the one candidate no-choice principle available at source level: whether service non-compositionality plus a source covariance/locality condition on step quotients excludes one member exactly - before considering any new premise.
```
