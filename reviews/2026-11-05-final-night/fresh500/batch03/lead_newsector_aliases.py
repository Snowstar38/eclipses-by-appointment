import json,numpy as np,hashlib
from pathlib import Path
from astropy.io import fits
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh500/batch03');D=b/'12878982';series=[]
for p,sec,pix in [(D/'helper-tesscut.fits',29,True),(D/'audit-s107.fits',107,True)]:
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);cube=np.array(a['FLUX']);n=cube.shape[1];yy,xx=np.indices((n,n));ap=(abs(xx-(n-1)/2)<=1)&(abs(yy-(n-1)/2)<=1);sky=(abs(xx-(n-1)/2)>1)|(abs(yy-(n-1)/2)>1);bg=np.nanmedian(cube[:,sky],axis=1);y=np.nansum(cube[:,ap]-bg[:,None],axis=1)
 ok=(q==0)&np.isfinite(t)&np.isfinite(y)&(y>0);series.append((sec,t[ok],y[ok],hashlib.sha256(p.read_bytes()).hexdigest()))
t0=2094.066305;end=4271.548735;dur=.36;tests=[]
for cy in range(1,int((end-t0)/5)+1):
 p=(end-t0)/cy;wins=[]
 for sec,t,y,sha in series:
  cad=np.median(np.diff(t))
  for n in range(int(np.ceil((t.min()-t0)/p)),int(np.floor((t.max()-t0)/p))+1):
   pred=t0+n*p;core=abs(t-pred)<dur*.35;left=(t>pred-dur*1.6)&(t<pred-dur*.75);right=(t>pred+dur*.75)&(t<pred+dur*1.6)
   if min(core.sum(),left.sum(),right.sum())<3:continue
   tc=t[core];cover=len(tc)*cad/(dur*.7)
   if cover<.75 or np.max(np.diff(tc))>max(cad*3,dur*.2):continue
   tl=np.median(t[left]);tr=np.median(t[right]);fl=np.median(y[left]);fr=np.median(y[right]);base=fl+(fr-fl)*(t-tl)/(tr-tl);z=y/base;noise=1.4826*np.median(abs(z[left|right]-np.median(z[left|right])))*1000;depth=(1-np.median(z[core]))*1000
   wins.append(dict(sector=sec,predicted_btjd=pred,depth_ppt=depth,noise_ppt=noise,null=bool(depth<max(4.5,noise*4/np.sqrt(core.sum()))),sha256=sha))
 tests.append(dict(cycles=cy,period_d=p,windows=wins,null_count=sum(w['null'] for w in wins)))
(D/'lead-newsector-aliases.json').write_text(json.dumps(tests,indent=2));print('survivors',[(x['cycles'],x['period_d'],len(x['windows'])) for x in tests if not x['null_count']])
