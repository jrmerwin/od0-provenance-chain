#!/usr/bin/env python3
"""Write R49_OUTPUT_MANIFEST.json (self-excluded, deterministic)."""
import hashlib
import json
from pathlib import Path

PKG = Path(__file__).resolve().parent

FILES = [
    "OD0_R49_REPORT.md",
    "OD0_R49_RESULTS.json",
    "OD0_R49_COUNTEREXAMPLES.md",
    "R49_INPUT_LOCK.json",
    "R49_ADJUNCTION_OPPORTUNITY_CLASSIFICATION.json",
    "R49_RECORD_OPPORTUNITY_CLASSIFICATION.json",
    "R49_OPPORTUNITY_OBSTRUCTION.json",
    # auxiliary work products and pipeline sources
    "R49_EXACT_CERTIFICATES.json",
    "r49_exact.py",
    "r49_adjudication_data.py",
    "build_r49_outputs.py",
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
        "schema": "OD0_R49_OUTPUT_MANIFEST_V1",
        "campaign": "OD0-R49",
        "package_version": "v0.1 (Claude Code executor)",
        "commit_A": "4946e4e (full hash resolvable in repo; no expansion "
                    "written here - see R48 erratum discipline)",
        "commit_B": "CREATED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE",
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "premises_stated_not_selected": ["CO1", "RO1"],
        "file_count": len(entries),
        "files": sorted(entries, key=lambda e: e["path"]),
        "self_excluded": True,
    }
    out = PKG / "R49_OUTPUT_MANIFEST.json"
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8", newline="\n")
    print("R49_OUTPUT_MANIFEST.json sha256 =", sha256_file(out))


if __name__ == "__main__":
    main()
