"""Hash-checked representative raw SAP windows for frozen batch01."""
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

B = Path(__file__).resolve().parent
S = B.parent.parent / 'binary-exploration-2026-11-04' / 'bulk-results'
Q = list(csv.DictReader((B / 'queue.csv').open(newline='', encoding='utf-8')))

for row in Q:
    tic = row['tic']
    data_path = S / f'{tic}.json'
    raw = data_path.read_bytes()
    obj = json.loads(raw)
    outdir = B / tic
    outdir.mkdir(exist_ok=True)
    sectors = []
    windows = []
    for item in obj['files']:
        if item['status'] != 'ok':
            sectors.append({'sector': item['sector'], 'status': item['status']})
            continue
        fp = Path(item['path'])
        actual = hashlib.sha256(fp.read_bytes()).hexdigest()
        if actual != item['sha256']:
            raise RuntimeError(f'hash mismatch: {fp}')
        with fits.open(fp, memmap=False) as h:
            arr = h[1].data
            t = np.asarray(arr['TIME'], float)
            f = np.asarray(arr['SAP_FLUX'], float)
            q = np.asarray(arr['QUALITY'], int)
        valid = np.isfinite(t) & np.isfinite(f) & (f > 0)
        good = valid & (q == 0)
        sectors.append({'sector': item['sector'], 'path': str(fp), 'sha256': actual,
                        'time_start': float(np.min(t[good])), 'time_end': float(np.max(t[good])),
                        'n_quality0': int(np.sum(good)), 'cadence_days': float(np.median(np.diff(t[good])))})
        flagged = [w for w in item['windows'] if w['flag']]
        picks = sorted(flagged, key=lambda w: abs(w['contrast']), reverse=True)[:2]
        for w in picks:
            c = float(w['time']); d = float(w['duration']); half = max(2*d, .7)
            select = good & (abs(t-c) < half)
            side = select & (abs(t-c) > max(.65*d, .18))
            if np.sum(select) < 10 or np.sum(side) < 6:
                continue
            baseline = float(np.median(f[side]))
            x = t[select]-c; y = f[select]/baseline
            core = abs(x) < max(.25*d, .08)
            left = side & (t<c); right = side & (t>c)
            flank = f[side]/baseline
            win = {'sector': item['sector'], 'kind': w['kind'], 'screen_center_btjd': c,
                   'screen_duration_days': d, 'screen_contrast': w['contrast'],
                   'screen_supported': w['supported'], 'n_window_quality0': int(np.sum(select)),
                   'n_core': int(np.sum(core)), 'n_left': int(np.sum(left)),
                   'n_right': int(np.sum(right)),
                   'local_baseline_flux': baseline,
                   'core_median_delta_ppt': float((np.median(y[core])-1)*1000) if np.sum(core) else None,
                   'side_mad_ppt': float(1482.6*np.median(abs(flank-np.median(flank)))),
                   'plot_x_days': x.tolist(), 'plot_y': y.tolist()}
            windows.append(win)
    plotwins = sorted(windows, key=lambda w: (w['kind']!='dip', -abs(w['screen_contrast'])))[:12]
    if plotwins:
        fig, axes = plt.subplots(len(plotwins), 1, figsize=(9, 2.25*len(plotwins)), squeeze=False)
        for ax, w in zip(axes[:, 0], plotwins):
            ax.scatter(w['plot_x_days'], w['plot_y'], s=4, alpha=.65)
            ax.axvline(0, color='r', lw=.6)
            ax.axhline(1, color='k', lw=.5)
            ax.set_title(f"s{w['sector']} {w['kind']} screen BTJD {w['screen_center_btjd']:.3f}, core {w['core_median_delta_ppt']:.1f} ppt", fontsize=9)
            ax.set_ylabel('SAP / local median')
        axes[-1, 0].set_xlabel('days from screening window (not fitted eclipse center)')
        fig.tight_layout()
        fig.savefig(outdir / 'raw-windows.png', dpi=120)
        plt.close(fig)
    for w in windows:
        del w['plot_x_days'], w['plot_y']
    result = {'sample_id': row['sample_id'], 'tic': tic, 'bulk_json_path': str(data_path),
              'bulk_json_sha256': hashlib.sha256(raw).hexdigest(),
              'gaia_period_days': float(row['gaia_period_days']), 'sectors': sectors,
              'representative_flagged_windows': windows,
              'caution': 'Screening centers and local core medians are not eclipse timing or fitted depths. Panels use raw SAP_FLUX and QUALITY=0.'}
    (outdir / 'raw-inspection.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(row['sample_id'], tic, len(sectors), len(windows), flush=True)
