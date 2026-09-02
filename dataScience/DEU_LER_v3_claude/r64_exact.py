#!/usr/bin/env python3
"""OD0-R64 exact certificate engine: the locality gate class.

(1) Exact gated reachability from genesis and from minimal seeds:
    deadlock/stall witnesses per gate (deterministic ideal-level
    analysis; service can serve any subset, so fireability = the
    existence of an absent pair satisfying g).
(2) Gated kernel trajectories (labeled): growth, leaf fraction,
    cone/chain scaling, ball-shell ratios, d_J - per gate.
"""
import json
import math
import random
from pathlib import Path

PKG = Path(__file__).resolve().parent


# ------------------------------------------------------------ state
class Ideal:
    def __init__(self, seed_pairs=()):
        self.par = [None, None]
        self.anc = [1, 2]
        self.ch = [1, 1]
        self.pth = [0, 0]
        self.dep = [0, 0]
        self.kids = [set(), set()]
        self.adj = [set(), set()]
        self.pairs = {}
        self.rec = 0
        for (u, v) in seed_pairs:
            self.add(u, v)

    def add(self, u, v):
        oid = len(self.anc)
        cone = self.anc[u] | self.anc[v]
        self.anc.append(cone | (1 << oid))
        self.par.append((u, v))
        self.ch.append(self.ch[u] + self.ch[v])
        self.pth.append(self.pth[u] + 1 + self.pth[v] + 1)
        self.dep.append(1 + max(self.dep[u], self.dep[v]))
        self.kids.append(set())
        self.kids[u].add(oid)
        self.kids[v].add(oid)
        self.adj.append({u, v})
        self.adj[u].add(oid)
        self.adj[v].add(oid)
        self.pairs[(min(u, v), max(u, v))] = oid
        self.rec |= cone
        return oid

    def n(self):
        return len(self.anc)


def related(S, u, v):
    return bool((S.anc[v] >> u) & 1 or (S.anc[u] >> v) & 1)


def is_pc(S, u, v):
    return (S.par[v] is not None and u in S.par[v]) or \
           (S.par[u] is not None and v in S.par[u])


def grandparents(S, u):
    g = set()
    if S.par[u]:
        for p in S.par[u]:
            if S.par[p]:
                g |= set(S.par[p])
    return g


def parents_set(S, u):
    return set(S.par[u]) if S.par[u] else set()


def is_gp(S, u, v):
    return (u in grandparents(S, v) and not is_pc(S, u, v)) or \
           (v in grandparents(S, u) and not is_pc(S, u, v))


def is_sib(S, u, v):
    return bool(parents_set(S, u) & parents_set(S, v))


def is_cousin1(S, u, v):
    return bool(grandparents(S, u) & grandparents(S, v)) and \
        not is_sib(S, u, v)


def is_leaf(S, u):
    return not S.kids[u]


def dg2(S, u, v):
    return v not in S.adj[u] and bool(S.adj[u] & S.adj[v])


def cost(S, u, v):
    union = S.anc[u] | S.anc[v]
    w = 0
    mm = union & S.rec
    while mm:
        lo = mm & -mm
        w += S.pth[lo.bit_length() - 1]
        mm ^= lo
    return 11 * (S.ch[u] + S.ch[v]) + 2 * w


GATES = {
    "ALL": lambda S, u, v: True,
    "REL": related,
    "UNREL": lambda S, u, v: not related(S, u, v),
    "PC": is_pc,
    "NOT_PC": lambda S, u, v: not is_pc(S, u, v),
    "GP": is_gp,
    "NOT_GP": lambda S, u, v: not is_gp(S, u, v),
    "SIB": is_sib,
    "NOT_SIB": lambda S, u, v: not is_sib(S, u, v),
    "COUSIN1": is_cousin1,
    "NOT_COUSIN1": lambda S, u, v: not is_cousin1(S, u, v),
    "LEAF1": lambda S, u, v: is_leaf(S, u) or is_leaf(S, v),
    "LEAF2": lambda S, u, v: is_leaf(S, u) and is_leaf(S, v),
    "NOT_LEAF2": lambda S, u, v: not (is_leaf(S, u) and is_leaf(S, v)),
    "REC2": lambda S, u, v: not is_leaf(S, u) and not is_leaf(S, v),
    "DG2": dg2,
    "NOT_DG2": lambda S, u, v: not dg2(S, u, v),
    "DG3PLUS": lambda S, u, v: v not in S.adj[u] and
        not (S.adj[u] & S.adj[v]),
    "NOT_DG3PLUS": lambda S, u, v: v in S.adj[u] or
        bool(S.adj[u] & S.adj[v]),
    "SIB_AND_LEAF1": lambda S, u, v: is_sib(S, u, v) and
        (is_leaf(S, u) or is_leaf(S, v)),
}
# MINCOST family handled inside the kernel (needs the served set);
# reachability-wise MINCOST == ALL, REL_AND_MINCOST == REL,
# UNREL_AND_MINCOST == UNREL (a single served pair is minimal).

