# RUNBOOK — B0 Boundary-Demand Instrument Runner Bundle

Built 2026-07-22 against the same byte-pinned base as C26.
Base pin: `rung1_v21_zeno.py` SHA-256 `8af1add9...c1a02`.
Derived variant: `rung1_v21i5_b0.py` SHA-256 `7f61ba9e...bad31` (printed by patcher).

## Bundle inventory
| File | Role |
|---|---|
| `make_v21i5_b0.py` | Patcher: base → B0 instrument (pre-service demand census, execution-attributed service by kind, P/B/X regions, radial shells, exact depth histograms) |
| `b0_worker.py` | Two arms per seed on the same stream: pocket (burst) + control (burst withheld); C15 clearance; atomic resumable caches |
| `b0_adjudicate.py` | Exact Fraction densities, shell-matched vacuum baseline, W1/W2 stationarity, gates G0–G4, four registered classifications |
| `b0_driver.py` | preflight → certify (10/10 + identity gate with b0_log=True) → run → adjudicate |
| `b0_freeze.py` | Seed list + SHA manifest from the ratified B0 spec |
| `b0_formation_adapter.py` | Same interface as C26; same archived-adapter integration point |
| `b0_config.json` | SMOKE config; frozen values in `_note` |

## Certification evidence (container, 2026-07-22)
1. Variant `certify.py` **PASS 10/10 bit-exact** (b0_log default off).
2. Identity gate, b0_log=True: **12 shared epoch-log columns bit-identical** to base.
3. End-to-end smoke (2 seeds, 2 arms each, ~145 epochs): pocket and depth-contrast
   boundary detected every epoch; exact rational ΔD positive on both seeds;
   gates discriminated on the G3 stationarity sub-criterion; STOCK_ONLY emitted
   in SMOKE mode. **This is a machinery demonstration, not a B0 result.**
4. Driver ergonomics fix carried from C26: the identity-gate step prints a label,
   not raw source, so no failure-string can be mistaken for a verdict.

## Instrument definitions the code made concrete (ratify before freeze)
1. **Pre-service timing** = the epoch-START snapshot: demand census taken before
   any core or exterior service that epoch. (Strictly earlier than the engine's
   own mid-epoch exterior recount; declared per the C-campaign timing rule.)
2. **Service attribution** at execution, five kinds: split_vac, split_forced,
   split_ext, flip (both parents), relief (pair excisions only — contraction
   rewrites are re-added and are NOT service).
3. **k_vac** = global modal depth over active faces (spec said "modal at same
   metric radius"; global modal is the simpler deterministic rendering — ratify
   or require the radial version, which costs one more pass).
4. **Pocket** = connected component of {depth ≥ k_vac + b0_kpocket} containing
   the anchor; **boundary** = faces with a cross-pocket neighbor at depth
   contrast ≥ 1. Both from topology+depth alone.
5. **Vacuum baseline** = control arm (same seed, burst withheld), shell densities
   weighted by the pocket arm's time-mean boundary shell occupancy
   (support-matching, the R26 lesson).
6. **λ_dress** (if RATE fires) = time-mean ΔS density per seed, exact Fractions
   retained; a registered candidate only, pending B1.

## Stagegate order
1. `python make_v21i5_b0.py` — verify variant SHA on both platforms.
2. `python b0_driver.py certify b0_config.json`.
3. Optional smoke as shipped (create a smoke `b0_seeds.json` first — B0 ships
   without one; the freeze tool writes the real one).
4. Install + certify the archived metric adapter (shared with C26).
5. Ratify spec [FREEZE-POINT]s + items above; write frozen values into
   `b0_config.json` (add `reserve_size`/`cohort_size`).
6. `python b0_freeze.py B0_instrument_spec_boundary_demand_stock_vs_rate.md`.
7. `python b0_driver.py all b0_config.json [budget]` — resumable; the frozen
   480-epoch window is the definitive-run scale (M2/Windows boxes).

## Dragons honored
UTF-8/LF writes; Path() everywhere; atomic caches + resume; foreground budget
chunks; wc -l preflight vs manifest; both arms of a seed inside one worker call
so a budget interrupt never splits an arm pair.
