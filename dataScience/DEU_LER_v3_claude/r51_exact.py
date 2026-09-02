#!/usr/bin/env python3
"""OD0-R51 exact certificate engine.

Part 1  - S4 genesis-service table (exact, all registered Gamma, m).
Part 3  - candidate adjudication computations: deadlock witnesses, growth
          bounds, lifetime>1 witness probabilities.
Part 4  - exact distribution dynamics for the survivors ADJ-V-S and ADJ-V-P
          over the registered (Gamma, m, H) domain (D consumed by the V~X
          identification; genesis B=0, P=0 per the R50 scan convention;
          Lambda_0 remains undeclared and is not chosen).

Exact arithmetic only (int/Fraction). Deterministic.
Load convention (carried from R50): 11 A12 requests per distinct record
(frozen Q1 minimum) - a declared lower-bound load, recorded in outputs.
"""
import json
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path

PKG = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Constructor primitives (frozen rule)
# ---------------------------------------------------------------------------


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


@lru_cache(maxsize=4096)
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


@lru_cache(maxsize=65536)
def event_records(X_key, e):
    """Distinct prefix-canonical RO-D record prefixes (ell>=1) for one
    event e fired on pre-fire state X."""
    recs = set()
    pe = tuple(sorted(parents(e), key=obj_str))
    anc = [closed_anc(z) for z in pe]
    for lam in lineages_of_key(X_key):
        pos = []
        for a in anc:
            hit = [i for i, mm in enumerate(lam) if mm in a]
            if hit:
                pos.append(max(hit))
        if pos and max(pos) >= 1:
            recs.add(lam[:max(pos) + 1])
    return frozenset(recs)


def record_count(X_key, batch_key):
    total = 0
    for e in batch_key:
        total += len(event_records(X_key, e))
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


QMIN = 11  # frozen Q1 per-record request minimum (lower-bound load)


# ---------------------------------------------------------------------------
# Survivor dynamics: exact distribution evolution
# ---------------------------------------------------------------------------

def step_distribution(dists, mode, Gamma, m, H, expansion_budget):
    """One global step. State = (X_key, gate_set_key, B, P) where gate_set
    is served-prev (mode 'S') or marked (mode 'P'). Returns (new_dists,
    step_stats) or (None, None) if the exact expansion would exceed the
    budget (the point then stops with that reason)."""
    # pre-estimate expansion cost exactly: sum over states of
    # sum over outcomes of C(D, sv)
    est = 0
    for (X_key, gate_key, B, P), prob in dists.items():
        X = frozenset(X_key)
        gate = sorted(frozenset(gate_key), key=obj_str)
        nb = sum(1 for i, u in enumerate(gate) for v in gate[i + 1:]
                 if frozenset({u, v}) not in X)
        D_svc = len(X) + nb
        F_min = B + m  # request count only increases F; C(D,sv) max at sv
        n = min(Gamma, F_min + D_svc)
        for sv in range(0, n + 1):
            est += comb(D_svc, sv)
        if est > expansion_budget:
            return None, None
    nxt = {}
    p_sv0 = Fraction(0)
    exp_sv = Fraction(0)
    exp_records = Fraction(0)
    exp_X = Fraction(0)
    x_min = None
    x_max = None
    shell_min = None
    shell_max = None
    b_min = None
    b_max = None
    for (X_key, gate_key, B, P), prob in dists.items():
        X = frozenset(X_key)
        gate = frozenset(gate_key)
        # fired batch: all absent pairs with both members in the gate set
        batch = []
        gl = sorted(gate, key=obj_str)
        for i, u in enumerate(gl):
            for v in gl[i + 1:]:
                cand = frozenset({u, v})
                if cand not in X:
                    batch.append(cand)
        batch_key = tuple(sorted(batch, key=obj_str))
        X_new = X | set(batch)
        X_new_key = tuple(sorted(X_new, key=obj_str))
        R = record_count(X_key, batch_key)
        arrivals = m + QMIN * R
        F = B + arrivals
        D_svc = len(X_new)
        n = min(Gamma, F + D_svc)
        exp_records += prob * R
        exp_X += prob * len(X_new)
        x_min = len(X_new) if x_min is None else min(x_min, len(X_new))
        x_max = len(X_new) if x_max is None else max(x_max, len(X_new))
        used = {p for o in X_new for p in parents(o)}
        shell = len(X_new) - len(used & X_new)
        shell_min = shell if shell_min is None else min(shell_min, shell)
        shell_max = shell if shell_max is None else max(shell_max, shell)
        objs = sorted(X_new, key=obj_str)
        for s in range(max(0, n - D_svc), min(F, n) + 1):
            sv = n - s
            p_s = hyper_pmf(F, D_svc, n, s)
            if p_s == 0:
                continue
            Bm = F - s
            Pm = P + 2 * s
            quota = even_relief_quota(Pm)
            g = Bm >= Gamma and Pm >= 6
            voided = min(quota, H, Bm, Pm) if g else 0
            B2, P2 = Bm - voided, Pm - voided
            b_min = B2 if b_min is None else min(b_min, B2)
            b_max = B2 if b_max is None else max(b_max, B2)
            if sv == 0:
                p_sv0 += prob * p_s
            exp_sv += prob * p_s * sv
            # served vacuum subsets: uniform over C(D_svc, sv)
            total_subsets = comb(D_svc, sv)
            p_each = p_s / total_subsets
            for served in combinations(objs, sv):
                sset = frozenset(served)
                if mode == "S":
                    g_new = tuple(sorted(sset, key=obj_str))
                else:  # persistent marks
                    g_new = tuple(sorted(gate | sset, key=obj_str))
                key = (X_new_key, g_new, B2, P2)
                nxt[key] = nxt.get(key, Fraction(0)) + prob * p_each
    stats = {
        "P_SV0": p_sv0, "E_SV": exp_sv, "E_records": exp_records,
        "E_X": exp_X, "X_range": [x_min, x_max],
        "shell_range": [shell_min, shell_max], "B_range": [b_min, b_max],
        "states": len(nxt),
    }
    return nxt, stats


