#!/usr/bin/env python3
"""OD0-R53 sampled readout engine (Part 4). SAMPLED - LABELED - NEVER PROOF.

50 trajectories x 10^4 steps per registered point (frozen in
R53_INPUT_LOCK.json), seeds random.Random(1000000*Gamma+10000*m+100*H+t).
Tracks |X_k| at checkpoints, cycle statistics (F-excursions from 0), burst
sizes/costs, depth/chains of new objects, time in E0, E1 entry step, shell,
and chain-multiplicity distributions. Exact-integer sampling; aggregates as
deterministic decimal strings.
"""
import json
import random
from fractions import Fraction
from pathlib import Path

PKG = Path(__file__).resolve().parent

TRAJ = 50
STEPS = 10000
CHECKPOINTS = [100, 1000, 3000, 10000]
OP_BUDGET = 8_000_000
QF, QR = 11, 2


def dec(fr, digits=12):
    if fr == 0:
        return "0"
    neg = fr < 0
    fr = abs(fr)
    scale = 10 ** (digits + 2)
    q = (fr.numerator * scale) // fr.denominator
    s = str(q).rjust(digits + 3, "0")
    return ("-" if neg else "") + (s[:-digits - 2] or "0") + "." + s[-digits - 2:-2]


def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def run_trajectory(Gamma, m, H, seed, relief_on=True, pop_factor=2):
    rng = random.Random(seed)
    anc = [1, 2]
    paths_to = [0, 0]
    depth_a = [0, 0]
    chains_a = [1, 1]
    pairs = {}
    children = [0, 0]
    recorded = 0
    B = 0
    P = 0
    served_prev = ()
    ops = 0
    e0_time = 0
    e1_entry = None
    cycles = 0
    prev_F_zero = True
    burst_steps = 0
    total_burst_cost = 0
    new_depths_max = 0
    new_chains_max = 0
    cp = {}
    k_end = 0
    for k in range(1, STEPS + 1):
        k_end = k
        sp = sorted(served_prev)
        batch = []
        for i in range(len(sp)):
            for j in range(i + 1, len(sp)):
                if (sp[i], sp[j]) not in pairs:
                    batch.append((sp[i], sp[j]))
        new_rec = 0
        rep_rec = 0
        for (u, v) in batch:
            oid = len(anc)
            anc.append(anc[u] | anc[v] | (1 << oid))
            paths_to.append((paths_to[u] + 1) + (paths_to[v] + 1))
            depth_a.append(1 + max(depth_a[u], depth_a[v]))
            chains_a.append(chains_a[u] + chains_a[v])
            new_depths_max = max(new_depths_max, depth_a[-1])
            new_chains_max = max(new_chains_max, chains_a[-1])
            children[u] += 1
            children[v] += 1
            children.append(0)
            pairs[(u, v)] = oid
            cone = anc[u] | anc[v]
            for w in bits(cone & ~recorded):
                new_rec += paths_to[w]
                ops += 1
            for w in bits(cone & recorded):
                rep_rec += paths_to[w]
                ops += 1
            recorded |= cone
        requests = QF * new_rec + QR * rep_rec
        if batch:
            burst_steps += 1
            total_burst_cost += requests
        F = B + m + requests
        D = len(anc)
        if F + D <= Gamma:
            e0_time += 1
        if e1_entry is None and D > Gamma:
            e1_entry = k
        n = min(Gamma, F + D)
        f_rem, d_rem = F, D
        sF = 0
        sV = 0
        for _ in range(n):
            r = rng.randrange(f_rem + d_rem)
            if r < d_rem:
                sV += 1
                d_rem -= 1
            else:
                sF += 1
                f_rem -= 1
        served_prev = tuple(rng.sample(range(D), sV)) if sV else ()
        Bm = F - sF
        Pm = P + pop_factor * sF
        if relief_on:
            base = max(1, Pm // 6)
            quota = 2 * ((base + 1) // 2)
            gate = Bm >= Gamma and Pm >= 6
            voided = min(quota, H, Bm, Pm) if gate else 0
        else:
            voided = 0
        B, P = Bm - voided, Pm - voided
        if B == 0 and not prev_F_zero:
            cycles += 1
        prev_F_zero = (B == 0)
        if k in CHECKPOINTS:
            used = sum(1 for c in children if c > 0)
            cp[k] = {"X": len(anc), "shell": len(anc) - used,
                     "x_dec": dec(Fraction(D, F + D)),
                     "B_digits": len(str(B)), "cycles": cycles,
                     "burst_steps": burst_steps,
                     "max_depth": new_depths_max,
                     "max_chains": new_chains_max,
                     "e0_time": e0_time, "e1_entry": e1_entry}
        if ops > OP_BUDGET:
            break
    return cp, k_end


def run_point(Gamma, m, H, relief_on=True, pop_factor=2, tag=""):
    agg = {}
    ends = []
    for t in range(TRAJ):
        seed = 1000000 * Gamma + 10000 * m + 100 * H + t
        cps, kend = run_trajectory(Gamma, m, H, seed, relief_on, pop_factor)
        ends.append(kend)
        for k, row in cps.items():
            s = agg.setdefault(k, {kk: [] for kk in
                                   ("X", "shell", "x", "B_digits", "cycles",
                                    "burst_steps", "max_depth",
                                    "max_chains", "e0_time", "e1_entry")})
            for kk in s:
                val = row["x_dec"] if kk == "x" else row[kk]
                s[kk].append(val)
    summary = {}
    for k in sorted(agg):
        s = agg[k]
        xs = sorted(s["x"])
        e1s = [v for v in s["e1_entry"] if v is not None]
        summary[str(k)] = {
            "n": len(s["X"]),
            "X_mean_dec": dec(Fraction(sum(s["X"]), len(s["X"]))),
            "X_min_max": [min(s["X"]), max(s["X"])],
            "shell_mean_dec": dec(Fraction(sum(s["shell"]),
                                           len(s["shell"]))),
            "x_median_dec": xs[len(xs) // 2],
            "cycles_mean_dec": dec(Fraction(sum(s["cycles"]),
                                            len(s["cycles"]))),
            "burst_steps_mean_dec": dec(Fraction(sum(s["burst_steps"]),
                                                 len(s["burst_steps"]))),
            "max_depth_max": max(s["max_depth"]),
            "max_chains_max": max(s["max_chains"]),
            "e0_time_mean_dec": dec(Fraction(sum(s["e0_time"]),
                                             len(s["e0_time"]))),
            "e1_entry_median": (sorted(e1s)[len(e1s) // 2] if e1s else None),
            "B_digits_min_max": [min(s["B_digits"]), max(s["B_digits"])],
        }
    return {"Gamma": Gamma, "m": m, "H": H, "tag": tag,
            "min_k_end": min(ends), "summary": summary}


def main():
    points = []
    for Gamma in range(2, 6):
        for m in range(4):
            for H in range(9):
                points.append(run_point(Gamma, m, H))
    sensitivity = []
    for (G, m, H) in ((2, 0, 0), (5, 3, 8)):
        sensitivity.append(run_point(G, m, H, relief_on=False,
                                     tag="SENSITIVITY_READOUT_NOT_A_MODEL:"
                                         "relief_disabled"))
        sensitivity.append(run_point(G, m, H, pop_factor=1,
                                     tag="SENSITIVITY_READOUT_NOT_A_MODEL:"
                                         "population_factor_1"))
    out = {
        "schema": "R53_SAMPLED_READOUT_V1",
        "label": "SAMPLED - seeded - never cited as proof",
        "protocol": {"trajectories": TRAJ, "steps": STEPS,
                     "checkpoints": CHECKPOINTS,
                     "seed_scheme": "random.Random(1000000*Gamma+10000*m"
                                    "+100*H+t)",
                     "op_budget": OP_BUDGET,
                     "load_law": "c_first=11 per new prefix, c_repeat=2 "
                                 "per repeat record"},
        "points": points,
        "sensitivity": sensitivity,
    }
    (PKG / "R53_SAMPLED_READOUT.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    ex = points[0]["summary"]
    print("points:", len(points))
    for k in sorted(ex, key=int):
        print(" k=", k, "X:", ex[k]["X_mean_dec"], "cycles:",
              ex[k]["cycles_mean_dec"], "maxdepth:", ex[k]["max_depth_max"],
              "maxchains:", ex[k]["max_chains_max"],
              "e1:", ex[k]["e1_entry_median"])


if __name__ == "__main__":
    main()