SEEDS = {"genesis": (), "seed3": ((0, 1),),
         "seed4": ((0, 1), (0, 2)),
         "seed5": ((0, 1), (0, 2), (1, 2)),
         "seed7": ((0, 1), (0, 2), (1, 2), (0, 3), (1, 4))}


def fireable(S, gate):
    out = []
    n = S.n()
    for u in range(n):
        for v in range(u + 1, n):
            if (u, v) in S.pairs:
                continue
            if GATES[gate](S, u, v):
                out.append((u, v))
    return out


def reach(gate, seed, n_cap=9, state_cap=20000):
    """Exhaustive gated reachability over creation-ordered histories;
    returns classification. Early exit once n_cap is reached."""
    from collections import deque
    start = tuple(SEEDS[seed])
    seen = {start}
    q = deque([start])
    max_n = Ideal(start).n()
    dead_end = None
    while q and len(seen) < state_cap:
        st = q.popleft()
        S = Ideal(st)
        f = fireable(S, gate)
        if not f:
            if dead_end is None or S.n() < dead_end:
                dead_end = S.n()
            continue
        if S.n() >= n_cap:
            max_n = max(max_n, S.n() + 1)
            break
        for (u, v) in f:
            key = st + ((u, v),)
            if key not in seen:
                seen.add(key)
                q.append(key)
            max_n = max(max_n, S.n() + 1)
        if max_n >= n_cap + 1:
            break
    if max_n >= n_cap:
        cls = "SUSTAINS"
    elif dead_end is not None and not q:
        cls = f"DEADLOCK_ALL_BRANCHES_BY_n={max_n}"
    elif dead_end is not None:
        cls = f"DEADLOCK_SEEN_MAX_n={max_n}"
    else:
        cls = "UNDETERMINED"
    return {"seed": seed, "max_n_reached": max_n,
            "earliest_dead_end_n": dead_end, "class": cls,
            "states_explored": len(seen)}


# ------------------------------------------------------------ kernel
def run_gated(gate, G, m, H, seed_pairs, seed, steps, mincost=False):
    rng = random.Random(seed)
    S = Ideal(seed_pairs)
    B = 0
    P = 0
    sp = ()
    bursts = 0
    for k in range(1, steps + 1):
        srv = sorted(sp)
        cand = []
        for i in range(len(srv)):
            for j in range(i + 1, len(srv)):
                u, v = srv[i], srv[j]
                if (min(u, v), max(u, v)) in S.pairs:
                    continue
                if mincost or GATES[gate](S, u, v):
                    cand.append((u, v))
        if mincost and cand:
            base_gate = gate if gate in GATES else "ALL"
            cand = [c for c in cand if GATES[base_gate](S, *c)]
            if cand:
                costs = [cost(S, u, v) for (u, v) in cand]
                mn = min(costs)
                cand = [c for c, cc in zip(cand, costs) if cc == mn]
        req = 0
        created = 0
        for (u, v) in cand:
            if (min(u, v), max(u, v)) in S.pairs:
                continue
            cone = S.anc[u] | S.anc[v]
            nw = rp = 0
            m1 = cone & ~S.rec
            while m1:
                lo = m1 & -m1
                nw += S.pth[lo.bit_length() - 1]
                m1 ^= lo
            m2 = cone & S.rec
            while m2:
                lo = m2 & -m2
                rp += S.pth[lo.bit_length() - 1]
                m2 ^= lo
            req += 11 * nw + 2 * rp
            S.add(u, v)
            created += 1
        if created:
            bursts += 1
        D = S.n()
        F = B + m + req
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
    return S, bursts


