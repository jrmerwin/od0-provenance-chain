#!/usr/bin/env python3
"""OD0-R59 exact certificate engine.

(1) paths_to = 2*chains - 2 identity, exhaustive on the frozen universe.
(2) Exhaustive exact enumeration of the uniform-pair-attachment law
    (T1 marginal) for n <= 10: ensemble moments E[T_n], E[T_n^2],
    E[chains(new)], E[|cone(new)|], E[weighted cone(new)], E[cost(new)],
    and the descendant-fraction table E[d_j(n)] - merged by canonical
    ideal, exact Fractions.
(3) Mean-field comparison table (exact/mean-field ratios).
(4) Martingale normalization M_n = T_n/(E-growth product): variance table
    over the exhaustive range (L2 certificate evidence).
(5) Readout containment: R53 sampled |X_k| means vs the two-sided
    sqrt(k/log k)..sqrt(k) band with theorem-side constant bands.
(6) Bedrock/a_j readout from 2-point seeded trajectories (labeled).
"""
import json
import random
from fractions import Fraction
from functools import lru_cache
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
def chains(o):
    if isinstance(o, str):
        return 1
    u, v = sorted(parents(o), key=obj_str)
    return chains(u) + chains(v)


@lru_cache(maxsize=None)
def paths_to(o):
    if isinstance(o, str):
        return 0
    u, v = sorted(parents(o), key=obj_str)
    return (paths_to(u) + 1) + (paths_to(v) + 1)


def identity_check():
    """paths_to = 2*chains - 2 on every composite of the frozen universe."""
    allobj = {"a", "b"}
    for size in range(2, 8):
        cur = sorted(allobj, key=obj_str)
        new = set()
        for i, l in enumerate(cur):
            for r in cur[i + 1:]:
                cand = frozenset({l, r})
                if cand not in allobj and len(closed_anc(cand)) == size:
                    new.add(cand)
        allobj |= new
    fails = sum(1 for o in allobj if not isinstance(o, str)
                and paths_to(o) != 2 * chains(o) - 2)
    return len(allobj), fails


# ---------------------------------------------------------------------------
# Exhaustive uniform-pair-attachment enumeration (ideals as tuples of
# birth-indexed parent pairs; canonical form = the sequence of parent-pair
# index sets, order-insensitive within the exchange symmetry is NOT
# quotiented - we enumerate labeled growth histories merged by the labeled
# ideal, which is exact for ensemble moments).
# ---------------------------------------------------------------------------

def enumerate_law(n_max=10, state_cap=400000):
    """States: tuple of (i, j) parent index pairs for objects 2..n-1
    (objects 0, 1 are primitives). Probabilities exact."""
    from collections import defaultdict
    dists = {(): Fraction(1)}
    stats = {}
    for n in range(2, n_max):
        # current size = n objects (indices 0..n-1); choose a non-existing
        # pair uniformly
        nxt = defaultdict(Fraction)
        mom = {"ETn": Fraction(0), "ETn2": Fraction(0),
               "Echains_new": Fraction(0), "Econe_new": Fraction(0),
               "Ewcone_new": Fraction(0), "Ecost_new": Fraction(0),
               "Ed": defaultdict(Fraction)}
        for st, p in dists.items():
            k = len(st) + 2  # current object count
            existing = set(st)
            # chains and ancestries of current objects
            ch = [1, 1]
            anc = [frozenset({0}), frozenset({1})]
            for (i, j) in st:
                ch.append(ch[i] + ch[j])
                anc.append(anc[i] | anc[j] | {len(ch) - 1})
            Tn = sum(ch)
            npairs = k * (k - 1) // 2 - len(existing)
            # record stats at size k before growth (weighted by p)
            for choice_i in range(k):
                for choice_j in range(choice_i + 1, k):
                    if (choice_i, choice_j) in existing:
                        continue
                    q = p / npairs
                    newch = ch[choice_i] + ch[choice_j]
                    cone = anc[choice_i] | anc[choice_j]
                    wcone = sum(ch[w] for w in cone)
                    cost = 11 * newch + 2 * wcone  # c_first=11 typing floor
                    key = st + ((choice_i, choice_j),)
                    nxt[key] += q
                    mom["ETn"] += q * (Tn + newch)
                    mom["ETn2"] += q * (Tn + newch) ** 2
                    mom["Echains_new"] += q * newch
                    mom["Econe_new"] += q * len(cone)
                    mom["Ewcone_new"] += q * wcone
                    mom["Ecost_new"] += q * cost
                    for w in cone:
                        mom["Ed"][w] += q
        dists = dict(nxt)
        stats[n + 1] = {kk: (mom[kk] if kk != "Ed" else dict(mom["Ed"]))
                        for kk in mom}
        if len(dists) > state_cap:
            break
    return stats


