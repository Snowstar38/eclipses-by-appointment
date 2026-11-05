"""Replot S94 and S104 synchronous features using verified FITS files."""
import csv,hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
rows=list(csv.DictReader((B/'queue.csv').open(encoding='utf8')))
out=[]
for sec,center,span in ((94,3874.87,1.5),(104,4197.3,1.5)):
    sectors=[]
    for q in rows:
        c=json.loads((B/q['tic']/'lead-context.json').read_text())
        s=next((s for s in c['sectors'] if s['sector']==sec),None)
        if s is None:continue
        f=[f for f in s['flags'] if f['kind']=='dip' and abs(f['screen_center_btjd']-center)<.3]
        if not f:continue
        sectors.append((q,s,f[0]))
    fig,axs=plt.subplots(len(sectors),1,figsize=(10,1.8*len(sectors)),sharex=True,squeeze=False)
    for ax,(q,s,flag) in zip(axs[:,0],sectors):
        p=Path(s['source_path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['source_sha256']
        with fits.open(p,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);qual=np.asarray(a['QUALITY'],int)
            cam=h[0].header['CAMERA'];ccd=h[0].header['CCD']
        m=np.isfinite(t)&np.isfinite(y)&(y>0)&(qual==0)&(abs(t-center)<span)
        tt=t[m];yy=y[m]
        x=tt-center; side=(abs(x)>.9)&(abs(x)<span)
        norm=yy/np.median(yy[side]) if side.sum()>5 else yy/np.median(yy)
        ax.plot(x,norm,'.',ms=2,color='black');ax.axvline(flag['screen_center_btjd']-center,color='red',lw=.6)
        for a,b in s['gaps_over_3cadences']:
            if b-a>.1 and a<center+span and b>center-span:
                ax.axvspan(a-center,b-center,color='orange',alpha=.15)
        ax.set_ylabel(f"{q['sample_id']} C{cam}/{ccd}",fontsize=9)
        out.append(dict(sample_id=q['sample_id'],tic=q['tic'],sector=sec,camera=cam,ccd=ccd,
                        screen_center_btjd=flag['screen_center_btjd'],source_sha256=s['source_sha256'],
                        actual_points=int(m.sum()),gap_intervals_btjd=[g for g in s['gaps_over_3cadences'] if g[1]-g[0]>.1 and g[0]<center+span and g[1]>center-span]))
    axs[-1,0].set_xlabel(f'BTJD minus {center:.2f}');fig.tight_layout()
    fig.savefig(B/f'lead-common-s{sec:03d}.png',dpi=140);plt.close(fig)
(B/'lead-common-events.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(len(out),'synchronized windows')
