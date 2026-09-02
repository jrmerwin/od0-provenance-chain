#!/usr/bin/env python3
"""Write R52_OUTPUT_MANIFEST.json (self-excluded, deterministic, no hand hashes)."""
import hashlib
import json
from pathlib import Path

PKG = Path(__file__).resolve().parent

FILES = [
    "OD0_R52_REPORT.md",
    "OD0_R52_RESULTS.json",
    "OD0_R52_COUNTEREXAMPLES.md",
    "R52_INPUT_LOCK.json",
    "R52_STRUCTURAL_THEOREMS.json",
    "R52_OBSERVABLE_INVENTORY.json",
    "R52_CLOSURE_LADDER.json",
    "R52_INTENSIVE_DYNAMICS.json",
    # auxiliary work products and pipeline sources
    "R52_EXACT_CERTIFICATES.json",
    "R52_SAMPLED_READOUT.json",
    "r52_exact.py",
    "r52_sampled.py",
    "r52_adjudication_data.py",
    "build_r52_outputs.py",
    "build_r52_input_lock.py",
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
        "schema": "OD0_R52_OUTPUT_MANIFEST_V1",
        "campaign": "OD0-R52",
        "package_version": "v0.1 (Claude Code executor)",
        "commit_A_short": "44f2197",
        "commit_B": "CREATED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE",
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "hand_produced_hashes": 0,
        "new_premises": 0,
        "sampled_files_labeled": True,
        "file_count": len(entries),
        "files": sorted(entries, key=lambda e: e["path"]),
        "self_excluded": True,
    }
    out = PKG / "R52_OUTPUT_MANIFEST.json"
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8", newline="\n")
    print("R52_OUTPUT_MANIFEST.json sha256 =", sha256_file(out))


if __name__ == "__main__":
    main()
