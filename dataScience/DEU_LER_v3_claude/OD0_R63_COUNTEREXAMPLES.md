# OD0-R63 Counterexamples and corrections (append-only)

## CX-R63-1: the ultrametric inequality FAILS on pair-closure ideals
Witness (n = 8, exact): p = {a,ab}, q = {b,ab}, x = {a,p}, z = {b,q},
y = {p,q}. beta(x,y) = 3, beta(y,z) = 4, beta(x,z) = 2 (only {a,b,ab}
shared): d(x,z) = 6 > max(d(x,y), d(y,z)) = 5. Sharing breaks the
tree ultrametric. Both birth-index and depth variants fail.

## CX-R63-2: d_U fails even the ORDINARY triangle inequality
Witness (n = 13, exact): with p = {a,{a,ab}}, q = {b,{b,ab}} born
after half-time (births 8, 9): d(x,z) = 11 > 9 = d(x,y) + d(y,z).
d_U is classified NONE (a symmetric premetric).

## CX-R63-3: registered bedrock claims REFUTED (two)
(i) 'The bedrock is nearly totally ordered' - refuted: by exact
self-similarity its internal related fraction is (pi^{3/2}/2) m^{-1/2}
= Theta(n^{-1/4}) -> 0 (sparse self-similar partial order).
(ii) 'Every late object is within O(1) graph distance of the bedrock'
- refuted: the distance is Theta(log n) (greedy earlier-parent rate
exactly 3/2 log-units/step gives (1/3) ln n; BFS measured 0.289 ln n
at n = 1e7; lower bound from the base-8 volume law).

## CX-R63-4: the D3 trichotomy is INCOMPLETE
d_J between typical late objects realizes a fourth outcome: a
NONDEGENERATE bounded limit law (ratio-of-means 22/35 exactly, the
E[sqrt(W)] factor canceling; measured mean -> 0.627 at n = 2e5, sd
flattening at ~0.055, component fluctuation |cone|/sqrt(n) with limit
sd ~ 0.75). Not STABLE, not DRIFTING, not DEGENERATE. The registered
prediction (dJ DEGENERATE) is refuted; the frozen trichotomy is
refuted as exhaustive.

## CX-R63-5: pre-run constants corrected by the adversarial panel
(i) The cone-overlap integral is 13pi/32 = 1.2763, not 9pi/16 (my
pre-run slip); c_cap = 13 pi^{3/2}/64 = 1.1311; d_J ratio-of-means
= 1 - 13/35 = 22/35. (ii) The latest-common-ancestor scale is
n^{2/3}, not sqrt(n) (E[W^2] = 2 doubles the pair-ancestor density;
median beta/n^{2/3} ~ 1.0 stable across n = 1e3..1e5). (iii) The
interval bedrock-domination threshold is j = O(n^{1/4}), not
O(sqrt n). (iv) The greedy-descent constant to the bedrock is 1/3
ln n (2/3 ln n is the route to the primitives). (v) The max-depth
constant sharpens to c_max = 4.3111 (the frozen 2e ln n outer bound
holds), and the directed lower constant is c_min = 0.373365 - the
two roots of c(1 + ln 2 - ln c) = 1.
