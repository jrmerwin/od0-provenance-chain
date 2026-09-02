# OD0-R59 Counterexamples and corrections (append-only)

## CX-R59-1: registered Gamma-ratio product form for E[T_n] REFUTED
The registered prediction gave E[T_n] via the product 4*prod_{k=3}^{n-1}
(1 + 2/k) = n(n+1)/3. The exact law is E[T_n] = n(n-1)/2 + 1 (proven
fixed point of the exact linear recursion E[chains(new)|state] =
2((k-2)T+2)/(k^2-3k+4); certified exhaustively for n <= 10, e.g.
E[T_10] = 46 vs product form 110/3). The product form omits the
existing-pair exclusion, which shifts the quadratic constant from 1/3
to 1/2. Recorded as a refutation of the registered closed form; the
target's Theta(n^2) claim stands with the corrected constant.

## CX-R59-2: registered ancestry form is the descendant fraction, not
## the ancestor law
n/(n + j(j-1)) is the descendant FRACTION phi_j(n). The ancestor
probability of the new object is a_j(n) = 2 phi_j - phi_j^2 + O(1/n).
Witness (exhaustive exact, j = 8, n = 9): a = 0.2759; corrected law
0.258; registered phi-form 0.139. The phi-form as ancestor law is
refuted; the corrected identification is adopted.

## CX-R59-3: registered cone constant pi/2 REFUTED; correct constant
## 3 pi/4
sum_j phi_j = (pi/2) sqrt(n) is the single-parent cone; the pair-union
cone is sum_j (2 phi_j - phi_j^2) = (3 pi/4) sqrt(n) (1+o(1)).
Registered constant corrected; the Theta(sqrt n) order stands.
