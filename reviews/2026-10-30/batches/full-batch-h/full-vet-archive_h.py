from pathlib import Path
import json,csv,urllib.request,urllib.parse,hashlib,datetime
F=Path('C:/Home/Astra/made/binary-handoff-2026-10-30/full-batch-h/full-vet'); S=F.parent.parent/'shared-full-review';T=json.load(open(F.parent/'targets-selected.json'))
tables=['B/vsx/vsx','II/366','B/sb9/main','B/wds/wds','J/ApJS/279/50/table2','J/ApJS/279/50/table3','J/ApJS/279/50/table4','J/A+A/691/A242/obaf-eb1','J/ApJS/258/16/tess-ebs']
tic=next(iter(T));t=T[tic];url='https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?'+urllib.parse.urlencode({'-source':','.join(tables),'-c':f"{t['ra']} {t['dec']}",'-c.rs':60,'-out.max':100,'-out.all':'','-out.add':'_r'})
r={'tic':tic,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'policy':'one bounded mirror probe after batch G all IDIA9 timeouts'}
try:
 with urllib.request.urlopen(url,timeout=25) as h:b=h.read(2000000)
 (F/'catalogue-mirror-probe.tsv').write_bytes(b);r.update(status='received',sha256=hashlib.sha256(b).hexdigest(),sections=[x for x in b.decode('latin1').splitlines() if x.startswith('#Table')])
except Exception as e:r.update(status='unavailable',error=repr(e))
json.dump(r,open(F/'catalogue-mirror-probe.json','w'),indent=2)
out={}
for tic,t in T.items():
 sid=str(t['gaia']['source_id']);ex=S/'exofop'/(tic+'.json')
 try:
  j=json.load(open(ex));es={'toi_count':len(j['tois']),'ctoi_count':len(j['ctois'])}
 except Exception as e:es={'error':repr(e)}
 out[tic]={'simbad':[x for x in csv.DictReader(open(S/'simbad-targets.csv')) if sid in x['id']], 'gaia_vari_summary':[x for x in csv.DictReader(open(S/'gaia-vari_summary.csv')) if x['source_id']==sid], 'gaia_eb':[x for x in csv.DictReader(open(S/'gaia-vari_eclipsing_binary.csv')) if x['source_id']==sid], 'exofop':es,'shared_receipts':[]}
 for p in [S/'vsx'/(tic+'.tsv'),ex]:
  out[tic]['shared_receipts'].append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
json.dump(out,open(F/'archive-shared-gates.json','w'),indent=2);print(r);print(json.dumps(out,indent=2))
