"""R623: test the two light-travel branches of its eclipse timing against Gaia DR3's SB1 orbit.

Earthshine's 160 TESS-SPOC eclipse times (sectors 15-78) fit an eccentric
light-travel orbit with P_out >= 2000 d, but P_out is not bounded above: a
2000-2500 d branch and a >= 3500 d branch fit equally well and part by about
33 min in 2027. Gaia's RVs (2014-07-25 to 2017-05-28, before TESS) give two
independent checks, because each branch predicts the light-travel delay then:
  1. the eclipse (conjunction) time at Gaia's epoch, against Gaia's kind-0
     conjunction propagated with Gaia's full covariance;
  2. the apparent period over Gaia's span, P(1 + d tau/dt), against Gaia's
     period.
For each fixed P_out the light-travel orbit is refitted (grid in e, omega,
T_peri; amplitude and both per-family ephemerides solved by weighted least
squares, event errors scaled by the best reduced chi2).
Run from the repository root (about 3 minutes; R623_SKIP_FIT=1 reuses r623-gaia-branches.csv):
  python3 reviews/duet-findings/timing/r623_gaia_branches.py > reviews/duet-findings/timing/r623-gaia-branches-output.txt
"""
import csv, json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EVENTS = os.path.join(HERE, 'r623-events-earthshine.csv')
GEOM = 'reviews/2026-11-01-remaining136/campaign/batch09/gaia-geometry.json'
NSS = 'reviews/2026-11-01-remaining136/campaign/shared-catalogues/gaia-nss-full.csv'
SRC = '1603058197763982976'
GAIA_T1, GAIA_T2 = 2456863.9 - 2457000, 2457901.5 - 2457000  # DR3 span, BTJD
GAIA_OFFSET = 389.0  # t_periastron is days from 2016.0 = BTJD 389.0


def kepler_nu(M, e):
    E = M.copy()
    for _ in range(50):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))


def shape(t, P, e, om, tp):
    nu = kepler_nu(np.mod(2 * math.pi * (t - tp) / P, 2 * math.pi), e)
    return (1 - e * e) / (1 + e * np.cos(nu)) * np.sin(nu + om) + e * math.sin(om)


def load():
    rows = list(csv.DictReader(open(EVENTS)))
    fam = np.array([r['family'] for r in rows])
    t = np.array([float(r['t_btjd']) for r in rows])
    s = np.array([float(r['sigma_d']) for r in rows])
    n = np.array([float(r['epoch']) for r in rows])
    return fam, t, s, n


def design(fam, n):
    p = (fam == 'P').astype(float)
    return np.column_stack([p, 1 - p, n * p, n * (1 - p)])


def solve(t, w, B, g):
    A = np.column_stack([B, g])
    Aw = A * w[:, None]
    cov = np.linalg.inv(A.T @ Aw)
    b = cov @ (Aw.T @ t)
    r = t - A @ b
    return float((w * r * r).sum()), b, cov


def fit_fixed_P(t, w, B, P):
    best = None
    for e in np.arange(0, 0.91, 0.05):
        for om in np.radians(np.arange(0, 360, 10)):
            for ph in np.arange(0, 1, 1 / 48):
                c, *_ = solve(t, w, B, shape(t, P, e, om, 1700 + ph * P))
                if best is None or c < best[0]:
                    best = (c, e, om, 1700 + ph * P)
    c, e, om, tp = best
    for step in (1.0, 0.4, 0.15):
        for de in np.linspace(-0.04, 0.04, 5) * step:
            for dom in np.radians(np.linspace(-8, 8, 9) * step):
                for dtp in np.linspace(-0.02, 0.02, 9) * step:
                    ee = min(max(e + de, 0), 0.95)
                    cc, *_ = solve(t, w, B, shape(t, P, ee, om + dom, tp + dtp * P))
                    if cc < best[0]:
                        best = (cc, ee, om + dom, tp + dtp * P)
        c, e, om, tp = best
    return best


def gaia_conjunction():
    nss = next(r for r in csv.DictReader(open(NSS)) if r['source_id'] == SRC)
    v = np.array([float(nss['period']), float(nss['eccentricity']),
                  math.radians(float(nss['arg_periastron'])), float(nss['t_periastron']) + GAIA_OFFSET])
    err = np.array([float(nss['period_error']), float(nss['eccentricity_error']),
                    math.radians(float(nss['arg_periastron_error'])), float(nss['t_periastron_error'])])
    C = np.eye(6)
    vals = [float(x) for x in nss['corr_vec'].strip('{}').split(',')]
    z = 0
    for i in range(1, 6):
        for j in range(i):
            C[i, j] = C[j, i] = vals[z]
            z += 1
    sub = C[np.ix_([0, 3, 4, 5], [0, 3, 4, 5])]
    cov = sub * np.outer(err, err)

    def conj(x):
        p, e, w_, tp = x
        nu = math.pi / 2 - w_  # kind 0, the conjunction the primary eclipse falls on
        E = 2 * math.atan2(math.sqrt(1 - e) * math.sin(nu / 2), math.sqrt(1 + e) * math.cos(nu / 2))
        return tp + (E - e * math.sin(E)) % (2 * math.pi) / (2 * math.pi) * p
    tc = conj(v)
    J = np.zeros(4)
    for i in range(4):
        h = np.zeros(4); h[i] = err[i] * 1e-3
        J[i] = (conj(v + h) - conj(v - h)) / (2 * h[i])
    return tc, math.sqrt(J @ cov @ J), v[0], err[0], nss


