#!/usr/bin/env python3
# PROJECT: DEU Work-Energy Campaign, compiler track, Round B0
# PURPOSE: Derive rung1_v21i5_b0.py from the byte-pinned base rung1_v21_zeno.py.
#          PURE READS ONLY, per the B0 instrument spec:
#            - PRE-SERVICE demand: full frustrated-face census taken from the
#              epoch-START snapshot (declared-measure timing rule; the C17/C16
#              and unification-6.1 timing failures are the controlling precedents)
#            - service attributed AT EXECUTION: split_vac / split_forced /
#              split_ext / flip / relief (pair excisions only; contraction
#              rewrites are re-added and are NOT counted as service)
#            - region assignment from topology+depth alone: P (pocket: connected
#              component of faces with depth >= kvac + b0_kpocket containing the
#              anchor), B (depth-contrast interface), X (rest)
#            - weighted radial shells from the anchor (width b0_shellw, cap
#              b0_rmax) for the support-matched vacuum baseline
#            - everything logged as EXACT depth histograms: Counter keyed by
#              (region, shell, depth) or (kind, region, shell, depth); analysis
#              reconstitutes exact sums with Fraction(1, 3**k). No floats stored.
#          No dynamics changes. No new RNG draws. b0_log=False (default) is
#          bit-identical to base; b0_log=True adds reads only.
import hashlib, sys
from pathlib import Path

BASE_SHA256 = "8af1add97e9193df1f1a09acd0f4dc16a2eb1c2fc75e75fc24559f546b5c1a02"
HERE = Path(__file__).resolve().parent

def find_base():
    for cand in [HERE / "rung1_v21_zeno.py",
                 HERE.parent / "generative-ledger" / "engines" / "rung1_v21_zeno.py",
                 HERE / ".." / "engines" / "rung1_v21_zeno.py",
                 Path("engines") / "rung1_v21_zeno.py"]:
        cand = Path(cand)
        if cand.exists():
            return cand
    sys.exit("PATCHER ABORT: base engine rung1_v21_zeno.py not found")

REGION_BLOCK = '''        a0, t0, d0, f0, n0, df0 = snapshot_raw()
        core, gamma = core_partition()
        _b0_reg = {}; _b0_shell = {}
        if b0_log:
            _b0_kv = Counter(d0[f] for f in a0).most_common(1)[0][0] if a0 else 0
            _b0_deep = {f for f in a0 if d0[f] >= _b0_kv + int(b0_kpocket)}
            _b0_pock = set()
            if anchor_center_node is not None and _b0_deep:
                _b0_srcp = [f for f in a0 if anchor_center_node in f0[f] and f in _b0_deep]
                if not _b0_srcp and anchor_nodes:
                    _b0_srcp = [f for f in _b0_deep if f0[f] & set(anchor_nodes)]
                _b0_q = deque(_b0_srcp); _b0_pock = set(_b0_srcp)
                while _b0_q:
                    _b0_u = _b0_q.popleft()
                    for _b0_w in n0.get(_b0_u, ()):
                        if _b0_w in _b0_deep and _b0_w not in _b0_pock:
                            _b0_pock.add(_b0_w); _b0_q.append(_b0_w)
            _b0_bnd = set()
            for _b0_f in a0:
                _b0_inp = _b0_f in _b0_pock
                for _b0_w in n0.get(_b0_f, ()):
                    if ((_b0_w in _b0_pock) != _b0_inp
                            and abs(d0[_b0_f] - d0[_b0_w]) >= 1):
                        _b0_bnd.add(_b0_f); break
            for _b0_f in a0:
                _b0_reg[_b0_f] = ("B" if _b0_f in _b0_bnd
                                  else ("P" if _b0_f in _b0_pock else "X"))
            if anchor_center_node is not None:
                _b0_L = lambda _k: (3.0 ** -0.5) ** _k
                _b0_src = [f for f in a0 if anchor_center_node in f0[f]]
                _b0_dist = {s: 0.5 * _b0_L(d0[s]) for s in _b0_src}
                _b0_hp = [(d, s) for s, d in _b0_dist.items()]; heapq.heapify(_b0_hp)
                while _b0_hp:
                    _b0_du, _b0_u = heapq.heappop(_b0_hp)
                    if _b0_du != _b0_dist.get(_b0_u) or _b0_du > float(b0_rmax): continue
                    for _b0_w in n0.get(_b0_u, ()):
                        _b0_nd = _b0_du + 0.5 * (_b0_L(d0[_b0_u]) + _b0_L(d0[_b0_w]))
                        if _b0_nd <= float(b0_rmax) and _b0_nd < _b0_dist.get(_b0_w, 1e18):
                            _b0_dist[_b0_w] = _b0_nd; heapq.heappush(_b0_hp, (_b0_nd, _b0_w))
                for _b0_f in a0:
                    _b0_d = _b0_dist.get(_b0_f)
                    _b0_shell[_b0_f] = (int(_b0_d / float(b0_shellw))
                                        if _b0_d is not None else -1)
            _b0_ep = dict(epoch=int(epoch), kvac=int(_b0_kv),
                          pocket_faces=len(_b0_pock), boundary_faces=len(_b0_bnd),
                          frus=Counter(), area=Counter(), served=Counter())
            for _b0_f in a0:
                _b0_key = (_b0_reg[_b0_f], _b0_shell.get(_b0_f, -1), int(d0[_b0_f]))
                _b0_ep["area"][_b0_key] += 1
                if is_frustrated(_b0_f, t0, n0):
                    _b0_ep["frus"][_b0_key] += 1
            _b0_cur[0] = _b0_ep'''

