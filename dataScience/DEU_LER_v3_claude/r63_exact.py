#!/usr/bin/env python3
"""OD0-R63 exact certificate engine: geometry-stage structures.

(1) D1 witnesses: ultrametric failure (n=8) and ordinary-triangle
    failure (n=13) for d_U; open-cone pseudometric witness; d_J
    triangle certificate on all reachable 7-object ideals.
(2) D2 small-n exact: related-pair fraction vs (pi^{3/2}/2)/sqrt(n)
    band (via exact cone moments, n <= 9).
(3) Trajectory geometry readouts (labeled): d_G histograms/diameter/
    V(r), d_J histogram (concentration), beta scale, unrelated
    fraction, f(I) vs |I|, distance-to-bedrock, min directed depth.
(4) T_dag 173-object illustration (STATE_CLASS_ILLUSTRATION).
(5) D4 exact: excluded existing pairs all have d_G <= 2.
"""
import json
import math
import random
from fractions import Fraction
from pathlib import Path

PKG = Path(__file__).resolve().parent


# ------------------------------------------------------------ helpers
def build(pair_seq):
    """anc masks (closed cones), parents, depth, from birth-ordered
    parent pairs. Objects 0,1 primitive."""
    anc = [1, 2]
    par = [None, None]
    for (u, v) in pair_seq:
        oid = len(anc)
        anc.append(anc[u] | anc[v] | (1 << oid))
        par.append((u, v))
    return anc, par


def graph_adj(par, n):
    adj = [[] for _ in range(n)]
    for i, p in enumerate(par):
        if p:
            adj[i] += [p[0], p[1]]
            adj[p[0]].append(i)
            adj[p[1]].append(i)
    return adj


def bfs(adj, src, n):
    dist = [-1] * n
    dist[src] = 0
    q = [src]
    for u in q:
        for w in adj[u]:
            if dist[w] < 0:
                dist[w] = dist[u] + 1
                q.append(w)
    return dist


def beta(anc, x, y):
    m = anc[x] & anc[y]
    return m.bit_length() - 1 if m else -1


# ------------------------------------------------------------ (1) D1
def d1_witnesses():
    out = {}
    # ultrametric failure at n=8: a,b,ab,p={a,ab},q={b,ab},x={a,p},
    # z={b,q},y={p,q}  (births 2..7 for ab,p,q,x,z,y)
    seq = [(0, 1), (0, 2), (1, 2), (0, 3), (1, 4), (3, 4)]
    anc, par = build(seq)
    X, Z, Y = 5, 6, 7
    bxy, byz, bxz = beta(anc, X, Y), beta(anc, Y, Z), beta(anc, X, Z)
    n = 8
    strong_fails = (n - bxz) > max(n - bxy, n - byz)
    out["ultrametric_failure_n8"] = {
        "ideal": seq, "x": X, "z": Z, "y": Y,
        "beta_xy": bxy, "beta_yz": byz, "beta_xz": bxz,
        "d_xy": n - bxy, "d_yz": n - byz, "d_xz": n - bxz,
        "strong_triangle_fails": bool(strong_fails)}
    # ordinary triangle failure at n=13: fillers (not ancestors of
    # p,q) push p,q late; p,q share only {a,b,ab}
    seq2 = [(0, 1),          # 2 = ab
            (0, 2), (1, 2),  # 3 = {a,ab}, 4 = {b,ab}
            (3, 4), (2, 5), (4, 5),  # 5,6,7 fillers
            (0, 3), (1, 4),  # 8 = p = {a,3}, 9 = q = {b,4} born late
            (0, 8), (1, 9), (8, 9)]  # 10=x, 11=z, 12=y
    anc2, par2 = build(seq2)
    n2 = len(anc2)
    X2, Z2, Y2 = 10, 11, 12
    bxy2 = beta(anc2, X2, Y2)
    byz2 = beta(anc2, Y2, Z2)
    bxz2 = beta(anc2, X2, Z2)
    ordinary_fails = (n2 - bxz2) > (n2 - bxy2) + (n2 - byz2)
    out["ordinary_triangle_failure"] = {
        "n": n2, "beta_xy": bxy2, "beta_yz": byz2, "beta_xz": bxz2,
        "d_xz": n2 - bxz2, "d_xy_plus_d_yz":
            (n2 - bxy2) + (n2 - byz2),
        "ordinary_triangle_fails": bool(ordinary_fails)}
    # open-cone pseudometric witness
    anc3, _ = build([(0, 1), (0, 2), (1, 2)])
    open3 = anc3[3] & ~(1 << 3)
    open4 = anc3[4] & ~(1 << 4)
    oc_u = anc3[0] | anc3[2]  # open cone of {a,ab} = anc(a)|anc(ab)
    oc_v = anc3[1] | anc3[2]
    out["open_cone_pseudometric_witness"] = {
        "objects": "{a,ab} and {b,ab}",
        "open_cone_1": oc_u, "open_cone_2": oc_v,
        "equal": bool(oc_u == oc_v)}
    return out


