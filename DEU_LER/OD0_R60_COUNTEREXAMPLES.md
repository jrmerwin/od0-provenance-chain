# OD0-R60 Counterexamples and corrections (append-only)

## CX-R60-1: carried cycle-average form REFUTED
The package carried <Phi^2>_cycle ~ ln(1 + 4 ln n)/(4 ln n) (linear
drain at constant rate). The hypergeometric drain slows as F falls
(rate Gamma F/(F+D)), and the chain spends Theta(D ln C) steps at low
F where Phi^2 ~ 1. Exact law: <Phi^2>_cycle = 1 - C/(Gamma E[tau]) =
D H_C/(C + D H_C) (1+o(1)) -> 1/(1+c) for C = c D ln D - a positive
constant. Witness (exact backward induction, Gamma=2, D=150,
C=3006): exact 0.29956, corrected formula 0.29993, carried formula
0.15202.

## CX-R60-2: 'mid-drain bursts O(1) per cycle' REFUTED (late regime)
Expected S^V >= 2 triggers per full drain = (1/Gamma) D ln D (1+o(1))
+ Theta(D) - unbounded. Witness (exact induction, Gamma=2): 34.2 /
137.3 / 414.2 triggers at D = 20/60/150. P(uninterrupted full drain)
= exp(-Theta(D log D)) (ln P = -520.7 at D=500). Consequence: pure
renewal cycles are an early-regime object; the late regime is the
balance band. Panel correction folded in: the general-Gamma
prefactor is 1/Gamma, not C(Gamma,2)/Gamma (equal only at Gamma=2).

## CX-R60-3: carried late-decay Theta(ln ln n / ln n) REPLACED
The balance-band law gives mean-square vacuum fraction x*^2 =
r/(4 C(Gamma,2) n ln n) at maturity n (run-average twice that), so
the time-averaged lapse^2 is O((n ln n)^{-1/2}) - a polynomial
scale, not ln ln n/ln n. Verified decisively in a self-consistent
simulation (late-window ratio 1.098 +/- 0.051 vs 2.0 for the
alternative bookkeeping, >17 sigma).

## CX-R60-4: carried N_V ~ Gamma n^2 ln ln n/(2(Gamma+H-m)) REFUTED
It presupposed the ln ln n/ln n decay. Corrected: N_V =
O(Gamma sqrt(2/(C(Gamma,2) r)) n^{3/2} sqrt(ln n)) (upper THEOREM
at E-level; matching lower CONJECTURE).

## CX-R60-5: registered depth-constant band [1, 2] REFUTED
Labeled readout: M_n/ln n = 3.58 at n = 10^3 (40/40 seeds >= 3.0),
rising to ~4.34 at n = 10^6. Proven E-level band: [1, 2e] in ln
units (upper by the Poisson-tail union bound with exact parent
marginal <= 2/(n-2); lower by max >= average with summable
exclusion bias).
