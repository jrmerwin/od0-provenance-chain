#!/usr/bin/env python3
# C26 firewall (C23 template).
# The eligibility/selection function receives ONLY whitelisted pre-outcome fields.
# This module is the sole legal loader for selection: it strips every blacklisted
# field from the run cache BEFORE the selector sees it. The selector must import
# load_whitelisted(); importing the raw cache in selection code is a protocol
# violation. The freeze manifest pins this file's hash.
#
# WHITELIST (prereg section 6):
#   - relief event log: identity and timing only (evid, epoch, fired, loci,
#     removed/created face records: id, type, depth, defect flag, lineage ids)
#   - frustrated-face availability log (ids per epoch; no magnitudes)
#   - lineage snapshots (fid -> lineage ids, per snapshot epoch)
#   - topology snapshots (face_nodes, face_types, face_depth, face_defect)
#   - seed, formation schedule timing, clearance timing flags
# BLACKLIST (no code path):
#   - epoch_log in its entirety (contains backlog, served_forced, served_vac,
#     deferred counts -- demand/service/backlog magnitudes)
#   - n_voided / n_tagged / wedge magnitudes
#   - anything from the C9 field pipeline
import gzip, pickle
from pathlib import Path

WHITELIST_TOP = ("schema", "seed", "config", "cfg_hash", "final_epoch", "formation_end",
                 "clearance_epoch", "clearance_ok",
                 "relief_log", "frus_log", "lineage_snaps", "snapshots")
EVENT_FIELDS = ("evid", "epoch", "fired", "loci", "removed", "created")

def load_whitelisted(cache_path):
    with gzip.open(Path(cache_path), "rb") as f:
        raw = pickle.load(f)
    assert raw.get("schema") == "c26_cache_v1", "unknown cache schema"
    view = {k: raw[k] for k in WHITELIST_TOP if k in raw}
    view["relief_log"] = [{k: e[k] for k in EVENT_FIELDS} for e in view["relief_log"]]
    # structural guarantee: no epoch_log, no served/backlog fields survive
    forbidden = {"epoch_log", "backlog", "served_forced", "served_vac",
                 "n_voided", "n_tagged", "wedge_removed", "pop_trig", "vac_demand"}
    assert not (set(view) & forbidden), "firewall breach: blacklisted top-level field"
    return view
