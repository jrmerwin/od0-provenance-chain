#!/usr/bin/env python3
"""OD0-R54 Part 4: POST_OPENING_READOUT_NOT_ADJUDICATION.

Computes the UNMAPPED_COMPUTABLE historical observables (by their H1
definitions) on derived R53-law sampled trajectories. Quarantined: nothing
here enters the verdict. Seeded identically to the R53 protocol; 5
trajectories at the two deterministic rule points; checkpoints 100/1000/
10000. Exact integers; decimal strings by integer division.
"""
import json
import random
from fractions import Fraction
from pathlib import Path

PKG = Path(__file__).resolve().parent
QF, QR = 11, 2
CHECKPOINTS = [100, 1000, 10000]


def dec(fr, digits=8):
    if fr == 0:
        return "0"
    scale = 10 ** (digits + 2)
    q = (abs(fr).numerator * scale) // abs(fr).denominator
    s = str(q).rjust(digits + 3, "0")
    return ("-" if fr < 0 else "") + (s[:-digits - 2] or "0") + "." + s[-digits - 2:-2]


def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def diameter(adj, n):
    """Exact diameter by BFS from every vertex (n small)."""
    if n < 2:
        return 0
    best = 0
    for s in range(n):
        dist = {s: 0}
        frontier = [s]
        while frontier:
            nxt = []
            for v in frontier:
                for w in adj[v]:
                    if w not in dist:
                        dist[w] = dist[v] + 1
                        nxt.append(w)
            frontier = nxt
        if len(dist) < n:
            return None  # disconnected
        best = max(best, max(dist.values()))
    return best


# Faithful replay: import the R53 sampled trajectory logic inline
def run_traj(Gamma, m, H, seed, steps):
    rng = random.Random(seed)
    anc = [1, 2]
    paths_to = [0, 0]
    pairs = {}
    children = [0, 0]
    recorded = 0
    B = 0
    P = 0
    served_prev = ()
    checkpoints = {}
    for k in range(1, steps + 1):
        sp = sorted(served_prev)
        batch = [(sp[i], sp[j]) for i in range(len(sp))
                 for j in range(i + 1, len(sp)) if (sp[i], sp[j]) not in pairs]
        new_rec = rep_rec = 0
        for (u, v) in batch:
            oid = len(anc)
            anc.append(anc[u] | anc[v] | (1 << oid))
            paths_to.append((paths_to[u] + 1) + (paths_to[v] + 1))
            children[u] += 1
            children[v] += 1
            children.append(0)
            pairs[(u, v)] = oid
            cone = anc[u] | anc[v]
            for w in bits(cone & ~recorded):
                new_rec += paths_to[w]
            for w in bits(cone & recorded):
                rep_rec += paths_to[w]
            recorded |= cone
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
            nobj = len(anc)
            # historical-definition observables on the derived DAG:
            # containment(w) = # objects whose ancestry contains w
            containment = [0] * nobj
            for i in range(nobj):
                for w in bits(anc[i] & ~(1 << i)):
                    containment[w] += 1
            # pair coembedding for the earliest composite pair (a,b)->c
            co_ab = 0
            if nobj > 2:
                for i in range(nobj):
                    if (anc[i] >> 0) & 1 and (anc[i] >> 1) & 1 and i > 1:
                        co_ab += 1
            # support size: # objects with containment > 0 (used in hosts)
            support = sum(1 for c in containment if c > 0)
            # participation ratio of containment weights (exact rational)
            tot = sum(containment)
            if tot:
                num = Fraction(tot * tot,
                               sum(c * c for c in containment if c))
            else:
                num = Fraction(0)
            # parent-child graph diameter
            adj = {i: set() for i in range(nobj)}
            for (u, v), oid in pairs.items():
                adj[u].add(oid)
                adj[oid].add(u)
                adj[v].add(oid)
                adj[oid].add(v)
            diam = diameter(adj, nobj)
            # dilution analog: fraction of X at dag_size <= 7
            ds = [bin(a).count("1") for a in anc]
            early = sum(1 for d0 in ds if d0 <= 7)
            checkpoints[k] = {
                "X": nobj,
                "containment_max": max(containment),
                "containment_mean_dec": dec(Fraction(tot, nobj)),
                "support_fraction_dec": dec(Fraction(support, nobj)),
                "participation_ratio_dec": dec(num),
                "coembed_ab": co_ab,
                "diameter": diam,
                "early_layer_fraction_dec": dec(Fraction(early, nobj)),
            }
    return checkpoints


def main():
    results = []
    for (G, m, H) in ((2, 0, 0), (5, 3, 8)):
        for t in range(5):
            seed = 1000000 * G + 10000 * m + 100 * H + t
            cps = run_traj(G, m, H, seed, 10000)
            results.append({"Gamma": G, "m": m, "H": H, "seed": seed,
                            "checkpoints": {str(k): v
                                            for k, v in cps.items()}})
    out = {
        "schema": "R54_POST_OPENING_READOUT_V1",
        "label": "POST_OPENING_READOUT_NOT_ADJUDICATION - quarantined; "
                 "nothing here enters the verdict; only permitted future "
                 "use is candidate target-blind freezing before H2-H5",
        "observables_computed_by_historical_definition": [
            "containment (objects containing w in ancestry)",
            "pair coembedding (hosts containing both a and b)",
            "support fraction", "participation ratio (containment weights)",
            "parent-child diameter", "early-layer (dag_size<=7) fraction",
        ],
        "trajectories": results,
    }
    (PKG / "R54_POST_OPENING_READOUT.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    ex = results[0]["checkpoints"]
    print("exemplar (2,0,0) seed0:")
    for k in sorted(ex, key=int):
        print(" k=", k, ex[k])


if __name__ == "__main__":
    main()
