"""Does Gaia's RUWE match the sky wobble that the light-travel orbits imply?

A light-travel orbit gives a12 sin i, the inner binary's orbit about the triple's centre of mass.
At parallax p (mas) the binary's photocentre then moves by a12 * p mas on the sky (a dark or faint
tertiary; a tertiary's own light only shrinks it). Gaia DR3's RUWE comes from a five-parameter
single-star fit over BTJD -136.1 to 901.5, so the part of the wobble that position, proper motion
and parallax cannot absorb shows up as RUWE^2 - 1 ~ (residual rms / sigma_AL)^2.

Model: 35 field-of-view transits at random times in the DR3 span, random scan angles, an Earth on
a circular orbit for the parallax factor; the five-parameter fit is solved exactly. The orbit's
phase comes from the timing fit; the node angle Omega is drawn uniformly, and i is set on a grid
(a12 = a12 sin i / sin i). sigma_AL per CCD is taken as 0.10 mas at G 12-12.6 (results also for
0.06 and 0.20: the scale is the main uncertainty). Circular orbits for R630, R423 and R371 are
refitted here from etv4-times.csv at the periods that etv_orbits.py allows (Delta chi2 < 4);
R623's eccentric branches come from r623-gaia-branches.csv.
A luminous tertiary moves the photocentre the other way: the wobble is a12 (1 - beta / f) with f the
tertiary's mass fraction and beta its light fraction. For each inclination the tertiary mass comes
from f(m3) and the inner masses, and its light from a main-sequence mass-luminosity law (L = M^4 above
0.43 Msun, 0.23 M^2.3 below; bolometric, which overstates an M dwarf's G-band share, so it errs toward
more dilution and lower allowed inclinations). A white-dwarf tertiary would add no light.

Run from the repository root: python3 reviews/duet-findings/timing/ruwe_wobble.py
"""
import csv, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
C_AU_S = 499.004784   # light seconds per au
T0, T1 = -136.1, 901.5  # Gaia DR3 span, BTJD
NT, NREAL = 35, 200
SIG = (0.06, 0.10, 0.20)
JIT = dict(R630=45.0, R423=0.0, R371=52.0)
M_IN = dict(R630=(1.06, 0.64), R423=(0.929, 0.561), R371=(2.05, 1.23), R623=(0.64, 0.41))   # (M1, M2): etv_orbits.py and r623_gaia_branches.py
INCS = (90, 80, 70, 60, 50, 40, 30)
rng = np.random.default_rng(20261126)

acc = {r['review_id']: r for r in csv.DictReader(open('accepted-systems.csv'))}
gaia = {r['review_id']: r for r in csv.DictReader(open(os.path.join(HERE, 'gaia-ruwe-r-systems.csv')))}


def kepler(M, e):
    E = M.copy()
    for _ in range(60):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E


def orbit_xyz(t, P, e, w, tp, a, inc, Om):
    """Sky (X, Y) in units of a, for argument of latitude u = nu + w measured so Z = r sin u sin i."""
    M = 2 * np.pi * (t - tp) / P
    E = kepler(np.mod(M, 2 * np.pi), e)
    nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
    r = a * (1 - e * np.cos(E))
    u = nu + w
    X = r * (np.cos(Om) * np.cos(u) - np.sin(Om) * np.sin(u) * np.cos(inc))
    Y = r * (np.sin(Om) * np.cos(u) + np.cos(Om) * np.sin(u) * np.cos(inc))
    return X, Y


def gaia_epochs(ra, dec):
    t = np.sort(rng.uniform(T0, T1, NT))
    th = rng.uniform(0, np.pi, NT)
    lam = 2 * np.pi * (t - 1197.0) / 365.25 + np.pi    # Sun's longitude ~0 near March 20 2019 (BTJD 1563 - 365.25)
    eps = math.radians(23.44)
    X, Y, Z = np.cos(lam), np.sin(lam) * math.cos(eps), np.sin(lam) * math.sin(eps)
    a, d = math.radians(ra), math.radians(dec)
    pa = X * math.sin(a) - Y * math.cos(a)
    pd = X * math.cos(a) * math.sin(d) + Y * math.sin(a) * math.sin(d) - Z * math.cos(d)
    ty = (t - 389.0) / 365.25
    s, c = np.sin(th), np.cos(th)
    D = np.column_stack([s, c, s * ty, c * ty, s * pa + c * pd])
    return t, s, c, D


