"""Actual raw cadence and local baseline tests for N004 P/2-P/4 alternatives."""
from pathlib import Path
import json,hashlib,math
import numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='114244481';bulk=json.loads((B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'/f'{tic}.json').read_text());arr=[]
for rec in bulk['files']:
 p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
 with fits.open(p,memmap=False) as hd:
  a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 z=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[z];f=f[z]/np.median(f[z]);arr.append((int(rec['sector']),t,f,float(np.median(np.diff(t)))))
t0=2510.81385;P=20.44984;dur=.4;out=[];panels=[]
for div in [2,3,4]:
 per=P/div
 for s,t,f,cad in arr:
  for n in range(math.ceil((t.min()-t0)/per),math.floor((t.max()-t0)/per)+1):
   if n%div==0:continue
   mid=t0+n*per;core=abs(t-mid)<dur/2;pre=(t>mid-1.2)&(t<mid-.4);post=(t>mid+.4)&(t<mid+1.2)
   if sum(core)<2:continue
   base=(np.median(f[pre])+np.median(f[post]))/2 if min(sum(pre),sum(post))>=4 else None
   dep=1000*(1-np.median(f[core])/base) if base is not None else None
   noise=1000*1.4826*np.median(abs(np.r_[f[pre],f[post]]-np.median(np.r_[f[pre],f[post]]))) if base is not None else None
   full=bool(sum(core)>=(.75*dur/cad) and t[core].min()<mid-.3*dur and t[core].max()>mid+.3*dur and max(np.diff(t[core]))<2.5*cad and min(sum(pre),sum(post))>=4)
   row={'submultiple':div,'sector':s,'cycle':n,'mid':mid,'core_n':int(sum(core)),'expected_core_n':dur/cad,'pre_n':int(sum(pre)),'post_n':int(sum(post)),'core_first':float(t[core].min()),'core_last':float(t[core].max()),'max_internal_gap':float(max(np.diff(t[core]))),'cadence':cad,'full':full,'depth_ppt':dep,'baseline_mad_ppt':noise};out.append(row)
   if full and len(panels)<10:panels.append((row,t,f))
(B/tic/'submultiple-tests.json').write_text(json.dumps(out,indent=2)+'\n')
if panels:
 fig,ax=plt.subplots(len(panels),1,figsize=(10,2*len(panels)),squeeze=False)
 for a,(r,t,f) in zip(ax[:,0],panels):
  x=t-r['mid'];sel=abs(x)<1.3;a.plot(x[sel],f[sel],'.',ms=2);a.axvspan(-dur/2,dur/2,color='red',alpha=.1);a.set_title(f"P/{r['submultiple']} S{r['sector']} {r['mid']:.3f}: depth {r['depth_ppt']:.1f} ppt, MAD {r['baseline_mad_ppt']:.1f}",fontsize=9)
 fig.tight_layout();fig.savefig(B/tic/'submultiple-tests.png',dpi=130);plt.close(fig)
print([(r['submultiple'],r['sector'],round(r['mid'],3),r['full'],round(r['depth_ppt'] or 0,1),round(r['baseline_mad_ppt'] or 0,1)) for r in out])
