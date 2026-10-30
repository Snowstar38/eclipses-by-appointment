"""Numerical limb-darkened two-disk feasibility fit, both eclipse shapes.
Rings integrate occulted angle (u1=.4,u2=.6). Shape normalization is free for
each kind, so aperture dilution and surface brightness are not overconstrained.
This is geometry feasibility, not a precise stellar characterization.
"""
import json
import numpy as np
import fit_batch as f
ROOT=f.ROOT
def loss(z,k,u):
    radii=(np.arange(40)+.5)/40;weights=radii*(1-u*(1-np.sqrt(1-radii*radii)));weights/=sum(weights)
    z=np.maximum(np.asarray(z),1e-6)[:,None];rr=radii[None,:];c=(rr*rr+z*z-k*k)/(2*rr*z)
    angle=np.arccos(np.clip(c,-1,1))/np.pi
    return angle@weights
def profile(tic,kind,r,sec):
    ep=r['ephemeris'];secs=f.read(tic);rows=r['events'] if kind=='A' else sec['events'];shape=r['shape'] if kind=='A' else json.load(open(ROOT/tic/'secondary-shape.json'))
    bins=np.linspace(-.32,.32,65);vals=[[] for _ in range(len(bins)-1)]
    for ev in rows:
        if ev['status']!='fit' or ev['scan_edge'] or ev['depth']<3*ev['depth_error']:continue
        s=next(x for x in secs if x['sec']==ev['sec']);x,y,_=f.cut(s,ev['tc'],.5);oot=abs(x)>max(shape['T14']*.65,.10)
        if sum(oot)<12:continue
        A=np.column_stack([np.ones(sum(oot)),x[oot],x[oot]**2]);c=np.linalg.lstsq(A,y[oot],rcond=None)[0];yy=1-y/np.polyval(c[::-1],x)
        ib=np.digitize(x,bins)-1
        for i in range(len(vals)):
            vv=yy[ib==i]
            if len(vv):vals[i].append(float(np.mean(vv)))
    xx=(bins[1:]+bins[:-1])/2;yy=np.array([np.mean(v) if len(v) else np.nan for v in vals]);ee=np.array([max(np.std(v)/np.sqrt(len(v)),.00015) if len(v)>1 else .001 for v in vals]);ok=np.isfinite(yy)
    return xx[ok],yy[ok],ee[ok]
for tic in f.targets:
    p=ROOT/tic;r=json.load(open(p/'fit-results.json'));s=json.load(open(p/'secondary-fit.json'));o=json.load(open(p/'orbit-gates.json'));ph=o['physics'][len(o['physics'])//2];P=r['ephemeris']['P'];a=ph['a_rsun']/ph['r1_rsun'];ecc=float(json.load(open(p/'gaia-nss.json'))['eccentricity']);pa=profile(tic,'A',r,s);pb=profile(tic,'B',r,s)
    if len(pb[0])<10:
        json.dump(dict(status='insufficient secondary shape'),open(p/'geometry.json','w'));continue
    best=None;grid=[]
    for k in np.arange(.10,.451,.025):
     for b in np.arange(.2,1.251,.035):
      for es in np.arange(-.20,.201,.025):
        b2=b*(1+es)/(1-es);chi=0;amps=[]
        for kind,(x,y,er),bb,vel,u in [('A',pa,b,2*np.pi*a/P*(1+es)/np.sqrt(1-ecc*ecc),.4),('B',pb,b2,2*np.pi*a/P*(1-es)/np.sqrt(1-ecc*ecc),.6)]:
            z=np.sqrt(bb*bb+(vel*x)**2);model=loss(z,k,u) if kind=='A' else loss(z/k,1/k,u)
            # Integrated cadence/profile smoothing is ~0.01d; model is sampled
            # at bins, with 0.15ppt floor and event-scatter errors.
            A=np.column_stack([np.ones(len(x)),model]);ww=1/er;coef=np.linalg.lstsq(A*ww[:,None],y*ww,rcond=None)[0]
            # Both luminosity fractions must be <=1. Unconstrained values >1
            # cannot be rescued by aperture dilution and are not physical fits.
            coef[1]=np.clip(coef[1],0,1);coef[0]=np.average(y-coef[1]*model,weights=ww**2)
            chi+=float(sum(((y-A@coef)/er)**2));amps.append(float(coef[1]))
        tup=(chi,k,b,es,*amps);grid.append(tup)
        if best is None or chi<best[0]:best=tup
    dof=len(pa[0])+len(pb[0])-7;scale=max(1,best[0]/max(dof,1));allowed=[x for x in grid if (x[0]-best[0])/scale<7.81]
    out=dict(status='conditional shape feasibility',best=dict(chi2=best[0],dof=dof,k=best[1],b_A=best[2],e_sin_omega=best[3],primary_scale=best[4],secondary_scale=best[5]),profile_interval_approx_95={name:[float(min(x[i] for x in allowed)),float(max(x[i] for x in allowed))] for name,i in [('k',1),('b_A',2),('e_sin_omega',3)]},error_inflation=scale,assumptions='Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.',primary_profile_n=len(pa[0]),secondary_profile_n=len(pb[0]))
    json.dump(out,open(p/'geometry.json','w'),indent=2);print(tic,out,flush=True)
