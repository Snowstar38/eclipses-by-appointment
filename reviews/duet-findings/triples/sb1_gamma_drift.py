"""How much systemic-velocity drift can a Gaia DR3 SB1 orbit carry, and do the light-travel
triples' outer orbits fit inside it?

1. Gaia DR3's published SB1 solutions stop at goodness_of_fit F2 = 3: every SB1 row in the
   repository's review gaia.json files is below it (42 of 571 in 2.5-3, none above), while
   the SB2 rows go to 29. F2 = sqrt(9 nu / 2) [(chi2 / nu)^(1/3) + 2 / (9 nu) - 1] with
   chi2 = obj_func and nu = N_RV - 6 reproduces every published F2, so the cut is
   chi2 / nu < (1 + 3 / sqrt(9 nu / 2) - 2 / (9 nu))^3.
2. Per-epoch RV error: sigma = err(K1) * sqrt(N / 2) (the scaling for a sinusoid's
   amplitude), as in timing/r623_gaia_branches.py.
3. For each outer orbit allowed by the timing (R630, R423, R371: circular fits of
   timing/ruwe_wobble.py; R623: the eccentric branches in timing/r623-gaia-branches.csv),
   the inner pair's systemic velocity v(t) follows from the delay (v = c d tau / dt, sign
   fixed by the timing). Simulated DR3 epochs: N transits in pairs 0.074 d apart (Gaia's
   two fields of view), the pairs placed at random over 2014-07-25 to 2017-05-28; RVs =
   inner orbit (Gaia's P, e, T_peri, omega, K1) + v(t) + noise of sigma times a factor
   that puts the median simulated F2 without a tertiary at the sample's 0.80. Fitted with
   the inner orbit's P, e and T_peri fixed and gamma, K1 cos omega and K1 sin omega free,
   which absorbs only a constant offset of a slow drift.
   Reported: the median simulated F2 and the chance F2 < 3 (that Gaia publishes the SB1).
Run from the repository root: python3 reviews/duet-findings/triples/sb1_gamma_drift.py
"""
import csv, glob, json, math, os, sys
import numpy as np

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TIM = os.path.join(HERE, '..', 'timing')
sys.path.insert(0, TIM)
from ruwe_wobble import circ_fits

C = 299792.458
T1, T2 = 2456863.9 - 2457000, 2457901.5 - 2457000
NSIM = 3000
rng = np.random.default_rng(20261126)


def F2(chi2, nu):
    return math.sqrt(9 * nu / 2) * ((chi2 / nu) ** (1 / 3) + 2 / (9 * nu) - 1)


def kepler_nu(M, e):
    E = M.copy()
    for _ in range(60):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))


# 1. the cut, from every SB1/SB2 row in the review gaia.json files
sb = {}
for f in glob.glob('reviews/**/gaia.json', recursive=True):
    try:
        g = json.load(open(f))
    except (ValueError, OSError):
        continue
    for n in g.get('nss') or []:
        if n.get('nss_solution_type', '').startswith('SB') and n.get('goodness_of_fit'):
            sb[(n['source_id'], n['nss_solution_type'])] = n
f1 = np.array([float(n['goodness_of_fit']) for (s, t), n in sb.items() if t == 'SB1'])
f2 = np.array([float(n['goodness_of_fit']) for (s, t), n in sb.items() if t == 'SB2'])
chk = []
for (s, t), n in sb.items():
    if t == 'SB1' and n.get('obj_func'):
        nu = int(n['rv_n_good_obs_primary']) - 6
        chk.append(abs(F2(float(n['obj_func']), nu) - float(n['goodness_of_fit'])))
print(f"SB1 rows: {len(f1)}, F2 median {np.median(f1):.2f}, max {f1.max():.2f}; {np.sum(f1 > 2.5)} in 2.5-3, {np.sum(f1 >= 3)} at 3 or above")
print(f"SB2 rows: {len(f2)}, F2 max {f2.max():.1f} ({np.sum(f2 >= 3)} at 3 or above): the cut is on SB1 only")
allx = {}
for f in glob.glob('reviews/**/*nss*.csv', recursive=True):
    try:
        for n in csv.DictReader(open(f)):
            if n.get('nss_solution_type') and n.get('goodness_of_fit'):
                try:
                    allx[(n['source_id'], n['nss_solution_type'])] = float(n['goodness_of_fit'])
                except ValueError:
                    pass
    except (UnicodeDecodeError, csv.Error, OSError):
        continue
for (s_, t), n in sb.items():
    allx.setdefault((s_, t), float(n['goodness_of_fit']))
