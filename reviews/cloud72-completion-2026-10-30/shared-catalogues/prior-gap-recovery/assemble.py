import csv,json
from pathlib import Path
p=Path(__file__).parent;c=json.load(open('[local working path omitted]'));r=json.load(open('[local working path omitted]'));b={(x['tic'],x['table']):x for x in json.load(open(p/'eb-battery-receipts.json'))};a={x['tic']:x for x in json.load(open(p/'asassn-receipts.json'))};prior={x['tic']:x for x in json.load(open('[local working path omitted]'))};tabs=['J/A+A/691/A242/obaf-eb1','J/ApJS/279/50/table3','J/ApJS/279/50/table4'];rows=[]
for x in c['stars']:
 tic=x['tic'];v=x['evidence_matrix'];assert all(b[(tic,t)]['status']=='success' and not b[(tic,t)]['rows'] for t in tabs);assert prior[tic]['status']=='success' and not prior[tic]['rows'];rows.append({'review_id':x['review_id'],'tic':tic,'vsx':v['VSX'],'simbad_primary':v['SIMBAD variability'],'gaia_dr3_eb':'fresh exact Gaia identifier: zero rows','prsa2022':v['Prsa2022'],'ijspeert2024':'fresh 5-arcsec cone: zero rows','kostov2025_vetted_table3':'fresh 5-arcsec cone: zero rows','kostov2025_vetted_table4':'fresh 5-arcsec cone: zero rows','asassn':'prior recovery 60-arcsec cone: zero rows','coverage_complete':'yes','scoped_prior_eb_status':'no identified prior EB','notes':x['note'],'prior_evidence':'[local working path omitted]'})
for x in r['objects']:
 tic=x['tic']
 if tic not in a:continue
 assert a[tic]['status']=='success' and not a[tic]['rows'];rows.append({'review_id':x['review_id'],'tic':tic,'vsx':'prior successful check: no target EB','simbad_primary':'SB*','gaia_dr3_eb':'prior target check: zero rows','prsa2022':'original 5-arcsec battery: zero rows','ijspeert2024':'original 5-arcsec battery: zero rows','kostov2025_vetted_table3':'original 5-arcsec battery: zero rows','kostov2025_vetted_table4':'original 5-arcsec battery: zero rows','asassn':'fresh 60-arcsec cone: zero rows','coverage_complete':'yes','scoped_prior_eb_status':'no identified prior EB','notes':'Kostov table2 candidate not vetted prior EB' if tic=='351541670' else '', 'prior_evidence':'[local working path omitted]'})
assert len(rows)==13
with (p/'coverage-matrix.csv').open('w',newline='',encoding='utf8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('13 complete')
