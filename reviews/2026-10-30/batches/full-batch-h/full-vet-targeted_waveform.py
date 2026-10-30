import json,numpy as np
import fit_batch as f
from pathlib import Path
D=f.ROOT; tic='1989681813'; r=json.load(open(D/tic/'fit-results.json')); n=json.load(open(D/tic/'gaia-nss.json')); P=float(n['period']); e=float(n['eccentricity']); w=np.deg2rad(float(n['arg_periastron'])); tp=float(n['t_periastron'])+389; t0=r['ephemeris']['T0']; out=[]
for s in f.read(tic):
 m=(s['q']==0);t=s['t'][m];y=s['f'][m]; phase=((t-t0+P/2)%P)-P/2; M=2*np.pi*(t-tp)/P; E=M.copy()
 for _ in range(12):E-= (E-e*np.sin(E)-M)/(1-e*np.cos(E))
 nu=2*np.arctan2(np.sqrt(1+e)*np.sin(E/2),np.sqrt(1-e)*np.cos(E/2)); tide=(1-3*np.sin(nu+w)**2)/(1-e*np.cos(E))**3
 # per-sector polynomial + low-order orbital harmonics absorb evolving smooth variability; Gaia heartbeat basis retained
 x=(t-np.mean(t))/P; A=np.column_stack([np.ones(len(t)),x,x*x,tide]+[v for k in [1,2,3] for v in (np.sin(2*np.pi*k*t/P),np.cos(2*np.pi*k*t/P))]); base=np.linalg.lstsq(A,y,rcond=None)[0];res=y-A@base; rss0=float(res@res);best=None
 for T in np.linspace(.15,1.5,55):
  for shift in np.linspace(-.25,.25,21):
   z=f.trap(phase-shift,T,.5,s['cad']); B=np.column_stack([A,-z]); c=np.linalg.lstsq(B,y,rcond=None)[0]; rr=y-B@c; rss=float(rr@rr)
   if c[-1]>0 and (best is None or rss<best[0]):best=(rss,T,shift,float(c[-1]))
 # robust correlated noise not modeled; fractional RSS gain descriptive only
 out.append(dict(sector=s['sec'],n=len(t),baseline_rss=rss0,best_rss=best[0],T14=best[1],shift=best[2],depth=best[3],fractional_rss_improvement=(rss0-best[0])/rss0,note='sector-level 3 harmonics plus Gaia-eccentric heartbeat basis, quadratic drift; positive eclipse scanned in width and shift; no calibrated significance; full sector, nonstationary modulation possible'))
json.dump(out,open(D/tic/'targeted-waveform.json','w'),indent=2);print(json.dumps(out,indent=2))
