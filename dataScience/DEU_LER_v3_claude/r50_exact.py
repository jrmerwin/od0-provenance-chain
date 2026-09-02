#!/usr/bin/env python3
"""OD0-R50 exact certificate engine.

Computes, with exact arithmetic only:
  Part 1 - family identification (T_sat = depth filtration, T_dag = dag_size
           filtration), smallest depth/dag_size divergent object, record-poset
           invariance check, cumulative-ledger divergence witness, mark-support
           envelope witness, coherence-lifetime verification.
  Part 3 - growth (closed recurrence + direct verification), exact record-use
           counts k<=4 and batch lower bounds k<=6, full ledger scan over the
           registered (Gamma, D, m, H) domain for both members, k<=K_max=3.
  Part 5 - registry identification against the frozen CD0 native universe.

No frozen file is modified (bytecode writing disabled before importing the
frozen CD0 module).
"""
import json
import sys
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path

sys.dont_write_bytecode = True

PKG = Path(__file__).resolve().parent
CD0_SRC = (PKG.parent / "DEU_LER_v0_1_Codex_Package" / "deu_ler_v0_1"
           / "deu_unified_equations_v1_0" / "deu_combinatorial_descent_cd0")

# ---------------------------------------------------------------------------
# Constructor (same frozen rule as r49_exact.py)
# ---------------------------------------------------------------------------
from functools import lru_cache


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


def dag_size(o):
    return len(closed_anc(o))


@lru_cache(maxsize=None)
def depth(o):
    if isinstance(o, str):
        return 0
    return 1 + max(depth(c) for c in o)


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


def enabled(X, universe):
    return frozenset(o for o in universe if o not in X and parents(o) <= X)


def t_sat(X, universe):
    return X | enabled(X, universe)


def t_dag(X, universe):
    en = enabled(X, universe)
    if not en:
        return X
    m = min(dag_size(o) for o in en)
    return X | {o for o in en if dag_size(o) == m}


def unbounded_step_sat(X):
    """T_sat in the unbounded universe: X + every absent pair of distinct
    members."""
    add = set()
    cur = sorted(X, key=obj_str)
    for i, l in enumerate(cur):
        for r in cur[i + 1:]:
            cand = frozenset({l, r})
            if cand not in X:
                add.add(cand)
    return frozenset(X | add)


def lineages_of(X, max_depth=None):
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
        if max_depth is not None and len(path) - 1 >= max_depth:
            return
        for ch in children.get(path[-1], []):
            extend(path + [ch])

    for root in sorted(X, key=obj_str):
        extend([root])
    return result


def record_uses(X, batch):
    """Distinct record events under the frozen RO-D rule.

    A record's identity is (using event e, recorded prefix path lam[0..ell]):
    the A10 write copies pi_ell of the lineage word, and every suffix
    extension of the lineage shares that prefix, so uses reaching the same
    ancestor position through extensions of one path are ONE record. The
    recorded prefix path lies inside closed_anc(z) for the touching parent z,
    hence is formed before e under every ancestry-compatible quotient.
    Returns {(e, prefix_path): ell} with ell >= 1.
    """
    recs = {}
    lins = lineages_of(X)
    for lam in lins:
        for e in batch:
            pos = []
            for z in sorted(parents(e), key=obj_str):
                anc = closed_anc(z)
                hit = [i for i, m in enumerate(lam) if m in anc]
                if hit:
                    pos.append(max(hit))
            if pos and max(pos) >= 1:
                ell = max(pos)
                recs[(e, lam[:ell + 1])] = ell
    return recs


# ---------------------------------------------------------------------------
# Frozen ledger kernel (reimplemented verbatim from UEQ0 src/ledger.py:37-83)
# ---------------------------------------------------------------------------

