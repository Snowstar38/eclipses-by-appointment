from pathlib import Path
import json,numpy as np
from scipy.optimize import least_squares
from scipy.special import erf
R=Path(__file__).parent; rows=json.load(open(R/'pixel-results.json')); ns=json.load(open(R/'neighbour-results.json')); out=[]
for r in rows:
 if 'error'in r:continue
 z=np.load(R/r['tic']/('pixel_s%03d.npz'%r['sector']))['deficit']; yy,xx=np.mgrid[:11,:11];tx,ty=r['target_px']; mask=(abs(xx-tx)<3.5)&(abs(yy-ty)<3.5);X=xx[mask];Y=yy[mask];Z=z[mask];scale=max(abs(Z).max(),1); n=next(n for n in ns if n['tic']==r['tic'] and n['sector']==r['sector']); cs=[{'tic':int(r['tic']),'px':[tx,ty],'separation_arcsec':0}]+n['capable_neighbours']; fits=[]
 for c in cs:
  cx,cy=c['px']
  def model(a):
   amp,sx,sy,bg=a;return amp*(erf((X+.5-cx)/(2**.5*sx))-erf((X-.5-cx)/(2**.5*sx)))*(erf((Y+.5-cy)/(2**.5*sy))-erf((Y-.5-cy)/(2**.5*sy)))/4+bg
  fit=least_squares(lambda a:(model(a)-Z)/scale,[max(Z)*5,.7,.7,0],bounds=([0,.3,.3,-scale],[scale*200,2,2,scale]));fits.append({'tic':c['tic'],'separation_arcsec':c['separation_arcsec'],'sse':float(np.sum((model(fit.x)-Z)**2))})
 base=fits[0]['sse'];out.append({'tic':r['tic'],'sector':r['sector'],'target_sse':base,'neighbours':[{**v,'sse_ratio_to_target':v['sse']/base} for v in fits[1:]],'note':'Fixed source coordinate signed image Gaussian with free amplitude, widths and constant; ratios are descriptive, not calibrated likelihoods; source model and noise assumptions can fail.'})
json.dump(out,open(R/'fixed-source-comparison.json','w'),indent=2)
for o in out:
 ns=sorted(o['neighbours'],key=lambda v:v['separation_arcsec']);print(o['tic'],o['sector'],[(n['tic'],round(n['separation_arcsec'],1),round(n['sse_ratio_to_target'],2)) for n in ns[:3]])
