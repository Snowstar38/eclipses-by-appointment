import pathlib,json,csv,numpy as np
from astropy.io import fits
D=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-a\full-vet'); events=list(csv.DictReader((D.parent/'events.csv').open()))
def depth(t,f,q,c):
 x=t-c; ok=np.isfinite(t)&np.isfinite(f)&(q==0); oot=ok&(abs(x)>.16)&(abs(x)<.5); core=ok&(abs(x)<.04)
 if sum(oot)<8 or sum(core)<2:return None
 v=np.polyfit(x[oot],f[oot],1); pred=np.polyval(v,x[core]); z=1000*(1-np.median(f[core]/pred)); return (round(float(z),2),int(sum(core)))
for p in D.glob('*_indep.fits'):
 tic=p.name.split('_')[0]
 with fits.open(p) as h:
  sec=h[0].header['SECTOR']; a=h[1].data; t=np.array(a['TIME']);q=np.array(a['QUALITY']);f=np.array(a['PDCSAP_FLUX']); fs=np.array(a['SAP_FLUX'])
 qpath=D.parent/'data'/f'{tic}_s{sec:03}.fits'
 with fits.open(qpath) as h:
  a=h[1].data; qt=np.array(a['TIME']);qf=np.array(a['SAP_FLUX']);qq=np.array(a['QUALITY'])
 print(tic,'sector',sec)
 for e in events:
  if e['tic']==tic and int(e['sector'])==sec:
   c=float(e['scan_mid_btjd'] or e['pred_btjd']);print(round(c,4),'PDCSAP',depth(t,f,q,c),'SPOC_SAP',depth(t,fs,q,c),'QLP_SAP',depth(qt,qf,qq,c))
