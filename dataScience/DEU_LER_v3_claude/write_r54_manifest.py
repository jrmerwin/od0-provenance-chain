#!/usr/bin/env python3
"""Write R54_OUTPUT_MANIFEST.json (self-excluded) and, after Commit B,
R54_PROVENANCE_STAMP.json is written by write_r54_stamp.py."""
import hashlib
import json
from pathlib import Path

PKG = Path(__file__).resolve().parent

FILES = [
    "OD0_R54_REPORT.md",
    "OD0_R54_RESULTS.json",
    "OD0_R54_COUNTEREXAMPLES.md",
    "R54_INPUT_LOCK.json",
    "R54_H1_EXTRACTION.json",
    "R54_MAP_TABLE_AND_ADJUDICATION.json",
    "R54_POST_OPENING_READOUT.json",
    "R52_PROVENANCE_STAMP.json",
    "R53_PROVENANCE_STAMP.json",
    "r54_adjudication_data.py",
    "r54_quarantine.py",
    "build_r54_outputs.py",
    "build_r54_prelude.py",
]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    entries = [{"path": n, "bytes": (PKG / n).stat().st_size,
                "sha256": sha256_file(PKG / n)} for n in FILES]
    manifest = {
        "schema": "OD0_R54_OUTPUT_MANIFEST_V1",
        "campaign": "OD0-R54",
        "package_version": "v0.1 (Claude Code executor)",
        "commit_stamps_short": "bd21aca",
        "commit_A_short": "45eb08c",
        "commit_B": "CREATED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE_SEE_STAMP",
        "BELL2_opened": False,
        "h2_h5_sentinels_parsed": False,
        "hand_produced_hashes": 0,
        "file_count": len(entries),
        "files": sorted(entries, key=lambda e: e["path"]),
        "self_excluded": True,
    }
    out = PKG / "R54_OUTPUT_MANIFEST.json"
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8", newline="\n")
    print("R54_OUTPUT_MANIFEST.json sha256 =", sha256_file(out))


if __name__ == "__main__":
    main()
