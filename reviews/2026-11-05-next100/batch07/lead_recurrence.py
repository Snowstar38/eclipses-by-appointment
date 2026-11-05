"""Measured-clock raw SAP coverage and narrow dip search near Q061/Q068 cycles."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
EPH={'295176393':(2365.97185,27.25454039,.06,.05),'341419787':(1493.43643,21.07162267,.12,.5)}
for tic,(t0,p,width,search) in EPH.items():
    ctx=json.loads((B/tic/'lead-context.json').read_text());out=[]
    for s in ctx['sectors']:
        fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[m];f=f[m]
        for n in range(int(np.floor((t.min()-t0)/p))-1,int(np.ceil((t.max()-t0)/p))+2):
            c=t0+n*p
            if not t.min()-width<c<t.max()+width:continue
            core=np.abs(t-c)<width/2;baseline=(np.abs(t-c)>width*1.5)&(np.abs(t-c)<width*5)
            expected=int(round(width/s['cadence_days']))+1
            near=[]
            for cc in np.arange(c-search,c+search+width/4,width/4):
                co=np.abs(t-cc)<width/2;ba=(np.abs(t-cc)>width*1.5)&(np.abs(t-cc)<width*5)
                if co.sum()<expected*.65 or ba.sum()<expected*.8:continue
                near.append((float(1000*(1-np.median(f[co])/np.median(f[ba]))),float(cc),int(co.sum())))
            best=max(near) if near else None
            out.append(dict(sector=s['sector'],cycle=n,predicted_btjd=float(c),core_count=int(core.sum()),expected=expected,
                core_first=float(t[core].min()) if core.any() else None,core_last=float(t[core].max()) if core.any() else None,
                baseline_count=int(baseline.sum()),core_depth_ppt=float(1000*(1-np.median(f[core])/np.median(f[baseline]))) if core.sum()>2 and baseline.sum()>6 else None,
                best_nearby_depth_ppt=best[0] if best else None,best_nearby_center_btjd=best[1] if best else None,best_nearby_core_count=best[2] if best else None))
    (B/tic/'lead-recurrence.json').write_text(json.dumps(dict(measured_epoch_btjd=t0,measured_period_days=p,core_width_days=width,search_halfwidth_days=search,windows=out),indent=2)+'\n',encoding='utf8')
    print(tic,[(x['sector'],x['cycle'],round(x['predicted_btjd'],3),x['core_count'],x['expected'],round(x['core_depth_ppt'],2) if x['core_depth_ppt'] is not None else None,round(x['best_nearby_depth_ppt'],2) if x['best_nearby_depth_ppt'] is not None else None,round(x['best_nearby_center_btjd']-x['predicted_btjd'],3) if x['best_nearby_center_btjd'] is not None else None) for x in out])
