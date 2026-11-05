"""Step 1: Gaia DR3 orbit + source + astrophysical parameters, TIC, MAST inventory, downloads (QLP, SPOC, TESS-SPOC).
Writes gaia.json, tic.json, s1_out.txt, mast_inventory.txt. FITS go to %TEMP%/heartbeats/vet438089101."""
import os, json
import numpy as np
from lib import *

say = say_to(open(os.path.join(OUT, "s1_out.txt"), "w"))

n = tap(f"SELECT * FROM gaiadr3.nss_two_body_orbit WHERE source_id={GAIA_ID}")
assert len(n) == 1, n
n = n[0]
keys = ["nss_solution_type", "period", "period_error", "t_periastron", "t_periastron_error", "eccentricity",
        "eccentricity_error", "arg_periastron", "arg_periastron_error", "center_of_mass_velocity",
        "center_of_mass_velocity_error", "semi_amplitude_primary", "semi_amplitude_primary_error",
        "bit_index", "corr_vec", "goodness_of_fit", "efficiency", "significance", "flags", "obs_time_rv"]
for k in keys:
    if k in n: say(f"nss.{k} = {n[k]}")
g = tap("SELECT source_id, ra, dec, parallax, parallax_error, pmra, pmdec, phot_g_mean_mag, bp_rp, ruwe, "
        "phot_variable_flag, non_single_star, radial_velocity, radial_velocity_error, rv_nb_transits, "
        "rv_amplitude_robust, rv_chisq_pvalue, rv_renormalised_gof, rv_method_used, grvs_mag, rv_template_teff, "
        "ipd_frac_multi_peak, ipd_gof_harmonic_amplitude, visibility_periods_used, "
        "teff_gspphot, logg_gspphot, distance_gspphot, has_epoch_photometry, has_epoch_rv "
        f"FROM gaiadr3.gaia_source WHERE source_id={GAIA_ID}")[0]
for k, v in g.items(): say(f"src.{k} = {v}")
ap = tap("SELECT teff_gspphot, logg_gspphot, mh_gspphot, radius_gspphot, radius_flame, mass_flame, lum_flame, age_flame, "
         "evolstage_flame, teff_esphs, spectraltype_esphs, vsini_esphs, teff_gspspec, logg_gspspec, "
         "classprob_dsc_combmod_star, classprob_dsc_combmod_binarystar "
         f"FROM gaiadr3.astrophysical_parameters WHERE source_id={GAIA_ID}")
for k, v in (ap[0] if ap else {}).items(): say(f"ap.{k} = {v}")

# DR3 datamodel: SB1 parameter order period, center_of_mass_velocity, semi_amplitude_primary, eccentricity,
# arg_periastron, t_periastron; corr_vec = upper triangle, column-major.
names = ["period", "center_of_mass_velocity", "semi_amplitude_primary", "eccentricity", "arg_periastron", "t_periastron"]
cv = [float(x) for x in n["corr_vec"].strip("()[]").replace(",", " ").split()] if n.get("corr_vec") else []
say("corr_vec len", len(cv))
C = np.eye(len(names)); k = 0
for j in range(1, len(names)):
    for i in range(j):
        if k < len(cv): C[i, j] = C[j, i] = cv[k]; k += 1
say("correlation matrix (rows/cols:", ", ".join(names), ")")
for i in range(len(names)): say("  " + " ".join(f"{C[i, j]:+.3f}" for j in range(len(names))))
P = float(n["period"]); K1 = float(n["semi_amplitude_primary"]); e = float(n["eccentricity"])
fm = 1.0361e-7 * (1 - e * e) ** 1.5 * K1 ** 3 * P
say(f"mass function f(m) = {fm:.5f} Msun ; 2*K1 = {2*K1:.1f} km/s vs rv_amplitude_robust {g.get('rv_amplitude_robust')}")
gj = {k: n[k] for k in keys if k in n}
gj.update({"src": g, "ap": ap[0] if ap else {}, "corr": C.tolist(), "corr_names": names, "fm": fm,
           "tp_btjd": float(n["t_periastron"]) + GAIA_OFF})
json.dump(gj, open(os.path.join(OUT, "gaia.json"), "w"), indent=1)

tic = mast({"service": "Mast.Catalogs.Filtered.Tic", "format": "json",
            "params": {"columns": "*", "filters": [{"paramName": "ID", "values": [TIC]}]}})["data"][0]
for k in ("ID", "ra", "dec", "Tmag", "Teff", "e_Teff", "logg", "rad", "e_rad", "mass", "e_mass", "lum", "d", "contratio",
          "GAIA", "TYC", "HIP", "TWOMASS", "UCAC", "Vmag", "Bmag", "objType", "disposition"):
    say(f"tic.{k} = {tic.get(k)}")
json.dump(tic, open(os.path.join(OUT, "tic.json"), "w"), indent=1)

cols = "obsid,obs_collection,provenance_name,target_name,sequence_number,dataproduct_type,t_exptime,dataURL"
rows = []
for name in (TIC, f"TIC {TIC}", f"{int(TIC):016d}"):
    rows += mast({"service": "Mast.Caom.Filtered", "format": "json",
                  "params": {"columns": cols, "filters": [{"paramName": "target_name", "values": [name]}]}})["data"]
cone = mast({"service": "Mast.Caom.Cone", "format": "json", "params": {"ra": RA, "dec": DEC, "radius": 3 / 3600},
             "pagesize": 2000, "page": 1})["data"]
seen = {r["obsid"] for r in rows}
rows += [r for r in cone if r["obsid"] not in seen and r.get("obs_collection") in ("TESS", "HLSP")]
with open(os.path.join(OUT, "mast_inventory.txt"), "w") as f:
    for r in sorted(rows, key=lambda r: (str(r.get("provenance_name")), r.get("sequence_number") or 0)):
        f.write(f"{r.get('obs_collection')}\t{r.get('provenance_name')}\t{r.get('target_name')}\ts{r.get('sequence_number')}\t"
                f"{r.get('dataproduct_type')}\texp={r.get('t_exptime')}\t{r.get('dataURL')}\n")
got = []
for r in rows:
    u = r.get("dataURL") or ""
    if r.get("dataproduct_type") != "timeseries" or not u.endswith(".fits"): continue
    prov = r.get("provenance_name"); s = r.get("sequence_number")
    if prov not in ("QLP", "SPOC", "TESS-SPOC"): continue
    if str(r.get("target_name")).lstrip("0").replace("TIC ", "") != TIC: continue
    if prov == "SPOC" and not u.endswith("_lc.fits"): continue
    tag = {"QLP": "qlp", "SPOC": "spoc", "TESS-SPOC": "tspoc"}[prov]
    exp = r.get("t_exptime")
    if prov == "SPOC" and exp and float(exp) < 60: tag = "spoc20"
    p = os.path.join(DL, f"{tag}_s{int(s):03d}.fits")
    try:
        download(u, p); got.append((tag, s, exp))
    except Exception as ex:
        say("download fail", u, ex)
for x in sorted(got, key=lambda x: (x[0], x[1])): say("downloaded", x)
