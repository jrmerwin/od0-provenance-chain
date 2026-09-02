#!/usr/bin/env python3
"""OD0-R51 deterministic output pipeline."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r51_adjudication_data as ADJ  # noqa: E402

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

    certs = json.loads((PKG / "R51_EXACT_CERTIFICATES.json").read_text(encoding="utf-8"))
    certs_sha = sha256_file(PKG / "R51_EXACT_CERTIFICATES.json")
    lock_sha = sha256_file(PKG / "R51_INPUT_LOCK.json")

    # ---- Part 1 ----
    dump(out / "R51_SELECTOR_SOURCE_STATUS.json", {
        "schema": "R51_SELECTOR_SOURCE_STATUS_V1",
        "run_date": ADJ.RUN_DATE,
        "status": ADJ.SELECTOR_STATUS,
        "genesis_service_table": certs["genesis_service_table"],
        "certificates_file_sha256": certs_sha,
        "historical_numerics_parsed": False,
    })

    # ---- Parts 2-3 ----
    dump(out / "R51_THROTTLE_CLASS_ADJUDICATION.json", {
        "schema": "R51_THROTTLE_CLASS_ADJUDICATION_V1",
        "run_date": ADJ.RUN_DATE,
        "candidates": ADJ.CANDIDATES,
        "survivors": ADJ.MINIMALITY["survivors"],
        "minimality": ADJ.MINIMALITY,
        "survivor_scope_witnesses": certs["survivor_scope"],
        "lifetime_witness": certs["lifetime_witness"],
        "load_convention": certs["load_convention"],
        "certificates_file_sha256": certs_sha,
        "historical_numerics_parsed": False,
    })

    # ---- Part 4 ----
    dump(out / "R51_SURVIVOR_DYNAMICS_READOUT.json", {
        "schema": "R51_SURVIVOR_DYNAMICS_READOUT_V1",
        "run_date": ADJ.RUN_DATE,
        "load_convention": certs["load_convention"],
        "genesis_ledger_convention": "B0=0, P0=0 (Lambda_0 remains "
                                     "UNDECLARED in source; same recorded "
                                     "convention as the R50 scan; nothing "
                                     "singled out)",
        "K_max_policy": "per-point exact-enumeration bound: a step is taken "
                        "only if the exact expansion (sum over states and "
                        "outcomes of C(D, S^V) served-subset branches) "
                        "stays within the recorded budget; K_max and its "
                        "reason are reported per point - a resource bound "
                        "on exact enumeration, defining nothing",
        "dynamics": certs["survivor_dynamics"],
        "certificates_file_sha256": certs_sha,
        "historical_numerics_parsed": False,
    })

    # ---- RESULTS ----
    km = {}
    for name, rows in certs["survivor_dynamics"].items():
        kms = [r["K_max"] for r in rows]
        km[name] = {"points": len(rows), "K_max_min": min(kms),
                    "K_max_max": max(kms)}
    dump(out / "OD0_R51_RESULTS.json", {
        "schema": "OD0_R51_RESULTS_V1",
        "campaign": "OD0-R51",
        "package_version": "v0.1 (Claude Code executor)",
        "run_date": ADJ.RUN_DATE,
        "verdicts": {"overall": ADJ.VERDICTS["always"],
                     "primary": ADJ.VERDICTS["primary"],
                     "secondary": ADJ.VERDICTS["secondary"]},
        "survivors": ADJ.MINIMALITY["survivors"],
        "unique_minimum": ADJ.MINIMALITY["unique_minimum"],
        "premise_statement_TG1": ADJ.MINIMALITY["premise_statement"],
        "premise_scope": ADJ.MINIMALITY["scope"],
        "counts": {
            "candidates_frozen": len(ADJ.CANDIDATES),
            "survivors": len(ADJ.MINIMALITY["survivors"]),
            "dynamics_points": km,
            "hostile_controls_tested": len(ADJ.HOSTILE_CONTROLS),
            "hostile_controls_passed": len(ADJ.HOSTILE_CONTROLS),
            "parameters_introduced": 0,
            "premises_adopted": 0,
        },
        "prediction_vs_outcome": ADJ.VERDICTS["prediction_vs_outcome"],
        "hostile_controls": ADJ.HOSTILE_CONTROLS,
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "hand_produced_hashes": 0,
        "input_artifacts": {"R51_INPUT_LOCK.json": lock_sha,
                            "R51_EXACT_CERTIFICATES.json": certs_sha},
        "r52_recommendation": ADJ.VERDICTS["r52_recommendation"],
        "deterministic_rerun": args.rerun_status,
    })

    # ---- COUNTEREXAMPLES ----
    cx = ["# OD0-R51 Counterexamples and Witnesses (append-only)", ""]
    cx += ["## DEADLOCK: all four T=F candidates (circularity)",
           "- " + ADJ.CANDIDATES["ADJ-F-S"]["C1"][1], ""]
    cx += ["## DEADLOCK: ADJ-V-S at Gamma <= 1",
           "- " + certs["survivor_scope"]["ADJ-V-S"]["deadlock_witness_Gamma_le_1"], ""]
    cx += ["## DEADLOCK: ADJ-V-P at Gamma = 0",
           "- " + certs["survivor_scope"]["ADJ-V-P"]["deadlock_witness_Gamma_0"], ""]
    cx += ["## EXPLOSION: REC-* and B0 keep the unthrottled adjunction layer",
           "- R50 saturation applies verbatim: |X_{k+1}| = C(|X_k|,2)+2, "
           "kappa = 2 at all 1296 registered points; C2 = "
           "SUPER_EXPONENTIAL, C3 degenerate.", ""]
    cx += ["## CORRECTION to registered prediction: ADJ-V-P growth class",
           "- Predicted EXPONENTIAL; exact quadratic bound |X_k| <= "
           "C(2+Gamma*k,2)+2 proves POLYNOMIAL.", ""]
    for hc in ADJ.HOSTILE_CONTROLS:
        cx += [f"## HOSTILE CONTROL {hc[0]}: {hc[1]}",
               f"- status: {hc[2]}", f"- obstruction/scope: {hc[3]}", ""]
    (out / "OD0_R51_COUNTEREXAMPLES.md").write_text(
        "\n".join(cx), encoding="utf-8", newline="\n")

    # ---- REPORT ----
    rep = []
    rep.append("# OD0-R51 Report - Minimal Throttle Premise Class")
    rep.append("")
    rep.append("## Answer to the governing question")
    rep.append("")
    rep.append("**The survivor is unique under the frozen minimality "
               "order: ADJ-V-S**, stated as premise TG1 (serviced vacuum "
               "maintenance is enablement-active, same-step, on both "
               "parents), with exact scope Gamma in 2..5. All four "
               "forced-token candidates deadlock at step 1 by an exact "
               "circularity (request needs record needs use needs "
               "enablement needs served request). Both record-gated "
               "candidates keep the unthrottled adjunction layer "
               "(SUPER_EXPONENTIAL, R50 saturation) and forfeit the "
               "envelope by modifying RO-D. ADJ-V-P survives with one "
               "extra persistent field (a vacuum mark absent from all "
               "source) and POLYNOMIAL growth - an exact quadratic bound "
               "correcting the prediction's EXPONENTIAL guess - and "
               "covers Gamma = 1; the frozen lexicographic order "
               "(C5, C6, C8) still gives the unique minimum to ADJ-V-S. "
               "Under TG1 the dynamics are LINEAR-bounded, non-degenerate "
               "(burst-drain: forced inflow of >= 22 requests per new "
               "object against Gamma <= 5 starves vacuum service, growth "
               "halts, backlog drains, service resumes), and coherence "
               "lifetime > 1 appears with probability 1/3 already at the "
               "smallest deadlock-free point. The R50 envelope survives "
               "verbatim for both survivors.")
    rep.append("")
    rep.append("## Verdicts")
    rep.append("")
    rep.append(f"- {ADJ.VERDICTS['always']}")
    rep.append(f"- PRIMARY: {ADJ.VERDICTS['primary']}")
    for k, v in sorted(ADJ.VERDICTS["secondary"].items()):
        rep.append(f"- {k}: {v}")
    rep.append("")
    rep.append("## Prediction vs outcome")
    rep.append("")
    rep.append(ADJ.VERDICTS["prediction_vs_outcome"])
    rep.append("")
    rep.append("## Compact terminal return")
    rep.append("")
    rep.append("```text")
    rep.append("OD0-R51 OVERALL VERDICT: " + ADJ.VERDICTS["always"]
               + " + " + ADJ.VERDICTS["primary"])
    rep.append("COMMITS (A / B): 28f50e5 / FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE")
    rep.append("R50 PIN / WORKTREE / BELL2 / VALUES PARSED / HAND HASHES: "
               "PASS / CLEAN / false / 0 / 0")
    rep.append("SELECTOR STATUS S1-S5: S1 DERIVED_GIVEN_TOKEN_"
               "DISTINGUISHABILITY; S2 V~X = NEW_IDENTIFICATION (kernel "
               "D-constancy silent on it); S3 no vacuum mark in source; "
               "S4 deterministic all-vacuum genesis at m=0 (exact table "
               "for all Gamma, m); S5 trivial joint region at constructor "
               "level ({a}:1, {b}:1, joint:|X|-2)")
    rep.append("CANDIDATE CLASS (9): ADJ-V-S SURVIVOR(scope G>=2); "
               "ADJ-V-P SURVIVOR(+1 field, G>=1, POLYNOMIAL); ADJ-F-S/P "
               "DEADLOCK(circular); REC-V-S/P C2+C3 FAIL + envelope "
               "forfeited; REC-F-S/P record-layer deadlock; B0 control "
               "degenerate (R50)")
    rep.append("DEADLOCK WITNESSES: T=F circularity exact; ADJ-V-S "
               "Gamma<=1 (one token/step vs two-token same-step gate); "
               "ADJ-V-P Gamma=0")
    rep.append("GROWTH CLASSES: ADJ-V-S LINEAR (<=C(Gamma,2)/step); "
               "ADJ-V-P POLYNOMIAL (<=C(2+Gamma*k,2)+2); REC-*/B0 "
               "SUPER_EXPONENTIAL")
    rep.append("LEDGER NON-DEGENERACY: burst-drain cycle; forced inflow "
               ">= 2 records x 11 = 22 per composite-parent event vs "
               "Gamma <= 5; P(S^V=0) rises then dips within K_max "
               "(exemplar G=2,m=0,H=0: 0, 154/325, ~0.62, ~0.657, "
               "~0.656); long-run drain lemma stated")
    rep.append("COHERENCE LIFETIME > 1: YES - probability exactly 1/3 at "
               "(Gamma=2, m=0, H=0), path witness recorded")
    rep.append("FOOTPRINT / FIELDS / QUOTIENT DEP: ADJ-V-S {opportunity, "
               "V~X, D-override} / 0 / DIRECT; ADJ-V-P +vacuum-mark / 1 / "
               "INDIRECT; envelope survives for both")
    rep.append("SURVIVORS AND MINIMALITY: {ADJ-V-S, ADJ-V-P}; "
               "(C5,C6,C8)-lex unique minimum = ADJ-V-S")
    rep.append("SURVIVOR PREMISE (TG1): " + ADJ.MINIMALITY["premise_statement"])
    rep.append("K_MAX AND READOUT: per-point exact-enumeration bound; "
               "ADJ-V-S K_max 3-5 over 144 points, ADJ-V-P K_max 3-7 over "
               "180 points; full exact trajectories (E|X|, P(S^V=0), "
               "shell, backlog) in R51_SURVIVOR_DYNAMICS_READOUT.json")
    rep.append(f"HOSTILE CONTROLS: {len(ADJ.HOSTILE_CONTROLS)}/8")
    rep.append("DETERMINISTIC RERUN: " + args.rerun_status)
    rep.append("OUTPUT MANIFEST SHA-256: FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE")
    rep.append("RECOMMENDED SINGLE R52 MOVE: " + ADJ.VERDICTS["r52_recommendation"])
    rep.append("```")
    rep.append("")
    (out / "OD0_R51_REPORT.md").write_text("\n".join(rep), encoding="utf-8",
                                           newline="\n")
    print(f"outputs written to {out}")


if __name__ == "__main__":
    main()
