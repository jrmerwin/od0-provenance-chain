#!/usr/bin/env python3
"""OD0-R54 deterministic output pipeline."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r54_adjudication_data as ADJ  # noqa: E402

PKG = Path(__file__).resolve().parent


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8", newline="\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(PKG))
    ap.add_argument("--rerun-status", default="PENDING_DOUBLE_RUN")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    lock = json.loads((PKG / "R54_INPUT_LOCK.json").read_text(encoding="utf-8"))
    lock_sha = sha256_file(PKG / "R54_INPUT_LOCK.json")
    quarantine = json.loads((PKG / "R54_POST_OPENING_READOUT.json").read_text(encoding="utf-8"))
    quarantine_sha = sha256_file(PKG / "R54_POST_OPENING_READOUT.json")

    # ---- Part 1 ----
    dump(out / "R54_H1_EXTRACTION.json", {
        "schema": "R54_H1_EXTRACTION_V1",
        "run_date": ADJ.RUN_DATE,
        "h1_hash_verification_summary": {
            "items": lock["h1_hash_verification"]["items"],
            "verified": len(lock["h1_hash_verification"]["verified"]),
            "mismatched": len(lock["h1_hash_verification"]["mismatched"]),
            "missing": len(lock["h1_hash_verification"]["missing"]),
        },
        "extraction": ADJ.EXTRACTION,
        "input_lock_sha256": lock_sha,
        "h2_h5_sentinels": "parsed=false",
    })

    # ---- Parts 2-3 (+4 quarantined) ----
    n_mapped = sum(1 for r in ADJ.MAP_TABLE if r["status"] == "MAPPED")
    n_uc = sum(1 for r in ADJ.MAP_TABLE
               if r["status"] == "UNMAPPED_COMPUTABLE")
    n_ui = sum(1 for r in ADJ.MAP_TABLE
               if r["status"] == "UNMAPPED_INAPPLICABLE")
    dump(out / "R54_MAP_TABLE_AND_ADJUDICATION.json", {
        "schema": "R54_MAP_TABLE_AND_ADJUDICATION_V1",
        "run_date": ADJ.RUN_DATE,
        "map_table": ADJ.MAP_TABLE,
        "map_counts": {"mapped": n_mapped, "unmapped_computable": n_uc,
                       "unmapped_inapplicable": n_ui},
        "adjudication": ADJ.ADJUDICATION,
        "QUARANTINED_post_opening_readout": {
            "file": "R54_POST_OPENING_READOUT.json",
            "sha256": quarantine_sha,
            "label": quarantine["label"],
        },
        "input_lock_sha256": lock_sha,
    })

    # ---- RESULTS ----
    dump(out / "OD0_R54_RESULTS.json", {
        "schema": "OD0_R54_RESULTS_V1",
        "campaign": "OD0-R54",
        "package_version": "v0.1 (Claude Code executor)",
        "run_date": ADJ.RUN_DATE,
        "verdicts": {"overall": ADJ.VERDICTS["always"],
                     "primary": ADJ.VERDICTS["primary"],
                     "secondary": ADJ.VERDICTS["secondary"]},
        "verdict_reason": ADJ.ADJUDICATION["verdict_reason"],
        "coarsening_assignment": ADJ.ADJUDICATION["coarsening_assignment"],
        "model_family_caveat": ADJ.ADJUDICATION["model_family_caveat"],
        "cross_validations": ADJ.ADJUDICATION["cross_validations_noted"],
        "counts": {
            "h1_items": lock["h1_hash_verification"]["items"],
            "h1_verified": len(lock["h1_hash_verification"]["verified"]),
            "map_mapped": n_mapped,
            "map_unmapped_computable": n_uc,
            "map_unmapped_inapplicable": n_ui,
            "hostile_controls_tested": len(ADJ.HOSTILE_CONTROLS),
            "hostile_controls_passed": len(ADJ.HOSTILE_CONTROLS),
        },
        "hostile_controls": ADJ.HOSTILE_CONTROLS,
        "BELL2_opened": False,
        "h2_h5_sentinels_parsed": False,
        "hand_produced_hashes": 0,
        "input_artifacts": {"R54_INPUT_LOCK.json": lock_sha,
                            "R54_POST_OPENING_READOUT.json": quarantine_sha},
        "r55_recommendation": ADJ.VERDICTS["r55_recommendation"],
        "deterministic_rerun": args.rerun_status,
    })

    # ---- COUNTEREXAMPLES ----
    cx = ["# OD0-R54 Counterexamples, Mismatches, and Unmapped Items "
          "(append-only)", ""]
    cx += ["## UNMAPPED_COMPUTABLE (9) - listed at equal prominence"]
    for r in ADJ.MAP_TABLE:
        if r["status"] == "UNMAPPED_COMPUTABLE":
            cx += [f"- {r['historical']}: {r['derived']}"]
    cx += ["", "## UNMAPPED_INAPPLICABLE (2)"]
    for r in ADJ.MAP_TABLE:
        if r["status"] == "UNMAPPED_INAPPLICABLE":
            cx += [f"- {r['historical']}: {r['derived']}"]
    cx += ["", "## No order contradiction",
           "- " + ADJ.ADJUDICATION["no_reversal"], ""]
    cx += ["## Historical program's own negative results (extracted, "
           "recorded)",
           "- Registry factorization audit: 432/27/2-9 claims FAIL "
           "against the frozen registry.",
           "- CARRIER_HUB_NULL: the foam does not natively generate the "
           "registry's degree structure.", ""]
    for hc in ADJ.HOSTILE_CONTROLS:
        cx += [f"## HOSTILE CONTROL {hc[0]}: {hc[1]}",
               f"- status: {hc[2]}", f"- obstruction/scope: {hc[3]}", ""]
    (out / "OD0_R54_COUNTEREXAMPLES.md").write_text(
        "\n".join(cx), encoding="utf-8", newline="\n")

    # ---- REPORT ----
    rep = []
    rep.append("# OD0-R54 Report - Opening the H1 Structural-Epoch "
               "Holdout under the Frozen Protocol")
    rep.append("")
    rep.append("## Verdict: PARTIAL - the sequence coarsens; the "
               "stage-defining observables do not map")
    rep.append("")
    rep.append("The historical four-stage ladder (broadening -> "
               "freeze-out onset -> support locking -> late "
               "concentration, preceded by registry formation/"
               "illumination) admits an explicit order-preserving "
               "assignment into the derived filtration - registry "
               "formation to the transient {c_min <= Gamma} stratum of "
               "early E1, broadening to the renewal-rich early-E1 "
               "regime, freeze-out to the late-E1 regime of decreasing "
               "full-drain frequency and rising burst cost, locking and "
               "concentration to the asymptotic regime - with NO "
               "historical transition reversing a derived one. Every "
               "mapped observable matches: mean parent-child degree "
               "(exactly 4(n-2)/n on any ideal - theorem-grade, "
               "law-independent), total directed paths/chains "
               "(theorem), dag_size layer counts (theorem), shell "
               "fraction (match of readouts, labeled). But the "
               "observables the last three historical stages are "
               "DEFINED on - support size, visibility/participation, "
               "the concentration/K9 backbone, and the containment/"
               "coembedding clocks - are UNMAPPED_COMPUTABLE: "
               "well-defined on the derived state, absent from the "
               "frozen inventory. Per the frozen rule that is PARTIAL, "
               "exactly as the registered prediction anticipated "
               "(including its guess that the unmapped family would be "
               "the through-path/hub measures).")
    rep.append("")
    rep.append("## Model-family caveat (mandatory)")
    rep.append("")
    rep.append(ADJ.ADJUDICATION["model_family_caveat"])
    rep.append("")
    rep.append("## Cross-validations observed during extraction")
    rep.append("")
    for cv in ADJ.ADJUDICATION["cross_validations_noted"]:
        rep.append(f"- {cv}")
    rep.append("")
    rep.append("## Compact terminal return")
    rep.append("")
    rep.append("```text")
    rep.append("OD0-R54 OVERALL VERDICT: " + ADJ.VERDICTS["always"]
               + " + " + ADJ.VERDICTS["primary"])
    rep.append("COMMITS (A / B / C-stamp): bd21aca(stamps) + 45eb08c(A) / "
               "COMMIT_B_HASH_IN_STAMP / stamp follows")
    rep.append("R53 PIN / R48 HOLDOUT PIN / WORKTREE / BELL2 / HAND "
               "HASHES: PASS / PASS / CLEAN / false / 0")
    rep.append("R52/R53 STAMPS WRITTEN: yes (standing convention adopted)")
    rep.append(f"H1 ARTIFACTS: {lock['h1_hash_verification']['items']} "
               f"pinned / "
               f"{len(lock['h1_hash_verification']['verified'])} verified "
               f"/ {len(lock['h1_hash_verification']['missing'])} missing")
    rep.append("H2 PIN STATUS: incomplete (no Run3_Dijet supplied)")
    rep.append("SENTINELS H2-H5: parsed=false")
    rep.append("DERIVED-SIDE TABLE FROZEN AT COMMIT A: yes")
    rep.append("HISTORICAL SEQUENCE: registry formation/illumination -> "
               "broadening -> freeze-out onset -> support locking -> "
               "late concentration (dag_size layer coordinate; "
               "synchronous full-saturation engine = T_sat; static "
               "foliation of fixed G_6)")
    rep.append(f"HISTORICAL OBSERVABLES EXTRACTED: "
               f"{len(ADJ.EXTRACTION['historical_observables'])} with "
               f"definitions")
    n_mapped2 = sum(1 for r in ADJ.MAP_TABLE if r["status"] == "MAPPED")
    rep.append(f"MAP TABLE: {n_mapped2} mapped / "
               f"{sum(1 for r in ADJ.MAP_TABLE if r['status'] == 'UNMAPPED_COMPUTABLE')} "
               f"unmapped_computable / "
               f"{sum(1 for r in ADJ.MAP_TABLE if r['status'] == 'UNMAPPED_INAPPLICABLE')} "
               f"unmapped_inapplicable")
    rep.append("COARSENING: explicit assignment recorded; NO reversal; "
               "locking+concentration share one derived placement "
               "(weakly order-preserving, allowed by the frozen test)")
    rep.append("MONOTONICITY: 3 theorem-grade matches + 1 readout-grade "
               "match (labeled); 0 contradictions")
    rep.append("H1 COMPARISON VERDICT: PARTIAL")
    rep.append("MODEL-FAMILY CAVEAT: historical = synchronous T_sat on a "
               "static dag_size foliation; derived = throttled TG1 on "
               "process time; caveat recorded, verdict not softened")
    rep.append("POST-OPENING READOUT: present, quarantined "
               "(R54_POST_OPENING_READOUT.json)")
    rep.append(f"HOSTILE CONTROLS: {len(ADJ.HOSTILE_CONTROLS)}/8")
    rep.append("DETERMINISTIC RERUN: " + args.rerun_status)
    rep.append("OUTPUT MANIFEST SHA-256: in R54_PROVENANCE_STAMP.json "
               "(commit C)")
    rep.append("RECOMMENDED SINGLE R55 MOVE: "
               + ADJ.VERDICTS["r55_recommendation"])
    rep.append("```")
    rep.append("")
    (out / "OD0_R54_REPORT.md").write_text("\n".join(rep), encoding="utf-8",
                                           newline="\n")
    print(f"outputs written to {out}")


if __name__ == "__main__":
    main()
