#!/usr/bin/env python3
"""OD0-R56 Part 4 (M5) engine.

Exact: K<=4 distribution evolutions at all 144 registered points tracking
first appearance of record TYPE CLASSES (single first-use, sibling-pair,
sibling-group >= 3, repeat-use) - P(type appeared by k) exact.

Sampled (labeled, seeded, 3 trajectories x 10^4 steps per point): first
appearance steps per type class, max sibling group, max per-object reuse
count (carrier-chain length proxy), reachable type counts by Gamma.
"""
import json
import random
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path

PKG = Path(__file__).resolve().parent
QF, QR = 11, 2


def obj_str(o):
    if isinstance(o, str):
        return o
    return "{" + ",".join(sorted(obj_str(c) for c in o)) + "}"


def parents(o):
    return frozenset() if isinstance(o, str) else o


@lru_cache(maxsize=None)
def closed_anc(o):
    if isinstance(o, str):
        return frozenset({o})
    r = {o}
    for c in o:
        r |= closed_anc(c)
    return frozenset(r)


@lru_cache(maxsize=None)
def paths_to(o):
    if isinstance(o, str):
        return 0
    u, v = sorted(parents(o), key=obj_str)
    return (paths_to(u) + 1) + (paths_to(v) + 1)


def hyper_pmf(F, D, n, s):
    if min(F, D, n, s) < 0 or n > F + D:
        return Fraction(0)
    v = n - s
    if s > F or v < 0 or v > D:
        return Fraction(0)
    return Fraction(comb(F, s) * comb(D, v), comb(F + D, n))


