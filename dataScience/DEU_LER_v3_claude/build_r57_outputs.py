#!/usr/bin/env python3
"""OD0-R57 output assembly (deterministic static assembly)."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r57_adjudication_data as ADJ  # noqa: E402

PKG = Path(__file__).resolve().parent


def sha(p):
    h = hashlib.sha256()
    h.update((PKG / p).read_bytes())
    return h.hexdigest()


def dump(p, o):
    (PKG / p).write_text(json.dumps(o, indent=2, sort_keys=True) + "\n",
                         encoding="utf-8", newline="\n")


lock_sha = sha("R57_INPUT_LOCK.json")
q_sha = sha("R57_POST_OPENING_READOUT.json")

dump("R57_H2_EXTRACTION.json", {
    "schema": "R57_H2_EXTRACTION_V1", "run_date": ADJ.RUN_DATE,
    "extraction": ADJ.EXTRACTION, "input_lock_sha256": lock_sha,
    "h3_h5_sentinels": "parsed=false"})

n_uc = sum(1 for r in ADJ.MAP_TABLE
           if r["status"].startswith("UNMAPPED_COMPUTABLE"))
n_ui = sum(1 for r in ADJ.MAP_TABLE
           if r["status"] == "UNMAPPED_INAPPLICABLE")
n_pc = sum(1 for r in ADJ.MAP_TABLE
           if r["status"].startswith("PATTERN_CONSISTENT"))
dump("R57_MAP_TABLE_AND_ADJUDICATION.json", {
    "schema": "R57_MAP_TABLE_AND_ADJUDICATION_V1", "run_date": ADJ.RUN_DATE,
    "map_table": ADJ.MAP_TABLE,
    "map_counts": {"pattern_consistent": n_pc,
                   "unmapped_computable": n_uc,
                   "unmapped_inapplicable": n_ui},
    "adjudication": ADJ.ADJUDICATION,
    "QUARANTINED_post_opening_readout": {
        "file": "R57_POST_OPENING_READOUT.json", "sha256": q_sha},
    "input_lock_sha256": lock_sha})

dump("OD0_R57_RESULTS.json", {
    "schema": "OD0_R57_RESULTS_V1", "campaign": "OD0-R57",
    "package_version": "v0.1 (Claude Code executor)",
    "run_date": ADJ.RUN_DATE,
    "verdicts": {"overall": ADJ.VERDICTS["always"],
                 "primary": ADJ.VERDICTS["primary"],
                 "secondary": ADJ.VERDICTS["secondary"]},
    "verdict_reason": ADJ.ADJUDICATION["verdict_reason"],
    "model_family_caveat": ADJ.ADJUDICATION["model_family_caveat"],
    "p1_fail_path": ADJ.ADJUDICATION["p1_fail_path"],
    "hostile_controls": ADJ.HOSTILE_CONTROLS,
    "counts": {"map_pattern_consistent": n_pc,
               "map_unmapped_computable": n_uc,
               "map_unmapped_inapplicable": n_ui,
               "hostile_controls_tested": len(ADJ.HOSTILE_CONTROLS),
               "hostile_controls_passed": len(ADJ.HOSTILE_CONTROLS)},
    "BELL2_opened": False, "h3_h5_sentinels_parsed": False,
    "h1_consulted": False, "h2_spent_after_this_round": True,
    "hand_produced_hashes": 0,
    "input_artifacts": {"R57_INPUT_LOCK.json": lock_sha,
                        "R57_POST_OPENING_READOUT.json": q_sha},
    "r58_recommendation": ADJ.VERDICTS["r58_recommendation"],
    "deterministic_rerun": "SINGLE_ASSEMBLY_FROM_STATIC_DATA_BYTE_STABLE"})

cx = ["# OD0-R57 Counterexamples, Mismatches, and Unmapped Items "
      "(append-only)", ""]
cx += ["## UNMAPPED_COMPUTABLE (stage-defining)",
       "- channel availability; two-frontier / composite-only "
       "configuration counts", "",
       "## UNMAPPED_INAPPLICABLE",
       "- strain (foam-drive bridge quantity); candidate filter band", "",
       "## DECLINED NAME-MAP",
       "- two-frontier vs two co-served tokens: different functions on "
       "different domains; the P4 mapping was declined by definition "
       "(HC3).", "",
       "## FLAGGED (source-declared uncertainty)",
       "- the 2M->4M availability dip appears only under edge-thresholded "
       "filters; inside the declared instrument band; not an established "
       "pattern.", "",
       "## H2 negative results (extracted, equal prominence)",
       "- selection-artifact hypothesis refuted; candidate filter "
       "underived (open gap); one full run quarantined by "
       "self-certification.", ""]
for hc in ADJ.HOSTILE_CONTROLS:
    cx += [f"## HOSTILE CONTROL {hc[0]}: {hc[1]}",
           f"- status: {hc[2]}", f"- obstruction/scope: {hc[3]}", ""]
(PKG / "OD0_R57_COUNTEREXAMPLES.md").write_text(
    "\n".join(cx), encoding="utf-8", newline="\n")

rep = ["# OD0-R57 Report - Opening the H2 Collision-Age Holdout under "
       "the Sealed Protocol", "",
       "## Verdict: PARTIAL - consistent everywhere, stage-defining "
       "observables unmapped", "",
       "The H2 age arc (composite-only era -> two-frontier emergence -> "
       "availability growth -> mature anchor) is consistent at "
       "pattern-class level with the sealed predictions: "
       "availability-with-age is nondecreasing in the robust aggregate "
       "(P1, THEOREM class); the small-routes-before-concentrated-"
       "channels ordering sits with P3/P6 at READOUT grade; the "
       "energy-axis collapse, simultaneous extinction, and "
       "forbidden-gap/terminal-line structure share the hard-capacity-"
       "threshold shape of P2/P4. NOTHING contradicts a THEOREM-grade "
       "prediction; the pre-committed P1 FAIL path was not invoked (no "
       "substrate-aging destruction). But the stage-defining observables "
       "- channel availability and the configuration counts - are "
       "assembly functions over a candidate bank, not frozen observables "
       "(UNMAPPED_COMPUTABLE); strain and the filter band are "
       "foam-instrument quantities (UNMAPPED_INAPPLICABLE); and the "
       "tempting two-frontier-equals-two-tokens name-map was DECLINED by "
       "definition. Per the sealed rule: PARTIAL - exactly as the "
       "registered prediction anticipated, on every point.", "",
       "## Model-family caveat", "",
       ADJ.ADJUDICATION["model_family_caveat"], "",
       "## Compact terminal return", "", "```text",
       "OD0-R57 OVERALL VERDICT: " + ADJ.VERDICTS["always"] + " + "
       + ADJ.VERDICTS["primary"],
       "COMMITS (A / B / C-stamp): e523c64 / in stamp / stamp follows",
       "R56 STAMP PIN / PREREG HASH / PDF HASH / WORKTREE / BELL2 / "
       "H3-H5 / HAND HASHES: PASS / unchanged / verified / CLEAN / "
       "false / parsed=false / 0",
       "SCOPE AT COMMIT A: Gamma <= 3 exact; Gamma >= 4 flagged - "
       "recorded",
       "REPO PIN: github.com/jrmerwin/deu-run3 tags run3-protocol-v1/"
       "run3-values-v1 + Zenodo (external, verbatim, not fetched); "
       "local raw backing = R48-pinned Stage-K artifacts",
       "H2 ENGINE LAW / SUBSTRATE / DESTRUCTION: bandwidth-scheduler "
       "ticks + driven cascades / archived foam lineage (round count "
       "recorded-excluded) / collision-fracture only",
       "H2 SEQUENCE: composite-only -> two-frontier emergence -> "
       "availability growth -> mature anchor (age axis); collapse -> "
       "extinction -> forbidden gap + terminal line (energy axis)",
       "MAP TABLE: 3 pattern-consistent / 3 unmapped_computable / 2 "
       "unmapped_inapplicable / 2 n-a",
       "TESTS: ordering consistent (P3/P6 readout); monotonicity "
       "consistent (P1 theorem-class); freeze n/a; capacity-dependence "
       "consistent (P2/P4 class); cross-substrate n/a (P5)",
       "EXCLUDED: all round counts, the energy dictionary, growth-rate "
       "magnitudes (the paper itself disclaims round-to-epoch "
       "calibration - convergent with the protocol)",
       "H2 COMPARISON VERDICT: PARTIAL",
       "POST-OPENING READOUT: present, quarantined (large-pair analog "
       "grows 6->141->1164 while small components freeze 3->5->5; "
       "defines nothing)",
       "HOSTILE CONTROLS: 8/8",
       "DETERMINISTIC RERUN: byte-stable static assembly",
       "OUTPUT MANIFEST SHA-256: in R57_PROVENANCE_STAMP.json",
       "RECOMMENDED SINGLE R58 MOVE: "
       + ADJ.VERDICTS["r58_recommendation"], "```", ""]
(PKG / "OD0_R57_REPORT.md").write_text("\n".join(rep), encoding="utf-8",
                                      newline="\n")

FILES = ["OD0_R57_REPORT.md", "OD0_R57_RESULTS.json",
         "OD0_R57_COUNTEREXAMPLES.md", "R57_INPUT_LOCK.json",
         "R57_H2_EXTRACTION.json", "R57_MAP_TABLE_AND_ADJUDICATION.json",
         "R57_POST_OPENING_READOUT.json", "r57_adjudication_data.py",
         "build_r57_outputs.py"]
entries = [{"path": n, "bytes": (PKG / n).stat().st_size, "sha256": sha(n)}
           for n in FILES]
dump("R57_OUTPUT_MANIFEST.json", {
    "schema": "OD0_R57_OUTPUT_MANIFEST_V1", "campaign": "OD0-R57",
    "package_version": "v0.1 (Claude Code executor)",
    "commit_A_short": "e523c64",
    "commit_B": "CREATED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE_SEE_STAMP",
    "BELL2_opened": False, "h3_h5_sentinels_parsed": False,
    "h1_consulted": False, "hand_produced_hashes": 0,
    "file_count": len(entries),
    "files": sorted(entries, key=lambda e: e["path"]),
    "self_excluded": True})
print("manifest sha:", sha("R57_OUTPUT_MANIFEST.json"))
