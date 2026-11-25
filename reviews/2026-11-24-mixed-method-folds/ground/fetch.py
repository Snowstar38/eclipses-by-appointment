"""Fetch ZTF object measurements within 2.16 arcseconds of each transferred TIC."""
import argparse
import csv
import gzip
import hashlib
import io
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
URL = "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves"


def download(row, cache):
    tic = row["tic"]
    query = dict(POS=f"CIRCLE {row['ra_deg']} {row['dec_deg']} 0.0006", BANDNAME="g,r",
                 FORMAT="csv", BAD_CATFLAGS_MASK=32768)
    url = requests.Request("GET", URL, params=query).prepare().url
    out = cache / (tic + ".csv.gz")
    record = dict(tic=tic, url=url)
    try:
        if out.exists():
            data = gzip.decompress(out.read_bytes())
        else:
            r = requests.get(url, timeout=(10, 90))
            r.raise_for_status()
            data = r.content
        reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig")))
        if not {"oid", "mjd", "mag", "catflags"}.issubset(reader.fieldnames or []):
            raise ValueError("response lacks ZTF measurement fields: " + repr(data[:160]))
        count = sum(1 for _ in reader)
        if not out.exists():
            out.write_bytes(gzip.compress(data, mtime=0))
        record.update(rows=count, sha256=hashlib.sha256(data).hexdigest())
    except (OSError, ValueError) as exc:
        record["error"] = str(exc)
    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    with (HERE.parent / "batch.csv").open() as f:
        rows = list(csv.DictReader(f))
    with ThreadPoolExecutor(4) as pool:
        records = list(pool.map(lambda r: download(r, args.cache), rows))
    (HERE / "receipts.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf8")
    print(len(records), "searched;", sum("rows" in r for r in records), "valid responses")
