import csv,json,pathlib,hashlib
w=pathlib.Path(__file__).parent; root=pathlib.Path('Astra/made'); targets=json.load(open(w/'target-results.json')); pending=[x for x in targets if x['scope']=='pending']; statuses={}; seals={}
for p in root.glob('binary-*/shared-catalogues/TARGET-STATUS.csv'):
 d=json.load(open(p.parent/'SHA256SUMS.json'));ok=d.get('files',d).get(p.name)==hashlib.sha256(p.read_bytes()).hexdigest();seals[str(p)]=ok
 if ok:
  for r in csv.DictReader(open(p,encoding='utf-8-sig',newline='')):statuses[r['tic']]=(r,str(p))
p=root/'binary-extension-2026-11-04/unmatched512/catalogue-recovery-full-primary/coverage-matrix.csv';d=json.load(open(p.parent/'SHA256SUMS.json')); ok=d.get('files',d).get(p.name)==hashlib.sha256(p.read_bytes()).hexdigest();seals[str(p)]=ok
if ok:
 for r in csv.DictReader(open(p,encoding='utf-8-sig',newline='')):
  if r['tic'] not in statuses:statuses[r['tic']]=(r,str(p))
(w/'historical-hash-checks.json').write_text(json.dumps(seals,indent=2))
rows=[]
for t in pending:
 tic=t['tic'];prev,path=statuses.get(tic,({},'')); row={'label':t['label'],'tic':tic,'historical_status_path':path,'historical_sha_verified':bool(path)}
 if 'catalogue_statuses' in prev:
  old=json.loads(prev['catalogue_statuses']); row.update({k:old.get(k,'unknown') for k in ['gaia_eb','gaia_summary','gaia_nss','simbad']});row.update(prsa='success' if old.get('prsa2022')=='success' else 'unknown',ijspeert='success' if old.get('ijspeert2024')=='success' else 'unknown',historical_prior=prev.get('exact_prior_eb_identifications','unknown'))
 else:
  row.update({k:prev.get(k,'unknown') for k in ['gaia_eb','gaia_summary','gaia_nss','simbad']});row['prsa']='success' if 'prsa_exact' in prev else 'unknown';row['ijspeert']='success' if 'ijspeert_exact' in prev else 'unknown';row['historical_prior']='PRSA exact='+prev.get('prsa_exact','unknown')+'; IJspeert exact='+prev.get('ijspeert_exact','unknown')+'; Gaia EB='+prev.get('gaia_eb','unknown')
 for k in ['vsx','asassn','table3','table4']:row[k]=t['catalogues'][k]['status']
 hits=[]
 for m in t['catalogues']['vsx']['matches']:
  if float(m['_r'])<3 and m.get('Type','').upper().startswith(('EA','EB','EW','E|','E:','E ')):hits.append(m['Name']+' '+m['Type']+' P='+m['Period']+' sep='+m['_r'])
 row['vsx_close_eb_alert']='; '.join(hits); row['toi']='fresh exact 969 query: no match';row['literature']='saved bounded 56-candidate gate' if not t['label'].startswith('R7') else 'unknown: verify prior literature coverage';row['kepler']='saved 1105 footprint check; current CAOM timed out' if tic in json.load(open('Fable 5.1/made/gate-xm/positions-1105.json')) else 'unknown: absent old 969 input; current CAOM timed out'
 rows.append(row)
with open(w/'pending-gate-matrix.csv','w',encoding='utf8',newline='') as f: z=csv.DictWriter(f,fieldnames=list(rows[0]));z.writeheader();z.writerows(rows)
print('rows',len(rows),'historic',sum(x['historical_sha_verified'] for x in rows),'alerts',[(x['label'],x['vsx_close_eb_alert']) for x in rows if x['vsx_close_eb_alert']]);print('unknown legacy',[(x['label'],x['gaia_eb'],x['prsa'],x['ijspeert']) for x in rows if 'unknown' in [x['gaia_eb'],x['prsa'],x['ijspeert']]])
