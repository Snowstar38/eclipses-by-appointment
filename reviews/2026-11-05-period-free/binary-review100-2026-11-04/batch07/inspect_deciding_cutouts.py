"""WCS-centred diagnostic on two uncached TESS sectors; not a QLP substitute."""
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS

B = Path(__file__).resolve().parent
Q = {r['tic']: r for r in csv.DictReader((B / 'queue.csv').open())}
for tic, sector in [('368903210', 59), ('321154190', 66)]:
    p = B / tic / f's{sector}-tesscut.fits'
    with fits.open(p, memmap=False) as h:
        a = h[1].data
        time = np.asarray(a['TIME'], float)
        quality = np.asarray(a['QUALITY'], int)
        flux = np.asarray(a['FLUX'], float)
        x, y = WCS(h[2].header).all_world2pix(float(Q[tic]['ra_deg']), float(Q[tic]['dec_deg']), 0)
    yy, xx = np.indices(flux.shape[1:])
    aperture = (abs(xx-x) <= 1.5) & (abs(yy-y) <= 1.5)
    target = np.nansum(flux[:, aperture], axis=1)
    good = np.isfinite(time) & (quality == 0) & np.isfinite(target) & (target > 0)
    tg, fg = time[good], target[good]
    normalized = fg / np.median(fg)
    fig, ax = plt.subplots(figsize=(11, 3))
    ax.plot(tg, normalized, '.', ms=1)
    ax.set(xlabel='BTJD', ylabel='3x3 FFI flux / sector median', title=f'TIC {tic} s{sector}; WCS x={x:.2f} y={y:.2f}')
    fig.tight_layout()
    fig.savefig(B / tic / f's{sector}-cutout-lightcurve.png', dpi=130)
    plt.close(fig)
    rec = {'tic': tic, 'sector': sector, 'fits_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
           'wcs_target_x': float(x), 'wcs_target_y': float(y),
           'aperture_pixels': np.argwhere(aperture).tolist(),
           'n_quality0_positive_target': int(good.sum()),
           'time_start_btjd': float(tg.min()) if len(tg) else None,
           'time_end_btjd': float(tg.max()) if len(tg) else None,
           'positive_target_flux_fraction_quality0': float(np.mean(target[quality == 0] > 0)),
           'flux_median': float(np.median(fg)) if len(fg) else None,
           'note': 'Cutout 3x3 WCS aperture is an exploratory independent reduction. Zero-flux samples are missing evidence, never eclipse nulls.'}
    (B / tic / f's{sector}-cutout-inspection.json').write_text(json.dumps(rec, indent=2) + '\n')
    print(tic, sector, rec['n_quality0_positive_target'], rec['positive_target_flux_fraction_quality0'], flush=True)
