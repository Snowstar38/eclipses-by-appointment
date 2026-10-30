import json,pathlib,glob,numpy as np,csv
from astropy.io import fits
r=pathlib.Path(__file__).parent; d=json.loads((r.parent/'selected.json').read_text()); search={x['tic']:x for x in d['search']}
def fit(t,y,bg,guess,period,quality=None):
 sel=np.isfinite(t)&np.isfinite(y)&(abs(t-guess)<.8)
 t=t[sel];y=y[sel];bg=bg[sel] if bg is not None else None
 if len(t)<15:return None
 y=y/np.nanmedian(y); x=t-guess; cadence=np.nanmedian(np.diff(np.sort(t))); noise=1.4826*np.nanmedian(abs(np.diff(y)-np.nanmedian(np.diff(y))))/2**.5
 if not np.isfinite(noise) or noise==0:return None
 best=None; profiles=[]
 for center in np.arange(-.12,.121,.01):
  for width in np.arange(.06,.601,.02):
   for frac in [.2,.35,.5]:
    # finite exposure sampling
    h=np.zeros(len(t))
    for off in [-.4,-.2,0,.2,.4]:h+=np.clip((width/2-abs(x+off*cadence-center))/(width*frac),0,1)/5
    A=np.array([np.ones(len(t)),x,-h]).T; c=np.linalg.lstsq(A,y,rcond=None)[0]; res=y-A@c; chi=np.sum(res**2)
    if c[2]>0 and (best is None or chi<best[0]):best=(chi,center,width,frac,c,res,h,A)
 if best is None:return None
 # Refine profiles around the coarse optimum; record all candidate solutions.
 chi,c,w,f,co,res,h,A=best; candidates=[]
 for center in np.arange(c-.012,c+.0121,.0002):
  for width in np.arange(max(.03,w-.03),min(.65,w+.0301),.005):
   for frac in [.15,.2,.25,.3,.35,.4,.45,.5]:
    h=np.zeros(len(t))
    for off in [-.4,-.2,0,.2,.4]:h+=np.clip((width/2-abs(x+off*cadence-center))/(width*frac),0,1)/5
    A=np.array([np.ones(len(t)),x,-h]).T; co=np.linalg.lstsq(A,y,rcond=None)[0]; res=y-A@co; chi=np.sum(res**2)
    if co[2]>0:candidates.append((chi,center,width,frac,co,res,h,A))
 best=min(candidates,key=lambda a:a[0]);chi,c,w,f,co,res,h,A=best;n=len(t);bins=[]
 for k in range(0,n,5):
  if len(res[k:k+5])==5:bins.append(np.mean(res[k:k+5]))
 red=max(1.,np.std(bins)/(np.std(res)/np.sqrt(5))) if len(bins)>4 and np.std(res)>0 else 1.
 cov=np.linalg.pinv(A.T@A)*np.var(res)*red**2; dep=co[2]; de=np.sqrt(cov[2,2]);
 # compare local baseline windows and background regressor
 sens=[]
 for span in [.5,.7]:
  z=abs(x)<span
  if z.sum()>10:
   cc=np.linalg.lstsq(A[z],y[z],rcond=None)[0];sens.append(float(cc[2]))
 bcoef=None
 if bg is not None:
  b=np.nan_to_num(bg-np.nanmedian(bg)); b=b/(np.std(b) or 1); B=np.column_stack((A,b)); cb=np.linalg.lstsq(B,y,rcond=None)[0]; bcoef=float(cb[2])
 # slope crossing timing uncertainty; conservative cadence floor
 # Profile red-noise-adjusted residual threshold; bounded by grid resolution.
 threshold=chi+np.var(res)*red**2
 allowed=[v for v in candidates if v[0]<=threshold]
 centers=[v[1] for v in allowed]; widths=[v[2] for v in allowed]; ingress=[v[2]*v[3] for v in allowed]; flats=[v[2]*(1-2*v[3]) for v in allowed]
 te=max(.0001,(max(centers)-min(centers))/2)
 in_count=int(sum(abs(x-c)<w/2));left=int(sum((x<c-w/2)&(x>c-w/2-.25)));right=int(sum((x>c+w/2)&(x<c+w/2+.25)))
 coverage_ok=in_count>=3 and left>=3 and right>=3
 gap=float(np.max(np.diff(np.sort(t[abs(x-c)<w/2])))) if sum(abs(x-c)<w/2)>1 else None
 return dict(tc=float(guess+c),tc_error_d=float(te),depth=float(dep),depth_error=float(de),T14_d=float(w),T12_d=float(w*f),T23_d=float(w*(1-2*f)),shape_grid_resolution_d=.005,T14_profile_d=[float(min(widths)),float(max(widths))],T12_profile_d=[float(min(ingress)),float(max(ingress))],T23_profile_d=[float(min(flats)),float(max(flats))],coverage_ok=coverage_ok,in_count=in_count,left_count=left,right_count=right,baseline_depths=sens,background_regressed_depth=bcoef,background_fractional_change=float((bcoef-dep)/dep) if bcoef is not None else None,red_factor=float(red),n=int(n),max_in_event_gap_d=gap,cadence_d=float(cadence))
