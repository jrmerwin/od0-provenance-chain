#!/usr/bin/env python3
"""OD0-R60 exact certificate engine: lapse/clock epoch laws.

(1) L2 case-table certification (exact hypergeometric, all cases).
(2) L1/L3 exact early evolution per registered (Gamma, m): E0/middle
    durations and the E1-entry Phi^2 distribution (exact Fractions,
    horizon-exact with residual recorded).
(3) L4 pure-drain backward induction: cycle length, cycle-average
    Phi^2, expected mid-drain trigger count - adjudicates the two
    candidate cycle-average formulas (float64 deterministic; one small
    case cross-checked in exact rationals).
(4) Exhaustive depth-count check n <= 10 + chains <= 2^depth on the
    frozen universe.
(5) Relief subsystem fixed point: long-run voided/step v*(Gamma, H).
(6) Seeded trajectory readouts (labeled): x, Phi^2, bursts, renewals,
    N_V, max depth, direct-limit reading vs n at k = 1e2, 1e3, 1e4.
"""
import json
import math
import random
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path

PKG = Path(__file__).resolve().parent


def C(a, b):
    return math.comb(a, b) if 0 <= b <= a else 0


def hyper(F, D, s):
    """Exact dist of S_V when drawing s from F forced + D vacuum."""
    tot = C(F + D, s)
    return {v: Fraction(C(D, v) * C(F, s - v), tot)
            for v in range(max(0, s - F), min(D, s) + 1)}


# ---------------------------------------------------------------- (1) L2
def l2_case_table(Gmax=5, FDmax=30):
    fails = 0
    checked = 0
    for G in range(2, Gmax + 1):
        for D in range(0, FDmax + 1):
            for F in range(0, FDmax + 1):
                if F + D == 0:
                    continue
                s = min(G, F + D)
                dist = hyper(F, D, s)
                V0 = min(G, D)
                checked += 1
                ESV = sum(v * p for v, p in dist.items())
                if F + D <= G:
                    ok = dist.get(D, 0) == 1 and (
                        D == 0 or Fraction(D, V0) == 1)
                elif D > G:
                    ok = (ESV == Fraction(G * D, F + D)
                          and dist.get(G, 0) ==
                          Fraction(C(D, G), C(F + D, G)))
                else:  # D <= G < F+D
                    ok = (D == 0 or
                          (ESV / D == Fraction(G, F + D)
                           and dist.get(D, 0) ==
                           Fraction(C(F, G - D), C(F + D, G))))
                fails += 0 if ok else 1
    return checked, fails


# ------------------------------------------------- cost law (paths-form)
def rebuild(pair_seq):
    """Rebuild anc/pth/dep/pairs from the creation-ordered pair tuple."""
    anc = [1, 2]
    pth = [0, 0]
    dep = [0, 0]
    pairs = {}
    for (u, v) in pair_seq:
        oid = len(anc)
        anc.append(anc[u] | anc[v] | (1 << oid))
        pth.append(pth[u] + 1 + pth[v] + 1)
        dep.append(1 + max(dep[u], dep[v]))
        pairs[(u, v)] = oid
    return anc, pth, dep, pairs


def do_burst(sp, pair_seq, rec):
    """Form all absent pairs among served vacuum objects (creation order
    = sorted pair order). Returns (requests, created, new_pair_seq,
    new_rec)."""
    anc, pth, dep, pairs = rebuild(pair_seq)
    s = sorted(sp)
    nw = rp = created = 0
    seq = list(pair_seq)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            u, v = s[i], s[j]
            if (u, v) in pairs:
                continue
            oid = len(anc)
            cone = anc[u] | anc[v]
            anc.append(cone | (1 << oid))
            pth.append(pth[u] + 1 + pth[v] + 1)
            dep.append(1 + max(dep[u], dep[v]))
            pairs[(u, v)] = oid
            seq.append((u, v))
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
            created += 1
    return 11 * nw + 2 * rp, created, tuple(seq), rec, len(anc)


