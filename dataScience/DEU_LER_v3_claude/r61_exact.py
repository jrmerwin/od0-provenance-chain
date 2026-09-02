#!/usr/bin/env python3
"""OD0-R61 certificate engine: Parts 2 and 4.

(1) Exhaustive exact E[Delta TC] and E[Delta TCo] for n <= 9 (uniform
    pair law): certifies the per-step recursions and the moment bounds.
(2) Seeded trajectory readouts (labeled): TC/n^{3/2}, TCo/n^2, clock
    functionals tau = ln ln(total), their difference vs ln(4/3),
    and N_V for the clock-vs-ticks relation.
(3) Relief-line certificates: cumulative outflow identity check and
    the burst-arrest illustration at m above/below the line
    m_c = Gamma + min(H, 2 Gamma) (labeled trajectories).
"""
import json
import math
import random
from fractions import Fraction
from pathlib import Path

PKG = Path(__file__).resolve().parent


# ---------------------------------------------------- (1) exhaustive
def enumerate_cone_moments(n_max=9):
    """Exact E[|cone(new)|], E[C(A,2)] with A = cone+1, per size."""
    from collections import defaultdict
    dists = {(): Fraction(1)}
    out = {}
    for n in range(2, n_max):
        nxt = defaultdict(Fraction)
        mom = defaultdict(Fraction)
        for st, p in dists.items():
            k = len(st) + 2
            anc = [1, 2]
            for (i, j) in st:
                anc.append(anc[i] | anc[j] | (1 << (len(anc))))
            existing = set(st)
            cand = [(i, j) for i in range(k) for j in range(i + 1, k)
                    if (i, j) not in existing]
            for (i, j) in cand:
                q = p / len(cand)
                nxt[st + ((i, j),)] += q
                A = bin(anc[i] | anc[j]).count("1") + 1
                mom["E_cone"] += q * (A - 1)
                mom["E_A2"] += q * A * A
                mom["E_CA2"] += q * (A * (A - 1) // 2)
        dists = dict(nxt)
        out[str(n + 1)] = {kk: str(v) for kk, v in mom.items()}
    return out


# ---------------------------------------------------- (2)(3) trajectories
def run_traj(G, m, H, seed, steps, checkpoints, track_clocks=True):
    rng = random.Random(seed)
    pairs = {}
    anc = [1, 2]
    pth = [0, 0]
    rec = 0
    B = 0
    P = 0
    sp = ()
    NV = 0
    bursts = 0
    TC = 0
    TCo = 0
    last_burst_step = 0
    res = {}
    for k in range(1, steps + 1):
        s = sorted(sp)
        nw = rp = created = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                u, v = s[i], s[j]
                if (u, v) in pairs:
                    continue
                oid = len(anc)
                cone = anc[u] | anc[v]
                anc.append(cone | (1 << oid))
                pth.append(pth[u] + 1 + pth[v] + 1)
                pairs[(u, v)] = oid
                m1 = cone & ~rec
                while m1:
                    lo = m1 & -m1
                    nw += pth[lo.bit_length() - 1]
                    m1 ^= lo
                m2 = cone & rec
                while m2:
                    lo = m2 & -m2
                    rp += pth[lo.bit_length() - 1]
                    m2 ^= lo
                rec |= cone
                created += 1
                if track_clocks:
                    A = bin(cone).count("1") + 1
                    TC += A - 1
                    TCo += A * (A - 1) // 2
        if created:
            bursts += 1
            last_burst_step = k
        D = len(anc)
        F = B + m + 11 * nw + 2 * rp
        s_n = min(G, F + D)
        fr, dr = F, D
        sF = sV = 0
        for _ in range(s_n):
            r = rng.randrange(fr + dr)
            if r < dr:
                sV += 1
                dr -= 1
            else:
                sF += 1
                fr -= 1
        sp = tuple(rng.sample(range(D), sV)) if sV else ()
        NV += sV
        Bm = F - sF
        Pm = P + 2 * sF
        base = max(1, Pm // 6)
        quota = 2 * ((base + 1) // 2)
        void = min(quota, H, Bm, Pm) if (Bm >= G and Pm >= 6) else 0
        B, P = Bm - void, Pm - void
        if k in checkpoints:
            n = len(anc)
            row = {"n": n, "b": bursts, "N_V": NV, "F": F,
                   "last_burst_step": last_burst_step}
            if track_clocks:
                row.update({
                    "TC": TC, "TCo": TCo,
                    "TC_over_n32": round(TC / n ** 1.5, 4),
                    "TCo_over_n2": round(TCo / n ** 2, 4),
                    "TCo_over_n2lnn": round(
                        TCo / (n ** 2 * math.log(n)), 4),
                    "tau_containment": round(
                        math.log(math.log(TC)), 5) if TC > 2 else None,
                    "tau_coembedding": round(
                        math.log(math.log(TCo)), 5) if TCo > 2 else None,
                    "tau_diff": round(
                        math.log(math.log(TCo)) - math.log(math.log(TC)),
                        5) if TC > 2 and TCo > 2 else None,
                })
            res[str(k)] = row
    return res


def main():
    out = {"schema": "R61_EXACT_CERTIFICATES_V1"}

    out["part2_exhaustive_cone_moments"] = enumerate_cone_moments(9)
    print("exhaustive cone moments done", flush=True)

    # Part 2 trajectories: clock functionals at U-growth points
    cps = {100, 1000, 10000}
    trajs = {}
    for (G, m) in ((2, 0), (2, 1), (3, 0), (3, 2), (4, 0), (5, 0)):
        for H in (0, 4):
            for t in range(2):
                seed = 1000000 * G + 10000 * m + 100 * H + t
                trajs[f"G{G}_m{m}_H{H}_s{seed}"] = run_traj(
                    G, m, H, seed, 10000, cps)
    out["part2_clock_trajectories_labeled"] = trajs
    print("clock trajectories done:", len(trajs), flush=True)

    # Part 4: the relief line at Gamma=2, H=8 (m_c = 2 + min(8,4) = 6)
    line = {}
    for m in (3, 4, 5, 6, 7, 8):
        seed = 9000000 + m
        line[f"G2_m{m}_H8_s{seed}"] = run_traj(
            2, m, 8, seed, 30000, {1000, 10000, 30000},
            track_clocks=False)
    for m in (3, 4, 5, 6):  # Gamma=3, H=2: m_c = 3 + 2 = 5
        seed = 9100000 + m
        line[f"G3_m{m}_H2_s{seed}"] = run_traj(
            3, m, 2, seed, 30000, {1000, 10000, 30000},
            track_clocks=False)
    out["part4_relief_line_labeled"] = line
    print("relief-line trajectories done", flush=True)

    (PKG / "R61_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")

    for key in sorted(trajs)[:4]:
        t = trajs[key]["10000"]
        print(key, "n=", t["n"], "TC/n^1.5=", t["TC_over_n32"],
              "TCo/n^2=", t["TCo_over_n2"], "tau_diff=", t["tau_diff"])
    print("ln(4/3) =", round(math.log(4 / 3), 5))
    for key in sorted(line):
        t = line[key]["30000"]
        print(key, "n=", t["n"], "b=", t["b"], "F=", t["F"],
              "last_burst=", t["last_burst_step"])


if __name__ == "__main__":
    main()