def main():
    fam, t, s, n = load()
    w = 1 / s ** 2
    B = design(fam, n)
    tc, sig_tc, Pg, ePg, nss = gaia_conjunction()
    print(f"Gaia DR3 SB1 {SRC}: P {Pg:.8f} +/- {ePg:.8f} d, K1 {float(nss['semi_amplitude_primary']):.1f} km/s, "
          f"e {float(nss['eccentricity']):.3f}; kind-0 conjunction BTJD {tc:.5f} +/- {sig_tc*1440:.1f} min (full covariance)")
    # linear-only reference
    Bw = B * w[:, None]
    cl = np.linalg.inv(B.T @ Bw); bl = cl @ (Bw.T @ t)
    chil = float((w * (t - B @ bl) ** 2).sum())
    out = []
    for Pout in (1800, 2000, 2200, 2500, 3000, 3500, 4000, 5000, 6500, 8000, 12000):
        c, e, om, tp = fit_fixed_P(t, w, B, Pout)
        g = shape(t, Pout, e, om, tp)
        c, b, cov = solve(t, w, B, g)
        T0, Pin, A = b[0], b[2], b[4]
        # 1. eclipse time at Gaia's conjunction
        ncyc = round((tc - T0) / Pin)
        def tpred(bb):
            tt = bb[0] + bb[2] * ncyc
            return tt + bb[4] * shape(np.array([tt]), Pout, e, om, tp)[0]
        tp_g = tpred(b)
        # error of the prediction from the linear parameters (fixed shape)
        J = np.zeros(5)
        for i in range(5):
            h = np.zeros(5); h[i] = 1e-7
            J[i] = (tpred(b + h) - tpred(b - h)) / 2e-7
        s2 = c / (t.size - 9)
        sig_p = math.sqrt(J @ cov @ J * max(s2, 1))
        dt = tc - tp_g
        z_t = dt / math.hypot(sig_tc, sig_p)
        # 2. apparent period over Gaia's span
        g1, g2 = shape(np.array([GAIA_T1, GAIA_T2]), Pout, e, om, tp)
        Papp = Pin * (1 + A * (g2 - g1) / (GAIA_T2 - GAIA_T1))
        z_p = (Pg - Papp) / ePg
        tau_g = A * shape(np.array([tc]), Pout, e, om, tp)[0]
        out.append(dict(P_out=Pout, chi2=round(c, 1), e=round(e, 3), omega_deg=round(math.degrees(om) % 360, 1),
                        T_peri=round(tp, 1), A_s=round(A * 86400, 1), tau_gaia_min=round(tau_g * 1440, 2),
                        pred_btjd=round(tp_g, 5), gaia_minus_pred_min=round(dt * 1440, 1),
                        sig_pred_min=round(sig_p * 1440, 1), z_time=round(z_t, 2),
                        P_app_gaia=round(Papp, 8), z_period=round(z_p, 2), chi2_total=round(c + z_t ** 2 + z_p ** 2, 1)))
        o = out[-1]
        print(f"P_out {Pout:6d}: TESS chi2 {o['chi2']:6.1f}  e {o['e']:.2f}  A {o['A_s']:+7.0f} s  "
              f"tau(Gaia) {o['tau_gaia_min']:+6.1f} min | Gaia-pred {o['gaia_minus_pred_min']:+6.1f} +/- "
              f"{math.hypot(sig_tc, sig_p)*1440:4.1f} min (z {o['z_time']:+5.2f}) | P_app {Papp:.8f} (z {o['z_period']:+5.2f})"
              f" | total {o['chi2_total']:.1f}")
    nl = round((tc - bl[0]) / bl[2])
    sl = math.sqrt(cl[0, 0] + nl * nl * cl[2, 2] + 2 * nl * cl[0, 2]) * math.sqrt(chil / (t.size - 4))
    dl = tc - (bl[0] + bl[2] * nl)
    print(f"linear ephemerides only: TESS chi2 {chil:.0f}; Gaia-pred {dl*1440:+.1f} +/- "
          f"{math.hypot(sig_tc, sl)*1440:.1f} min (z {dl/math.hypot(sig_tc, sl):+.2f}), P {bl[2]:.8f} "
          f"(Gaia z {(Pg - bl[2]) / ePg:+.2f})")
    with open(os.path.join(HERE, 'r623-gaia-branches.csv'), 'w', newline='') as fh:
        wr = csv.DictWriter(fh, fieldnames=list(out[0]), lineterminator='\n')
        wr.writeheader(); wr.writerows(out)



