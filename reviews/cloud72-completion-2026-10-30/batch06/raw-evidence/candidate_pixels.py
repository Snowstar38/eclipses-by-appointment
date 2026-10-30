from pathlib import Path
import json,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
R=Path(__file__).parent;T=json.load(open(R.parent/'targets-selected.json'));recs={x['tic']:x for x in json.load(open(R/'search-receipts.json'))};DL=json.load(open(R/'tesscut-downloads.json'));out=[]
for d in DL:
 tic=d['tic'];sec=d['sector'];s=recs[tic]['P'];p=R/tic/d['members'][0];res={'tic':tic,'sector':sec,'events':[],'candidate_only':True}
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME']);F=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header);tx,ty=w.all_world2pix(T[tic]['ra'],T[tic]['dec'],0);res['target_px']=[float(tx),float(ty)]
 m=np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)&(q==0);t=t[m];F=F[m];F-=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:30],axis=1)[:,None,None];ds=[];os=[]
 ns=np.arange(np.ceil((t.min()-s['t0'])/s['P']),np.floor((t.max()-s['t0'])/s['P'])+1)
 for n in ns:
  tc=s['t0']+n*s['P'];dur=s['dur'];x=t-tc;i=abs(x)<dur*.3;pre=(x<-.75*dur)&(x> -1.75*dur);post=(x>.75*dur)&(x<1.75*dur)
  if min(i.sum(),pre.sum(),post.sum())<3:continue
  O=(np.median(F[pre],axis=0)+np.median(F[post],axis=0))/2;Z=O-np.median(F[i],axis=0);ds.append(Z);os.append(O);res['events'].append({'nominal_tc':tc,'duration_d':dur,'n_in':int(i.sum()),'n_pre':int(pre.sum()),'n_post':int(post.sum())})
 if not ds:res['error']='No two-sided coverage at original nominal event';out.append(res);continue
 O=np.mean(os,axis=0);Z=np.mean(ds,axis=0);ix=int(round(float(tx)));iy=int(round(float(ty)));dep=float(Z[iy-1:iy+2,ix-1:ix+2].sum()/O[iy-1:iy+2,ix-1:ix+2].sum());res['depth_3x3']=dep;res['note']='Candidate-only signed difference at original search phase; eclipse not established; signed depth can be negative. No valid eclipse localization follows.';np.savez_compressed(R/tic/f'pixel_s{sec:03d}.npz',out=O,deficit=Z);out.append(res)
json.dump(out,open(R/'pixel-results.json','w'),indent=2)
