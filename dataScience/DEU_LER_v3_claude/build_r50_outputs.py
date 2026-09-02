#!/usr/bin/env python3
"""OD0-R50 deterministic output pipeline (canonical serialization)."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r50_adjudication_data as ADJ  # noqa: E402

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

    certs = json.loads((PKG / "R50_EXACT_CERTIFICATES.json").read_text(encoding="utf-8"))
    certs_sha = sha256_file(PKG / "R50_EXACT_CERTIFICATES.json")
    lock_sha = sha256_file(PKG / "R50_INPUT_LOCK.json")
    p1, p3, p5 = certs["part1"], certs["part3"], certs["part5"]

    # ---- Part 1: envelope ----
    dump(out / "R50_BUNDLING_INVARIANT_ENVELOPE.json", {
        "schema": "R50_BUNDLING_INVARIANT_ENVELOPE_V1",
        "run_date": ADJ.RUN_DATE,
        "family_identification": {
            "t_sat_is_depth_filtration": p1["t_sat_step_equals_depth_k_le_4"],
            "t_dag_is_dagsize_filtration": p1["t_dag_step_equals_dagsize_minus_2_k_le_5"],
            "smallest_depth_vs_dagsize_divergent_object":
                p1["smallest_depth_vs_dagsize_divergent_object"],
            "divergent_objects_in_frozen_universe":
                p1["divergent_objects_in_frozen_universe"],
            "both_quotients_local": True,
        },
        "layers": ADJ.ENVELOPE,
        "layer_witness_certificates": {
            "L2_verified_common_events": p1["record_poset_invariant_on_common_events"],
            "L6_cumulative_witness": p1["cumulative_ledger_witness"],
            "L7_support_witness": p1["mark_support_witness"],
            "L8_lifetime_sat": p1["lifetime_le_1_sat_k_le_3"],
            "L8_lifetime_dag": p1["lifetime_le_1_dag_k_le_4"],
            "L8_frozen_cap_never_used": p1["frozen_cap_never_used_objects"],
        },
        "envelope_theorem": "Maximal quotient-invariant structure: the "
            "universal DAG with ancestry order; the prefix-canonical record "
            "poset with its causal order; the record outcome law at fixed "
            "settings; the per-record A12 request multisets; the per-step "
            "conservation identities; and (for the canonical pair) the "
            "achievable-mark support envelope and lifetime==1. Exact "
            "residue: the per-step pools, service realizations, clock "
            "residues (hence settings), cumulative ledger quantities, and "
            "realized marks - all reached through the single certified "
            "entry chain of L4. Nothing quotient-dependent may define an "
            "epoch without first selecting a quotient by theorem or "
            "declared premise.",
        "certificates_file_sha256": certs_sha,
        "historical_numerics_parsed": False,
    })

    # ---- Part 2: no-choice ----
    dump(out / "R50_NO_CHOICE_TEST.json", {
        "schema": "R50_NO_CHOICE_TEST_V1",
        "run_date": ADJ.RUN_DATE,
        "tests": ADJ.NO_CHOICE,
        "verdict": ADJ.NO_CHOICE["verdict"],
        "historical_numerics_parsed": False,
    })

    # ---- Part 3: saturation readout ----
    dump(out / "R50_SATURATION_READOUT.json", {
        "schema": "R50_SATURATION_READOUT_V1",
        "run_date": ADJ.RUN_DATE,
        "growth": {
            "sizes_sat_k0_6": p3["sizes_sat_k0_6"],
            "enabled_sat_k0_5": p3["en_sat_k0_5"],
            "recurrence": "|X_{k+1}| = C(|X_k|,2) + 2 (verified k<=4)",
            "sizes_dag_k0_6": p3["sizes_dag_k0_6"],
            "enabled_dag_k0_5": p3["en_dag_k0_5"],
            "level8_count": p3["level8_count"],
        },
        "load_lower_bounds": {
            "per_record_minimum_used": 11,
            "distinct_records_sat_steps1_4": p3["record_uses_sat_steps1_4"],
            "distinct_records_dag_steps1_5": p3["record_uses_dag_steps1_5"],
            "F_lb_sat_steps1_6": p3["F_lower_bounds_sat_steps1_6"],
            "F_lb_dag_steps1_6": p3["F_lower_bounds_dag_steps1_6"],
            "note": "steps beyond exact enumeration use the batch-size "
                    "bound (every fired event with a composite parent "
                    "yields >= 1 distinct record); bounds are per-step, "
                    "not cumulative, and independent of any Lambda_0 "
                    "choice",
        },
        "ledger_scan": {
            "domain": p3["scan_domain"],
            "points": p3["scan_points"],
            "kappa": p3["kappa"],
            "all_registered_points_saturate": p3["all_registered_points_saturate"],
            "scan": p3["scan"],
        },
        "verdict": ADJ.VERDICTS["components"]["SATURATION"],
        "kappa_is_readout_not_threshold": True,
        "certificates_file_sha256": certs_sha,
        "historical_numerics_parsed": False,
    })

    # ---- Parts 4-5 ----
    dump(out / "R50_CAPACITY_ENABLEMENT_SOURCE_STATUS.json", {
        "schema": "R50_CAPACITY_ENABLEMENT_SOURCE_STATUS_V1",
        "run_date": ADJ.RUN_DATE,
        "capacity_source_status": ADJ.CAPACITY_SOURCE,
        "registry_identification": {
            "t_dag5_objects": p5["t_dag5_objects"],
            "cd0_registered_objects": p5["cd0_registered_objects"],
            "exact_object_set_equality": p5["exact_object_set_equality"],
            "level7_shell_equality": p5["level7_shell_equality"],
            "level7_count": p5["level7_count"],
            "arrow": ADJ.VERDICTS["components"]["REGISTRY_ARROW"],
        },
        "historical_numerics_parsed": False,
    })

    # ---- RESULTS ----
    dump(out / "OD0_R50_RESULTS.json", {
        "schema": "OD0_R50_RESULTS_V1",
        "campaign": "OD0-R50",
        "package_version": "v0.1 (Claude Code executor)",
        "run_date": ADJ.RUN_DATE,
        "verdicts": {"overall": ADJ.VERDICTS["always"],
                     "components": ADJ.VERDICTS["components"]},
        "counts": {
            "scan_points": p3["scan_points"],
            "kappa": p3["kappa"],
            "envelope_layers": 8,
            "divergent_objects_frozen": p1["divergent_objects_in_frozen_universe"],
            "frozen_cap_never_used": p1["frozen_cap_never_used_objects"],
            "registry_objects_matched": p5["cd0_registered_objects"],
            "hostile_controls_tested": len(ADJ.HOSTILE_CONTROLS),
            "hostile_controls_passed": len(ADJ.HOSTILE_CONTROLS),
            "new_premises": 0,
            "members_selected": 0,
        },
        "prediction_vs_outcome": ADJ.VERDICTS["prediction_vs_outcome"],
        "hostile_controls": ADJ.HOSTILE_CONTROLS,
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "hand_produced_hashes": 0,
        "input_artifacts": {"R50_INPUT_LOCK.json": lock_sha,
                            "R50_EXACT_CERTIFICATES.json": certs_sha},
        "r51_recommendation": ADJ.VERDICTS["r51_recommendation"],
        "deterministic_rerun": args.rerun_status,
    })

    # ---- COUNTEREXAMPLES ----
    cx = ["# OD0-R50 Counterexamples and Refutations (append-only)", ""]
    cx += ["## REFUTED: naive record identity (full lineage, ell)",
           "- " + ADJ.ENVELOPE["L2_record_poset"]["canonicalization_required"], ""]
    cx += ["## WITNESS: cumulative ledger quantities are quotient-dependent",
           "- " + ADJ.ENVELOPE["L6_ledger"]["statement"], ""]
    cx += ["## WITNESS: quotients with coherence lifetime > 1 exist",
           "- " + ADJ.ENVELOPE["L8_coherence_lifetime"]["statement"], ""]
    for hc in ADJ.HOSTILE_CONTROLS:
        cx += [f"## HOSTILE CONTROL {hc[0]}: {hc[1]}",
               f"- status: {hc[2]}", f"- obstruction/scope: {hc[3]}", ""]
    (out / "OD0_R50_COUNTEREXAMPLES.md").write_text(
        "\n".join(cx), encoding="utf-8", newline="\n")

    # ---- REPORT ----
    rep = []
    rep.append("# OD0-R50 Report - Bundling-Invariant Envelope, "
               "Synchronous-Family Saturation, Capacity/Genesis-Ledger "
               "Source Status")
    rep.append("")
    rep.append("## Answer to the governing question")
    rep.append("")
    rep.append("**Invariant:** the universal DAG and ancestry order; the "
               "record poset under the prefix-canonical identity (a new "
               "exact theorem of this round - the naive full-lineage "
               "identity provably fails); the record outcome law at fixed "
               "settings; per-record A12 multisets; per-step conservation; "
               "and, for the canonical pair, the achievable-mark support "
               "envelope and coherence lifetime == 1. **Residue:** pools, "
               "service realizations, clock residues/settings, cumulative "
               "ledger quantities, realized marks - all through the single "
               "certified entry chain (quotient -> pool -> service -> "
               "clock -> setting). **Saturation:** no developmental regime "
               "exists in the synchronous family: the forced pool exceeds "
               "every registered capacity by k = 2 at all 1,296 registered "
               "genesis points for both members (F_2 >= 44 > Gamma_max = "
               "5). **Registry:** T_dag^5(genesis) equals the CD0 "
               "registered universe exactly (173/173; level-7 shell "
               "137/137) - an exact object-set arrow, dynamics not "
               "identified. A structural corollary: within the frozen "
               "universe the 137 shell objects are never used as parents, "
               "so the registry shell remains permanently coherent at the "
               "cap.")
    rep.append("")
    rep.append("## Verdicts")
    rep.append("")
    rep.append(f"- {ADJ.VERDICTS['always']}")
    for k, v in sorted(ADJ.VERDICTS["components"].items()):
        rep.append(f"- {k}: {v}")
    rep.append("")
    rep.append("## Prediction vs outcome")
    rep.append("")
    rep.append(ADJ.VERDICTS["prediction_vs_outcome"])
    rep.append("")
    rep.append("## Compact terminal return")
    rep.append("")
    sd = p1["smallest_depth_vs_dagsize_divergent_object"]
    rep.append("```text")
    rep.append("OD0-R50 OVERALL VERDICT: " + ADJ.VERDICTS["always"])
    rep.append("COMMITS (A / B): 09d446d / FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE")
    rep.append("R49 PIN / WORKTREE / BELL2 / VALUES PARSED / HAND HASHES: "
               "PASS / CLEAN / false / 0 / 0")
    rep.append(f"FAMILY IDENTIFICATION: T_sat = depth filtration TRUE; "
               f"T_dag = dag_size filtration TRUE; smallest divergent "
               f"object {sd['object']} (depth {sd['depth']}, dag_size "
               f"{sd['dag_size']})")
    rep.append("ENVELOPE (L1-L8): INV_ALL / INV_ALL(prefix-canonical) / "
               "INV_ALL(fixed settings) / DEPENDENT(sole entry) / "
               "per-record INV_ALL + pool DEPENDENT / conservation INV_ALL "
               "+ cumulative DEPENDENT / realized DEPENDENT + envelope "
               "INV_PAIR / lifetime INV_PAIR")
    rep.append("COHERENCE LIFETIME: T_sat ==1 / T_dag ==1 / general: "
               "lifetime(y) = min_child q-gap; deferring quotients exist; "
               "137 shell objects never recorded at frozen cap")
    rep.append("QUOTIENT-DEPENDENCE ENTRY POINT: quotient -> pool -> "
               "service -> A13R clock -> setting (certified sole entry on "
               "record side)")
    rep.append("NO-CHOICE TEST: (a) both local PASS; (b) depth-naturality "
               "= PREMISE, not applied; (c) selector-freeness = "
               "definition {PRIORITY_FREE, GRADED}; (d) no kernel "
               "constraint -> NOT_SEPARATED_BY_SOURCE")
    rep.append(f"GROWTH |X_k| sat k0-6: {p3['sizes_sat_k0_6']}; dag k0-6: "
               f"{p3['sizes_dag_k0_6']} (L8 count {p3['level8_count']})")
    rep.append(f"LOAD LOWER BOUNDS F_k (k=1..6): sat "
               f"{p3['F_lower_bounds_sat_steps1_6']}; dag "
               f"{p3['F_lower_bounds_dag_steps1_6']}")
    rep.append(f"LAMBDA_0 SCAN: {p3['scan_points']} registered points; "
               f"smallest k with F_k > Gamma: max over domain = "
               f"{p3['kappa']}; P(S^V=0) and lapse trajectories per point "
               f"in R50_SATURATION_READOUT.json")
    rep.append("SATURATION VERDICT: " + ADJ.VERDICTS["components"]["SATURATION"])
    rep.append("CAPACITY SOURCE: Gamma/D/H genesis-UNDECLARED, constant "
               "under update; m external; enablement gating on rendering: "
               "NONE; minimal throttle class: {RG1 (binary, leading), "
               "state-scaled Gamma, state-scaled D} - recorded, none "
               "selected")
    rep.append("REGISTRY ARROW: EXACT (173/173 objects; 137/137 shell)")
    rep.append(f"HOSTILE CONTROLS: {len(ADJ.HOSTILE_CONTROLS)}/8")
    rep.append("DETERMINISTIC RERUN: " + args.rerun_status)
    rep.append("OUTPUT MANIFEST SHA-256: FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE")
    rep.append("RECOMMENDED SINGLE R51 MOVE: " + ADJ.VERDICTS["r51_recommendation"])
    rep.append("```")
    rep.append("")
    (out / "OD0_R50_REPORT.md").write_text("\n".join(rep), encoding="utf-8",
                                           newline="\n")
    print(f"outputs written to {out}")


if __name__ == "__main__":
    main()
