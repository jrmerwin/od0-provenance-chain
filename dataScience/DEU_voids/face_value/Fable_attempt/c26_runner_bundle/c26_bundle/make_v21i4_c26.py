#!/usr/bin/env python3
# PROJECT: DEU Work-Energy Campaign, Round C26 (dual-candidate structural preflight)
# PURPOSE: Derive rung1_v21i4_c26.py from the byte-pinned base rung1_v21_zeno.py
#          by anchored EXACT-STRING replacements. Adds PURE READS ONLY:
#            - material-lineage provenance (splits inherit, flips union,
#              relief contractions stamp the event lineage id)
#            - relief event log (identity and timing only: epoch, loci,
#              removed/created face records with type/depth/defect/lineage;
#              NO backlog magnitudes, NO n_voided)
#            - per-epoch frustrated-face id log (availability only)
#            - periodic + relief-epoch topology & lineage snapshots
#          No dynamics changes. No new RNG draws. Default-off kwargs preserve
#          the base trajectory bit-exactly (certified by certify.py 10/10 and
#          by the driver's shared-column identity gate with instruments ON).
# RULE:    Every replacement anchor must occur EXACTLY ONCE or the patcher aborts.
# ENCODING: explicit UTF-8 / LF everywhere (known dragon: Windows cp1252).
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

