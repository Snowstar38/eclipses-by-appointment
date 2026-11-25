"""Diagnose periodogram peaks per sector and the source of archived event seeds."""
import argparse
import json
from pathlib import Path

import numpy as np
from astropy.timeseries import LombScargle

from timing import HERE, mad


def sinusoid(t, f, period, ref):
    phase = 2*np.pi*(t-ref)/period
    x = np.column_stack([np.ones(len(t)),t-np.median(t),np.sin(phase),np.cos(phase)])
    coef,*_ = np.linalg.lstsq(x,f,rcond=None)
    residual = f-x@coef
    null = f-x[:,:2]@np.linalg.lstsq(x[:,:2],f,rcond=None)[0]
    amp = float(np.hypot(coef[2],coef[3]))
    minimum_phase = float((.75-np.arctan2(coef[3],coef[2])/(2*np.pi))%1)
    return dict(amplitude_ppt=amp, minimum_phase=minimum_phase,
                residual_mad_ppt=float(mad(residual)),
                local_power=float(1-np.sum(residual**2)/np.sum(null**2)))


def sector_periodogram(t, f, candidates):
    # Rebin to 0.05 d and clip extreme outliers for exploratory variability.
    good = np.abs(f-np.median(f)) < max(12*mad(f), 10.)
    _, inverse = np.unique(np.floor((t[good]-t[0])/.05),return_inverse=True)
    n = np.bincount(inverse)
    t,f = [np.bincount(inverse,x[good])/n for x in (t,f)]
    if len(t)<30:
        return {}
    model=LombScargle(t,f)
    freq,power=model.autopower(minimum_frequency=1/8,maximum_frequency=7,samples_per_peak=15)
    peak=int(np.argmax(power))
    return dict(period_days=float(1/freq[peak]), power=float(power[peak]), fits={
        label:sinusoid(t,f,p,2000) for label,p in candidates.items()
    })


def diagnose(t,s,d,center,w):
    x=(t-center)/w
    windows=[(-2.5,-1.3),(-1.3,-.55),(-.55,.55),(.55,1.3),(1.3,2.5)]
    points=[]
    for a,b in windows:
        take=(x>=a)&(x<b)
        points.append(dict(n=int(take.sum()), sap_median=float(np.median(s[take])) if any(take) else None,
                           det_median=float(np.median(d[take])) if any(take) else None))
    use=(x>=-2.5)&(x<2.5)
    return dict(windows=points, offsets_days=(t[use]-center).round(6).tolist(),
                sap_ppt=s[use].round(4).tolist(), det_ppt=d[use].round(4).tolist())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=HERE.parent/'cadences')
    cache = parser.parse_args().cache
    all_results=[]
    for item in json.loads((HERE/'timing.json').read_text()):
        tic=item['tic']
        candidates={k:m['period_days'] for k,m in item['models'].items() if
                    k.startswith(('ls_','box_')) and m['period_days']<8}
        segments=[]
        for path in sorted(cache.glob(tic+'-*.npz')):
            sector=int(path.stem.split('-')[-1])
            with np.load(path) as a:
                good=np.isfinite(a['t']+a['sap']+a['pdc'])
                t,s,d=[a[k][good] for k in ('t','sap','pdc')]
            s,d=[(f/np.median(f)-1)*1000 for f in (s,d)]
            diagnostics={}
            for tag,m in item['models'].items():
                if tag not in ('archived_P','archived_P2','gaia_at_archived_epoch'):
                    continue
                for e in m['predictions']:
                    if e['sector']==sector:
                        w=m['width_days']
                        diagnostics[f"{tag}:{e['center_btjd']:.6f}"]=diagnose(t,s,d,e['center_btjd'],w)
            segments.append(dict(sector=sector, BTJD=[float(min(t)),float(max(t))],
                                 detrended=sector_periodogram(t,d,candidates),
                                 sap=sector_periodogram(t,s,candidates),diagnostics=diagnostics))
        all_results.append(dict(tic=tic,segments=segments))
    (HERE/'diagnostics.json').write_text(json.dumps(all_results,separators=(',',':'),allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