def masses_and_acceleration():
    """Minimum tertiary mass per branch (M12 from TIC M1 and Gaia's mass function at i = 90 deg)
    and the sky-plane acceleration of the inner pair at 2016.0 for an edge-on outer orbit,
    to compare with Gaia's astrometric NSS solution for this source (not in this repository)."""
    geom = json.load(open(GEOM))['165793290']
    m1, m2 = geom['assumed_m1_solar'], geom['minimum_m2_solar']
    m12 = m1 + m2
    plx = 7.817916712094154  # mas, gaia.json
    rows = list(csv.DictReader(open(os.path.join(HERE, 'r623-gaia-branches.csv'))))
    print(f"\nM1 {m1:.2f} (TIC) + M2 {m2:.2f} (Gaia f(m), i 90) = {m12:.2f} Msun; parallax {plx:.2f} mas")
    for r in rows:
        P, A, e = float(r['P_out']), abs(float(r['A_s'])), float(r['e'])
        om, tp = math.radians(float(r['omega_deg'])), float(r['T_peri'])
        a12 = A / 499.004784  # AU, edge-on
        fm = a12 ** 3 / (P / 365.25) ** 2
        lo, hi = 0.01, 30
        for _ in range(80):
            m = 0.5 * (lo + hi)
            lo, hi = (m, hi) if m ** 3 / (m12 + m) ** 2 < fm else (lo, m)
        # inner-pair barycentre: r = a12 (1 - e cos E); edge-on, sky coordinate x = r cos(nu + om)
        nu = kepler_nu(np.array([np.mod(2 * math.pi * (389.0 - tp) / P, 2 * math.pi)]), e)[0]
        rr = a12 * (1 - e * e) / (1 + e * math.cos(nu))
        n = 2 * math.pi / (P / 365.25)  # rad / yr
        acc = n * n * a12 ** 3 / rr ** 2 * abs(math.cos(nu + om)) * plx  # mas / yr^2 on the sky
        acc_tot = n * n * a12 ** 3 / rr ** 2 * plx
        print(f"P_out {int(P):6d}: a12 sin i {a12:.2f} AU, f(M3) {fm:.3f}, M3 >= {m:.2f} Msun; "
              f"2016.0 acceleration {acc:.2f} mas/yr^2 on the sky edge-on (total {acc_tot:.2f})")



def gamma_curves():
    """Systemic-velocity curve of the inner pair predicted by each branch:
    v = K [cos(nu + omega) + e cos omega], K = 2 pi A c / (P sqrt(1 - e^2)), same sign as tau.
    (a) its scatter over Gaia DR3's RV span, against what DR3's constant-gamma SB1 fit can hide:
        obj_func 50.5 for 35 - 6 dof leaves 21.5 of chi2, and K1's error of 0.78 km/s from
        35 epochs implies about 3.3 km/s per epoch, so an rms drift of at most about 2.6 km/s;
    (b) the swing across Gaia DR4's span (2014-07-25 to 2020-01-20), sealed before DR4."""
    rows = list(csv.DictReader(open(os.path.join(HERE, 'r623-gaia-branches.csv'))))
    nss = next(r for r in csv.DictReader(open(NSS)) if r['source_id'] == SRC)
    nobs = int(nss['rv_n_good_obs_primary']); obj = float(nss['obj_func'])
    sig_ep = float(nss['semi_amplitude_primary_error']) * math.sqrt(nobs / 2)
    cap = math.sqrt(max(obj - (nobs - 6), 0) / nobs) * sig_ep
    print(f"\nDR3: {nobs} RVs, obj_func {obj:.1f}; per-epoch error about {sig_ep:.1f} km/s; "
          f"hidden gamma drift at most about {cap:.1f} km/s rms")
    t3 = np.linspace(GAIA_T1, GAIA_T2, 400)
    DR4_T2 = 2458868.5 - 2457000
    t4 = np.linspace(GAIA_T1, DR4_T2, 800)
    years = [2015.0, 2016.0, 2017.0, 2018.0, 2019.0, 2020.0]
    tb = np.array([(y - 2016.0) * 365.25 + 389.0 for y in years])
    for r in rows:
        P, A, e = float(r['P_out']), float(r['A_s']), float(r['e'])
        om, tp = math.radians(float(r['omega_deg'])), float(r['T_peri'])
        K = 2 * math.pi * A * 299792.458 / (P * 86400 * math.sqrt(1 - e * e))

        def v(tt):
            nu = kepler_nu(np.mod(2 * math.pi * (tt - tp) / P, 2 * math.pi), e)
            return K * (np.cos(nu + om) + e * math.cos(om))
        v3, v4, vy = v(t3), v(t4), v(tb)
        print(f"P_out {int(P):6d}: K3-orbit {abs(K):5.1f} km/s | DR3-span rms {v3.std():4.1f} km/s "
              f"({'hidden' if v3.std() <= cap else 'too large'}) | DR4-span swing {v4.max()-v4.min():5.1f} km/s | "
              + " ".join(f"{y:.0f}:{x - vy[1]:+5.1f}" for y, x in zip(years, vy)))


if __name__ == '__main__':
    if not os.environ.get('R623_SKIP_FIT'):
        main()
    masses_and_acceleration()
    gamma_curves()