EDITS = [
# E-KW: add instrument kwargs (defaults preserve base behavior exactly)
("""def grow_native(*, final_epoch=100, seed=101, p_ext=0.75, m_defects=0,
                defect_inject_epoch=50, r_core=0.30, snapshot_final=True,
                spike_epoch=None, spike_ops=0,
                pulse_size=0, pulse_every=0, pulse_start=55, n_pulses=0):""",
 """def grow_native(*, final_epoch=100, seed=101, p_ext=0.75, m_defects=0,
                defect_inject_epoch=50, r_core=0.30, snapshot_final=True,
                spike_epoch=None, spike_ops=0,
                pulse_size=0, pulse_every=0, pulse_start=55, n_pulses=0,
                snap_every=0, snap_relief=False):"""),

# E-STATE: instrumentation state (pure containers)
("""    anchor_face = anchor_nodes = anchor_center_node = None
    backlog = 0; k_stitch = 0; rot = [0]""",
 """    anchor_face = anchor_nodes = anchor_center_node = None
    backlog = 0; k_stitch = 0; rot = [0]
    _c26_lin = {}; _c26_relief_log = []; _c26_frus_log = []; _c26_lin_snaps = {}"""),

# E-RM: drop lineage entry when a face is removed (bookkeeping only)
("""        active.discard(fid)
        del faces[fid], face_types[fid], face_depth[fid], face_defect[fid]""",
 """        active.discard(fid)
        del faces[fid], face_types[fid], face_depth[fid], face_defect[fid]
        _c26_lin.pop(fid, None)"""),

# E-SPLIT-A: capture parent lineage before removal
("""    def split_face(fid, *, forced=False, fdc=None):
        if fid not in active: return None
        old = sorted(faces[fid]); od = int(face_depth[fid])""",
 """    def split_face(fid, *, forced=False, fdc=None):
        if fid not in active: return None
        old = sorted(faces[fid]); od = int(face_depth[fid])
        _c26_plin = _c26_lin.get(fid, frozenset())"""),

# E-SPLIT-B: children inherit parent lineage
("""        _tp = [str(t) for t in rng.permutation(["S", "I", "G"])]
        for nd, ft in zip([(new, a, b), (new, a, c), (new, b, c)], _tp):
            add_face(nd, ft, od + 1, cd)""",
 """        _tp = [str(t) for t in rng.permutation(["S", "I", "G"])]
        for nd, ft in zip([(new, a, b), (new, a, c), (new, b, c)], _tp):
            _c26_cid = add_face(nd, ft, od + 1, cd)
            if _c26_plin: _c26_lin[_c26_cid] = _c26_plin"""),

# E-FLIP: flip products inherit the union of both parents' lineages
("""        d1, t1, df1 = face_depth[f1], face_types[f1], face_defect[f1]
        d2, t2, df2 = face_depth[f2], face_types[f2], face_defect[f2]
        remove_face(f1); remove_face(f2)
        add_face((a, c, d), t1, d1, df1); add_face((b, c, d), t2, d2, df2)
        return True""",
 """        d1, t1, df1 = face_depth[f1], face_types[f1], face_defect[f1]
        d2, t2, df2 = face_depth[f2], face_types[f2], face_defect[f2]
        _c26_ulin = _c26_lin.get(f1, frozenset()) | _c26_lin.get(f2, frozenset())
        remove_face(f1); remove_face(f2)
        _c26_g1 = add_face((a, c, d), t1, d1, df1); _c26_g2 = add_face((b, c, d), t2, d2, df2)
        if _c26_ulin:
            _c26_lin[_c26_g1] = _c26_ulin; _c26_lin[_c26_g2] = _c26_ulin
        return True"""),

# E-FRUS-INIT: per-epoch core-frustration capture slot (v21i3 idiom)
("""        served_f = served_v = deferred_f = 0; core_flips = 0; wedge_info = None""",
 """        served_f = served_v = deferred_f = 0; core_flips = 0; wedge_info = None; _c26_frus_core = []"""),

# E-FRUS-CORE: record core frustrated ids (availability only)
("""            frus = [f for f in a0 if f in core and is_frustrated(f, t0, n0)]""",
 """            frus = [f for f in a0 if f in core and is_frustrated(f, t0, n0)]
            _c26_frus_core = list(frus)"""),

# E-EV-INIT: allocate relief event id and identity buffers at trigger
("""                _nt=0; _coll=0""",
 """                _nt=0; _coll=0
                _c26_evid=(int(epoch), len(_c26_relief_log))
                _c26_rm=[]; _c26_cr=[]; _c26_loci=[]"""),

# E-EV-PAIR: record collapse locus and removed pair (identity/timing only)
("""                        _nt+=sum(1 for _f in (_f1,_f2) if face_defect.get(_f,False))
                        for _f in (_f1,_f2):
                            for _n in faces[_f]: _n2f[_n].discard(_f)
                            remove_face(_f)""",
 """                        _c26_loci.append(int(_a))
                        for _f in (_f1,_f2):
                            _c26_rm.append((int(_f), face_types[_f], int(face_depth[_f]),
                                            bool(face_defect[_f]), sorted(_c26_lin.get(_f, ()))))
                        _nt+=sum(1 for _f in (_f1,_f2) if face_defect.get(_f,False))
                        for _f in (_f1,_f2):
                            for _n in faces[_f]: _n2f[_n].discard(_f)
                            remove_face(_f)"""),

# E-EV-REWRITE-A: capture rewritten face's lineage and record its removal
("""                            _tp,_dp,_df=face_types[_f],face_depth[_f],face_defect[_f]
                            _od=_dist.get(_f)""",
 """                            _tp,_dp,_df=face_types[_f],face_depth[_f],face_defect[_f]
                            _od=_dist.get(_f)
                            _c26_fl=_c26_lin.get(_f, frozenset())
                            _c26_rm.append((int(_f), _tp, int(_dp), bool(_df), sorted(_c26_fl)))"""),

# E-EV-REWRITE-B: stamp event lineage on the contraction product
("""                            if len(_nnd)==3:
                                _g=add_face(_nnd,_tp,_dp,_df)
                                for _n in _nnd: _n2f[_n].add(_g)
                                if _od is not None: _dist[_g]=_od""",
 """                            if len(_nnd)==3:
                                _g=add_face(_nnd,_tp,_dp,_df)
                                _c26_lin[_g]=_c26_fl|{_c26_evid}; _c26_cr.append(int(_g))
                                for _n in _nnd: _n2f[_n].add(_g)
                                if _od is not None: _dist[_g]=_od"""),

# E-EV-APPEND: append the event record (no backlog, no n_voided)
("""                if _nt>0:
                    k_stitch+=1
                    wedge_info=dict(n_removed=2*_coll,n_tagged=_nt)
                    backlog=max(0,backlog-_nt)
                    stats["purge_collapses"]+=_coll""",
 """                if _nt>0:
                    k_stitch+=1
                    wedge_info=dict(n_removed=2*_coll,n_tagged=_nt)
                    backlog=max(0,backlog-_nt)
                    stats["purge_collapses"]+=_coll
                _c26_relief_log.append(dict(evid=_c26_evid, epoch=int(epoch),
                    fired=bool(_nt>0), loci=list(_c26_loci),
                    removed=list(_c26_rm), created=list(_c26_cr)))
                if snap_every and snap_relief and _nt>0:
                    record_snapshot(epoch)
                    _c26_lin_snaps[int(epoch)]={int(_f): sorted(_v)
                        for _f,_v in _c26_lin.items() if _v}"""),

# E-EPOCH-TAIL: frustration log + periodic snapshots, before the epoch_log append
("""        epoch_log.append(dict(epoch=epoch, gamma=gamma, core_faces=len(core),""",
 """        _c26_frus_log.append(dict(epoch=int(epoch),
            frus=sorted(set(_c26_frus_core) | set(frus_e))))
        if snap_every and (epoch % int(snap_every) == 0):
            record_snapshot(epoch)
            _c26_lin_snaps[int(epoch)]={int(_f): sorted(_v)
                for _f,_v in _c26_lin.items() if _v}
        epoch_log.append(dict(epoch=epoch, gamma=gamma, core_faces=len(core),"""),

# E-RETURN: ship instrumentation through stats (final lineage state included)
("""    if snapshot_final: record_snapshot(final_epoch)
    return CoherentStitchRun(stats=dict(stats, k_stitch=k_stitch),
                             spatial_snapshots=dict(snaps),
                             epoch_log=pd.DataFrame(epoch_log))""",
 """    if snapshot_final: record_snapshot(final_epoch)
    _c26_lin_snaps[int(final_epoch)]={int(_f): sorted(_v)
        for _f,_v in _c26_lin.items() if _v}
    return CoherentStitchRun(stats=dict(stats, k_stitch=k_stitch,
                                 c26=dict(relief_log=_c26_relief_log,
                                          frus_log=_c26_frus_log,
                                          lineage_snaps=_c26_lin_snaps)),
                             spatial_snapshots=dict(snaps),
                             epoch_log=pd.DataFrame(epoch_log))"""),
]

HEADER = '''"""rung1_v21i4_c26 -- INSTRUMENTED VARIANT (Round C26 preflight).
Derived from rung1_v21_zeno.py (SHA-256 %s)
by make_v21i4_c26.py via anchored exact-string replacements.
PURE READS ONLY: lineage provenance, relief identity/timing log, frustration
availability log, periodic snapshots. No dynamics changes, no new RNG draws.
Certification required before use: certify.py 10/10 bit-exact AND the driver
shared-column identity gate with instruments enabled.
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
    dst = base.parent / "rung1_v21i4_c26.py"
    dst.write_text(out, encoding="utf-8", newline="\n")
    print(f"WROTE {dst}")
    print(f"VARIANT SHA-256 {hashlib.sha256(out.encode('utf-8')).hexdigest()}")

if __name__ == "__main__":
    main()
