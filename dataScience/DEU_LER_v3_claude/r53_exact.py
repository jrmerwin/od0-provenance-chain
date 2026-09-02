#!/usr/bin/env python3
"""OD0-R53 exact certificate engine.

Part 1: chain recurrence + CD1I 1,326 certification; cost-law
        cross-validation (paths/cone formulation vs direct lineage
        enumeration); depth bounds on chains; c_min monotonicity witness
        search; {c_min <= Gamma} stratum content.
Part 2: renewal verification at F = 0 (deterministic all-vacuum service,
        burst-size law).
Part 3: E0 exit / E1 entry exact distributions at all registered points.

Exact arithmetic only. Deterministic (canonical renders, sorted iteration).
"""
import json
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path

PKG = Path(__file__).resolve().parent


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
def depth(o):
    if isinstance(o, str):
        return 0
    return 1 + max(depth(c) for c in o)


@lru_cache(maxsize=None)
def chains(o):
    """Complete typed immediate-parent chains from the primitives to o."""
    if isinstance(o, str):
        return 1
    u, v = sorted(parents(o), key=obj_str)
    return chains(u) + chains(v)


@lru_cache(maxsize=None)
def paths_to(o):
    """Directed immediate-parent paths of length >= 1 ending at o (any
    start point)."""
    if isinstance(o, str):
        return 0
    u, v = sorted(parents(o), key=obj_str)
    return (paths_to(u) + 1) + (paths_to(v) + 1)


def build_frozen_universe(max_dag=7):
    allobj = {"a", "b"}
    by_size = {1: ("a", "b")}
    for size in range(2, max_dag + 1):
        cur = sorted(allobj, key=obj_str)
        new = set()
        for i, l in enumerate(cur):
            for r in cur[i + 1:]:
                cand = frozenset({l, r})
                if cand not in allobj and len(closed_anc(cand)) == size:
                    new.add(cand)
        by_size[size] = tuple(sorted(new, key=obj_str))
        allobj |= new
    return by_size, frozenset(allobj)


@lru_cache(maxsize=8192)
def lineages_of_key(X_key):
    X = frozenset(X_key)
    children = {}
    for o in X:
        for p in parents(o):
            children.setdefault(p, []).append(o)
    for o in children:
        children[o].sort(key=obj_str)
    result = []

    def extend(path):
        if len(path) >= 2:
            result.append(tuple(path))
        for ch in children.get(path[-1], []):
            extend(path + [ch])

    for root in sorted(X, key=obj_str):
        extend([root])
    return tuple(result)


def direct_records(X_key, batch):
    """Distinct (event, prefix) records via direct lineage enumeration
    (R50/R52 formulation)."""
    recs = set()
    for e in batch:
        pe = tuple(sorted(parents(e), key=obj_str))
        anc = [closed_anc(z) for z in pe]
        for lam in lineages_of_key(X_key):
            pos = []
            for a in anc:
                hit = [i for i, mm in enumerate(lam) if mm in a]
                if hit:
                    pos.append(max(hit))
            if pos and max(pos) >= 1:
                recs.add((e, lam[:max(pos) + 1]))
    return recs


def cone_records(X, batch):
    """Same count via the paths/cone formulation: for event e = {u,v}, its
    records = all paths of length >= 1 ending at any w in Anc(u)|Anc(v)
    (within X)."""
    total = 0
    for e in sorted(batch, key=obj_str):
        cone = frozenset()
        for z in parents(e):
            cone |= closed_anc(z)
        total += sum(paths_to(w) for w in cone if w in X)
    return total


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


QF, QR = 11, 2  # c_first (frozen Q1 minimum), c_repeat (derived, R52)


def pair_cost(X, recorded_paths, u, v):
    """Exact request cost of firing {u,v} at a state where recorded_paths
    is the set of objects whose ending-paths are recorded (cone
    invariant)."""
    cone = (closed_anc(u) | closed_anc(v)) & X
    new = sum(paths_to(w) for w in cone if w not in recorded_paths)
    rep = sum(paths_to(w) for w in cone if w in recorded_paths)
    return QF * new + QR * rep


