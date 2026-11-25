"""Build quality-zero portable cadences from the original archived QLP FITS."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

import numpy as np
from astropy.io import fits

HERE = Path(__file__).resolve().parent
DOWNLOAD = "https://mast.stsci.edu/api/v0.1/Download/file?"


def require_fits(path, expected, uri, fetch):
    if not path.exists() and fetch:
        with urlopen(DOWNLOAD+urlencode({"uri": uri}), timeout=60) as response:
            data = response.read()
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError(f"Archive response does not match frozen FITS SHA-256 for {uri}")
        path.parent.mkdir(parents=True, exist_ok=True)
        temp = path.with_suffix(".fits.tmp")
        temp.write_bytes(data)
        temp.replace(path)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != expected:
        raise ValueError(f"Hash mismatch for {path}")
    return digest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=HERE.parent/"cadences")
    parser.add_argument("--fits-cache", type=Path, default=HERE.parent/"fits-cache",
                        help="Folder for original FITS named TIC_sNNN.fits")
    parser.add_argument("--fetch", action="store_true", help="Fetch missing original FITS from MAST")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((HERE/"archive-manifest.json").read_text())
    for record in manifest:
        path = args.fits_cache / Path(record["path"]).name
        require_fits(path, record["sha256"], record["mast_uri"], args.fetch)
        with fits.open(path) as hdus:
            data = hdus[1].data
            select = (data["QUALITY"] == 0) & np.isfinite(data["TIME"])
            t = np.array(data["TIME"][select], dtype=float)
            sap = np.array(data["SAP_FLUX"][select], dtype=float)
            pdc = np.array(data[record["flux_column"]][select], dtype=float)
        name = record["cache_name"]
        temp = args.out / f"{name}.tmp.npz"
        np.savez_compressed(temp, t=t, sap=sap, pdc=pdc, url=record["path"])
        temp.replace(args.out / name)
    print(f"{len(manifest)} sector files in {args.out}")


if __name__ == "__main__":
    main()
