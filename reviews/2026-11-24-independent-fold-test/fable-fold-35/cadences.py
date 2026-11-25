"""Rebuild the 35-star photometry cache from its archived TESS-SPOC light curves."""
import argparse
import csv
import hashlib
import io
from pathlib import Path

from astropy.io import fits
import numpy as np
import requests

HERE = Path(__file__).resolve().parent


def signature(t, sap, pdc):
    sha = hashlib.sha256()
    for values, dtype in [(t, "<f8"), (sap, "<f4"), (pdc, "<f4")]:
        sha.update(np.asarray(values, dtype=dtype).tobytes())
    return sha.hexdigest()


def recover(row, folder):
    path = folder / (row["tic"] + "-" + row["sector"] + ".npz")
    if path.exists():
        with np.load(path) as data:
            if signature(data["t"], data["sap"], data["pdc"]) == row["arrays_sha256"]:
                return
    resp = requests.get(row["url"], timeout=(10, 90))
    resp.raise_for_status()
    with fits.open(io.BytesIO(resp.content), memmap=False) as h:
        if (int(h[0].header["TICID"]), int(h[0].header["SECTOR"])) != (int(row["tic"]), int(row["sector"])):
            raise ValueError("Wrong archive product for " + path.name)
        d = h[1].data
        good = (d["QUALITY"] == 0) & np.isfinite(d["TIME"])
        t, sap, pdc = [np.asarray(d[key][good], dtype=dt) for key, dt in
                       [("TIME", float), ("SAP_FLUX", np.float32), ("PDCSAP_FLUX", np.float32)]]
    if signature(t, sap, pdc) != row["arrays_sha256"]:
        raise ValueError("Archive arrays differ from the original input for " + path.name)
    np.savez_compressed(path, t=t, sap=sap, pdc=pdc, url=row["url"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    parser.add_argument("--tic", help="Optional single target")
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    with (HERE / "cadences.csv").open() as stream:
        for row in csv.DictReader(stream):
            if args.tic is None or row["tic"] == args.tic:
                recover(row, args.cache)
