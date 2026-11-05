"""Enumerate TIC 128720791 integer-cycle fits over the three measured centers."""
import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
m=json.loads((B/'128720791'/'measurements.json').read_text(encoding='utf-8'))
ev=sorted((e for e in m['events'] if e.get('timing_usable')),key=lambda e:e['mid_btjd'])
assert len(ev)==3
t=np.array([e['mid_btjd'] for e in ev]);err=np.array([e['timing_error_days'] for e in ev]);records=[]
for n1 in range(35,75):
 for n2 in range(n1+1,120):
  n=np.array([0,n1,n2]);X=np.column_stack([np.ones(3),n]);A=X/err[:,None];cov=np.linalg.inv(A.T@A);beta=cov@(A.T@(t/err));res=t-X@beta;chi=float(np.sum((res/err)**2));P=float(beta[1])
  if 15<P<30 and chi<25:records.append(dict(cycles=[0,n1,n2],period_days=P,chi_square=chi,maximum_abs_residual_minutes=float(max(abs(res))*1440)))
records.sort(key=lambda x:x['chi_square'])
src=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf-8'))['128720791'];dur=m['screen_duration_days']
for z in records:
 z['clean_predicted_windows']=[]
 for rec in src['target']['file_receipts']:
  with fits.open(rec['path'],memmap=False) as h:
   a=h[1].data;tt=np.asarray(a['TIME'],float);ff=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  good=np.isfinite(tt)&np.isfinite(ff)&(ff>0)&(q==0);tt=tt[good];ff=ff[good]
  for n in range(math.ceil((tt.min()-t[0])/z['period_days']),math.floor((tt.max()-t[0])/z['period_days'])+1):
   pred=t[0]+n*z['period_days'];dt=tt-pred;core=np.abs(dt)<max(dur*.5,.06);side=(np.abs(dt)>.18)&(np.abs(dt)<.4);pre=side&(dt<0);post=side&(dt>0)
   if sum(core)<3 or sum(pre)<3 or sum(post)<3:continue
   base=np.median(ff[side]);dep=(1-np.median(ff[core])/base)*1000;noise=1.4826*np.median(abs(ff[side]/base-1))*1000
   z['clean_predicted_windows'].append(dict(sector=rec['sector'],cycle=n,predicted_btjd=pred,core_samples=int(sum(core)),median_deficit_ppt=float(dep),oot_scatter_ppt=float(noise)))
out=dict(tic='128720791',measured_centers_btjd=t.tolist(),conservative_timing_errors_days=err.tolist(),searched_cycle_ranges={'second_event':[35,74],'third_event':[36,119]},period_search_days=[15,30],accepted_chi_square_under_25=records,gaia_period_days=21.7089228516977,interpretation='Conditional integer-cycle enumeration, not blind all-period completeness. Three centers minus epoch/period leave one timing degree of freedom. The 16.2798-day alias has three clean additional predicted windows with approximately zero loss, versus 4–8 ppt measured events, and is rejected as an equal-depth same-kind clock. The Gaia-near 21.7064-day branch has no contradictory clean predicted window in retained sectors. The partial sector-56 first cycle is not used as a clean null.')
(B/'alias-128720791.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('n',len(records));print(records[:10])