def residual_rms(t, s, c, D, X, Y):
    w = X * s + Y * c
    coef = np.linalg.lstsq(D, w, rcond=None)[0]
    return math.sqrt(np.mean((w - D @ coef) ** 2))


def circ_fits(rid):
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'etv4-times.csv'))) if r['rid'] == rid]
    if rid == 'R630':   # R630's two sector-15 times on TESS-SPOC, as in etv_orbits.py
        sp = [r for r in csv.DictReader(open(os.path.join(HERE, 's1415-tspoc-times.csv')))
              if r['flag'] == 'ok' and r['sector'] == '15' and r['tic'] == rows[0]['tic']]
        for r in rows:
            if r['sector'] == '15':
                m = [x for x in sp if abs(float(x['t_mid_listed']) - float(r['t_mid_btjd'])) < 0.01][0]
                r['t_mid_btjd'], r['err_s'] = m['t_mid_tspoc'], m['err_s']
    t = np.array([float(r['t_mid_btjd']) for r in rows]); E = np.array([float(r['cycle']) for r in rows])
    sd = np.hypot(np.array([float(r['err_s']) for r in rows]), JIT[rid]) / 86400
    out = []
    for P3 in np.geomspace(400, 7300, 400):
        ph = 2 * np.pi * t / P3
        A = np.column_stack([np.ones_like(t), E, np.sin(ph), np.cos(ph)]) / sd[:, None]
        c = np.linalg.lstsq(A, t / sd, rcond=None)[0]
        chi2 = float(np.sum((t / sd - A @ c) ** 2))
        amp = math.hypot(c[2], c[3]) * 86400
        # tau = amp sin(2 pi t/P3 + phi) = amp sin(u) with u = 2 pi (t - tp)/P3
        phi = math.atan2(c[3], c[2])
        tp = -phi * P3 / (2 * np.pi)
        out.append((P3, chi2, amp, tp))
    best = min(o[1] for o in out)
    return [o for o in out if o[1] < best + 4], best


def lum(m):
    return m ** 4 if m >= 0.43 else 0.23 * m ** 2.3


def tertiary(rid, P, a_sini_au, inc):
    """m3 from the mass function at this inclination, and the photocentre factor 1 - beta / f."""
    M12 = sum(M_IN[rid]); fm = a_sini_au ** 3 / (P / 365.25) ** 2
    si = math.sin(math.radians(inc)); lo, hi = 1e-4, 1e3
    for _ in range(200):
        m = (lo + hi) / 2
        if (m * si) ** 3 / (M12 + m) ** 2 > fm: hi = m
        else: lo = m
    f = m / (M12 + m); L3 = lum(m); beta = L3 / (L3 + sum(lum(x) for x in M_IN[rid]))
    return m, beta, abs(1 - beta / f)


def predict(rid, P, e, w, tp, a_sini_au, incs=INCS):
    a, g = acc[rid], gaia[rid]
    plx = float(g['parallax'])
    res = {}
    for inc in incs:
        rr = []
        for _ in range(NREAL):
            t, s, c, D = gaia_epochs(float(a['ra_deg']), float(a['dec_deg']))
            Om = rng.uniform(0, 2 * np.pi)
            X, Y = orbit_xyz(t, P, e, w, tp, a_sini_au / math.sin(math.radians(inc)) * plx, math.radians(inc), Om)
            rr.append(residual_rms(t, s, c, D, X, Y))
        m3, beta, fac = tertiary(rid, P, a_sini_au, inc)
        res[inc] = (np.percentile(rr, [16, 50, 84]), m3, beta, fac)
    return res


def ruwe_from(d, sig):
    return math.sqrt(1 + (d / sig) ** 2)


