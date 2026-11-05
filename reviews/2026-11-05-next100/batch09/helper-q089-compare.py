from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(r'[local-path-redacted]')
def read(p):
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY']);names=d.names; k=np.array(d['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in names else np.full(len(t),np.nan);head=h[0].header
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);return t[g],f[g],k[g],head
out={};fig,ax=plt.subplots(2,1,figsize=(12,8))
for j,(sec,start,end) in enumerate([(67,3143.5,3149.5),(39,2378,2383)]):
 edges=np.arange(start,end,.1)
 def bins(t,f):
  return np.array([np.median(f[(t>=x)&(t<x+.1)]) if np.sum((t>=x)&(t<x+.1)) else np.nan for x in edges])
 p=D/f'382040915_s{sec:03d}.fits';t,f,k,h=read(p); f=f/np.median(f)-1;b=bins(t,f);ax[j].plot(edges,b*1000,label='Q089',lw=2)
 if np.isfinite(k).sum()>10:ax[j].plot(edges,bins(t,k/np.nanmedian(k)-1)*1000,label='Q089 KSPSAP',lw=1)
 rows=[]
 for p2 in list(D.glob(f'*_s{sec:03d}.fits'))[:250]:
  if p2 == p: continue
  try:
   t2,f2,k2,h2=read(p2);b2=bins(t2,f2/np.median(f2)-1);good=np.isfinite(b)&np.isfinite(b2)
   if good.sum()<30:continue
   cor=np.corrcoef(b[good],b2[good])[0,1];rows.append((cor,p2,b2,h2))
  except:pass
 rows.sort(key=lambda x:-x[0]); select=rows[:3]
 if sec==39:
  p2=D/'74352282_s039.fits';t2,f2,k2,h2=read(p2);b2=bins(t2,f2/np.median(f2)-1);g=np.isfinite(b)&np.isfinite(b2);select.append((np.corrcoef(b[g],b2[g])[0,1],p2,b2,h2))
 out[sec]=dict(source_hash=hashlib.sha256(p.read_bytes()).hexdigest(),target_camera=h.get('CAMERA'),target_ccd=h.get('CCD'),good_times=[float(x) for x in t[(t>start)&(t<end)]],comparisons=[])
 for cor,p2,b2,h2 in select:
  ax[j].plot(edges,b2*1000,label=f'{p2.stem} r={cor:.2f}');out[sec]['comparisons'].append(dict(path=str(p2),sha256=hashlib.sha256(p2.read_bytes()).hexdigest(),correlation=float(cor),camera=h2.get('CAMERA'),ccd=h2.get('CCD')))
 ax[j].legend(fontsize=8);ax[j].set_title(f'S{sec}');ax[j].set_ylabel('SAP ppt');ax[j].set_xlabel('BTJD')
fig.tight_layout();fig.savefig('helper-q089-compare.png',dpi=140);Path('helper-q089-compare.json').write_text(json.dumps(out,indent=2));print(json.dumps({x:{k:v for k,v in d.items() if k!='good_times'} for x,d in out.items()},indent=2))