# ------------------------------------------------- (2) L1/L3 exact early
def early_evolution(G, m, H, max_steps=40, state_cap=250000):
    """Exact distribution evolution from genesis until every branch has
    D > G (E1 entered) or horizon. Branch state: (pair_seq, sp, B, P,
    rec, e0_steps, mid_steps) -> prob. Returns E0 duration dist, middle
    duration dist, entry Phi^2 dist, residual prob."""
    branches = {((), (), 0, 0, 0, 0, 0): Fraction(1)}
    e0d, midd, entry = {}, {}, {}
    for step in range(1, max_steps + 1):
        nxt = {}
        for (pseq, sp, B, P, rec, e0, mid), prob in branches.items():
            req, created, pseq2, rec2, D = do_burst(sp, pseq, rec)
            F = B + m + req
            if D > G:  # E1 entered at this step
                e0d[e0] = e0d.get(e0, Fraction(0)) + prob
                midd[mid] = midd.get(mid, Fraction(0)) + prob
                s = min(G, F + D)
                for sv, p in hyper(F, D, s).items():
                    phi2 = Fraction(sv, min(G, D))
                    entry[phi2] = entry.get(phi2, Fraction(0)) + prob * p
                continue
            in_e0 = (F + D <= G)
            s = min(G, F + D)
            for sv, p_sv in hyper(F, D, s).items():
                sF = s - sv
                Bm = F - sF
                Pm = P + 2 * sF
                base = max(1, Pm // 6)
                quota = 2 * ((base + 1) // 2)
                void = min(quota, H, Bm, Pm) if (Bm >= G and Pm >= 6) \
                    else 0
                nsub = C(D, sv)
                for sub in combinations(range(D), sv):
                    key = (pseq2, sub, Bm - void, Pm - void, rec2,
                           e0 + (1 if in_e0 else 0),
                           mid + (0 if in_e0 else 1))
                    nxt[key] = nxt.get(key, Fraction(0)) + \
                        prob * p_sv / nsub
        branches = nxt
        if not branches or len(branches) > state_cap:
            break
    resid = sum(branches.values(), Fraction(0))
    return e0d, midd, entry, resid


# ------------------------------------------------- (3) L4 drain
def drain_induction(G, D, Cst, exact=False):
    """Pure drain, m=0, H=0, no burst injection: E[tau], E[sum x],
    E[#steps with S_V>=2] from F=Cst to absorption at F=0."""
    zero = Fraction(0) if exact else 0.0
    Etau = [zero] * (Cst + 1)
    Ax = [zero] * (Cst + 1)
    Trig = [zero] * (Cst + 1)
    for F in range(1, Cst + 1):
        s = min(G, F + D)
        dist = hyper(F, D, s)
        if not exact:
            dist = {v: float(p) for v, p in dist.items()}
        x = Fraction(D, F + D) if exact else D / (F + D)
        tg0 = sum(p for v, p in dist.items() if v >= 2)
        p0 = sum(p for v, p in dist.items() if s - v == 0)
        acc_t = acc_x = acc_g = zero
        for v, p in dist.items():
            sF = s - v
            if sF > 0:
                acc_t += p * Etau[F - sF]
                acc_x += p * Ax[F - sF]
                acc_g += p * Trig[F - sF]
        den = 1 - p0
        Etau[F] = (1 + acc_t) / den
        Ax[F] = (x + acc_x) / den
        Trig[F] = (tg0 + acc_g) / den
    return Etau[Cst], Ax[Cst], Trig[Cst]


# --------------------------------------------- (4) depth certificates
def obj_str(o):
    if isinstance(o, str):
        return o
    return "{" + ",".join(sorted(obj_str(c) for c in o)) + "}"


@lru_cache(maxsize=None)
def _anc(o):
    if isinstance(o, str):
        return frozenset({o})
    r = {o}
    for c in o:
        r |= _anc(c)
    return frozenset(r)


@lru_cache(maxsize=None)
def _chains(o):
    if isinstance(o, str):
        return 1
    u, v = sorted(o, key=obj_str)
    return _chains(u) + _chains(v)


@lru_cache(maxsize=None)
def _depth(o):
    if isinstance(o, str):
        return 0
    u, v = sorted(o, key=obj_str)
    return 1 + max(_depth(u), _depth(v))


def frozen_universe_depth_check():
    allobj = {"a", "b"}
    for size in range(2, 8):
        cur = sorted(allobj, key=obj_str)
        new = set()
        for i, l in enumerate(cur):
            for r in cur[i + 1:]:
                cand = frozenset({l, r})
                if cand not in allobj and len(_anc(cand)) == size:
                    new.add(cand)
        allobj |= new
    fails = sum(1 for o in allobj if _chains(o) > 2 ** _depth(o))
    return len(allobj), fails


def depth_enumeration(n_max=10):
    from collections import defaultdict
    dists = {(): Fraction(1)}
    out = {}
    for n in range(2, n_max):
        nxt = defaultdict(Fraction)
        for st, p in dists.items():
            k = len(st) + 2
            existing = set(st)
            cand = [(i, j) for i in range(k) for j in range(i + 1, k)
                    if (i, j) not in existing]
            for ij in cand:
                nxt[st + (ij,)] += p / len(cand)
        dists = dict(nxt)
        Nd = defaultdict(Fraction)
        Emax = Fraction(0)
        for st, p in dists.items():
            dep = [0, 0]
            for (i, j) in st:
                dep.append(1 + max(dep[i], dep[j]))
            for d in dep:
                Nd[d] += p
            Emax += p * max(dep)
        k = len(next(iter(dists))) + 2
        Hn = sum(Fraction(1, t) for t in range(1, k))
        bound_ok = all(
            float(Nd[d]) <= float((2 * Hn) ** d) / math.factorial(d)
            + 1e-12 for d in Nd if d >= 1)
        out[str(k)] = {"E_Nd": {str(d): str(Nd[d]) for d in sorted(Nd)},
                       "E_maxdepth": str(Emax),
                       "poisson_bound_holds": bool(bound_ok)}
    return out


# --------------------------------------------- (5) relief fixed point
def relief_fixed_point(G, H):
    P = 0
    seen = {}
    voided_tot = 0
    t = 0
    while True:
        if P in seen:
            t0, v0 = seen[P]
            return Fraction(voided_tot - v0, t - t0)
        seen[P] = (t, voided_tot)
        Pm = P + 2 * G
        base = max(1, Pm // 6)
        quota = 2 * ((base + 1) // 2)
        v = min(quota, H, Pm) if Pm >= 6 else 0  # B-cap assumed slack
        P = Pm - v
        voided_tot += v
        t += 1
        if t > 500000:
            return Fraction(voided_tot, t)


# --------------------------------------------- (6) trajectories (labeled)
def run_traj(G, m, H, seed, steps, checkpoints):
    rng = random.Random(seed)
    pairs = {}
    anc = [1, 2]
    pth = [0, 0]
    dep = [0, 0]
    rec = 0
    B = 0
    P = 0
    sp = ()
    NV = 0
    bursts = 0
    renewals = 0
    sum_phi2 = 0.0
    sum_x2 = 0.0
    win_x2 = 0.0
    win_start = 0
    tick_depth_counts = {}
    res = {}
    for k in range(1, steps + 1):
        # in-place burst (no rebuild: persistent structures)
        s = sorted(sp)
        nw = rp = created = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                u, v = s[i], s[j]
                if (u, v) in pairs:
                    continue
                oid = len(anc)
                cone = anc[u] | anc[v]
                anc.append(cone | (1 << oid))
                pth.append(pth[u] + 1 + pth[v] + 1)
                dep.append(1 + max(dep[u], dep[v]))
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
                created += 1
        if created:
            bursts += 1
        D = len(anc)
        F = B + m + 11 * nw + 2 * rp
        if F == 0:
            renewals += 1
        x = D / (F + D)
        sum_x2 += x * x
        win_x2 += x * x
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
        NV += sV
        M = max(dep)
        tick_depth_counts[M] = tick_depth_counts.get(M, 0) + sV
        sum_phi2 += sV / min(G, D)
        Bm = F - sF
        Pm = P + 2 * sF
        base = max(1, Pm // 6)
        quota = 2 * ((base + 1) // 2)
        void = min(quota, H, Bm, Pm) if (Bm >= G and Pm >= 6) else 0
        B, P = Bm - void, Pm - void
        if k in checkpoints:
            n = len(anc)
            Mfin = max(dep)
            reading = sum(c * 3 ** (Mfin - Md)
                          for Md, c in tick_depth_counts.items())
            wlen = k - win_start
            res[str(k)] = {
                "n": n, "b": bursts, "N_V": NV, "renewals": renewals,
                "max_depth": Mfin,
                "avg_phi2": round(sum_phi2 / k, 6),
                "rms_x": round(math.sqrt(sum_x2 / k), 6),
                "window_rms_x": round(math.sqrt(win_x2 / wlen), 6),
                "reading_log10": round(math.log10(reading), 3)
                if reading else None,
                "reading_over_3maxdepth": round(
                    reading / 3 ** Mfin, 3) if reading else None,
            }
            win_x2 = 0.0
            win_start = k
    return res


def main():
    out = {"schema": "R60_EXACT_CERTIFICATES_V1"}

    checked, fails = l2_case_table()
    out["L2_case_table"] = {"states_checked": checked, "failures": fails}
    print("L2 cases:", checked, "failures:", fails, flush=True)

    r53 = json.loads((PKG / "R53_SAMPLED_READOUT.json").read_text(
        encoding="utf-8"))
    gm_points = sorted({(p["Gamma"], p["m"]) for p in r53["points"]
                        if p["m"] < p["Gamma"]})

    early = {}
    for (G, m) in gm_points:
        for H in (0, 8):
            e0d, midd, entry, resid = early_evolution(G, m, H)
            mass = sum(entry.values(), Fraction(0))
            Ephi = (sum(ph * p for ph, p in entry.items()) / mass
                    if mass else Fraction(0))
            early[f"G{G}_m{m}_H{H}"] = {
                "E0_duration_dist": {str(k): str(v) for k, v in
                                     sorted(e0d.items())},
                "middle_duration_dist": {str(k): str(v) for k, v in
                                         sorted(midd.items())},
                "entry_phi2_dist": {str(k): str(v) for k, v in
                                    sorted(entry.items())},
                "E_phi2_at_entry_given_entered": str(Ephi),
                "drop_magnitude_given_entered": str(1 - Ephi),
                "entered_prob_within_horizon": str(mass),
                "unresolved_prob": str(resid)}
    out["L1_L3_early_evolution"] = early
    print("early evolution done:", len(early), "entries", flush=True)

    # small exact-vs-float cross-check
    Et_e, Ax_e, Tg_e = drain_induction(2, 8, 40, exact=True)
    Et_f, Ax_f, Tg_f = drain_induction(2, 8, 40, exact=False)
    cross = {"D": 8, "C": 40, "Gamma": 2,
             "exact_avg_phi2": str(Ax_e / Et_e),
             "float_avg_phi2": repr(Ax_f / Et_f),
             "abs_diff": repr(abs(float(Ax_e / Et_e) - Ax_f / Et_f))}
    drains = [cross]
    for G in (2, 3):
        for D in (20, 60, 150):
            Cst = int(4 * D * math.log(D))
            Et, Ax_, Tg = drain_induction(G, D, Cst)
            avg = Ax_ / Et
            HC = sum(1.0 / t for t in range(1, Cst + 1))
            mine = D * HC / (Cst + D * HC)
            naive = (D / Cst) * math.log(1 + Cst / D)
            drains.append({
                "Gamma": G, "D": D, "C": Cst,
                "exact_E_tau": round(Et, 2),
                "exact_avg_phi2": round(avg, 5),
                "formula_DHC_over_C_plus_DHC": round(mine, 5),
                "naive_constant_rate_formula": round(naive, 5),
                "E_middrain_triggers": round(Tg, 2)})
            print("drain", G, D, Cst, round(avg, 5), round(mine, 5),
                  round(naive, 5), round(Tg, 2), flush=True)
    out["L4_drain_induction"] = drains

    nobj, dfails = frozen_universe_depth_check()
    out["L7_chains_le_2pow_depth"] = {"objects": nobj,
                                      "failures": dfails}
    print("depth check:", nobj, dfails, flush=True)
    out["L7_depth_enumeration_n_le_10"] = depth_enumeration(10)
    print("depth enumeration done", flush=True)

    relief = {}
    for G in range(2, 6):
        for H in range(0, 9):
            v = relief_fixed_point(G, H)
            relief[f"G{G}_H{H}"] = {"v_star": str(v),
                                    "min_H_2G": min(H, 2 * G)}
    out["L4_relief_fixed_point"] = relief
    print("relief G2:", {h: relief[f"G2_H{h}"]["v_star"]
                         for h in range(9)}, flush=True)

    cps = {100, 1000, 10000}
    trajs = {}
    for (G, m) in gm_points:
        Hs = range(0, 9) if G in (2, 3) else (0, 4, 8)
        for H in Hs:
            seed = 1000000 * G + 10000 * m + 100 * H
            trajs[f"G{G}_m{m}_H{H}_s{seed}"] = run_traj(
                G, m, H, seed, 10000, cps)
    out["L5_L6_L7_trajectories_labeled"] = trajs
    print("trajectories done:", len(trajs), flush=True)

    (PKG / "R60_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("written", flush=True)


if __name__ == "__main__":
    main()