def analyze_gated(S):
    n = S.n()
    leaves = sum(1 for u in range(n) if is_leaf(S, u))
    csz = [bin(S.anc[i]).count("1") for i in range(n)]
    lnch = [math.log(S.ch[i]) for i in range(max(2, n // 2), n)]
    # shell ratios from late vertices
    ratios = []
    for src in range(max(0, n - 12), n):
        dist = {src: 0}
        q = [src]
        shells = {0: 1}
        for u in q:
            for w in S.adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    shells[dist[w]] = shells.get(dist[w], 0) + 1
                    q.append(w)
        rr = [shells[i + 1] / shells[i] for i in range(1, len(shells) - 2)
              if shells.get(i, 0) >= 4 and
              shells.get(i + 1, 0) / max(shells[i], 1) > 0]
        ratios += rr[:3]
    # d_J late pairs
    rng = random.Random(11)
    djs = []
    late = list(range(n // 2, n))
    if len(late) >= 3:
        for _ in range(200):
            x, y = rng.sample(late, 2)
            i = bin(S.anc[x] & S.anc[y]).count("1")
            u2 = bin(S.anc[x] | S.anc[y]).count("1")
            djs.append(1 - i / u2)
    return {
        "n": n, "leaf_fraction": round(leaves / n, 4),
        "mean_cone": round(sum(csz) / n, 2),
        "mean_cone_over_sqrt_n": round(sum(csz) / n / math.sqrt(n), 3),
        "mean_cone_over_ln_n": round(sum(csz) / n / math.log(n), 3)
        if n > 2 else None,
        "mean_ln_chains_late": round(sum(lnch) / len(lnch), 3)
        if lnch else None,
        "ln_n": round(math.log(n), 3),
        "shell_ratio_mean": round(sum(ratios) / len(ratios), 2)
        if ratios else None,
        "dJ_mean_late": round(sum(djs) / len(djs), 4) if djs else None,
    }


def main():
    out = {"schema": "R64_EXACT_CERTIFICATES_V1"}

    # (1) reachability table
    tbl = {}
    for gate in GATES:
        rows = {}
        rows["genesis"] = reach(gate, "genesis")
        if rows["genesis"]["class"].startswith("DEADLOCK") or \
                rows["genesis"]["max_n_reached"] <= 3:
            for sd in ("seed3", "seed4", "seed5", "seed7"):
                rows[sd] = reach(gate, sd)
                if rows[sd]["class"] == "SUSTAINS":
                    break
        tbl[gate] = rows
        cls = {k: v["class"] for k, v in rows.items()}
        print(gate, cls, flush=True)
    out["reachability_table"] = tbl

    # (2) gated trajectories
    runs = {}
    plan = [
        ("ALL", (), 3, 20000, False),
        ("REL", SEEDS["seed3"], 3, 20000, False),
        ("PC", SEEDS["seed3"], 3, 20000, False),
        ("NOT_PC", (), 3, 20000, False),
        ("LEAF1", (), 3, 40000, False),
        ("NOT_LEAF2", SEEDS["seed3"], 3, 20000, False),
        ("REC2", SEEDS["seed5"], 3, 20000, False),
        ("DG2", SEEDS["seed4"], 3, 40000, False),
        ("NOT_DG3PLUS", SEEDS["seed4"], 3, 40000, False),
        ("GP", SEEDS["seed4"], 3, 40000, False),
        ("SIB", SEEDS["seed5"], 3, 20000, False),
        ("ALL", (), 4, 20000, True),   # MINCOST at Gamma=4
        ("REL", SEEDS["seed3"], 4, 20000, True),  # REL_AND_MINCOST
    ]
    for (gate, seedp, G, steps, mc) in plan:
        name = ("MINCOST" if gate == "ALL" else gate + "_AND_MINCOST") \
            if mc else gate
        seed = 7000000 + G * 1000 + len(seedp) * 10 + (1 if mc else 0)
        S, bursts = run_gated(gate, G, 0, 0, seedp, seed, steps,
                              mincost=mc)
        runs[f"{name}_G{G}"] = dict(analyze_gated(S), bursts=bursts,
                                    steps=steps,
                                    seed_objects=2 + len(seedp))
        print(name, G, runs[f"{name}_G{G}"], flush=True)
    out["gated_trajectories_labeled"] = runs

    (PKG / "R64_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("written", flush=True)


if __name__ == "__main__":
    main()
