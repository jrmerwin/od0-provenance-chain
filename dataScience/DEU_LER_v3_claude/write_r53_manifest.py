#!/usr/bin/env python3
"""Write R53_OUTPUT_MANIFEST.json (self-excluded, deterministic, no hand hashes)."""
import hashlib
import json
from pathlib import Path

PKG = Path(__file__).resolve().parent

FILES = [
    "OD0_R53_REPORT.md",
    "OD0_R53_RESULTS.json",
    "OD0_R53_COUNTEREXAMPLES.md",
    "R53_INPUT_LOCK.json",
    "R53_COST_THEOREM.json",
    "R53_GROWTH_LAW.json",
    "R53_MATURATION_FILTRATION.json",
    "R53_READOUTS.json",
    "R53_R54_COMPARISON_PROTOCOL.json",
    # auxiliary work products and pipeline sources
    "R53_EXACT_CERTIFICATES.json",
    "R53_SAMPLED_READOUT.json",
    "r53_exact.py",
    "r53_sampled.py",
    "r53_adjudication_data.py",
    "build_r53_outputs.py",
    "build_r53_input_lock.py",
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
        "schema": "OD0_R53_OUTPUT_MANIFEST_V1",
        "campaign": "OD0-R53",
        "package_version": "v0.1 (Claude Code executor)",
        "commit_A_short": "33c1782",
        "commit_B": "CREATED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE",
        "BELL2_opened": False,
        "historical_numerical_content_parsed": False,
        "hand_produced_hashes": 0,
        "new_premises": 0,
        "r54_protocol_frozen": True,
        "file_count": len(entries),
        "files": sorted(entries, key=lambda e: e["path"]),
        "self_excluded": True,
    }
    out = PKG / "R53_OUTPUT_MANIFEST.json"
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8", newline="\n")
    print("R53_OUTPUT_MANIFEST.json sha256 =", sha256_file(out))


if __name__ == "__main__":
    main()
