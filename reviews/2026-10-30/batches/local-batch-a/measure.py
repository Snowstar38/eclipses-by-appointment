import json,csv,glob,os
import numpy as np
from astropy.io import fits
r=json.load(open('receipts.json')); search={x['tic']:x['P'] for x in r['search.jsonl']}; rows=[]; inventory=[]
sys={60:[2943.2],61:[2981.8],62:[3007],63:[3033.5],65:[3082.8,3089.8],67:[3147],83:[3564.5],85:[3616.5],86:[3649.3],87:[3688.8],89:[3732],94:[3875]}
for tic,p in search.items():
 P,t0,d=p['P'],p['t0'],p['dur']; w=min(max(4*d,0.45),0.38*P) if not os.environ.get('SHORT_BASELINE') else min(2.5*d,0.25*P)
 for fn in sorted(glob.glob('data/'+tic+'_s*.fits')):
  sec=int(fn.split('_s')[-1][:3])
  with fits.open(fn,memmap=False) as h:
   dat=h[1].data; t=np.array(dat['TIME'],float); f=np.array(dat['SAP_FLUX'],float); q=np.array(dat['QUALITY'],int); b=np.array(dat['SAP_BKG'],float)
  valid=np.isfinite(t)&np.isfinite(f)&(f>0); good=valid&(q==0)
  if not good.any():continue
  inventory.append(dict(tic=tic,sector=sec,total=len(t),finite=int(valid.sum()),quality0=int(good.sum()),start=float(t[good].min()),end=float(t[good].max())))
  for n in range(int(np.floor((t[good].min()-t0)/P))-1,int(np.ceil((t[good].max()-t0)/P))+2):
   tc=t0+n*P
   if not t[good].min()<=tc<=t[good].max():continue
   dt=t-tc; core=valid&(abs(dt)<d*.35); core0=core&(q==0); oot=good&(abs(dt)>d)&(abs(dt)<w)
   left=np.sum(oot&(dt<0)); right=np.sum(oot&(dt>0)); win=good&(abs(dt)<w)
   v={'tic':tic,'sector':sec,'cycle':n,'pred_btjd':round(tc,5),'n_core_q0':int(core0.sum()),'n_core_flagged':int((core&(q!=0)).sum()),'core_flag_fraction':round(float((core&(q!=0)).sum()/core.sum()),4) if core.sum() else None,'flag_bits_core':int(np.bitwise_or.reduce(q[core],initial=0)),'n_oot_left':int(left),'n_oot_right':int(right),'search_box_d':d,'status':'insufficient','near_systematic':any(abs(tc-x)<w for x in sys.get(sec,[]))}
   if np.sum(win)>1:v['max_gap_d']=round(float(np.max(np.diff(np.sort(t[win])))),4)
   if core0.sum()>=3 and left>=5 and right>=5:
    # Linear fit with 3 rounds of robust clipping in OOT. Core is excluded.
    x=dt[oot]; y=f[oot]; keep=np.ones(len(x),bool)
    for _ in range(3):
     co=np.polyfit(x[keep],y[keep],1); resid=y-np.polyval(co,x); sig=1.4826*np.median(np.abs(resid-np.median(resid))); keep=np.abs(resid-np.median(resid))<max(3*sig,1e-12)
     if keep.sum()<10:keep=np.ones(len(x),bool);break
    baseline=np.polyval(co,dt[core0]); depth=(1-np.median(f[core0]/baseline))*1000
    norm=f[oot]/np.polyval(co,dt[oot]); scatter=1.4826*np.median(abs(norm-np.median(norm)))*1000
    bc=b[core0]; bo=b[oot]; bc=bc[np.isfinite(bc)]; bo=bo[np.isfinite(bo)]
    v.update(status='measured',depth_ppt=round(float(depth),3),oot_scatter_ppt=round(float(scatter),3),bkg_core_minus_oot=round(float(np.median(bc)-np.median(bo)),3) if len(bc) and len(bo) else None,bkg_oot_mad=round(float(1.4826*np.median(abs(bo-np.median(bo)))),3) if len(bo) else None)
    # Matched fixed box scan: sampled midpoints, held duration; trend refit outside a broad guard. Uncertainty not inferred.
    tx=dt[win]; fy=f[win]/np.polyval(co,tx); best=None
    for shift in np.linspace(-d,d,41):
     inside=abs(tx-shift)<d*.35
     if inside.sum()<3:continue
     dep=1-np.median(fy[inside]); score=dep*np.sqrt(inside.sum())
     if best is None or score>best[0]:best=(score,shift,dep,inside.sum())
    if best:v.update(scan_mid_btjd=round(tc+best[1],5),scan_depth_ppt=round(float(best[2]*1000),3),scan_n=int(best[3]))
   rows.append(v)
suffix='_short' if os.environ.get('SHORT_BASELINE') else ''; json.dump(inventory,open('inventory'+suffix+'.json','w'),indent=2); json.dump(rows,open('events'+suffix+'.json','w'),indent=2)
keys=sorted({k for row in rows for k in row});
with open('events'+suffix+'.csv','w',newline='') as f:
 wr=csv.DictWriter(f,keys);wr.writeheader();wr.writerows(rows)
for tic in search:
 print('\n',tic,'sectors',len([x for x in inventory if x['tic']==tic]))
 for sec in sorted({x['sector'] for x in rows if x['tic']==tic}):
  a=[x for x in rows if x['tic']==tic and x['sector']==sec]; vals=[x['depth_ppt'] for x in a if x['status']=='measured']; flags=sum(x['n_core_flagged'] for x in a)
  print('sector',sec,'windows',len(a),'measured',len(vals),'median/range ppt', (round(float(np.median(vals)),2),round(min(vals),2),round(max(vals),2)) if vals else None,'flagged core',flags)
