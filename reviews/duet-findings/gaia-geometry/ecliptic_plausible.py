"""Are the period-free review's unconfirmable ("plausible") dips concentrated near the ecliptic,
where main-belt asteroids cross TESS apertures (the house found seven such crossings on Nov 24)?
Controls for TESS coverage (usable QLP sectors), which is also lower near the ecliptic.
Needs numpy, scipy, astropy. Usage: python3 ecliptic_plausible.py [repo=.] [out.csv]"""
import csv,sys,os,numpy as np
from scipy.stats import fisher_exact
from scipy.optimize import minimize
from astropy.coordinates import SkyCoord
import astropy.units as u
root=sys.argv[1] if len(sys.argv)>1 else '.'
pf=list(csv.DictReader(open(os.path.join(root,'period-free-review.csv'))))
at={r['tic']:r for r in csv.DictReader(open(os.path.join(root,'reviews/2026-11-05-period-free/selection/all-targets.csv')))}
pf=[r for r in pf if r['tic'] in at]
ra=[float(at[r['tic']]['ra_deg']) for r in pf]; de=[float(at[r['tic']]['dec_deg']) for r in pf]
beta=np.abs(SkyCoord(ra*u.deg,de*u.deg).barycentrictrueecliptic.lat.deg)
nsec=np.array([int(at[r['tic']]['usable_files'] or 0) for r in pf])
ver=[r['physical_verdict'] for r in pf]
low=beta<20
print(f'period-free reviews with coordinates: {len(pf)}; |beta|<20 deg: {low.sum()} (median usable sectors {np.median(nsec[low]):.1f} vs {np.median(nsec[~low]):.1f})')
for lab,S in (('PLAUSIBLE',{'PLAUSIBLE'}),('CONFIRMED+PROBABLE',{'CONFIRMED','PROBABLE'}),('REFUTED',{'REFUTED'})):
    a=sum(v in S for v,l in zip(ver,low) if l); c=sum(v in S for v,l in zip(ver,low) if not l)
    p=fisher_exact([[a,low.sum()-a],[c,(~low).sum()-c]],alternative='greater').pvalue
    print(f'  {lab:20s} near ecliptic {a}/{low.sum()} ({a/low.sum():.2f})  elsewhere {c}/{(~low).sum()} ({c/(~low).sum():.2f})  one-sided p={p:.3g}')
y=np.array([v=='PLAUSIBLE' for v in ver],float)
X=np.column_stack([np.ones(len(y)),low.astype(float),np.log(np.maximum(nsec,1))])
nll=lambda w:np.sum(np.logaddexp(0,X@w)-y*(X@w))
res=minimize(nll,np.zeros(3),method='BFGS'); se=np.sqrt(np.diag(res.hess_inv))
print(f'  logistic, plausible ~ near-ecliptic + ln(sectors): near-ecliptic {res.x[1]:+.2f} +- {se[1]:.2f} ({res.x[1]/se[1]:.1f} sigma), ln(sectors) {res.x[2]:+.2f} +- {se[2]:.2f}')
for nlo,nhi in((0,4),(4,10)):
    for l in (True,False):
        s=[v for v,n,b in zip(ver,nsec,low) if nlo<=n<nhi and b==l]
        print(f'  sectors {nlo}-{nhi-1}, {"near" if l else "far "}: plausible {s.count("PLAUSIBLE")}/{len(s)} ({s.count("PLAUSIBLE")/len(s):.2f})')
out=[dict(sample_id=r['sample_id'],tic=r['tic'],abs_ecliptic_lat_deg=round(b,1),usable_sectors=n,physical_verdict=v,report=r['report']) for r,b,n,v in zip(pf,beta,nsec,ver) if b<20 and v in('PLAUSIBLE','UNRESOLVED')]
print('near-ecliptic plausible/unresolved (first targets for a moving-object check):',' '.join(o['sample_id'] for o in sorted(out,key=lambda o:o['abs_ecliptic_lat_deg'])))
if len(sys.argv)>2:
    w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(out[0]));w.writeheader();w.writerows(sorted(out,key=lambda o:o['abs_ecliptic_lat_deg']))
