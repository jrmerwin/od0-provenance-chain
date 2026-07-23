#!/usr/bin/env python3
# B0 analysis and adjudication (spec sections 5, 7, 8).
# Exact arithmetic (Fraction) end to end for densities; floats only inside the
# registered bootstrap. Per seed and epoch t in the observation window:
#   d_B(t) = D_B/A_B   demand density on the boundary (pre-service, exact)
#   s_B(t) = S_B/A_B   service density on the boundary (execution-attributed)
#   v_d(t), v_s(t)     shell-matched vacuum baselines from the control arm,
#                      weighted by the pocket arm's time-mean boundary shell
#                      occupancy (support matching, R26 lesson)
#   dD(t) = d_B - v_d, dS(t) = s_B - v_s
# Gates (thresholds from config, frozen at registration):
#   G0 excess demand; G1 boundary persistence; G2 rate; G3 stationarity
#   (W1/W2 relative change + seed-level bootstrap slope test); G4 stock class.
# Usage: python3 b0_adjudicate.py <config.json> <cache_dir> <out_json>
import gzip, hashlib, json, pickle, sys
from fractions import Fraction
from pathlib import Path

CLASSES = ["B0_BOUNDARY_RATE_CERTIFIED__COMPILER_CANDIDATE_OPEN",
           "B0_BOUNDARY_STOCK_ONLY__RATE_ABSENT",
           "B0_NO_BOUNDARY_EXCESS",
           "B0_POCKET_NOT_PERSISTENT"]
W = lambda k: Fraction(1, 3 ** k)

def region_sum(cnt, region):
    return sum((W(k) * n for (r, s, k), n in cnt.items() if r == region), Fraction(0))

def served_region_sum(cnt, region):
    return sum((W(k) * n for (kd, r, s, k), n in cnt.items() if r == region), Fraction(0))

def shell_sums(cnt):
    out = {}
    for (r, s, k), n in cnt.items():
        if s >= 0: out[s] = out.get(s, Fraction(0)) + W(k) * n
    return out

def served_shell_sums(cnt):
    out = {}
    for (kd, r, s, k), n in cnt.items():
        if s >= 0: out[s] = out.get(s, Fraction(0)) + W(k) * n
    return out

def seed_series(rec):
    obs = [e for e in rec["pocket_log"] if e["epoch"] >= rec["obs_start"]]
    ctl = {e["epoch"]: e for e in rec["control_log"]}
    # time-mean boundary shell occupancy (support matching weights)
    occ = {}
    for e in obs:
        for (r, s, k), n in e["area"].items():
            if r == "B" and s >= 0:
                occ[s] = occ.get(s, Fraction(0)) + W(k) * n
    tot = sum(occ.values(), Fraction(0))
    wts = {s: v / tot for s, v in occ.items()} if tot > 0 else {}
    rows = []
    for e in obs:
        c = ctl.get(e["epoch"])
        if c is None: continue
        A_B = region_sum(e["area"], "B")
        row = dict(epoch=e["epoch"], boundary_faces=e["boundary_faces"],
                   pocket_faces=e["pocket_faces"], A_B=A_B)
        if A_B > 0:
            row["d_B"] = region_sum(e["frus"], "B") / A_B
            row["s_B"] = served_region_sum(e["served"], "B") / A_B
        ca, cf, cs = shell_sums(c["area"]), shell_sums(c["frus"]), served_shell_sums(c["served"])
        vd = vs = Fraction(0); wt_used = Fraction(0)
        for s, w in wts.items():
            if ca.get(s, 0) > 0:
                vd += w * (cf.get(s, Fraction(0)) / ca[s])
                vs += w * (cs.get(s, Fraction(0)) / ca[s])
                wt_used += w
        if wt_used > 0:
            row["v_d"], row["v_s"] = vd / wt_used, vs / wt_used
        if "d_B" in row and "v_d" in row:
            row["dD"], row["dS"] = row["d_B"] - row["v_d"], row["s_B"] - row["v_s"]
        rows.append(row)
    return rows

def halves(rows):
    good = [r for r in rows if "dD" in r]
    h = len(good) // 2
    return good[:h], good[h:]

def fmean(rows, key):
    vals = [r[key] for r in rows if key in r]
    return sum(vals, Fraction(0)) / len(vals) if vals else None

def ols_slope(rows, key):
    pts = [(r["epoch"], float(r[key])) for r in rows if key in r]
    if len(pts) < 3: return None
    n = len(pts); sx = sum(p[0] for p in pts); sy = sum(p[1] for p in pts)
    sxx = sum(p[0] ** 2 for p in pts); sxy = sum(p[0] * p[1] for p in pts)
    den = n * sxx - sx * sx
    return (n * sxy - sx * sy) / den if den else None

def bootstrap_p_neg(slopes, n=2000, seed=20260722):
    """Seed-level bootstrap: one-sided p that the mean W2 dS slope is negative."""
    import random
    rng = random.Random(seed); k = len(slopes)
    if k == 0: return None
    neg = 0
    for _ in range(n):
        m = sum(rng.choice(slopes) for _ in range(k)) / k
        if m < 0: neg += 1
    return neg / n