def even_relief_quota(population):
    base = max(1, population // 6)
    return 2 * ((base + 1) // 2)


TYPES = ("SINGLE_FIRST_USE", "SIBLING_PAIR", "SIBLING_GROUP_GE3",
         "REPEAT_USE")


def batch_types(X, batch):
    """Type flags fired by this batch on pre-fire state X."""
    flags = set()
    par_use = {}
    for e in batch:
        for z in parents(e):
            par_use[z] = par_use.get(z, 0) + 1
    if par_use:
        mx = max(par_use.values())
        if mx == 2:
            flags.add("SIBLING_PAIR")
        elif mx >= 3:
            flags.add("SIBLING_GROUP_GE3")
            flags.add("SIBLING_PAIR")
    used = {p for o in X for p in parents(o)} & X
    recorded = frozenset().union(*(closed_anc(z) for z in used)) & X \
        if used else frozenset()
    for e in batch:
        cone = (frozenset().union(*(closed_anc(z)
                                    for z in parents(e)))) & X
        comp_cone = {w for w in cone if not isinstance(w, str)}
        if comp_cone - recorded:
            flags.add("SINGLE_FIRST_USE")
        if comp_cone & recorded:
            flags.add("REPEAT_USE")
    return flags


def evolve(Gamma, m, H, K):
    genesis = {}
    F, D0 = m, 2
    n = min(Gamma, F + D0)
    for s in range(max(0, n - D0), min(F, n) + 1):
        sv = n - s
        p_s = hyper_pmf(F, D0, n, s)
        if p_s == 0:
            continue
        Bm, Pm = F - s, 2 * s
        quota = even_relief_quota(Pm)
        g = Bm >= Gamma and Pm >= 6
        voided = min(quota, H, Bm, Pm) if g else 0
        for served in combinations(("a", "b"), sv):
            key = (("a", "b"), tuple(sorted(served)), Bm - voided,
                   Pm - voided, frozenset())
            genesis[key] = genesis.get(key, Fraction(0)) + p_s / comb(D0, sv)

    dists = genesis
    appeared = {t: [] for t in TYPES}
    for k in range(1, K + 1):
        nxt = {}
        mass = {t: Fraction(0) for t in TYPES}
        for st, prob in sorted(dists.items(), key=lambda t: str(t[0])):
            X_key, served_key, B, P, seen = st
            X = frozenset(X_key)
            served = sorted(frozenset(served_key), key=obj_str)
            batch = []
            for i, u in enumerate(served):
                for v in served[i + 1:]:
                    cand = frozenset({u, v})
                    if cand not in X:
                        batch.append(cand)
            seen2 = seen | frozenset(batch_types(X, batch))
            used = {p for o in X for p in parents(o)} & X
            recorded = frozenset().union(*(closed_anc(z) for z in used)) & X \
                if used else frozenset()
            reqs = 0
            rec_now = set(recorded)
            for e in sorted(batch, key=obj_str):
                cone = (frozenset().union(*(closed_anc(z)
                                            for z in parents(e)))) & X
                new = sum(paths_to(w) for w in cone if w not in rec_now)
                rep = sum(paths_to(w) for w in cone if w in rec_now)
                reqs += QF * new + QR * rep
                rec_now |= cone
            F2 = B + m + reqs
            X_new = X | set(batch)
            X_new_key = tuple(sorted(X_new, key=obj_str))
            D_svc = len(X_new)
            n2 = min(Gamma, F2 + D_svc)
            objs = sorted(X_new, key=obj_str)
            for s2 in range(max(0, n2 - D_svc), min(F2, n2) + 1):
                sv = n2 - s2
                p_s = hyper_pmf(F2, D_svc, n2, s2)
                if p_s == 0:
                    continue
                Bm = F2 - s2
                Pm = P + 2 * s2
                quota = even_relief_quota(Pm)
                g = Bm >= Gamma and Pm >= 6
                voided = min(quota, H, Bm, Pm) if g else 0
                p_each = p_s / comb(D_svc, sv)
                for sub in combinations(objs, sv):
                    key = (X_new_key, tuple(sorted(sub, key=obj_str)),
                           Bm - voided, Pm - voided, seen2)
                    nxt[key] = nxt.get(key, Fraction(0)) + prob * p_each
            for t in TYPES:
                if t in seen2:
                    mass[t] += prob
        for t in TYPES:
            appeared[t].append(str(mass[t]))
        dists = nxt
        if len(dists) > 3000:
            break
    return appeared


def run_sampled(Gamma, m, H, seed, steps=10000):
    rng = random.Random(seed)
    anc = [1, 2]
    paths_arr = [0, 0]
    pairs = {}
    parent_uses = [0, 0]
    recorded = 0
    B = 0
    P = 0
    served_prev = ()
    first = {}
    max_group = 0
    for k in range(1, steps + 1):
        sp = sorted(served_prev)
        batch = [(sp[i], sp[j]) for i in range(len(sp))
                 for j in range(i + 1, len(sp)) if (sp[i], sp[j]) not in pairs]
        par_use = {}
        new_rec = rep_rec = 0
        for (u, v) in batch:
            par_use[u] = par_use.get(u, 0) + 1
            par_use[v] = par_use.get(v, 0) + 1
        if par_use:
            mx = max(par_use.values())
            max_group = max(max_group, mx)
            if mx >= 2:
                first.setdefault("SIBLING_PAIR", k)
            if mx >= 3:
                first.setdefault("SIBLING_GROUP_GE3", k)
        for (u, v) in batch:
            oid = len(anc)
            anc.append(anc[u] | anc[v] | (1 << oid))
            paths_arr.append((paths_arr[u] + 1) + (paths_arr[v] + 1))
            parent_uses[u] += 1
            parent_uses[v] += 1
            parent_uses.append(0)
            pairs[(u, v)] = oid
            cone = anc[u] | anc[v]
            comp_cone_new = cone & ~recorded & ~3  # exclude primitive bits
            comp_cone_rep = cone & recorded & ~3
            if comp_cone_new:
                first.setdefault("SINGLE_FIRST_USE", k)
            if comp_cone_rep:
                first.setdefault("REPEAT_USE", k)
            mask = cone & ~recorded
            while mask:
                low = mask & -mask
                new_rec += paths_arr[low.bit_length() - 1]
                mask ^= low
            mask = cone & recorded
            while mask:
                low = mask & -mask
                rep_rec += paths_arr[low.bit_length() - 1]
                mask ^= low
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
    max_reuse = max(parent_uses) if parent_uses else 0
    return first, max_group, max_reuse


def main():
    exact = []
    for Gamma in range(2, 6):
        for m in range(4):
            for H in range(9):
                app = evolve(Gamma, m, H, 4)
                exact.append({"Gamma": Gamma, "m": m, "H": H,
                              "P_type_by_k": app})
    sampled = []
    for Gamma in range(2, 6):
        for m in range(4):
            for H in range(9):
                firsts = {t: [] for t in TYPES}
                groups = []
                reuses = []
                for t in range(3):
                    seed = 1000000 * Gamma + 10000 * m + 100 * H + t
                    first, mg, mr = run_sampled(Gamma, m, H, seed)
                    for ty in TYPES:
                        firsts[ty].append(first.get(ty))
                    groups.append(mg)
                    reuses.append(mr)
                sampled.append({
                    "Gamma": Gamma, "m": m, "H": H,
                    "first_appearance": {ty: firsts[ty] for ty in TYPES},
                    "max_sibling_group": max(groups),
                    "max_parent_reuse": max(reuses),
                })
    by_gamma = {}
    for row in sampled:
        g = row["Gamma"]
        agg = by_gamma.setdefault(g, {ty: 0 for ty in TYPES})
        for ty in TYPES:
            if any(v is not None for v in row["first_appearance"][ty]):
                agg[ty] += 1
    out = {
        "schema": "R56_M5_ENGINE_V1",
        "exact_type_first_appearance": exact,
        "sampled": sampled,
        "reachable_type_points_by_gamma": {str(g): v
                                           for g, v in by_gamma.items()},
    }
    (PKG / "R56_M5_ENGINE_RAW.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("reachable-type point counts by Gamma:",
          json.dumps({str(g): v for g, v in sorted(by_gamma.items())}))
    ex = exact[0]
    print("exact (2,0,0) P(type by k<=4):",
          {t: ex["P_type_by_k"][t] for t in TYPES})
    mg = max(r["max_sibling_group"] for r in sampled)
    mr = max(r["max_parent_reuse"] for r in sampled)
    print("max sibling group observed:", mg, "| max parent reuse:", mr)


if __name__ == "__main__":
    main()
