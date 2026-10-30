import json,pathlib,numpy as np,math,glob,csv
from astropy.io import fits
r=pathlib.Path(__file__).parent; targets=json.loads((r.parent/'selected.json').read_text())['targets']; phys=json.loads((r/'physics-initial.json').read_text()); gaia={x['source_id']:x for x in csv.DictReader(open(r'C:\Home\Astra\made\binary-handoff-2026-10-30\shared-full-review\gaia-nss-ari.csv'))};nr=100; rr=(np.arange(nr)+.5)/nr

def blocked(z,k,u):
 # fraction of flux blocked for star radius1 by opaque circle radius k, at separations z
 z=np.atleast_1d(z); arg=(rr[None,:]**2+z[:,None]**2-k*k)/(2*np.maximum(z[:,None]*rr[None,:],1e-15));theta=np.arccos(np.clip(arg,-1,1))/np.pi;theta=np.where(arg<=-1,1,theta);theta=np.where(arg>=1,0,theta); intensity=1-u*(1-np.sqrt(1-rr**2));wt=rr*intensity;return (theta@wt)/sum(wt)

def phase_data(tic,m,se):
 events=[]
 for kind in ['primary','secondary']:
  entries=m['events'] if kind=='primary' else json.loads((r/f'{tic}_secondary_timing.json').read_text())['events']
  for e in entries:
   if kind=='primary' and not e['coverage_ok']:continue
   if kind=='secondary' and e['center_edge']:continue
   f=r.parent/'data'/f"{tic}_s{e['sector']:03d}.fits";a=fits.getdata(f,1);tt=np.array(a['TIME'],float); yy=np.array(a['SAP_FLUX'],float); q=np.array(a['QUALITY']);center=e['tc'];width=e['T14_d'];ok=(q==0)&np.isfinite(tt)&np.isfinite(yy)&(abs(tt-center)<max(.8,2*width));x=tt[ok]-center;y=yy[ok];outer=(abs(x)>width*.7)&(abs(x)<max(.75,width*1.7));
   if len(y)<20 or outer.sum()<6:continue
   bas=np.polyval(np.polyfit(x[outer],y[outer],1),x); norm=y/bas;cad=np.nanmedian(np.diff(x));events.append((kind,x,norm,cad,e['sector']))
 return events

def bins(events,kind,width):
 edges=np.linspace(-max(.5,width*1.5),max(.5,width*1.5),61);centers=(edges[:-1]+edges[1:])/2;values=[];cad=[]
 for k,x,y,c,sector in events:
  if k!=kind:continue
  digit=np.digitize(x,edges)-1;z=np.array([np.median(y[digit==j]) if np.any(digit==j) else np.nan for j in range(len(centers))]);values.append(z);cad.append(c)
 a=np.array(values);mean=np.nanmedian(a,axis=0);scatter=1.4826*np.nanmedian(abs(a-mean),axis=0);N=np.sum(np.isfinite(a),axis=0);sigma=np.maximum(scatter/np.sqrt(np.maximum(N,1)),.0004);use=(N>=3)&np.isfinite(mean);return centers[use],mean[use],sigma[use],float(np.median(cad)),len(values)

for tic,targ in targets.items():
 p=phys[tic];m=json.loads((r/f'{tic}_measurements.json').read_text());se=json.loads((r/f'{tic}_secondary_ephemeris.json').read_text());events=phase_data(tic,m,se);primary=[e['T14_d'] for e in m['events'] if e['coverage_ok']];width=np.median(primary);xp,yp,sp,cp,np1=bins(events,'primary',width);xs,ys,ss,cs,ns1=bins(events,'secondary',width);row=gaia[targ['gaia']['source_id']];e=float(row['eccentricity']);esg=e*math.sin(math.radians(float(row['arg_periastron'])));phase=json.loads((r/f'{tic}_secondary_timing.json').read_text())['weighted_phase'];ec=np.pi/2*(phase-.5);msk=p['M2_min_msun']/p['R1_catalogue']; ks=np.arange(max(.08,.7*msk),min(.9,2*msk)+.001,.04);bs=np.arange(0,1.61,.08);ess=sorted(set([-.12,-.06,0,.06,.12,round(esg,4)]));best=None;records=[]
 for k in ks:
  for scale in [.85,1,1.15]:
   r1=p['R1_catalogue']*scale; v0=2*np.pi*p['a_Rsun']/(p['P_d']*r1)
   for es in ess:
    e_trial=math.sqrt(ec*ec+es*es);v=v0/math.sqrt(1-e_trial*e_trial)
    for b in bs:
     bb=b*(1+es)/(1-es)
     if b>=1+k or bb>=1+k:continue
     # finite integration, approximate per-sector typical cadence
     zp=np.concatenate([np.sqrt(b*b+(v*(1+es)*(xp+o*cp))**2) for o in [-.4,-.2,0,.2,.4]]);zs=np.concatenate([np.sqrt(bb*bb+(v*(1-es)*(xs+o*cs))**2)/k for o in [-.4,-.2,0,.2,.4]])
     A=blocked(zp,k,.5).reshape(5,-1).mean(axis=0);B=blocked(zs,1/k,.7).reshape(5,-1).mean(axis=0)
     # observed deficits = alpha*A and (1-alpha)*B, alpha=F1/(F1+F2)
     den=np.sum((A/sp)**2)+np.sum((B/ss)**2);alpha=(np.sum(A*(1-yp)/sp**2)+np.sum(B*(B-(1-ys))/ss**2))/den;alpha=float(np.clip(alpha,.5,1));score=float(np.sum(((1-yp-alpha*A)/sp)**2)+np.sum(((1-ys-(1-alpha)*B)/ss)**2)); rec=(score,float(k),float(b),float(es),scale,alpha);records.append(rec)
     if best is None or score<best[0]:best=rec
 records.sort();n=len(xp)+len(xs);out={'grid':{'k':ks.tolist(),'b':bs.tolist(),'e_sin_omega':ess,'R1_scales': [.85,1,1.15],'ld_u1':.5,'ld_u2':.7,'ring_count':nr,'exposure_samples':5,'R2_range_relative_to_illustrative_M2min':[.7,2.0]},'n_primary_events':np1,'n_secondary_events':ns1,'number_bins':n,'best':{'chi2':best[0],'radius_ratio_k':best[1],'impact_parameter_A':best[2],'e_sin_omega':best[3],'R1_scale':best[4],'primary_flux_fraction':best[5],'R2_solar':best[1]*p['R1_catalogue']*best[4],'R2_over_M2min':best[1]*p['R1_catalogue']*best[4]/p['M2_min_msun']},'top_20':[list(x) for x in records[:20]],'eccentricity_convention':'e_trial=sqrt((pi/2*(observed secondary phase-0.5))^2+(e sin omega trial)^2); small-e approximation', 'caveats':'Coarse bounded grid; event-centering uses each fitted tc and may blur shape; uncertainties from inter-event binned scatter with 0.4 ppt floor. Correlated bins, local baseline, TIC parameter errors and systematics imply chi-square is diagnostic not calibrated. Uniform 5-point integration at median cadence is approximate for mixed cadences. No third light. R1 range illustrative +/-15%, not measured catalog errors. e cos omega fixed indirectly by observed individual times; no RV refit.'};(r/f'{tic}_limbdark_grid.json').write_text(json.dumps(out,indent=2));print(tic,out['best'], 'bins',n,flush=True)
