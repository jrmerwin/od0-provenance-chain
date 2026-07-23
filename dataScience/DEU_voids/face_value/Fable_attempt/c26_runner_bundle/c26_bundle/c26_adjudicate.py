#!/usr/bin/env python3
# C26 adjudication: applies prereg gates G1-G4 per candidate class over the
# discovery/validation split (seed-list position: odd->discovery, even->validation,
# frozen in prereg section 5) and emits exactly one registered classification.
# Usage: python3 c26_adjudicate.py <config.json> <selection.json> <seeds.json> <out_json>
import json, sys
from pathlib import Path

CLASSES = ["C26_PREFLIGHT_A_ELIGIBLE__B_INELIGIBLE",
           "C26_PREFLIGHT_B_ELIGIBLE__A_INELIGIBLE",
           "C26_PREFLIGHT_BOTH_ELIGIBLE",
           "C26_PREFLIGHT_BOTH_ELIGIBLE__NOT_SEPARATED",
           "C26_PREFLIGHT_BOTH_INELIGIBLE__SCAR_FAMILY_CLOSED"]

def gate_frac(rows, key):
    """(hits, defined_count) among valid seeds where the candidate is defined."""
    d = [r for r in rows if r["valid"] and r[key[0]]["defined"]]
    return sum(1 for r in d if r[key[0]].get(key[1])), len(d)

def eligible(rows_disc, rows_val, cand, g):
    res = {}
    for gname, obs, thr in (("G1", "P", g["g1_min"]), ("G2", "M", g["g2_min"]),
                            ("G4", None, g["g4_min_defined"])):
        for tag, rows in (("disc", rows_disc), ("val", rows_val)):
            if gname == "G4":
                valid = [r for r in rows if r["valid"]]
                hits = sum(1 for r in valid if r[cand]["defined"]); den = len(valid)
            else:
                hits, den = gate_frac(rows, (cand, obs))
            res[f"{gname}_{tag}"] = [hits, den, hits >= thr]
    for tag, rows in (("disc", rows_disc), ("val", rows_val)):
        d = [r for r in rows if r["valid"] and r[cand]["defined"]]
        hits = sum(1 for r in d if r[cand].get("S") and r[cand].get("C"))
        res[f"G3_{tag}"] = [hits, len(d), hits >= g["g3_min"]]
    ok = all(v[2] for v in res.values())
    return ok, res

def main(cfgp, selp, seedsp, outp):
    g = json.loads(Path(cfgp).read_text(encoding="utf-8"))["gates"]
    rows = json.loads(Path(selp).read_text(encoding="utf-8"))
    order = json.loads(Path(seedsp).read_text(encoding="utf-8"))["cohort"]
    pos = {s: i for i, s in enumerate(order)}
    rows = [r for r in rows if r["seed"] in pos]
    missing = [s for s in order if s not in {r["seed"] for r in rows}]
    if missing:
        sys.exit(f"ADJUDICATE ABORT: cohort incomplete -- missing seeds {missing}. "
                 "Rerun run+select stages; adjudication requires the full cohort.")
    disc = [r for r in rows if pos[r["seed"]] % 2 == 0]
    val  = [r for r in rows if pos[r["seed"]] % 2 == 1]
    okA, resA = eligible(disc, val, "A", g)
    okB, resB = eligible(disc, val, "B", g)
    if okA and okB:
        sep_seeds = [r for r in rows if r["valid"] and not r.get("coincide")
                     and r["A"]["defined"] and r["B"]["defined"]]
        cls = CLASSES[2] if sep_seeds else CLASSES[3]
    elif okA: cls = CLASSES[0]
    elif okB: cls = CLASSES[1]
    else:     cls = CLASSES[4]
    rec = dict(classification=cls, gates=dict(A=resA, B=resB),
               n_seeds=len(rows), n_disc=len(disc), n_val=len(val),
               coincide_seeds=[r["seed"] for r in rows if r.get("coincide")],
               stopping_rule_fired=(cls == CLASSES[4]))
    Path(outp).write_text(json.dumps(rec, indent=1), encoding="utf-8", newline="\n")
    print(json.dumps(rec, indent=1))
    if rec["stopping_rule_fired"]:
        print("\n*** STOPPING RULE: relief-scar family PERMANENTLY CLOSED "
              "(prereg section 9). No effect round may launch. ***")

if __name__ == "__main__":
    main(*sys.argv[1:5])
