#!/usr/bin/env python3
"""Write R51_OUTPUT_MANIFEST.json (self-excluded, deterministic, no hand hashes)."""
import hashlib
import json
from pathlib import Path

PKG = Path(__file__).resolve().parent

FILES = [
    "OD0_R51_REPORT.md",
    "OD0_R51_RESULTS.json",
    "OD0_R51_COUNTEREXAMPLES.md",
    "R51_INPUT_LOCK.json",
    "R51_SELECTOR_SOURCE_STATUS.json",
    "R51_THROTTLE_CLASS_ADJUDICATION.json",
    "R51_SURVIVOR_DYNAMICS_READOUT.json",
    # auxiliary work products and pipeline sources
    "R51_EXACT_CERTIFICATES.json",
    "r51_exact.py",
    "r51_adjudication_data.py",
    "build_r51_outputs.py",
    "build_r51_input_lock.py",
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
        "schema": "OD0_R51_OUTPUT_MANIFEST_V1",
        "campaign": "OD0-R51",
        "package_version": "v0.1 (Claude Code executor)",
        "commit_A_short": "28f50e5",
        "commit_B": "CREATED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE",
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "hand_produced_hashes": 0,
        "parameters_introduced": 0,
        "premises_adopted": 0,
        "premises_stated": ["TG1 (with V~X identification)", "carried: CO1, RO1, SV-pool"],
        "file_count": len(entries),
        "files": sorted(entries, key=lambda e: e["path"]),
        "self_excluded": True,
    }
    out = PKG / "R51_OUTPUT_MANIFEST.json"
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8", newline="\n")
    print("R51_OUTPUT_MANIFEST.json sha256 =", sha256_file(out))


if __name__ == "__main__":
    main()
