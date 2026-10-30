"""Fixed-shape secondary phase profile and independent event timing.
Profiles per-event quadratic baselines. Global phase scan is conditional on
Gaia conjunction and is not a blind-significance claim; empirical controls
and individual repeat detections adjudicate significance.
"""
import json
import numpy as np
import fit_batch as f
def combine(rows):
    a=[x for x in rows if x['status']=='fit'];d=np.array([x['depth'] for x in a]);e=np.array([x['depth_error'] for x in a]);w=1/e**2
    if not len(a):return dict(n=0)
    mu=float(sum(w*d)/sum(w));err=float(1/np.sqrt(sum(w)))
    return dict(n=len(a),depth=mu,error=err,snr=mu/err,scatter=float(np.std(d)),chi2=float(sum(w*(d-mu)**2)),dof=len(a)-1)
ROOT=f.ROOT
for tic in f.targets:
    dest=ROOT/tic;r=json.load(open(dest/'fit-results.json'));og=json.load(open(dest/'orbit-gates.json'));ep=r['ephemeris'];sh=json.load(open(dest/'secondary-shape.json')) if (dest/'secondary-shape.json').exists() else r['shape'];secs=f.read(tic);f.P=ep['P'];phase=og['predicted_secondary_phase']
    cuts=[];windows=[]
    for s in secs:
      for cyc in range(int(np.ceil((min(s['t'])-ep['T0'])/f.P-phase)),int(np.floor((max(s['t'])-ep['T0'])/f.P-phase))+1):
        tc=ep['T0']+(cyc+phase)*f.P;x,y,_=f.cut(s,tc,max(3*sh['T14'],.32));windows.append((s,cyc,tc))
        if sum(abs(x)<sh['T14']/2)>=3 and sum(x<-.65*sh['T14'])>=5 and sum(x>.65*sh['T14'])>=5:cuts.append((s,x,y,tc))
    candidates=[]
    for shift in np.linspace(-min(.06*f.P,sh['T14']),min(.06*f.P,sh['T14']),101):
        chi=0
        for s,x,y,tc in cuts:
            a=f.linear(x/max(3*sh['T14'],.32),y,f.trap(x-shift,sh['T14'],sh['fr'],s['cad']));chi+=a[0]
        candidates.append((chi,shift))
    best=min(candidates);bestphase=(phase+best[1]/f.P)%1;rows=[]
    for s,cyc,tc in windows:
        a=f.event(s,tc+best[1],sh['T14'],sh['fr']);a['cycle']=cyc;rows.append(a)
    stat=combine(rows);fit=[x for x in rows if x['status']=='fit'];strong=[x for x in fit if x['depth']>3*x['depth_error'] and not x['scan_edge']]
    se=None
    if len(strong)>=3:
        se=f.ephemeris(rows,f.P,ep['T0']+bestphase*f.P)
    # Include formal global depth error and between-event random effects.
    err=max(stat.get('error',0),np.std([x['depth'] for x in fit])/np.sqrt(max(len(fit),1)))
    stat['empirical_error']=float(err);stat['n_individual_gt3sigma']=len(strong)
    out=dict(predicted_gaia_phase=phase,profile_phase=float(bestphase),statistic=stat,events=rows,ephemeris=se,shape=sh,profile_scan_note='Conditional fitted secondary shape when secondary-shape.json exists, otherwise primary shape; phase optimized over +/- one T14. Weak/modulated secondary shape remains model dependent.')
    json.dump(out,open(dest/'secondary-fit.json','w'),indent=2);print(tic,'phase',bestphase,'secondary',stat,'eph',se,flush=True)
