#!/usr/bin/env python3
"""OD0-R52 sampled readout engine (Part 4.3 + Part 5).

SAMPLED - LABELED - NEVER PROOF. Seeded per the frozen scheme
random.Random(1000000*Gamma + 10000*m + 100*H + trajectory_index).
Sampling is exact-integer (sequential without-replacement draws); reported
aggregates are decimal strings produced by integer division (12 significant
digits) and are labeled sampled/approximate. Load law: c_first = 11 per
newly recorded prefix, c_repeat = 2 per repeat record (Part 1.4).

Objects are abstract ids; ancestry as bitmasks; per-prefix record counting
via exact path counts (paths_to) and the monotone recorded-cone mask.
A recorded per-trajectory operation budget bounds bit-iteration cost; a
trajectory exceeding it is truncated at that step and counted (deterministic
under the recorded seeds).
"""
import json
import random
from fractions import Fraction
from pathlib import Path

PKG = Path(__file__).resolve().parent

TRAJ = 100
STEPS = 500
CHECKPOINTS = [50, 100, 200, 300, 400, 500]
OP_BUDGET = 3_000_000


def dec(fr, digits=12):
    """Deterministic decimal string of a Fraction via integer division."""
    if fr == 0:
        return "0"
    neg = fr < 0
    fr = abs(fr)
    scale = 10 ** (digits + 2)
    q = (fr.numerator * scale) // fr.denominator
    s = str(q).rjust(digits + 3, "0")
    intpart = s[:-digits - 2] or "0"
    fracpart = s[-digits - 2:-2]
    return ("-" if neg else "") + intpart + "." + fracpart


def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def run_trajectory(Gamma, m, H, seed, steps, relief_on=True, pop_factor=2):
    rng = random.Random(seed)
    # object arrays
    anc = [1 << 0, 1 << 1]          # closed ancestry masks (self included)
    paths_to = [0, 0]               # directed paths of length >=1 ending at o
    pairs = {}                      # frozenset({u,v}) -> object id
    children_count = [0, 0]
    recorded = 0                    # mask: objects whose ending-paths are recorded
    B = 0
    P = 0
    served_prev = ()
    ops = 0
    truncated = False
    checkpoints = {}
    F_cur = 0
    for k in range(1, steps + 1):
        # fire batch
        batch = []
        sp = sorted(served_prev)
        for i in range(len(sp)):
            for j in range(i + 1, len(sp)):
                key = (sp[i], sp[j])
                if key not in pairs:
                    batch.append(key)
        new_records = 0
        repeat_records = 0
        cone_union_new = 0
        for (u, v) in batch:
            oid = len(anc)
            a = anc[u] | anc[v] | (1 << oid)
            anc.append(a)
            paths_to.append((paths_to[u] + 1) + (paths_to[v] + 1))
            children_count[u] += 1
            children_count[v] += 1
            children_count.append(0)
            pairs[(u, v)] = oid
            cone = anc[u] | anc[v]
            new_mask = cone & ~recorded
            rep_mask = cone & recorded
            for w in bits(new_mask):
                new_records += paths_to[w]
                ops += 1
            for w in bits(rep_mask):
                repeat_records += paths_to[w]
                ops += 1
            cone_union_new |= new_mask
            recorded |= cone
        # note: aggregate first/repeat across the step is order-free; the
        # per-event loop above records each event's cone with the running
        # recorded mask (canonical order), and the step totals equal
        # 11*(paths in union-of-cones minus previously recorded) +
        # 2*(all other cone paths) exactly.
        requests = 11 * new_records + 2 * repeat_records
        F = B + m + requests
        D = len(anc)
        n = min(Gamma, F + D)
        # exact sequential without-replacement service sampling
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
        F_cur = F
        if ops > OP_BUDGET:
            truncated = True
        if k in CHECKPOINTS or truncated or k == steps:
            used = sum(1 for c in children_count if c > 0)
            shell = len(anc) - used
            checkpoints[k] = {
                "X": len(anc), "shell": shell,
                "x_dec": dec(Fraction(D, F + D)),
                "B_digits": len(str(B)),
                "g_new_this_step": len(batch),
                "new_records": new_records,
                "repeat_records": repeat_records,
            }
        if truncated:
            break
    return checkpoints, truncated, k


def run_point(Gamma, m, H, relief_on=True, pop_factor=2, tag=""):
    agg = {}
    truncations = 0
    last_k = []
    for t in range(TRAJ):
        seed = 1000000 * Gamma + 10000 * m + 100 * H + t
        cps, trunc, kend = run_trajectory(Gamma, m, H, seed, STEPS,
                                          relief_on, pop_factor)
        truncations += int(trunc)
        last_k.append(kend)
        for k, row in cps.items():
            slot = agg.setdefault(k, {"X": [], "shell": [], "x": [],
                                      "B_digits": [], "g": []})
            slot["X"].append(row["X"])
            slot["shell"].append(row["shell"])
            slot["x"].append(row["x_dec"])
            slot["B_digits"].append(row["B_digits"])
            slot["g"].append(row["g_new_this_step"])
    summary = {}
    for k in sorted(agg):
        s = agg[k]
        xs = sorted(s["x"])
        summary[str(k)] = {
            "n_traj_at_k": len(s["X"]),
            "X_mean_dec": dec(Fraction(sum(s["X"]), len(s["X"]))),
            "X_min_max": [min(s["X"]), max(s["X"])],
            "shell_mean_dec": dec(Fraction(sum(s["shell"]), len(s["shell"]))),
            "x_median_dec": xs[len(xs) // 2],
            "x_min_max_dec": [xs[0], xs[-1]],
            "B_digits_min_max": [min(s["B_digits"]), max(s["B_digits"])],
            "g_mean_dec": dec(Fraction(sum(s["g"]), len(s["g"]))),
        }
    return {"Gamma": Gamma, "m": m, "H": H, "tag": tag,
            "trajectories": TRAJ, "steps": STEPS,
            "truncated_trajectories": truncations,
            "checkpoint_summary": summary}


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
        "schema": "R52_SAMPLED_READOUT_V1",
        "label": "SAMPLED - seeded - never cited as proof",
        "protocol": {"trajectories_per_point": TRAJ,
                     "steps_per_trajectory": STEPS,
                     "seed_scheme": "random.Random(1000000*Gamma + 10000*m "
                                    "+ 100*H + trajectory_index)",
                     "op_budget_per_trajectory": OP_BUDGET,
                     "aggregates": "decimal strings via integer division, "
                                   "12 significant digits, deterministic"},
        "points": points,
        "sensitivity": sensitivity,
    }
    (PKG / "R52_SAMPLED_READOUT.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    ex = points[0]["checkpoint_summary"]
    print("points:", len(points), "sensitivity:", len(sensitivity))
    print("exemplar (2,0,0):")
    for k in sorted(ex, key=int):
        print("  k=", k, "X:", ex[k]["X_mean_dec"], "x_med:",
              ex[k]["x_median_dec"], "shell:", ex[k]["shell_mean_dec"],
              "B_digits:", ex[k]["B_digits_min_max"])


if __name__ == "__main__":
    main()
