"""Step 6a: Gaia DR3 neighbours within 90 arcsec (live ESA TAP), the Gaia-ECL neighbour 5307278580723030144
(vari_eclipsing_binary + vari_classifier_result), and the residual amplitude at its frequency and harmonics.
Writes s6a_out.txt, neighbours.json."""
import os, json
import numpy as np
from astropy.timeseries import LombScargle
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s6a_out.txt"), "w"))
q = (f"SELECT source_id, ra, dec, phot_g_mean_mag AS g, bp_rp, parallax, phot_variable_flag AS vf, "
     f"DISTANCE(POINT('ICRS', ra, dec), POINT('ICRS', {RA}, {DEC})) * 3600 AS sep "
     f"FROM gaiadr3.gaia_source WHERE 1 = CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {RA}, {DEC}, {90/3600})) ORDER BY sep")
nb = tap(q)
for r in nb:
    r["sep"] = float(r["sep"]); r["g"] = float(r["g"]) if r["g"] else 99.0
tg = [r for r in nb if r["source_id"] == GAIA_ID][0]
say(f"{len(nb)} Gaia sources within 90\" (target G {tg['g']:.3f}); {sum(1 for r in nb if r['sep'] <= 60)} within 60\"")
ids = ",".join(r["source_id"] for r in nb)
veb = tap(f"SELECT source_id, frequency, frequency_error, reference_time, global_ranking, derived_primary_ecl_depth, "
          f"derived_secondary_ecl_depth, model_type FROM gaiadr3.vari_eclipsing_binary WHERE source_id IN ({ids})")
vcl = tap(f"SELECT source_id, best_class_name, best_class_score FROM gaiadr3.vari_classifier_result WHERE source_id IN ({ids})")
vsum = tap(f"SELECT * FROM gaiadr3.vari_summary WHERE source_id IN ({ids})")
nss = tap(f"SELECT source_id, nss_solution_type, period FROM gaiadr3.nss_two_body_orbit WHERE source_id IN ({ids})")
say(f"vari_eclipsing_binary rows: {len(veb)}; vari_classifier_result rows: {len(vcl)}; vari_summary rows: {len(vsum)}; nss rows: {len(nss)}")
for r in veb: say("  veb", r)
for r in vcl: say("  vcl", r)
for r in vsum: say("  vsum", {k: v for k, v in r.items() if v not in ("", None, "false")})
for r in nss: say("  nss", r)
ftg = 10 ** (-0.4 * tg["g"])
A_hb = 11.0e-3       # observed peak-to-trough of the pulse in QLP SAP (s2)
A_dip = 7.0e-3
say("\nWithin 60\": G, sep, BP-RP, flux ratio to target, intrinsic depth needed to fake the 7-ppt dip (all target light in aperture)")
for r in nb:
    if r["source_id"] == GAIA_ID or r["sep"] > 60: continue
    rat = 10 ** (-0.4 * r["g"]) / ftg
    r["need"] = A_dip / rat
    flag = " <-- formally capable (<100%)" if r["need"] < 1 else ""
    say(f"  {r['source_id']}  G {r['g']:.2f}  sep {r['sep']:.1f}\"  bp_rp {r['bp_rp'] or '-':>6}  ratio {rat:.4f}  need {r['need']*100:.0f}%  {r['vf']}{flag}")
json.dump(nb, open(os.path.join(OUT, "neighbours.json"), "w"), indent=1)
ecl = [r for r in nb if r["source_id"] == "5307278580723030144"]
if ecl:
    r = ecl[0]; v = [x for x in veb if x["source_id"] == r["source_id"]]
    say(f"\nGaia-ECL neighbour 5307278580723030144: G {r['g']:.2f} at {r['sep']:.1f}\" ({r['sep']/21:.2f} TESS px); "
        f"flux ratio {10**(-0.4*r['g'])/ftg:.4f}")
    if v:
        fe = float(v[0]["frequency"]); sfe = float(v[0]["frequency_error"] or 0)
        Pe = 1 / fe
        Plc = 4.800079
        say(f"  frequency {fe:.6f} +- {sfe:.1e} c/d -> P_ecl {Pe:.6f} d; P_orb/P_ecl = {Plc/Pe:.4f}; P_orb/(2 P_ecl) = {Plc/(2*Pe):.4f}")
        say(f"  depths prim {v[0]['derived_primary_ecl_depth']} sec {v[0]['derived_secondary_ecl_depth']} mag; model {v[0]['model_type']}")
        # beat: phase drift of the neighbour's eclipse against the target's orbit per orbit
        for k in (4, 5):
            drift = (Plc - k * Pe) / Pe
            say(f"  vs {k} x P_ecl: drift {drift:+.4f} neighbour-cycles per target orbit -> full smear over {1/abs(drift):.1f} orbits ({abs(Plc/drift):.0f} d)")
        # residual amplitude at the neighbour's frequency and harmonics
        J = json.load(open(os.path.join(OUT, "s3_fit.json"))); best = J["fits"]["beam_Pfree"]
        G = gaia(); d = np.load(os.path.join(OUT, "detr.npz"))
        EXP = {9: 1800 / 86400, 10: 1800 / 86400, 36: 600 / 86400, 37: 600 / 86400, 62: 200 / 86400, 63: 200 / 86400, 89: 200 / 86400, 90: 200 / 86400}
        U = bin_series(d["t"], d["f"], d["sec"], 1e-6, EXP)
        M = Model(U, G["tp_btjd"], float(G["period"]), mode="beam", pfree=True)
        rr, coef, cov, X = M.solve(np.array(best["x"]), full=True)
        res = U["y"] - X @ coef
        for k in (1, 2, 3, 4):
            fr = np.linspace(k * fe - 0.003, k * fe + 0.003, 301)
            pw = LombScargle(U["t"], res, normalization="psd").power(fr); amp = np.sqrt(4 * pw / len(res))
            frb = np.linspace(k * fe - 0.5, k * fe + 0.5, 2001)
            pwb = LombScargle(U["t"], res, normalization="psd").power(frb); ampb = np.sqrt(4 * pwb / len(res))
            say(f"  residual amplitude near {k} f_ecl ({k*fe:.4f}): max {amp.max()*1e6:.0f} ppm at {fr[np.argmax(amp)]:.5f}; local median {np.median(ampb)*1e6:.0f} ppm")
        # BLS-like: fold residuals on P_ecl and look for a dip
        ph = ((U["t"] - float(v[0]["reference_time"] or 0) - 389.0 + 2457389.0 - 2457389.0) / Pe) % 1
        xb, yb, eb, _ = binstat(ph, res, np.linspace(0, 1, 51), minn=20)
        say(f"  residuals folded on P_ecl (50 bins): min {yb.min()*1e6:.0f} ppm at phase {xb[np.argmin(yb)]:.2f}, max {yb.max()*1e6:.0f}, bin err ~{np.median(eb)*1e6:.0f} ppm")
else:
    say("Gaia-ECL neighbour 5307278580723030144 not within 90\"; querying directly")
    r = tap("SELECT source_id, ra, dec, phot_g_mean_mag FROM gaiadr3.gaia_source WHERE source_id = 5307278580723030144")
    say(r)
