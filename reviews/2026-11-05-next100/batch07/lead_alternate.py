"""Compare raw SAP with same-photon pipeline reductions at decisive windows."""
import csv,hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
KEY={'295176393':[2365.973,3101.843,3837.719,4083.012],
     '219377638':[1677.468,3874.869,4002.515],
     '25194865':[1473.344,1661.386,4010.650],
     '339768963':[3759.628,3874.896,3954.714],
     '312243976':[1701.863,2816.930,3540.183],
     '341403511':[3869.583,3874.874,4113.264],
     '51223058':[2778.216,2799.182,3526.963],
     '341419787':[1493.429,1514.492,2256.561],
     '63121270':[1694.489,1704.406,2422.187],
     '401575160':[2047.174,3867.581,4112.556]}
for q in csv.DictReader((B/'queue.csv').open(encoding='utf8')):
    tic=q['tic'];c=json.loads((B/tic/'lead-context.json').read_text());out=[]
    fig,axs=plt.subplots(len(KEY[tic]),1,figsize=(10,2.8*len(KEY[tic])),squeeze=False)
    for ax,center in zip(axs[:,0],KEY[tic]):
        s=next(s for s in c['sectors'] if s['time_start_btjd']<center<s['time_end_btjd'])
        p=Path(s['source_path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['source_sha256']
        with fits.open(p,memmap=False) as h:
            a=h[1].data;names=h[1].columns.names
            t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);qual=np.asarray(a['QUALITY'],int)
            m=np.isfinite(t)&np.isfinite(f)&(f>0)&(qual==0)&(np.abs(t-center)<1.5);tt=t[m]
            rec={'sector':s['sector'],'screen_center_btjd':center,'columns':{}}
            for name in ('SAP_FLUX','DET_FLUX','SYS_RM_FLUX','KSPSAP_FLUX'):
                if name not in names:continue
                v=np.asarray(a[name],float)[m];good=np.isfinite(v)&(v>0)
                if good.sum()<10:continue
                base=np.median(v[good]);y=v[good]/base
                ax.plot(tt[good]-center,y,'.',ms=2,alpha=.4,label=name)
                rec['columns'][name]={'good_points':int(good.sum()),'median_flux':float(base),'local_min_fraction':float(np.min(y)),'local_max_fraction':float(np.max(y))}
            ax.axvline(0,color='black',lw=.5);ax.set_title(f"{q['sample_id']} S{s['sector']} {center:.3f}");ax.set_ylabel('flux / local median');ax.legend(fontsize=7,ncol=4);out.append(rec)
    fig.tight_layout();fig.savefig(B/tic/'lead-alternate.png',dpi=130);plt.close(fig)
    (B/tic/'lead-alternate.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print(q['sample_id'],tic)
