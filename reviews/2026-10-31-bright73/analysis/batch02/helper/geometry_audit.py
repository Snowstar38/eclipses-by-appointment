import json,csv,math
D=json.load(open('gaia-geometry.json')); m={r['source_id']:r for r in csv.DictReader(open('../shared-catalogues/gaia-nss-full.csv'))};results={}
for tic,d in D.items():
 r=m[d['gaia_source_id']];p=float(r['period']);e=float(r['eccentricity']);w=math.radians(float(r['arg_periastron']));tp=float(r['t_periastron'])+389;epoch=json.load(open(tic+'/measurements.json'))['primary_epoch_btjd'];f=1.036149e-7*p*float(r['semi_amplitude_primary'])**3*(1-e*e)**1.5; offsets=[]
 for nu in (math.pi/2-w,3*math.pi/2-w):
  eccentric=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2)); c=tp+((eccentric-e*math.sin(eccentric))%(2*math.pi))*p/(2*math.pi); offsets.append((epoch-c+p/2)%p-p/2)
 results[tic]={'mass_function_diff':f-d['mass_function_solar'],'conjunction_offset_diff':[offsets[i]-d['conjunction'][i]['offset_days'] for i in range(2)],'mass_function_residual':d['minimum_m2_solar']**3/(d['assumed_m1_solar']+d['minimum_m2_solar'])**2-f}
json.dump(results,open('helper/geometry-audit.json','w'),indent=2);print(json.dumps(results,indent=2))
