#!/usr/bin/env python3
# C26 selection: candidate identification (A: final-relief survivor; B: max-reuse
# lineage), deterministic tie-breaks (prereg 4.3), exact-type control matching,
# and the five preflight observables P/U/M/S/C (prereg section 7).
# Consumes ONLY the firewall view (c26_firewall.load_whitelisted).
#
# Implementation definitions requiring PI ratification before freeze (flagged in
# RUNBOOK_C26.md): snapshot-lattice support counting; d/ell* with ell* = the
# candidate's max-depth face scale 3^(-k/2); identity-based control cleanliness.
#
# Usage: python3 c26_select.py <config.json> <cache_dir> <out_json>
import hashlib, heapq, itertools, json, sys
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path
from c26_firewall import load_whitelisted

L = lambda k: (3.0 ** -0.5) ** k          # face length scale
AREA = lambda k: Fraction(1, 3 ** k)      # exact face area weight

# ---------- geometry on a snapshot -------------------------------------------
def face_adjacency(snap):
    e2f = {}
    for f, nodes in snap["face_nodes"].items():
        for e in itertools.combinations(sorted(nodes), 2):
            e2f.setdefault(frozenset(e), set()).add(f)
    adj = {f: set() for f in snap["face_nodes"]}
    for fs in e2f.values():
        for a, b in itertools.combinations(sorted(fs), 2):
            adj[a].add(b); adj[b].add(a)
    return adj

def face_dijkstra_from_node(snap, node, adj=None, maxd=1e18):
    """Weighted face distances from a locus NODE (mirrors core_partition metric)."""
    adj = adj or face_adjacency(snap)
    dep = snap["face_depth"]
    src = [f for f, nd in snap["face_nodes"].items() if node in nd]
    dist = {s: 0.5 * L(dep[s]) for s in src}
    heap = [(d, s) for s, d in dist.items()]; heapq.heapify(heap)
    while heap:
        du, u = heapq.heappop(heap)
        if du != dist.get(u) or du > maxd: continue
        for w in adj[u]:
            nd = du + 0.5 * (L(dep[u]) + L(dep[w]))
            if nd <= maxd and nd < dist.get(w, 1e18):
                dist[w] = nd; heapq.heappush(heap, (nd, w))
    return dist

# ---------- lineage machinery -------------------------------------------------
def members_at(view, evid, epoch):
    ls = view["lineage_snaps"].get(epoch, {})
    ev = tuple(evid)
    return sorted(f for f, lins in ls.items()
                  if ev in {tuple(l) for l in lins})

def snap_epochs(view):
    return sorted(view["snapshots"])

def nearest_snap(view, epoch, mode="le"):
    eps = snap_epochs(view)
    c = [e for e in eps if (e <= epoch if mode == "le" else e >= epoch)]
    return (max(c) if mode == "le" else min(c)) if c else None

def exact_extent(view, evid, epoch):
    snap = view["snapshots"].get(epoch)
    if snap is None: return Fraction(0)
    dep = snap["face_depth"]
    return sum((AREA(dep[f]) for f in members_at(view, evid, epoch) if f in dep),
               Fraction(0))

def tiebreak_key(view, evid, te):
    ext = exact_extent(view, evid, te)
    mem = members_at(view, evid, te)
    snap = view["snapshots"].get(te, {"face_depth": {}})
    maxdep = max((snap["face_depth"].get(f, -1) for f in mem), default=-1)
    # prereg 4.3: larger extent, earlier creation, deeper max depth, lowest evid
    return (-ext, evid[0], -maxdep, tuple(evid))

def formation_events(view):
    fe = view["formation_end"]
    return [e for e in view["relief_log"] if e["fired"] and e["epoch"] <= fe]

def candidate_A(view, te):
    evs = [e for e in formation_events(view) if e["created"]]
    if not evs: return None, "A_UNDEFINED_NO_RELIEF"
    last_ep = max(e["epoch"] for e in evs)
    finalists = [tuple(e["evid"]) for e in evs if e["epoch"] == last_ep]
    return min(finalists, key=lambda ev: tiebreak_key(view, ev, te)), None