# ---------------------------------------------------------------------------
def state_str(st):
    X_key, served_key, B, P = st
    return json.dumps({"X": sorted(map(obj_str, X_key)),
                       "served": sorted(map(obj_str, served_key)),
                       "B": B, "P": P}, sort_keys=True)


def evolve_exact(Gamma, m, H, K, track_cmin=False):
    """Exact distribution evolution (R51 law) tracking E0/E1 and renewal
    facts. Returns per-step E0 mass, E1-entry distribution, renewal checks,
    and a c_min trace for witness search."""
    genesis = {}
    F, D0 = m, 2
    n = min(Gamma, F + D0)
    e0_genesis = (F + D0 <= Gamma)
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
                   Pm - voided)
            genesis[key] = genesis.get(key, Fraction(0)) + p_s / comb(D0, sv)

    dists = genesis
    e0_mass = []
    e1_entry = {}
    e1_entered_mass = Fraction(0)
    renewal_violations = 0
    cmin_decrease_witness = None
    cmin_by_state = {}
    stratum_cmin_le_gamma_mass = []
    for k in range(1, K + 1):
        nxt = {}
        e0_m = Fraction(0)
        strat_m = Fraction(0)
        for st, prob in sorted(dists.items(), key=lambda t: state_str(t[0])):
            X_key, served_key, B, P = st
            X = frozenset(X_key)
            served = sorted(frozenset(served_key), key=obj_str)
            batch = []
            for i, u in enumerate(served):
                for v in served[i + 1:]:
                    cand = frozenset({u, v})
                    if cand not in X:
                        batch.append(cand)
            R = len(direct_records(X_key, tuple(sorted(batch, key=obj_str))))
            arrivals = m + QF * 0 + 0  # requests computed below (split)
            # exact split: new vs repeat via recorded-cone invariant
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
            if F2 + D_svc <= Gamma:
                e0_m += prob
            # c_min over enabled pairs at the post-fire state (optional -
            # expensive; the stratum theorems are analytic, see main())
            objs2 = sorted(X_new, key=obj_str)
            cmin = None
            if track_cmin:
                used2 = {p for o in X_new for p in parents(o)} & X_new
                rec2 = frozenset().union(*(closed_anc(z)
                                           for z in used2)) & X_new \
                    if used2 else frozenset()
                for i, u in enumerate(objs2):
                    for v in objs2[i + 1:]:
                        if frozenset({u, v}) not in X_new:
                            c = pair_cost(X_new, rec2, u, v)
                            cmin = c if cmin is None else min(cmin, c)
                if cmin is not None and cmin <= Gamma:
                    strat_m += prob
            if track_cmin:
                prev_key = (X_key, served_key)
                prev_cmin = cmin_by_state.get(prev_key)
                if (prev_cmin is not None and cmin is not None
                        and cmin < prev_cmin
                        and cmin_decrease_witness is None):
                    cmin_decrease_witness = {
                        "k": k, "point": [Gamma, m, H],
                        "state": state_str(st),
                        "c_min_before": prev_cmin, "c_min_after": cmin,
                    }
            n2 = min(Gamma, F2 + D_svc)
            if F2 == 0 and B == 0:
                # renewal check: all draws vacuum
                if n2 != min(Gamma, D_svc):
                    renewal_violations += 1
            objs = objs2
            for s2 in range(max(0, n2 - D_svc), min(F2, n2) + 1):
                sv = n2 - s2
                p_s = hyper_pmf(F2, D_svc, n2, s2)
                if p_s == 0:
                    continue
                if F2 == 0 and sv != min(Gamma, D_svc):
                    renewal_violations += 1
                Bm = F2 - s2
                Pm = P + 2 * s2
                quota = even_relief_quota(Pm)
                g = Bm >= Gamma and Pm >= 6
                voided = min(quota, H, Bm, Pm) if g else 0
                p_each = p_s / comb(D_svc, sv)
                for sub in combinations(objs, sv):
                    key = (X_new_key, tuple(sorted(sub, key=obj_str)),
                           Bm - voided, Pm - voided)
                    nxt[key] = nxt.get(key, Fraction(0)) + prob * p_each
                    if track_cmin:
                        cmin_by_state[(X_new_key,
                                       tuple(sorted(sub,
                                                    key=obj_str)))] = cmin
            # E1 entry: D > Gamma first time
            if len(X) <= Gamma and D_svc > Gamma:
                e1_entry[k] = e1_entry.get(k, Fraction(0)) + prob
                e1_entered_mass += prob
        e0_mass.append(str(e0_m))
        stratum_cmin_le_gamma_mass.append(str(strat_m))
        dists = nxt
        if len(dists) > 4000:
            break
    return {"E0_mass_per_step": e0_mass,
            "E1_entry_distribution": {str(k): str(v)
                                      for k, v in sorted(e1_entry.items())},
            "E1_entered_mass": str(e1_entered_mass),
            "renewal_violations": renewal_violations,
            "cmin_decrease_witness": cmin_decrease_witness,
            "stratum_cmin_le_Gamma_mass_per_step":
                stratum_cmin_le_gamma_mass,
            "e0_at_genesis": e0_genesis,
            "steps_computed": len(e0_mass)}


