"""Fixed-period control phases and the provisional two-window TIC 197243461 clock."""
import argparse
import json
from pathlib import Path

import numpy as np

from timing import HERE, STEP, predictions, prepare


def get_curves(cache,tic):
    return prepare(list(cache.glob(tic+'-*.npz')))[0]


def signed_score(curves, centers, period, width):
    all_values = []
    for curve in curves:
        g = curve['grid']
        for k in range(int(np.floor((g[0]-centers[-1])/period)), int(np.ceil((g[-1]-centers[0])/period))+1):
            ix = np.rint((centers+k*period-g[0])/STEP).astype(int)
            keep = (ix>=0)&(ix<len(g))
            clipped = np.clip(ix,0,len(g)-1)
            s,d = curve['scores'][width]
            values = np.where(keep,np.minimum(s[clipped],d[clipped]),np.nan)
            if np.isfinite(values).any():
                all_values.append(values)
    a = np.asarray(all_values)
    coverage = np.isfinite(a).sum(axis=0)
    score = np.sum(np.clip(np.nan_to_num(a),-3,8),axis=0)/np.sqrt(np.maximum(1,coverage))
    return coverage, score


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=HERE.parent/'cadences')
    cache = parser.parse_args().cache
    all_results=[]
    for item in json.loads((HERE/'timing.json').read_text()):
        tic = item['tic']
        curves = get_curves(cache,tic)
        m = item['models']['archived_P']
        period,epoch,width = [m[k] for k in ('period_days','epoch_btjd','width_days')]
        w = min(curves[0]['scores'], key=lambda v:abs(v-width))
        centers = np.arange(0,period,STEP)+epoch
        cover, scores = signed_score(curves,centers,period,w)
        eligible = cover>=max(2,int(cover[0]))
        offsets = ((centers-epoch+period/2)%period)-period/2
        eligible &= abs(offsets)>=2*width
        out = dict(tic=tic,period=period,epoch=epoch,scoring_width=w,covered=int(cover[0]),
                   score=float(scores[0]),comparable_control_phases=int(eligible.sum()),
                   control_phases_at_least_as_deep=int((eligible&(scores>=scores[0])).sum()))
        if tic == '197243461':
            sensitivity = json.loads((HERE/'sensitivity.json').read_text())
            epochs = sorted(row['locally_recentered']['btjd'] for row in sensitivity if
                row['tic']==tic and row['model']=='archived_P' and row['locally_recentered'])
            cycles=round((epochs[1]-epochs[0])/period)
            fit=(epochs[1]-epochs[0])/cycles
            out['two_window_fit']=dict(period=fit,epoch=epochs[0],width=width,
                cycles=cycles,predictions=predictions(curves,fit,epochs[0],width))
        all_results.append(out)
    (HERE/'controls.json').write_text(json.dumps(all_results,indent=2,allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
