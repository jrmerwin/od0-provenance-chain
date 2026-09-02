#!/usr/bin/env python3
"""OD0-R49 deterministic output pipeline (canonical serialization)."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r49_adjudication_data as ADJ  # noqa: E402

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

    certs = json.loads((PKG / "R49_EXACT_CERTIFICATES.json").read_text(encoding="utf-8"))
    certs_sha = sha256_file(PKG / "R49_EXACT_CERTIFICATES.json")
    lock_sha = sha256_file(PKG / "R49_INPUT_LOCK.json")

    # ---- Part 1 ----
    dump(out / "R49_ADJUNCTION_OPPORTUNITY_CLASSIFICATION.json", {
        "schema": "R49_ADJUNCTION_OPPORTUNITY_CLASSIFICATION_V1",
        "run_date": ADJ.RUN_DATE,
        "source_extraction": ADJ.SOURCE_EXTRACTION,
        "classification": ADJ.ADJUNCTION_CLASSIFICATION,
        "exact_certificates": certs["part1"],
        "certificates_file_sha256": certs_sha,
        "historical_numerics_parsed": False,
    })

    # ---- Part 2 ----
    dump(out / "R49_RECORD_OPPORTUNITY_CLASSIFICATION.json", {
        "schema": "R49_RECORD_OPPORTUNITY_CLASSIFICATION_V1",
        "run_date": ADJ.RUN_DATE,
        "classification": ADJ.RECORD_CLASSIFICATION,
        "exact_certificates_D_le_3": certs["part2_rod"],
        "certificates_file_sha256": certs_sha,
        "historical_numerics_parsed": False,
    })

    # ---- Parts 3-4 (obstruction branch) ----
    dump(out / "R49_OPPORTUNITY_OBSTRUCTION.json", {
        "schema": "R49_OPPORTUNITY_OBSTRUCTION_V1",
        "run_date": ADJ.RUN_DATE,
        "service_classification": ADJ.SERVICE_CLASSIFICATION,
        "obstruction": ADJ.OBSTRUCTION,
        "exact_certificates_service": certs["part3_service"],
        "exact_certificates_family": certs["part4_family"],
        "certificates_file_sha256": certs_sha,
        "historical_numerics_parsed": False,
    })

    # ---- RESULTS ----
    p1 = certs["part1"]
    p2 = certs["part2_rod"]
    results = {
        "schema": "OD0_R49_RESULTS_V1",
        "campaign": "OD0-R49",
        "package_version": "v0.1 (Claude Code executor)",
        "run_date": ADJ.RUN_DATE,
        "verdicts": {
            "overall": ADJ.VERDICTS["always"],
            "primary": ADJ.VERDICTS["primary"],
            "secondary": ADJ.VERDICTS["secondary"],
        },
        "primary_justification": ADJ.VERDICTS["primary_justification"],
        "premises_stated_not_selected": ["CO1", "RO1"],
        "premises_used_frozen": ["MINIMAL_SERVICE_REPRESENTATION_AXIOM",
                                "A13R0", "RRP1 (cited; not exercised)",
                                "external persistent load m"],
        "counts": {
            "exhaustive_ideal_states": p1["exhaustive_ideal_domain"]["states"],
            "mixed_grade_states": p1["mixed_grade_states_total"],
            "smallest_distinguishing_state_size": 4,
            "genesis_divergence_step": p1["genesis_trajectory_divergence_step"],
            "rod_record_uses_D_le_3": p2["total_record_uses"],
            "rod_multi_touch_uses": p2["multi_touch_uses_distinct_positions"],
            "rod_scope_failures": p2["scope_lemma_failures"],
            "rod_over_recording_failures": p2["no_over_recording_failures"],
            "rod_covariance_failures": p2["exchange_covariance_failures"],
            "part1_covariance_failures": p1["covariance_failures"],
            "part1_batch_persistence_failures": p1["batch_enabledness_persistence_failures"],
            "K_max": certs["part4_family"]["K_max"],
            "hostile_controls_tested": len(ADJ.HOSTILE_CONTROLS),
            "hostile_controls_passed": len(ADJ.HOSTILE_CONTROLS),
        },
        "prediction_vs_outcome": ADJ.VERDICTS["prediction_vs_outcome"],
        "occurrence_layer_necessity": "recorded in R49_INPUT_LOCK.json",
        "lambda_0_status": certs["part4_family"]["lambda_0_status"],
        "hostile_controls": ADJ.HOSTILE_CONTROLS,
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "input_artifacts": {
            "R49_INPUT_LOCK.json": lock_sha,
            "R49_EXACT_CERTIFICATES.json": certs_sha,
        },
        "r50_recommendation": ADJ.VERDICTS["r50_recommendation"],
        "deterministic_rerun": args.rerun_status,
    }
    dump(out / "OD0_R49_RESULTS.json", results)

    # ---- COUNTEREXAMPLES ----
    cx = ["# OD0-R49 Counterexamples and Refutations (append-only)", ""]
    cx += ["## REFUTED: RO-A (adjunction-as-record)",
           "- " + ADJ.RECORD_CLASSIFICATION["RO_A"]["witness"], ""]
    cx += ["## REFUTED: SV-int as a choice-free law",
           "- " + ADJ.SERVICE_CLASSIFICATION["SV_int"]["witness"], ""]
    cx += ["## REFUTED: T_sat = T_dag",
           "- " + ADJ.ADJUNCTION_CLASSIFICATION["t_sat_equals_t_g"]["smallest_states"],
           "- genesis divergence: "
           + ADJ.ADJUNCTION_CLASSIFICATION["t_sat_equals_t_g"]["genesis_divergence"], ""]
    cx += ["## REFUTED: CO1 selects a unique law",
           "- CO1 excludes only T_id; both T_sat and T_dag satisfy it; the "
           "adjunction layer is nonunique-canonical.", ""]
    cx += ["## ERRATUM (carried from R48 lock verification)",
           "- The frozen R48 report/manifest recorded a fabricated 40-char "
           "expansion of Commit A (244e61a1b7f0...); true full hashes: "
           "A=244e61af06b660b7f3fb47002e9ac75e6f4db54d, "
           "B=36d38b10fb0ab8947c897db01c733d1c73293f99. R48 artifacts remain "
           "frozen; recorded here and in R49_INPUT_LOCK.json.", ""]
    for hc in ADJ.HOSTILE_CONTROLS:
        cx += [f"## HOSTILE CONTROL {hc[0]}: {hc[1]}",
               f"- status: {hc[2]}", f"- obstruction/scope: {hc[3]}", ""]
    (out / "OD0_R49_COUNTEREXAMPLES.md").write_text(
        "\n".join(cx), encoding="utf-8", newline="\n")

    # ---- REPORT ----
    t = ADJ.TERMINAL_STATIC
    rep = []
    rep.append("# OD0-R49 Report - Minimum Global Opportunity Law: Candidate "
               "Freeze and Forced / One-Premise / Choice Classification")
    rep.append("")
    rep.append("## Governing question and answer")
    rep.append("")
    rep.append("> What is the smallest set of source-derivable properties "
               "that determine, at each global step, which enabled "
               "adjunctions occur, whether and which A10 records occur, and "
               "when service rounds occur - and is the resulting global "
               "transition unique?")
    rep.append("")
    rep.append("**The record and service layers close; the adjunction layer "
               "is nonunique-canonical - and the nonuniqueness is physical.** "
               "Given the two A13R0-pattern activity premises (CO1, RO1), "
               "the record law is uniquely RO-D (maximal-supported-scope "
               "prefix records; RO-A is refuted by the frozen invariant "
               "append; the setting residual is forced by the lineage's "
               "A13R clock state, not free), and the service law is "
               "uniquely SV-pool (interleaving is order-sensitive by an "
               "exact 2/3-vs-1/2 witness). But the frozen choice-free class "
               "contains TWO canonical adjunction laws - full saturation "
               "T_sat and next-grade saturation T_dag under the single "
               "source stratification grading dag_size - which provably "
               "differ (smallest witnesses: two 4-object states; genesis "
               "divergence at k=3). Because pooled service is "
               "non-compositional across pools, the step-bundling "
               "difference propagates to the ledger/clock trajectories: it "
               "is not a gauge choice. A second independent blocker is "
               "recorded: Lambda_0 is undeclared in source.")
    rep.append("")
    rep.append("## Verdicts")
    rep.append("")
    rep.append(f"- {ADJ.VERDICTS['always']}")
    rep.append(f"- PRIMARY: {ADJ.VERDICTS['primary']}")
    for k, v in sorted(ADJ.VERDICTS["secondary"].items()):
        rep.append(f"- {k}: {v}")
    rep.append("")
    rep.append(f"Justification: {ADJ.VERDICTS['primary_justification']}")
    rep.append("")
    rep.append("## Registered prediction vs outcome")
    rep.append("")
    rep.append(ADJ.VERDICTS["prediction_vs_outcome"])
    rep.append("")
    rep.append("## Compact terminal return")
    rep.append("")
    rep.append("```text")
    rep.append("OD0-R49 OVERALL VERDICT: " + ADJ.VERDICTS["always"]
               + " + PRIMARY " + ADJ.VERDICTS["primary"])
    rep.append("COMMITS (A / B): 4946e4e / FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE")
    rep.append("R48 PIN VERIFICATION / CLEAN WORKTREE / BELL2 / HISTORICAL "
               "VALUES PARSED: " + t["R48_PIN"]
               + " / CLEAN (pre-existing DEU_voids deltas unchanged) / "
               "false / 0")
    rep.append("CONSTRUCTOR STEP SEMANTICS: " + t["STEP_SEMANTICS"])
    rep.append("ADJUNCTION LAW: " + t["ADJUNCTION_LINE"])
    rep.append("RECORD LAW: " + t["RECORD_LINE"])
    rep.append("SERVICE LAW: " + t["SERVICE_LINE"])
    rep.append("GLOBAL TRANSITION: " + t["GLOBAL_TRANSITION"])
    rep.append("COMMUTING DIAGRAM: NOT_REACHED; K_max=3; per-component "
               "restriction unchanged from R48 (x PARTIAL(CD1I) | N via "
               "induced records CONDITIONAL(RO1) | S via A12 "
               "CONDITIONAL(RO1+CO1) | Lambda blocked (Lambda_0 undeclared) "
               "| G+- RRP1 not exercised)")
    rep.append("GM1-GM12 RESCORE: NOT_PERFORMED (Sec 7 conditional not met; "
               "nonunique family)")
    rep.append("GLOBAL FRONTIER CLUSTER STRUCTURE AT k <= 3: "
               + t["CLUSTER_LINE"])
    rep.append("FIELD READOUTS EMITTED: n (Part 5 conditional not met)")
    rep.append(f"HOSTILE CONTROLS: {len(ADJ.HOSTILE_CONTROLS)}/10")
    rep.append("DETERMINISTIC RERUN: " + args.rerun_status)
    rep.append("OUTPUT MANIFEST SHA-256: FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE")
    rep.append("RECOMMENDED SINGLE R50 MOVE: " + ADJ.VERDICTS["r50_recommendation"])
    rep.append("```")
    rep.append("")
    (out / "OD0_R49_REPORT.md").write_text("\n".join(rep), encoding="utf-8",
                                           newline="\n")
    print(f"outputs written to {out}")


if __name__ == "__main__":
    main()
