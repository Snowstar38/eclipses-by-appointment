"""A fold of GD1 and GD2 (Fable 5.1's diary-dr3 conjunction-only hits) from the raw QLP/SPOC files,
with conjunctions derived here from Gaia's orbit, a box search near Gaia's period, and an odd/even test.
Usage (from the repository root):  python3 .../gd_fold.py <dir with GDn_sNNN_pipe.csv files> <gaia-orbits.csv>
"""
import sys, os, glob, math, csv
import numpy as np
D = 'reviews/duet-findings/'
sys.path.insert(0, D); sys.path.insert(0, D + 'gaia-errors')
import window_covariance as W
from a_epoch_test import orbit
LC, ORB = sys.argv[1], sys.argv[2]

def load(gd):
    t, f = [], []
    for p in sorted(glob.glob(os.path.join(LC, f'{gd}_s*_qlp.csv'))):
        r = np.genfromtxt(p, delimiter=',', names=True)
        m = (r['quality'] == 0) & np.isfinite(r['flux']) & np.isfinite(r['btjd'])
        tt, ff = r['btjd'][m], r['flux'][m]
        # detrend: running median over 1.0 d, iteratively ignoring points > 3 sigma low (eclipses)
        keep = np.ones(len(tt), bool)
        for _ in range(3):
            tr = np.array([np.median(ff[keep & (np.abs(tt - x) < 0.5)]) if np.any(keep & (np.abs(tt - x) < 0.5)) else np.nan for x in tt])
            res = ff / tr - 1; s = 1.4826 * np.median(np.abs(res[keep] - np.median(res[keep])))
            keep = res > -3 * s
        ok = np.isfinite(tr)
        t.append(tt[ok]); f.append((ff / tr - 1)[ok])
    return np.concatenate(t), np.concatenate(f)

def box(t, f, P, T0, w):
    ph = ((t - T0) / P + 0.5) % 1 - 0.5
    inn = np.abs(ph * P) < w / 2
    return inn, (np.mean(f[inn]) if inn.sum() > 3 else np.nan)

def search(t, f, P0, dP, wmin, wmax):
    best = (0, None)
    s = 1.4826 * np.median(np.abs(f - np.median(f)))
    for P in np.linspace(P0 - dP, P0 + dP, 801):
        ph = (t / P) % 1
        for w in (wmin, (wmin + wmax) / 2, wmax):
            nb = int(round(1 / (w / P / 2)))
            idx = np.floor(ph * nb).astype(int)
            sums = np.bincount(idx, f, nb); cnt = np.bincount(idx, minlength=nb)
            # box of two adjacent bins
            S = sums + np.roll(sums, -1); N = cnt + np.roll(cnt, -1)
            with np.errstate(invalid='ignore', divide='ignore'):
                snr = -S / (s * np.sqrt(N))
            snr[N < 5] = 0
            j = int(np.argmax(snr))
            if snr[j] > best[0]:
                best = (snr[j], (P, (j + 1) / nb * P, w))   # T0 at the bin edge between the two bins
    return best