def candidate_B(view, te):
    part = Counter()
    for e in formation_events(view):
        touched = set()
        for (_f, _t, _d, _df, lins) in e["removed"]:
            touched |= {tuple(l) for l in lins}
        touched.discard(tuple(e["evid"]))
        for l in touched: part[l] += 1
    if not part: return None, "B_UNDEFINED_NO_REUSE", 0
    mx = max(part.values())
    finalists = [l for l, c in part.items() if c == mx]
    return (min(finalists, key=lambda ev: tiebreak_key(view, ev, te)), None, mx)

# ---------- controls ----------------------------------------------------------
def signature(snap, faces):
    """Exact-type multiset + sorted depth list (prereg: type exact, depth +/-1)."""
    tps = sorted(snap["face_types"][f] for f in faces)
    dps = sorted(snap["face_depth"][f] for f in faces)
    return tps, dps

def locus_node(view, evid):
    ev = next(e for e in view["relief_log"] if tuple(e["evid"]) == tuple(evid))
    return ev["loci"][0] if ev["loci"] else None

def find_control(view, evid, te, cfg):
    """Deterministic exact-type, depth +/-1, metric-disjoint connected pseudo-locus.
    Scans snapshot epochs in [te, te + control_window]; first match wins."""
    mem0 = members_at(view, evid, te)
    if not mem0: return None
    node = locus_node(view, evid)
    win = [ep for ep in snap_epochs(view) if te <= ep <= te + cfg["control_window"]]
    excl = float(cfg["support_radius_dlstar"])
    for ep in win:
        snap = view["snapshots"][ep]
        mem = [f for f in members_at(view, evid, ep) if f in snap["face_depth"]] or \
              [f for f in mem0 if f in snap["face_depth"]]
        if not mem: continue
        want_t, want_d = signature(snap, mem)
        n = len(mem)
        adj = face_adjacency(snap)
        kc = max(snap["face_depth"][f] for f in mem)
        dist = face_dijkstra_from_node(snap, node, adj) if node is not None else {}
        lstar = L(kc)
        far = lambda f: dist.get(f, 1e18) / lstar > excl
        for start in sorted(snap["face_nodes"]):
            if snap["face_types"][start] != want_t[0] or not far(start): continue
            # deterministic BFS growth, type-multiset constrained
            need = Counter(want_t); sel = []
            q = deque([start]); seen = {start}
            while q and len(sel) < n:
                f = q.popleft()
                t = snap["face_types"][f]
                if need[t] > 0 and far(f):
                    need[t] -= 1; sel.append(f)
                    for w in sorted(adj[f]):
                        if w not in seen: seen.add(w); q.append(w)
            if len(sel) == n:
                st, sd = signature(snap, sel)
                if st == want_t and all(abs(a - b) <= cfg["depth_tolerance"]
                                        for a, b in zip(sd, want_d)):
                    return dict(epoch=ep, faces=sorted(sel))
    return None

def control_clean(view, ctrl, cfg):
    """Identity-based cleanliness: no fired relief event touches the control's
    face set within +/- clean_window epochs of alignment."""
    if ctrl is None: return False
    cf = set(ctrl["faces"]); ep0 = ctrl["epoch"]; w = cfg["clean_window"]
    for e in view["relief_log"]:
        if not e["fired"] or abs(e["epoch"] - ep0) > w: continue
        rm = {r[0] for r in e["removed"]}
        if (rm | set(e["created"])) & cf: return False
    return True

