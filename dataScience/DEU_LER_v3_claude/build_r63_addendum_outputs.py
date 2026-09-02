#!/usr/bin/env python3
"""OD0-R63 ADDENDUM output builder. Deterministic; byte-identical."""
import hashlib
import json
from pathlib import Path

import r63_addendum_adjudication as A

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8", newline="\n")


certs = json.loads((PKG / "R63_ADDENDUM_CERTIFICATES.json").read_text(
    encoding="utf-8"))

layer = {
    "schema": "R63_OPERATIONAL_LAYER_V1",
    "D7_readability": A.D7,
    "D8_backaction_theorem": A.D8,
    "D9_cost_distance": A.D9,
    "certificates": certs,
    "adversarial_verification": A.PANEL,
    "addendum_corrections": [
        "CX-A-1: the registered D9 prediction 'triangle inequality "
        "fails (witness with a shared parent)' is REFUTED - the "
        "triangle inequality is a THEOREM at any common snapshot "
        "(slack >= 22 ch_y, tight at 22), and d_cost with zero "
        "diagonal is a full METRIC on the absent-pair domain; the "
        "registered pseudometric-after-normalization is superseded. "
        "The metric property is snapshot-relative: mixed-snapshot "
        "comparisons violate it (panel witnesses).",
        "CX-A-2: new exact law - the operational horizon is "
        "E|U|/n = 1/3 - 2/(3n) + o(1/n) (U = leaves, exactly); "
        "recorded here because the base counterexample file's hash "
        "is frozen in the base manifest."],
    "primary_verdict_update": "NONE_UNDER_UNIFORM_PAIRING stands "
        "over all seven structures including d_cost (DEGENERATE at "
        "the 1/sqrt(log n) rate).",
}
dump(PKG / "R63_OPERATIONAL_LAYER.json", layer)

results = {
    "schema": "OD0_R63_ADDENDUM_RESULTS_V1",
    "run_date": A.RUN_DATE,
    "verdict": A.VERDICTS["addendum_verdict"],
    "ADDENDUM_FROZEN_AFTER_A": True,
    "addendum_lock_sha256": sha(PKG / "R63_ADDENDUM_LOCK.json"),
    "D7": "classified per structure; horizon law 1/3 (leaf theorem)",
    "D8": "PROVEN (collapse/invariance certified exactly)",
    "D9": "METRIC (triangle THEOREM, snapshot-relative); "
          "Theta(n log n); DEGENERATE at 1/sqrt(log n) rate; "
          "READABLE_FROM_S on X_rec",
    "hostile_control_9": {"id": A.HC9[0], "control": A.HC9[1],
                          "status": A.HC9[2], "basis": A.HC9[3]},
    "panel": A.PANEL,
    "prediction_vs_outcome": A.VERDICTS["prediction_vs_outcome"],
    "seals": {"BELL2_opened": False, "H1_H4": "spent",
              "H5": {"parsed": False}},
}
dump(PKG / "OD0_R63_ADDENDUM_RESULTS.json", results)

report = f"""# OD0-R63 Addendum Report: Operational Layer

Run date: {A.RUN_DATE}. Verdict: **{A.VERDICTS["addendum_verdict"]}**.
ADDENDUM_FROZEN_AFTER_A = true (D7-D9 frozen in a hashed appendix at
Commit A2 before any D7-D9 computation; base R63 outputs untouched).

## D7 - readability
Shell identity: {A.D7["shell_identity"]}

Horizon law: {A.D7["horizon_law"]}

Per-structure: {json.dumps(A.D7["classification"], indent=1)[1:-1]}

## D8 - back-action theorem: {A.D8["verdict"]}
{A.D8["statement"]}

## D9 - cost-distance
Triangle: {A.D9["triangle"]}

Metric status: {A.D9["pseudometric"]}

Scaling: {A.D9["scaling"]}

D3 status: {A.D9["D3_status"]}

## Prediction vs outcome
{A.VERDICTS["prediction_vs_outcome"]}

## Hostile controls
Base HC1-HC8 plus HC9: all REJECTED.
"""
(PKG / "OD0_R63_ADDENDUM_REPORT.md").write_text(report,
                                                encoding="utf-8",
                                                newline="\n")

base_manifest_sha = sha(PKG / "R63_OUTPUT_MANIFEST.json")
files = ["R63_ADDENDUM_LOCK.json", "R63_OPERATIONAL_LAYER.json",
         "R63_ADDENDUM_CERTIFICATES.json",
         "OD0_R63_ADDENDUM_RESULTS.json",
         "OD0_R63_ADDENDUM_REPORT.md", "r63_addendum_exact.py",
         "r63_addendum_adjudication.py",
         "build_r63_addendum_outputs.py",
         "make_r63_addendum_lock.py"]
manifest = {"schema": "R63_ADDENDUM_MANIFEST_V1",
            "note": "manifest excludes itself; supplements the frozen "
                    "base manifest (pinned below) per the addendum's "
                    "append instruction",
            "base_manifest_sha256_pinned": base_manifest_sha,
            "files": {f: sha(PKG / f) for f in files}}
dump(PKG / "R63_ADDENDUM_MANIFEST.json", manifest)
print("operational layer sha256:",
      sha(PKG / "R63_OPERATIONAL_LAYER.json"))
print("addendum manifest sha256:",
      sha(PKG / "R63_ADDENDUM_MANIFEST.json"))
