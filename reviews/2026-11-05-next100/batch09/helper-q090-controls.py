from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(r'[local-path-redacted]'); edges=np.arange(2420,2447,.25); target=D/'243276811_s041.fits'
def series(p):
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY']);hdr=h[0].header
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g]; f=f/np.median(f)-1
 b=np.array([np.median(f[(t>=a)&(t<a+.25)]) if np.sum((t>=a)&(t<a+.25))>=3 else np.nan for a in edges]);return b,hdr
base,bh=series(target); all=[]
for p in list(D.glob('*_s041.fits'))[:160]:
 try:
  b,h=series(p);g=np.isfinite(b)&np.isfinite(base)
  if g.sum()<50:continue
  corr=np.corrcoef(b[g],base[g])[0,1]; all.append((corr,p,b,h))
 except Exception:pass
all.sort(key=lambda x:-x[0]); selected=all[:5];out=[]
fig,ax=plt.subplots(figsize=(11,5));ax.plot(edges,base*1000,label='Q090',lw=2)
for corr,p,b,h in selected:
 ax.plot(edges,b*1000,label=f'{p.stem} r={corr:.2f}',alpha=.7);out.append(dict(file=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),correlation=float(corr),camera=h.get('CAMERA'),ccd=h.get('CCD')))
ax.legend(fontsize=8);ax.set(xlabel='BTJD',ylabel='SAP / median - 1 (ppt)',title=f'S41 unrelated stars: top matches from {len(all)} examined');fig.tight_layout();fig.savefig('helper-q090-controls.png',dpi=140)
Path('helper-q090-controls.json').write_text(json.dumps({'target_camera':bh.get('CAMERA'),'target_ccd':bh.get('CCD'),'examined':len(all),'top':out},indent=2));print(json.dumps(out,indent=2))
