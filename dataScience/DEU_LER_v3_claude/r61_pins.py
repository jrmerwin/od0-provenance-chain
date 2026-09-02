#!/usr/bin/env python3
"""OD0-R61 Part 3: artifact pinning. Names and byte-hashes ONLY - no
scientific content is parsed. Deterministic."""
import hashlib
import json
import subprocess
from pathlib import Path

PKG = Path(__file__).resolve().parent
DS = Path("c:/Users/merwijas/dataScience")


def fsha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


manifest = json.loads((PKG / "R48_HOLDOUT_MANIFEST.json").read_text(
    encoding="utf-8"))

pins = {}
for tag in ("H3", "H4"):
    rows = []
    present = missing = changed = 0
    nonpaper_present = 0
    for it in manifest["items_by_tag"][tag]:
        p = Path(it["path"])
        row = {"path": it["path"],
               "manifest_sha256": it.get("sha256")}
        if not p.exists():
            row["status"] = "MISSING"
            missing += 1
        else:
            cur = fsha(p) if p.is_file() else "DIRECTORY"
            row["current_sha256"] = cur
            if it.get("sha256") and cur == it["sha256"]:
                row["status"] = "PINNED_UNCHANGED"
                present += 1
            elif it.get("sha256") and cur not in (
                    it["sha256"], "DIRECTORY"):
                row["status"] = "PRESENT_HASH_CHANGED"
                changed += 1
            else:
                row["status"] = "PRESENT"
                present += 1
            if p.suffix.lower() not in (".pdf", ".tex", ".md", ".txt"):
                nonpaper_present += 1
        rows.append(row)
    pins[tag] = {
        "items": rows,
        "summary": {"present": present, "missing": missing,
                    "hash_changed": changed,
                    "non_manuscript_artifacts_present": nonpaper_present,
                    "paper_only": nonpaper_present == 0}}

# DEU_voids source line: last commit touching the tracked directory
voids_commit = subprocess.run(
    ["git", "log", "-1", "--format=%H", "--", "dataScience/DEU_voids"],
    cwd=DS.parent, capture_output=True, text=True, check=True
).stdout.strip()
head_commit = subprocess.run(
    ["git", "rev-parse", "HEAD"], cwd=DS.parent, capture_output=True,
    text=True, check=True).stdout.strip()

# v31l-v31o generating sources: filename search only
v31 = {}
for tagname in ("v31l", "v31m", "v31n", "v31o"):
    hits = sorted(str(q.relative_to(DS)).replace("\\", "/")
                  for q in DS.rglob(f"*{tagname}*") if q.is_file())
    v31[tagname] = {"found": hits, "status":
                    "FOUND" if hits else "MISSING"}

out = {
    "schema": "R61_ARTIFACT_PINS_V1",
    "note": "Byte-level pinning only; no scientific content parsed; "
            "H3/H4 remain sealed.",
    "H3": pins["H3"], "H4": pins["H4"],
    "deu_voids_source_line": {
        "last_commit_touching_DEU_voids": voids_commit,
        "repo_HEAD_at_pinning": head_commit,
        "status": "SOURCE_CONFLICT with the manuscript per R48; "
                  "recorded, unresolved"},
    "v31_generating_sources": v31,
}
(PKG / "R61_ARTIFACT_PINS.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n",
    encoding="utf-8", newline="\n")
for tag in ("H3", "H4"):
    s = pins[tag]["summary"]
    print(tag, s)
print("DEU_voids commit:", voids_commit[:12])
print("v31:", {k: v["status"] for k, v in v31.items()})
