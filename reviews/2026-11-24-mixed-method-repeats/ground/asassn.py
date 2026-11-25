"""Download ASAS-SN Sky Patrol master-list light curves within four arcseconds."""
import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path

import pandas as pd
from pyasassn.client import SkyPatrolClient

HERE = Path(__file__).resolve().parent


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    client = SkyPatrolClient(verbose=False)
    receipts = []
    for target in csv.DictReader((HERE.parent / "batch.csv").open()):
        tic = target["tic"]
        path = args.cache / f"asassn-{tic}.csv.gz"
        record = dict(tic=tic, ra_deg=target["ra_deg"], dec_deg=target["dec_deg"],
                      radius_arcsec=4, catalog="master_list")
        try:
            if not path.exists():
                result = client.cone_search(ra_deg=float(target["ra_deg"]), dec_deg=float(target["dec_deg"]),
                                            radius=4, units="arcsec", catalog="master_list", download=True, threads=1)
                data = getattr(result, "data", None)
                if data is None or not len(data):
                    data = pd.DataFrame(columns=["asas_sn_id","jd","mag","mag_err","phot_filter","quality","camera"])
                path.write_bytes(gzip.compress(data.to_csv(index=False, lineterminator="\n").encode("utf8"), mtime=0))
            data = pd.read_csv(path)
            record.update(rows=len(data), ids=[str(i) for i in data.asas_sn_id.unique()],
                          hash_uncompressed=hashlib.sha256(gzip.decompress(path.read_bytes())).hexdigest())
        except Exception as exc:
            record["error"] = str(exc)[:300]
        receipts.append(record)
        (HERE/"asassn-receipts.json").write_text(json.dumps(receipts, indent=2)+"\n", encoding="utf8")
        print(tic, record.get("rows", record.get("error")), flush=True)
