"""Prepare one ten-target review, or its field controls, from verified public QLP products."""
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


def fetch(row, destination):
    path = destination / row["filename"]
    expected = row["sha256"]
    if path.exists():
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f"Existing file differs from the published input: {path}")
        return
    response = requests.get(row["url"], timeout=(15,90))
    response.raise_for_status()
    if hashlib.sha256(response.content).hexdigest() != expected:
        raise ValueError(f"Archive product differs from the published input: {path.name}")
    with NamedTemporaryFile(dir=destination, delete=False) as temp:
        temp.write(response.content)
    os.replace(temp.name,path)


def prepare(batch, controls, root):
    data = root / "sky/data/qlp-sb-p20-60"
    old = root / "Astra/made/binary-exploration-2026-11-04/bulk-results"
    flags = root / "sky/mixed-fold-2026-11-24/cadence-controls"
    for folder in (data,old,flags):
        folder.mkdir(parents=True,exist_ok=True)
    scans = json.loads(gzip.decompress((HERE/"historical-scans.json.gz").read_bytes()))
    for tic,document in scans.items():
        (old/f"{tic}.json").write_text(json.dumps(document),encoding="utf8")
    shutil.copyfile(HERE/"gaia-orbits.csv",data/"nss.csv")
    shutil.copyfile(HERE/"exposure-guard.csv",flags/"flagged-exposures.csv")
    with (HERE/"qlp.csv").open(newline="") as stream:
        wanted = [r for r in csv.DictReader(stream) if str(batch) in r["batches"].split("|")
                  or (controls and str(batch) in r["control_batches"].split("|"))]
    print(f"Checking {len(wanted)} products for batch {batch}",flush=True)
    with ThreadPoolExecutor(4) as pool:
        list(pool.map(lambda row: fetch(row,data),wanted))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("batch",type=int,choices=range(1,7))
    ap.add_argument("--controls",action="store_true",help="Also download same-camera comparison stars")
    ap.add_argument("--root",type=Path,default=HERE/"workspace")
    args = ap.parse_args()
    prepare(args.batch,args.controls,args.root)