def main():
    total_obj, id_fails = identity_check()

    stats = enumerate_law(10)
    table = {}
    for n, mom in stats.items():
        ETn = mom["ETn"]
        mf_T = Fraction(1)
        # mean-field: E[T_n] ~ T_3 * prod_{k=3}^{n-1} (1 + 2/k);
        # T at size 3 (after first object): exact 1+1+2 = 4
        mfv = Fraction(4)
        for k in range(3, n):
            mfv *= (1 + Fraction(2, k))
        var = mom["ETn2"] - ETn ** 2
        table[str(n)] = {
            "E_T": str(ETn), "meanfield_T": str(mfv),
            "ratio_exact_over_mf": str(ETn / mfv),
            "Var_T": str(var),
            "CV2_T": str(var / ETn ** 2),
            "E_chains_new": str(mom["Echains_new"]),
            "E_cone_new": str(mom["Econe_new"]),
            "E_wcone_new": str(mom["Ewcone_new"]),
            "E_cost_new": str(mom["Ecost_new"]),
            "ancestor_prob_by_birth": {
                str(j): str(pr) for j, pr in sorted(mom["Ed"].items())},
        }

    # ---- martingale variance-ratio evidence over the exhaustive range ----
    cv2 = [Fraction(table[str(n)]["CV2_T"].split("/")[0]) /
           Fraction(table[str(n)]["CV2_T"].split("/")[1])
           if "/" in table[str(n)]["CV2_T"]
           else Fraction(table[str(n)]["CV2_T"])
           for n in sorted(int(x) for x in table)]
    cv2_str = [str(x) for x in cv2]
    cv2_increments = [str(cv2[i + 1] - cv2[i]) for i in range(len(cv2) - 1)]

    # ---- readout containment (labeled) ----
    r53 = json.loads((PKG / "R53_SAMPLED_READOUT.json").read_text(encoding="utf-8"))
    import math
    containment = []
    for pt in r53["points"]:
        G, m, H = pt["Gamma"], pt["m"], pt["H"]
        if m >= G:
            continue  # U-growth regime only
        row = {"Gamma": G, "m": m, "H": H, "inside": True, "values": {}}
        for kk in ("1000", "10000"):
            if kk not in pt["summary"]:
                continue
            X = float(pt["summary"][kk]["X_mean_dec"])
            k = int(kk)
            lo = 0.5 * math.sqrt(k / math.log(k))
            hi = 12.0 * math.sqrt(k)
            row["values"][kk] = {"X_mean": X,
                                 "lower_band": round(lo, 2),
                                 "upper_band": round(hi, 2)}
            if not (lo <= X <= hi):
                row["inside"] = False
        containment.append(row)
    inside_all = all(r["inside"] for r in containment)

    # ---- bedrock/a_j readout (labeled, 2 points x 2 seeds) ----
    def run_traj(Gamma, m, H, seed, steps):
        rng = random.Random(seed)
        anc = [1, 2]
        pth = [0, 0]
        pairs = {}
        rec = 0
        B = 0
        P = 0
        sp = ()
        birth_anc_hits = []
        for k in range(1, steps + 1):
            s = sorted(sp)
            batch = [(s[i], s[j]) for i in range(len(s))
                     for j in range(i + 1, len(s))
                     if (s[i], s[j]) not in pairs]
            nw = rp = 0
            for (u, v) in batch:
                oid = len(anc)
                cone_mask = anc[u] | anc[v]
                birth_anc_hits.append((oid, cone_mask))
                anc.append(cone_mask | (1 << oid))
                pth.append(pth[u] + 1 + pth[v] + 1)
                pairs[(u, v)] = oid
                mask = cone_mask & ~rec
                while mask:
                    low = mask & -mask
                    nw += pth[low.bit_length() - 1]
                    mask ^= low
                mask = cone_mask & rec
                while mask:
                    low = mask & -mask
                    rp += pth[low.bit_length() - 1]
                    mask ^= low
                rec |= cone_mask
            F = B + m + 11 * nw + 2 * rp
            D = len(anc)
            n = min(Gamma, F + D)
            fr, dr = F, D
            sF = sV = 0
            for _ in range(n):
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
            voided = min(quota, H, Bm, Pm) if (Bm >= Gamma and Pm >= 6) \
                else 0
            B, P = Bm - voided, Pm - voided
        # bedrock fraction: for late-born objects (last quarter), fraction
        # of their cone born before sqrt(final n)
        import math as _m
        nfin = len(anc)
        cut = int(_m.sqrt(nfin))
        fracs = []
        for (oid, cone_mask) in birth_anc_hits[-max(1, len(birth_anc_hits) // 4):]:
            tot = bin(cone_mask).count("1")
            early = bin(cone_mask & ((1 << cut) - 1)).count("1")
            if tot:
                fracs.append(Fraction(early, tot))
        mean_frac = (sum(fracs) / len(fracs)) if fracs else Fraction(0)
        return nfin, str(mean_frac.numerator) + "/" + str(mean_frac.denominator)

    bedrock = []
    for (G, m, H) in ((2, 0, 0), (3, 0, 0)):
        for t in range(2):
            seed = 1000000 * G + 10000 * m + 100 * H + t
            nfin, frac = run_traj(G, m, H, seed, 10000)
            bedrock.append({"Gamma": G, "m": m, "H": H, "seed": seed,
                            "final_n": nfin,
                            "bedrock_fraction_late_cones": frac})

    out = {
        "schema": "R59_EXACT_CERTIFICATES_V1",
        "paths_chains_identity": {
            "statement": "paths_to(x) = 2*chains(x) - 2 exactly (q = "
                         "paths_to + 2 satisfies the chains recursion "
                         "with q(primitive) = 2)",
            "objects_checked": total_obj, "failures": id_fails},
        "exhaustive_law_moments_n_le_10": table,
        "cv2_trajectory": {"values": cv2_str,
                           "increments": cv2_increments},
        "readout_containment": {"band": "0.5*sqrt(k/log k) <= X <= "
                                        "12*sqrt(k) (theorem-side "
                                        "constant band)",
                                "points": containment,
                                "all_inside": inside_all},
        "bedrock_readout_labeled": bedrock,
    }
    (PKG / "R59_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("identity: checked", total_obj, "objects,", id_fails, "failures")
    for n in sorted(int(x) for x in table):
        t = table[str(n)]
        print(f"n={n}: E[T]={t['E_T']} mf={t['meanfield_T']} "
              f"ratio={t['ratio_exact_over_mf'][:12]} "
              f"Ecost={t['E_cost_new'][:10]}")
    print("readout containment all inside:", inside_all)
    print("bedrock:", [(b['final_n'], b['bedrock_fraction_late_cones'][:8])
                       for b in bedrock])


if __name__ == "__main__":
    main()
