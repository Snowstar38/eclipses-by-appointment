"""Prepare the selected review batch from SHA-256-verified public QLP FITS."""
import argparse
import csv
import gzip
import hashlib
import json
import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import NamedTemporaryFile

import requests

HERE = Path(__file__).resolve().parent


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def check(row, size, digest, path):
    if size != int(row["bytes"]) or digest != row["sha256"]:
        raise ValueError(
            f"FITS differs from release bytes: {path} "
            f"(expected {row['bytes']} bytes SHA-256 {row['sha256']}, found {size} bytes {digest})"
        )


def fetch(row, destination, verify_only):
    path = destination / row["filename"]
    if path.exists():
        check(row, path.stat().st_size, sha256(path), path)
        return "reused"
    if verify_only:
        raise FileNotFoundError(f"Replay FITS is missing: {path}")

    response = requests.get(row["url"], timeout=(15, 90))
    response.raise_for_status()
    content = response.content
    check(row, len(content), hashlib.sha256(content).hexdigest(), row["url"])
    with NamedTemporaryFile(dir=destination, delete=False) as temp:
        temp_path = Path(temp.name)
        temp.write(content)
    try:
        os.replace(temp_path, path)
    finally:
        temp_path.unlink(missing_ok=True)
    return "downloaded"


def prepare(batch, controls, root, target=None, verify_only=False):
    data = root / "sky/data/qlp-sb-p20-60"
    history_dir = root / "Astra/made/binary-exploration-2026-11-04/bulk-results"
    guard = root / "sky/mixed-fold-2026-11-24/cadence-controls"
    with (HERE / "qlp.csv").open(encoding="utf-8-sig", newline="") as stream:
        products = list(csv.DictReader(stream))
    targets = {
        row["tic"] for row in products
        if str(batch) in row["batches"].split("|") and (target is None or target == row["tic"])
    }
    if not targets:
        raise ValueError(f"No matching targets in batch {batch}")
    wanted = [
        row for row in products
        if row["tic"] in targets or (controls and str(batch) in row["control_batches"].split("|"))
    ]
    if not verify_only:
        for folder in (data, history_dir, guard):
            folder.mkdir(parents=True, exist_ok=True)
    print(f"Checking {len(wanted)} FITS for {len(targets)} targets in batch {batch}", flush=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        actions = list(pool.map(lambda row: fetch(row, data, verify_only), wanted))

    with gzip.open(HERE / "historical-scans.json.gz", "rt", encoding="utf-8") as stream:
        history = json.load(stream)
    for tic in sorted(targets):
        content = json.dumps(history[tic], separators=(",", ":"), sort_keys=True).encode("utf-8")
        path = history_dir / f"{tic}.json"
        if verify_only:
            if path.read_bytes() != content:
                raise ValueError(f"Historical scan differs from release: {path}")
        else:
            path.write_bytes(content)
    guard_path = guard / "flagged-exposures.csv"
    if verify_only:
        if guard_path.read_bytes() != (HERE / "exposure-guard.csv").read_bytes():
            raise ValueError(f"Exposure guard differs from release: {guard_path}")
    else:
        shutil.copyfile(HERE / "exposure-guard.csv", guard_path)
    print(f"Verified {len(actions)} FITS, {actions.count('downloaded')} downloaded, "
          f"{actions.count('reused')} reused, {len(targets)} historical scans and the exposure guard.",
          flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("batch", type=int, choices=range(1, 17))
    ap.add_argument("--controls", action="store_true", help="Also include every same-camera comparison FITS used by the batch")
    ap.add_argument("--target", help="Prepare just this TIC within the selected batch")
    ap.add_argument("--root", type=Path, default=HERE / "workspace")
    ap.add_argument("--verify-only", action="store_true", help="Verify an existing replay without network access or writes")
    args = ap.parse_args()
    prepare(args.batch, args.controls, args.root, args.target, args.verify_only)
