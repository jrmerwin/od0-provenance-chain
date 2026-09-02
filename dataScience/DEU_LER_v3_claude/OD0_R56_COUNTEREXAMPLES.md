# OD0-R56 Counterexamples, Audits, and Gaps (append-only)

## AUDIT: the >= 3-sibling costing convention
- Every engine costed every record at the uniform Q1-minimum lower-bound load (11 per newly recorded prefix, 2 per repeat), declared in advance at the R50/R51 Commit A locks; Q2 typing was never applied and sibling groups of any size were costed as independent records. This is a coarser convention than pairwise reduction and was recorded as a lower-bound convention throughout.
- classification: PAIRWISE_REDUCTION_CONVENTION (scoped Gamma <= 3) - the nearest frozen class, with the exact description above recorded verbatim; NOT AD_HOC (declared in advance, direction-consistent) and NOT FROZEN_ALPHABET_COVERS (>= 3 groups have no frozen typing)
- theorems unaffected; readouts flagged; label-emission statements scoped to Gamma <= 3; the m-sibling alphabet is the recorded gap.

## O8 diameter: monotonicity NONE
- Adding objects can create shortcuts as well as distant vertices; neither direction is a theorem - classified NONE, readout only.

## HOSTILE CONTROL HC1: additions to Sections 4-6 after Commit A
- status: REJECTED
- obstruction/scope: R56_H2_PREREGISTRATION.json is byte-identical to its Commit-A seal; the adjudication references it read-only.

## HOSTILE CONTROL HC2: H2 content read; sentinels not false
- status: REJECTED
- obstruction/scope: The H2 PDF hash re-verified untouched at lock time; sentinels parsed=false at start and end.

## HOSTILE CONTROL HC3: rate or round-number statement in prereg/protocol
- status: REJECTED
- obstruction/scope: Excluded by construction; the protocol compares only reparametrization-invariant shapes.

## HOSTILE CONTROL HC4: >=3-sibling convention presented as frozen source
- status: REJECTED
- obstruction/scope: The 7.1 audit classifies it PAIRWISE_REDUCTION_CONVENTION with the exact engine behavior recorded; label-emission statements scoped to Gamma <= 3.

## HOSTILE CONTROL HC5: label promoted to particle/species/channel
- status: REJECTED
- obstruction/scope: CCE4 restated; no species language anywhere.

## HOSTILE CONTROL HC6: H1 used beyond disclosed provenance
- status: REJECTED
- obstruction/scope: Only definitional provenance disclosure; no H1 values used.

## HOSTILE CONTROL HC7: TG1/cost law/filtration/frozen roots modified; BELL2
- status: REJECTED
- obstruction/scope: Nothing modified; worktree clean; BELL2 unopened.

## HOSTILE CONTROL HC8: hand hash; placeholder
- status: REJECTED
- obstruction/scope: All hashes in-process; stamp commit closes the round.
