"""Five accepted systems eclipse on the orbit Gaia DR3 solved astrometrically: A19 (290.9 d),
A72 (215.0 d), A74 (173.9 d), and A5 and A20 (19.45 and 26.38 d, also Gaia SB1s). Eclipses on
these orbits fix the inclination near 90 deg and the conjunction times, so they test Gaia's
astrometric orbits the way the SB1 conjunctions test the spectroscopic ones.

For each: Gaia's Thiele-Innes elements, e, P and T_peri (days from 2016.0 = BTJD 389.0) with
their full covariance (corr_vec order ra, dec, parallax, pmra, pmdec, A, B, F, G, e, P, T_peri)
are drawn 20,000 times; each draw gives i, omega and the two conjunction times nearest 2016.
The eclipse ephemeris (CHECKCARD.csv) is carried back to the nearer conjunction. The inclination
an eclipse allows is generous: |cos i| <= (R1 + R2) (1 + e) / (a (1 - e^2)) with R2 <= R1 (TIC radius),
and a from Kepler's law with the TIC mass alone (the smallest a). For A5 and A20 the astrometric
orbit is compared with Gaia's own SB1 at the same period (a0 against a1 sin i, and e).
Run from the repository root: python3 reviews/duet-findings/gaia-geometry/astrometric_eclipsers.py
"""
import csv, math
import numpy as np

NSS = 'reviews/duet-findings/gaia-errors/fable51-nss-appointments.csv'
rng = np.random.default_rng(7)
card = {r['label'].strip(): r for r in csv.DictReader(open('CHECKCARD.csv'))}
tic = {r['ID']: r for r in csv.DictReader(open('reviews/duet-findings/masses/tic-records.csv'))}
acc = {r['review_id']: r['tic'] for r in csv.DictReader(open('accepted-systems.csv'))}
sb1 = {r['review_id']: r for r in csv.DictReader(open(NSS)) if r['nss_solution_type'] == 'SB1'}
rows = [r for r in csv.DictReader(open(NSS)) if r['nss_solution_type'].startswith('Orbital')
        and r['review_id'] in ('A5', 'A19', 'A20', 'A72', 'A74')]
NAMES = ['ra', 'dec', 'parallax', 'pmra', 'pmdec', 'a_thiele_innes', 'b_thiele_innes', 'f_thiele_innes',
         'g_thiele_innes', 'eccentricity', 'period', 't_periastron']


def elements(A, B, F, G):
    u = (A * A + B * B + F * F + G * G) / 2
    v = A * G - B * F
    a0 = np.sqrt(u + np.sqrt((u + v) * (u - v)))
    i = np.arccos(np.clip(v / a0 ** 2, -1, 1))
    w = (np.arctan2(B - F, A + G) + np.arctan2(-B - F, A - G)) / 2
    return a0, i, w


def conj(P, e, w, tp, which):
    nu = (np.pi / 2 if which == 0 else 3 * np.pi / 2) - w
    E = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2))
    return tp + np.mod(E - e * np.sin(E), 2 * np.pi) / (2 * np.pi) * P


