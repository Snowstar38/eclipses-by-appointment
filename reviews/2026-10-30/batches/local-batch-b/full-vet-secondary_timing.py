import pathlib,json,numpy as np
from astropy.io import fits
r=pathlib.Path(__file__).parent
for tic in ['295945076','372376841','416525506','451493289','348737250']:
 m=json.loads((r/f'{tic}_measurements.json').read_text());ep=m['ephemeris']; phase=.52 if tic=='295945076' else .5; s=json.loads((r/f'{tic}_secondary_phase{phase}.json').read_text()); entries=[]
 for win in s['windows']:
  sec=win['sector'];a=fits.getdata(next((r.parent/'data').glob(f'{tic}_s{sec:03d}.fits')),1);t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']); guess=win['tc_predicted'];idx=(q==0)&np.isfinite(t)&np.isfinite(y)&(abs(t-guess)<.7);x=t[idx]-guess;y=y[idx];
  if len(y)<15:continue
  y=y/np.median(y);w=s['shape_width_primary_median_d'];best=None;prof=[]
  for c in np.arange(-.055,.0551,.001):
   for wid in [w*.7,w,w*1.3]:
    for f in [.2,.35,.5]:
     h=np.clip((wid/2-abs(x-c))/(wid*f),0,1);A=np.column_stack((np.ones(len(x)),x,-h));coef=np.linalg.lstsq(A,y,rcond=None)[0];res=y-A@coef;loss=np.sum(res**2);v=(loss,c,wid,f,coef,res)
     if coef[2]>0:prof.append(v)
     if coef[2]>0 and (best is None or loss<best[0]):best=v
  if best is None:continue
  loss,c,wid,f,coef,res=best;bins=[np.mean(res[i:i+5]) for i in range(0,len(res)-4,5)];red=max(1,np.std(bins)/(np.std(res)/np.sqrt(5))) if len(bins)>4 and np.std(res)>0 else 1;allowed=[z[1] for z in prof if z[0]<=loss+np.var(res)*red**2];err=max(.0005,(max(allowed)-min(allowed))/2);entries.append({'tc':guess+c,'error_d':err,'depth':float(coef[2]),'T14_d':wid,'sector':sec,'cycle':win['cycle'],'center_edge':bool(abs(c)>.054)})
 usable=[e for e in entries if not e['center_edge']];phase_vals=[((e['tc']-ep['T0'])/ep['P']-e['cycle']) for e in usable]; weights=[1/e['error_d']**2 for e in usable];ave=float(np.average(phase_vals,weights=weights)) if weights else None;out={'starting_phase':phase,'events':entries,'weighted_phase':ave,'formal_phase_error':float(1/np.sqrt(sum(weights))/ep['P']) if weights else None,'caveat':'Exploratory phase grid and local per-event fits; red-noise, phase selection, correlated events, width boundary, and cycle alias can inflate uncertainty. Not an independent significance test.'};(r/f'{tic}_secondary_timing.json').write_text(json.dumps(out,indent=2));print(tic,len(entries),len(usable),ave,out['formal_phase_error'])

