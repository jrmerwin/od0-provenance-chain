#!/usr/bin/env python3
"""OD0-R62 Part 4: quarantined post-opening readouts.
POST_OPENING_READOUT_NOT_ADJUDICATION. Computes, on the seeded derived
trajectories (random ideal of the throttled process), the historical
UNMAPPED_COMPUTABLE functionals: the containment-weight participation
ratio (R56 O4 definition), the top-hub containment share (condensation
proxy), and the condensation fraction f = 1 - 1/d_max over containment
degrees. Deterministic."""
import json
import math
import random
from pathlib import Path

PKG = Path(__file__).resolve().parent


def run(G, m, H, seed, steps):
    rng = random.Random(seed)
    pairs = {}
    anc = [1, 2]
    rec_dummy = 0
    pth = [0, 0]
    B = 0
    P = 0
    sp = ()
    rec = 0
    for k in range(1, steps + 1):
        s = sorted(sp)
        nw = rp = 0
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
        Bm = F - sF
        Pm = P + 2 * sF
        base = max(1, Pm // 6)
        quota = 2 * ((base + 1) // 2)
        void = min(quota, H, Bm, Pm) if (Bm >= G and Pm >= 6) else 0
        B, P = Bm - void, Pm - void
    n = len(anc)
    # containment weights c_w = strict descendant counts
    c = [0] * n
    for o in range(n):
        mask = anc[o] & ~(1 << o)
        while mask:
            lo = mask & -mask
            c[lo.bit_length() - 1] += 1
            mask ^= lo
    tot = sum(c)
    tot2 = sum(x * x for x in c)
    pr = (tot * tot / tot2) if tot2 else 0.0
    cmax = max(c)
    return {"n": n, "total_containment": tot,
            "participation_ratio_O4": round(pr, 3),
            "PR_over_n": round(pr / n, 4),
            "top_hub_share": round(cmax / tot, 4) if tot else None,
            "condensation_f_1_minus_1_over_dmax":
                round(1 - 1 / cmax, 4) if cmax else None}


out = {"schema": "R62_PART4_QUARANTINED_READOUTS_V1",
       "label": "POST_OPENING_READOUT_NOT_ADJUDICATION",
       "note": "Historical UNMAPPED_COMPUTABLE functionals evaluated on "
               "the derived random-ideal trajectories (labeled, seeded). "
               "The lnln clock functionals on derived trajectories are "
               "already tabulated in R61_EXACT_CERTIFICATES.json "
               "(part2_clock_trajectories_labeled) and are cited, not "
               "recomputed. Only permitted future use: candidate "
               "target-blind freezing for H5.",
       "rows": {}}
for (G, m, H) in ((2, 0, 0), (3, 0, 0), (4, 0, 4)):
    seed = 1000000 * G + 10000 * m + 100 * H
    out["rows"][f"G{G}_m{m}_H{H}_s{seed}"] = run(G, m, H, seed, 10000)
(PKG / "R62_PART4_READOUTS.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n",
    encoding="utf-8", newline="\n")
for k, v in out["rows"].items():
    print(k, v)