def main():
    lines = []
    P = lines.append
    P("Gaia DR3 RUWE against the light-travel wobble (photocentre = inner binary; residual after a 5-parameter fit)")
    P("observed residual implied by RUWE, delta = sigma_AL sqrt(RUWE^2 - 1), for sigma_AL 0.06 / 0.10 / 0.20 mas")
    cases = []
    for rid in ('R630', 'R423', 'R371'):
        ok, best = circ_fits(rid)
        picks = sorted({ok[int(q * (len(ok) - 1))] for q in (0, 0.25, 0.5, 0.75, 1)} | {min(ok, key=lambda o: o[1])})
        for P3, chi2, amp, tp in picks:
            cases.append((rid, f"circular P3 {P3:.0f} d (chi2 {chi2:.1f}, best {best:.1f})", P3, 0.0, 0.0, tp, amp))
    for r in csv.DictReader(open(os.path.join(HERE, 'r623-gaia-branches.csv'))):
        if r['P_out'] in ('2000', '2500', '4000', '8000'):
            A = float(r['A_s']); w = math.radians(float(r['omega_deg'])) + (math.pi if A < 0 else 0.0)
            cases.append(('R623', f"eccentric P3 {r['P_out']} d, e {float(r['e']):.2f}", float(r['P_out']),
                          float(r['e']), w, float(r['T_peri']), abs(A)))
    out_rows = []
    last = None
    for rid, label, P3, e, w, tp, amp in cases:
        g = gaia[rid]; ruwe = float(g['ruwe']); plx = float(g['parallax'])
        if rid != last:
            dl = [s * math.sqrt(max(ruwe ** 2 - 1, 0)) for s in SIG]
            P(f"\n{rid}: RUWE {ruwe:.2f}, G {float(g['phot_g_mean_mag']):.2f}, parallax {plx:.2f} mas, "
              f"non_single_star {g['non_single_star']}; observed delta {dl[0]:.2f} / {dl[1]:.2f} / {dl[2]:.2f} mas")
            last = rid
        a_sini = amp / C_AU_S
        pr = predict(rid, P3, e, w, tp, a_sini)
        P(f"   {label}: light-time {amp:.0f} s, a12 sin i {a_sini:.2f} au = {a_sini * plx:.2f} mas")
        allowed = {s_: [] for s_ in SIG}
        for inc, ((lo, me, hi), m3, beta, fac) in pr.items():
            dark = [ruwe_from(me, s) for s in SIG]
            lo, me, hi = lo * fac, me * fac, hi * fac
            rw = [ruwe_from(me, s) for s in SIG]
            for s_ in SIG:   # allowed when the observed RUWE lies inside the 68% band of the prediction (luminous or dark tertiary)
                rlo, rhi = ruwe_from(lo, s_), max(ruwe_from(hi / fac, s_), ruwe_from(hi, s_))
                if min(rlo, ruwe_from(lo / fac, s_)) * 0.85 <= ruwe <= rhi * 1.15:
                    allowed[s_].append(inc)
            P(f"      i {inc:2d}: m3 {m3:.2f}, light {beta:.2f}, factor {fac:.2f}; residual {me:.2f} mas (68%: {lo:.2f}-{hi:.2f}) "
              f"-> RUWE {rw[0]:.1f} / {rw[1]:.1f} / {rw[2]:.1f} (dark tertiary {dark[0]:.1f} / {dark[1]:.1f} / {dark[2]:.1f})")
            out_rows.append(dict(review_id=rid, model=label, P3_d=round(P3), e=e, light_time_s=round(amp),
                                 a12_sini_au=round(a_sini, 3), wobble_sini_mas=round(a_sini * plx, 3), inc_deg=inc,
                                 m3=round(m3, 2), light_frac=round(beta, 3), photocentre_factor=round(fac, 3), resid_p16=round(lo, 3), resid_p50=round(me, 3), resid_p84=round(hi, 3),
                                 ruwe_obs=round(ruwe, 3), ruwe_pred_sig010=round(ruwe_from(me, 0.10), 2)))
        for s_ in SIG:
            P(f"      allowed i (sigma_AL {s_:.2f}, RUWE within 15% of the 68% band): {allowed[s_] or 'none'}")
    with open(os.path.join(HERE, 'ruwe-wobble.csv'), 'w', newline='') as fh:
        wr = csv.DictWriter(fh, fieldnames=list(out_rows[0]), lineterminator='\n'); wr.writeheader(); wr.writerows(out_rows)
    txt = "\n".join(lines)
    print(txt)
    open(os.path.join(HERE, 'ruwe-wobble-output.txt'), 'w').write(txt + "\n")


if __name__ == '__main__':
    main()