EDITS = [
# E-KW: instrument kwargs (defaults preserve base behavior exactly)
("""def grow_native(*, final_epoch=100, seed=101, p_ext=0.75, m_defects=0,
                defect_inject_epoch=50, r_core=0.30, snapshot_final=True,
                spike_epoch=None, spike_ops=0,
                pulse_size=0, pulse_every=0, pulse_start=55, n_pulses=0):""",
 """def grow_native(*, final_epoch=100, seed=101, p_ext=0.75, m_defects=0,
                defect_inject_epoch=50, r_core=0.30, snapshot_final=True,
                spike_epoch=None, spike_ops=0,
                pulse_size=0, pulse_every=0, pulse_start=55, n_pulses=0,
                b0_log=False, b0_rmax=0.6, b0_kpocket=2, b0_shellw=0.05):"""),

# E-STATE: log containers + the service recorder closure
("""    anchor_face = anchor_nodes = anchor_center_node = None
    backlog = 0; k_stitch = 0; rot = [0]""",
 """    anchor_face = anchor_nodes = anchor_center_node = None
    backlog = 0; k_stitch = 0; rot = [0]
    _b0_log = []; _b0_cur = [None]; _b0_reg = {}; _b0_shell = {}
    def _b0_serve(kind, fid, dep):
        if not b0_log or _b0_cur[0] is None or dep is None: return
        _b0_cur[0]["served"][(str(kind), _b0_reg.get(fid, "X"),
                              _b0_shell.get(fid, -1), int(dep))] += 1"""),

# E-EPOCH-HEAD: region/shell assignment + pre-service demand census
("""        a0, t0, d0, f0, n0, df0 = snapshot_raw()
        core, gamma = core_partition()""",
 REGION_BLOCK),

# E-SERVE-F: forced split, depth captured pre-split
("""                    if ti >= len(tagged):
                        deferred_f += 1; continue
                    if split_face(tagged[ti], forced=True, fdc=True) is not None:
                        served_f += 1; cap -= 1""",
 """                    if ti >= len(tagged):
                        deferred_f += 1; continue
                    _b0_fid = tagged[ti]; _b0_dep = face_depth.get(_b0_fid)
                    if split_face(_b0_fid, forced=True, fdc=True) is not None:
                        served_f += 1; cap -= 1
                        _b0_serve("split_forced", _b0_fid, _b0_dep)"""),

# E-SERVE-V: core vacuum split
("""                else:
                    if fid in active and split_face(fid) is not None:
                        served_v += 1; cap -= 1""",
 """                else:
                    _b0_dep = face_depth.get(fid)
                    if fid in active and split_face(fid) is not None:
                        served_v += 1; cap -= 1
                        _b0_serve("split_vac", fid, _b0_dep)"""),

# E-SERVE-CFLIP: core flips, parent pair captured pre-flip
("""                rng.shuffle(edges)
                for e in edges:
                    if cap <= 0: break
                    if try_flip(e): core_flips += 1; cap -= 1""",
 """                rng.shuffle(edges)
                for e in edges:
                    if cap <= 0: break
                    _b0_pf = ([(_bf, face_depth[_bf]) for _bf in edge_to_faces.get(e, ())]
                              if b0_log else [])
                    if try_flip(e):
                        core_flips += 1; cap -= 1
                        for _bf, _bd in _b0_pf: _b0_serve("flip", _bf, _bd)"""),

# E-SERVE-RELIEF: pair excisions only (rewrites are re-added, not service)
("""                        _nt+=sum(1 for _f in (_f1,_f2) if face_defect.get(_f,False))""",
 """                        for _f in (_f1,_f2):
                            _b0_serve("relief", _f, face_depth.get(_f))
                        _nt+=sum(1 for _f in (_f1,_f2) if face_defect.get(_f,False))"""),

# E-SERVE-EXT: exterior frustrated splits
("""            rng.shuffle(frus_e)
            for fid in frus_e[:ebud]:
                if fid in active and split_face(fid) is not None:
                    norm_e += 1; ebud -= 1""",
 """            rng.shuffle(frus_e)
            for fid in frus_e[:ebud]:
                _b0_dep = face_depth.get(fid)
                if fid in active and split_face(fid) is not None:
                    norm_e += 1; ebud -= 1
                    _b0_serve("split_ext", fid, _b0_dep)"""),

# E-SERVE-EFLIP: exterior flips
("""            rng.shuffle(edges)
            for e in edges[:min(len(edges), 4000)]:
                if ebud <= 0: break
                if try_flip(e): ext_flips += 1; ebud -= 1""",
 """            rng.shuffle(edges)
            for e in edges[:min(len(edges), 4000)]:
                if ebud <= 0: break
                _b0_pf = ([(_bf, face_depth[_bf]) for _bf in edge_to_faces.get(e, ())]
                          if b0_log else [])
                if try_flip(e):
                    ext_flips += 1; ebud -= 1
                    for _bf, _bd in _b0_pf: _b0_serve("flip", _bf, _bd)"""),

# E-EPOCH-TAIL: flush the epoch record
("""        epoch_log.append(dict(epoch=epoch, gamma=gamma, core_faces=len(core),""",
 """        if b0_log and _b0_cur[0] is not None:
            _b0_e = _b0_cur[0]
            _b0_log.append(dict(epoch=_b0_e["epoch"], kvac=_b0_e["kvac"],
                pocket_faces=_b0_e["pocket_faces"],
                boundary_faces=_b0_e["boundary_faces"],
                frus=dict(_b0_e["frus"]), area=dict(_b0_e["area"]),
                served=dict(_b0_e["served"])))
            _b0_cur[0] = None
        epoch_log.append(dict(epoch=epoch, gamma=gamma, core_faces=len(core),"""),

# E-RETURN: ship the log through stats
("""    if snapshot_final: record_snapshot(final_epoch)
    return CoherentStitchRun(stats=dict(stats, k_stitch=k_stitch),
                             spatial_snapshots=dict(snaps),
                             epoch_log=pd.DataFrame(epoch_log))""",
 """    if snapshot_final: record_snapshot(final_epoch)
    return CoherentStitchRun(stats=dict(stats, k_stitch=k_stitch,
                                        b0=dict(log=_b0_log)),
                             spatial_snapshots=dict(snaps),
                             epoch_log=pd.DataFrame(epoch_log))"""),
]