def main(cfgp, cache_dir, seedsp, outp):
    cohort = json.loads(Path(seedsp).read_text(encoding="utf-8"))["cohort"]
    full = json.loads(Path(cfgp).read_text(encoding="utf-8"))
    cfg = full["gates_b0"]
    cfgh = hashlib.sha256(json.dumps(full, sort_keys=True).encode("utf-8")).hexdigest()[:8]
    seeds = []
    for p in sorted(Path(cache_dir).glob("b0_seed*.pkl.gz")):
        with gzip.open(p, "rb") as f: rec = pickle.load(f)
        if rec.get("cfg_hash") != cfgh:
            sys.exit(f"ADJUDICATE ABORT: {p.name} was produced under a different "
                     f"config (cache {rec.get('cfg_hash')} vs current {cfgh}). "
                     "Clear stale caches from the cache_dir and rerun the run stage.")
        rows = seed_series(rec)
        w1, w2 = halves(rows)
        nb = [r for r in rows if r["boundary_faces"] > 0]
        s = dict(seed=rec["seed"], clearance_ok=rec["clearance_ok"],
                 n_epochs=len(rows),
                 frac_boundary_nonempty=(len(nb) / len(rows)) if rows else 0.0,
                 mean_dD=fmean(rows, "dD"), mean_dS=fmean(rows, "dS"),
                 mean_dS_W1=fmean(w1, "dS"), mean_dS_W2=fmean(w2, "dS"),
                 slope_dS_W2=ols_slope(w2, "dS"), slope_dD_W2=ols_slope(w2, "dD"))
        m1, m2 = s["mean_dS_W1"], s["mean_dS_W2"]
        if m1 is not None and m2 is not None and (m1 + m2) != 0:
            s["rel_change_dS"] = float(abs(m2 - m1) / abs((m1 + m2) / 2))
        seeds.append(s)
    present = {s["seed"] for s in seeds}
    missing = [s for s in cohort if s not in present]
    if missing:
        sys.exit(f"ADJUDICATE ABORT: cohort incomplete -- missing seeds {missing}. "
                 "Rerun the run stage to resume; adjudication requires the full cohort.")
    val = [s for s in seeds if s["clearance_ok"]]
    n = len(val)
    med = lambda xs: sorted(xs)[len(xs) // 2] if xs else None
    dD = [s["mean_dD"] for s in val if s["mean_dD"] is not None]
    dS = [s["mean_dS"] for s in val if s["mean_dS"] is not None]
    g = {}
    g["G0"] = (med(dD) is not None and med(dD) > 0
               and sum(1 for x in dD if x > 0) >= cfg["g0_min_pos"])
    g["G1"] = sum(1 for s in val
                  if s["frac_boundary_nonempty"] >= cfg["g1_min_frac_nonempty"]) \
              >= cfg["g1_min_seeds"]
    g["G2"] = (med(dS) is not None and med(dS) > 0
               and sum(1 for x in dS if x > 0) >= cfg["g2_min_pos"])
    rel_ok = [s for s in val if s.get("rel_change_dS") is not None
              and s["rel_change_dS"] <= cfg["g3_rel_tol"]]
    slopes = [s["slope_dS_W2"] for s in val if s["slope_dS_W2"] is not None]
    p_neg = bootstrap_p_neg(slopes)
    g["G3"] = (len(rel_ok) >= cfg["g3_min_seeds"]
               and (p_neg is None or p_neg > cfg["g3_alpha"]))
    stock = {}
    for s in val:
        sl = s["slope_dD_W2"]
        stock[s["seed"]] = ("UNKNOWN" if sl is None else
                            "POOLING" if sl > cfg["g4_stock_tol"] else
                            "DRAINING" if sl < -cfg["g4_stock_tol"] else "STEADY")
    if not g["G1"]:
        cls = CLASSES[3]
    elif not g["G0"]:
        cls = CLASSES[2]
    elif g["G2"] and g["G3"]:
        cls = CLASSES[0]
    else:
        cls = CLASSES[1]
    lam = None
    if cls == CLASSES[0]:
        per = [float(s["mean_dS"]) for s in val if s["mean_dS"] is not None]
        lam = dict(note="lambda_dress candidate: time-mean dS density, per seed "
                        "(exact Fractions in per-seed table); registered rate "
                        "pending B1 (additivity, vacuum-zero, covariance audit)",
                   per_seed_float=per)
    rec = dict(classification=cls, gates=g, n_valid_seeds=n,
               bootstrap_p_slope_neg=p_neg, stock_classes=stock,
               lambda_dress=lam,
               per_seed=[{k: (str(v) if isinstance(v, Fraction) else v)
                          for k, v in s.items()} for s in seeds])
    Path(outp).write_text(json.dumps(rec, indent=1), encoding="utf-8", newline="\n")
    print(json.dumps({k: rec[k] for k in ("classification", "gates",
          "n_valid_seeds", "bootstrap_p_slope_neg", "stock_classes")}, indent=1))

if __name__ == "__main__":
    main(*sys.argv[1:5])
