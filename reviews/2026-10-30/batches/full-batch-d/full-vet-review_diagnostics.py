from pathlib import Path
import json,numpy as np
import fit_batch as f
F=f.ROOT;out={}
for tic in f.targets:
 d=F/tic;r=json.load(open(d/'fit-results.json'));s=json.load(open(d/'secondary-fit.json'));o=json.load(open(d/'orbit-gates.json'));n=json.load(open(d/'gaia-nss.json'));ep=r['ephemeris'];events=[x for x in r['events'] if x['status']=='fit'];depth=float(np.median([x['depth'] for x in events]));phase=s['profile_phase'];an=[]
 for c in r['census']:
  dist=min(abs((c['phase']+.5)%1-.5),abs((c['phase']-phase+.5)%1-.5))
  if dist>max(r['shape']['T14']/ep['P'],.025) and c['depth']>depth*.5:an.append(c)
 sec={};
 for se in sorted(set(x['sec'] for x in events)):
  a=[x for x in events if x['sec']==se];sec[se]=dict(n=len(a),median_depth=float(np.median([x['depth'] for x in a])),min_depth=float(min(x['depth'] for x in a)),max_depth=float(max(x['depth'] for x in a)))
 timing=None
 if s['ephemeris']:
  se=s['ephemeris'];cyc=round((ep['Tref']-se['Tref'])/se['P']);tc=se['Tref']+cyc*se['P'];ph=((tc-ep['Tref'])/ep['P'])%1;er=np.sqrt(ep['Tref_error']**2+se['Tref_error']**2+(cyc*se['P_error'])**2)/ep['P'];ecos_approx=np.pi/2*(ph-.5);ec=float(n['eccentricity'])*np.cos(np.deg2rad(float(n['arg_periastron'])));
  timing=dict(phase_at_primary_Tref=ph,phase_error_conservative=er,ecos_first_order=ecos_approx,ecos_first_order_error=np.pi/2*er,gaia_ecos=ec,warning='First order relation inaccurate at large e; phase itself is measured and compared with exact Gaia prediction. Per-kind ephemeris covariance absent, so phase uncertainty conservatively adds period extrapolation in quadrature.')
 out[tic]=dict(primary_depth_median=depth,sector_depths=sec,primary_scan_edges=sum(x['scan_edge'] for x in events),flagged_core_events=sum(x['flagged_core']>0 for x in events),background_largest_fake_depth=max([abs(x['background_fake_depth']) for x in events if x['background_fake_depth'] is not None],default=0),background_median_depth_change=float(np.median([x['depth_with_background']-x['depth'] for x in events if x['depth_with_background'] is not None])),blind_census_count=len(r['census']),offphase_deep=an,timing=timing)
 print(tic,'offphase',an,'bg',out[tic]['background_largest_fake_depth'],'scanedges',out[tic]['primary_scan_edges'],'timing',timing)
json.dump(out,open(F/'review-diagnostics.json','w'),indent=2)
