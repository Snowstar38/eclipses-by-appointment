#!/usr/bin/env python3
"""Asteroid veto for the flags of the track-3 pilot (dips and bumps).

A main-belt asteroid crossing the photometric aperture of a TESS star adds light for a few hours (a bump that can mimic
a self-lensing flare); crossing the pixels used for the background, it makes the background too bright and the star
appear to dim (a dip). This script checks every flagged window of pilot_results/windows.csv:
  1. SkyBoT (IMCCE) cone search around the star at the time of the flag, from the geocentre, radius --search-arcmin
     (wide, because TESS, up to ~375 000 km from the Earth, sees main-belt asteroids several arcminutes away from
     their geocentric positions);
  2. for every asteroid bright enough to matter (V < star G + --dmag), a JPL Horizons ephemeris seen from TESS itself
     (spacecraft -95), every 20 minutes over +/- 1 day: smallest separation from the star and its time.
A flag is vetoed when an asteroid passes within --aperture-arcmin of the star within --dt-days of the flag.
Run from ~/Desktop/piste3 (needs astroquery; a few seconds per flag):
    python3 asteroid_veto.py              [--kind both|bump|dip]
Output: pilot_results/asteroid_veto.csv
"""
import argparse, os, time, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
BTJD0 = 2457000.0


def skybot_candidates(ra, dec, jd, radius_arcmin):
    from astroquery.imcce import Skybot
    from astropy.coordinates import SkyCoord
    from astropy.time import Time
    import astropy.units as u
    try:
        t = Skybot.cone_search(SkyCoord(ra * u.deg, dec * u.deg), radius_arcmin * u.arcmin, Time(jd, format="jd", scale="tdb"),
                               location="500", find_planets=False, find_comets=True)
    except Exception as exc:
        msg = str(exc).lower()
        if "no solar system" in msg or "no table found" in msg:      # SkyBoT answers with an empty VOTable
            return []
        raise
    out = []
    for r in t:
        v = r["V"]
        out.append(dict(name=str(r["Name"]), number=str(r["Number"]), V=float(v.value if hasattr(v, "value") else v)))
    return out


def tess_track(target, jd, ra, dec):
    """Smallest separation (arcmin) from the star seen from TESS, and its time, over jd +/- 1 d every 20 min."""
    from astroquery.jplhorizons import Horizons
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    obj = Horizons(id=target, location="500@-95", epochs={"start": f"JD{jd - 1:.5f}", "stop": f"JD{jd + 1:.5f}", "step": "20m"}, id_type=None)
    eph = obj.ephemerides(quantities="1,9")
    star = SkyCoord(ra * u.deg, dec * u.deg)
    pos = SkyCoord(np.asarray(eph["RA"], float) * u.deg, np.asarray(eph["DEC"], float) * u.deg)
    sep = star.separation(pos).arcmin
    k = int(np.argmin(sep))
    return float(sep[k]), float(eph["datetime_jd"][k])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", default="both", choices=["both", "bump", "dip"])
    ap.add_argument("--search-arcmin", type=float, default=20.0)
    ap.add_argument("--aperture-arcmin", type=float, default=1.5, help="radius treated as the aperture plus background pixels")
    ap.add_argument("--dt-days", type=float, default=0.3)
    ap.add_argument("--dmag", type=float, default=7.5, help="asteroids fainter than G_star + dmag cannot make a 0.1 per cent signal")
    ap.add_argument("--retry-failed", action="store_true", help="check again the flags whose SkyBoT or Horizons query failed")
    a = ap.parse_args()
    win = pd.read_csv("pilot_results/windows.csv")
    det = pd.read_csv("track3_detail.csv").drop_duplicates("source_id").set_index("source_id")
    rows = []
    if a.kind in ("both", "bump"):
        b = win[win["bump_flag"] == True]
        rows += [dict(source_id=int(r.source_id), kind="bump", sector=int(r.sector), author=r.author, t=float(r.bump_t), amplitude=float(r.bump_height)) for r in b.itertuples()]
    if a.kind in ("both", "dip"):
        d = win[(win["dip_flag"] == True) & (win["dip_depth"] <= 0.5)]
        rows += [dict(source_id=int(r.source_id), kind="dip", sector=int(r.sector), author=r.author, t=float(r.dip_t), amplitude=float(r.dip_depth)) for r in d.itertuples()]
    out_path = "pilot_results/asteroid_veto.csv"
    done = {}
    if os.path.exists(out_path):
        for _, x in pd.read_csv(out_path).iterrows():
            if a.retry_failed and "failed" in str(x.get("note", "")):
                continue                                      # checked again below
            done[(int(x["source_id"]), x["kind"], round(float(x["t"]), 4))] = x.to_dict()
    print(f"{len(rows)} flags to check ({a.kind}); {len(done)} already checked", flush=True)
    for i, r in enumerate(rows):
        key = (r["source_id"], r["kind"], round(r["t"], 4))
        if key in done:
            continue
        s = det.loc[r["source_id"]]; ra, dec, g = float(s["ra"]), float(s["dec"]), float(s["g"])
        jd = r["t"] + BTJD0
        rec = dict(r, ra=ra, dec=dec, G_star=g, n_asteroids_near=0, closest=None, closest_sep_arcmin=None, closest_dt_d=None, closest_V=None, veto=False, note="")
        try:
            cands = [c for c in skybot_candidates(ra, dec, jd, a.search_arcmin) if c["V"] < g + a.dmag]
        except Exception as exc:
            rec["note"] = f"SkyBoT failed: {str(exc)[:60]}"; cands = []
        rec["n_asteroids_near"] = len(cands)
        best = None
        for c in cands:
            target = c["number"] if c["number"] not in ("", "--", "None", "nan") else c["name"]
            try:
                sep, tmin = tess_track(target, jd, ra, dec)
            except Exception as exc:
                rec["note"] += f" Horizons failed for {c['name']};"; continue
            if best is None or sep < best[1]:
                best = (c, sep, tmin)
            time.sleep(0.3)
        if best:
            c, sep, tmin = best
            rec.update(closest=c["name"], closest_sep_arcmin=round(sep, 2), closest_dt_d=round(tmin - jd, 3), closest_V=round(c["V"], 1),
                       veto=bool(sep < a.aperture_arcmin and abs(tmin - jd) < a.dt_days))
        done[key] = rec
        pd.DataFrame(list(done.values())).to_csv(out_path, index=False)
        print(f"  [{i + 1}/{len(rows)}] Gaia DR3 {r['source_id']} {r['kind']} S{r['sector']} at BTJD {r['t']:.3f}: "
              + (f"{best[0]['name']} (V {best[0]['V']:.1f}) at {best[1]:.2f}' and {best[2] - jd:+.2f} d" if best else "no asteroid nearby")
              + ("  -> VETO" if rec["veto"] else ""), flush=True)
    df = pd.DataFrame(list(done.values()))
    if len(df):
        print("\nvetoed:", df.groupby("kind")["veto"].sum().to_dict(), "of", df.groupby("kind").size().to_dict())
    print(f"-> {out_path}")


if __name__ == "__main__":
    main()
