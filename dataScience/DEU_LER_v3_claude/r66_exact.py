#!/usr/bin/env python3
"""OD0-R66 exact certificate engine.

(1) G1 back-action invariance: on a gated trajectory, form an
    adjunction and certify that all pairwise record-tree distances
    among existing records are bit-identical before/after (records
    append-only; prefixes immutable).
(2) G2 character-pairing consistency: exact tables at depths d <= 4 -
    for every q in Z/3^{d+1} and a set of 3-adic words w, verify
    <[d,q],w> = <[d+1,3q],w> (consistency under the embedding), the
    homomorphism property, and distinctness of characters for
    distinct word-truncations.
"""
import json
from fractions import Fraction
from itertools import product
from pathlib import Path

PKG = Path(__file__).resolve().parent


# ------------------------------------------------------------- (1) G1
def g1_backaction():
    """Record-tree distances: records = prefix nodes; an adjunction
    appends new records (new prefix occupations) and never edits
    existing ones. Certificate: distances among a fixed record set are
    invariant under appending arbitrary new records."""
    def cp(a, b):
        c = 0
        for x, y in zip(a, b):
            if x != y:
                break
            c += 1
        return c

    def dist(a, b):
        return Fraction(0) if a == b else Fraction(1, 3 ** cp(a, b))

    base = [(), (0,), (0, 1), (1,), (1, 2, 0), (2, 2)]
    before = {(i, j): dist(base[i], base[j])
              for i in range(len(base)) for j in range(i)}
    appended = base + [(0, 1, 2), (2,), (1, 2, 0, 1), (0, 0)]
    after = {(i, j): dist(appended[i], appended[j])
             for i in range(len(base)) for j in range(i)}
    return {"pairs_checked": len(before),
            "invariant": before == after,
            "note": "distances among pre-existing records are "
                    "functions of their fixed prefixes only; "
                    "appending records cannot alter them (records "
                    "are never erased, prefixes never rewritten - "
                    "R63 D8 carried to the record tree)"}


# ------------------------------------------------------------- (2) G2
def g2_pairing(dmax=4):
    """Pairing <[d,q],w> = q * w^{(d+1)} mod 3^{d+1} (as an angle
    numerator over 3^{d+1}). Certify embedding-consistency,
    homomorphism, and separation."""
    words = list(product((0, 1, 2), repeat=dmax + 2))
    import random
    rng = random.Random(66)
    wsample = [words[0], words[-1]] + rng.sample(words, 25)

    def wm(w, m):
        # w^{(m)} = sum w_i 3^i for i < m  (3-adic truncation)
        return sum(w[i] * 3 ** i for i in range(m))

    fails_embed = fails_hom = 0
    checked = 0
    for d in range(0, dmax):
        N1 = 3 ** (d + 1)
        N2 = 3 ** (d + 2)
        for q in range(N1):
            for w in wsample:
                checked += 1
                # angle of <[d,q],w> = q*w^{(d+1)}/N1
                a1 = Fraction(q * wm(w, d + 1) % N1, N1)
                # embedded: [d+1, 3q]: angle = 3q*w^{(d+2)}/N2
                a2 = Fraction((3 * q * wm(w, d + 2)) % N2, N2)
                if (a1 - a2) % 1 != 0:
                    fails_embed += 1
        # homomorphism in q at fixed d
        for w in wsample[:8]:
            for q1 in range(N1):
                for q2 in range(N1):
                    a = Fraction((q1 + q2) % N1 * wm(w, d + 1) % N1, N1)
                    b = (Fraction(q1 * wm(w, d + 1) % N1, N1) +
                         Fraction(q2 * wm(w, d + 1) % N1, N1)) % 1
                    if (a - b) % 1 != 0:
                        fails_hom += 1
    # separation: distinct truncations give distinct characters at
    # the witnessing depth
    sep_fails = 0
    d = dmax
    N = 3 ** (d + 1)
    seen = {}
    for w in words:
        key = wm(w, d + 1)
        tab = tuple((q * key) % N for q in range(N))
        if key in seen:
            if seen[key] != tab:
                sep_fails += 1
        else:
            for k2, t2 in seen.items():
                if t2 == tab and k2 != key:
                    sep_fails += 1
            seen[key] = tab
    distinct = len({tuple(v) for v in seen.values()})
    return {"embedding_consistency_checks": checked,
            "embedding_failures": fails_embed,
            "homomorphism_failures": fails_hom,
            "separation_failures": sep_fails,
            "distinct_characters_at_depth": {"depth": d,
                                             "expected": N,
                                             "found": distinct}}


def main():
    out = {"schema": "R66_EXACT_CERTIFICATES_V1"}
    out["G1_backaction_invariance"] = g1_backaction()
    print("G1:", out["G1_backaction_invariance"], flush=True)
    out["G2_character_pairing"] = g2_pairing(4)
    print("G2:", out["G2_character_pairing"], flush=True)
    (PKG / "R66_EXACT_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="\n")
    print("written", flush=True)


if __name__ == "__main__":
    main()
