# OD0-R51 Counterexamples and Witnesses (append-only)

## DEADLOCK: all four T=F candidates (circularity)
- circular deadlock at step 1, exact: a forced request exists only after an A12 compile of a record; a record (RO-D) fires only on a downstream USE; a use is a fired adjunction; and every adjunction is gated on a served forced request. At genesis there are no records, hence no forced requests, hence no serveable gate token, hence no adjunction ever fires.

## DEADLOCK: ADJ-V-S at Gamma <= 1
- n = min(Gamma, F+D) <= 1 serves at most one token per step, and the same-step gate needs both parents served in ONE step; no adjunction ever fires; X stays {a,b} forever (exact, all m, H)

## DEADLOCK: ADJ-V-P at Gamma = 0
- n = 0: no token is ever served, no mark is ever created, no adjunction fires

## EXPLOSION: REC-* and B0 keep the unthrottled adjunction layer
- R50 saturation applies verbatim: |X_{k+1}| = C(|X_k|,2)+2, kappa = 2 at all 1296 registered points; C2 = SUPER_EXPONENTIAL, C3 degenerate.

## CORRECTION to registered prediction: ADJ-V-P growth class
- Predicted EXPONENTIAL; exact quadratic bound |X_k| <= C(2+Gamma*k,2)+2 proves POLYNOMIAL.

## HOSTILE CONTROL HC1: selecting by preference or dynamics readout
- status: REJECTED
- obstruction/scope: Survivorship and minimality are decided solely by the frozen C1-C8 rule and (C5,C6,C8) order; the dynamics readout is Part 4 output, not a criterion.

## HOSTILE CONTROL HC2: tuning or singling out Gamma; Gamma>=2 as physical claim
- status: REJECTED
- obstruction/scope: The full registered Gamma range is scanned; Gamma>=2 is reported as exact scope with its witness, explicitly not a physical claim.

## HOSTILE CONTROL HC3: external referent in outputs
- status: REJECTED
- obstruction/scope: No cosmology, particle, inflation, or time referent appears in any R51 output.

## HOSTILE CONTROL HC4: historical rounds = steps; historical numerics
- status: REJECTED
- obstruction/scope: No identification made; all numerics are this round's own exact computations or frozen structural constants.

## HOSTILE CONTROL HC5: hidden parameters
- status: REJECTED
- obstruction/scope: All nine candidates are binary and parameter-free by construction (C7=0 verified per candidate); the load convention (11/record) is a frozen lower bound, not a tunable.

## HOSTILE CONTROL HC6: readouts defining an epoch or basin
- status: REJECTED
- obstruction/scope: No epoch, basin, regime label, or threshold is defined; shell size and burst structure are reported as raw trajectories.

## HOSTILE CONTROL HC7: frozen-root modification; BELL2
- status: REJECTED
- obstruction/scope: Read-only access; worktree clean at start and end; BELL2 unopened.

## HOSTILE CONTROL HC8: hand-produced hash
- status: REJECTED
- obstruction/scope: All hashes computed in-process at recording time.
