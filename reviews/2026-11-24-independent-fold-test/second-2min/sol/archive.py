import argparse
import csv
import hashlib
import io
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import shutil

import numpy as np
import pandas as pd
import requests
from astropy.io import fits

HERE = Path(__file__).resolve().parent
SKY = HERE.parents[2]
ARCHIVE = SKY / "data/fable52-tce-graveyard"
CACHE = HERE / "cadences"
PRIOR = SKY / "fable-pairs-2026-11-24/sol/cadences"
CACHE.mkdir(exist_ok=True)

def download(tic, sec, stream, filename):
    if stream == "ffi":
        digits = tic.zfill(16)
        dirs = "/".join(digits[i:i+4] for i in range(0, 16, 4))
        urls = [f"https://archive.stsci.edu/hlsps/tess-spoc/s{sec:04d}/target/{dirs}/hlsp_tess-spoc_tess_phot_{digits}-s{sec:04d}_tess_v1_lc.fits"]
    elif filename:
        # SPOC official file has pipeline timestamp in the filename.
        stem = "/".join(tic.zfill(16)[i:i+4] for i in range(0, 16, 4))
        urls = [f"https://archive.stsci.edu/missions/tess/tid/s{sec:04d}/{stem}/{filename}",
                f"https://mast.stsci.edu/api/v0.1/Download/file?uri=mast:TESS/product/{filename}"]
    else:
        raise ValueError("SPOC index has no matching sector/file")
    cache = CACHE / f"{tic}-{sec}.npz"
    if cache.exists():
        with np.load(cache) as a:
            return a["t"], a["sap"], a["pdc"], str(a["url"]), str(a["sha"]), int(a["raw_n"])
    errors = []
    for url in urls:
        try:
            response = requests.get(url, timeout=(5, 25))
            response.raise_for_status()
            with fits.open(io.BytesIO(response.content), memmap=False) as hdus:
                assert int(hdus[0].header["TICID"]) == int(tic)
                assert int(hdus[0].header["SECTOR"]) == sec
                data = hdus[1].data
                t = np.array(data["TIME"], float)
                sap = np.array(data["SAP_FLUX"], float)
                pdc = np.array(data["PDCSAP_FLUX"], float)
                raw_n = len(t)
                good = (data["QUALITY"] == 0) & np.isfinite(t)
            t, sap, pdc = t[good], sap[good], pdc[good]
            sha = hashlib.sha256(response.content).hexdigest()
            np.savez_compressed(cache, t=t, sap=sap, pdc=pdc, url=url, sha=sha, raw_n=raw_n)
            return t, sap, pdc, url, sha, raw_n
        except Exception as exc:
            errors.append(f"{url}: {type(exc).__name__} {str(exc)[:160]}")
    raise RuntimeError(" | ".join(errors))



def load_batch():
    with (HERE.parent / "batch.csv").open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def prepare():
    rows = load_batch()
    wanted = {int(row["tic"]) for row in rows}
    files = {}
    ffi = {}
    for chunk in pd.read_csv(ARCHIVE / "lc-index.csv.gz", chunksize=350000):
        for row in chunk[chunk.tic.isin(wanted)].itertuples(index=False):
            files.setdefault(str(row.tic), {})[int(row.sector)] = row.file
    for chunk in pd.read_csv(ARCHIVE / "tessspoc-index.csv.gz", chunksize=350000):
        for row in chunk[chunk.tic.isin(wanted)].itertuples(index=False):
            ffi.setdefault(str(row.tic), set()).add(int(row.sector))
    jobs = []
    for row in rows:
        tic = row["tic"]
        stream = row.get("stream")
        explicit = next((row.get(key) for key in ("sectors", "indexed_sectors", "sectors_used", "sector") if row.get(key)), None)
        if explicit:
            import re
            sectors = [int(s) for s in re.findall(r"\d+", explicit)]
        else:
            primary = sorted(ffi.get(tic, ())) if stream == "ffi" else sorted(files.get(tic, ()))
            sectors = primary or (sorted(files.get(tic, ())) if stream == "ffi" else sorted(ffi.get(tic, ())))
        for sector in sectors:
            file = files.get(tic, {}).get(sector)
            product_stream = "ffi" if stream == "ffi" and sector in ffi.get(tic, ()) else "2min" if file else "ffi"
            jobs.append((tic, sector, product_stream, file))
    return rows, jobs


def fetch(job):
    tic, sector, stream, filename = job
    record = dict(tic=tic, sector=sector, stream=stream)
    dest = CACHE / f"{tic}-{sector}.npz"
    prior = PRIOR / dest.name
    try:
        if not dest.exists() and prior.exists():
            with np.load(prior) as old:
                if ("hlsp_tess-spoc" in str(old["url"])) == (stream == "ffi"):
                    shutil.copyfile(prior, dest)
        t, sap, pdc, url, sha, raw_n = download(tic, sector, stream, filename)
        record.update(url=url, sha=sha, raw_n=raw_n, quality_zero_count=len(t), cadence_minutes=float(np.median(np.diff(t))*1440))
    except Exception as exc:
        record.update(error=str(exc))
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()
    manifest = HERE / "archive.json"
    if manifest.exists():
        initial = json.loads(manifest.read_text(encoding="utf8"))
        if all(r.get("url") and r.get("sha") for r in initial):
            jobs = [(r["tic"], r["sector"], r["stream"], r["url"].rsplit("/", 1)[-1]) for r in initial]
            with ThreadPoolExecutor(args.workers) as pool:
                for previous, fetched in zip(initial, pool.map(fetch, jobs)):
                    if fetched.get("sha") != previous["sha"]:
                        raise RuntimeError(f"Archive fingerprint mismatch for {previous['url']}")
            print(f"Verified {len(jobs)} archive products")
            return
    rows, jobs = prepare()
    print(f"{len(rows)} targets, {len(jobs)} sector jobs", flush=True)
    records = []
    with ThreadPoolExecutor(args.workers) as pool:
        for record in pool.map(fetch, jobs):
            records.append(record)
            print(record["tic"], record["sector"], "error" if "error" in record else record["quality_zero_count"], flush=True)
    (HERE / "archive.json").write_text(json.dumps(records, indent=2), encoding="utf8")


if __name__ == "__main__":
    main()
