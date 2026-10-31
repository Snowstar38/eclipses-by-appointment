"""Blind dip census: raw QLP SAP_FLUX (q==0, and all-q), 0.35-d sliding box vs local linear baseline (0.4-1.2 d either side);
list local maxima of box depth > 0.2%. python census.py"""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vetlib import load_qlp
D = '[local path omitted]'
for s in (12, 39, 65, 103):
    for allq in (False, True):
        d = load_qlp(D + f'255077215_s{s:03d}.fits', allq=allq); t, f = d['t'], d['f']
        grid = np.arange(t.min() + 0.3, t.max() - 0.3, 0.02); dep = np.full(len(grid), np.nan)
        for i, tc in enumerate(grid):
            inn = np.abs(t - tc) < 0.175; out = (np.abs(t - tc) > 0.4) & (np.abs(t - tc) < 1.2)
            if inn.sum() < 3 or out.sum() < 10: continue
            c = np.polyfit(t[out] - tc, f[out], 1); dep[i] = 1 - np.median(f[inn]) / np.polyval(c, 0)
        hits = []
        for i in range(1, len(grid) - 1):
            if np.isfinite(dep[i]) and dep[i] > 0.002 and dep[i] == np.nanmax(dep[max(0, i - 15):i + 16]): hits.append((grid[i], dep[i]))
        print(f"s{s} {'allq' if allq else 'q0'}: " + ', '.join(f'{a:.2f} ({b*100:.2f}%)' for a, b in hits))