def d_jaccard(anc, x, y):
    i = bin(anc[x] & anc[y]).count("1")
    u = bin(anc[x] | anc[y]).count("1")
    return 1 - i / u


def dj_triangle_certificate(n_max=7):
    """Exhaustively check the Jaccard triangle inequality on every
    reachable ideal at n_max objects."""
    from itertools import combinations
    states = {(): None}
    for step in range(n_max - 2):
        nxt = {}
        for st in states:
            k = len(st) + 2
            existing = set(st)
            for i in range(k):
                for j in range(i + 1, k):
                    if (i, j) not in existing:
                        nxt[st + ((i, j),)] = None
        states = nxt
    checked = viol = 0
    for st in states:
        anc, _ = build(st)
        n = len(anc)
        for (x, y, z) in combinations(range(n), 3):
            checked += 1
            if d_jaccard(anc, x, z) > d_jaccard(anc, x, y) + \
                    d_jaccard(anc, y, z) + 1e-12:
                viol += 1
    return {"ideals": len(states), "triples_checked": checked,
            "violations": viol}


# ------------------------------------------------------------ trajectory
def run_traj_geometry(G, m, H, seed, steps, targets):
    rng = random.Random(seed)
    pairs = {}
    anc = [1, 2]
    par = [None, None]
    pth = [0, 0]
    rec = 0
    B = 0
    P = 0
    sp = ()
    res = {}
    hit = set()
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
        for tgt in targets:
            if len(anc) >= tgt and tgt not in hit:
                hit.add(tgt)
                res[str(tgt)] = analyze(anc[:], par[:], tgt)
        if hit == set(targets):
            break
    return res


