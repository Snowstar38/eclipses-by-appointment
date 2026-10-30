import numpy as np,pathlib,json,csv,math
r=pathlib.Path(__file__).parent; d=json.loads((r.parent/'selected.json').read_text());rows={x['source_id']:x for x in csv.DictReader(open(r'C:\Home\Astra\made\binary-handoff-2026-10-30\shared-full-review\gaia-nss-ari.csv'))};phys=json.loads((r/'physics-initial.json').read_text())
def overlap(k,b):
 if b>=1+k:return 0.
 if b<=abs(1-k):return math.pi*min(1,k)**2
 return math.acos(max(-1,min(1,(b*b+1-k*k)/(2*b))))+k*k*math.acos(max(-1,min(1,(b*b+k*k-1)/(2*b*k))))-.5*math.sqrt(max(0,(-b+1+k)*(b+1-k)*(b-1+k)*(b+1+k)))
for tic,t in d['targets'].items():
 row=rows[t['gaia']['source_id']];e=float(row['eccentricity']);w=math.radians(float(row['arg_periastron']));es=e*math.sin(w);p=phys[tic];m=json.loads((r/f'{tic}_measurements.json').read_text());ev=[x for x in m['events'] if x['coverage_ok'] and x['depth']/x['depth_error']>4];depth=np.median([x['depth'] for x in ev]);dur=np.median([x['T14_d'] for x in ev]);s=json.loads((r/f'{tic}_secondary_timing.json').read_text());sec=np.median([x['depth'] for x in s['events'] if not x['center_edge']]);sdur=np.median([x['T14_d'] for x in s['events'] if not x['center_edge']]);valid=[]
 # uniform surface brightness, spherical bodies, small angle duration approximation
 for k in np.arange(.05,1.001,.01):
  for b in np.arange(0,1+k,.01):
   bb=b*(1+es)/(1-es);o1=overlap(k,b);o2=overlap(k,bb)
   if o1<=0 or o2<=0:continue
   J=sec*o1/(depth*o2);d1=o1/(math.pi*(1+J*k*k));dur1=p['P_d']/math.pi*(p['R1_catalogue']/p['a_Rsun'])*math.sqrt(max(0,(1+k)**2-b*b))*math.sqrt(1-e*e)/(1+es);dur2=p['P_d']/math.pi*(p['R1_catalogue']/p['a_Rsun'])*math.sqrt(max(0,(1+k)**2-bb*bb))*math.sqrt(1-e*e)/(1-es)
   # deliberately broad 25% to allow uncertain shape, TIC radius, LD, dilution
   if abs(d1/depth-1)<.25 and abs(dur1/dur-1)<.25 and abs(dur2/sdur-1)<.3:valid.append((k,b,J,d1,dur1,dur2))
 out={'primary_depth':float(depth),'primary_duration_d':float(dur),'secondary_depth':float(sec),'secondary_duration_d':float(sdur),'Gaia_e_sin_omega':es,'n_grid_feasible':len(valid),'assumptions':'uniform brightness two discs, edge-on minimum-mass semimajor axis, catalog R1, Gaia e sin omega; broad 25-30% tolerance; no limb darkening/integration/dilution; secondary duration weakly identified','feasible_ranges':{str(i):[float(min(x[i] for x in valid)),float(max(x[i] for x in valid))] for i in range(3)} if valid else None,'range_keys':['radius_ratio','impact_parameter_A','surface_brightness_ratio'],'illustrative_ms_radius_ratio':p['M2_min_msun']/p['R1_catalogue'],'grid_count_within_30pct_ms_radius':sum(1 for x in valid if .7*p['M2_min_msun']/p['R1_catalogue']<=x[0]<=1.3*p['M2_min_msun']/p['R1_catalogue']),'minimum_feasible_R2_solar':float(min(x[0] for x in valid)*p['R1_catalogue']) if valid else None};(r/f'{tic}_geometry_grid.json').write_text(json.dumps(out,indent=2));print(tic,len(valid),out['feasible_ranges'])

