"""Freeze the local QLP products and historical inputs used by the review."""
import argparse
import csv
import gzip
import hashlib
import json
import shutil
from collections import defaultdict
from pathlib import Path

from astropy.io import fits

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
ARCHIVE = "https://archive.stsci.edu/hlsps/qlp"


def read(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def url(tic, sector):
    padded = f"{int(tic):016d}"
    nodes = "/".join(padded[i:i + 4] for i in range(0, 16, 4))
    version = "02" if 74 <= sector <= 79 else "01"
    return f"{ARCHIVE}/s{sector:04d}/{nodes}/hlsp_qlp_tess_ffi_s{sector:04d}-{padded}_tess_v{version}_llc.fits"


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def build(source_root):
    targets = {}
    control_batches = defaultdict(set)
    expected_controls = defaultdict(set)
    for batch in range(1, 17):
        folder = REVIEW / f"batch{batch:02d}"
        for row in read(folder / "batch.csv"):
            tic = row["tic"]
            if tic in targets:
                raise ValueError(f"Repeated target in batches: {tic}")
            targets[tic] = batch
        source = folder / "control-events.csv"
        if source.exists():
            for row in read(source):
                control_batches[(int(row["sector"]), int(row["camera"]))].add(batch)
        results = folder / "camera-controls.csv"
        if results.exists():
            for row in read(results):
                expected_controls[batch].add((row["control_tic"], int(row["sector"])))
    if len(targets) != 154:
        raise ValueError(f"Expected 154 distinct targets, found {len(targets)}")

    fits_dir = source_root / "sky/data/qlp-sb-p20-60"
    history_dir = source_root / "Astra/made/binary-exploration-2026-11-04/bulk-results"
    history = {}
    historical_hashes = {}
    for tic in targets:
        doc = json.loads((history_dir / f"{tic}.json").read_text(encoding="utf-8-sig"))
        for entry in doc["files"]:
            entry["path"] = Path(entry["path"].replace("\\", "/")).name
            historical_hashes[entry["path"]] = entry["sha256"]
        history[tic] = doc

    control_sectors = {sector for sector, _ in control_batches}
    manifest = []
    seen_history = set()
    actual_controls = defaultdict(set)
    for path in sorted(fits_dir.glob("*_s*.fits")):
        tic, tag = path.stem.rsplit("_s", 1)
        sector = int(tag)
        batch = targets.get(tic)
        if batch is None and sector not in control_sectors:
            continue
        header = fits.getheader(path, 0)
        camera = int(header["CAMERA"])
        ccd = int(header["CCD"])
        if int(header["SECTOR"]) != sector or int(header["TICID"]) != int(tic):
            raise ValueError(f"Unexpected FITS identity: {path}")
        peers = control_batches.get((sector, camera), set())
        if batch is None and not peers:
            continue
        digest = sha256(path)
        if path.name in historical_hashes:
            if digest != historical_hashes[path.name]:
                raise ValueError(f"Historical scan hash mismatch: {path.name}")
            seen_history.add(path.name)
        for peer_batch in peers:
            actual_controls[peer_batch].add((tic, sector))
        manifest.append(
            dict(tic=tic, sector=sector, camera=camera, ccd=ccd, filename=path.name,
                 batches=batch or "", control_batches="|".join(map(str, sorted(peers))),
                 bytes=path.stat().st_size, sha256=digest, url=url(tic, sector))
        )
    missing = set(historical_hashes) - seen_history
    if missing:
        raise ValueError(f"Missing historical FITS inputs: {sorted(missing)}")
    for batch, peers in expected_controls.items():
        missing = peers - actual_controls[batch]
        if missing:
            raise ValueError(f"Missing batch {batch} comparison products: {sorted(missing)}")
    missing_targets = set(targets) - {r["tic"] for r in manifest if r["batches"]}
    if missing_targets:
        raise ValueError(f"Targets without FITS products: {sorted(missing_targets)}")

    with (HERE / "qlp.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, manifest[0].keys())
        writer.writeheader()
        writer.writerows(manifest)
    scans = json.dumps(history, separators=(",", ":"), sort_keys=True).encode()
    (HERE / "historical-scans.json.gz").write_bytes(gzip.compress(scans, mtime=0))
    shutil.copyfile(
        source_root / "sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv",
        HERE / "exposure-guard.csv",
    )
    print(f"{len(targets)} targets, {len(historical_hashes)} historical FITS, "
          f"{sum(bool(r['batches']) for r in manifest)} target FITS, "
          f"{sum(bool(r['control_batches']) for r in manifest)} peer FITS, "
          f"{len(manifest)} distinct files.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=HERE.parents[2])
    build(parser.parse_args().source_root)
