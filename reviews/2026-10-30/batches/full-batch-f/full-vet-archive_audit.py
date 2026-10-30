from pathlib import Path
import csv,json,urllib.request,hashlib,datetime
F=Path(__file__).parent;D=F.parent;S=D.parent/'shared-full-review';T=json.load(open(D/'targets-selected.json'))
out={};cats={};neighbors={}
for tic,t in T.items():
 sections={};section=None;header=None;stage=0
 for line in (F/(tic+'_idia.tsv')).read_text(encoding='latin1').splitlines():
  if line.startswith('#Table'):
   section=line.split('\t')[1].rstrip(':');sections[section]=[];header=None;stage=0
  elif line and not line.startswith('#') and section:
   a=[x.strip() for x in line.split('\t')]
   if header is None:header=a;stage=1
   elif stage==1:stage=2
   elif stage==2:stage=3
   else: sections[section].append(dict(zip(header,a)))
 assert len(sections)==9
 cats[tic]=sections
 sid=t['gaia']['source_id'];simb=[r for r in csv.DictReader(open(S/'simbad-targets.csv')) if sid in r['id']]
 vs=[r for r in csv.DictReader(open(S/'gaia-vari_summary.csv')) if r['source_id']==sid]
 eb=[r for r in csv.DictReader(open(S/'gaia-vari_eclipsing_binary.csv')) if r['source_id']==sid]
 ex=S/'exofop'/(tic+'.json')
 if tic=='349273287':
  url=f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}&json';receipt={'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  try:
   with urllib.request.urlopen(url,timeout=40) as r:raw=r.read(1000000)
   ex=F/(tic+'_exofop.json');ex.write_bytes(raw);j=json.loads(raw);receipt.update(status='success',sha256=hashlib.sha256(raw).hexdigest(),toi_count=len(j['tois']),ctoi_count=len(j['ctois']))
  except Exception as e:receipt.update(status='unavailable',error=repr(e))
  json.dump(receipt,open(F/'exofop-retry-receipt.json','w'),indent=2)
 try:j=json.load(open(ex));exsum={'toi_count':len(j['tois']),'ctoi_count':len(j['ctois'])}
 except Exception as e:exsum={'error':repr(e)}
 out[tic]=dict(simbad=simb,gaia_vari_summary=vs,gaia_eb=eb,exofop=exsum,catalog_counts={k:len(v) for k,v in sections.items()})
 fitpath=F/tic/'fit-results.json'; search={str(r['tic']):r for r in json.load(open(D/'receipts.json'))['search.jsonl']}; depth=__import__('numpy').median([r['depth'] for r in json.load(open(fitpath))['events'] if r['status']=='fit']) if fitpath.exists() else search[tic]['P']['depth']/1e6
 n=[]
 for r in csv.DictReader(open(F/(tic+'_neighbors_ari.csv'))):
  if r['source_id']==sid:continue
  req=float(depth)*10**(.4*(float(r['phot_g_mean_mag'])-float(t['gaia']['phot_g_mean_mag'])));n.append(dict(**r,required_fraction_G_approx=req,capable=req<=1))
 neighbors[tic]=n
 print(tic,'cats',out[tic]['catalog_counts'],'simbad',simb,'gaiaEB',len(eb),'exofop',exsum,'capable',[(r['sep'],r['phot_g_mean_mag']) for r in n if r['capable']])
json.dump(cats,open(F/'catalogue-rows.json','w'),indent=2)
json.dump(out,open(F/'archive-shared-gates.json','w'),indent=2)
json.dump(neighbors,open(F/'neighbors-summary.json','w'),indent=2)

