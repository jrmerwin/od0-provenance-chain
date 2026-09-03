# OD0-R52 Counterexamples and Witnesses (append-only)

## WITNESS: equal (n,s), different growth distributions
- n=5, s=3: ['a', 'b', '{a,b}', '{a,{a,b}}', '{a,{a,{a,b}}}'] vs ['a', 'b', '{a,b}', '{a,{a,b}}', '{b,{a,b}}'] - distributions {'1': '3/10', '2': '3/10', '3': '2/5'} vs {'0': '1/10', '2': '3/5', '3': '3/10'}

## LADDER L0 NOT LUMPABLE
- point (Gamma,m,H) = [2, 0, 0]; witness pair {"B": 0, "P": 0, "X": ["a", "b", "{a,b}"], "served": ["a", "b"]} vs {"B": 0, "P": 0, "X": ["a", "b", "{a,b}"], "served": ["a", "{a,b}"]}

## LADDER L1 NOT LUMPABLE
- point (Gamma,m,H) = [2, 0, 0]; witness pair {"B": 0, "P": 0, "X": ["a", "b", "{a,b}"], "served": ["a", "b"]} vs {"B": 0, "P": 0, "X": ["a", "b", "{a,b}"], "served": ["a", "{a,b}"]}

## LADDER L2 NOT LUMPABLE
- point (Gamma,m,H) = [2, 0, 0]; witness pair {"B": 0, "P": 0, "X": ["a", "b", "{a,b}"], "served": ["a", "b"]} vs {"B": 0, "P": 0, "X": ["a", "b", "{a,b}"], "served": ["a", "{a,b}"]}

## LADDER L3 NOT LUMPABLE
- point (Gamma,m,H) = [2, 0, 0]; witness pair {"B": 0, "P": 0, "X": ["a", "b", "{a,b}"], "served": ["a", "b"]} vs {"B": 0, "P": 0, "X": ["a", "b", "{a,b}"], "served": ["a", "{a,b}"]}

## CORRECTION to registered prediction: record scope
- Predicted BEFORE_OWN_LETTER with persistent m-party equality states; the frozen R49 rule gives THROUGH_OWN_LETTER, product clusters between steps, and within-step-only sibling correlation.

## CAVEAT recorded: mean-field c_eff is state-dependent
- The Part 1 identities make c_eff STATE-DEPENDENT and unbounded: the record count of a use equals the number of ancestry-cone paths, which grows with DAG depth. A stationary (x*, u*, g*) with constant c_eff therefore presupposes bounded-depth growth; the sampled readout tests exactly this. The conjecture is recorded with this caveat rather than repaired.

## HOSTILE CONTROL HC1: observable added/dropped after Commit A
- status: REJECTED
- obstruction/scope: The Section-5 inventory was frozen in R52_INPUT_LOCK.json at Commit A and is emitted unchanged; readouts removed nothing.

## HOSTILE CONTROL HC2: epoch label, threshold, or basin from readouts
- status: REJECTED
- obstruction/scope: No label, threshold, or basin appears anywhere; settle/drift language in the readout summary describes sampled curves only.

## HOSTILE CONTROL HC3: sampled results cited as theorems or used to choose a quotient level
- status: REJECTED
- obstruction/scope: The closure ladder was adjudicated purely on the exact transition systems; the sampled file carries a NEVER-PROOF label.

## HOSTILE CONTROL HC4: mean-field map presented as more than a conjecture
- status: REJECTED
- obstruction/scope: Labeled MEAN_FIELD_CONJECTURE with an explicit validity caveat; no convergence claim; nothing fitted.

## HOSTILE CONTROL HC5: Gamma extrapolated; regions refined without source
- status: REJECTED
- obstruction/scope: All dynamics at registered Gamma 2..5; regions declared FIXED per the frozen UEQ0 declaration.

## HOSTILE CONTROL HC6: external referent
- status: REJECTED
- obstruction/scope: None appears.

## HOSTILE CONTROL HC7: historical numeric; rounds=steps
- status: REJECTED
- obstruction/scope: All numerics generated in-round or frozen structural constants.

## HOSTILE CONTROL HC8: frozen-root modification; BELL2
- status: REJECTED
- obstruction/scope: Read-only; worktree clean at start and end; BELL2 unopened.

## HOSTILE CONTROL HC9: hand-produced hash
- status: REJECTED
- obstruction/scope: All hashes computed in-process.
