# OD0-R56 Report - H2 Preregistration and the M5 Opening

## H2 is preregistered; the label ladder is proven

The sealed preregistration (hash 298d21da179d8e6a...) freezes the nine provenance-disclosed observables, the P1-P6 prediction set (rates and round counts excluded by construction), and the comparison protocol with its advance rule. M5 opens with the configuration ladder PROVEN: every record needs 2 co-served tokens (repeat-use and single-first-use labels at Gamma >= 2), sibling-pair Q2 content needs 3, m-sibling groups need m+1 - a HARD capacity bound (n <= Gamma), confirmed by the engines: sibling pairs never occur at Gamma = 2 and >= 3-groups never below Gamma = 4, in exact evolutions and sampled trajectories alike. Recurrence is proven in the harmonic form: every object is reused as a parent infinitely often a.s. under U-growth, carrier chains are unbounded with Theta(log N) expected length - logarithmically sparse recurrence, exactly the CCP1 chain structure. The alphabet audit finds the engines' >= 3-group costing to be a declared lower-bound convention (theorems unaffected; readouts flagged; emission statements scoped to Gamma <= 3; the m-sibling alphabet is the recorded gap).

## Compact terminal return

```text
OD0-R56 OVERALL VERDICT: OD0_R56_PASS_H2_PREREGISTERED_AND_M5_OPENED
COMMITS (A / B / C-stamp): 6659b9f / in stamp / stamp follows
R55 STAMP PIN / WORKTREE / BELL2 / H2-H5 SENTINELS / H2 PDF HASH / HAND HASHES: PASS / CLEAN / false / parsed=false / verified untouched / 0
SECTIONS 4-6 FROZEN AT COMMIT A: yes; H2_PREREG_HASH: 298d21da179d8e6a08c485a52e74b70999ab732f6da7ef16ae54fa5bebb366cc
OBSERVABLES (9): O1-O3, O9 THEOREM-monotone; O6 THEOREM-limit; O7 inherits; O4, O5 READOUT; O8 NONE (shortcut reason recorded)
PREDICTION SET: P1, P2, P4, P5 THEOREM; P3, P6 THEOREM(bound)/READOUT(order)
ALPHABET SCOPE: PAIRWISE_CONVENTION scoped Gamma <= 3; engines' uniform-Q1-minimum convention recorded verbatim
LABEL CLASSIFICATION: repeat-use Gamma_min=2 (repeat only); single-first-use Gamma_min=2; sibling-pair Gamma_min=3; m-groups Gamma_min=m+1 (scoped)
P4 STATUS: PROVEN (hard bound) + engine-confirmed (sibling pair zero at Gamma=2; GE3 zero at Gamma<=3)
FIRST-APPEARANCE: exact traces at K<=4 all points (exemplar (2,0,0): P(single first-use by k=4) = 26/27); reachable counts by Gamma in certificates
RECURRENCE: PROVEN - reuse i.o. a.s.; chains unbounded; E[length after N bursts] = Theta(log N)
READOUT: max sibling group 4 (at Gamma=5); max parent reuse 17 (labeled)
HOSTILE CONTROLS: 8/8
DETERMINISTIC RERUN: IDENTICAL_BYTE_FOR_BYTE
OUTPUT MANIFEST SHA-256: in R56_PROVENANCE_STAMP.json
RECOMMENDED SINGLE R57 MOVE: ALPHABET_SCOPE scoped cleanly and P4 PROVEN, so per the R57 rule: open H2 under the sealed protocol (R56_H2_PREREGISTRATION.json, hash-pinned) - one comparison, no repair, mirroring R54: verify the Run3_Dijet hash, extract definitions, map by definition, adjudicate PASS/PARTIAL/FAIL with the model-family caveat. Content at Gamma >= 4 label granularity is outside the sealed comparison (scoped); the random-DAG cost problem stays queued unless H2 makes it the immediate dependency.
```
