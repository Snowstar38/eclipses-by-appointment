"""How big a timing signal should the astrometrically flagged R systems show?

Inverse of ruwe_wobble.py. RUWE gives the photocentre residual that the five-parameter fit left,
delta = sigma_AL sqrt(RUWE^2 - 1). For a circular outer orbit of period P3 seen edge-on (coplanar
with the eclipsing pair) and a dark tertiary, the residual is a fraction r(P3) of the photocentre
semi-major axis (median over orbital phase and node, the same simulated DR3 scans as ruwe_wobble.py).
So a_ph = delta / r(P3), and the eclipse delay has semi-amplitude a_ph / (parallax * c). The
smallest such amplitude over P3 is the floor a coplanar tertiary must reach. A luminous tertiary
raises it (the photocentre moves less than the binary); an inclined outer orbit lowers it by sin i,
so the floor holds only for near-coplanar triples. The wobble could also come from a resolved or
background neighbour, which has no timing signal at all.
For the systems timed in TESS (etv-events.csv) the observed sector-mean O-C rms and range are
listed beside the floor, and a Monte Carlo asks how often a tertiary that makes the observed RUWE
leaves timing as flat as observed: P3 log-uniform 150-12000 d, circular, isotropic inclination,
random phase and node, sigma_AL log-uniform 0.06-0.20 mas, dark tertiary; the delay is evaluated
at the event times, a linear ephemeris is removed, and the draw counts as flat when the leftover
rms is below the observed linear-fit rms of the event O-C. Sector 101 times carry the 3.5-min
clock fault (R225), so that comparison is loose.
Run from the repository root: python3 reviews/duet-findings/timing/astrometric_timing_floor.py
"""
import csv, math, os, sys
import numpy as np
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ruwe_wobble as W

P3S = np.geomspace(150, 12000, 36)
SIG = W.SIG
gaia = W.gaia; acc = W.acc
ev = {}
for r in csv.DictReader(open(os.path.join(HERE, 'etv-events.csv'))):
    ev.setdefault(r['tic'], []).append(r)


def frac(rid, P3, n=120):
    a = acc[rid]; out = []
    for _ in range(n):
        t, s, c, D = W.gaia_epochs(float(a['ra_deg']), float(a['dec_deg']))
        tp = W.rng.uniform(0, P3); Om = W.rng.uniform(0, 2 * np.pi)
        X, Y = W.orbit_xyz(t, P3, 0.0, 0.0, tp, 1.0, math.pi / 2, Om)
        out.append(W.residual_rms(t, s, c, D, X, Y))
    return float(np.median(out))


