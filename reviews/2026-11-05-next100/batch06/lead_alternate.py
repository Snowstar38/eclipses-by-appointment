"""Compare raw and pipeline alternate reductions near deciding windows."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
KEY={'373314632':[4010.62,4029.15], '409938734':[3874.87,4197.37],
     '325338671':[3874.89,4147.03,4197.34], '158235054':[3874.82,4197.27],
     '346727714':[3874.87,4145.07], '469821735':[3874.87,4170.13],
     '278271047':[1614.05,3874.88], '161168392':[1340.33,4133.86,4197.07],
     '108655701':[1496.51,3711.84], '399951126':[1693.11,3522.13,3542.82]}
for q in csv.DictReader((B/'queue.csv').open(encoding='utf8')):
    tic=q['tic']
    if tic not in KEY: continue
    c=json.loads((B/tic/'lead-context.json').read_text())
    out=[]; fig,axs=plt.subplots(len(KEY[tic]),1,figsize=(10,2.8*len(KEY[tic])),squeeze=False)
    for ax,center in zip(axs[:,0],KEY[tic]):
        s=next(s for s in c['sectors'] if s['time_start_btjd']<center<s['time_end_btjd'])
        p=Path(s['source_path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['source_sha256']
        with fits.open(p,memmap=False) as h:
            a=h[1].data; names=h[1].columns.names
            t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);qual=np.asarray(a['QUALITY'],int)
            mask=np.isfinite(t)&np.isfinite(f)&(f>0)&(qual==0)&(np.abs(t-center)<1.5)
            tt=t[mask]; rec={'sector':s['sector'],'screen_center_btjd':center,'columns':{}}
            for name in ('SAP_FLUX','DET_FLUX','SYS_RM_FLUX','KSPSAP_FLUX'):
                if name not in names:continue
                v=np.asarray(a[name],float)[mask]
                good=np.isfinite(v)&(v>0)
                if good.sum()<10:continue
                base=np.median(v[good]); y=v[good]/base
                ax.plot(tt[good]-center,y,'.',ms=2,alpha=.45,label=name)
                rec['columns'][name]={'good_points':int(good.sum()),'median_flux':float(base),
                    'local_min_fraction':float(np.min(y)),'local_max_fraction':float(np.max(y))}
            ax.axvline(0,color='black',lw=.5);ax.set_title(f"{q['sample_id']} S{s['sector']} {center:.3f}")
            ax.set_ylabel('flux / local median');ax.legend(fontsize=7,ncol=4)
            out.append(rec)
    fig.tight_layout();fig.savefig(B/tic/'lead-alternate.png',dpi=130);plt.close(fig)
    (B/tic/'lead-alternate.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print(q['sample_id'],tic)
