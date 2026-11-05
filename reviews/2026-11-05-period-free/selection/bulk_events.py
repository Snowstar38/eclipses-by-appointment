"""Vectorized raw-SAP local-contrast harvest. Exploratory, not classification."""
from pathlib import Path
import argparse,hashlib,json,time
import numpy as np
from astropy.io import fits
DUR=[.06,.12,.24,.48,.96,1.6]
CONFIG={'durations_days':DUR,'flux':'SAP_FLUX','quality':0,'bin_minutes':10,
 'core':'[-.5d,+.5d]','sidebands':'[-1.75d,-.75d], [.75d,1.75d]',
 'noise':'max(side residual RMS about side-mean interpolated line, robust adjacent-difference noise)',
 'min_core':3,'min_each_side':4,'min_sampling_fraction':.5,
 'max_internal_gap':'max(3*cadence,.5*duration), tested separately in core and both sides',
 'flag':'supported and signed contrast>=5 and signed depth>=.001',
 'retention':'four dips and two brightenings per sector; flag-eligible ranked before others; suppress overlapping duration windows',
 'score_is_not_significance':True,'period_free':True}
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def scan(path,tic):
 rec={'path':str(path),'sha256':sha(path)}
 with fits.open(path) as h:
  assert int(h[0].header['TICID'])==int(tic)
  rec.update(sector=int(h[0].header['SECTOR']),camera=int(h[0].header.get('CAMERA',0)),ccd=int(h[0].header.get('CCD',0)))
  d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float)
  m=np.isfinite(t)&np.isfinite(f)&(f>0)&(d['QUALITY']==0);t,f=t[m],f[m]
 rec['quality_samples']=len(t)
 if len(t)<20:return dict(rec,status='insufficient_data',windows=[])
 assert np.all(np.diff(t)>0)
 f/=np.median(f)
 if np.median(np.diff(t))<.8*10/1440:
  _,inv,n=np.unique(np.floor((t-t[0])/(10/1440)).astype(int),return_inverse=True,return_counts=True)
  t,f=np.bincount(inv,t)/n,np.bincount(inv,f)/n
 epoch=float(t[0]);t=t-epoch
 cad=float(np.median(np.diff(t)));df=np.diff(f)[np.diff(t)<1.8*cad]
 noise=max(float(1.4826*np.median(np.abs(df-np.median(df)))/np.sqrt(2)),1e-9)
 sums=[np.r_[0,np.cumsum(x)] for x in [t,f,t*t,f*f,t*f]]
 allrows=[];n_valid=0
 for dur in DUR:
  a,b,c,d,e,g=[np.searchsorted(t,t+x*dur) for x in [-1.75,-.75,-.5,.5,.75,1.75]]
  nl,nc,nr=b-a,d-c,g-e
  ok=(nl>=4)&(nc>=3)&(nr>=4)
  idx=np.flatnonzero(ok)
  if not len(idx):continue
  a,b,c,d,e,g=[x[idx] for x in [a,b,c,d,e,g]];nl,nc,nr=nl[idx],nc[idx],nr[idx]
  def stats(lo,hi):return [s[hi]-s[lo] for s in sums]
  lt,lf,lt2,lf2,ltf=stats(a,b);rt,rf,rt2,rf2,rtf=stats(e,g)
  ct,cf,_,_,_=stats(c,d)
  slope=(rf/nr-lf/nl)/(rt/nr-lt/nl);intercept=lf/nl-slope*lt/nl
  dep=intercept+slope*ct/nc-cf/nc
  # Analytic sum of squared side residuals; time origins shifted for stability.
  ns=nl+nr;st=lt+rt;sf=lf+rf;st2=lt2+rt2;sf2=lf2+rf2;stf=ltf+rtf
  var=(sf2-2*intercept*sf-2*slope*stf+intercept**2*ns+2*intercept*slope*st+slope**2*st2)/ns
  scatter=np.maximum(noise,np.sqrt(np.maximum(var,0)))
  contrast=dep/scatter
  corefrac=np.minimum(1,nc*cad/dur);sidefrac=np.minimum(1,np.minimum(nl,nr)*cad/dur)
  # Prefix count detects any excessive INTERNAL gap within each interval.
  breaks=np.r_[0,np.cumsum(np.diff(t)>max(3*cad,.5*dur))]
  gapok=(breaks[d-1]-breaks[c]==0)&(breaks[b-1]-breaks[a]==0)&(breaks[g-1]-breaks[e]==0)
  support=(corefrac>=.5)&(sidefrac>=.5)&gapok
  n_valid+=len(idx)
  # Keep enough per-duration candidates for final ranked nonmaximum suppression.
  for sign in [1,-1]:
   flag=support&(sign*contrast>=5)&(sign*dep>=.001)
   order=np.lexsort((-sign*contrast,-flag.astype(int)))
   selected=[]
   for j in order:
    if sign*contrast[j]<=0:break
    if any(abs(t[idx[j]]-t[idx[k]])<dur for k in selected):continue
    selected.append(j)
    if len(selected)==12:break
   for j in selected:
    allrows.append({'time':float(t[idx[j]]+epoch),'duration':dur,'depth':float(dep[j]),'contrast':float(contrast[j]),
     'core_n':int(nc[j]),'left_n':int(nl[j]),'right_n':int(nr[j]),'core_fraction':float(corefrac[j]),
     'side_fraction':float(sidefrac[j]),'internal_gaps_ok':bool(gapok[j]),'supported':bool(support[j]),
     'flag':bool(flag[j]),'kind':'dip' if sign==1 else 'brightening','scatter':float(scatter[j]),'slope_per_day':float(slope[j])})
 windows=[]
 for kind,limit in [('dip',4),('brightening',2)]:
  sign=1 if kind=='dip' else -1;selected=[]
  for x in sorted((x for x in allrows if x['kind']==kind),key=lambda x:(x['flag'],sign*x['contrast']),reverse=True):
   if any(abs(x['time']-y['time'])<max(x['duration'],y['duration']) for y in selected):continue
   selected.append(x)
   if len(selected)==limit:break
  windows+=selected
 return dict(rec,status='ok',cadence=cad,point_noise=noise,scanned_windows=n_valid,windows=windows)
def one(tic,tg):
 out=[]
 for f in tg['files']:
  path=f['path'] if isinstance(f,dict) else f
  try:
   r=scan(path,tic)
   if isinstance(f,dict):assert r['sha256']==f['sha256'],'frozen source changed'
  except Exception as e:r={'path':str(path),'status':'failed','error':repr(e),'windows':[]}
  out.append(r)
 return {'tic':str(tic),'files':out}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('queue',type=Path);ap.add_argument('output',type=Path);a=ap.parse_args()
 q=json.loads(a.queue.read_text(encoding='utf8'));a.output.mkdir(parents=True,exist_ok=True)
 seal={'queue_sha256':sha(a.queue),'program_sha256':sha(__file__),'config':CONFIG}
 p=a.output/'seal.json'
 if p.exists():assert json.loads(p.read_text())==seal
 else:p.write_text(json.dumps(seal,indent=2)+'\n',encoding='utf8')
 for i,(tic,tg) in enumerate(q['targets'].items(),1):
  p=a.output/(str(tic)+'.json')
  if p.exists():continue
  start=time.time();r=one(tic,tg)
  p.write_text(json.dumps(r,separators=(',',':'),allow_nan=False)+'\n',encoding='utf8')
  if i%50==0 or len(q['targets'])<50:print(i,tic,'seconds',round(time.time()-start,2),flush=True)
if __name__=='__main__':main()