def main():
    L = []
    P = L.append
    P("Light-travel floor for a coplanar, dark tertiary implied by Gaia DR3 RUWE (sigma_AL 0.06 / 0.10 / 0.20 mas per CCD)")
    flagged = [g for g in gaia.values() if g['non_single_star'] and int(g['non_single_star']) & 1]
    flagged.sort(key=lambda g: int(g['review_id'][1:]))
    rows = []
    for g in flagged:
        rid = g['review_id']; ruwe = float(g['ruwe']); plx = float(g['parallax'])
        if rid not in acc:
            continue
        fr = np.array([frac(rid, p) for p in P3S])
        dl = [s * math.sqrt(max(ruwe ** 2 - 1, 0)) for s in SIG]
        amps = [d / fr / plx * W.C_AU_S for d in dl]          # delay semi-amplitude, s, per P3
        j = int(np.argmin(amps[1]))
        line = (f"{rid}: RUWE {ruwe:.2f}, parallax {plx:.2f} mas, G {float(g['phot_g_mean_mag']):.2f}; residual {dl[1]:.2f} mas; "
                f"floor {amps[0][j] / 60:.1f} / {amps[1][j] / 60:.1f} / {amps[2][j] / 60:.1f} min at P3 ~ {P3S[j]:.0f} d "
                f"(P3 1000 d: {np.interp(1000, P3S, amps[1]) / 60:.1f}, 3000 d: {np.interp(3000, P3S, amps[1]) / 60:.1f}, "
                f"8000 d: {np.interp(8000, P3S, amps[1]) / 60:.1f} min at 0.10)")
        e = ev.get(g['tic'], [])
        obs = ''
        if e:
            sec = {}
            for r in e:
                sec.setdefault(r['sector'], []).append(float(r['oc_min']))
            m = {k: np.mean(v) for k, v in sec.items()}
            vals = np.array(list(m.values()))
            obs = (f"; timed in {len(m)} sectors ({', '.join(sorted(m, key=int))}): sector-mean O-C rms {vals.std():.2f} min, "
                   f"range {np.ptp(vals):.2f} min")
        P(line + obs)
        rows.append(dict(review_id=rid, ruwe=round(ruwe, 3), parallax=round(plx, 3), resid_mas_sig010=round(dl[1], 3),
                         floor_min_sig006=round(amps[0][j] / 60, 2), floor_min_sig010=round(amps[1][j] / 60, 2),
                         floor_min_sig020=round(amps[2][j] / 60, 2), P3_at_floor_d=round(P3S[j]),
                         floor_P1000_min=round(np.interp(1000, P3S, amps[1]) / 60, 2),
                         floor_P3000_min=round(np.interp(3000, P3S, amps[1]) / 60, 2),
                         floor_P8000_min=round(np.interp(8000, P3S, amps[1]) / 60, 2), n_sectors_timed=len(set(r['sector'] for r in e))))
    P("\nHow often a RUWE-matching tertiary leaves the timing this flat (isotropic orientation):")
    for g in flagged:
        rid = g['review_id']; e = ev.get(g['tic'], [])
        if rid not in acc or not e:
            continue
        t = np.array([float(r['t_mid']) for r in e]); cyc = np.array([float(r['cycle']) for r in e])
        oc = np.array([float(r['oc_min']) for r in e])
        A = np.column_stack([np.ones_like(cyc), cyc])
        obs_rms = math.sqrt(np.mean((oc - A @ np.linalg.lstsq(A, oc, rcond=None)[0]) ** 2))
        ruwe = float(g['ruwe']); plx = float(g['parallax'])
        flat = 0; N = 600; lowi = []
        for _ in range(N):
            P3 = math.exp(W.rng.uniform(math.log(150), math.log(12000)))
            sig = math.exp(W.rng.uniform(math.log(0.06), math.log(0.20)))
            ci = W.rng.uniform(0, 1); inc = math.acos(ci); Om = W.rng.uniform(0, 2 * np.pi); tp = W.rng.uniform(0, P3)
            a = acc[rid]
            tg, sg, cg, D = W.gaia_epochs(float(a['ra_deg']), float(a['dec_deg']))
            X, Y = W.orbit_xyz(tg, P3, 0.0, 0.0, tp, 1.0, inc, Om)
            r = W.residual_rms(tg, sg, cg, D, X, Y)
            aph = sig * math.sqrt(max(ruwe ** 2 - 1, 0)) / r / plx          # au
            tau = aph * math.sin(inc) * W.C_AU_S / 60 * np.sin(2 * np.pi * (t - tp) / P3)   # min
            res = tau - A @ np.linalg.lstsq(A, tau, rcond=None)[0]
            if math.sqrt(np.mean(res ** 2)) < obs_rms:
                flat += 1; lowi.append(math.degrees(inc))
        med_i = f", median i of those {np.median(lowi):.0f} deg" if lowi else ""
        P(f"   {rid}: observed linear-fit rms {obs_rms:.2f} min over {len(set(r['sector'] for r in e))} sectors; "
          f"flat in {flat / N:.0%} of draws{med_i}")
    P("\nresidual fraction r(P3) for R625's scans, edge-on circular: " + " ".join(f"{p:.0f}:{f:.2f}" for p, f in zip(P3S[::5], [frac('R625', p) for p in P3S[::5]])))
    with open(os.path.join(HERE, 'astrometric-timing-floor.csv'), 'w', newline='') as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator='\n'); wr.writeheader(); wr.writerows(rows)
    txt = "\n".join(L); print(txt)
    open(os.path.join(HERE, 'astrometric-timing-floor-output.txt'), 'w').write(txt + "\n")


if __name__ == '__main__':
    main()
