"""Actual raw SAP local shapes for four independent sky positions near BTJD 3875."""
from pathlib import Path
import csv,json,hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
out=[];fig,axs=plt.subplots(4,1,figsize=(10,9),sharex=True)
for ax,sid in zip(axs,['F021','F024','F026','F029']):
    row=next(r for r in csv.DictReader((B/'queue.csv').open(encoding='utf8')) if r['sample_id']==sid)
    pack=json.loads((B.parent/'source-packets'/row['tic']/'sources.json').read_text(encoding='utf8'))
    r=next(r for r in pack['verified_files'] if int(r['sector'])==94)
    p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
    with fits.open(p,memmap=False) as h:
        a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
    good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-3875)<4);t=t[good];f=f[good]
    base=np.median(f[(t<3872)|(t>3878)])
    ax.plot(t,f/base,'.',ms=1);ax.set_ylabel(sid)
    gaps=[[float(t[i]),float(t[i+1])] for i in np.where(np.diff(t)>.1)[0]]
    out.append(dict(sample_id=sid,tic=row['tic'],sector=94,source=r,points=len(t),first=float(t.min()),last=float(t.max()),gaps_over_0p1_days=gaps))
axs[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/'lead-common3875.png',dpi=140);plt.close(fig)
(B/'lead-common3875.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