# ---------- support -----------------------------------------------------------
def support_count(view, node, cfg, lstar, epochs):
    """Number of snapshot epochs with >=1 frustrated face within d/ell* < radius.
    (Snapshot-lattice implementation of prereg gate S; see RUNBOOK freeze-point.)"""
    frus_by_ep = {d["epoch"]: set(d["frus"]) for d in view["frus_log"]}
    n = 0
    for ep in epochs:
        snap = view["snapshots"][ep]
        fr = frus_by_ep.get(ep, set()) & set(snap["face_depth"])
        if not fr or node is None: continue
        dist = face_dijkstra_from_node(snap, node,
                                       maxd=cfg["support_radius_dlstar"] * lstar * 1.01)
        if any(dist.get(f, 1e18) / lstar < cfg["support_radius_dlstar"] for f in fr):
            n += 1
    return n

# ---------- per-seed preflight ------------------------------------------------
def preflight_seed(view, cfg):
    te = nearest_snap(view, view["formation_end"], "le")
    tend = max(snap_epochs(view))
    out = dict(seed=view["seed"], clearance_ok=view["clearance_ok"],
               formation_end=view["formation_end"], te=te)
    if te is None or not view["clearance_ok"]:
        out["valid"] = False; return out
    out["valid"] = True
    a_ev, a_flag = candidate_A(view, te)
    b_res = candidate_B(view, te)
    b_ev, b_flag, b_reuse = b_res
    out["coincide"] = (a_ev is not None and a_ev == b_ev)
    win_epochs = [ep for ep in snap_epochs(view) if te <= ep <= tend]
    for name, ev, flag in (("A", a_ev, a_flag), ("B", b_ev, b_flag)):
        rec = dict(defined=ev is not None, flag=flag, evid=list(ev) if ev else None)
        if ev is not None:
            mem_end = members_at(view, ev, tend)
            rec["P"] = len(mem_end) > 0
            rec["U"] = b_reuse if name == "B" else None
            node = locus_node(view, ev)
            snap_te = view["snapshots"][te]
            mem_te = [f for f in members_at(view, ev, te) if f in snap_te["face_depth"]]
            kc = max((snap_te["face_depth"][f] for f in mem_te), default=0)
            lstar = L(kc)
            ctrl = find_control(view, ev, te, cfg)
            rec["M"] = ctrl is not None
            rec["control"] = ctrl
            rec["C"] = control_clean(view, ctrl, cfg)
            s_cand = support_count(view, node, cfg, lstar, win_epochs)
            rec["S_cand_snaps"] = s_cand
            if ctrl is not None:
                csnap = view["snapshots"][ctrl["epoch"]]
                cnode = min(min(csnap["face_nodes"][f]) for f in ctrl["faces"])
                rec["S_ctrl_snaps"] = support_count(view, cnode, cfg, lstar, win_epochs)
            else:
                rec["S_ctrl_snaps"] = 0
            thr = cfg["support_min_snaps"]
            rec["S"] = (s_cand >= thr) and (rec["S_ctrl_snaps"] >= thr)
        out[name] = rec
    return out

def main(cfgp, cache_dir, outp):
    full = json.loads(Path(cfgp).read_text(encoding="utf-8"))
    cfg = full["selection"]
    cfgh = hashlib.sha256(json.dumps(full, sort_keys=True).encode("utf-8")).hexdigest()[:8]
    rows = []
    for p in sorted(Path(cache_dir).glob("c26_seed*.pkl.gz")):
        view = load_whitelisted(p)
        if view.get("cfg_hash") != cfgh:
            sys.exit(f"SELECT ABORT: {p.name} was produced under a different "
                     f"config (cache {view.get('cfg_hash')} vs current {cfgh}). "
                     "Clear stale caches from the cache_dir and rerun the run stage.")
        rows.append(preflight_seed(view, cfg))
        print(f"selected seed {rows[-1]['seed']}: valid={rows[-1]['valid']}")
    Path(outp).write_text(json.dumps(rows, indent=1, default=str),
                          encoding="utf-8", newline="\n")
    print(f"WROTE {outp} ({len(rows)} seeds)")

if __name__ == "__main__":
    main(*sys.argv[1:4])
