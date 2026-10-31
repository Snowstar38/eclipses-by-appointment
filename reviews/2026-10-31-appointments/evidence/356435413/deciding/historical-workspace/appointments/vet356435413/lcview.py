"""Overview of every QLP sector (raw SAP, all cadences; flagged red) with nominal Gaia A/B conjunctions,
plus blind box census (0.1,0.2 d boxes, q==0) of dips > 0.5%. python lcview.py"""
import glob, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from vetlib import load_qlp
P, e, w, Tp = 27.4787767793643, 0.4449434084190493, np.radians(313.21494429696895), 2.9401907750914678 + 389.0
def tc(nu0):
    nu = nu0 - w; E = 2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2), np.sqrt(1+e)*np.cos(nu/2)); M = (E - e*np.sin(E)) % (2*np.pi); return Tp + M/(2*np.pi)*P
tA, tB = tc(np.pi/2), tc(1.5*np.pi); print('nominal A', tA, 'B', tB, 'phase sep', ((tB-tA)/P) % 1)
fs = sorted(glob.glob('[local path omitted]'))
fig, axs = plt.subplots(len(fs), 1, figsize=(16, 3*len(fs)))
for a, fn in zip(axs, fs):
    d = load_qlp(fn); t, f, q, bk = d['t'], d['f'], d['q'], d['bkg']
    a.plot(t[q == 0], f[q == 0], 'k.', ms=1); a.plot(t[q != 0], f[q != 0], 'r.', ms=1)
    a.set_ylim(0.97, 1.015); a.set_title(f"s{d['sec']}  {t.min():.2f}-{t.max():.2f}  dt {np.median(np.diff(t))*1440:.1f} min  nq0 {np.sum(q==0)} nflag {np.sum(q!=0)}")
    for lab, t0, c in (('A', tA, 'b'), ('B', tB, 'g')):
        for k in range(int((t.min()-t0)//P)-1, int((t.max()-t0)//P)+2):
            x = t0 + k*P
            if t.min()-2 < x < t.max()+2:
                a.axvline(x, color=c); a.axvspan(x-1, x+1, color=c, alpha=0.1)
                near = np.abs(t - x) < 1.0; nq = np.abs(t[q == 0] - x) < 1.0
                print(f"s{d['sec']} {lab} pred {x:.2f}: cadences within 1 d all {near.sum()} q0 {nq.sum()}; within 0.3 d all {(np.abs(t-x)<0.3).sum()} q0 {(np.abs(t[q==0]-x)<0.3).sum()}")
    # blind census on q==0
    tq, fq = t[q == 0], f[q == 0]
    for W in (0.1, 0.25):
        hits = []
        for tt in np.arange(tq.min()+W, tq.max()-W, W/4):
            i = np.abs(tq-tt) < W/2; o = (np.abs(tq-tt) > W) & (np.abs(tq-tt) < W+0.5)
            if i.sum() > 3 and o.sum() > 10:
                dd = np.median(fq[o]) - np.mean(fq[i])
                if dd > 0.005: hits.append((tt, dd))
        # merge
        m = []
        for h in hits:
            if m and h[0]-m[-1][0] < W: 
                if h[1] > m[-1][1]: m[-1] = h
            else: m.append(h)
        print(f"  census s{d['sec']} box {W}: " + ', '.join(f'{h[0]:.2f}({h[1]*100:.2f}%)' for h in m))
plt.tight_layout(); plt.savefig('overview.png', dpi=60)