def run_point(mode, Gamma, m, H, k_cap, state_cap):
    genesis = (("a", "b"), (), 0, 0)
    # step 0: no firing, arrivals = m, D = 2, service seeds the gate set
    dists = {}
    F = m
    D0 = 2
    n = min(Gamma, F + D0)
    for s in range(max(0, n - D0), min(F, n) + 1):
        sv = n - s
        p_s = hyper_pmf(F, D0, n, s)
        if p_s == 0:
            continue
        Bm = F - s
        Pm = 2 * s
        quota = even_relief_quota(Pm)
        g = Bm >= Gamma and Pm >= 6
        voided = min(quota, H, Bm, Pm) if g else 0
        for served in combinations(("a", "b"), sv):
            key = (("a", "b"), tuple(sorted(served)), Bm - voided, Pm - voided)
            dists[key] = dists.get(key, Fraction(0)) + p_s / comb(D0, sv)
    traj = []
    k = 0
    reason = "k_cap_reached"
    EXP_BUDGET = 60000
    while k < k_cap:
        nd, st = step_distribution(dists, mode, Gamma, m, H, EXP_BUDGET)
        if nd is None:
            reason = f"exact_expansion_budget_{EXP_BUDGET}_exceeded"
            break
        k += 1
        dists = nd
        assert sum(dists.values()) == 1
        traj.append({
            "k": k, "P_SV0": str(st["P_SV0"]), "E_SV": str(st["E_SV"]),
            "E_records": str(st["E_records"]), "E_X": str(st["E_X"]),
            "X_range": st["X_range"], "shell_range": st["shell_range"],
            "B_range": st["B_range"], "states": st["states"],
        })
        if st["states"] > state_cap:
            reason = f"state_cap_{state_cap}_exceeded"
            break
    lapse_note = ("lapse Phi^2 = S^V / D with D = |X| (V ~ X); "
                  "E[Phi^2]_k = E_SV/E_X reported componentwise; "
                  "square root withheld (exact arithmetic)")
    return {"K_max": k, "K_max_reason": reason, "trajectory": traj,
            "lapse_convention": lapse_note}


