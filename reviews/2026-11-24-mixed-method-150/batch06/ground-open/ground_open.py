"""Run fixed TESS-clock dip contrasts for six open leads, without fitting ground phase."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path

from astropy.coordinates import EarthLocation, SkyCoord
from astropy.time import Time
import astropy.units as u
import numpy as np

HERE = Path(__file__).resolve().parent
LEADS = {"409755474": 6, "341293943": 6, "235594109": 7, "94039922": 8,
         "331825104": 10, "156003438": 10}


def rows(path, compressed=False):
    reader = gzip.open if compressed else open
    with reader(path, "rt", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def save(path, result):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, list(result[0]))
        writer.writeheader()
        writer.writerows(result)


def survey_data(items, survey, target):
    good = []
    for r in items:
        if survey == "ASAS-SN":
            if r["quality"] != "G" or not r["mag"] or not r["mag_err"]:
                continue
            obj, band, detector = r["asas_sn_id"], r["phot_filter"], r["camera"]
            jd, mag, err = float(r["jd"]), float(r["mag"]), float(r["mag_err"])
        else:
            if int(r["catflags"]) != 0:
                continue
            obj, band, detector = r["oid"], r["filtercode"], r["field"]+"_"+r["ccdid"]
            jd, mag, err = float(r["mjd"])+2400000.5, float(r["mag"]), float(r["magerr"])
        if np.isfinite(jd+mag+err) and 0 < err < .10 and 0 < mag < 30:
            good.append((obj, band, detector, jd, mag, err))
    if not good:
        return {}
    loc = EarthLocation.from_geocentric(0, 0, 0, unit=u.m)
    direction = SkyCoord(float(target["ra_deg"]), float(target["dec_deg"]), unit="deg")
    times = Time([r[3] for r in good], format="jd", scale="utc", location=loc)
    dates = (times.tdb + times.light_travel_time(direction)).jd - 2457000
    groups = {}
    for (obj, band, detector, _, mag, error), t in zip(good, dates):
        groups.setdefault((obj, band), []).append((t, mag, error, detector))
    return groups


def nightly_group(samples, epoch, period):
    # Only compare night medians within a detector and observing season.
    seasons = {}
    for t, mag, _, det in samples:
        seasons.setdefault((det, int(t//365.25)), []).append((t, mag))
    nights = []
    for subset in seasons.values():
        if len(subset) < 15:
            continue
        by_night = {}
        for t, mag in subset:
            by_night.setdefault(int(t+.5), []).append((t, mag))
        if len(by_night) < 5:
            continue
        seen = [np.median(group, axis=0) for group in by_night.values()]
        template = np.median([row[1] for row in seen])
        nights.extend((t, m-template) for t, m in seen)
    # A network night receives a single vote, even if multiple cameras measured it.
    total = {}
    for t, m in nights:
        total.setdefault(int(t+.5), []).append((t, m))
    result = np.array([np.median(group, axis=0) for group in total.values()])
    if not len(result):
        return np.array([]), np.array([]), np.array([])
    t, residual = result.T
    cycle = np.rint((t-epoch)/period).astype(int)
    return cycle, t-epoch-cycle*period, residual


def assess(samples, epoch, period, width):
    cycle, dt, residual = nightly_group(samples, epoch, period)
    core = abs(dt) < width/2
    wing = (abs(dt) >= width/2) & (abs(dt) <= 1.5*width)
    quiet = ~core & ~wing
    cycles = np.union1d(cycle[core],cycle[wing])
    table = []
    for k in cycles:
        c = residual[core & (cycle == k)]
        w = residual[wing & (cycle == k)]
        table.append(dict(cycle=int(k), center_btjd=epoch+k*period, core_nights=len(c),
                          wing_nights=len(w), depth_mmag=1000*(np.median(c)-np.median(w)) if len(c)*len(w) else ""))
    stats = dict(valid_epochs=len(samples), usable_nights=len(dt), core_nights=int(core.sum()),
                 wing_nights=int(wing.sum()), core_cycles=len(np.unique(cycle[core])),
                 paired_cycles=sum(x["depth_mmag"] != "" for x in table),
                 out_of_window_mad_mmag="", population_depth_mmag="", lo95_mmag="", hi95_mmag="")
    if quiet.any():
        stats["out_of_window_mad_mmag"] = 1482.6*np.median(abs(residual[quiet]-np.median(residual[quiet])))
    if core.sum() < 5 or wing.sum() < 10 or len(np.unique(cycle[core])) < 4:
        return stats | {"test_status": "insufficient_window_sampling"}, table
    depth = 1000*(np.median(residual[core])-np.median(residual[wing]))
    blocks = [(residual[core & (cycle == k)], residual[wing & (cycle == k)]) for k in cycles]
    rng = np.random.default_rng(20261124)
    boot = []
    for selection in rng.integers(0,len(blocks),size=(1500,len(blocks))):
        c = np.concatenate([blocks[i][0] for i in selection])
        w = np.concatenate([blocks[i][1] for i in selection])
        if len(c)*len(w):
            boot.append(1000*(np.median(c)-np.median(w)))
    lo, hi = np.quantile(boot,[.025,.975])
    return stats | dict(population_depth_mmag=depth,lo95_mmag=lo,hi95_mmag=hi,
                        test_status="estimated"), table


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    parser.add_argument("--fallback-cache", type=Path)
    args = parser.parse_args()
    roster = {r["tic"]:r for r in rows(HERE.parents[1]/"roster.csv")}
    evidence, cycle_evidence, receipts = [], [], []
    for tic, batch in LEADS.items():
        target = roster[tic]
        windows = rows(HERE.parents[1]/f"batch{batch:02d}"/"predicted-windows.csv")
        clocks = {r["hypothesis"]: tuple(float(r[k]) for k in ("period_d","epoch_btjd","width_d"))
                  for r in windows if r["tic"] == tic}
        for survey, filename in (("ASAS-SN",f"asassn-{tic}.csv.gz"), ("ZTF",f"{tic}.csv.gz")):
            primary = args.cache/filename
            path = args.fallback_cache/filename if args.fallback_cache and not primary.exists() else primary
            items = rows(path, compressed=True) if path.exists() else []
            data = survey_data(items,survey,target)
            receipts.append(dict(tic=tic,survey=survey,filename=filename,state="cached" if path.exists() else "missing_cache",
                                 rows=len(items), groups=len(data),
                                 sha256_uncompressed=hashlib.sha256(gzip.decompress(path.read_bytes())).hexdigest() if path.exists() else ""))
            for h, (p, e, w) in clocks.items():
                kind = "Gaia-period_assumption" if h == "gaia_period_days" else "TESS-only_trial"
                for (obj,band), samples in (data or {("",""):[]}).items():
                    meta = dict(tic=tic,survey=survey,object_id=obj,band=band,hypothesis=h,
                                clock_type=kind,period_d=p,epoch_btjd=e,width_d=w)
                    stats, detail = assess(samples,e,p,w)
                    if not samples:
                        stats["test_status"] = ("missing_cache" if not path.exists() else
                                                "no_catalog_photometry" if not items else "quality_rejected")
                    evidence.append(meta | stats)
                    cycle_evidence.extend(meta | r for r in detail)
    save(HERE/"phase-contrasts.csv",evidence)
    save(HERE/"per-cycle.csv",cycle_evidence)
    save(HERE/"cache-receipts.csv",receipts)


if __name__ == "__main__":
    main()
