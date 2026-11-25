"""Check local epoch/width/baseline sensitivity for the archived event candidates."""
import argparse
import json
from pathlib import Path

import numpy as np

from timing import HERE


def measurements(t, s, d, center, w, flank_near, flank_far):
    edges = np.searchsorted(t, center + w*np.array(
        [-flank_far,-flank_near,-.5,.5,flank_near,flank_far]))
    zones = [slice(a,b) for a,b in zip(edges[::2],edges[1::2])]
    tx = [t[k] for k in zones]
    dt = np.median(np.diff(t))
    if min(map(len,tx)) < max(2,.60*w/dt):
        return None
    gap = np.max(np.diff(t[edges[0]:edges[-1]]),initial=0)
    if gap > max(.36*w,2.2*dt):
        return None
    left,core,right = [np.median(x) for x in tx]
    weight = (core-left)/(right-left)
    values = []
    for f in (s,d):
        a,b,c = [np.median(f[k]) for k in zones]
        base = a+weight*(c-a)
        values.append(float(1000*(1-b/base)))
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=HERE.parent/'cadences')
    cache = parser.parse_args().cache
    results=[]
    for item in json.loads((HERE/'timing.json').read_text()):
        for tag in ('archived_P','gaia_at_archived_epoch','gaia','fold_refit'):
            m=item['models'][tag]
            for event in m['predictions']:
                sec=event['sector']
                with np.load(cache/f"{item['tic']}-{sec}.npz") as a:
                    good=np.isfinite(a['t']+a['sap']+a['pdc'])
                    t,s,d=[a[k][good] for k in ('t','sap','pdc')]
                w=m['width_days']
                center=event['center_btjd']
                checks={}
                for mult in (.75,1.,1.5):
                    this_width=w*mult
                    for near,far in ((.65,1.45),(.70,1.75),(.85,2.40)):
                        key=f'{mult:.2f}/{near:.2f}/{far:.2f}'
                        values=measurements(t,s,d,center,this_width,near,far)
                        checks[key]=values
                grid=[]
                for shift in np.linspace(-.5,.5,25):
                    epoch=center+w*shift
                    v=measurements(t,s,d,epoch,w,.70,1.75)
                    if v is not None:
                        grid.append(dict(btjd=epoch,sap_ppt=v[0],det_ppt=v[1]))
                results.append(dict(tic=item['tic'],model=tag,sector=sec,prediction_btjd=center,
                                    checks=checks,locally_recentered=max(
                                        grid,key=lambda x:min(x['sap_ppt'],x['det_ppt']),default=None)))
    (HERE/'sensitivity.json').write_text(json.dumps(results,indent=2,allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