for tic,s in search.items():
 P=s['P']['P']; t0=s['P']['t0']; events=[]; files=glob.glob(str(r.parent/'data'/f'{tic}_s*.fits'))
 for file in files:
  with fits.open(file) as h:
   a=h[1].data; t=np.array(a['TIME'],float); y=np.array(a['SAP_FLUX'],float); q=np.array(a['QUALITY']); bg=np.array(a['SAP_BKG'],float); ok=(q==0)&np.isfinite(t)&np.isfinite(y); tt=t[ok]; yy=y[ok]; bb=bg[ok]
   if len(tt)<20:continue
   sector=int(pathlib.Path(file).stem.split('_s')[-1]); lo=int(np.floor((min(tt)-t0)/P));hi=int(np.ceil((max(tt)-t0)/P))
   for k in range(lo,hi+1):
    guess=t0+k*P
    if sum(abs(tt-guess)<.3)<6:continue
    z=fit(tt,yy,bb,guess,P)
    if z:
     z.update(sector=sector,cycle=k,flagged_in_0p3d=int(sum((q!=0)&np.isfinite(t)&(abs(t-guess)<.3))));events.append(z)
 # independent using same event model
 ind=[]
 for file in glob.glob(str(r/'data'/f'{tic}_TESS-SPOC*.fits')):
  with fits.open(file) as h:
   a=h[1].data;t=np.array(a['TIME'],float);y=np.array(a['PDCSAP_FLUX'],float);q=np.array(a['QUALITY']);ok=np.isfinite(t)&np.isfinite(y)&(q==0);t=t[ok];y=y[ok];sec=int(pathlib.Path(file).stem.split('_s')[-1])
   for e in events:
    if e['sector']==sec:
     z=fit(t,y,None,e['tc'],P)
     if z:z.update(sector=sec,cycle=e['cycle']);ind.append(z)
 good=[e for e in events if e['coverage_ok'] and e['depth']/e['depth_error']>4 and abs(e['tc']-(t0+e['cycle']*P))<.12]
 ep=None
 if len(good)>2:
  cycles=np.array([e['cycle'] for e in good]); times=np.array([e['tc'] for e in good]);err=np.array([e['tc_error_d'] for e in good]); mid=int(np.median(cycles)); X=np.column_stack((np.ones(len(cycles)),cycles-mid)); W=1/err**2; cov=np.linalg.inv(X.T@(W[:,None]*X)); beta=cov@(X.T@(W*times));res=times-X@beta; cov*=max(1.,float(np.sum((res/err)**2)/max(1,len(res)-2))); ep=dict(T0=float(beta[0]),cycle_zero=mid,P=float(beta[1]),covariance=cov.tolist(),oc_rms_d=float(np.sqrt(np.mean(res**2))),oc_d=res.tolist(),cycles=cycles.tolist())
 out=dict(tic=tic,search_period=P,search_t0=t0,events=events,independent=ind,ephemeris=ep,caveat='Local grid profile ranges; may be clipped by search boundaries; red-noise inflation approximated by 5-point residual bins. Timing errors are approximate. Event inclusion requires actual coverage; no post-gap trimming.')
 (r/f'{tic}_measurements.json').write_text(json.dumps(out,indent=2));print(tic,len(events),len(good),len(ind),ep and ep['P'],flush=True)
