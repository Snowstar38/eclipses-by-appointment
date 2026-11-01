"""Bounded per-event source-position audit of the saved s53 TESScut stack."""
import json
import math
from pathlib import Path

import numpy as np
from astropy.io import fits
from astropy.wcs import WCS

B = Path(__file__).parent
tic = '368260545'
cut = Path('[local path omitted]')
G = json.load(open('[local path omitted] 5/made/sb1-scale/diffimg/368260545/gaia.json'))
pixel = json.load(open('[local path omitted] 5/made/sb1-scale/diffimg/368260545/diff_s53.json'))
with fits.open(cut, memmap=False) as h:
    a = h[1].data
    t = np.asarray(a['TIME'], float)
    F = np.asarray(a['FLUX'], float)
    q = np.asarray(a['QUALITY'], int)
    wcs = WCS(h[2].header)
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1) & (q == 0)
t, F = t[ok], F[ok]
flat = F.reshape(len(t), -1)
bk = np.array([np.median(np.sort(r)[:int(0.4 * len(r))]) for r in flat])
F = F - bk[:, None, None]
target = pixel['target_px']
nb = next(n for n in pixel['neighbours_60'] if n['possible'])['px']
yy, xx = np.mgrid[:F.shape[1], :F.shape[2]]
ix, iy = map(lambda z: int(round(z)), target)
mask = (np.abs(xx - ix) <= 2) & (np.abs(yy - iy) <= 2)
dur = 0.18
events = []
for old in pixel['events']:
    tp = old['t']
    dt = abs(t - tp)
    mi = dt < 0.3 * dur
    mo = (dt > 0.75 * dur) & (dt < 1.75 * dur)
    pre, post = mo & (t < tp), mo & (t > tp)
    din = np.median(F[mi], axis=0)
    dout = (np.median(F[pre], axis=0) + np.median(F[post], axis=0)) / 2
    D = dout - din
    weight = np.clip(D, 0, None) * mask
    cen = [(weight * xx).sum() / weight.sum(), (weight * yy).sum() / weight.sum()]
    # Flux-weighted centroid's sampling distribution across independently
    # repeated eclipse windows is more informative than a single stack center.
    events.append({'cycle': old['cycle'], 'center_px': cen,
                   'distance_to_target_px': math.dist(cen, target),
                   'distance_to_capable_neighbor_px': math.dist(cen, nb),
                   'deficit_total': float(D[mask].sum())})
centers = np.array([e['center_px'] for e in events])
mean = centers.mean(axis=0)
sd = centers.std(axis=0, ddof=1)
out = {'tic': tic, 'sector': 53, 'target_px': target, 'capable_neighbor_px': nb,
       'target_neighbor_separation_px': math.dist(target, nb),
       'per_event': events, 'mean_center_px': mean.tolist(),
       'event_scatter_px': sd.tolist(), 'mean_distance_to_target_px': math.dist(mean, target),
       'mean_distance_to_neighbor_px': math.dist(mean, nb),
       'method': 'Recomputed local-background-subtracted TESScut difference for four historical windows with the same 0.18-d duration and core/side windows as diffstack.py; centroid uses positive deficit in 5x5 pixels around target. Scatter across only four events is descriptive, not a calibrated positional confidence interval.'}
(B / tic / 'pixel-event-audit.json').write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
