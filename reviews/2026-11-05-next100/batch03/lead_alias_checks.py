"""Bounded neighboring integer-cycle predictions and actual cadence coverage."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
for tic,centers,ns in [('70887357',(1454.3408972358316,2178.1690328238556),list(range(10,21))),('94255849',(1588.4142892400582,4075.502275612701),list(range(50,65)))]:
    d=json.loads((B/tic/'lead-measurements.json').read_text())
    sources={int(Path(x['path']).stem.split('_s')[-1]):x for x in d['source_receipts']}
    data={}
    for sec,src in sources.items():
        fp=Path(src['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
        data[sec]=(t[ok],f[ok],src['sha256'])
    out=[]
    for n in ns:
        p=(centers[1]-centers[0])/n
        predicted=[]
        for sec,(t,f,sha) in data.items():
            cad=float(np.median(np.diff(t)))
            for k in range(int(np.floor((min(t)-centers[0])/p)),int(np.ceil((max(t)-centers[0])/p))+1):
                c=centers[0]+k*p
                if abs(c-centers[0])<1 or abs(c-centers[1])<1:continue
                if c<min(t)+.5 or c>max(t)-.5:continue
                x=t-c;core=np.abs(x)<.09;wing=(np.abs(x)>.2)&(np.abs(x)<.45)
                ct=t[core];complete=bool(len(ct)>5 and ct.min()<c-.06 and ct.max()>c+.06 and np.max(np.diff(ct))<3*cad and core.sum()>.13/cad*.6 and wing.sum()>.5/cad*.5)
                depth=None
                if complete:
                    slope,base=np.polyfit(x[wing],f[wing],1);depth=float((1-np.median(f[core]/(base+slope*x[core])))*1000)
                predicted.append({'sector':sec,'cycle':k,'predicted_btjd':float(c),'core_count':int(core.sum()),'wing_count':int(wing.sum()),'core_complete':complete,'local_depth_ppt':depth,'source_sha256':sha})
        out.append({'integer_cycles_between_two_clean_events':n,'conditional_period_days':float(p),'additional_predictions_in_cached_sector_interiors':predicted})
    (B/tic/'lead-alias-checks.json').write_text(json.dumps({'scope':'Only neighboring integer aliases of two clean observed events. Predicted windows use nominal centers; no claim of conjunction geometry or all possible aliases. Sensitive null requires stable baseline as well as coverage.','cases':out},indent=2)+'\n',encoding='utf8')
    if tic=='94255849':
        t,f,_=data[64]; fig,axs=plt.subplots(1,2,figsize=(10,3))
        for ax,n in zip(axs,[56,58]):
            case=next(x for x in out if x['integer_cycles_between_two_clean_events']==n)
            c=next(x['predicted_btjd'] for x in case['additional_predictions_in_cached_sector_interiors'] if x['sector']==64)
            ok=np.abs(t-c)<.55; xx=t[ok]-c;yy=f[ok]/np.median(f[ok]);ax.plot(xx,yy,'.',ms=3);ax.axvspan(-.09,.09,color='pink',alpha=.3);ax.set_title(f'S64 n={n}, BTJD {c:.3f}');ax.set_xlabel('days from predicted dip');ax.set_ylabel('SAP/local median')
        fig.tight_layout();fig.savefig(B/tic/'lead-alias-nulls.png',dpi=140);plt.close(fig)
    print(tic,[(x['integer_cycles_between_two_clean_events'],round(x['conditional_period_days'],5),len(x['additional_predictions_in_cached_sector_interiors'])) for x in out])
