# OD0-R61 Counterexamples and corrections (append-only)

## CX-R61-1: registered co-embedding total order CORRECTED
The registered prediction placed both clock totals at n^{3/2} with the
containment clock ahead. Each new object contributes C(A,2) ~ A^2/2
co-embedding pairs (not A), so TCo(n) is n^2-scale (proven band
[c1 n^2, c2 n^2 ln n]) while TC(n) = (pi/2) n^{3/2} (1+o(1)); under
the frozen ln ln functionals the CO-EMBEDDING clock runs ahead, by
the additive constant ln(4/3) = 0.2877. Labeled witness: tau_Co -
tau_C = 0.265-0.276 at n ~ 50-80.

## CX-R61-2: R48 missing-artifact list partially stale
v31l, v31m, v31n generating sources were located on this machine
(DEU_voids sol_effort/face_value bundles; filenames pinned in
R61_ARTIFACT_PINS.json); only v31o remains missing. Recorded as a
correction to the carried missing-list; no content parsed.

## CX-R61-3: FORWARD ERRATUM to R59 T3 (and the R60 stamp headline)
The cone constant 3 pi/4 in R59 T3 is a mean-field artifact. The
descendant chain d_j is a rate-2 Yule process in log-time, so the
descendant fraction converges to n W/(n W + j^2) with W ~ Exp(1)
RANDOM; summing the ancestor law over j then carries the factor
E[sqrt(W)] = sqrt(pi)/2: E|cone(new at n)| = (3/8) pi^{3/2} sqrt(n)
(1+o(1)) ~ 2.0881 sqrt(n). Witnesses: exact-marginal chains of the
certified per-state law give E|cone|/sqrt(n) = 2.0936 +/- 0.0075 at
n = 16000 (35 SE below 3 pi/4 = 2.3562); the R59 exhaustive n = 9
value 6.165 vs 6.26 predicted vs 7.07 mean-field; DAG simulation
TC/n^{3/2} -> 1.3873 at n = 30000 (pi^{3/2}/4 = 1.3921, pi/2 =
1.5708). The Theta(sqrt n) ORDER of R59 T3 stands; only the sharp
constant is corrected. R59/R60 stay frozen; correction recorded
forward here (same convention as the R48 hash erratum). Secondary:
R59 T2's stated recursion omits composite j's own parent pair from
the non-descendant existing-pair count (+1; O(1/k^2) effect,
asymptotics unaffected; the fixed form reproduces R59's own
certified exact values 8/29 and 109/319 at n = 9).
