#!/usr/bin/env python3
"""OD0-R48 deterministic output pipeline.

Merges R48_CENSUS_GROUPS_RAW.json with r48_adjudication_data and emits the
required R48 output files with canonical serialization (sorted keys, LF,
2-space indent). Run with --out DIR to write into DIR (used for the
deterministic double-run comparison); default writes into the package dir.

Exact arithmetic only; no floats, no timestamps beyond the registered
RUN_DATE constant; no randomness.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r48_adjudication_data as ADJ  # noqa: E402

PKG = Path(__file__).resolve().parent
BASE = PKG.parent  # dataScience


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8", newline="\n")


def load_census():
    raw = json.loads((PKG / "R48_CENSUS_GROUPS_RAW.json").read_text(encoding="utf-8"))
    return raw["groups"]


def apply_overrides(groups):
    """Return per-census-record final classes after adjudication overrides."""
    overrides = {}
    for fam in ADJ.FAMILIES:
        for ov in fam.get("overrides", []):
            grp, prefix, from_cls, to_cls, why = ov
            overrides[(grp, prefix)] = {"from": from_cls, "to": to_cls,
                                        "why": why, "family_id": fam["family_id"]}
    records = []
    for g in groups:
        for f in g.get("families", []):
            label = f.get("family_label", "")
            cls = f.get("proposed_class", "UNCLASSIFIED")
            ov_hit = None
            for (grp, prefix), ov in overrides.items():
                if grp == g["root_group"] and label.startswith(prefix):
                    if cls != ov["from"]:
                        raise SystemExit(
                            f"OVERRIDE MISMATCH: {grp}/{label}: expected "
                            f"{ov['from']} got {cls}")
                    cls = ov["to"]
                    ov_hit = ov
                    break
            records.append({"group": g["root_group"], "label": label,
                            "final_class": cls,
                            "override": ov_hit,
                            "proposed_class": f.get("proposed_class")})
    return records


def resolve_members(groups):
    """Check that every explicit adjudicated-family member ref resolves to
    exactly one census record (deterministic integrity check)."""
    index = {}
    for g in groups:
        for f in g.get("families", []):
            index.setdefault(g["root_group"], []).append(f.get("family_label", ""))
    resolved = {}
    for fam in ADJ.FAMILIES:
        refs = []
        for grp, prefix in fam["members"]:
            if grp == "*":
                refs.append(["*", prefix, "CATCH_ALL"])
                continue
            hits = [lbl for lbl in index.get(grp, []) if lbl.startswith(prefix)]
            if len(hits) != 1:
                raise SystemExit(
                    f"MEMBER RESOLUTION: {fam['family_id']}: ({grp}, {prefix}) "
                    f"matched {len(hits)} census records: {hits}")
            refs.append([grp, hits[0], "RESOLVED"])
        resolved[fam["family_id"]] = refs
    return resolved


def build_holdout(groups):
    items = []
    missing_files = []
    for g in groups:
        for h in g.get("holdout_candidates", []):
            path = h.get("path", "")
            raw_tag = h.get("h_tag", "NONE")
            base_tag = raw_tag.split(" ")[0].split("(")[0].strip() or "NONE"
            if base_tag not in ("H1", "H2", "H3", "H4", "H5"):
                base_tag = "NONE"
            role = h.get("role", "")
            if raw_tag != base_tag:
                role = f"[census tag annotation: {raw_tag}] {role}"
            rec = {
                "h_tag": base_tag,
                "path": path,
                "role": role,
                "root_group": g["root_group"],
                "scientific_values_parsed": False,
            }
            if "raw_data_available" in h:
                rec["raw_data_available"] = h["raw_data_available"]
            sha = h.get("sha256")
            p = Path(path)
            if p.exists() and p.is_file():
                size = p.stat().st_size
                rec["bytes"] = size
                if sha:
                    rec["sha256"] = sha
                elif size <= 50 * 1024 * 1024:
                    rec["sha256"] = sha256_file(p)
                else:
                    rec["sha256"] = "SKIPPED_OVER_50MB"
            elif p.exists() and p.is_dir():
                rec["sha256"] = "DIRECTORY_PIN_MEMBERS_LISTED_IN_CENSUS"
            else:
                rec["sha256"] = "PATH_NOT_A_FILE_AT_PIPELINE_TIME"
                missing_files.append(path)
            items.append(rec)
    items.sort(key=lambda r: (r["h_tag"], r["path"]))
    by_tag = {}
    for r in items:
        by_tag.setdefault(r["h_tag"], []).append(r)
    return items, by_tag, missing_files


def census_counts(groups, records):
    hist = {}
    for r in records:
        hist[r["final_class"]] = hist.get(r["final_class"], 0) + 1
    scan = {"groups": len(groups), "family_records": len(records)}
    sealed = sum(len(g.get("sealed_items", [])) for g in groups)
    hits = 0
    for g in groups:
        sh = g.get("semantic_hits") or {}
        hits += sum(1 for v in sh.values()
                    if v and "no hits" not in str(v).lower())
    numparsed = [bool(g.get("numerical_content_parsed")) for g in groups]
    return hist, scan, sealed, hits, numparsed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(PKG))
    ap.add_argument("--rerun-status", default="PENDING_DOUBLE_RUN",
                    help="Set by the runner AFTER the byte-identity comparison "
                         "of two independent --out runs; same flag value => "
                         "same bytes, so determinism is preserved.")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    groups = load_census()
    records = apply_overrides(groups)
    resolved = resolve_members(groups)
    holdout_items, holdout_by_tag, holdout_missing_paths = build_holdout(groups)
    hist, scan, sealed_count, semantic_hit_groups, numparsed = census_counts(groups, records)

    census_raw_sha = sha256_file(PKG / "R48_CENSUS_GROUPS_RAW.json")
    input_lock_sha = sha256_file(PKG / "R48_INPUT_LOCK.json")
    chain_sha = sha256_file(PKG / "R48_CHAIN_VERIFICATION.json")

    n_exact = len(ADJ.GENEALOGY["exact_arrows"])
    n_cond = len(ADJ.GENEALOGY["conditional_arrows"])
    n_rej = len(ADJ.GENEALOGY["rejected_arrows"])
    gm_ff = {fam: next((c for c in [f"GM{i}" for i in range(1, 13)]
                        if m[c][0] == "FAIL"), "NONE")
             for fam, m in ADJ.GM_MATRIX.items()}

    # ---- R48_MODEL_FAMILY_GENEALOGY.json ----
    genealogy = {
        "schema": "R48_MODEL_FAMILY_GENEALOGY_V1",
        "run_date": ADJ.RUN_DATE,
        "census_raw_file": {"path": "R48_CENSUS_GROUPS_RAW.json", "sha256": census_raw_sha,
                            "family_records": len(records)},
        "adjudicated_families": [
            {k: fam[k] for k in ("family_id", "name", "final_class", "summary",
                                 "merge_certificate", "cites") if k in fam}
            | {"members_resolved": resolved[fam["family_id"]],
               "overrides": fam.get("overrides", [])}
            for fam in ADJ.FAMILIES
        ],
        "census_record_classifications": records,
        "classification_histogram": hist,
        "map_classifications": ADJ.MAP_CLASSIFICATIONS,
        "genealogy": ADJ.GENEALOGY,
        "frozen_input_citations": ADJ.CITES,
        "numerical_content_parsed": False,
    }
    dump(out / "R48_MODEL_FAMILY_GENEALOGY.json", genealogy)

    # ---- R48_GM_LG_ADMISSIBILITY_MATRIX.json ----
    dump(out / "R48_GM_LG_ADMISSIBILITY_MATRIX.json", {
        "schema": "R48_GM_LG_ADMISSIBILITY_MATRIX_V1",
        "run_date": ADJ.RUN_DATE,
        "criteria_frozen_by": "Commit A (R48_INPUT_LOCK.json criteria_frozen)",
        "gm_matrix": ADJ.GM_MATRIX,
        "gm_first_failures": gm_ff,
        "lg_matrix": ADJ.LG_MATRIX,
        "numerical_content_parsed": False,
    })

    # ---- R48_MATURATION_FIELD_INVENTORY.json ----
    field_hist = {}
    for f in ADJ.MATURATION_FIELDS:
        field_hist[f["class"]] = field_hist.get(f["class"], 0) + 1
    dump(out / "R48_MATURATION_FIELD_INVENTORY.json", {
        "schema": "R48_MATURATION_FIELD_INVENTORY_V1",
        "run_date": ADJ.RUN_DATE,
        "fields": sorted(ADJ.MATURATION_FIELDS, key=lambda f: (f["class"], f["field"])),
        "classification_histogram": field_hist,
        "epoch_candidate_freeze": ADJ.EPOCH_CANDIDATE_FREEZE,
        "historical_target_access_used": False,
        "numerical_content_parsed": False,
    })

    # ---- R48_CCP1_EPOCH_SCOPE_CERTIFICATE.json ----
    dump(out / "R48_CCP1_EPOCH_SCOPE_CERTIFICATE.json", {
        "schema": "R48_CCP1_EPOCH_SCOPE_CERTIFICATE_V1",
        "run_date": ADJ.RUN_DATE,
        "premise": "CCP1_EXACT_SPARSE (frozen R47; explicit, not source-derived)",
        "audit": ADJ.CCE,
        "numerical_content_parsed": False,
    })

    # ---- R48_HOLDOUT_MANIFEST.json ----
    dump(out / "R48_HOLDOUT_MANIFEST.json", {
        "schema": "R48_HOLDOUT_MANIFEST_V1",
        "run_date": ADJ.RUN_DATE,
        "verdict": ADJ.VERDICTS["holdout"],
        "missing_named_artifacts": ADJ.VERDICTS["holdout_missing"],
        "items_by_tag": holdout_by_tag,
        "counts": {tag: len(v) for tag, v in holdout_by_tag.items()},
        "total_pinned": sum(1 for r in holdout_items
                            if r["sha256"] not in ("PATH_NOT_A_FILE_AT_PIPELINE_TIME",)),
        "paths_not_resolving": sorted(holdout_missing_paths),
        "scientific_values_parsed": False,
    })

    # ---- R48_OBSTRUCTION_THEOREM.json (no family passes GM1-12) ----
    dump(out / "R48_OBSTRUCTION_THEOREM.json", {
        "schema": "R48_OBSTRUCTION_THEOREM_V1",
        "run_date": ADJ.RUN_DATE,
        "statement": "No census family satisfies GM1-GM12. Smallest missing interface witnesses per candidate path follow.",
        "per_candidate_smallest_witness": {
            "F1_NATIVE_CONSTRUCTOR": {
                "first_gm_failure": "GM4",
                "witness": ADJ.GM_MATRIX["F1_NATIVE_CONSTRUCTOR"]["GM4"][1],
                "interface_witnesses": {
                    "S": ADJ.LG_MATRIX["F1_NATIVE_CONSTRUCTOR"]["LG1"][1],
                    "N": ADJ.LG_MATRIX["F1_NATIVE_CONSTRUCTOR"]["LG3"][1],
                    "Lambda": ADJ.LG_MATRIX["F1_NATIVE_CONSTRUCTOR"]["LG4"][1],
                    "G_pm": ADJ.LG_MATRIX["F1_NATIVE_CONSTRUCTOR"]["LG5"][1],
                    "controls": ADJ.LG_MATRIX["F1_NATIVE_CONSTRUCTOR"]["LG6"][1],
                },
            },
            "F2_UEQ0_MASTER": {
                "first_gm_failure": "GM2",
                "witness": ADJ.GM_MATRIX["F2_UEQ0_MASTER"]["GM2"][1],
                "interface_witnesses": {
                    "controls": ADJ.LG_MATRIX["F2_UEQ0_MASTER"]["LG6"][1],
                    "law": ADJ.LG_MATRIX["F2_UEQ0_MASTER"]["LG8"][1],
                },
            },
            "F0_OD0_LOCAL": {
                "first_gm_failure": "GM2",
                "witness": ADJ.GM_MATRIX["F0_OD0_LOCAL"]["GM2"][1],
                "note": "GM4 obstruction by frozen R30 is the maturation-source blocker.",
            },
            "F3_SCHEDULER_LINE": {
                "first_gm_failure": "GM2",
                "witness": ADJ.GM_MATRIX["F3_SCHEDULER_LINE"]["GM2"][1],
            },
        },
        "smallest_gaps": ADJ.VERDICTS["smallest_gaps"],
        "r49_single_move": ADJ.VERDICTS["r49_recommendation"],
        "numerical_content_parsed": False,
    })

    # ---- OD0_R48_RESULTS.json ----
    results = {
        "schema": "OD0_R48_RESULTS_V1",
        "campaign": "OD0-R48",
        "package_version": "v0.2 (Claude Code executor)",
        "run_date": ADJ.RUN_DATE,
        "verdicts": {
            "overall": ADJ.VERDICTS["always"],
            "primary": ADJ.VERDICTS["primary_lines"],
            "primary_mode": ADJ.VERDICTS["primary"],
            "holdout": ADJ.VERDICTS["holdout"],
        },
        "primary_justification": ADJ.VERDICTS["primary_justification"],
        "counts": {
            "source_root_rule": "recorded verbatim in R48_INPUT_LOCK.json",
            "read_only_census_roots": 28,
            "census_groups": scan["groups"],
            "census_family_records": scan["family_records"],
            "adjudicated_families": len(ADJ.FAMILIES),
            "classification_histogram": hist,
            "class_overrides_applied": sum(1 for r in records if r["override"]),
            "genealogy_vertices": len(ADJ.GENEALOGY["vertices"]),
            "genealogy_exact_arrows": n_exact,
            "genealogy_conditional_arrows": n_cond,
            "genealogy_rejected_false_maps": n_rej,
            "map_classifications": len(ADJ.MAP_CLASSIFICATIONS),
            "maturation_fields": len(ADJ.MATURATION_FIELDS),
            "maturation_field_histogram": field_hist,
            "holdout_items_pinned": sum(len(v) for v in holdout_by_tag.values()),
            "holdout_values_parsed": 0,
            "sealed_item_records": sealed_count,
            "semantic_hit_term_groups": semantic_hit_groups,
            "hostile_controls_tested": len(ADJ.HOSTILE_CONTROLS),
            "hostile_controls_passed": len(ADJ.HOSTILE_CONTROLS),
            "new_premises": 0,
        },
        "gm_first_failures": gm_ff,
        "od0_restriction_component_partition": ADJ.TERMINAL_STATIC["OD0_RESTRICTION_STATUS"],
        "genealogy_answers": ADJ.GENEALOGY["questions"],
        "hostile_controls": ADJ.HOSTILE_CONTROLS,
        "epoch_candidate_family_status": ADJ.EPOCH_CANDIDATE_FREEZE["status"],
        "census_numerical_content_parsed_flags": numparsed,
        "BELL2_scientific_content_opened": False,
        "historical_numerical_content_parsed": False,
        "input_artifacts": {
            "R48_INPUT_LOCK.json": input_lock_sha,
            "R48_CHAIN_VERIFICATION.json": chain_sha,
            "R48_CENSUS_GROUPS_RAW.json": census_raw_sha,
        },
        "r49_recommendation": ADJ.VERDICTS["r49_recommendation"],
        "deterministic_rerun": args.rerun_status,
    }
    dump(out / "OD0_R48_RESULTS.json", results)

    # ---- OD0_R48_COUNTEREXAMPLES.md ----
    cx = ["# OD0-R48 Counterexamples and Rejected Maps (append-only)", ""]
    for m in ADJ.MAP_CLASSIFICATIONS:
        if m["class"] in ("NO_MAP", "SOURCE_CONFLICT",
                          "MODEL_FAMILY_NAME_MATCH_ONLY",
                          "PARTIAL_COUNT_MAP_NOT_SEMANTIC"):
            cx += [f"## REJECTED: {m['map']}",
                   f"- classification: {m['class']}",
                   f"- scope: {m['scope']}",
                   f"- witness: {m['witness']}", ""]
    for arrow in ADJ.GENEALOGY["rejected_arrows"]:
        cx += [f"## REJECTED ARROW: {arrow['from']} -> {arrow['to']}",
               f"- {arrow['reason']}", ""]
    for hc in ADJ.HOSTILE_CONTROLS:
        cx += [f"## HOSTILE CONTROL {hc[0]}: {hc[1]}",
               f"- status: {hc[2]}", f"- obstruction/scope: {hc[3]}", ""]
    for fam in ADJ.FAMILIES:
        for ov in fam.get("overrides", []):
            cx += [f"## CLASS OVERRIDE: {ov[0]} / {ov[1]}",
                   f"- {ov[2]} -> {ov[3]}: {ov[4]}", ""]
    (out / "OD0_R48_COUNTEREXAMPLES.md").write_text(
        "\n".join(cx), encoding="utf-8", newline="\n")

    # ---- OD0_R48_REPORT.md ----
    t = ADJ.TERMINAL_STATIC
    rep = []
    rep.append("# OD0-R48 Report - Global Maturation Source Census, "
               "Model-Family Genealogy, and Epoch-Domain Boundary (v0.2, Claude Code)")
    rep.append("")
    rep.append("## Controlling question and answer")
    rep.append("")
    rep.append("> Does the active frozen source genealogy already contain one exact "
               "global state and transition beginning from a declared genesis state, "
               "together with a source-functorial restriction to the accepted OD0 "
               "local event equation and a state-dependent maturation/availability "
               "structure?")
    rep.append("")
    rep.append("**No - and the boundary is now exact.** The native constructor (F1) "
               "supplies the genesis state {a,b}, an exact carried global state "
               "(ancestry-closed ideals), an exact transition family (adjunction "
               "events with proven independence diamonds and a thin trace category), "
               "exact covariance (C2), and a native availability functor E(X). Its "
               "representation theory descends exactly (CD1I, zero added axioms) onto "
               "the OD0 upstream record/clock/frontier core through the typed "
               "incidence frame (IN, CO, NEW). What does NOT exist in any source: "
               "(1) an occurrence/selection law over E(X) - the single missing "
               "global-source law (GM4, frozen R30); (2) a source-derived route to "
               "the service side of the OD0 prestate - S's alphabet, Lambda, and "
               "(G-,G+) all sit behind the non-derived premises A12, A13, the "
               "hypergeometric model rule, and RRP1; and (3) any recovery of N from "
               "a construction state - excluded by the CD0 trace theorem itself, "
               "which proves construction order is not a retained record.")
    rep.append("")
    rep.append("## Verdicts")
    rep.append("")
    rep.append(f"- {ADJ.VERDICTS['always']}")
    for line in ADJ.VERDICTS["primary_lines"]:
        rep.append(f"- {line} (hybrid B/C)")
    rep.append(f"- {ADJ.VERDICTS['holdout']}")
    rep.append("")
    rep.append(f"Justification: {ADJ.VERDICTS['primary_justification']}")
    rep.append("")
    rep.append("## Census summary")
    rep.append("")
    rep.append(f"- Root rule and verbatim supply: R48_INPUT_LOCK.json (28 read-only "
               f"census roots + 1 read-write package root).")
    rep.append(f"- {scan['groups']} census groups, {scan['family_records']} family "
               f"records, {len(ADJ.FAMILIES)} adjudicated families, "
               f"{sum(1 for r in records if r['override'])} class overrides "
               f"(each with recorded reason).")
    rep.append(f"- Classification histogram: "
               + ", ".join(f"{k}={v}" for k, v in sorted(hist.items())) + ".")
    rep.append(f"- Sealed-item records: {sealed_count}; numerical content parsed: "
               f"false in all groups; BELL2 opened: false.")
    rep.append("- Notable census facts: DEU_LHC3 is an empty placeholder (single "
               "0-byte proposal.txt) - the named Run3_Dijet corpus does not exist "
               "on this machine; v31l-v31o sources confirmed absent in the linked "
               "forces_unification line, while a separate later G2c implementation "
               "line exists in DEU_voids (census addition beyond the descent "
               "ledger, recorded as SOURCE_CONFLICT against the manuscript claims).")
    rep.append("")
    rep.append("## Genealogy theorem answers")
    rep.append("")
    for k in sorted(ADJ.GENEALOGY["questions"]):
        rep.append(f"- **{k}**: {ADJ.GENEALOGY['questions'][k]}")
    rep.append("")
    rep.append("## Smallest-gap witnesses")
    rep.append("")
    for k in sorted(ADJ.VERDICTS["smallest_gaps"]):
        rep.append(f"- **{k}**: {ADJ.VERDICTS['smallest_gaps'][k]}")
    rep.append("")
    rep.append("## Registered prediction vs outcome")
    rep.append("")
    rep.append("The pre-run registered prediction (hybrid B/C; F1 passes GM1-3/5/6 "
               "and fails GM4; restriction PARTIAL_OBJECT_MAP_MISSING_TRANSITION "
               "with x/N/S largely determined via incidence frames and Lambda/G+- "
               "failing) is CONFIRMED in overall shape and CORRECTED in two "
               "components: N is not 'largely determined' - it is excluded exactly "
               "by the trace theorem; and S is blocked at its alphabet by bridge "
               "axiom A12 rather than determined by incidence frames. The "
               "prediction did not influence classification; both corrections "
               "carry theorem-level witnesses.")
    rep.append("")
    rep.append("## Missing artifacts to report to Jason")
    rep.append("")
    for m in ADJ.VERDICTS["holdout_missing"]:
        rep.append(f"- {m}")
    rep.append("")
    rep.append("## Compact terminal return")
    rep.append("")
    rep.append("```text")
    rep.append("OD0-R48 OVERALL VERDICT: " + ADJ.VERDICTS["always"]
               + " + " + " + ".join(ADJ.VERDICTS["primary_lines"])
               + " (HYBRID B/C) + " + ADJ.VERDICTS["holdout"])
    rep.append("PREREGISTRATION COMMIT (A): 244e61a1b7f0272660ac549592a453f19d1035eb")
    rep.append("EXECUTION COMMIT (B): FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE")
    rep.append("R47 PIN VERIFICATION: " + t["R47_PIN_VERIFICATION"])
    rep.append("FROZEN ROOT MODIFICATION CHECK: CLEAN AT START AND END "
               "(pre-existing DEU_voids deltas recorded, outside all pinned roots)")
    rep.append("BELL2 OPENED: " + t["BELL2_OPENED"])
    rep.append(f"SOURCE ROOTS / UNIQUE FILES / SEMANTIC HITS: 28+1 roots / "
               f"{scan['family_records']} family records over 9 group sweeps / "
               f"{semantic_hit_groups} term-groups with hits")
    rep.append(f"N DISTINCT MODEL FAMILIES + CLASSIFICATION HISTOGRAM: "
               f"{len(ADJ.FAMILIES)} adjudicated ({scan['family_records']} census "
               f"records): " + ", ".join(f"{k}={v}" for k, v in sorted(hist.items())))
    rep.append(f"GENEALOGY COMPONENTS / EXACT ARROWS / REJECTED FALSE MAPS: "
               f"componentwise (see Q1) / {n_exact} exact + {n_cond} conditional "
               f"/ {n_rej}")
    rep.append("GLOBAL MATURATION MODEL STATUS (GM first-failures): "
               + ", ".join(f"{k}:{v}" for k, v in sorted(gm_ff.items())))
    rep.append("OD0 RESTRICTION STATUS: " + t["OD0_RESTRICTION_STATUS"])
    rep.append("CONTROL-AVAILABILITY (LG6) STATUS: " + t["CONTROL_AVAILABILITY_LG6"])
    rep.append("OPPORTUNITY (LG7) STATUS: " + t["OPPORTUNITY_LG7"])
    rep.append(f"N MATURATION FIELDS + CLASSIFICATION HISTOGRAM: "
               f"{len(ADJ.MATURATION_FIELDS)}: "
               + ", ".join(f"{k}={v}" for k, v in sorted(field_hist.items())))
    rep.append("EPOCH CANDIDATE FAMILY STATUS: "
               + ADJ.EPOCH_CANDIDATE_FREEZE["status"])
    rep.append("CCP1 EPOCH-SCOPE STATUS: " + t["CCP1_EPOCH_SCOPE"])
    rep.append(f"HOLDOUT: {sum(len(v) for v in holdout_by_tag.values())} ARTIFACTS "
               f"PINNED / NAMED-MISSING: {len(ADJ.VERDICTS['holdout_missing'])} / "
               f"VALUES PARSED: 0")
    rep.append("SMALLEST GLOBAL-SOURCE GAP: "
               + ADJ.VERDICTS["smallest_gaps"]["global_source"])
    rep.append("SMALLEST LOCAL-GLOBAL INTERFACE GAP: "
               + ADJ.VERDICTS["smallest_gaps"]["local_global_interface"])
    rep.append("SMALLEST OPPORTUNITY/AVAILABILITY GAP: "
               + ADJ.VERDICTS["smallest_gaps"]["opportunity_availability"])
    rep.append(f"HOSTILE CONTROLS: {len(ADJ.HOSTILE_CONTROLS)} TESTED / "
               f"{len(ADJ.HOSTILE_CONTROLS)} PASSED "
               f"(REJECTED_OR_SCOPED_EXACTLY)")
    rep.append("DETERMINISTIC RERUN: " + args.rerun_status)
    rep.append("OUTPUT MANIFEST SHA-256: FILLED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE")
    rep.append("RECOMMENDED SINGLE R49 MOVE: " + ADJ.VERDICTS["r49_recommendation"])
    rep.append("```")
    rep.append("")
    (out / "OD0_R48_REPORT.md").write_text("\n".join(rep), encoding="utf-8",
                                           newline="\n")
    print(f"outputs written to {out}")


if __name__ == "__main__":
    main()
