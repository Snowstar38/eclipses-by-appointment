"""Run 9a figure: A73's secondary phase and secondary depth (Fable's measurements, s17-s86)
against the best joint N-body fits at a low e_out and at Gaia's e_out = 0.41, with the
models continued to 2028. Plain SVG, no plotting library.
Usage: python3 a73_figure.py a73-secondary-phases.csv low.json gaia.json out.svg"""
import sys, json
import numpy as np
import a73_fit as F

t, ph, dep = F.load(sys.argv[1])
W, H, L, R, T, G = 760, 560, 70, 20, 30, 50   # width, height, margins, gap between panels
PH = (H - T - 50 - G) / 2
X0, X1 = 1700, 4900
def X(x): return L + (x - X0) / (X1 - X0) * (W - L - R)
def panel(y, lo, hi, top): return top + (hi - y) / (hi - lo) * PH
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="12">',
       '<style>.a{stroke:#888;stroke-width:1;fill:none}.o{fill:#222}.m1{stroke:#1f6fb4;stroke-width:1.6;fill:none}.m2{stroke:#c0532b;stroke-width:1.6;fill:none;stroke-dasharray:5 3}</style>']
tops = [T, T + PH + G]
rngs = [(0.44, 0.55), (0.0, 0.16)]
labs = ['secondary phase', 'secondary depth']
for top, (lo, hi), lab in zip(tops, rngs, labs):
    out.append(f'<rect class="a" x="{L}" y="{top}" width="{W-L-R}" height="{PH}"/>')
    for k in range(5):
        v = lo + (hi - lo) * k / 4; yy = panel(v, lo, hi, top)
        out.append(f'<text x="{L-6}" y="{yy+4}" text-anchor="end">{v:.3f}</text>')
    out.append(f'<text x="16" y="{top+PH/2}" transform="rotate(-90 16 {top+PH/2})" text-anchor="middle">{lab}</text>')
    out.append(f'<line class="a" x1="{X(3700)}" x2="{X(3700)}" y1="{top}" y2="{top+PH}" stroke-dasharray="2 3"/>')
for yr, bt in ((2019, 1484), (2020, 1849), (2021, 2215), (2022, 2580), (2023, 2945), (2024, 3310), (2025, 3676), (2026, 4041), (2027, 4406), (2028, 4772)):
    out.append(f'<text x="{X(bt)}" y="{H-28}" text-anchor="middle">{yr}</text>') if bt >= X0 else None
out.append(f'<text x="{(W+L)/2}" y="{H-8}" text-anchor="middle">year (TESS data end at s86, dotted line; models continue)</text>')
for i in range(len(t)):
    out.append(f'<circle class="o" cx="{X(t[i]):.1f}" cy="{panel(ph[i], *rngs[0], tops[0]):.1f}" r="3"/>')
    out.append(f'<circle class="o" cx="{X(t[i]):.1f}" cy="{panel(dep[i], *rngs[1], tops[1]):.1f}" r="3"/>')
for fn, cls, name in ((sys.argv[2], 'm1', 'low'), (sys.argv[3], 'm2', 'gaia')):
    r = json.load(open(fn)); p = r['params']; x = [p[k] for k in F.NAMES]
    tt = np.arange(1770, X1, F.P_IN)
    prim, sec = F.model_phases(x, r['e_out'], tt, span=X1 - F.T_START)
    pt = np.array([a for a, _ in prim])
    pts_p, pts_d, B = [], [], []
    for s_, b in sec:
        k = np.searchsorted(pt, s_) - 1
        if k < 0: continue
        pts_p.append((s_, (s_ - pt[k]) / F.P_IN)); B.append(b)
    _, D0 = F.depth_term(np.array(F.phases_at(prim, sec, t)[1]), dep)
    D = D0 * F.covered_fraction(np.array(B) / F.RSUN)
    out.append(f'<polyline class="{cls}" points="' + ' '.join(f'{X(a):.1f},{panel(min(max(v,0.44),0.55), *rngs[0], tops[0]):.1f}' for a, v in pts_p) + '"/>')
    out.append(f'<polyline class="{cls}" points="' + ' '.join(f'{X(a):.1f},{panel(v, *rngs[1], tops[1]):.1f}' for (a, _), v in zip(pts_p, D)) + '"/>')
    lab = f"e_out = {r['e_out']:.2f}, m3 = {p['m3']:.2f} Msun, i_mut = {p['i_mut_deg']:.1f} deg (chi2 {r['chi2']:.0f})"
    yy = T + 16 if name == 'low' else T + 32
    out.append(f'<line class="{cls}" x1="{L+10}" x2="{L+40}" y1="{yy-4}" y2="{yy-4}"/><text x="{L+46}" y="{yy}">{lab}</text>')
out.append('</svg>')
open(sys.argv[4], 'w').write('\n'.join(o for o in out if o))
print('wrote', sys.argv[4])
