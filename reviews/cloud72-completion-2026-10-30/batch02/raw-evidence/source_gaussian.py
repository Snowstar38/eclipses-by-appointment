from pathlib import Path
import json,numpy as np
from scipy.optimize import least_squares
from scipy.special import erf
R=Path(__file__).parent;rows=json.load(open(R/'pixel-results.json'));ns=json.load(open(R/'neighbour-results.json'));out=[]
for r in rows:
 if 'error'in r:continue
 z=np.load(R/r['tic']/('pixel_s%03d.npz'%r['sector']))['deficit'];yy,xx=np.mgrid[:11,:11];tx,ty=r['target_px'];mask=(abs(xx-tx)<3.5)&(abs(yy-ty)<3.5);X=xx[mask];Y=yy[mask];Z=z[mask];scale=max(np.max(abs(Z)),1)
 def model(a):
  amp,cx,cy,sx,sy,bg=a;return amp*(erf((X+.5-cx)/(2**.5*sx))-erf((X-.5-cx)/(2**.5*sx)))*(erf((Y+.5-cy)/(2**.5*sy))-erf((Y-.5-cy)/(2**.5*sy)))/4+bg
 a0=[max(Z)*5,tx,ty,.7,.7,0];lo=[0,tx-2,ty-2,.3,.3,-scale];hi=[scale*200,tx+2,ty+2,2,2,scale]
 fit=least_squares(lambda a:(model(a)-Z)/scale,a0,bounds=(lo,hi));a=fit.x;res=model(a)-Z;J=fit.jac;cov=np.linalg.pinv(J.T@J)*sum((res/scale)**2)/max(1,len(Z)-6);se=np.sqrt(np.maximum(0,np.diag(cov)));n=next(n for n in ns if n['tic']==r['tic'] and n['sector']==r['sector']);cand=[]
 for s in [{'tic':int(r['tic']),'px':[tx,ty],'separation_arcsec':0}]+n['capable_neighbours']:
  cx,cy=s['px'];cand.append(dict(tic=s['tic'],separation_arcsec=s['separation_arcsec'],distance_to_gaussian_arcsec=float(np.hypot(cx-a[1],cy-a[2])*21)))
 out.append(dict(tic=r['tic'],sector=r['sector'],gaussian_xy=a[1:3].tolist(),formal_xy_error_arcsec=(se[1:3]*21).tolist(),target_offset_arcsec=float(np.hypot(a[1]-tx,a[2]-ty)*21),sigma_xy=a[3:5].tolist(),residual_rms=float(np.std(res)),candidates=cand,note='Pixel-integrated axis-aligned Gaussian plus constant on signed stack; iid residual formal errors exclude PRF mismatch/systematics; diagnostic only, not calibrated localization confidence.'))
json.dump(out,open(R/'gaussian-source-diagnostic.json','w'),indent=2);print([(a['tic'],a['sector'],round(a['target_offset_arcsec'],2),[round(b,2) for b in a['formal_xy_error_arcsec']]) for a in out])
