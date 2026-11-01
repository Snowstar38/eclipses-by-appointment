import csv,json,hashlib,collections
from pathlib import Path
p=Path(__file__).parent;t=json.loads((p/'targets-selected.json').read_text());vs={r['tic']:r for r in json.loads((p/'vsx70-receipts.json').read_text())};ass={r['tic']:r for r in json.loads((p/'asassn-receipts.json').read_text())};sim={r['id'].replace('Gaia DR3 ',''):r for r in csv.DictReader(open(p/'simbad-targets.csv'))};eb={r['source_id'] for r in csv.DictReader(open(p/'gaia-vari_eclipsing_binary.csv'))};battery={(r['tic'],r['table']):r for r in json.loads((p/'eb-battery-receipts.json').read_text())};tabs=['J/ApJS/258/16/tess-ebs','J/A+A/691/A242/obaf-eb1','J/ApJS/279/50/table3','J/ApJS/279/50/table4']
base=Path('[local path omitted] 5.1/made/paper/work/novelty-reconciliation/chopard-evidence/extracted/gaia-dr3-edge-on-orbits-tess-eclipses-v1.2.0');track=list(csv.DictReader(open(base/'track3_detail.csv')));dossier=list(csv.DictReader(open(base/'vetting/dossier.csv')));rows=[];overlap=[]
for pos,(tic,x) in enumerate(t.items(),1):
 g=str(x['gaia']['source_id']);v=vs[tic];a=ass[tic];vr=v['rows'];ar=a['rows'];ve=[r for r in vr if r.get('Name')=='Gaia DR3 '+g];ae=[r for r in ar if r.get('TIC','').lstrip('0')==tic or r.get('GaiaDR3')==g];close=[r for r in vr if r not in ve and float(r['_r'])<2];b=[battery[(tic,tb)] for tb in tabs];known=[]
 for label,items in [('VSX',ve),('ASASSN',ae)]:
  for z in items:
   if any(s.rstrip(':') in ('E','EA','EB','EW') for s in z.get('Type','').split('/')):known.append({'source':label,'row':z})
 nearby_possible_eb=[{'source':'VSX close positional counterpart; exact alias identifier unresolved','separation_arcsec':z['_r'],'row':z} for z in close if any(v.rstrip(':') in ('E','EA','EB','EW') for v in z.get('Type','').split('/'))]
 if tic=='66072136':
  assert len(nearby_possible_eb)==1 and nearby_possible_eb[0]['row']['Name']=='V0693 Lac'
  known.append({'source':'VSX','identity_basis':'positionally secure counterpart; Gaia target 0.01 arcsec from rounded VSX coordinates, next Gaia source 1.96 arcsec away and 7.83 mag fainter; exact catalogue alias absent','period_note':'VSX EA period 1.08916 d differs from Gaia SB1 orbit 4.589208 d; physical signal and period require independent review','row':nearby_possible_eb[0]['row']})
  nearby_possible_eb=[]
 if g in eb:known.append({'source':'GaiaDR3 vari_eclipsing_binary','source_id':g})
 if sim[g]['otype'] in ('EB*','Al*','bL*','WU*'):known.append({'source':'SIMBAD primary otype','row':sim[g]})
 for label,item in zip(['Prsa2022','IJspeert2024','Kostov2025 table3','Kostov2025 table4'],b):
  for z in item['rows']:
   if z.get('TIC','').lstrip('0')==tic:known.append({'source':label,'row':z})
 tr=[r for r in track if r.get('source_id')==g];dr=[r for r in dossier if r.get('source_id')==g or r.get('TIC')==tic]
 if tr or dr:overlap.append({'tic':tic,'gaia_dr3':g,'track3':tr,'dossier':dr})
 complete=v['status']=='success' and a['status']=='success' and g in sim and all(z['status']=='success' for z in b)
 r=dict(position=pos,tic=tic,gaia_dr3=g,vsx_status=v['status'],vsx_exact_gaia=json.dumps(ve),vsx_close_identity_review=json.dumps(close),vsx_other_neighbours=json.dumps([z for z in vr if z not in ve and z not in close]),simbad_status='success',simbad_primary_otype=sim[g]['otype'],gaia_dr3_eb_status='success',gaia_dr3_eb='exact match' if g in eb else 'no exact match',prsa2022_status=b[0]['status'],ijspeert2024_status=b[1]['status'],kostov2025_vetted_status='success' if all(z['status']=='success' for z in b[2:]) else 'unavailable',historical_battery_receipts=json.dumps(b),asassn_status=a['status'],asassn_exact=json.dumps(ae),asassn_neighbours=json.dumps([z for z in ar if z not in ae]),known_prior_eb_identification=json.dumps(known),nearby_possible_eb=json.dumps(nearby_possible_eb),coverage_complete='yes' if complete else 'no',scoped_prior_eb_status='known prior EB' if known else 'nearby EB identity unresolved' if nearby_possible_eb else 'no identified prior EB' if complete else 'coverage incomplete',headline_discovery_eligible='no: known prior EB' if known else 'catalogue scope only; physical verdict pending',chopard_track3_exact_gaia=bool(tr),chopard_dossier_exact_gaia=any(z.get('source_id')==g for z in dr),chopard_dossier_exact_tic=any(z.get('TIC')==tic for z in dr),chopard_embargo93_status='unknown: cannot establish embargoed identities')
 rows.append(r)
with (p/'coverage-matrix.csv').open('w',newline='',encoding='utf8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
(p/'chopard-exact-overlaps.json').write_text(json.dumps(overlap,indent=2))
assert len(rows)==40 and all(r['coverage_complete']=='yes' for r in rows)
print(collections.Counter(r['scoped_prior_eb_status'] for r in rows));print('known',[r['tic'] for r in rows if r['known_prior_eb_identification']!='[]']);print('Chopard',[(r['tic'],r['chopard_track3_exact_gaia'],r['chopard_dossier_exact_gaia'],r['chopard_dossier_exact_tic']) for r in rows if any(r[k] for k in ('chopard_track3_exact_gaia','chopard_dossier_exact_gaia','chopard_dossier_exact_tic'))])
manifest=[]
for f in sorted(p.rglob('*')):
 if f.is_file() and f.name!='sha256-manifest.csv' and f.suffix!='.log':manifest.append({'file':str(f.relative_to(p)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
with (p/'sha256-manifest.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=['file','sha256']);w.writeheader();w.writerows(manifest)