rows = {r['gd']: r for r in csv.DictReader(open(ORB))}
for gd in ('GD1', 'GD2'):
    n = rows[gd]; n['nss_solution_type'] = 'SB1'
    v, err, corr = orbit(n)
    tA, tB = W.conj(v, 0), W.conj(v, 1)
    print(f"\n{gd} (Gaia SB1 P {v[0]:.6f} +- {err[0]:.6f} d, e {v[1]:.3f} +- {err[1]:.3f}, omega {math.degrees(v[2]):.1f} +- {math.degrees(err[2]):.1f})")
    print(f"  conjunctions here: A {tA:.4f}, B {tB:.4f} BTJD (B - A {((tB-tA)/v[0])%1:.4f});"
          f" house pilot: A {float(n['pilot_TconjA_btjd']):.4f}, B {float(n['pilot_TconjB_btjd']):.4f} ({float(n['pilot_phaseB_from_A']):.4f})")
    t, f = load(gd)
    print(f'  {len(t)} quality-0 cadences, BTJD {t.min():.1f}-{t.max():.1f}; point scatter {1.4826*np.median(np.abs(f-np.median(f)))*1e3:.2f} ppt')
    snr, (P, T0, w) = search(t, f, v[0], 0.004 * v[0], 0.08, 0.25)
    # refine T0 and width on a fine grid
    best = None
    for ww in np.linspace(0.06, 0.30, 25):
        for dt in np.linspace(-0.1, 0.1, 81):
            inn, d = box(t, f, P, T0 + dt, ww)
            if inn.sum() < 10: continue
            sn = -d * math.sqrt(inn.sum())
            if best is None or sn > best[0]: best = (sn, T0 + dt, ww, d)
    _, T0, w, dep = best
    cyc = np.round((t - T0) / P)
    # move T0 to the middle of the data
    T0 = T0 + np.round(np.median(cyc)) * P
    print(f'  box search near Gaia P: P {P:.6f} d (Gaia {v[0]:.6f}; z {(P - v[0])/err[0]:+.1f} with Gaia error), T0 {T0:.4f}, width {w*24:.1f} h, depth {-dep*1e3:.1f} ppt, SNR {snr:.0f}')
    # timing fit: one mid-time per cycle with enough points, then a linear ephemeris
    tm, kk = [], []
    for k in np.unique(np.round((t - T0) / P)):
        m = np.abs(t - (T0 + k * P)) < 1.5 * w
        if m.sum() < 8: continue
        tc = T0 + k * P
        grid = np.linspace(tc - w / 2, tc + w / 2, 121)
        chi = [np.sum((f[m] - np.where(np.abs(t[m] - g) < w / 2, dep, 0)) ** 2) for g in grid]
        g = grid[int(np.argmin(chi))]
        if np.sum(np.abs(t[m] - g) < w / 4) >= 3: tm.append(g); kk.append(k)
    tm, kk = np.array(tm), np.array(kk)
    A_ = np.vstack([np.ones_like(kk), kk]).T
    sol, *_ = np.linalg.lstsq(A_, tm, rcond=None)
    rr = tm - A_ @ sol; s = math.sqrt(np.sum(rr ** 2) / max(len(tm) - 2, 1)); C = s ** 2 * np.linalg.inv(A_.T @ A_)
    T0, P = sol; eP = math.sqrt(C[1, 1])
    print(f'  timing fit to {len(tm)} eclipses: P {P:.6f} +- {eP:.6f} d, T0 {T0:.4f} +- {math.sqrt(C[0,0]):.4f}, rms {s*24*60:.0f} min;'
          f' P - P_Gaia = {(P - v[0])*86400:+.0f} s ({(P - v[0])/math.hypot(err[0], eP):+.1f} sigma)')
    # where do the eclipses sit against Gaia's conjunctions, at TESS (Gaia's P carried forward) and at Gaia's epoch (eclipse P carried back)?
    for k, lab in ((0, 'A'), (1, 'B')):
        tg = W.conj(v, k)
        cyc = round((T0 - tg) / v[0]); oT = T0 - W.t_at(v, k, cyc); sTf, sTi = W.sigmas(v, err, corr, k, cyc)
        nb = round((tg - T0) / P); o0 = T0 + nb * P - tg; s0f, s0i = W.sigmas(v, err, corr, k, 0); sb = abs(nb) * eP
        print(f'  vs conjunction {lab}: at TESS {oT:+.3f} d = {oT/v[0]:+.4f} phase (z {oT/sTf:+.1f} full, {oT/sTi:+.1f} independent);'
              f' at Gaia epoch {o0:+.3f} d = {o0/v[0]:+.4f} phase (z {o0/math.hypot(s0f, sb):+.1f} full, {o0/math.hypot(s0i, sb):+.1f} independent)')
    # odd/even and secondary
    cyc = np.round((t - T0) / P)
    so = 1.4826 * np.median(np.abs(f - np.median(f)))
    res = {}
    for lab, sel in (('odd', cyc % 2 == 1), ('even', cyc % 2 == 0)):
        inn, d = box(t[sel], f[sel], P, T0, w * 0.6)
        res[lab] = (d, so / math.sqrt(inn.sum()), inn.sum(), len(np.unique(cyc[sel][inn])))
    (d1, e1, n1, c1), (d2, e2, n2, c2) = res['odd'], res['even']
    print(f'  odd/even (central 60% of the box): odd {-d1*1e3:.1f} +- {e1*1e3:.1f} ppt ({c1} eclipses), even {-d2*1e3:.1f} +- {e2*1e3:.1f} ppt ({c2});'
          f' difference {(d1-d2)/math.hypot(e1,e2):+.1f} sigma')
    # the same within each TESS year (sectors of one year share an aperture and dilution), weighted together
    yrs = np.floor((t - 1325) / 365.25)
    num = den = 0.0; per = []
    for y in np.unique(yrs):
        q = yrs == y
        o_ = [box(t[q & (cyc % 2 == j)], f[q & (cyc % 2 == j)], P, T0, w * 0.6) for j in (1, 0)]
        if any(x[0].sum() < 10 for x in o_): continue
        dd = o_[0][1] - o_[1][1]; ee = so * math.sqrt(1 / o_[0][0].sum() + 1 / o_[1][0].sum())
        # scale the white-noise error by the scatter of single-eclipse depths in that year
        sing = [box(t[q & (cyc == c)], f[q & (cyc == c)], P, T0, w * 0.6) for c in np.unique(cyc[q])]
        sd = np.array([x[1] for x in sing if x[0].sum() >= 5])
        nin = np.array([x[0].sum() for x in sing if x[0].sum() >= 5])
        infl = max(1.0, np.std(sd, ddof=1) / (so / np.sqrt(nin)).mean()) if len(sd) > 2 else 1.0
        ee *= infl; num += dd / ee ** 2; den += 1 / ee ** 2
        per.append(f'BTJD {int(t[q].min())}-{int(t[q].max())}: {dd*1e3:+.2f} +- {ee*1e3:.2f} ppt (x{infl:.1f})')
    print(f'  odd - even within each year: {"; ".join(per)}; combined {num/den*1e3:+.2f} +- {1e3/math.sqrt(den):.2f} ppt = {num/den*math.sqrt(den):+.1f} sigma')
    sepG = ((W.conj(v, 1) - W.conj(v, 0)) / v[0]) % 1
    prim_is_A = abs(((T0 - W.t_at(v, 0, round((T0 - W.conj(v, 0)) / v[0]))) / v[0] + 0.5) % 1 - 0.5) < \
                abs(((T0 - W.t_at(v, 1, round((T0 - W.conj(v, 1)) / v[0]))) / v[0] + 0.5) % 1 - 0.5)
    sep_exp = sepG if prim_is_A else (1 - sepG) % 1
    best2 = None
    for ph in np.linspace(0.3, 0.7, 401):
        inn, d = box(t, f, P, T0 + ph * P, w)
        if inn.sum() < 10: continue
        sn = -d / (so / math.sqrt(inn.sum()))
        if best2 is None or sn > best2[0]: best2 = (sn, ph, d)
    inn, dG = box(t, f, P, T0 + sep_exp * P, w)
    print(f'  primary at conjunction {"A" if prim_is_A else "B"}; secondary expected at phase {sep_exp:.4f} from Gaia (e, omega):'
          f' depth there {-dG*1e3:.1f} +- {so/math.sqrt(max(inn.sum(),1))*1e3:.1f} ppt; deepest dip in 0.3-0.7: phase {best2[1]:.4f}, {-best2[2]*1e3:.1f} ppt (SNR {best2[0]:.0f})')
    ecosw = math.pi / 2 * (best2[1] - 0.5)
    print(f'  e cos omega from the secondary (first order): {ecosw:+.4f}; Gaia {v[1]*math.cos(v[2]):+.4f}')
