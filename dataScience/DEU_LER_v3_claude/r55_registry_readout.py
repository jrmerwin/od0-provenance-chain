#!/usr/bin/env python3
"""OD0-R55 Part 4: registry-inclusion readout (labeled; H1 provenance of
the question disclosed; H1 is spent - this is NOT a comparison).

5 seeded trajectories x 10^4 steps at all 144 registered points, objects
carried with exact recursive identity; per checkpoint: fraction of the 173
registry objects (R50 exact arrow) present, by grade; still-changing flag
between 10^3 and 10^4. Also, at the supercritical point (2,3,0):
burst-count trace (terminal-size readout for Part 2).
"""
import json
import random
from fractions import Fraction
from pathlib import Path

PKG = Path(__file__).resolve().parent
QF, QR = 11, 2
CHECKPOINTS = [100, 1000, 10000]


def obj_str(o):
    if isinstance(o, str):
        return o
    return "{" + ",".join(sorted(obj_str(c) for c in o)) + "}"


def dec(fr, digits=6):
    if fr == 0:
        return "0"
    scale = 10 ** (digits + 2)
    q = (abs(fr).numerator * scale) // abs(fr).denominator
    s = str(q).rjust(digits + 3, "0")
    return (s[:-digits - 2] or "0") + "." + s[-digits - 2:-2]


def build_registry():
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def canc(o):
        if isinstance(o, str):
            return frozenset({o})
        r = {o}
        for c in o:
            r |= canc(c)
        return frozenset(r)

    allobj = {"a", "b"}
    for size in range(2, 8):
        cur = sorted(allobj, key=obj_str)
        new = set()
        for i, l in enumerate(cur):
            for r in cur[i + 1:]:
                cand = frozenset({l, r})
                if cand not in allobj and len(canc(cand)) == size:
                    new.add(cand)
        allobj |= new
    grade = {o: len(canc(o)) for o in allobj}
    return allobj, grade


REGISTRY, GRADE = build_registry()
GRADES = sorted(set(GRADE.values()))


def run_traj(Gamma, m, H, seed, steps):
    rng = random.Random(seed)
    objs = ["a", "b"]                     # id -> object
    anc = [1, 2]
    paths_to = [0, 0]
    pairs = {}
    children = [0, 0]
    recorded = 0
    B = 0
    P = 0
    served_prev = ()
    bursts = 0
    cp = {}
    for k in range(1, steps + 1):
        sp = sorted(served_prev)
        batch = [(sp[i], sp[j]) for i in range(len(sp))
                 for j in range(i + 1, len(sp)) if (sp[i], sp[j]) not in pairs]
        new_rec = rep_rec = 0
        for (u, v) in batch:
            oid = len(anc)
            objs.append(frozenset({objs[u], objs[v]}))
            anc.append(anc[u] | anc[v] | (1 << oid))
            paths_to.append((paths_to[u] + 1) + (paths_to[v] + 1))
            children[u] += 1
            children[v] += 1
            children.append(0)
            pairs[(u, v)] = oid
            cone = anc[u] | anc[v]
            mask = cone & ~recorded
            while mask:
                low = mask & -mask
                new_rec += paths_to[low.bit_length() - 1]
                mask ^= low
            mask = cone & recorded
            while mask:
                low = mask & -mask
                rep_rec += paths_to[low.bit_length() - 1]
                mask ^= low
            recorded |= cone
        if batch:
            bursts += 1
        requests = QF * new_rec + QR * rep_rec
        F = B + m + requests
        D = len(anc)
        n = min(Gamma, F + D)
        f_rem, d_rem = F, D
        sF = sV = 0
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
        Pm = P + 2 * sF
        base = max(1, Pm // 6)
        quota = 2 * ((base + 1) // 2)
        gate = Bm >= Gamma and Pm >= 6
        voided = min(quota, H, Bm, Pm) if gate else 0
        B, P = Bm - voided, Pm - voided
        if k in CHECKPOINTS:
            present = set(objs) & REGISTRY
            by_grade = {}
            for o in present:
                g = GRADE[o]
                by_grade[g] = by_grade.get(g, 0) + 1
            cp[k] = {"X": len(objs), "registry_present": len(present),
                     "by_grade": {str(g): by_grade.get(g, 0)
                                  for g in GRADES},
                     "bursts": bursts}
    return cp


def main():
    grade_totals = {}
    for o in REGISTRY:
        grade_totals[GRADE[o]] = grade_totals.get(GRADE[o], 0) + 1
    points = []
    for Gamma in range(2, 6):
        for m in range(4):
            for H in range(9):
                per_cp = {k: {"present": [], "by_grade": {}, "bursts": []}
                          for k in CHECKPOINTS}
                for t in range(5):
                    seed = 1000000 * Gamma + 10000 * m + 100 * H + t
                    cps = run_traj(Gamma, m, H, seed, 10000)
                    for k, row in cps.items():
                        per_cp[k]["present"].append(row["registry_present"])
                        per_cp[k]["bursts"].append(row["bursts"])
                        for g, c in row["by_grade"].items():
                            per_cp[k]["by_grade"].setdefault(g, []).append(c)
                summ = {}
                for k in CHECKPOINTS:
                    pc = per_cp[k]
                    summ[str(k)] = {
                        "registry_present_mean_dec": dec(
                            Fraction(sum(pc["present"]),
                                     len(pc["present"]))),
                        "fraction_of_173_dec": dec(
                            Fraction(sum(pc["present"]),
                                     173 * len(pc["present"]))),
                        "by_grade_mean": {
                            g: dec(Fraction(sum(v), len(v)))
                            for g, v in sorted(pc["by_grade"].items())},
                        "bursts_mean_dec": dec(
                            Fraction(sum(pc["bursts"]), len(pc["bursts"]))),
                    }
                changing = (summ["10000"]["registry_present_mean_dec"]
                            != summ["1000"]["registry_present_mean_dec"])
                points.append({"Gamma": Gamma, "m": m, "H": H,
                               "checkpoints": summ,
                               "still_changing_1e3_to_1e4": changing})
    out = {
        "schema": "R55_REGISTRY_READOUT_V1",
        "label": "READOUT - labeled, seeded, never proof; H1 provenance "
                 "of the question disclosed; H1 is spent (no comparison)",
        "registry_grade_totals": {str(g): c for g, c
                                  in sorted(grade_totals.items())},
        "protocol": {"trajectories": 5, "steps": 10000,
                     "checkpoints": CHECKPOINTS,
                     "seed_scheme": "random.Random(1000000*Gamma+10000*m"
                                    "+100*H+t)"},
        "points": points,
    }
    (PKG / "R55_REGISTRY_READOUT_RAW.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    ex = next(p for p in points
              if p["Gamma"] == 2 and p["m"] == 0 and p["H"] == 0)
    sup = next(p for p in points
               if p["Gamma"] == 2 and p["m"] == 3 and p["H"] == 0)
    print("exemplar (2,0,0):")
    for k in CHECKPOINTS:
        s = ex["checkpoints"][str(k)]
        print(" k=", k, "present:", s["registry_present_mean_dec"],
              "frac:", s["fraction_of_173_dec"], "grades:",
              s["by_grade_mean"])
    print("supercritical (2,3,0) bursts:",
          [sup["checkpoints"][str(k)]["bursts_mean_dec"]
           for k in CHECKPOINTS])


if __name__ == "__main__":
    main()
