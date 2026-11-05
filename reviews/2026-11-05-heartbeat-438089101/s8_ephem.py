"""Step 8: next periastra, A/B conjunctions and the flux minimum, from the emcee chain of the tide+beam fit on the
light-curve ephemeris (s3b_chain.npy), after BTJD 4326.5 (2026-10-13) and after 4348.5 (2026-11-04).
Also the light-curve periastron near each TESS season and the Gaia comparison. Writes s8_out.txt, ephem.json."""
import os, json
import numpy as np
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s8_out.txt"), "w"))
G = gaia(); P0 = float(G["period"]); sPG = float(G["period_error"]); tp0 = G["tp_btjd"]; stpG = float(G["t_periastron_error"])
ch = np.load(os.path.join(OUT, "s3b_chain.npy"))
tp_c = tp0 + ch[:, 0]; P_c = P0 + ch[:, 1]; e_c = ch[:, 2]; w_c = ch[:, 3]
J = json.load(open(os.path.join(OUT, "s3b.json")))
sP_bs = J["bs_sigma"]["P"]; sP_jk = J["jk_sigma"]["P"]; stp_bs = J["bs_sigma"]["tp"]
# reference epoch near the data centre to decorrelate
Nref = int(round((3000 - np.median(tp_c)) / np.median(P_c)))
T_ref = tp_c + Nref * P_c
Pm, sPm = np.median(P_c), max(np.std(P_c), sP_bs, sP_jk)
Tm, sTm = np.median(T_ref), max(np.std(T_ref), stp_bs)
say(f"light-curve ephemeris: T_peri(N={Nref}) = BTJD {Tm:.4f} +- {sTm:.4f}, P = {Pm:.6f} +- {sPm:.6f} (errors = max of emcee, passage bootstrap, sector jackknife)")
say(f"   = BJD_TDB {Tm+2457000:.4f}; Gaia P {P0:.6f} +- {sPG:.6f} -> {(Pm-P0)/sPG:+.2f} sigma_G")
# Gaia's periastron extrapolated to N_ref vs the light curve
Tg = tp0 + Nref * P0; sTg = np.hypot(stpG, Nref * sPG)
say(f"Gaia Tp extrapolated to N={Nref}: {Tg:.3f} +- {sTg:.3f}; light curve - Gaia = {Tm-Tg:+.3f} d = {(Tm-Tg)/sTg:+.2f} sigma; "
    f"at Gaia's own epoch N=0 the light-curve ephemeris gives {Tm - Nref*Pm:.3f} +- {np.hypot(sTm, Nref*sPm):.3f} vs Gaia {tp0:.3f} +- {stpG:.3f}")
e, w = np.median(e_c), np.median(w_c)
fA, fB = conj_phase(e, np.degrees(w), "A"), conj_phase(e, np.degrees(w), "B")
best = json.load(open(os.path.join(OUT, "s3_fit.json")))["fits"]["beam_Pfree"]
tt = np.linspace(-0.5, 0.5, 20001) * Pm
mdl = tide(tt, 0, Pm, best["e"], np.radians(best["w"]), np.radians(best["i"]), best["S"]) + beam(tt, 0, Pm, best["e"], np.radians(best["w"]), best["Bm"])
tmin = tt[np.argmin(mdl)]; tmax1 = tt[np.argmax(np.where(tt < tmin, mdl, -1))]; tmax2 = tt[np.argmax(np.where(tt > tmin, mdl, -1))]
say(f"conjunction A at +{fA*Pm:.3f} d after periastron, B at +{fB*Pm:.3f} d; model minimum {tmin:+.3f} d, humps {tmax1:+.3f} and {tmax2:+.3f} d; "
    f"peak-to-trough {(mdl.max()-mdl.min())*1e3:.2f} ppt")
out = {"T_ref": Tm, "sT_ref": sTm, "P": Pm, "sP": sPm, "N_ref": Nref}
for start in (4326.5, 4348.5):
    n0 = int(np.ceil((start - Tm) / Pm))
    rows = []
    for n in range(n0, n0 + 6):
        tpn = Tm + n * Pm; s = np.hypot(sTm, n * sPm)
        rows.append((round(tpn, 3), round(s, 3), round(tpn + tmin, 3), round(tpn + fA * Pm, 3), round(tpn + fB * Pm, 3)))
    say(f"after BTJD {start}: periastron (+-), dip, A, B:")
    for r in rows: say(f"   {r[0]:.3f} +- {r[1]:.3f}   dip {r[2]:.3f}   A {r[3]:.3f}   B {r[4]:.3f}")
    out[str(start)] = rows
json.dump(out, open(os.path.join(OUT, "ephem.json"), "w"), indent=1)