def even_relief_quota(population):
    base = max(1, population // 6)
    return 2 * ((base + 1) // 2)


def hyper_pmf(F, D, n, s):
    if min(F, D, n, s) < 0 or n > F + D:
        return Fraction(0)
    v = n - s
    if s > F or v < 0 or v > D:
        return Fraction(0)
    return Fraction(comb(F, s) * comb(D, v), comb(F + D, n))


def ledger_step(state, chronic, render):
    """state = (B, D, Gamma, P, H) -> list of ((next_state, sF, sV), prob)."""
    B, D, G, P, H = state
    arrivals = chronic + render
    F = B + arrivals
    n = min(G, F + D)
    rows = []
    for sF in range(max(0, n - D), min(F, n) + 1):
        sV = n - sF
        Bm = F - sF
        Pm = P + 2 * sF
        quota = even_relief_quota(Pm)
        gate = Bm >= G and Pm >= 6
        voided = min(quota, H, Bm, Pm) if gate else 0
        nxt = (Bm - voided, D, G, Pm - voided, H)
        rows.append(((nxt, sF, sV), hyper_pmf(F, D, n, sF)))
    assert sum(p for _, p in rows) == 1
    return rows


# ---------------------------------------------------------------------------
def main():
    by_size, universe = build_frozen_universe(7)

    # ---------------- Part 1: family identification -----------------------
    # T_sat formation step = depth: build unbounded T_sat trajectory to k=4
    # and check step(y) = depth(y) for every object formed.
    X = frozenset({"a", "b"})
    sat_states = [X]
    for _ in range(4):
        X = unbounded_step_sat(X)
        sat_states.append(X)
    sat_step_eq_depth = True
    for k in range(1, 5):
        for o in sat_states[k] - sat_states[k - 1]:
            if depth(o) != k:
                sat_step_eq_depth = False
    # T_dag formation step = dag_size - 2 within the frozen universe
    Xd = frozenset({"a", "b"})
    dag_states = [Xd]
    for _ in range(5):
        Xd = t_dag(Xd, universe)
        dag_states.append(Xd)
    dag_step_eq_size = True
    for k in range(1, 6):
        for o in dag_states[k] - dag_states[k - 1]:
            if dag_size(o) - 2 != k:
                dag_step_eq_size = False

    # smallest object with depth quotient != dag_size quotient
    # (compare q_sat = depth vs q_dag = dag_size - 2 on all frozen objects)
    divergent = sorted(
        (o for o in universe if not isinstance(o, str)
         and depth(o) != dag_size(o) - 2),
        key=lambda o: (dag_size(o), obj_str(o)))
    smallest_div = {
        "object": obj_str(divergent[0]),
        "depth": depth(divergent[0]),
        "dag_size": dag_size(divergent[0]),
        "q_sat": depth(divergent[0]),
        "q_dag": dag_size(divergent[0]) - 2,
    } if divergent else None

    # record-poset invariance: events present in both k<=3 trajectories carry
    # identical (lineage, ell) record sets computed from ancestry only
    sat3 = [frozenset({"a", "b"})]
    for _ in range(3):
        sat3.append(t_sat(sat3[-1], universe))
    rec_sat = {}
    for k in range(3):
        for (e, pref), ell in record_uses(sat3[k], sorted(
                sat3[k + 1] - sat3[k], key=obj_str)).items():
            rec_sat.setdefault(e, set()).add((pref, ell))
    rec_dag = {}
    for k in range(5):
        for (e, pref), ell in record_uses(dag_states[k], sorted(
                dag_states[k + 1] - dag_states[k], key=obj_str)).items():
            rec_dag.setdefault(e, set()).add((pref, ell))
    common = set(rec_sat) & set(rec_dag)
    poset_invariant = all(rec_sat[e] == rec_dag[e] for e in common)

    # coherence lifetime <= 1 check: every object formed at step k is used
    # (as a parent of some fired event) at step k+1, for k+1 within range
    def lifetime_ok(states):
        ok = True
        for k in range(1, len(states) - 1):
            formed = states[k] - states[k - 1]
            batch_next = states[k + 1] - states[k]
            for y in formed:
                if not any(y in parents(z) for z in batch_next):
                    ok = False
        return ok

    lifetime_sat = lifetime_ok(sat3 + [t_sat(sat3[-1], universe)])
    lifetime_dag = lifetime_ok(dag_states)
    # frozen-cap boundary: objects never used within the frozen universe
    complete = dag_states[5]
    never_used = [o for o in complete
                  if not isinstance(o, str)
                  and not any(o in parents(z) for z in complete)]

    # cumulative-ledger divergence witness (layer 6): same two unit requests,
    # quotient A pools them at step 1; quotient B splits across steps 1,2.
    # Ledger point (B=0, D=1, Gamma=1, P=0, H=0), m=0. Horizon: 2 steps.
    def run_paths(state, injections):
        dists = {(state, 0, 0): Fraction(1)}  # (state, totF, totV) -> prob
        for c in injections:
            nxt = {}
            for (st, tf, tv), p in dists.items():
                for (st2, sF, sV), q in ledger_step(st, 0, c):
                    key = (st2, tf + sF, tv + sV)
                    nxt[key] = nxt.get(key, Fraction(0)) + p * q
            dists = nxt
        return dists

    lp = (0, 1, 1, 0, 0)
    distA = run_paths(lp, [2, 0])
    distB = run_paths(lp, [1, 1])

    def marg_tf(d):
        m = {}
        for (st, tf, tv), p in d.items():
            m[tf] = m.get(tf, Fraction(0)) + p
        return {str(k): str(v) for k, v in sorted(m.items())}

    cum_witness = {
        "ledger_point": "B=0,D=1,Gamma=1,P=0,H=0,m=0",
        "quotient_A_injections": [2, 0],
        "quotient_B_injections": [1, 1],
        "total_served_forced_A": marg_tf(distA),
        "total_served_forced_B": marg_tf(distB),
        "distributions_differ": marg_tf(distA) != marg_tf(distB),
    }

    # mark-support envelope witness (layer 7): achievable cumulative
    # (served-forced count) SUPPORT over the horizon
    suppA = sorted({tf for (st, tf, tv) in distA})
    suppB = sorted({tf for (st, tf, tv) in distB})
    support_witness = {
        "achievable_total_served_forced_A": suppA,
        "achievable_total_served_forced_B": suppB,
        "supports_equal": suppA == suppB,
    }

    # ---------------- Part 3: growth, loads, ledger scan --------------------
    # growth closed recurrence for T_sat: |X_{k+1}| = C(|X_k|,2) + 2
    sizes_sat = [2]
    for _ in range(6):
        n = sizes_sat[-1]
        sizes_sat.append(n * (n - 1) // 2 + 2)
    # verify against direct unbounded computation k<=4
    growth_verified = all(len(sat_states[k]) == sizes_sat[k]
                          for k in range(5))

    # T_dag growth: level-8 count = pairs {u,v} from O_<=7 with |union|=7
    o7 = sorted(universe, key=obj_str)
    lvl8 = 0
    for i, u in enumerate(o7):
        au = closed_anc(u)
        for v in o7[i + 1:]:
            if len(au | closed_anc(v)) == 7:
                lvl8 += 1
    sizes_dag = [2, 3, 5, 11, 36, 173, 173 + lvl8]
    en_dag = [sizes_dag[k + 1] - sizes_dag[k] for k in range(6)]
    en_sat = [sizes_sat[k + 1] - sizes_sat[k] for k in range(6)]

    # exact record-use counts (ell>=1) k<=4 for both members
    def use_counts(states, upto):
        out = []
        for k in range(min(upto, len(states) - 1)):
            out.append(len(record_uses(states[k], sorted(
                states[k + 1] - states[k], key=obj_str))))
        return out

    sat4 = [frozenset({"a", "b"})]
    for _ in range(4):
        sat4.append(t_sat(sat4[-1], universe))
    U_sat = use_counts(sat4, 4)          # steps 1..4
    U_dag = use_counts(dag_states, 5)    # steps 1..5
    QMIN = 11  # frozen Q1 per-record request minimum (package Sec 6.2)
    # lower bounds: exact 11*U_k where U_k computed; 11*|batch_k| beyond
    F_lb_sat = [QMIN * u for u in U_sat] + [QMIN * en_sat[4], QMIN * en_sat[5]]
    F_lb_dag = [QMIN * u for u in U_dag] + [QMIN * en_dag[5]]

    # ledger scan: registered domain Gamma,D in 0..5 (service.py:81),
    # m in 0..3 (service.py:81), H in 0..8 (population_relief.py:36).
    # Genesis B=0, P=0 (Lambda_0 undeclared -> scan; nothing singled out).
    # Load injection per step: C_k = 11 * U_k (exact lower-bound load,
    # identical for both members at k<=2; divergence at k=3 noted).
    K = 3
    inj_sat = [QMIN * U_sat[k] for k in range(K)]
    inj_dag = [QMIN * U_dag[k] for k in range(K)]
    scan = []
    for G, D, m, H in product(range(6), range(6), range(4), range(9)):
        row = {"Gamma": G, "D": D, "m": m, "H": H}
        for name, inj in (("T_sat", inj_sat), ("T_dag", inj_dag)):
            dists = {(0, D, G, 0, H): Fraction(1)}
            traj = []
            Fk_list = []
            sat_k = None
            for k in range(K):
                C = inj[k]
                # pool F_k is deterministic given backlog distribution;
                # track P(S^V=0), backlog range, lapse support exactly
                nxt = {}
                p_sv0 = Fraction(0)
                pool_min = None
                pool_max = None
                lapse2 = set()
                for st, p in dists.items():
                    F = st[0] + m + C
                    pool_min = F if pool_min is None else min(pool_min, F)
                    pool_max = F if pool_max is None else max(pool_max, F)
                    for (st2, sF, sV), q in ledger_step(st, m, C):
                        nxt[st2] = nxt.get(st2, Fraction(0)) + p * q
                        if sV == 0:
                            p_sv0 += p * q
                        if D > 0:
                            lapse2.add(Fraction(sV, D))
                dists = nxt
                Fk_list.append([pool_min, pool_max])
                if sat_k is None and pool_min > G:
                    sat_k = k + 1
                blo = min(s[0] for s in dists)
                bhi = max(s[0] for s in dists)
                traj.append({
                    "k": k + 1, "pool_range": [pool_min, pool_max],
                    "P_SV0": str(p_sv0), "backlog_range": [blo, bhi],
                    "lapse_sq_support": sorted(str(x) for x in lapse2),
                })
            row[name] = {"smallest_k_pool_exceeds_Gamma": sat_k,
                         "trajectory": traj}
        scan.append(row)
    kappa = max(r[nm]["smallest_k_pool_exceeds_Gamma"]
                for r in scan for nm in ("T_sat", "T_dag"))
    all_saturate = all(r[nm]["smallest_k_pool_exceeds_Gamma"] is not None
                       for r in scan for nm in ("T_sat", "T_dag"))

    # ---------------- Part 5: registry identification ----------------------
    sys.path.insert(0, str(CD0_SRC))
    from src.native import build_universe as cd0_build  # frozen, read-only
    cd0_uni = cd0_build(7)
    cd0_set = sorted(obj_str(o) if isinstance(o, str) else
                     cd0_canon(o) for o in cd0_uni.objects)
    ours = sorted(obj_str(o) for o in dag_states[5])
    registry_equal = cd0_set == ours
    cd0_level7 = sorted(cd0_canon(o) for o in cd0_uni.level7)
    ours_l7 = sorted(obj_str(o) for o in dag_states[5]
                     if dag_size(o) == 7)
    shell_equal = cd0_level7 == ours_l7

    out = {
        "schema": "R50_EXACT_CERTIFICATES_V1",
        "part1": {
            "t_sat_step_equals_depth_k_le_4": sat_step_eq_depth,
            "t_dag_step_equals_dagsize_minus_2_k_le_5": dag_step_eq_size,
            "smallest_depth_vs_dagsize_divergent_object": smallest_div,
            "divergent_objects_in_frozen_universe": len(divergent),
            "record_poset_invariant_on_common_events": poset_invariant,
            "common_events_checked": len(common),
            "lifetime_le_1_sat_k_le_3": lifetime_sat,
            "lifetime_le_1_dag_k_le_4": lifetime_dag,
            "frozen_cap_never_used_objects": len(never_used),
            "cumulative_ledger_witness": cum_witness,
            "mark_support_witness": support_witness,
        },
        "part3": {
            "sizes_sat_k0_6": sizes_sat,
            "en_sat_k0_5": en_sat,
            "growth_recurrence_verified_k_le_4": growth_verified,
            "level8_count": lvl8,
            "sizes_dag_k0_6": sizes_dag,
            "en_dag_k0_5": en_dag,
            "record_uses_sat_steps1_4": U_sat,
            "record_uses_dag_steps1_5": U_dag,
            "F_lower_bounds_sat_steps1_6": F_lb_sat,
            "F_lower_bounds_dag_steps1_6": F_lb_dag,
            "scan_domain": "Gamma 0..5 x D 0..5 x m 0..3 x H 0..8 "
                           "(registered; service.py:81, "
                           "population_relief.py:36); genesis B=0, P=0",
            "scan_points": len(scan),
            "kappa": kappa,
            "all_registered_points_saturate": all_saturate,
            "scan": scan,
        },
        "part5": {
            "t_dag5_objects": len(ours),
            "cd0_registered_objects": len(cd0_set),
            "exact_object_set_equality": registry_equal,
            "level7_shell_equality": shell_equal,
            "level7_count": len(ours_l7),
        },
    }
    (PKG / "R50_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("family id:", sat_step_eq_depth, dag_step_eq_size,
          "| smallest divergent:", smallest_div["object"] if smallest_div else None)
    print("poset invariant:", poset_invariant, "on", len(common), "events;",
          "lifetime:", lifetime_sat, lifetime_dag,
          "| never-used at cap:", len(never_used))
    print("cumulative differ:", cum_witness["distributions_differ"],
          "| supports equal:", support_witness["supports_equal"])
    print("growth sat:", sizes_sat, "| dag:", sizes_dag, "(L8 =", lvl8, ")")
    print("uses sat:", U_sat, "| dag:", U_dag)
    print("F_lb sat:", F_lb_sat, "| dag:", F_lb_dag)
    print("scan:", len(scan), "points; kappa =", kappa,
          "; all saturate:", all_saturate)
    print("registry equal:", registry_equal, "| shell:", shell_equal)


def cd0_canon(o):
    """Canonical string via the same brace form as obj_str for frozensets
    coming from the frozen CD0 module."""
    if isinstance(o, str):
        return o
    return "{" + ",".join(sorted(cd0_canon(c) for c in o)) + "}"


if __name__ == "__main__":
    main()
