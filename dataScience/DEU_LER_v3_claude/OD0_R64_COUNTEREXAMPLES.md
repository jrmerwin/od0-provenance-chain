# OD0-R64 Counterexamples and corrections (append-only)

## CX-R64-1: registered gate-class guesses refuted (four)
(i) UNREL does not resemble ALL from genesis: exact witness -
permanent deadlock at n = 3 (both absent pairs are related through
ab); it sustains only from a 7-object seed with incomparable pairs.
(ii) LEAF1's spectral base is (5 + sqrt(41))/2 = 5.7016 (two-type
operator: lambda A = 4(A+C), lambda C = 2A + C), not 4: chain links
interact multiplicatively with the uniform bridges (measured shell
ratios 4.02-4.07 at n = 1e7, above 4 and rising). Stronger: the
leaf count is pathwise non-increasing and equals exactly 1 past
genesis.
(iii) MINCOST at Gamma >= 3 is exponentially ENHANCED, not
clustered-drifting: pair costs on the served ensemble are
birth-dominated (Theta(1) relative spread - the D9 late-pair
concentration does not transfer), the gate persistently fires
top-2-earliest-born pairs (0.60/0.50/0.43 at Gamma = 3/4/5, flat),
and the exact operator gives rho = 48/5, 384/35, 256/21 - above 8,
growing in Gamma; d_J shifts toward SMALLER overlap (0.627 ->
0.70-0.76).
(iv) PC/GP/COUSIN1/DG2 are exponential small worlds, not uniformly
'tree-like or chain-like'; the class's true chains are SIB from
its minimal seed, SIB_AND_LEAF1, and DG2_AND_LEAF1.

## CX-R64-2: the ancestry-gated cost law is neither of the two
## candidates
The package-carried Theta(ln n) AND the pre-run polynomial guess
are both refuted: under REL, ln chains = Theta(sqrt(log n)) with
lineage fixed point kappa = pi/sqrt(3) = 1.814 (local exponents
decline as a/(2 sqrt(ln n)), matching measurement across four
runs); cost = exp(Theta(sqrt(log n))) = n^{o(1)} but
omega(polylog); growth |X(T)| = T^{1-o(1)}.

## CX-R64-3: the frozen no-go route (i) corrected
'One parent uniform over Theta(n) with probability >= c' gives
rho >= 4c by kernel comparison - proving rho > 1 only for
c > 1/4. The conclusion holds for every c bounded below via the
bridging bound rho >= 1 + Theta(c) (measured base 2.13 at
c = 0.1, 1.39 at c = 0.02), with the hypothesis strengthened to
uniformity over all objects (or a time-representative set).

## CX-R64-4: a seed-dependent geometry class
SIB is the class's only gate whose structure type depends on the
seed: from its minimal 4-object seed it is a DETERMINISTIC forced
chain t_{k+1} = {t_{k-1}, t_k} with exactly one fireable pair at
every step (exponent 1); from richer seeds the eligible-pair
count is Theta(n) and the process is an exponential tree.
Recorded as a finding about gate/seed coupling.
