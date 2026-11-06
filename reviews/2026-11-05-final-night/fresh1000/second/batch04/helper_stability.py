import json,numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
from pathlib import Path
for tic,c,dur in [('469894984',3566.0527847072594,.287617),('248308520',2818.4607334418615,.23)]:
 d=Path(tic);l=json.loads((d/'helper-localization.json').read_text());n=json.loads((d/'helper-neighbors.json').read_text());
 with fits.open(d/'helper-tesscut.fits') as h:a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);cube=np.array(a['FLUX'])
 yy,xx=np.indices(cube.shape[1:]);out=[]
 for corewidth,side0,side1 in [(.2,.75,2),(.3,.75,2),(.25,1,2.5),(.25,.6,1.5),(.35,.8,2)]:
  g=(q==0)&np.isfinite(t);core=g&(abs(t-c)<dur*corewidth);side=g&(abs(t-c)>dur*side0)&(abs(t-c)<dur*side1);z=np.nanmedian(cube[side],axis=0)-np.nanmedian(cube[core],axis=0)
  def fn(v):return (v[0]*np.exp(-((xx-v[1])**2+(yy-v[2])**2)/(2*v[3]**2))+v[4]-z).ravel()
  iy,ix=np.unravel_index(np.argmax(z),z.shape);v=least_squares(fn,[z.max()-np.median(z),ix,iy,1,np.median(z)],bounds=([0,0,0,.3,-np.inf],[np.inf,6,6,3,np.inf])).x
  candidate=next(a for a in n['neighbors'] if a['source_id']==('2197843380808747904' if tic=='469894984' else '4226656532648133248'));out.append(dict(core_fraction=corewidth,side=[side0,side1],n=[int(core.sum()),int(side.sum())],xy=v[1:3].tolist(),target_distance=float(np.linalg.norm(v[1:3]-l['target_xy'])),neighbor_distance=float(np.linalg.norm(v[1:3]-candidate['pixel_xy']))))
 (d/'helper-window-stability.json').write_text(json.dumps(out,indent=2));print(tic,out)