for t in ('SB1', 'SB2', 'AstroSpectroSB1', 'Orbital'):
    v = np.array([F for (s_, tt), F in allx.items() if tt == t])
    if len(v):
        print(f"all NSS exports and gaia.json files, {t}: {len(v)} rows, F2 max {v.max():.2f}, {np.sum(v >= 3)} at 3 or above")
print(f"F2 from obj_func with nu = N - 6 reproduces the published value to {max(chk):.1e} (all {len(chk)} SB1 rows)")
med_obs = float(np.median(f1))

# per-system inputs
def nss_row(source_id):
    return sb[(source_id, 'SB1')]

ruwe = {r['review_id']: r for r in csv.DictReader(open(os.path.join(TIM, 'gaia-ruwe-r-systems.csv')))}


def sim(n, v_of_t, nsim=NSIM, infl=1.0):
    N = int(n['rv_n_good_obs_primary']); nu = N - 6
    P, e = float(n['period']), float(n['eccentricity'] or 0)
    tp = float(n['t_periastron']) + 389.0          # Gaia's reference epoch 2016.0 = BTJD 389.0
    w = math.radians(float(n['arg_periastron'] or 0)); K = float(n['semi_amplitude_primary'])
    sig = float(n['semi_amplitude_primary_error']) * math.sqrt(N / 2)
    out = np.empty(nsim)
    for k in range(nsim):
        tv = rng.uniform(T1, T2, (N + 1) // 2)
        t = np.sort(np.concatenate([tv, tv + 0.074]))[:N]
        nu_t = kepler_nu(np.mod(2 * math.pi * (t - tp) / P, 2 * math.pi), e)
        rv = K * (np.cos(nu_t + w) + e * math.cos(w)) + v_of_t(t) + rng.normal(0, sig * infl, N)
        A = np.column_stack([np.ones(N), np.cos(nu_t), np.sin(nu_t)])
        c = np.linalg.lstsq(A, rv, rcond=None)[0]
        chi2 = float(np.sum((rv - A @ c) ** 2)) / sig ** 2
        out[k] = F2(chi2, nu)
    return out, sig, N


def inflation(n):
    """noise factor that gives the sample's median F2 with no tertiary"""
    lo, hi = 0.8, 1.6
    for _ in range(14):
        mid = (lo + hi) / 2
        m = np.median(sim(n, lambda t: 0 * t, 600, mid)[0])
        lo, hi = (mid, hi) if m < med_obs else (lo, mid)
    return (lo + hi) / 2


def main():
    global infl0
    rows_out = []
    for rid in ('R630', 'R423', 'R371', 'R623'):
        src = ruwe[rid]['source_id']
        n = nss_row(src)
        fobs = float(n['goodness_of_fit'])
        infl = inflation(n)
        base, sig, N = sim(n, lambda t: 0 * t, NSIM, infl)
        print(f"\n{rid}: Gaia SB1 P {float(n['period']):.4f} d, K1 {float(n['semi_amplitude_primary']):.1f} km/s, N_RV {N}, "
              f"per-epoch error {sig:.1f} km/s (x{infl:.2f} to match the sample); published F2 {fobs:.2f}")
        print(f"   no tertiary: median F2 {np.median(base):.2f}, published (F2 < 3) {np.mean(base < 3):.0%}, F2 >= published {np.mean(base >= fobs):.0%}")
        orbits = []
        if rid in ('R630', 'R423', 'R371'):
            ok, best = circ_fits(rid)
            edges = [ok[i] for i in range(len(ok)) if i == len(ok) - 1 or ok[i + 1][0] > 1.1 * ok[i][0]] + \
                    [ok[i + 1] for i in range(len(ok) - 1) if ok[i + 1][0] > 1.1 * ok[i][0]]   # both sides of any gap
            pick = sorted(set(ok[::max(1, len(ok) // 12)] + edges + [min(ok, key=lambda o: o[1])]), key=lambda o: o[0])
            for P3, chi2, amp, tpo in pick:
                Kv = 2 * math.pi * amp / (P3 * 86400) * C
                orbits.append((f"circular P3 {P3:5.0f} d (dchi2 {chi2 - best:.1f})", P3,
                               (lambda Kv, P3, tpo: lambda t: Kv * np.cos(2 * math.pi * (t - tpo) / P3))(Kv, P3, tpo)))
        else:
            for r in csv.DictReader(open(os.path.join(TIM, 'r623-gaia-branches.csv'))):
                P3, A, e3 = float(r['P_out']), float(r['A_s']), float(r['e'])
                om, tpo = math.radians(float(r['omega_deg'])), float(r['T_peri'])
                Kv = 2 * math.pi * A * C / (P3 * 86400 * math.sqrt(1 - e3 * e3))
                orbits.append((f"e {e3:.2f} P3 {P3:5.0f} d (chi2 {float(r['chi2']):.1f})", P3,
                               (lambda Kv, P3, e3, om, tpo: lambda t: Kv * (np.cos(kepler_nu(np.mod(2 * math.pi * (t - tpo) / P3, 2 * math.pi), e3) + om) + e3 * math.cos(om)))(Kv, P3, e3, om, tpo)))
        tt = np.linspace(T1, T2, 600)
        for lab, P3, v in orbits:
            vt = v(tt); drift = float(np.std(vt))
            s, _, _ = sim(n, v, NSIM, infl)
            rows_out.append(dict(rid=rid, orbit=lab, P3_d=P3, dr3_drift_rms_kms=round(drift, 2), sigma_epoch_kms=round(sig, 2),
                                 median_F2=round(float(np.median(s)), 2), p_published=round(float(np.mean(s < 3)), 3),
                                 p_F2_le_observed=round(float(np.mean(s <= fobs)), 3), F2_published=fobs))
            print(f"   {lab}: DR3-span drift rms {drift:4.1f} km/s -> median F2 {np.median(s):5.2f}, published {np.mean(s < 3):4.0%}, "
                  f"F2 <= {fobs:.2f} in {np.mean(s <= fobs):4.0%}")

    # 4. the general threshold: drift that halves the chance of publication, per epoch error and N
    print("\nDrift (rms over DR3, linear ramp) at which an SB1 has a 50% chance of falling over the cut,")
    print("for the sample's median noise factor; in units of the per-epoch error:")
    proto = dict(rv_n_good_obs_primary='24', period='5.0', eccentricity='0', t_periastron='0', arg_periastron='0',
                 semi_amplitude_primary='40', semi_amplitude_primary_error='1.0')
    infl0 = inflation(proto)
    for N in (14, 20, 26, 34, 42):
        p = dict(proto, rv_n_good_obs_primary=str(N))
        sig = math.sqrt(N / 2)
        for x in np.arange(0.2, 3.01, 0.05):
            ramp = lambda t, x=x: x * sig * math.sqrt(12) * (t - (T1 + T2) / 2) / (T2 - T1)
            s, _, _ = sim(p, ramp, 800, infl0)
            if np.mean(s < 3) < 0.5:
                print(f"   N_RV {N:2d}: {x:.2f} sigma"); break
    with open(os.path.join(HERE, 'sb1-gamma-drift.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows_out[0]), lineterminator='\n'); w.writeheader(); w.writerows(rows_out)

    # 5. the sample's per-epoch errors, and A95 and A119 as if they were single-lined
    sg = np.array([float(n['semi_amplitude_primary_error']) * math.sqrt(int(n['rv_n_good_obs_primary']) / 2)
                   for (s, t), n in sb.items() if t == 'SB1' and n.get('semi_amplitude_primary_error')])
    Ns = np.array([int(n['rv_n_good_obs_primary']) for (s, t), n in sb.items() if t == 'SB1'])
    print(f"\nSB1 sample: per-epoch error median {np.median(sg):.1f} km/s (16-84%: {np.percentile(sg, 16):.1f}-{np.percentile(sg, 84):.1f}), N_RV median {np.median(Ns):.0f}")
    sys.path.insert(0, HERE)
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        import dr4_gamma_predictions as D   # silence its own predictions
    NSSF = {(r['review_id'], r['nss_solution_type']): r for r in csv.DictReader(open(D.NSS))}
    Nm = int(np.median(Ns)); sm = float(np.median(sg))
    proto = dict(rv_n_good_obs_primary=str(Nm), period='5.0', eccentricity='0', t_periastron='0', arg_periastron='0',
                 semi_amplitude_primary='40', semi_amplitude_primary_error=f"{sm / math.sqrt(Nm / 2):.4f}")
    for lab, amp, sign in (('A95', 3.48, -1), ('A119', 3.38, 1)):
        P, e, tp, w = D.elements(NSSF[(lab, 'Orbital')])
        Kd = D.semi_amp_to_K(amp, e, w) * sign
        v = lambda t, P=P, e=e, tp=tp, w=w, Kd=Kd: D.velocity(t, P, e, tp, w, Kd)
        tt = np.linspace(T1, T2, 600)
        s, _, _ = sim(proto, v, NSIM, infl0)
        print(f"   {lab} as an SB1 with N_RV {Nm} and {sm:.1f} km/s per epoch: DR3 drift rms {np.std(v(tt)):.1f} km/s, "
              f"median F2 {np.median(s):.1f}, published {np.mean(s < 3):.0%}")


if __name__ == '__main__':
    main()
