#!/usr/bin/env python3
"""Track 3, detailed feasibility: near-edge-on Gaia DR3 astrometric orbits and TESS.

For the orbits measured within --limit-deg of edge-on (default 1 deg) and brighter than --gmax:
  1. fetch from the Gaia archive the uncertainties of the orbital elements (period, periastron time,
     eccentricity, Thiele-Innes constants) and the coordinates;
  2. propagate them by Monte Carlo (independent errors) to the inclination and to the times of the two
     conjunctions at the TESS epochs (an astrometric orbit does not tell which conjunction is the primary
     eclipse: both are searched);
  3. ask MAST which TESS light curves (SPOC, TESS-SPOC, QLP) exist for each star, with their time spans;
  4. combine: probability that the system eclipses (from the inclination and its uncertainty) times the
     expected number of conjunctions falling inside the observed TESS time spans.

Usage (on the Mac, from the folder of track3_astrometric_orbits_1.csv):
  caffeinate -i python3 feas_track3_detail.py --orbits track3_astrometric_orbits_1.csv [--workers 8]
Resumable: the MAST answers are cached in track3_mast_cache.jsonl; rerun to continue after a stop.
Output: track3_detail.csv (one row per star) and track3_detail_summary.txt.
"""
import argparse, json, math, os, sys, time, warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np
import pandas as pd

REF_BTJD = 389.0          # DR3 t_periastron is relative to BJD 2457389.0
MJD_TO_BTJD = -56999.5    # BTJD = MJD + 2400000.5 - 2457000


def retry(fn, label, tries=5, wait=30):
    for k in range(tries):
        try:
            return fn()
        except Exception as exc:
            print(f"  {label}: attempt {k + 1} failed ({str(exc).splitlines()[0][:90]}); retrying in {wait} s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"{label}: no answer")


# ------------------------------------------------------------------ orbit geometry
def ti_to_elements(A, B, F, G):
    """Thiele-Innes -> (a, i, omega, Omega) in degrees; (omega, Omega) has the usual 180 deg ambiguity."""
    u = 0.5 * (A ** 2 + B ** 2 + F ** 2 + G ** 2); v = A * G - B * F
    a = np.sqrt(u + np.sqrt(np.maximum((u + v) * (u - v), 0)))
    i = np.degrees(np.arccos(np.clip(v / a ** 2, -1, 1)))
    wpO = np.arctan2(B - F, A + G); wmO = np.arctan2(-B - F, A - G)
    w = np.degrees(0.5 * (wpO + wmO)) % 360; O = np.degrees(0.5 * (wpO - wmO)) % 360
    return a, i, w, O


def conj_times(P, e, w_deg, tp):
    """Times of the two conjunctions following tp (true anomalies 90 - w and 270 - w)."""
    out = []
    for nu0 in (90.0, 270.0):
        nu = np.radians(nu0 - w_deg)
        E = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2))
        M = E - e * np.sin(E)
        out.append(tp + (np.mod(M, 2 * np.pi) / (2 * np.pi)) * P)
    return out


def eclipse_limit_deg(P, M=1.3, R=1.2):
    a_rsun = 215.032 * (M * (P / 365.25) ** 2) ** (1 / 3)
    return np.degrees(np.arcsin(np.clip(R / a_rsun, 0, 1)))


# ------------------------------------------------------------------ steps
def gaia_elements(ids):
    from astroquery.gaia import Gaia
    Gaia.ROW_LIMIT = -1
    cols = ("n.source_id, n.nss_solution_type, n.period, n.period_error, n.eccentricity, n.eccentricity_error, "
            "n.t_periastron, n.t_periastron_error, n.a_thiele_innes, n.a_thiele_innes_error, n.b_thiele_innes, "
            "n.b_thiele_innes_error, n.f_thiele_innes, n.f_thiele_innes_error, n.g_thiele_innes, n.g_thiele_innes_error, "
            "g.ra, g.dec, g.phot_g_mean_mag AS g")
    parts = []
    for k in range(0, len(ids), 400):
        chunk = ", ".join(str(int(x)) for x in ids[k:k + 400])
        q = (f"SELECT {cols} FROM gaiadr3.nss_two_body_orbit AS n JOIN gaiadr3.gaia_source AS g "
             f"ON g.source_id = n.source_id WHERE n.source_id IN ({chunk})")
        res = retry(lambda: Gaia.launch_job(q).get_results().to_pandas(), f"Gaia chunk {k // 400 + 1}")
        print(f"  Gaia chunk {k // 400 + 1}: {len(res)} rows", flush=True)
        parts.append(res)
    return pd.concat(parts, ignore_index=True)


