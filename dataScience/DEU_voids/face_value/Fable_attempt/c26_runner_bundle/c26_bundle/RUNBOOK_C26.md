# RUNBOOK — C26 Dual-Candidate Structural Preflight Runner Bundle

Built 2026-07-22 against `generative-ledger` public HEAD.
Base engine pin: `rung1_v21_zeno.py` SHA-256 `8af1add9...c1a02` (full hash in patcher).
Derived variant: `rung1_v21i4_c26.py` SHA-256 `69e808c7...f4abd` (printed by patcher).

## Bundle inventory

| File | Role |
|---|---|
| `make_v21i4_c26.py` | Patcher: base → instrumented variant, anchored exact-string, SHA-pinned, aborts on ambiguity |
| `c26_formation_adapter.py` | Formation schedule interface + **uncertified native-pulse fallback** |
| `c26_worker.py` | Per-seed run → atomic gzip-pickle cache; resumable; clearance certification (C15 zero-hold) |
| `c26_firewall.py` | C23-template whitelist loader; sole legal cache access for selection |
| `c26_select.py` | Candidates A/B, tie-breaks (prereg 4.3), controls, observables P/U/M/S/C |
| `c26_adjudicate.py` | Gates G1–G4, discovery/validation split, registered classification, stopping rule |
| `c26_driver.py` | Stages: preflight (wc -l) → certify → run → select → adjudicate; SMOKE vs FROZEN modes |
| `c26_freeze.py` | Ordered seed list (deterministic LCG64 from prereg hash) + FREEZE_MANIFEST |
| `c26_config.json` | Currently the SMOKE configuration; frozen values noted in its `_note` |

## Certification evidence (this container, 2026-07-22)

1. Base engine: `certify.py` **PASS 10/10 bit-exact**.
2. Variant (instruments default-off): `certify.py` **PASS 10/10 bit-exact**.
3. Keystone gate — instruments ON (`snap_every=10, snap_relief=True`), panel row (m=26, Δt=4, seed 110): **all 12 shared epoch-log columns bit-identical to base**. This gate re-runs at every driver invocation (stage 1).
4. End-to-end smoke (2 seeds, ~145 epochs): candidates identified, lineage propagation through splits/flips/relief verified, reuse counts computed, control matcher and cleanliness exercised, classification + stopping-rule banner emitted, resume-on-rerun confirmed.

Engineering note (pre-freeze, so no amendment required): smoke exposed a tuple/list
mismatch in `members_at` (lineage ids are tuples in the pickle; the query was
list-typed, so every membership read returned empty). Fixed and re-verified before
this runbook was written. Recorded here per known-dragons practice.

## Stagegate order on your machines

1. `python3 make_v21i4_c26.py` in the bundle dir (finds `../generative-ledger/engines`, or copy the base beside it). Verify the printed variant SHA matches the pin above on **both** Windows and Mac.
2. `python3 c26_driver.py certify c26_config.json` — must print PASS ×2 + identity gate PASS on each platform.
3. Optional smoke: current config as-is (`c26_driver.py all c26_config.json 600`).
4. **Install the archived C6/C13 metric adapter** as `ArchivedMetricAdapter` in `c26_formation_adapter.py`, certified by exact reproduction of one archived C13/C15 formation row. The fallback is schedule-shaped but delivers native ops, not equal-metric action; the driver and freezer refuse frozen runs while it is active.
5. Ratify every [FREEZE-POINT] in the prereg **and** the implementation freeze-points below; set the frozen values in `c26_config.json` (guidance in its `_note`).
6. `python3 c26_freeze.py C26_prereg_dual_candidate_structural_preflight.md` — writes `c26_seeds.json` + `FREEZE_MANIFEST.json`. Commit both with the prereg.
7. `python3 c26_driver.py all c26_config.json [budget_seconds]` — FROZEN mode; resumable; rerun with a budget to chunk long grids (definitive runs on the M2/Windows boxes per standing practice).

## Implementation freeze-points (ratify before step 6)

These are measurement definitions the code had to make concrete. Each must be
either ratified as written or revised **now** — never after data exist.

1. **Snapshot-lattice support.** Gate S counts *snapshot epochs* with ≥1 frustrated face in the support region. At `snap_every=10`, the prereg's "≥90 frustrated-face epochs" renders as `support_min_snaps=9`. Ratify the lattice rendering (or lower `snap_every` at memory cost).
2. **d/ℓ\* definition.** Implemented as weighted face-distance (core_partition metric: ½(L(u)+L(w)) per step, L = 3^(−k/2)) from the event's first locus node, divided by ℓ\* = 3^(−k_max/2) with k_max = deepest candidate member at tₑ. **Reconcile against the C24 archive definition** before freeze.
3. **Control cleanliness (gate C).** Identity-based: no fired relief event's removed/created faces intersect the control set within ±64 epochs. (Exact and deterministic; distance-based cleanliness would need per-event geometry.)
4. **Control matcher.** Deterministic scan: snapshot epochs ascending, start faces by ascending id, BFS growth constrained to the exact type multiset among faces beyond the exclusion radius; first match wins. Depth matched ±1 order-matched on the sorted signature.
5. **Tie-break evaluation epoch** tₑ = nearest snapshot ≤ formation_end.
6. **Seed-list generator.** LCG64 seeded by the prereg hash (self-verifying: anyone can regenerate the list from the frozen document).
7. **Candidate-A finalists.** If several events fire at the last relief epoch, all are finalists and tie-breaks (4.3) decide — ratify that reading of "final relief event".

## Constraints and dragons honored

- Explicit UTF-8/LF on every write (Windows cp1252 dragon); `Path()` everywhere.
- Atomic caches (`.tmp` + `os.replace`); reruns skip valid caches.
- No background processes; driver takes a foreground budget argument and resumes.
- Memory: snapshots at cadence 10 + relief epochs; if long frozen runs exhaust RAM on the miniconda box, raise `snap_every` to 20 **before freeze** (it is a measurement-definition change) and halve `support_min_snaps` accordingly.
- Stage 0 refuses any bundle file whose line count disagrees with the freeze manifest (silent shadow-cache dragon).
