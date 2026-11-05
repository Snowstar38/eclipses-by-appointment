"""Check actual cadence and flux at conditional short-period eclipse aliases."""
import hashlib, json, math
from pathlib import Path
import numpy as np
from astropy.io import fits

B=Path(__file__).resolve().parent
CONFIG={
 '398073873':dict(epoch=1811.26020146,period=22.42906598,halfcore=.045,cycles=(0,8,48,73,74)),
 '143497778':dict(epoch=1520.09707851,period=23.40062282,halfcore=.14,cycles=(-1,0,62,63,93,94,95)),
}
for tic,cfg in CONFIG.items():
 d=B/tic;ctx=json.loads((d/'lead-context.json').read_text());out=[]
 for s in ctx['sectors']:
  fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
  with fits.open(fp,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
  cad=s['cadence_days'];w=cfg['halfcore']
  for divisor in (2,3,4):
   per=cfg['period']/divisor
   lo=math.ceil((t.min()-cfg['epoch'])/per);hi=math.floor((t.max()-cfg['epoch'])/per)
   for n in range(lo,hi+1):
    if n%divisor==0:continue
    c=cfg['epoch']+n*per
    core=(t>=c-w)&(t<=c+w);left=(t>=c-5*w)&(t<c-2*w);right=(t>c+2*w)&(t<=c+5*w)
    ct=t[core];expected=2*w/cad
    coreok=bool(len(ct)>=.75*expected and len(ct)>2 and ct[0]<=c-w+2*cad and ct[-1]>=c+w-2*cad and np.max(np.diff(ct))<=3*cad)
    sideok=bool(left.sum()>=5 and right.sum()>=5)
    if not(coreok and sideok):continue
    st=np.concatenate([t[left],t[right]]);sf=np.concatenate([f[left],f[right]])
    trend=np.polyfit(st-c,sf,1);cv=f[core]/np.polyval(trend,ct-c);sv=sf/np.polyval(trend,st-c)
    out.append(dict(divisor=divisor,sector=s['sector'],predicted_btjd=float(c),core_first_btjd=float(ct[0]),core_last_btjd=float(ct[-1]),core_count=len(ct),core_expected=float(expected),core_max_gap_days=float(np.max(np.diff(ct))),left_count=int(left.sum()),right_count=int(right.sum()),local_depth_ppt=float((1-np.median(cv))*1000),side_mad_ppt=float(1.4826*np.median(np.abs(sv-np.median(sv)))*1000),source_sha256=s['source_sha256']))
 (d/'lead-alias-nulls.json').write_text(json.dumps(dict(config=cfg,covered_windows=out,caution='These are actual covered short-alias windows; local linear baseline and depth estimates are diagnostic, not formal non-detection bounds.'),indent=2)+'\n')
 print(tic,{k:[len(v:=[z for z in out if z['divisor']==k]),sum(abs(z['local_depth_ppt'])<3 for z in v)] for k in (2,3,4)})