def monte_carlo(row, rng, n=2000, epochs=(1600.0, 3100.0)):
    def draw(col):
        v, s = row[col], row.get(col + "_error", np.nan)
        s = 0.0 if not np.isfinite(s) else s
        return rng.normal(v, s, n)
    A, B, F, G = draw("a_thiele_innes"), draw("b_thiele_innes"), draw("f_thiele_innes"), draw("g_thiele_innes")
    P = np.abs(draw("period")); e = np.clip(draw("eccentricity"), 0, 0.95); tp = REF_BTJD + draw("t_periastron")
    _, inc, w, _ = ti_to_elements(A, B, F, G)
    d90 = np.abs(inc - 90.0)
    lim = eclipse_limit_deg(P)
    p_ecl = float(np.mean(d90 < lim))                     # probability that the true inclination allows an eclipse
    out = {"sigma_i_deg": float(np.std(inc)), "p_eclipse": p_ecl}
    c1, c2 = conj_times(P, e, w, tp)
    for ep in epochs:
        for lab, c in (("c1", c1), ("c2", c2)):
            k = np.round((ep - c) / P)
            t = c + k * P
            t = t - P * np.round((t - np.median(t)) / P)   # same cycle for every draw
            out[f"sigma_t_{lab}_{int(ep)}"] = float(np.std(t))
    out["_P"] = float(np.median(P)); out["_c"] = (float(np.median(c1)), float(np.median(c2)))
    out["_sig"] = (out["sigma_t_c1_3100"], out["sigma_t_c2_3100"])
    return out


def mast_coverage(ra, dec):
    from astroquery.mast import Observations
    t = Observations.query_criteria(coordinates=f"{ra} {dec}", radius="0.003 deg",
                                    obs_collection=["TESS", "HLSP"], dataproduct_type="timeseries")
    spans = []
    for r in t:
        prov = str(r["provenance_name"]).upper()
        if prov in ("SPOC", "TESS-SPOC", "QLP"):
            spans.append((float(r["t_min"]) + MJD_TO_BTJD, float(r["t_max"]) + MJD_TO_BTJD, prov))
    return spans


