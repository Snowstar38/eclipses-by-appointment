"""Measure the event clocks in TESS-SPOC instead of QLP, retaining unavailable sectors."""
import argparse
import hashlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import requests
from scipy.stats import binned_statistic

from frames import HERE, rows, save


def fetch(job):
    tic,sec,cache=job
    digits=f'{int(tic):016d}'
    tag=f's{int(sec):04d}'
    folders='/'.join(digits[i:i+4] for i in range(0,16,4))
    url=f'https://archive.stsci.edu/hlsps/tess-spoc/{tag}/target/{folders}/hlsp_tess-spoc_tess_phot_{digits}-{tag}_tess_v1_lc.fits'
    path=cache/f'{tic}-{sec}-lc.fits'
    try:
        if not path.exists():
            r=requests.get(url,timeout=35)
            r.raise_for_status()
            assert r.content.startswith(b'SIMPLE')
            path.write_bytes(r.content)
        return dict(tic=tic,sector=sec,url=url,sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    except requests.RequestException as exc:
        return dict(tic=tic,sector=sec,url=url,error=str(exc))


def main(cache):
    clocks=rows(HERE/'clocks.csv')
    cache.mkdir(parents=True,exist_ok=True)
    pairs=list(dict.fromkeys((r['tic'],r['sector'],cache) for r in clocks))
    with ThreadPoolExecutor(4) as pool: inputs=list(pool.map(fetch,pairs))
    save(HERE/'spoc-inputs.csv',inputs)
    results=[]
    for tic in dict.fromkeys(r['tic'] for r in clocks):
        plots=[]
        for r in (r for r in clocks if r['tic']==tic):
            path=cache/f"{tic}-{r['sector']}-lc.fits"
            if not path.exists():continue
            p,e,w=[float(r[k]) for k in ('period_d','epoch_btjd','width_d')]
            with fits.open(path) as h:
                assert int(h[0].header['TICID'])==int(tic) and int(h[0].header['SECTOR'])==int(r['sector'])
                d=h[1].data
                t=d['TIME']
                good=(d['QUALITY']==0)&np.isfinite(t)
                for name in ('SAP_FLUX','PDCSAP_FLUX'):good &= np.isfinite(d[name])&(d[name]>0)
                if good.sum()<5:continue
                dt=t-e
                if p:dt=(dt+p/2)%p-p/2
                sel=good&(abs(dt)<=3*w)
                centers=[e] if not p else e+p*np.arange(np.ceil((min(t[good])-e)/p),np.floor((max(t[good])-e)/p)+1)
                sep=np.median(np.diff(t[good]))
                values=[[],[]]
                traces=[[],[]]
                coords=[]
                for center in centers:
                    dist=t-center
                    masks=[good&(dist>=-2*w)&(dist<=-w),good&(abs(dist)<.35*w),good&(dist>=w)&(dist<=2*w)]
                    if any(m.sum()<max(2,.6*k*w/sep) for m,k in zip(masks,[1,.7,1])):continue
                    near=good&(abs(dist)<=2*w)
                    coords.extend(dist[near])
                    for j,name in enumerate(('SAP_FLUX','PDCSAP_FLUX')):
                        flux=d[name]
                        base=np.interp(dist,[np.median(dist[m]) for m in masks[::2]],
                                       [np.median(flux[m]) for m in masks[::2]])
                        y=1000*(flux/base-1)
                        traces[j].extend(y[near])
                        values[j].append(np.median(y[masks[1]]))
                if not coords:continue
                out=dict(**r,events=len(values[0]),SAP_change_ppt=round(float(np.median(values[0])),3),
                         PDC_change_ppt=round(float(np.median(values[1])),3))
                results.append(out)
                edges=np.linspace(-2*w,2*w,61)
                plots.append((out,(edges[1:]+edges[:-1])/2,[binned_statistic(coords,z,'median',edges)[0] for z in traces]))
        if plots:
            fig,axes=plt.subplots(1,len(plots),squeeze=False,figsize=(max(5,3.25*len(plots)),3.4),layout='constrained')
            for ax,(out,x,ys) in zip(axes.flat,plots):
                for y,color,label in zip(ys,['#215b95','#d2742c'],['SAP','PDC']):
                    ax.plot(x,y,color=color,label=label)
                ax.set(title=f"S{out['sector']}   {out['events']} event(s)",xlabel='Days from event center')
            axes[0,0].set_ylabel('Relative flux (ppt)')
            axes[0,0].legend()
            fig.suptitle(f'TIC {tic}   |   TESS-SPOC at QLP prediction')
            fig.savefig(HERE/f'spoc-{tic}.png',dpi=125)
            plt.close(fig)
    if results:save(HERE/'spoc-measurements.csv',results)


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('cache',type=Path)
    main(ap.parse_args().cache)
