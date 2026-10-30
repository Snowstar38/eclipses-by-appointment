import pathlib,json,glob,sys,numpy as np
from astropy.io import fits
r=pathlib.Path(__file__).parent;d=json.loads((r.parent/'selected.json').read_text())
for tic in d['targets']:
 m=json.loads((r/f'{tic}_measurements.json').read_text()); mc=json.loads((r/f'{tic}_gaia_mc.json').read_text()); ep=m['ephemeris']; P=ep['P'];t0=ep['T0'];phi=(float(sys.argv[1]) if len(sys.argv)>1 else mc['A_to_B_phase_quantiles'][1]); good=[e for e in m['events'] if e.get('coverage_ok',True) and e['depth']/e['depth_error']>4];width=np.median([e['T14_d'] for e in good]);windows=[]
 for path in glob.glob(str(r.parent/'data'/f'{tic}_s*.fits')):
  sector=int(pathlib.Path(path).stem.split('_s')[-1]);a=fits.getdata(path,1); t=np.array(a['TIME'],float); y=np.array(a['SAP_FLUX'],float); q=np.array(a['QUALITY']); valid=np.isfinite(t)&np.isfinite(y)&(q==0);t=t[valid];y=y[valid]
  if len(t)<10:continue
  for k in range(int((min(t)-t0)/P)-1,int((max(t)-t0)/P)+2):
   tc=t0+(k+phi)*P
   if sum(abs(t-tc)<width/2)<3:continue
   item={'sector':sector,'tc_predicted':tc,'cycle':k,'results':{}}
   for mult in [.7,1,1.3]:
    w=width*mult; idx=abs(t-tc)<max(.6,2*w);x=t[idx]-tc;v=y[idx];v=v/np.median(v);h=np.clip((w/2-abs(x))/(w*.3),0,1);left=sum(x< -w/2);right=sum(x>w/2)
    if left<3 or right<3 or sum(h>.1)<3:continue
    A=np.column_stack([np.ones(len(x)),x,-h]);c=np.linalg.lstsq(A,v,rcond=None)[0];res=v-A@c;cov=np.linalg.pinv(A.T@A)*np.var(res); bins=[np.mean(res[i:i+5]) for i in range(0,len(res)-4,5)]; red=max(1,np.std(bins)/(np.std(res)/np.sqrt(5))) if len(bins)>4 and np.std(res)>0 else 1.; err=np.sqrt(cov[2,2])*red
    item['results'][str(mult)]={'depth':float(c[2]),'error':float(err),'n':len(x),'red_factor':float(red),'left':int(left),'right':int(right)}
   if item['results']:windows.append(item)
 out={'gaia_phase_median':phi,'gaia_phase_16_84':mc['A_to_B_phase_quantiles'][::2],'shape_width_primary_median_d':width,'windows':windows,'caveat':'Fixed epoch and fixed width tests; phase uncertainty may shift a true secondary. Errors approximate red noise. Width alternatives are correlated tests, not independent discoveries.'}
 for mult in ['0.7','1','1.3']:
  vals=[x['results'][mult] for x in windows if mult in x['results']]; w=np.array([1/x['error']**2 for x in vals]); depth=np.array([x['depth'] for x in vals]);
  if len(w):out['combined_'+mult]={'depth':float(sum(depth*w)/sum(w)),'error':float(1/np.sqrt(sum(w))),'N':len(w)}
 (r/f'{tic}_secondary{"_phase"+sys.argv[1] if len(sys.argv)>1 else ""}.json').write_text(json.dumps(out,indent=2));print(tic,len(windows),out.get('combined_1'))

