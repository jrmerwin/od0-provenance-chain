# OD0-R53 Counterexamples and Witnesses (append-only)

## WITNESS: c_min is not monotone
- at point (Gamma,m,H)=[2, 0, 0], step 2: c_min decreased from 22 to 4

## CORRECTION: {c_min <= Gamma} is not empty everywhere
- genesis pair {a,b} costs 0 (empty ancestry cone); repeat-only pairs (fully recorded cones) cost 2*|cone paths| - exactly 4 for an unformed {a,c} with c used - so the stratum is nonempty at every registered point (genesis) and beyond genesis for Gamma in [4, 5].

## CORRECTION: growth-law rate
- The registered Theta(log k) target is NOT established; U is proven for m < Gamma without a rate below the linear upper bound; m >= Gamma remains P with the stated gap.

## HOSTILE CONTROL HC1: numeric threshold; criterion not in state fields
- status: REJECTED
- obstruction/scope: Every filtration criterion is a state relation (F+D<=Gamma, D>Gamma, F=0, batch nonempty, c_min<=Gamma); no numeric constant beyond frozen state fields appears.

## HOSTILE CONTROL HC2: historical label on a stratum; historical numeric
- status: REJECTED
- obstruction/scope: Strata are named E0/E1/drained/draining/burst/quiet only.

## HOSTILE CONTROL HC3: log-growth stated as theorem; U/T by readout
- status: REJECTED
- obstruction/scope: The Theta(log k) target is explicitly NOT established; U is proven for m < Gamma by the drift/Borel-Cantelli argument, not by readouts; m >= Gamma left as P with the precise gap.

## HOSTILE CONTROL HC4: modification of cost law, record scope, or TG1
- status: REJECTED
- obstruction/scope: All carried verbatim; the paths-vs-chains refinement is an exact restatement of the frozen R50 record identity, recorded as such.

## HOSTILE CONTROL HC5: capacity extrapolated; regions refined
- status: REJECTED
- obstruction/scope: Carry-forward verbatim: regions fixed, capacity total constant; all statements at registered Gamma.

## HOSTILE CONTROL HC6: R54 protocol altered after Commit A
- status: REJECTED
- obstruction/scope: Frozen in R53_INPUT_LOCK.json at Commit A; emitted unchanged.

## HOSTILE CONTROL HC7: external referent
- status: REJECTED
- obstruction/scope: None appears.

## HOSTILE CONTROL HC8: frozen roots; BELL2
- status: REJECTED
- obstruction/scope: Read-only; worktree clean at start and end; BELL2 unopened.

## HOSTILE CONTROL HC9: hand-produced hash
- status: REJECTED
- obstruction/scope: All hashes computed in-process.
