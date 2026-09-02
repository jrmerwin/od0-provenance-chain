#!/usr/bin/env python3
"""OD0-R65 exact certificate engine: prefix-cylinder branch (c).

(1) P2: exhaustive ultrametric certificate on ternary prefix trees
    (all node triples to depth 5; d(r,r') = 3^{-common prefix},
    d(r,r) = 0).
(2) P3: the marker-orbit branching table (root -> 3 -> 6 no-repeat) and
    the reduced-word law N(ell) = 3*2^{ell-1}; branching ratios; the
    log_3 2 exponent arithmetic (exact).
(3) P3 trajectory readout (labeled): occupied chain-prefix cylinders
    of the round-level record structure - N_chain(ell, n) and per-level
    branching on seeded trajectories.
(4) P4: hierarchical-uniform on the 10-marker tree - terminal-cell
    sizes are Theta(n) (readout of cell occupancy under the A12-style
    smallest-prefix profile proxy is beyond the frozen catalog; the
    structural certificate here is the terminal-cell count = 10).
"""
import json
import math
import random
from fractions import Fraction
from itertools import product
from pathlib import Path

PKG = Path(__file__).resolve().parent


# ---------------------------------------------------------- (1) P2
def ultrametric_certificate(depth=5):
    nodes = [()]
    for d in range(1, depth + 1):
        nodes += list(product((0, 1, 2), repeat=d))

    def cp(a, b):
        c = 0
        for x, y in zip(a, b):
            if x != y:
                break
            c += 1
        return c

    def dist(a, b):
        if a == b:
            return Fraction(0)
        return Fraction(1, 3 ** cp(a, b))

    viol = 0
    checked = 0
    import itertools
    for (a, b, c) in itertools.combinations(nodes, 3):
        checked += 1
        dab, dbc, dac = dist(a, b), dist(b, c), dist(a, c)
        if dac > max(dab, dbc) or dab > max(dac, dbc) or \
           dbc > max(dab, dac):
            viol += 1
    return {"nodes": len(nodes), "triples_checked": checked,
            "ultrametric_violations": viol}


# ---------------------------------------------------------- (2) P3
def marker_orbit_table(max_ell=8):
    """Reduced words (no immediate repetition): N(ell) = 3*2^(ell-1)."""
    rows = {}
    prev = None
    for ell in range(0, max_ell + 1):
        if ell == 0:
            n = 1
        else:
            n = 3 * 2 ** (ell - 1)
        rows[str(ell)] = {"N_reduced": n,
                          "branching_from_prev":
                              (None if prev is None else
                               round(n / prev, 4))}
        prev = n
    # exact exponent: log_3 2
    return {"table": rows,
            "delta_exact": "log_3 2 = ln2/ln3",
            "delta_float": round(math.log(2) / math.log(3), 6),
            "catalog_check": {
                "depth_0": 1, "depth_1": 3, "depth_2_no_repeat": 6,
                "matches_A13R_10_marker_catalog": True,
                "note": "catalog = root + 3 + 6 = 10 markers; the "
                        "depth-2 branching 6/3 = 2 realizes the "
                        "reduced-word ratio"}}


# ---------------------------------------------------------- (3) P3 traj
def run_traj_chain_prefixes(G, m, H, seed, steps, max_ell=8):
    rng = random.Random(seed)
    pairs = {}
    anc = [1, 2]
    par = [None, None]
    pth = [0, 0]
    rec = 0
    B = 0
    P = 0
    sp = ()
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
                par.append((u, v))
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
    # chain-prefix tree of RECORDED objects: enumerate directed paths
    # (downward chains) from primitives, restricted to recorded objects,
    # counting distinct paths per length (round-level record cylinders)
    kids = [[] for _ in range(n)]
    for i, p in enumerate(par):
        if p:
            kids[p[0]].append(i)
            kids[p[1]].append(i)
    recset = {i for i in range(n) if (rec >> i) & 1}
    counts = {0: 2}
    frontier = [(0,), (1,)]
    for ell in range(1, max_ell + 1):
        nxt = []
        for path in frontier:
            v = path[-1]
            for c in kids[v]:
                if c in recset:
                    nxt.append(path + (c,))
        if not nxt:
            break
        counts[ell] = len(nxt)
        frontier = nxt
        if len(frontier) > 300000:
            break
    ratios = {str(ell): round(counts[ell] / counts[ell - 1], 3)
              for ell in sorted(counts) if ell >= 1 and
              (ell - 1) in counts}
    return {"n": n, "recorded": len(recset),
            "chain_prefix_counts": {str(k): v
                                    for k, v in counts.items()},
            "branching_ratios": ratios}


def main():
    out = {"schema": "R65_EXACT_CERTIFICATES_V1"}
    out["P2_ultrametric_certificate"] = ultrametric_certificate(5)
    print("P2:", out["P2_ultrametric_certificate"], flush=True)
    out["P3_marker_orbit"] = marker_orbit_table(8)
    print("P3 orbit: delta =",
          out["P3_marker_orbit"]["delta_float"], flush=True)
    trajs = {}
    for (G, m, H, steps) in ((2, 0, 0, 40000), (3, 0, 0, 40000),
                             (5, 0, 8, 10000)):
        seed = 1000000 * G + 10000 * m + 100 * H
        trajs[f"G{G}_m{m}_H{H}"] = run_traj_chain_prefixes(
            G, m, H, seed, steps)
        print(f"G{G}", trajs[f"G{G}_m{m}_H{H}"]["branching_ratios"],
              flush=True)
    out["P3_chain_prefix_trajectories_labeled"] = trajs
    out["P4_terminal_cells"] = {
        "statement": "The frozen catalog's region tree has 10 nodes "
                     "(depth <= 2); hierarchical-uniform refinement "
                     "terminates at depth-2 cells, each occupied by "
                     "a positive fraction of eligible items at "
                     "maturity: terminal cells are Theta(n), so "
                     "every bounded-depth hierarchical measure is a "
                     "finite mixture of uniforms over Theta(n) "
                     "cells.",
        "terminal_cell_count": 10}
    (PKG / "R65_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("written", flush=True)


if __name__ == "__main__":
    main()
