import json,numpy as np
from pathlib import Path
from astropy.io import fits
from scipy.optimize import least_squares
from scipy.special import erf
R=Path(__file__).parent;rows=json.load(open(R/'pixel-results.json'));dl=json.load(open(R/'tesscut-downloads.json')); ns=json.load(open(R/'neighbour-results.json'));out=[]
for row in rows:
 if row['tic'] not in ('4646090','443106429') or not row['events']:continue
 d=next(x for x in dl if x['tic']==row['tic'] and x['sector']==row['sector']);p=R/row['tic']/d['members'][0]
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);F=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY']);ok=np.isfinite(t)&(q==0)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1);t=t[ok];F=F[ok];F-=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:48],axis=1)[:,None,None]
 tx,ty=row['target_px']; n=next(x for x in ns if x['tic']==row['tic'] and x['sector']==row['sector']);near=min(n['capable_neighbours'],key=lambda c:c['separation_arcsec']);yy,xx=np.mgrid[:11,:11];mask=(abs(xx-tx)<3.5)&(abs(yy-ty)<3.5);X=xx[mask];Y=yy[mask]
 for e in row['events']:
  x=t-e['tc'];D=e['duration_d'];Z=((np.median(F[(x<-.75*D)&(x>-1.75*D)],axis=0)+np.median(F[(x>.75*D)&(x<1.75*D)],axis=0))/2-np.median(F[abs(x)<.3*D],axis=0))[mask];scale=max(abs(Z).max(),1);vals=[]
  for cx,cy in ([tx,ty],near['px']):
   def model(a):return a[0]*(erf((X+.5-cx)/(2**.5*a[1]))-erf((X-.5-cx)/(2**.5*a[1])))*(erf((Y+.5-cy)/(2**.5*a[2]))-erf((Y-.5-cy)/(2**.5*a[2])))/4+a[3]
   fit=least_squares(lambda a:(model(a)-Z)/scale,[max(Z)*5,.7,.7,0],bounds=([0,.3,.3,-scale],[scale*200,2,2,scale]));vals.append(float(sum((model(fit.x)-Z)**2)))
  out.append(dict(tic=row['tic'],sector=row['sector'],tc=e['tc'],nearest_tic=near['tic'],neighbour_to_target_sse=vals[1]/vals[0],note='One-event signed difference image, fixed-position Gaussian SSE ratio descriptive only; noise, PRF mismatch and background can dominate.'))
json.dump(out,open(R/'per-event-source-comparison.json','w'),indent=2);print(out)
