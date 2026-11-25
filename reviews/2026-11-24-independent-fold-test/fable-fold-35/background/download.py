from pathlib import Path
import urllib.request, concurrent.futures

p = Path(__file__).resolve().parent
# Public MAST TESS-SPOC HLSP paths; no cadence cache is required.
def get(item):
    tic, sector = item
    target = f"{tic:016d}"
    folders = "/".join(target[i:i+4] for i in range(0, 16, 4))
    url = (f"https://archive.stsci.edu/hlsps/tess-spoc/s{sector:04d}/target/"
           f"{folders}/hlsp_tess-spoc_tess_phot_{target}-s{sector:04d}_tess_v1_lc.fits")
    dest = p / f"{tic}-{sector}.fits"
    urllib.request.urlretrieve(url, dest)
    return f"{url} -> {dest}"

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        for result in ex.map(get, [(tic, sector) for tic in (52157743, 218233922) for sector in (42, 43, 44)]):
            print(result)