out = []
for r in sorted(rows, key=lambda x: int(x['review_id'][1:])):
    lab = r['review_id']
    mu = np.array([float(r[n]) if n not in ('ra', 'dec') else 0.0 for n in NAMES])
    sd = np.array([float(r[n + '_error']) / (3.6e6 if n in ('ra', 'dec') else 1) if r[n + '_error'] else 0 for n in NAMES])
    vals = [float(x) for x in r['corr_vec'].strip('{}[]()').split(',')]
    C = np.eye(12); z = 0
    for i in range(1, 12):
        for j in range(i):
            C[i, j] = C[j, i] = vals[z]; z += 1
    cov = C * np.outer(sd, sd)
    d = rng.multivariate_normal(mu, cov, 20000, method='eigh')
    A, B, F, G, e, P, tp = d[:, 5], d[:, 6], d[:, 7], d[:, 8], np.clip(d[:, 9], 0, 0.95), d[:, 10], d[:, 11] + 389.0
    a0, inc, w = elements(A, B, F, G)
    a00, inc0, w0 = elements(*mu[5:9])
    Pg, eg, tpg = mu[10], mu[9], mu[11] + 389.0
    c = card[lab]
    Pe, T0 = float(c['P_days']), float(c['T0_primary_BTJD'])
    T14 = float(c['duration_h']) / 24
    best = None
    for which in (0, 1):
        tc0 = conj(Pg, eg, w0, tpg, which)
        n = round((tc0 - T0) / Pe)
        tc = conj(P, e, w, tp, which)
        off = (tc - (T0 + n * Pe) + Pe / 2) % Pe - Pe / 2  # wrap draws around the eclipse
        o, s = float(np.median(off)), float(np.std(off))
        if best is None or abs(o) / s < abs(best[1]) / best[2]:
            best = (which, o, s)
    i_med, i_sd = math.degrees(inc0), float(np.degrees(np.std(inc)))
    t = tic[acc[lab]]
    R1, M1 = float(t['rad']), float(t['mass'])
    a_rsun = (M1 * (Pe / 365.25) ** 2) ** (1 / 3) * 215.032
    allowed = math.degrees(math.asin(min(1.0, 2 * R1 * (1 + eg) / (a_rsun * (1 - eg ** 2)))))
    extra = ''
    if lab in sb1:
        q = sb1[lab]
        K, Ps, es = float(q['semi_amplitude_primary']), float(q['period']), float(q['eccentricity'])
        a1 = K * Ps * 86400 * math.sqrt(1 - es * es) / (2 * math.pi) / 1.495979e8
        plx = float(r['parallax'])
        extra = (f"; SB1 e {es:.3f} +- {float(q['eccentricity_error']):.3f} (astrometric {eg:.3f} +- {float(r['eccentricity_error']):.3f}),"
                 f" a1 sin i {a1:.4f} au against a0 {float(a00) / plx:.4f} au (16-84%: {np.percentile(a0 / d[:, 2], 16):.4f}-{np.percentile(a0 / d[:, 2], 84):.4f})")
    zi = (abs(i_med - 90) - allowed) / i_sd if abs(i_med - 90) > allowed else 0.0
    ti_err = max(sd[5:9]) / float(a00)
    degenerate = ti_err > 10  # Thiele-Innes errors far above the orbit itself: i and omega are not usable
    if degenerate:
        zi = float('nan')
    zp = (Pg - Pe) / float(r['period_error'])
    out.append(dict(review_id=lab, solution=r['nss_solution_type'], P_ecl=Pe, P_gaia=round(Pg, 4), sigma_P=round(float(r['period_error']), 4),
                    z_period=round(zp, 2), e=round(eg, 3), sigma_e=round(float(r['eccentricity_error']), 3),
                    inc_deg=round(i_med, 1), sigma_inc=round(i_sd, 1), allowed_from_90=round(allowed, 2), z_inc=round(zi, 2),
                    a0_mas=round(float(a00), 3), conj=best[0], offset_d=round(best[1], 2), sigma_conj_d=round(best[2], 2),
                    z_conj=round(best[1] / best[2], 2), significance=r['significance'], gof=r['goodness_of_fit']))
    o = out[-1]
    print(f"{lab:4s} {o['solution']:31s} P {Pe:9.4f} vs Gaia {o['P_gaia']:9.4f} +- {o['sigma_P']:.4f} (z {o['z_period']:+.1f}) | "
          f"i {o['inc_deg']:5.1f} +- {o['sigma_inc']:4.1f} (eclipse needs 90 +- {allowed:.1f}; z {zi:.1f}) | "
          f"nearer conjunction {o['offset_d']:+7.2f} +- {o['sigma_conj_d']:.2f} d (z {o['z_conj']:+.1f}) | e {o['e']:.3f}, sig {float(o['significance']):.1f}, GoF {float(o['gof']):.1f}"
          f" | TIC R1 {R1:.2f}, M1 {M1:.2f}" + extra
          + (f" | DEGENERATE: Thiele-Innes errors {ti_err:.0f} times a0, so i, omega and the conjunction are not tested" if degenerate else ''))
ok = [o for o in out if not math.isnan(o['z_inc'])]
pulls = [o['z_period'] for o in ok] + [(o['inc_deg'] - 90) / o['sigma_inc'] for o in ok] + [o['z_conj'] for o in ok]
print(f"usable solutions: {', '.join(o['review_id'] for o in ok)}; rms of their {len(pulls)} pulls (period, i - 90, conjunction) "
      f"{math.sqrt(np.mean(np.square(pulls))):.2f}")
with open('reviews/duet-findings/gaia-geometry/astrometric-eclipsers.csv', 'w', newline='') as fh:
    wr = csv.DictWriter(fh, fieldnames=list(out[0]), lineterminator='\n'); wr.writeheader(); wr.writerows(out)
