"""Audit the archived, Gaia, harmonics and exploratory clocks on original cadences."""
import argparse
import csv
import json
from pathlib import Path

import numpy as np
from astropy.timeseries import BoxLeastSquares, LombScargle

HERE = Path(__file__).resolve().parent
WIDTHS = (0.04, 0.07, 0.12, 0.20, 0.32, 0.50, 0.80)
STEP = 0.008


def mad(x):
    return 1.4826 * np.median(np.abs(x - np.median(x)))


def make_grid(t, flux, grid, w):
    # Compute three fixed windows per center. Both flanks constrain a linear baseline.
    cols = np.searchsorted(t, grid[:, None] + w*np.array([-1.75,-.70,-.5,.5,.70,1.75]))
    counts = cols[:, 1::2] - cols[:, ::2]
    dt = np.median(np.diff(t))
    valid = np.all(counts >= max(2, .60*w/dt), axis=1)
    valid &= (cols[:, 0] > 0) & (cols[:, -1] < len(t))
    gaps = np.r_[0, np.cumsum(np.r_[np.diff(t) > max(2.2*dt, 0.36*w), False])]
    valid &= gaps[np.maximum(0, cols[:, -1]-1)] == gaps[cols[:, 0]]
    if not np.any(valid):
        return np.full(len(grid), np.nan)
    cols = cols[valid]
    count = counts[valid]
    cumulative_flux = np.r_[0., np.cumsum(flux)]
    cumulative_time = np.r_[0., np.cumsum(t - t[0])]
    m = (cumulative_flux[cols[:, 1::2]] - cumulative_flux[cols[:, ::2]])/count
    times = (cumulative_time[cols[:, 1::2]] - cumulative_time[cols[:, ::2]])/count
    frac = (times[:, 1]-times[:, 0])/(times[:, 2]-times[:, 0])
    baseline = m[:, 0]+frac*(m[:, 2]-m[:, 0])
    depth = (1-m[:, 1]/baseline)*1000
    # Empirical scatter of comparable bracketed windows includes correlated residuals.
    out = np.full(len(grid), np.nan)
    scale = max(mad(depth), 0.03)
    out[valid] = depth / scale
    return out


def prepare(paths):
    curves = []
    starts = []
    dets = []
    for filename in paths:
        with np.load(filename) as a:
            good = np.isfinite(a['t']+a['sap']+a['pdc'])
            t, sap, det = [a[k][good] for k in ('t','sap','pdc')]
        if len(t) < 30 or min(np.median(sap), np.median(det)) <= 0:
            continue
        order = np.argsort(t)
        t, sap, det = t[order], sap[order], det[order]
        # Use a bounded excursion filter only for the exploratory periodograms.
        x = det/np.median(det)-1
        scan = np.abs(x) < max(0.01, 12*mad(x))
        _, inv = np.unique(np.floor((t[scan]-t[0])/.04).astype(int), return_inverse=True)
        n = np.bincount(inv)
        if len(n) >= 30:
            tt = np.bincount(inv,t[scan])/n
            ff = np.bincount(inv,x[scan])/n
            starts.append(tt)
            dets.append(ff)
        grid = np.arange(t[0], t[-1], STEP)
        sector = int(filename.stem.split('-')[-1])
        curves.append(dict(t=t, sap=sap, det=det, sector=sector, grid=grid,
                           scores={w: (make_grid(t,sap,grid,w), make_grid(t,det,grid,w)) for w in WIDTHS}))
    return sorted(curves,key=lambda c:c['t'][0]), np.concatenate(starts), np.concatenate(dets)


def at_phase(curves, p, w, ep=None):
    anchor = min(c['grid'][0] for c in curves)
    phases = np.arange(0, p, STEP) + anchor if ep is None else np.asarray([ep])
    all_scores = []
    for c in curves:
        t, g = c['t'], c['grid']
        lo = int(np.floor((t[0]-phases[-1])/p))
        hi = int(np.ceil((t[-1]-phases[0])/p))
        for cycle in range(lo, hi+1):
            idx = np.rint((phases + cycle*p-g[0])/STEP).astype(int)
            inside = (idx>=0)&(idx<len(g))
            ix = np.clip(idx,0,len(g)-1)
            sap, det = [np.where(inside,sc[ix],np.nan) for sc in c['scores'][w]]
            both = np.isfinite(sap+det)
            z = np.where(both, np.minimum(sap,det), np.nan)
            if np.isfinite(z).any():
                all_scores.append(z)
    if not all_scores:
        return (float(phases[0]), 0., 0, 0)
    a = np.stack(all_scores)
    hits = np.sum(a>=3, axis=0)
    covered = np.sum(np.isfinite(a),axis=0)
    evidence = np.sum(np.clip(np.nan_to_num(a), -3, 8),axis=0) / np.sqrt(np.maximum(covered,1))
    # Give priority to independently supported windows. Cap isolated anomalies.
    order = np.lexsort((evidence,hits))
    i = order[-1]
    return (float(phases[i]), float(evidence[i]), int(hits[i]), int(covered[i]))


