"""Raw and QLP alternative time series around hand-selected deciding windows."""
from pathlib import Path
import csv, json, hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
W={
 '259900992':[1339.9,3014.9,3028.4,3761.4,3874.95],
 '265066551':[1770.93,2000.43,2889.29,3604.24],
 '78053255':[1443.36,1486.01,2192.61],
 '166563438':[3054.44,3061.17,4053.24,4067.59,4107.72,4119.67],
 '306826020':[2999.87,3026.66,3053.94,3759.73],
 '389567330':[3668.85,3703.48],
 '147413927':[1546.413,1590.499,2317.923,3023.369,3750.813,3772.869,4081.434],
 '407622315':[1452.07,2047.4,3027.95,3874.91],
 '234302665':[3874.946,3926.404],
 '232632979':[2018.485,2029.467,2895.815,3623.531],
}
receipts={}
for tic,centers in W.items():
 bulk=json.loads((H/f'{tic}.json').read_text()); out=B/tic
 data=[]; hashes={}
 for rec in bulk['files']:
  near=[c for c in centers if abs(c-float(rec['windows'][0]['time']))<35 or True]
  if not near:continue
  p=Path(rec['path']);sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha==rec['sha256']
  hashes[str(p)]=sha
  with fits.open(p,memmap=False) as hd:
   assert str(int(hd[0].header['TICID']))==tic
   a=hd[1].data
   t=np.array(a['TIME'],float); sap=np.array(a['SAP_FLUX'],float)
   ksp=np.array(a['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in a.names else np.full(len(t),np.nan)
   x=np.array(a['SAP_X'],float) if 'SAP_X' in a.names else np.full(len(t),np.nan)
   y=np.array(a['SAP_Y'],float) if 'SAP_Y' in a.names else np.full(len(t),np.nan)
   q=np.array(a['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(sap)&(sap>0)&(q==0)
  data.append((int(rec['sector']),t[ok],sap[ok],ksp[ok],x[ok],y[ok]))
 info=[]
 for c in centers:
  match=[z for z in data if len(z[1]) and z[1].min()<c<z[1].max()]
  if not match: info.append({'center':c,'sector':None});continue
  s,t,f,k,x,y=min(match,key=lambda z:abs(np.median(z[1])-c))
  half=1.4;m=abs(t-c)<half;tt=t[m];ff=f[m];kk=k[m];xx=x[m];yy=y[m]
  if len(tt)<3:continue
  scale=lambda z:z/np.nanmedian(z)-1 if np.isfinite(z).sum()>3 else z*np.nan
  fs=scale(ff);ks=scale(kk)
  gap=float(np.max(np.diff(tt))) if len(tt)>1 else None
  info.append({'center':c,'sector':s,'n_q0':len(tt),'first':float(tt.min()),'last':float(tt.max()),'largest_gap_days':gap,'sap_core_median':float(np.nanmedian(fs[abs(tt-c)<.12])) if np.any(abs(tt-c)<.12) else None,'ksp_core_median':float(np.nanmedian(ks[abs(tt-c)<.12])) if np.any(abs(tt-c)<.12) else None,'x_range':float(np.nanmax(xx)-np.nanmin(xx)) if np.isfinite(xx).any() else None})
  fig,ax=plt.subplots(3,1,figsize=(9,6),sharex=True)
  ax[0].plot(tt-c,fs,'.',ms=2,label='SAP')
  ax[0].plot(tt-c,ks,'.',ms=2,label='KSPSAP')
  ax[0].legend(fontsize=8);ax[0].set_ylabel('relative flux')
  ax[1].plot(tt-c,xx,'.',ms=2);ax[1].set_ylabel('SAP X')
  ax[2].plot(tt-c,yy,'.',ms=2);ax[2].set_ylabel('SAP Y');ax[2].set_xlabel('BTJD minus selected time (d)')
  fig.suptitle(f'TIC {tic} S{s} selected {c:.3f} q0; same TESS photons')
  fig.tight_layout();fig.savefig(out/f'decide-{c:.3f}.png',dpi=120);plt.close(fig)
 receipts[tic]={'windows':info,'source_sha256':hashes}
(B/'deciding-windows.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf8')
