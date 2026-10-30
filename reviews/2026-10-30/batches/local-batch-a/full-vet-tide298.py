"""Adversarial smooth-tide+orbital-wave versus tide+wave+eclipse test.
Kumar-type equilibrium tide shape at Gaia e/omega, i=90deg; amplitude free.
Five per-sector orbital harmonics allow stronger smooth variability. This is
not an exhaustive pulsation model; correlated residuals prohibit formal FAP.
"""
import json
import numpy as np
import fit_batch as f
p=f.ROOT/'298645930';r=json.load(open(p/'fit-results.json'));n=json.load(open(p/'gaia-nss.json'));ep=r['ephemeris'];T=r['shape']['T14'];fr=r['shape']['fr'];secs=f.read('298645930');e=float(n['eccentricity']);omega=np.radians(float(n['arg_periastron']));tp=float(n['t_periastron'])+389
tot=[0.,0.];N=0;pars=[0,0];deps=[]
for s in secs:
 good=s['q']==0;t=s['t'][good];y=s['f'][good];x=(t-np.mean(t))/max(np.ptp(t),1);phase=(t-ep['T0'])/ep['P'];M=2*np.pi*(t-tp)/ep['P'];E=M.copy()
 for _ in range(12):E-=(E-e*np.sin(E)-M)/(1-e*np.cos(E))
 nu=2*np.arctan2(np.sqrt(1+e)*np.sin(E/2),np.sqrt(1-e)*np.cos(E/2));tide=(1-3*np.sin(nu+omega)**2)/(1-e*np.cos(E))**3
 cols=[np.ones(len(t)),x,x*x,tide]
 for k in range(1,6):cols.extend([np.sin(2*np.pi*k*phase),np.cos(2*np.pi*k*phase)])
 A=np.column_stack(cols);dt=(t-ep['T0']+ep['P']/2)%ep['P']-ep['P']/2;template=-f.trap(dt,T,fr,s['cad'])
 for i,B in enumerate([A,np.column_stack([A,template])]):
  c=np.linalg.lstsq(B,y,rcond=None)[0];res=y-B@c;tot[i]+=float(sum(res*res));pars[i]+=B.shape[1]
  if i==1:deps.append(dict(sector=s['sec'],eclipse_depth=float(c[-1])))
 N+=len(t)
out=dict(models=['per-sector quadratic+5 orbital harmonics+equilibrium tide','same+integrated fixed primary eclipse'],rss=tot,n=N,npar=pars,delta_BIC_tide_only_minus_plus_eclipse=float(N*np.log(tot[0]/tot[1])+(pars[0]-pars[1])*np.log(N)),eclipse_depths=deps,interpretation='Positive delta BIC favors a narrow eclipse beyond smooth tide/wave. Strong residual correlations/modulation remain, so no formal significance or physical tidal amplitude is inferred. Secondary is not established by this test.')
json.dump(out,open(p/'tide-test.json','w'),indent=2);print(out)
