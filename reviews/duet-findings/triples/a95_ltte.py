"""Does A95's eclipse timing follow Gaia's 541-d astrometric orbit in shape and phase?

Input: triples/a95-events.csv (Fable 5's 66 primary and secondary eclipse times of A95 =
TIC 154346187, from the house triples analysis whose epoch the paper adopts; sectors 16, 22,
23, 49, 50, 76, 77, none in a clock-fault sector) and Gaia's orbit (Fable 5.1's NSS export:
P3, e, T_peri, and w from the Thiele-Innes elements). Gaia's T_peri is days from J2016.0
(BTJD 389.0).
Fits, for each eclipse family separately and both together (separate T0 and P per family):
  flat:  linear ephemeris only
  gaia:  + light-travel term with Gaia's P3, e, T_peri and w fixed; only the amplitude (and
         its sign) free
  free:  + light-travel term with Gaia's P3 and e, phase and amplitude free
The gaia fit tests whether the timing has Gaia's shape and phase; free-minus-gaia chi2 says
how much phase freedom buys. Errors are inflated to reduced chi2 = 1 of the free fit.
usage (from the repo root): python3 reviews/duet-findings/triples/a95_ltte.py
"""
import csv, math
import numpy as np, pandas as pd

r = [x for x in csv.DictReader(open('reviews/duet-findings/gaia-errors/fable51-nss-appointments.csv'))
     if x['review_id'] == 'A95' and x['nss_solution_type'] == 'Orbital'][0]
A, B, F, G = (float(r[k + '_thiele_innes']) for k in 'abfg')
u = (A * A + B * B + F * F + G * G) / 2; v = A * G - B * F; a0 = math.sqrt(u + math.sqrt((u + v) * (u - v)))
w = ((math.atan2(B - F, A + G)) + math.atan2(-B - F, A - G)) / 2
P3 = float(r['period']); e = float(r['eccentricity']); tp = float(r['t_periastron']) + 389.0
ev = pd.read_csv('reviews/duet-findings/triples/a95-events.csv')


def kepler(M, e):
    E = M.copy()
    for _ in range(40):
        E -= (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E


def shape(t, tp_, w_):
    """Irwin's light-travel term per unit K: r/(a) sin(nu + w) + e sin w, r/a = (1-e^2)/(1+e cos nu)"""
    nu = 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(kepler(np.mod(2 * np.pi * (t - tp_) / P3, 2 * np.pi), e) / 2))
    return (1 - e ** 2) / (1 + e * np.cos(nu)) * np.sin(nu + w_) + e * np.sin(w_)


def design(df, extra):
    cols = []
    for k in ('p', 's'):
        m = (df.kind == k).values.astype(float)
        if m.any():
            cols += [m, m * df.cycle.values]
    return np.column_stack(cols + extra)


def wls(X, y, s):
    c = np.linalg.lstsq(X / s[:, None], y / s, rcond=None)[0]
    return np.sum(((y - X @ c) / s) ** 2), c


print(f'Gaia: P3 = {P3:.1f} d, e = {e:.3f}, T_peri = BTJD {tp:.1f}, w = {math.degrees(w) % 360:.0f} deg (photocentre); '
      f'events {len(ev)} ({(ev.kind == "p").sum()} primaries)')
for name, df in (('primaries', ev[ev.kind == 'p']), ('secondaries', ev[ev.kind == 's']), ('both', ev)):
    t = df.t_btjd.values; s0 = df.err_d.values
    # free phase: shape with w and tp free is linear in K cos w', K sin w' at fixed tp
    best = None
    for tq in tp + P3 * np.arange(0, 1, 1 / 72):
        Xf = design(df, [shape(t, tq, 0.0), shape(t, tq, np.pi / 2)])
        c2, c = wls(Xf, t, s0)
        if best is None or c2 < best[0]:
            best = (c2, c, tq)
    nfree = design(df, []).shape[1] + 3
    jit = math.sqrt(max(best[0] / (len(t) - nfree) - 1, 0)) * np.median(s0)
    s = np.hypot(s0, jit)
    c2_flat, _ = wls(design(df, []), t, s)
    Xg = design(df, [shape(t, tp, w)]); c2_gaia, cg = wls(Xg, t, s)
    cg_err = math.sqrt(np.linalg.inv((Xg / s[:, None]).T @ (Xg / s[:, None]))[-1, -1])
    best = None
    for tq in tp + P3 * np.arange(0, 1, 1 / 360):
        c2, c = wls(design(df, [shape(t, tq, 0.0), shape(t, tq, np.pi / 2)]), t, s)
        if best is None or c2 < best[0]:
            best = (c2, c, tq)
    c2_free, cf, tq = best
    K = math.hypot(cf[-2], cf[-1]); wf = math.atan2(cf[-1], cf[-2])
    amp = lambda K_, w_: K_ * math.sqrt(1 - (e * math.cos(w_)) ** 2) * 1440
    # phase of the free fit expressed as the time of maximum delay, against Gaia's
    tt = np.linspace(tp, tp + P3, 4000)
    tmax_g = tt[np.argmax(np.sign(cg[-1]) * shape(tt, tp, w))]; tmax_f = tt[np.argmax(cf[-2] * shape(tt, tq, 0) + cf[-1] * shape(tt, tq, np.pi / 2))]
    dph = ((tmax_f - tmax_g + P3 / 2) % P3) - P3 / 2
    print(f'{name:11s}: {len(t)} events, jitter {jit * 86400:.0f} s; chi2 flat {c2_flat:.1f}, gaia-fixed {c2_gaia:.1f} (1 more parameter), '
          f'free phase {c2_free:.1f} (3 more)')
    print(f'             gaia-fixed amplitude {amp(abs(cg[-1]), w):.2f} +- {amp(cg_err, w):.2f} min (sign {"+" if cg[-1] > 0 else "-"}); free amplitude {amp(K, wf):.2f} min, '
          f'its maximum delay {dph:+.0f} d from the gaia-fixed one ({dph / P3 * 360:+.0f} deg)')
print('Gaia photocentre lower bound on the amplitude: 3.25 min (68%: 3.01-3.54; ltte_from_astrometry.py); the paper: 3.4 +- 0.3')