HEADER = '''"""rung1_v21i5_b0 -- INSTRUMENTED VARIANT (Round B0, compiler track).
Derived from rung1_v21_zeno.py (SHA-256 %s)
by make_v21i5_b0.py via anchored exact-string replacements.
PURE READS ONLY: pre-service demand census, execution-attributed service by
kind, topology+depth region assignment (P/B/X), weighted radial shells,
exact depth-histogram logging. No dynamics changes, no new RNG draws.
Certification required before use: certify.py 10/10 bit-exact AND the driver
shared-column identity gate with b0_log=True.
"""
''' % BASE_SHA256

def main():
    base = find_base()
    src = base.read_text(encoding="utf-8")
    got = hashlib.sha256(src.encode("utf-8")).hexdigest()
    if got != BASE_SHA256:
        sys.exit(f"PATCHER ABORT: base SHA mismatch\n  expected {BASE_SHA256}\n  got      {got}")
    out = src
    for i, (old, new) in enumerate(EDITS):
        n = out.count(old)
        if n != 1:
            sys.exit(f"PATCHER ABORT: edit {i} anchor occurs {n} times (need exactly 1)")
        out = out.replace(old, new)
    out = HEADER + out
    dst = base.parent / "rung1_v21i5_b0.py"
    dst.write_text(out, encoding="utf-8", newline="\n")
    print(f"WROTE {dst}")
    print(f"VARIANT SHA-256 {hashlib.sha256(out.encode('utf-8')).hexdigest()}")

if __name__ == "__main__":
    main()
