#!/usr/bin/env python3
"""Are the stars flagged by pilot_track3.py already known as eclipsing binaries or variables?

Reads pilot_results/stars.jsonl (written as the pilot runs: this script can be run at any time, in a second
terminal, without disturbing the pilot) and track3_detail.csv (coordinates), and checks every star with at least
one flagged dip or bump against:
  VSX (B/vsx/vsx), the TESS eclipsing-binary catalogue (J/ApJS/258/16), the ASAS-SN variable stars (II/366),
  the Gaia DR3 eclipsing binaries (I/358/veb) and variability classes (I/358/vclassre), all through VizieR,
  and SIMBAD (object type).
For each catalogued period it also says whether it matches the Gaia orbital period (P, P/2 or 2P within 2 %):
a match means the known variable is this binary; a different period suggests another star in the aperture.

Usage:  python3 check_known.py            (from ~/Desktop/piste3; a few seconds per star)
Output: pilot_results/known_check.csv and a short summary on screen.
"""
import json, os, sys, time, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
RADIUS_ARCSEC = 5.0
CATS = {"VSX": "B/vsx/vsx", "TESS_EB": "J/ApJS/258/16", "ASASSN": "II/366", "GAIA_EB": "I/358/veb", "GAIA_CLASS": "I/358/vclassre"}
PERIOD_COLS = ("Period", "Per", "P", "period", "Porb")
TYPE_COLS = ("Type", "VarType", "Class", "Best", "Classif")


def first_col(row, names):
    for n in names:
        if n in row.colnames:
            v = row[n]
            try:
                if np.ma.is_masked(v):
                    continue
            except Exception:
                pass
            return v
    return None


def vizier_match(viz, ra, dec, cat):
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    res = viz.query_region(SkyCoord(ra * u.deg, dec * u.deg), radius=RADIUS_ARCSEC * u.arcsec, catalog=cat)
    out = []
    for tab in res:
        for row in tab:
            per = first_col(row, PERIOD_COLS)
            if per is None and "Freq" in row.colnames and not np.ma.is_masked(row["Freq"]) and float(row["Freq"]) > 0:
                per = 1.0 / float(row["Freq"])      # Gaia DR3 eclipsing binaries give a frequency (1/d)
            typ = first_col(row, TYPE_COLS)
            out.append((None if per is None else float(per), None if typ is None else str(typ)))
    return out


def simbad_type(ra, dec):
    from astroquery.simbad import Simbad
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    s = Simbad()
    try:
        s.add_votable_fields("otype")
    except Exception:
        pass
    t = s.query_region(SkyCoord(ra * u.deg, dec * u.deg), radius=RADIUS_ARCSEC * u.arcsec)
    if t is None or len(t) == 0:
        return None, None
    cols = {c.lower(): c for c in t.colnames}
    name = t[cols.get("main_id", t.colnames[0])][0]
    otype = t[cols["otype"]][0] if "otype" in cols else None
    return str(name), (None if otype is None else str(otype))


def period_relation(p_known, p_orb):
    if p_known is None or not p_orb:
        return ""
    for lab, f in (("P", 1.0), ("P/2", 0.5), ("2P", 2.0)):
        if abs(p_known - f * p_orb) / (f * p_orb) < 0.02:
            return lab
    return "different"


def main():
    from astroquery.vizier import Vizier
    viz = Vizier(columns=["*"], row_limit=20)
    rows = [json.loads(l) for l in open("pilot_results/stars.jsonl")]
    flagged = [r for r in rows if any(w.get("dip_flag") or w.get("bump_flag") for w in r["windows"])]
    det = pd.read_csv("track3_detail.csv").set_index("source_id")
    done = {}
    out_path = "pilot_results/known_check.csv"
    if os.path.exists(out_path):
        for _, x in pd.read_csv(out_path).iterrows():
            done[int(x["source_id"])] = x.to_dict()
    print(f"{len(flagged)} flagged stars in the pilot so far; {len(done)} already checked", flush=True)
    for k, r in enumerate(flagged):
        sid = int(r["source_id"])
        if sid in done:
            continue
        ra, dec = float(det.loc[sid, "ra"]), float(det.loc[sid, "dec"])
        n_dip = sum(bool(w.get("dip_flag")) for w in r["windows"]); n_bump = sum(bool(w.get("bump_flag")) for w in r["windows"])
        rec = dict(source_id=sid, type=r["type"], g=r["g"], period_orbit=r["period"], n_windows=len(r["windows"]), n_dip_flags=n_dip, n_bump_flags=n_bump)
        known = []
        for lab, cat in CATS.items():
            try:
                m = vizier_match(viz, ra, dec, cat)
            except Exception as exc:
                rec[lab] = f"query failed: {str(exc)[:40]}"; continue
            if not m:
                rec[lab] = ""; continue
            per, typ = m[0]
            rel = period_relation(per, r["period"])
            rec[lab] = f"{typ or ''} P={per:.4f} ({rel})" if per else (typ or "listed")
            known.append((lab, typ, per, rel))
            time.sleep(0.2)
        try:
            name, otype = simbad_type(ra, dec)
        except Exception:
            name, otype = None, None
        rec["SIMBAD"] = f"{name} [{otype}]" if name else ""
        eb_words = ("EA", "EB", "EW", "ECL", "E/", "ELL", "EP")
        is_eb = any((t and any(w in t.upper() for w in eb_words)) or lab in ("TESS_EB", "GAIA_EB") for lab, t, _, _ in known) or (otype and "EB" in otype.upper())
        same = any(rel in ("P", "P/2", "2P") for _, _, _, rel in known)
        rec["verdict"] = ("known eclipsing binary, same period" if is_eb and same else
                          "known eclipsing binary, other period (blend?)" if is_eb else
                          "known variable (not eclipsing)" if known else "not catalogued")
        done[sid] = rec
        pd.DataFrame(list(done.values())).to_csv(out_path, index=False)
        print(f"  [{k + 1}/{len(flagged)}] Gaia DR3 {sid} (P = {r['period']:.1f} d, {n_dip} dip / {n_bump} bump flags): {rec['verdict']}"
              + (f"  | {rec['SIMBAD']}" if rec["SIMBAD"] else ""), flush=True)
    df = pd.DataFrame(list(done.values()))
    if len(df):
        print("\nverdicts:", df["verdict"].value_counts().to_dict())
    print(f"-> {out_path}")


if __name__ == "__main__":
    main()
