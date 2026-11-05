import json,csv,numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent; Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}; n=json.loads((B.parent/'shared-catalogues/gaia-neighbors.json').read_text())['targets']; out=[]
for tic,sec,tm,half,edge,outer in [('235985439',19,1832.679,.07,.25,.55),('235985439',73,3292.676,.07,.25,.55),('325817130',12,1635.702,.3,1,1.5),('325817130',100,4079.325,.3,1,1.5)]:
 p=B/(f'helper-{tic}-s{sec}-tesscut.fits' if (B/f'helper-{tic}-s{sec}-tesscut.fits').exists() else f'helper-{tic}-tesscut.fits'); r=Q[tic]
 with fits.open(p,memmap=False) as h:
  t=np.array(h[1].data['TIME'],float);f=np.array(h[1].data['FLUX'],float);q=np.array(h[1].data['QUALITY']);w=WCS(h[2].header)
 good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2)); t=t[good];f=f[good];x=t-tm; bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);f-=bg[:,None,None];core=abs(x)<half;pre=(x<-edge)&(x>-outer);post=(x>edge)&(x<outer);base=.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0));dif=base-np.median(f[core],axis=0)
 rows=[]
 for z in n[r['sample_id']]:
  if not z['phot_g_mean_mag']:continue
  ratio=10**(-.4*(float(z['phot_g_mean_mag'])-float(r['gaia_G'])));px,py=map(float,w.all_world2pix(float(z['ra']),float(z['dec']),0))
  if ratio<.02 or not(-.5<=px<10.5 and -.5<=py<10.5):continue
  ix,iy=int(round(px)),int(round(py));b=base[iy,ix];d=dif[iy,ix];rows.append(dict(id=z['source_id'],xy=[px,py],ratio=ratio,pixel=[ix,iy],base=float(b),difference=float(d),fraction=float(d/b) if b>0 else None))
 rec=dict(tic=tic,sector=sec,counts=[int(core.sum()),int(pre.sum()),int(post.sum())],sources=rows);out.append(rec);
(B/'helper-final-local.json').write_text(json.dumps(out,indent=2))

