# OD0-R63 ADDENDUM v0.1 — Operational Layer: Readability, Back-Action, and Cost-Distance

Attach to OD0_CLAUDE_CODE_PACKAGE_R63 v0.1. If R63 Commit A has not yet been made, freeze D7–D9 with D1–D6. If Commit A exists, freeze D7–D9 in a hashed appendix before any D7–D9 computation and record `ADDENDUM_FROZEN_AFTER_A = true`. Zero new premises. Same locks, controls, and vocabulary rules as the base package.

### Motivation (recorded, not adjudicated)

D1's structures are adjudicator distances, computed from outside the process. Inside the process, structure is accessible only through the fact graph S (already-recorded, classical) or through adjunction (which creates a relation). The geometry stage must distinguish what is readable without disturbance from what can only be established by an act that changes the state.

---

**D7 (readability classification).** For each D1 structure, classify as:

- `READABLE_FROM_S`: a function of the recorded fact graph alone (recorded cones, recorded parentage, co-embedding among recorded objects); no state change required; defined only on the recorded subgraph X_rec = X ∖ U (the shell U carries no facts).
- `REQUIRES_ADJUNCTION`: determinable only by forming a new composite relating the two objects (or a chain of them).
- `MIXED`: readable on X_rec, requires adjunction to extend into U.

Prove for each; state the operational horizon: the fraction |U|/|X| of the universe invisible to S at object count n (from the shell readouts, labeled) and its theorem-grade behavior if available.

**D8 (back-action theorem).** For x, y ∈ X with {x,y} ∉ X, and z = {x,y} formed by an adjunction at object count n:

- d_G(x,y) becomes ≤ 2 permanently (through z), regardless of its prior value;
- co-embedding(x,y) increases by 1 + (future descendants of z); d_J(x,y) unchanged (cones fixed at formation) — state which D1 distances are invariant under the act and which are collapsed;
- the cones of x and y are recorded through their own letters (RO-D); any unresolved letters of x or y are resolved (outcome uniform, geometry-irrelevant: the dynamics is phase-blind, so only the event matters);
- the forced pool increases by c(z) = c_first·(chains(x) + chains(y)) + 2·(recorded cone of x ∪ recorded cone of y) exactly (R53/R58 typing), with expected order Θ(n log n) at maturity (R59);
- the lapse during the ensuing drain follows the R60 cycle law; give the expected drain length as a function of c(z), Γ, H, m.

State the theorem: every direct operational comparison of two objects collapses their graph distance, resolves their frontiers, and costs Θ(n log n) service; record-outcome values play no role.

**D9 (cost-distance).** Define d_cost(x,y) = c({x,y}) for {x,y} ∉ X (the rendering cost of relating x and y), and its time form t_cost(x,y) = expected drain length. Determine: symmetry (yes by definition); whether the triangle inequality holds on pair-closure ideals or fails (give the witness); whether d_cost is a pseudometric on X_rec after suitable normalization; its scaling law at maturity from R59 (chains(x) + chains(y) and the union of recorded cones); its relation to d_J and to the ancestry law (registered: d_cost is determined by cone sizes and overlap, hence by the same data as d_J plus chain counts); its ball-volume law V_cost(r) and D3 status (STABLE / DRIFTING / DEGENERATE). Classify d_cost under D7 (registered: `READABLE_FROM_S` on X_rec, since cost is a function of recorded cones and chains, but *realizing* it requires the adjunction).

Add d_cost to the D3 dimension question and to the primary verdict.

---

**Hostile control 9.** No operational claim beyond D7–D9; no observer, agent, or protocol is posited inside the model; "readable" means "a function of S," nothing more.

**Outputs.** Append `R63_OPERATIONAL_LAYER.json` (D7–D9 with certificates) to the base output list; include its hash in the manifest.

**Terminal return additions.**
```text
D7 READABILITY (per structure; operational horizon |U|/|X|):
D8 BACK-ACTION THEOREM (collapsed vs invariant distances; cost order; drain length):
D9 COST-DISTANCE (triangle status; pseudometric status; scaling; D3 status; readability):
```

**Registered prediction (Claude).** D7: d_J, d_U, and the causal order are `READABLE_FROM_S` on X_rec; d_G `MIXED`; R38 reachability closed. D8 PROVEN as stated. D9: symmetric; triangle inequality fails (witness with a shared parent); a pseudometric after subtracting the additive chain terms; scaling Θ(n log n) at maturity with variation dominated by cone overlap; D3 status DEGENERATE (costs between typical late objects concentrate near 4n ln n, so d_cost carries little distinguishing information at maturity under uniform pairing). This prediction constrains nothing in the run.
