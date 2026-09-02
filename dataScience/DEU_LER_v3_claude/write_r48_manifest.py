#!/usr/bin/env python3
"""Write R48_OUTPUT_MANIFEST.json: SHA-256 of every R48 output artifact.

Self-excluded (the manifest does not contain its own hash), matching the
R47 manifest convention. Deterministic: sorted keys, LF newlines.
"""
import hashlib
import json
from pathlib import Path

PKG = Path(__file__).resolve().parent

FILES = [
    # the ten required outputs (manifest itself self-excluded)
    "OD0_R48_REPORT.md",
    "OD0_R48_RESULTS.json",
    "OD0_R48_COUNTEREXAMPLES.md",
    "R48_INPUT_LOCK.json",
    "R48_MODEL_FAMILY_GENEALOGY.json",
    "R48_GM_LG_ADMISSIBILITY_MATRIX.json",
    "R48_MATURATION_FIELD_INVENTORY.json",
    "R48_CCP1_EPOCH_SCOPE_CERTIFICATE.json",
    "R48_HOLDOUT_MANIFEST.json",
    # conditional output (no family passed GM1-12)
    "R48_OBSTRUCTION_THEOREM.json",
    # auxiliary work products
    "R48_CHAIN_VERIFICATION.json",
    "R48_CENSUS_GROUPS_RAW.json",
    # pipeline sources (pinned for reproducibility)
    "verify_pinned_chain.py",
    "build_r48_input_lock.py",
    "r48_adjudication_data.py",
    "build_r48_outputs.py",
]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    entries = []
    for name in FILES:
        p = PKG / name
        entries.append({"path": name, "bytes": p.stat().st_size,
                        "sha256": sha256_file(p)})
    manifest = {
        "schema": "OD0_R48_OUTPUT_MANIFEST_V1",
        "campaign": "OD0-R48",
        "package_version": "v0.2 (Claude Code executor)",
        "commit_A": "244e61a1b7f0272660ac549592a453f19d1035eb",
        "commit_B": "CREATED_AFTER_SELF_EXCLUDED_MANIFEST_WRITE",
        "BELL2_scientific_content_opened": False,
        "historical_numerical_content_parsed": False,
        "new_premises": 0,
        "file_count": len(entries),
        "files": sorted(entries, key=lambda e: e["path"]),
        "self_excluded": True,
    }
    out = PKG / "R48_OUTPUT_MANIFEST.json"
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8", newline="\n")
    print("R48_OUTPUT_MANIFEST.json sha256 =", sha256_file(out))


if __name__ == "__main__":
    main()