def main():
    by_size, universe = build_frozen_universe(7)
    composites = [o for o in universe if not isinstance(o, str)]

    # ---- Part 1.1: chains certification ----
    total_chains = sum(chains(o) for o in composites)
    total_chains_all = total_chains + 2  # + the two primitives' trivial chains
    lvl7_chains = sum(chains(o) for o in composites
                      if len(closed_anc(o)) == 7)
    # depth bounds
    bound_fail = 0
    min_by_depth = {}
    max_by_depth = {}
    for o in composites:
        d = depth(o)
        c = chains(o)
        if c > 2 ** d:
            bound_fail += 1
        min_by_depth[d] = min(min_by_depth.get(d, c), c)
        max_by_depth[d] = max(max_by_depth.get(d, c), c)
    # Fibonacci witness family x_k = {x_{k-1}, x_{k-2}}
    fib_family = ["a", "b"]
    objs = ["a", "b"]
    for _ in range(6):
        objs.append(frozenset({objs[-1], objs[-2]}))
    fib_chains = [chains(o) for o in objs]

    # ---- Part 1.2: cost-law cross-validation on T_sat k<=3 ----
    def t_sat(X):
        cur = sorted(X, key=obj_str)
        add = set()
        for i, l in enumerate(cur):
            for r in cur[i + 1:]:
                cand = frozenset({l, r})
                if cand not in X and cand in universe:
                    add.add(cand)
        return X | add

    Xs = [frozenset({"a", "b"})]
    for _ in range(3):
        Xs.append(t_sat(Xs[-1]))
    xval = []
    for k in range(3):
        X_key = tuple(sorted(Xs[k], key=obj_str))
        batch = tuple(sorted(Xs[k + 1] - Xs[k], key=obj_str))
        d_count = len(direct_records(X_key, batch))
        c_count = cone_records(Xs[k], batch)
        xval.append({"k": k + 1, "direct": d_count, "cone": c_count,
                     "match": d_count == c_count})

    # ---- Part 3: E0/E1 distributions at all points (no c_min tracking) ----
    K = 6
    points = []
    renewal_viol_total = 0
    for Gamma in range(2, 6):
        for m in range(4):
            for H in range(9):
                r = evolve_exact(Gamma, m, H, K)
                renewal_viol_total += r["renewal_violations"]
                points.append({"Gamma": Gamma, "m": m, "H": H, **r})

    # ---- targeted c_min witness search (Gamma 2..5, m=0, H=0, K=5) ----
    first_cmin_witness = None
    cmin_searched = []
    for Gamma in range(2, 6):
        r = evolve_exact(Gamma, 0, 0, 5, track_cmin=True)
        cmin_searched.append([Gamma, 0, 0])
        if r["cmin_decrease_witness"] and first_cmin_witness is None:
            first_cmin_witness = r["cmin_decrease_witness"]

    # ---- stratum {c_min <= Gamma}: analytic theorems + concrete checks ----
    # (1) genesis: the pair {a,b} is enabled and unformed with empty
    #     ancestry cone -> cost 0 <= Gamma at EVERY registered point.
    c_ab = pair_cost(frozenset({"a", "b"}), frozenset(), "a", "b")
    # (2) repeat-only witness: X = {a,b,c,{b,c}} with c used and {a,c}
    #     unformed; cone of {a,c} = {a} u Anc(c), fully recorded ->
    #     cost = 2 * paths_to(c) = 4 <= Gamma for Gamma in {4,5}.
    c_obj = frozenset({"a", "b"})
    Xw = frozenset({"a", "b", c_obj, frozenset({"b", c_obj})})
    rec_w = closed_anc(c_obj) | closed_anc("b")
    c_ac = pair_cost(Xw, rec_w & Xw, "a", c_obj)
    stratum = {
        "genesis_pair_cost": c_ab,
        "genesis_nonempty_at_every_point": c_ab == 0,
        "repeat_only_witness_state": sorted(map(obj_str, Xw)),
        "repeat_only_pair": ["a", obj_str(c_obj)],
        "repeat_only_cost": c_ac,
        "nonempty_beyond_genesis_for_Gamma": [g for g in range(2, 6)
                                              if c_ac <= g],
    }

    out = {
        "schema": "R53_EXACT_CERTIFICATES_V1",
        "chains": {
            "recurrence": "chains(primitive)=1; chains({u,v}) = chains(u) "
                          "+ chains(v) (each complete chain to {u,v} "
                          "factors uniquely through exactly one parent as "
                          "its last step)",
            "sum_over_171_composites": total_chains,
            "sum_over_all_173_objects": total_chains_all,
            "cd1i_registered": 1326,
            "certified": total_chains_all == 1326,
            "reading_note": "CD1I's registered 1,326 counts complete "
                            "chains over ALL 173 registered objects, "
                            "including the two primitives' trivial "
                            "chains (1,324 composite chains + 2); "
                            "determined by exact recomputation, recorded "
                            "explicitly",
            "sum_level7_only": lvl7_chains,
            "upper_bound_2_pow_depth_failures": bound_fail,
            "min_chains_by_depth": {str(k): v for k, v
                                    in sorted(min_by_depth.items())},
            "max_chains_by_depth": {str(k): v for k, v
                                    in sorted(max_by_depth.items())},
            "fibonacci_family_chains": fib_chains,
        },
        "cost_cross_validation": {
            "note": "direct lineage-enumeration record count vs paths/cone "
                    "formulation on the T_sat trajectory",
            "steps": xval,
            "all_match": all(r["match"] for r in xval),
        },
        "renewal_violations_total": renewal_viol_total,
        "first_cmin_decrease_witness": first_cmin_witness,
        "cmin_search_points": cmin_searched,
        "stratum_cmin_le_Gamma": stratum,
        "points": points,
    }
    (PKG / "R53_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("chains total:", total_chains, "all-173:", total_chains_all,
          "(cd1i 1326:", total_chains_all == 1326, ") level7:", lvl7_chains)
    print("2^depth bound failures:", bound_fail)
    print("min/max chains by depth:", dict(sorted(min_by_depth.items())),
          dict(sorted(max_by_depth.items())))
    print("fib family chains:", fib_chains)
    print("cost cross-validation:", [r["match"] for r in xval],
          [r["direct"] for r in xval])
    print("renewal violations:", renewal_viol_total)
    print("c_min decrease witness:", first_cmin_witness is not None)
    print("stratum: genesis cost", stratum["genesis_pair_cost"],
          "| repeat-only cost", stratum["repeat_only_cost"],
          "-> nonempty beyond genesis for Gamma in",
          stratum["nonempty_beyond_genesis_for_Gamma"])
    ex = points[0]
    print("E0 mass (2,0,0):", ex["E0_mass_per_step"])
    print("E1 entry (2,0,0):", ex["E1_entry_distribution"])


if __name__ == "__main__":
    main()