def expected_covered(P, c, sig, spans):
    """Expected number of conjunctions (of one kind) whose true time falls inside the observed spans."""
    from math import erf, sqrt
    tot = 0.0
    sig = max(sig, 0.05)
    for t0, t1, _ in spans:
        k0 = math.floor((t0 - 5 * sig - c) / P); k1 = math.ceil((t1 + 5 * sig - c) / P)
        for k in range(k0, k1 + 1):
            m = c + k * P
            tot += 0.5 * (erf((t1 - m) / (sqrt(2) * sig)) - erf((t0 - m) / (sqrt(2) * sig)))
    return tot


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--orbits", default="track3_astrometric_orbits_1.csv")
    ap.add_argument("--limit-deg", type=float, default=1.0); ap.add_argument("--gmax", type=float, default=14.0)
    ap.add_argument("--no-mast", action="store_true", help="skip the MAST step (uncertainties only)")
    ap.add_argument("--workers", type=int, default=8, help="parallel MAST requests (default 8)")
    ap.add_argument("--ids-file", default=None, help="CSV with a source_id column: take these stars instead of the inclination cut")
    ap.add_argument("--out", default="track3_detail.csv", help="output file (default track3_detail.csv)")
    ap.add_argument("--far-from-edge-on", type=float, default=None, metavar="DEG",
                    help="control sample: orbits whose inclination is at least DEG from 90 (no eclipse possible)")
    ap.add_argument("--sample", type=int, default=0, help="random subsample of that size (control sample)")
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()
    t = pd.read_csv(a.orbits)
    if a.far_from_edge_on is not None:
        sel = t[(np.abs(t["inclination_deg"] - 90) >= a.far_from_edge_on) & (t["g"] < a.gmax)].reset_index(drop=True)
        if a.sample and a.sample < len(sel):
            sel = sel.sample(a.sample, random_state=a.seed).reset_index(drop=True)
        print(f"control sample: {len(sel)} orbits at least {a.far_from_edge_on} deg from edge-on and G < {a.gmax}", flush=True)
    elif a.ids_file:
        ids = set(pd.read_csv(a.ids_file)["source_id"].astype("int64"))
        sel = t[t["source_id"].isin(ids)].reset_index(drop=True)
        print(f"{len(sel)} of the {len(ids)} listed stars have a Gaia DR3 astrometric orbit", flush=True)
    else:
        sel = t[(np.abs(t["inclination_deg"] - 90) < a.limit_deg) & (t["g"] < a.gmax)].reset_index(drop=True)
        print(f"{len(sel)} orbits within {a.limit_deg} deg of edge-on and G < {a.gmax}", flush=True)
    el = gaia_elements(sel["source_id"].tolist())
    astro = ("Orbital", "AstroSpectroSB1", "OrbitalTargetedSearch", "OrbitalTargetedSearchValidated")
    n0 = len(el)
    el = el[el["nss_solution_type"].isin(astro) & el["a_thiele_innes"].notna()].drop_duplicates("source_id").reset_index(drop=True)
    print(f"  {n0} rows from the archive -> {len(el)} astrometric solutions (one per star)", flush=True)
    rng = np.random.default_rng(20261011)
    rows = []
    for _, r in el.iterrows():
        mc = monte_carlo(r, rng)
        rows.append({"source_id": int(r["source_id"]), "type": r["nss_solution_type"], "ra": r["ra"], "dec": r["dec"],
                     "g": r["g"], "period": r["period"], **{k: v for k, v in mc.items() if not k.startswith("_")},
                     "_P": mc["_P"], "_c": mc["_c"], "_sig": mc["_sig"]})
    print(f"Monte Carlo done for {len(rows)} orbits", flush=True)
    cache = {}
    if os.path.exists("track3_mast_cache.jsonl"):
        for line in open("track3_mast_cache.jsonl"):
            d = json.loads(line); cache[d["source_id"]] = d["spans"]
    if not a.no_mast:
        todo = [r for r in rows if r["source_id"] not in cache]
        print(f"MAST: {len(cache)} stars already cached, {len(todo)} to query with {a.workers} parallel requests", flush=True)
        warnings.filterwarnings("ignore")
        def job(r):
            try:
                return r["source_id"], retry(lambda: mast_coverage(r["ra"], r["dec"]), f"MAST {r['source_id']}", tries=3, wait=10)
            except Exception:
                return r["source_id"], None
        t0 = time.time(); done = 0; failed = 0
        with open("track3_mast_cache.jsonl", "a") as fh, ThreadPoolExecutor(a.workers) as ex:
            for fut in as_completed([ex.submit(job, r) for r in todo]):
                sid, spans = fut.result()
                done += 1
                if spans is None:
                    failed += 1; continue
                cache[sid] = spans
                fh.write(json.dumps({"source_id": sid, "spans": spans}) + "\n"); fh.flush()
                if done % 50 == 0:
                    rate = done / (time.time() - t0) * 60
                    print(f"  MAST: {done}/{len(todo)} stars ({rate:.0f} per minute, about {(len(todo) - done) / max(rate, 1e-6):.0f} min left)", flush=True)
        if failed:
            print(f"  MAST: {failed} stars failed; rerun the same command to retry them", flush=True)
    for r in rows:
        spans = cache.get(r["source_id"], [])
        r["n_lightcurves"] = len(spans)
        r["exp_conj_covered"] = sum(expected_covered(r["_P"], c, s, spans) for c, s in zip(r["_c"], r["_sig"]))
        r["exp_detectable"] = r["p_eclipse"] * min(1.0, r["exp_conj_covered"])
    df = pd.DataFrame([{k: v for k, v in r.items() if not k.startswith("_")} for r in rows])
    df.to_csv(a.out, index=False)
    label = (f"{len(df)} control orbits at least {a.far_from_edge_on} deg from edge-on (G < {a.gmax})" if a.far_from_edge_on is not None
             else f"{len(df)} listed orbits" if a.ids_file else f"{len(df)} near-edge-on astrometric orbits (|i-90| < {a.limit_deg} deg, G < {a.gmax})")
    lines = [label,
             f"inclination uncertainty (MC, independent errors): median {df.sigma_i_deg.median():.2f} deg, quartiles {df.sigma_i_deg.quantile(0.25):.2f}-{df.sigma_i_deg.quantile(0.75):.2f}",
             f"conjunction time uncertainty at 2023 (BTJD 3100): median {df.sigma_t_c1_3100.median():.1f} d; "
             f"< 1 d for {(df.sigma_t_c1_3100 < 1).sum()}, < 3 d for {(df.sigma_t_c1_3100 < 3).sum()}, < 10 d for {(df.sigma_t_c1_3100 < 10).sum()}",
             f"expected eclipsing systems (sum of p_eclipse): {df.p_eclipse.sum():.0f}",
             f"stars with at least one TESS light curve: {(df.n_lightcurves > 0).sum()}",
             f"expected conjunctions inside TESS coverage per star: median {df.exp_conj_covered.median():.2f}",
             f"EXPECTED DETECTABLE ECLIPSING SYSTEMS (p_eclipse x coverage): {df.exp_detectable.sum():.1f}",
             f"  of which AstroSpectroSB1 (radial velocities too): {df[df.type == 'AstroSpectroSB1'].exp_detectable.sum():.1f}"]
    open(a.out.replace(".csv", "_summary.txt"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
