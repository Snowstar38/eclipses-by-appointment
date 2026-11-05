"""Quantify nearest raw-SAP data gap and step around retained screening windows."""
import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;out=[]
for r in csv.DictReader((B/'queue.csv').open()):
    m=json.loads((B/r['tic']/'lead-numeric.json').read_text())
    for sector in set(e['sector'] for e in m['events']):
        s=next(s for s in m['sources'] if s['sector']==sector);p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
        with fits.open(p,memmap=False) as h:
            d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];cad=float(np.median(np.diff(t)))
        for e in [e for e in m['events'] if e['sector']==sector]:
            seed=e['screen_btjd'];i=np.argmin(np.abs(.5*(t[:-1]+t[1:])-seed));gap=[float(t[i]),float(t[i+1]),float(t[i+1]-t[i])]
            # Most consequential gap within three days of seed, if one exists.
            cand=np.where((np.abs(.5*(t[:-1]+t[1:])-seed)<3)&(np.diff(t)>3*cad))[0]
            if len(cand):
                j=max(cand,key=lambda x:np.diff(t)[x]);gap=[float(t[j]),float(t[j+1]),float(t[j+1]-t[j])]
            pre=(t>gap[0]-.25)&(t<gap[0]);post=(t>=gap[1])&(t<gap[1]+.25)
            step=1000*(np.median(f[post])/np.median(f[pre])-1) if sum(pre)>2 and sum(post)>2 else None
            out.append(dict(sample_id=r['sample_id'],tic=r['tic'],sector=sector,screen_btjd=seed,gap_start_btjd=gap[0],gap_end_btjd=gap[1],gap_days=gap[2],gap_mid_minus_screen_days=.5*(gap[0]+gap[1])-seed,post_minus_pre_ppt=float(step) if step is not None else None,cadence_days=cad,source_sha256=s['sha256']))
(B/'lead-gap-evidence.json').write_text(json.dumps(out,indent=2)+'\n')
for x in out:print(x['sample_id'],x['sector'],round(x['screen_btjd'],2),round(x['gap_mid_minus_screen_days'],2),round(x['gap_days'],2),round(x['post_minus_pre_ppt'],1) if x['post_minus_pre_ppt'] is not None else None)
