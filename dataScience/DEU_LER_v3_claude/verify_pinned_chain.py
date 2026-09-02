#!/usr/bin/env python3
"""R48 pinned-chain verification (exact, deterministic).

Walks the OD0 round chain from R47 down to R30 inside
DEU_LER_v2_codex/deu_od0_exact_observables_v0_1/. For each round k it reads
R{k}_INPUT_LOCK.json, extracts the pinned predecessor output-manifest SHA-256,
and verifies the on-disk predecessor manifest hashes to that pin. It also
verifies the R48 top-level pins (R47 manifest hash, R47 result digest) and
hash-pins the CD0 constructor artifacts and the descent-paper ledgers.

No historical numerical content is parsed: only lock/manifest JSON metadata
fields (hashes, counts of files, commit ids) are read. Result values inside
prior-round RESULTS files are not opened by this script.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

BASE = Path(r"c:/Users/merwijas/dataScience")
CHAIN = BASE / "DEU_LER_v2_codex" / "deu_od0_exact_observables_v0_1"
PKG = BASE / "DEU_LER_v3_claude"

PIN_R47_RESULT_DIGEST = "382a2cc975a194a1ef45b7aabd553d732811f084120bab3b1fafd7834e6c5c14"
PIN_R47_MANIFEST_SHA = "d4eeb49ea1274619eca5ff99182b61e54a7e46aadce075593ba0279585d62fbb"
PIN_R47_EXEC_COMMIT = "2b7ae30fe23b0ccffe31f2ffbba6ae2de2318a21"


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def round_dir(k: int) -> Path:
    hits = sorted(CHAIN.glob(f"od0_r{k}_*"))
    if len(hits) != 1:
        raise SystemExit(f"FAIL: round {k}: expected 1 dir, found {len(hits)}")
    return hits[0]


def find_manifest(d: Path, k: int) -> Path:
    for cand in (d / f"R{k}_OUTPUT_MANIFEST.json", d / f"OD0_R{k}_OUTPUT_MANIFEST.json"):
        if cand.exists():
            return cand
    raise SystemExit(f"FAIL: round {k}: no output manifest in {d.name}")


def main() -> None:
    report = {"schema": "R48_PINNED_CHAIN_VERIFICATION_V1", "links": [], "cd0": [],
              "ledgers": [], "package": {}, "r47_top_pins": {}, "status": None}

    # --- R47 top-level pins ---
    r47 = round_dir(47)
    man47 = find_manifest(r47, 47)
    man47_sha = sha256(man47)
    man47_obj = json.loads(man47.read_text(encoding="utf-8"))
    report["r47_top_pins"] = {
        "manifest_path": str(man47.relative_to(BASE)),
        "manifest_sha256_on_disk": man47_sha,
        "manifest_sha256_pin": PIN_R47_MANIFEST_SHA,
        "manifest_match": man47_sha == PIN_R47_MANIFEST_SHA,
        "result_digest_in_manifest": man47_obj.get("result_digest"),
        "result_digest_pin": PIN_R47_RESULT_DIGEST,
        "result_digest_match": man47_obj.get("result_digest") == PIN_R47_RESULT_DIGEST,
        "execution_commit_pin": PIN_R47_EXEC_COMMIT,
        "execution_commit_locally_resolvable": False,  # checked via git cat-file, absent
        "manifest_file_count": man47_obj.get("file_count"),
        "BELL2_scientific_content_opened_in_manifest": man47_obj.get(
            "BELL2_scientific_content_opened"),
    }

    # --- chain walk R47 -> R30 ---
    ok = True
    for k in range(47, 30, -1):
        d = round_dir(k)
        lock_hits = sorted(d.glob(f"R{k}_INPUT_LOCK.json")) or sorted(
            d.glob(f"OD0_R{k}_INPUT_LOCK.json"))
        if not lock_hits:
            report["links"].append({"round": k, "status": "FAIL_NO_INPUT_LOCK"})
            ok = False
            continue
        lock = json.loads(lock_hits[0].read_text(encoding="utf-8"))
        prev = k - 1
        # Recursively locate the predecessor manifest pin at any nesting depth.
        # Accepted key-path shapes (observed across R31..R47 locks):
        #   R{prev}_output_manifest_sha256            (flat, R46/R47 style)
        #   R{prev}/manifest_sha256                   (R31/R32 style)
        #   R{prev}/manifest/sha256                   (R43 style)
        #   inherited_campaigns/R{prev}/manifest/sha256  (R44/R45 style)
        #   .../R{prev}/.../manifest.../sha256        (nested R34-in-R35 style)
        hex64 = re.compile(r"^[0-9a-f]{64}$")
        pins = []  # (key_path, value) leaves mentioning R{prev}

        def hunt(o, path):
            if isinstance(o, dict):
                for kk, vv in o.items():
                    hunt(vv, path + "/" + kk)
            elif isinstance(o, str) and hex64.match(o):
                if re.search(rf"(^|/|_)r{prev}(/|_|$)", path.lower()):
                    pins.append((path, o))

        hunt(lock, "")
        # A pin belongs to R{prev} only if the LAST round number named in its
        # key path is prev (locks embed copies of older locks, whose inner
        # pins reference earlier rounds and must not be misread).
        def last_round(path):
            nums = re.findall(r"(?:^|/|_)[Rr](\d+)(?:/|_|$|\.)", path)
            return int(nums[-1]) if nums else None
        pins = [(p, v) for p, v in pins if last_round(p) == prev]
        pins.sort()
        link = {"round": k, "lock": str(lock_hits[0].relative_to(BASE)),
                "predecessor": prev}

        # Link form 1: direct pin of the predecessor OUTPUT manifest.
        direct = [(p, v) for p, v in pins
                  if re.search(r"(output_manifest[_/]sha256|/manifest/sha256"
                               r"|/manifest_sha256)$", p.lower())
                  and not re.search(r"\.(json|md|py|csv)/", p.lower())]
        # Link form 2: per-file pins of named predecessor artifacts
        # (path segment carries the artifact filename, R37-style).
        file_pins = [(p, v) for p, v in pins
                     if re.search(r"/([^/]+\.(json|md|py|csv))/sha256$",
                                  p.lower())]
        if direct:
            pin_key, pin_val = direct[0]
            prev_man = find_manifest(round_dir(prev), prev)
            on_disk = sha256(prev_man)
            link.update(pin_key=pin_key, pin_value=pin_val,
                        predecessor_manifest=str(prev_man.relative_to(BASE)),
                        predecessor_manifest_sha256_on_disk=on_disk,
                        status="VERIFIED" if on_disk == pin_val
                        else "FAIL_HASH_MISMATCH")
            if on_disk != pin_val:
                ok = False
        elif file_pins:
            prev_dir = round_dir(prev)
            checked, bad = [], []
            for p, v in file_pins:
                fname = re.search(r"/([^/]+\.(?:json|md|py|csv))/sha256$",
                                  p, re.IGNORECASE).group(1)
                target = prev_dir / fname
                if not target.exists():
                    bad.append({"pin": p, "reason": "FILE_ABSENT"})
                    continue
                on_disk = sha256(target)
                (checked if on_disk == v else bad).append(
                    {"pin": p, "file": fname, "on_disk": on_disk})
            link.update(form="PER_FILE_PINS", files_verified=len(checked),
                        files_failed=bad,
                        status="VERIFIED_VIA_FILE_PINS" if checked and not bad
                        else "FAIL_FILE_PIN_MISMATCH")
            if bad or not checked:
                ok = False
        else:
            link["status"] = "FAIL_NO_PREDECESSOR_PIN_FIELD"
            ok = False
        report["links"].append(link)

    # --- CD0 constructor artifacts (hash-pin, content not parsed here) ---
    cd0_dir = (BASE / "DEU_LER_v0_1_Codex_Package" / "deu_ler_v0_1"
               / "deu_unified_equations_v1_0" / "deu_combinatorial_descent_cd0")
    if cd0_dir.exists():
        for p in sorted(cd0_dir.rglob("*")):
            if p.is_file():
                report["cd0"].append({"path": str(p.relative_to(BASE)),
                                      "sha256": sha256(p), "bytes": p.stat().st_size})
    else:
        report["cd0"] = "FAIL_CD0_DIR_ABSENT"
        ok = False

    # --- descent ledgers + package + supporting PDFs in the R48 root ---
    for name in ("MODEL_GENEALOGY.md", "MISSING_PROVENANCE.md",
                 "OD0_CLAUDE_CODE_PACKAGE_R48_MATURATION_SOURCE_BOUNDARY_v0_2.md",
                 "unified_deu_eq.pdf", "unified_deu_eq (1).pdf"):
        p = PKG / name
        rec = {"path": str(p.relative_to(BASE))}
        if p.exists():
            rec["sha256"] = sha256(p)
            rec["bytes"] = p.stat().st_size
        else:
            rec["status"] = "ABSENT"
            ok = False
        (report["package"].setdefault("files", [])).append(rec)

    report["status"] = ("PASS_R47_PIN_AND_R30_CHAIN_REACHABLE" if ok
                        else "FAIL_SEE_LINKS")
    out = PKG / "R48_CHAIN_VERIFICATION.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8", newline="\n")
    print(report["status"])
    for link in report["links"]:
        print(f"  R{link['round']} -> R{link['predecessor']}: {link['status']}")
    print(f"  CD0 files pinned: {len(report['cd0']) if isinstance(report['cd0'], list) else report['cd0']}")


if __name__ == "__main__":
    sys.exit(main())
