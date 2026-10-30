import json,pathlib,numpy as np
from scipy.optimize import least_squares
r=pathlib.Path(__file__).parent;pix=json.load(open(r/'pixel-results.json'));nbs=json.load(open(r/'neighbour-results.json'));out=[]
for x in pix:
 if x.get('error'):continue
 tic=x['tic'];sec=x['sector']; n=next(a for a in nbs if a['tic']==tic and a['sector']==sec);arr=np.load(r/tic/f'pixel_s{sec:03d}.npz');O=arr['out'];D=arr['deficit'];yy,xx=np.mgrid[:11,:11];tx,ty=x['target_px'];mask=(abs(xx-tx)<3)&(abs(yy-ty)<3);base=lambda cx,cy,s:np.exp(-((xx-cx)**2+(yy-cy)**2)/(2*s*s))
 # Gaussian width from target-centered out-image fit, blended field may bias it.
 def fun(a):return (a[0]*base(tx,ty,a[1])+a[2]-O)[mask]
 try:
  fit=least_squares(fun,[max(O.max()-np.median(O),1),.9,np.median(O)],bounds=([0,.5,-np.inf],[np.inf,2,np.inf]));sigma=float(fit.x[1]);models=[]
  for label,px,sep in [('target',[tx,ty],0)]+[(str(z['tic']),z['px'],z['separation_arcsec']) for z in n['capable_neighbours'] if z['separation_arcsec']<30]:
   g=base(px[0],px[1],sigma);A=np.column_stack([g[mask],np.ones(mask.sum())]);b=D[mask];c=np.linalg.lstsq(A,b,rcond=None)[0];res=b-A@c;models.append(dict(source=label,separation_arcsec=sep,amplitude=float(c[0]),rss=float(res@res),rms=float(np.sqrt(np.mean(res**2)))))
  out.append(dict(tic=tic,sector=sec,sigma_px=sigma,models=models,n_pixels=int(mask.sum()),note='Circular Gaussian approximate fixed-position PSF with constant background; width fitted from blended out-image; same noise/region across candidates. RSS is relative shape evidence, not calibrated likelihood or significance. Close models overlap strongly and TESS PSF is not Gaussian.'))
 except Exception as e:out.append(dict(tic=tic,sector=sec,error=repr(e)))
json.dump(out,open(r/'source-model-comparison.json','w'),indent=2);print([(a['tic'],a['sector'],[(m['source'],round(m['rss']/a['models'][0]['rss'],2)) for m in a.get('models',[])]) for a in out])
