# OD0-R63 Addendum Report: Operational Layer

Run date: 2026-09-02. Verdict: **OD0_R63_ADDENDUM_PASS_OPERATIONAL_LAYER_FROZEN**.
ADDENDUM_FROZEN_AFTER_A = true (D7-D9 frozen in a hashed appendix at
Commit A2 before any D7-D9 computation; base R63 outputs untouched).

## D7 - readability
Shell identity: THEOREM: the unrecorded shell U is exactly the set of childless objects (leaves). The recorded set S accumulates the closed ancestries of parents at each formation; a parent's closed cone contains the parent and all its ancestors, so an object is recorded iff it has at least one child. Certified: U = leaves bit-exactly on all four round trajectories.

Horizon law: E|U|/|X| -> 1/3, with the sharp finite-n form E|U|/n = 1/3 - 2/(3n) + o(1/n), i.e. E|U| ~ (n-2)/3: P(the object born at j is childless at n) = prod_{k=j}^{n-1}(1 - 2(k-1)/(k^2-3k+4)) -> (j/n)^2 e^{-4/j} for j >= 4 (objects j <= 3 are deterministically recorded - the picks at k = 2, 3 are forced), so E|U|/n -> integral t^2 dt = 1/3. Panel-verified: exact-law evaluation 0.3332668 at n = 10^4; Monte Carlo through n = 10^6 (0.333355); burst-size independent (each birth consumes exactly one pair; b = 2, 5, 20 checked). Exact small-n expectations 0.250 -> 0.274 (n = 4..9); trajectory readouts 0.336-0.395 (labeled). One third of the universe is operationally invisible to S at maturity.

Per-structure: 
 "d_G": "MIXED - the recorded parent edges give an upper approximation on X_rec, but shortest paths may route through unrecorded leaves (a leaf z = {u,v} certifies d_G(u,v) <= 2 invisibly to S); exact values require adjunction or adjudicator access.",
 "d_arrow": "READABLE_FROM_S on X_rec - every interior vertex of a directed path has a child, hence is recorded; directed distances between recorded objects are functions of S.",
 "d_U": "READABLE_FROM_S on X_rec (recorded cones determine beta).",
 "d_J": "READABLE_FROM_S on X_rec (cones of recorded objects are recorded through their own letters, RO-D).",
 "causal_order": "READABLE_FROM_S on X_rec (recorded parentage).",
 "coembedding": "READABLE_FROM_S among recorded objects; MIXED for full counts (unrecorded leaf descendants are invisible).",
 "R38": "closed (identity-only; base round).",
 "d_cost": "READABLE_FROM_S on X_rec - a function of recorded cones and chains (chains recoverable from recorded parentage); REALIZING it requires the adjunction."


## D8 - back-action theorem: PROVEN
For absent {x,y} and z = {x,y} formed at count n: (i) d_G(x,y) <= 2 permanently through z, whatever its prior value - objects are never destroyed and edges never removed (certified exactly: 3 -> 2 in the round certificate). (ii) coembedding(x,y) increases by 1 + (future descendants of z); INVARIANT under the act: d_J(x,y), d_U(x,y) (closed cones are fixed at formation - certified bit-identical), d_arrow between x and y (z lies below both; acyclicity forbids new x-to-y directed paths), and the causal order between x and y (z does not relate them). COLLAPSED: d_G (and co-embedding grows). (iii) The cones of x and y are recorded through their own letters (RO-D); unresolved letters resolve with uniform, phase-blind outcomes (R58) - geometry-irrelevant, only the event matters. (iv) The forced pool increases by exactly c(z) = c_first (chains(x) + chains(y)) + 2 (recorded cone of x union y) (R53/R58 typing), of expected order Theta(n log n) at maturity (R59). (v) The ensuing drain follows the R60 cycle law: E[tau] = (c(z) + D H_{c(z)})/r with r = Gamma + min(H, 2 Gamma) - m and D = n; at maturity c(z) ~ 4 n ln n gives E[tau] = (5 n ln n / r)(1 + o(1)). THEOREM: every direct operational comparison of two objects collapses their graph distance, resolves their frontiers, and costs Theta(n log n) service; record-outcome values play no role.

## D9 - cost-distance
Triangle: THEOREM - the triangle inequality HOLDS on every pair-closure ideal (refuting the registered guess that it fails): d_cost(x,z) = 11(ch_x + ch_z) + 2 W(cone(x) U cone(z)) <= d_cost(x,y) + d_cost(y,z), with slack exactly >= 22 ch_y >= 22 (tight: minimum observed slack 22), since cone(x) U cone(z) is contained in (cone(x) U cone(y)) U (cone(y) U cone(z)) and the weights are nonnegative (paths_to = 2 chains - 2 >= 0; nonnegativity is load-bearing - signed weights fail generically). SNAPSHOT-RELATIVE: all three costs must be evaluated at a common snapshot (the addendum's definition); mixed-snapshot evaluation violates the inequality (panel exhibited 5,912 violations across 773,516 mixed triangles), because W_rec grows monotonically. Certified: zero violations on 219,063 exhaustive triangles over all 2,812 reachable (ideal, rec) snapshots at n <= 8, 1.96M random-history triangles at n <= 40, and 11,004 sampled trajectory triples (round engine).

Metric status: With d_cost(x,x) := 0, d_cost is a METRIC on the absent-pair domain at any snapshot (symmetry by definition; positivity >= 2 c_first off-diagonal; triangle above) - stronger than the registered pseudometric-after-normalization. On X_rec it is READABLE_FROM_S (D7).

Scaling: d_cost(x,y) = Theta(n log n) at maturity: the chains term contributes 11(ch_x + ch_y) ~ 22n and the recorded-union term ~ 4 n ln n (R59 orders); the leading term is the union weight, determined by the same cone data as d_J plus chain counts (as registered).

D3 status: DEGENERATE at logarithmic rate: d_cost/(4 n ln n) concentrates with relative fluctuation Theta(1/sqrt(log n)) - the union weight sums near-independent contributions across the ~ln n birth decades (decade-CLT; the cone-overlap term touches only a 1/ln n-relative slice). Labeled readouts: relative sd 0.4725 at n = 100 vs 1/sqrt(ln n) = 0.466; 0.4924 at n = 162 vs 0.443. Rate grade: BOUND/CONJECTURE (decade independence is E-level); the degeneracy verdict itself follows from the vanishing relative spread. d_cost carries little distinguishing information at maturity under uniform pairing (as registered); V_cost(r) is a step at the concentration value. The PRIMARY verdict is unchanged: NONE_UNDER_UNIFORM_PAIRING, now over all seven structures including d_cost.

## Prediction vs outcome
Registered: d_J/d_U/causal READABLE_FROM_S, d_G MIXED, R38 closed - as registered. D8 PROVEN as stated - as registered. D9: registered 'triangle fails (witness with a shared parent)' - REFUTED: the triangle inequality is a THEOREM (subadditivity of union weights + chain positivity), and d_cost with zero diagonal is a full metric, stronger than the registered pseudometric-after-normalization; scaling and DEGENERATE status as registered, with the explicit 1/sqrt(log n) rate. New exact law: the operational horizon |U|/|X| -> 1/3. The prediction constrained nothing.

## Hostile controls
Base HC1-HC8 plus HC9: all REJECTED.