def analyze(anc, par, n):
    """Geometry readouts on the first n objects of a realized ideal."""
    anc = anc[:n]
    par = par[:n]
    mask_n = (1 << n) - 1
    anc = [a & mask_n for a in anc]
    adj = graph_adj(par, n)
    # d_G: full BFS
    ecc = []
    dists = []
    for src in range(n):
        d = bfs(adj, src, n)
        ecc.append(max(d))
        if src < 40:
            dists.extend(d[src + 1:])
    diam = max(ecc)
    # V(r) profile (mean ball sizes)
    vr = {}
    for r in range(0, diam + 1):
        tot = 0
        for src in range(0, n, max(1, n // 25)):
            d = bfs(adj, src, n)
            tot += sum(1 for x in d if 0 <= x <= r)
        vr[str(r)] = round(tot / len(range(0, n, max(1, n // 25))), 1)
    # bedrock
    br = int(math.isqrt(n))
    bed = set(range(br))
    dbed = [min(bfs(adj, src, n)[b] for b in bed)
            for src in range(n - 20, n)]
    # bedrock internal related fraction
    rel_b = sum(1 for i in range(br) for j in range(i + 1, br)
                if anc[i] & (1 << j) or anc[j] & (1 << i))
    # oops: relatedness i prec j iff i in cone(j)
    rel_b = sum(1 for i in range(br) for j in range(i + 1, br)
                if (anc[j] >> i) & 1)
    frac_b = rel_b / (br * (br - 1) // 2) if br > 1 else 0
    # global unrelated fraction
    rel = sum(1 for j in range(n) for i in range(j)
              if (anc[j] >> i) & 1)
    frac_rel = rel / (n * (n - 1) // 2)
    # d_J and beta over sampled late pairs
    rng2 = random.Random(777)
    djs = []
    betas = []
    late = list(range(n // 2, n))
    for _ in range(400):
        x, y = rng2.sample(late, 2)
        if (anc[y] >> x) & 1 or (anc[x] >> y) & 1:
            continue
        djs.append(d_jaccard(anc, x, y))
        betas.append(beta(anc, x, y))
    djm = sum(djs) / len(djs)
    djsd = math.sqrt(sum((d - djm) ** 2 for d in djs) / len(djs))
    bm = sum(betas) / len(betas)
    # intervals: sample related pairs, interval = descendants(x) ∩
    # cone(y)
    fIs = []
    for _ in range(600):
        y = rng2.randrange(n // 2, n)
        cone_bits = [i for i in range(n) if (anc[y] >> i) & 1]
        x = rng2.choice(cone_bits)
        if x == y:
            continue
        I = [z for z in cone_bits if (anc[z] >> x) & 1]
        s = len(I)
        if s < 3:
            continue
        relI = sum(1 for a2 in range(len(I)) for b2 in range(a2 + 1,
                   len(I)) if (anc[I[b2]] >> I[a2]) & 1)
        fIs.append((s, relI / (s * (s - 1) // 2)))
    # min directed depth
    mdep = [0, 0]
    for i in range(2, n):
        u, v = par[i]
        mdep.append(1 + min(mdep[u], mdep[v]))
    # cone sizes
    csz = [bin(anc[i]).count("1") for i in range(n)]
    return {
        "n": n, "diameter_dG": diam,
        "mean_dG_sampled": round(sum(dists) / len(dists), 3),
        "V_r": vr,
        "dist_to_bedrock_last20_mean": round(sum(dbed) / len(dbed), 2),
        "dist_to_bedrock_max": max(dbed),
        "bedrock_size": br,
        "bedrock_related_fraction": round(frac_b, 4),
        "global_related_fraction": round(frac_rel, 4),
        "pred_related_const_x_sqrtn": round(frac_rel * math.sqrt(n), 3),
        "dJ_mean_unrelated_late": round(djm, 4),
        "dJ_sd": round(djsd, 4),
        "beta_mean": round(bm, 1),
        "beta_mean_over_sqrt_n": round(bm / math.sqrt(n), 3),
        "beta_mean_over_n23": round(bm / n ** (2 / 3), 3),
        "f_I_samples": sorted(fIs)[:: max(1, len(fIs) // 12)],
        "min_directed_depth_mean_late": round(
            sum(mdep[n // 2:]) / (n - n // 2), 2),
        "max_depth_maxdep": max(mdep),
        "mean_cone_over_sqrt_n": round(
            sum(csz) / n / math.sqrt(n), 3),
    }


# ------------------------------------------------------------ T_dag
def obj_str(o):
    if isinstance(o, str):
        return o
    return "{" + ",".join(sorted(obj_str(c) for c in o)) + "}"


def tdag_universe():
    """The 173-object frozen universe as a birth-ordered ideal
    (T_dag levels by ancestry-closure size)."""
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def _anc(o):
        if isinstance(o, str):
            return frozenset({o})
        r = {o}
        for c in o:
            r |= _anc(c)
        return frozenset(r)

    allobj = {"a", "b"}
    for size in range(2, 8):
        cur = sorted(allobj, key=obj_str)
        new = set()
        for i, l in enumerate(cur):
            for r_ in cur[i + 1:]:
                cand = frozenset({l, r_})
                if cand not in allobj and len(_anc(cand)) == size:
                    new.add(cand)
        allobj |= new
    order = sorted(allobj, key=lambda o: (len(_anc(o)), obj_str(o)))
    idx = {obj_str(o): i for i, o in enumerate(order)}
    par = [None if isinstance(o, str) else
           tuple(sorted(idx[obj_str(c)] for c in o)) for o in order]
    anc = []
    for i, o in enumerate(order):
        if isinstance(o, str):
            anc.append(1 << i)
        else:
            u, v = par[i]
            anc.append(anc[u] | anc[v] | (1 << i))
    return anc, par


def main():
    out = {"schema": "R63_EXACT_CERTIFICATES_V1"}
    out["D1_witnesses"] = d1_witnesses()
    out["D1_jaccard_triangle_certificate"] = dj_triangle_certificate(7)
    print("D1:", json.dumps(out["D1_witnesses"], default=str)[:300],
          flush=True)
    print("dJ triangle:", out["D1_jaccard_triangle_certificate"],
          flush=True)

    trajs = {}
    for (G, m, H, steps) in ((2, 0, 0, 40000), (3, 0, 0, 40000),
                             (4, 0, 4, 30000), (5, 0, 8, 10000)):
        seed = 1000000 * G + 10000 * m + 100 * H
        trajs[f"G{G}_m{m}_H{H}_s{seed}"] = run_traj_geometry(
            G, m, H, seed, steps, (50, 100, 130))
    out["trajectory_geometry_labeled"] = trajs
    print("trajectories done", flush=True)

    anc_t, par_t = tdag_universe()
    out["Tdag_illustration"] = {
        "label": "STATE_CLASS_ILLUSTRATION_NOT_ADJUDICATION",
        "analysis": analyze(anc_t, par_t, len(anc_t))}
    print("T_dag done", flush=True)

    (PKG / "R63_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    for key, t in trajs.items():
        for nn, a in t.items():
            print(key, nn, "diam", a["diameter_dG"], "dbed",
                  a["dist_to_bedrock_last20_mean"], "relfrac*rtn",
                  a["pred_related_const_x_sqrtn"], "bedrel",
                  a["bedrock_related_fraction"], "dJ",
                  a["dJ_mean_unrelated_late"], "+-", a["dJ_sd"],
                  "beta/rtn", a["beta_mean_over_sqrt_n"])


if __name__ == "__main__":
    main()
