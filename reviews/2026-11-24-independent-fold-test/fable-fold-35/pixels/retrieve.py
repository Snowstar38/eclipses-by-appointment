"""Fetch the original TESS-SPOC cutouts and Gaia DR3 scenes used in the window table."""
import argparse
import csv
import hashlib
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import NamedTemporaryFile
import os

import requests

HERE = Path(__file__).resolve().parent


def tpf_url(tic, sector):
    digits = f"{int(tic):016d}"
    folders = "/".join(digits[i:i+4] for i in range(0, 16, 4))
    tag = f"s{int(sector):04d}"
    return (f"https://archive.stsci.edu/hlsps/tess-spoc/{tag}/target/{folders}/"
            f"hlsp_tess-spoc_tess_phot_{digits}-{tag}_tess_v1_tp.fits")


def acquire(job):
    path, url, params, prefix = job
    if not path.is_file():
        for attempt in range(3):
            try:
                resp = requests.get(url, params=params, timeout=(12, 45))
                resp.raise_for_status()
                if not resp.content.lower().startswith(prefix):
                    raise ValueError(f"Unexpected content {resp.content[:80]}")
                with NamedTemporaryFile(dir=path.parent, delete=False) as temp:
                    temp.write(resp.content)
                os.replace(temp.name, path)
                break
            except (ValueError, requests.RequestException):
                if attempt == 2:
                    raise
                time.sleep(1+attempt)
    return dict(filename=path.name, url=requests.Request("GET", url, params=params).prepare().url,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest(), bytes=path.stat().st_size)


def jobs(cache, rows):
    stars, sectors = set(), set()
    for r in rows:
        tic, sector, ra, dec = (r[k] for k in ("tic","sector","ra","dec"))
        if (tic,sector) not in sectors:
            sectors.add((tic,sector))
            yield cache/f"{tic}-{sector}.fits", tpf_url(tic,sector), {}, b"simple"
        if tic not in stars:
            stars.add(tic)
            query=(f"SELECT source_id,ra,dec,pmra,pmdec,ref_epoch,phot_g_mean_mag AS g,"
                   f"phot_rp_mean_mag AS rp FROM gaiadr3.gaia_source WHERE 1=CONTAINS("
                   f"POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.064)) AND phot_g_mean_mag<20.5")
            params=dict(REQUEST="doQuery",LANG="ADQL",FORMAT="csv",QUERY=query,MAXREC=30000)
            yield HERE/f"gaia-{tic}.csv", "https://gea.esac.esa.int/tap-server/tap/sync", params, b"source_id,"


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("cache", type=Path)
    args=p.parse_args()
    args.cache.mkdir(parents=True,exist_ok=True)
    rows=list(csv.DictReader((HERE/"windows.csv").open()))
    receipt=HERE/"inputs.csv"
    published={}
    if receipt.exists():
        with receipt.open(encoding="utf8",newline="") as stream:
            published={r["filename"]:r["sha256"] for r in csv.DictReader(stream)}
    from concurrent.futures import as_completed
    results=[]
    with ThreadPoolExecutor(5) as pool:
        tasks={pool.submit(acquire, job):job[0] for job in jobs(args.cache, rows)}
        for f in as_completed(tasks):
            try:
                result=f.result()
                if result["filename"] in published and result["sha256"]!=published[result["filename"]]:
                    raise ValueError(f"SHA-256 differs from archived input for {result['filename']}")
                results.append(result)
                print(tasks[f].name, 'ok', flush=True)
            except Exception as exc:
                print(tasks[f].name, str(exc), flush=True)
    if len(results)!=len(tasks):
        raise SystemExit("Some inputs unavailable or changed")
    with receipt.open("w", encoding="utf8", newline="") as f:
        w=csv.DictWriter(f, ["filename","url","sha256","bytes"],lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(results,key=lambda r:r["filename"]))
