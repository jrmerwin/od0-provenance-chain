#!/usr/bin/env python3
"""OD0-R60 Commit A: input lock. All hashes in-process."""
import hashlib
import json
import re
from pathlib import Path

PKG = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256((PKG / p).read_bytes()).hexdigest()


stamp = json.loads((PKG / "R59_PROVENANCE_STAMP.json").read_text(encoding="utf-8"))
pkg_text = (PKG / "OD0_CLAUDE_CODE_PACKAGE_R60_M7_LAPSE_CLOCK_EPOCH_LAWS_v0_1.md"
            ).read_text(encoding="utf-8")

# extract targets L1-L8 verbatim from the package
m = re.search(r"# 4\. Targets \(frozen at Commit A\)\n(.*?)\n---",
              pkg_text, re.S)
targets_verbatim = m.group(1).strip()

manifest_ok = (stamp["output_manifest_sha256"] ==
               sha("R59_OUTPUT_MANIFEST.json"))

lock = {
    "schema": "R60_INPUT_LOCK_V1",
    "round": "OD0-R60",
    "package": "OD0_CLAUDE_CODE_PACKAGE_R60_M7_LAPSE_CLOCK_EPOCH_LAWS_v0_1.md",
    "package_sha256": sha(
        "OD0_CLAUDE_CODE_PACKAGE_R60_M7_LAPSE_CLOCK_EPOCH_LAWS_v0_1.md"),
    "r59_stamp_pin": {
        "stamp_sha256": sha("R59_PROVENANCE_STAMP.json"),
        "commit_A": stamp["commit_A_prereg"],
        "commit_B": stamp["commit_B_outputs"],
        "output_manifest_sha256": stamp["output_manifest_sha256"],
        "manifest_match_verified": manifest_ok},
    "targets_L1_L8_verbatim": targets_verbatim,
    "seals": {"BELL2_opened": False,
              "H1": "spent (R54)", "H2": "spent (R57)",
              "H3": {"parsed": False}, "H4": {"parsed": False},
              "H5": {"parsed": False}},
    "declarations": [
        "targets frozen verbatim before any computation",
        "no external referent; vocabulary of the package notes only",
        "no rate-in-process-time statement enters the prediction set",
        "no reinterpretation of Phi or the clock",
        "asymptotics carry finite-n bounds or are labeled CONJECTURE",
        "no readout enters a theorem",
        "hash hygiene: all hashes in-process",
        "M7 prediction set sealed and hashed at Commit B, target-blind"],
}
out = PKG / "R60_INPUT_LOCK.json"
out.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n",
               encoding="utf-8", newline="\n")
print("manifest_match_verified:", manifest_ok)
print("lock sha256:", sha("R60_INPUT_LOCK.json"))
