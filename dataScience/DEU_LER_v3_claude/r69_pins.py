#!/usr/bin/env python3
"""OD0-R69 Part 2: H5 artifact pinning. Names and byte-hashes ONLY -
no scientific content parsed. Deterministic."""
import hashlib
import json
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

rows = []
present = missing = changed = 0
nonpaper = 0
families = {}
for it in manifest["items_by_tag"]["H5"]:
    p = Path(it["path"])
    row = {"path": it["path"], "manifest_sha256": it.get("sha256")}
    if not p.exists():
        row["status"] = "MISSING"
        missing += 1
    else:
        cur = fsha(p) if p.is_file() else "DIRECTORY"
        row["current_sha256"] = cur
        if it.get("sha256") and cur == it["sha256"]:
            row["status"] = "PINNED_UNCHANGED"
            present += 1
        elif it.get("sha256") and cur not in (it["sha256"],
                                              "DIRECTORY"):
            row["status"] = "PRESENT_HASH_CHANGED"
            changed += 1
        else:
            row["status"] = "PRESENT"
            present += 1
        if p.suffix.lower() not in (".pdf", ".tex", ".md", ".txt"):
            nonpaper += 1
    rows.append(row)

# de Sitter closure / density artifacts by filename (names only)
searches = {}
for tag in ("de_sitter", "desitter", "sitter", "closure",
            "rho_c", "carrier_density"):
    hits = sorted(str(q.relative_to(DS)).replace("\\", "/")
                  for q in DS.rglob(f"*{tag}*") if q.is_file())[:20]
    searches[tag] = {"found_count": len(hits), "first_hits": hits[:8]}

out = {
    "schema": "R69_ARTIFACT_PINS_V1",
    "note": "Byte-level pinning only; no scientific content parsed; "
            "H5 remains sealed.",
    "H5": {"items": rows,
           "summary": {"present": present, "missing": missing,
                       "hash_changed": changed,
                       "non_manuscript_artifacts_present": nonpaper,
                       "paper_only": nonpaper == 0}},
    "filename_searches": searches,
}
(PKG / "R69_ARTIFACT_PINS.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n",
    encoding="utf-8", newline="\n")
print("H5:", out["H5"]["summary"])
for k, v in searches.items():
    print(k, v["found_count"])
