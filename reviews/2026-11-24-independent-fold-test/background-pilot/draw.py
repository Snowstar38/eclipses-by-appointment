"""Draw and reserve the fresh near-ecliptic sample before measuring the light curves."""
import csv
import hashlib
from pathlib import Path

from astropy.coordinates import SkyCoord

HERE = Path(__file__).resolve().parent
PILOT = HERE.parent
SKY = PILOT.parent


def read(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def coords(rows):
    return SkyCoord([float(r.get("ra_deg") or r["ra"]) for r in rows],
                    [float(r.get("dec_deg") or r["dec"]) for r in rows], unit="deg")


if __name__ == "__main__":
    exclusions = []
    for path in [PILOT/"batch.csv", PILOT/"ffi/batch.csv", PILOT/"second-2min/batch.csv",
                 SKY/"fable52-ffi-tce-2026-11-24/batch.csv",
                 SKY/"fable52-changing-2026-11-24/ephem.csv",
                 SKY.parent/"tmp/astra-credit-nov24/accepted-systems.csv"]:
        exclusions.extend(read(path))
    ids = {r["tic"] for r in exclusions}
    window = [r for r in read(PILOT/"eligible.csv") if r["stream"] == "2min"
              and r["tic"] not in ids and float(r["paired_bin_depth_ppt"]) >= 10]
    positions = coords(window)
    nearest = positions.match_to_catalog_sky(coords(exclusions))[1].arcsec
    candidates = []
    for row, lat, sep in zip(window, positions.barycentrictrueecliptic.lat.deg, nearest):
        if abs(lat) > 12 or sep <= 30:
            continue
        sectors = sorted(int(s) for s in row["sectors"].split("|"))
        chosen = sorted({sectors[0], sectors[-1]})
        candidates.append(dict(tic=row["tic"], stream="2min", sectors="|".join(map(str, chosen)),
                               ra_deg=row["ra_deg"], dec_deg=row["dec_deg"],
                               ecliptic_lat_deg=round(float(lat), 4),
                               min_prior_separation_arcsec=round(float(sep), 1),
                               owner="Astra", reserved_date="2026-11-24"))
    candidates.sort(key=lambda r: hashlib.sha256(("bg-pilot-v1/" + r["tic"]).encode()).digest())
    batch = candidates[:20]
    assert len(batch) == 20
    with (HERE/"batch.csv").open("w", newline="", encoding="utf8") as f:
        w = csv.DictWriter(f, batch[0], lineterminator="\n")
        w.writeheader()
        w.writerows(batch)
    print(f"{len(candidates)} eligible; {len(batch)} selected; "
          f"{sum(len(r['sectors'].split('|')) for r in batch)} products")
