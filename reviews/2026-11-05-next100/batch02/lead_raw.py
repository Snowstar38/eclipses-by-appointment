"""Hash-verified Q011-Q020 raw SAP overview and screening-window inventory."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent; ROOT=B.parent
rows=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
for row in rows:
    tic=row['tic']; out=B/tic; out.mkdir(exist_ok=True)
    pkt=json.loads((ROOT/'source-packets'/tic/'sources.json').read_text(encoding='utf-8'))
    bulk=Path(pkt['bulk_result'])
    assert hashlib.sha256(bulk.read_bytes()).hexdigest()==pkt['bulk_result_sha256']
    det=json.loads(bulk.read_text(encoding='utf-8'))
    receipts={int(v['sector']):v for v in pkt['verified_files']}
    data=[]; inventory=[]
    for item in det['files']:
        if item.get('status')!='ok': continue
        sec=int(item['sector']); rec=receipts[sec]; fp=Path(rec['path'])
        assert hashlib.sha256(fp.read_bytes()).hexdigest()==rec['sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data
            t=np.asarray(a['TIME'],float); f=np.asarray(a['SAP_FLUX'],float)
            q=np.asarray(a['QUALITY'],int)
        v=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0); t=t[v]; f=f[v]
        if not len(t):continue
        med=np.median(f); y=f/med
        dt=np.diff(t); cadence=float(np.median(dt)) if len(dt) else None
        windows=[dict(time=float(w['time']),duration=float(w['duration']),kind=w['kind'],flag=bool(w['flag']),depth=float(w['depth']),contrast=float(w['contrast'])) for w in item.get('windows',[]) if w.get('flag')]
        inventory.append(dict(sector=sec,file=str(fp),sha256=rec['sha256'],time_start=float(t.min()),time_end=float(t.max()),cadence_days=cadence,quality0_positive=int(len(t)),median_raw_sap=float(med),gaps_over_0p2_days=[[float(t[i]),float(t[i+1])] for i in np.where(dt>.2)[0]],flagged_windows=windows))
        data.append((sec,t,y,windows))
    n=len(data); fig,axs=plt.subplots(n,1,figsize=(14,max(3,2.2*n)),squeeze=False)
    for ax,(sec,t,y,windows) in zip(axs[:,0],data):
        ax.plot(t,y,'k.',ms=1,rasterized=True)
        for w in windows:
            ax.axvline(w['time'],color=('C3' if w['kind']=='dip' else 'C0'),lw=.8,alpha=.7)
        lo,hi=np.nanquantile(y,[.005,.995]); pad=max((hi-lo)*.1,.001)
        ax.set_ylim(lo-pad,hi+pad); ax.set_ylabel(f'S{sec}\nSAP/med'); ax.grid(alpha=.2)
    if n: axs[-1,0].set_xlabel('BTJD')
    fig.suptitle(f"{row['sample_id']} TIC {tic}: raw SAP (red flagged dips; blue brightenings)")
    fig.tight_layout(); fig.savefig(out/'lead-raw-overview.png',dpi=130); plt.close(fig)
    (out/'lead-inventory.json').write_text(json.dumps(dict(sample_id=row['sample_id'],tic=tic,bulk_result=str(bulk),bulk_sha256=pkt['bulk_result_sha256'],sectors=inventory),indent=2)+'\n',encoding='utf-8')
    print(row['sample_id'],tic,'sectors',n,'flags',sum(len(x['flagged_windows']) for x in inventory),flush=True)