# ---------------------------------------------------------------------------
def main():
    # ---- S4 genesis service table (Gamma 0..5, m 0..3) ----
    genesis_table = []
    for Gamma in range(6):
        for m in range(4):
            F, D0 = m, 2
            n = min(Gamma, F + D0)
            p_both = Fraction(0)  # P(served set = {a,b}) = P(S^V = 2)
            p_sv = {}
            for s in range(max(0, n - D0), min(F, n) + 1):
                sv = n - s
                p_s = hyper_pmf(F, D0, n, s)
                p_sv[sv] = p_sv.get(sv, Fraction(0)) + p_s
            p_both = p_sv.get(2, Fraction(0))
            genesis_table.append({
                "Gamma": Gamma, "m": m, "n0": n,
                "P_SV": {str(k): str(v) for k, v in sorted(p_sv.items())},
                "P_both_primitives_served": str(p_both),
                "deterministic_all_vacuum": (m == 0),
            })

    # ---- C4 lifetime>1 witness (ADJ-V-S, Gamma=2, m=0, H=0) ----
    # path: step0 serve {a,b} (prob 1); step1 fire c; serve a 2-subset of
    # {a,b,c} uniformly; if {a,b} (prob 1/3) then step2 fires nothing and c
    # remains unused: lifetime(c) >= 2 with probability 1/3.
    lifetime_witness = {
        "candidate": "ADJ-V-S", "point": "Gamma=2, m=0, H=0",
        "path": "step0 serves {a,b} with probability 1 (F=0, D=2, n=2); "
                "step1 fires c={a,b} (0 records); step1 service draws a "
                "uniform 2-subset of {a,b,c}; the subset {a,b} has "
                "probability 1/3 and fires nothing at step 2, leaving c "
                "un-built-upon",
        "probability_lifetime_c_ge_2": str(Fraction(1, 3)),
    }

    # ---- Part 4: survivor dynamics over the registered domain ----
    K_CAP = 8
    STATE_CAP = 2500
    scans = {}
    for mode, gammas in (("S", range(2, 6)), ("P", range(1, 6))):
        rows = []
        for Gamma in gammas:
            for m in range(4):
                for H in range(9):
                    res = run_point(mode, Gamma, m, H, K_CAP, STATE_CAP)
                    rows.append({"Gamma": Gamma, "m": m, "H": H, **res})
        scans["ADJ-V-" + mode] = rows

    # deadlocked scope points (exact): ADJ-V-S at Gamma<=1 - a pair needs
    # two same-step served tokens; n = min(Gamma, F+D) <= 1 forever.
    # ADJ-V-P at Gamma=0: n=0 forever, no token ever served.
    scope = {
        "ADJ-V-S": {"deadlock_free_Gamma": "2..5 (registered)",
                    "deadlock_witness_Gamma_le_1": "n = min(Gamma, F+D) <= 1 "
                    "serves at most one token per step, and the same-step "
                    "gate needs both parents served in ONE step; no "
                    "adjunction ever fires; X stays {a,b} forever "
                    "(exact, all m, H)"},
        "ADJ-V-P": {"deadlock_free_Gamma": "1..5 (registered)",
                    "deadlock_witness_Gamma_0": "n = 0: no token is ever "
                    "served, no mark is ever created, no adjunction fires"},
    }

    out = {
        "schema": "R51_EXACT_CERTIFICATES_V1",
        "load_convention": f"{QMIN} A12 requests per distinct "
                           "prefix-canonical record (frozen Q1 minimum; "
                           "declared lower-bound load, as in R50)",
        "genesis_service_table": genesis_table,
        "lifetime_witness": lifetime_witness,
        "survivor_scope": scope,
        "survivor_dynamics": scans,
    }
    (PKG / "R51_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    for name, rows in scans.items():
        kmaxes = [r["K_max"] for r in rows]
        print(name, "points:", len(rows), "K_max range:",
              min(kmaxes), "-", max(kmaxes))
        ex = rows[0]
        print("  exemplar (G,m,H)=(", ex["Gamma"], ex["m"], ex["H"], ") EX:",
              [t["E_X"] for t in ex["trajectory"][:6]])
        print("  P_SV0 trajectory:", [t["P_SV0"] for t in ex["trajectory"][:6]])


if __name__ == "__main__":
    main()
