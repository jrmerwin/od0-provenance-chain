# OD0-R53 Report - Rendering Cost, Renewal, Growth Law, and the Maturation Filtration (M3)

## Answer to the governing question

**Cost:** chains(x) obeys the exact parent-sum recurrence (CD1I 1,326 certified) and the frozen record identity counts PATHS - c(x) = c_first*paths_to(x) + c_repeat*(recorded cone), certified against the direct enumeration. chains grows between Fibonacci and 2^depth. c_min is NOT monotone (witness recorded). **Growth:** at every registered point with m < Gamma, unbounded growth is PROVEN a.s. (drift-band recurrence + positive burst probability + Borel-Cantelli); the rate is open between unbounded and linear - the registered log target is not established; m >= Gamma remains P with the precise gap. **Renewal:** at F=0 service is deterministically all-vacuum and the burst law is the exact R52 growth distribution at s = min(Gamma,D). **Filtration:** E0 = {F+D<=Gamma} with permanent exit at D>Gamma; E1 = {D>Gamma} forward-invariant; drained/draining and burst/quiet decompositions; the cost stratum {c_min<=Gamma} is transient and nonempty (correcting the prediction); NO basin beyond E1 is definable without a numeric choice - maturity is the asymptotic law.

## Verdicts

- OD0_R53_PASS_MATURATION_FILTRATION_DEFINED_TARGET_BLIND
- BASIN_BEYOND_E1: not definable without numeric choice
- CAPACITY_TOTAL: constant (carry-forward)
- GROWTH_LAW: U(m < Gamma: proven, rate PARTIAL [<= linear; log-target unproven]) / P(m >= Gamma: precise gap stated)
- R54_PROTOCOL: FROZEN
- RENEWAL: theorem at F=0; drain bounds two-sided; geometric cycle growth CONJECTURE

## Prediction vs outcome

Confirmed: chains recurrence exact with 1,326 certification; Fibonacci lower bound; renewal at F=0; E1 forward-invariant; no basin beyond E1 without a numeric choice; R54 protocol frozen. Corrected: (i) the growth law splits by m vs Gamma - U is proven only for m < Gamma, and the registered Theta(log k) rate is NOT established (the cost-growth argument fails against the c_min non-monotonicity); (ii) the stratum {c_min <= Gamma} is NOT empty everywhere - genesis cost 0 and repeat-only pairs of cost 4 defeat the c_first > 5 argument at Gamma in {4,5}. The prediction constrained nothing.

## Compact terminal return

```text
OD0-R53 OVERALL VERDICT: OD0_R53_PASS_MATURATION_FILTRATION_DEFINED_TARGET_BLIND
COMMITS (A / B): 33c1782 / FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE
R52 PIN / WORKTREE / BELL2 / VALUES PARSED / HAND HASHES: PASS / CLEAN / false / 0 / 0
R52 SEC-4.1 CARRY-FORWARD: regions FIXED; Gamma per region; capacity total CONSTANT
CHAIN RECURRENCE: chains(u,v)=chains(u)+chains(v); sum over 171 composites = 1324, +2 primitive trivial chains = 1326 (CD1I 1,326 certified: True)
COST FORMULA: c(x) = c_first*paths_to(x) + 2*(recorded cone); c_first 11..13/22..26 frozen; cross-validation True
DEPTH BOUNDS: Fib(k+2) family [1, 1, 2, 3, 5, 8, 13, 21]; chains <= 2^depth (0 failures)
c_min MONOTONICITY: NOT monotone; witness recorded
RENEWAL AT F=0: deterministic all-vacuum (0 violations); burst law = R52 identity at s=min(Gamma,D)
GROWTH LAW: U proven for m < Gamma (117 points; rate PARTIAL, log target unproven); P for m >= Gamma (27 points, gap stated)
DRAIN SCALING: two-sided exact bounds; geometric cycle growth CONJECTURE
SENSITIVITY: relief shifts boundary toward m < Gamma+H (conditional); population factor: class unchanged
FILTRATION: E0 exit permanent at D>Gamma (exact distributions per point); E1 forward-invariant; {c_min<=Gamma} transient, nonempty everywhere (genesis cost 0; repeat-only cost 4 for Gamma in [4, 5])
BASIN BEYOND E1: NOT definable without numeric choice
READOUTS: 10^4-step sampled trajectories at 144 points within proven envelope; exemplar (2,0,0) |X|: 100:7.680000000000, 1000:18.240000000000, 3000:29.000000000000, 10000:49.400000000000
R54 PROTOCOL FROZEN: yes - PASS iff historical regime sequence coarsens the derived filtration order with matching monotonicities; mismatches at equal prominence
HOSTILE CONTROLS: 9/9
DETERMINISTIC RERUN: IDENTICAL_BYTE_FOR_BYTE
OUTPUT MANIFEST SHA-256: FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE
RECOMMENDED SINGLE R54 MOVE: Open H1 under the frozen protocol - one comparison, no repair: derived sequence (E0 -> E1 -> renewal cycles with growing structure, U-growth for m < Gamma with rate gap reported at equal prominence) and derived monotone observables (|X|, shell fraction, chain-multiplicity distribution, cycle-length growth) against the historical qualitative regime sequence and observables, sequence and monotonicity only.
```