def measure(c, center, w):
    t = c['t']
    bounds = center+w*np.array([-1.75,-.70,-.5,.5,.70,1.75])
    idx = np.searchsorted(t, bounds)
    zones = [slice(a,b) for a,b in zip(idx[::2],idx[1::2])]
    times = [t[k] for k in zones]
    counts = [len(x) for x in times]
    dt = np.median(np.diff(t))
    record = dict(n_left=counts[0],n_core=counts[1],n_right=counts[2])
    global_gap = np.max(np.diff(t[idx[0]:idx[-1]]), initial=0.)
    if min(counts) < max(2, .60*w/dt) or global_gap > max(2.2*dt, .36*w):
        return dict(record, coverage='partial')
    mtime = [np.median(z) for z in times]
    weight = (mtime[1]-mtime[0])/(mtime[2]-mtime[0])
    widths_index = min(WIDTHS, key=lambda x:abs(x-w))
    for label, score in zip(('sap','det'),c['scores'][widths_index]):
        f = c[label]
        m = [np.median(f[k]) for k in zones]
        baseline = m[0]+weight*(m[2]-m[0])
        noise = mad(np.r_[f[zones[0]]-m[0],f[zones[2]]-m[2]]) / baseline * 1000
        record[label+'_ppt'] = round(1000*(1-m[1]/baseline),4)
        record[label+'_side_mad_ppt'] = round(noise,4)
        local_bins = np.searchsorted(t,center+w*np.linspace(-1.75,1.75,15))
        local_shape = [
            round(1000*(1-np.median(f[a:b])/(m[0]+(m[2]-m[0])*
               (np.median(t[a:b])-mtime[0])/(mtime[2]-mtime[0]))),3) if b>a else None
            for a,b in zip(local_bins[:-1],local_bins[1:])
        ]
        record[label+'_profile_ppt'] = local_shape
        i = round((center-c['grid'][0])/STEP)
        record[label+'_empirical_z'] = round(float(score[i]),3) if 0<=i<len(score) and np.isfinite(score[i]) else None
    return dict(record, coverage='full', core_time_btjd=float(mtime[1]))


def predictions(curves, p, ep, w):
    out = []
    for c in curves:
        t=c['t']
        for k in range(int(np.ceil((t[0]-ep)/p)), int(np.floor((t[-1]-ep)/p))+1):
            center = ep+k*p
            out.append(dict(sector=c['sector'], cycle=k, center_btjd=center, **measure(c,center,w)))
    return out


def exploratory(t, f):
    # Include both sinusoidal modulation and box searches. Coarse bins limit leverage
    # from cadence changes. The full data are used again for epoch-level validation.
    order = np.argsort(t)
    t, f = t[order], f[order]
    var = max(mad(f), .00003)
    ls = LombScargle(t, f)
    freq, power = ls.autopower(minimum_frequency=1/100, maximum_frequency=5, samples_per_peak=5)
    results = []
    for _ in range(3):
        i = int(np.argmax(power))
        results.append((f'ls_{len(results)+1}',float(1/freq[i]),float(power[i])))
        power[np.abs(freq-freq[i])<3/np.ptp(t)] = 0
    # Evaluate a broad logarithmic period grid with 0.1 d minimum duration.
    grid = 1/np.linspace(1/100, 1/.75, 4000)
    box = BoxLeastSquares(t, f, dy=np.full(len(t),var)).power(grid,[.10,.22,.48],oversample=5)
    power = box.power.copy()
    for j in range(3):
        i = int(np.argmax(power))
        results.append((f'box_{j+1}',float(grid[i]),float(power[i])))
        power[np.abs(1/grid-1/grid[i]) < 3/np.ptp(t)] = 0
    return results


def run(r, cache, original_models):
    tic = r['tic']
    src = original_models[tic]
    c, t, f = prepare(list(cache.glob(tic+'-*.npz')))
    models = {}
    def model(tag,p,ep,w, **extras):
        models[tag] = dict(period_days=p, epoch_btjd=ep, width_days=w, **extras,
                           predictions=predictions(c,p,ep,w))
    for source in ('P','P2'):
        b = src[source]
        model('archived_'+source,b['P'],b['t0'],b['dur'], archive_depth_ppm=b['depth'])
    gp = float(r['gaia_period_days'])
    options = [('gaia',gp,0),('gaia_half',gp/2,0),('gaia_double',gp*2,0),
               ('fold_refit',src['P']['P'],0),('fold_half_refit',src['P']['P']/2,0),
               ('fold_double_refit',src['P']['P']*2,0),('archived_P2_refit',src['P2']['P'],0),
               *exploratory(t,f)]
    for tag,p,power in options:
        fits = [(at_phase(c,p,w),w) for w in WIDTHS if w <= .24*p]
        (ep, evidence, hits, covered), w = max(fits,key=lambda item:(item[0][2],item[0][1]))
        model(tag,p,ep,w,grid_score=evidence,grid_hits=hits,grid_covered=covered,
              periodogram_power=power)
    for tag,p in [('gaia_at_archived_epoch',gp),('gaia_half_at_archived_epoch',gp/2),
                  ('gaia_double_at_archived_epoch',gp*2)]:
        b=src['P']
        model(tag,p,b['t0'],b['dur'])
    return dict(tic=tic, original_record=src['original_record'],
                sectors=[v['sector'] for v in c], models=models)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=HERE.parent/'cadences')
    parser.add_argument('--tic')
    args=parser.parse_args()
    original_models=json.loads((HERE/'original-fold-models.json').read_text())
    results=[]
    with (HERE.parent/'batch.csv').open() as stream:
        for row in csv.DictReader(stream):
            if args.tic and args.tic != row['tic']:
                continue
            result=run(row,args.cache,original_models)
            results.append(result)
            print(row['tic'],flush=True)
            (HERE / ('timing-'+args.tic+'.json' if args.tic else 'timing.json')).write_text(
                json.dumps(results,separators=(',',':'),allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
