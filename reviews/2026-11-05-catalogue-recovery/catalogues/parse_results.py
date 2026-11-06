import pathlib,csv,json,math,hashlib
w=pathlib.Path(__file__).parent;targets=json.load(open(w/'targets.json'));receipts=json.load(open(w/'cone-receipts.json'));lookup={(x['catalogue'],x['tic']):x for x in receipts}
def parse(p):
 lines=[x for x in p.read_text(encoding='utf-8-sig').splitlines() if x and not x.startswith('#')]
 if not lines:return []
 assert len(lines)>=3
 return [dict(zip(lines[0].split('\t'),[x.strip() for x in l.split('\t')])) for l in lines[3:]]
def sep(a,b,c,d):
 a,b,c,d=map(math.radians,(a,b,c,d));h=math.sin((b-d)/2)**2+math.cos(b)*math.cos(d)*math.sin((a-c)/2)**2;return math.degrees(2*math.asin(min(1,math.sqrt(h))))*3600
bulk={k:parse(w/(k+'-bulk.tsv')) for k in ('table3','table4')}; print('bulk rows',[(k,len(v)) for k,v in bulk.items()]); result=[]
for t in targets:
 record={'tic':t['tic'],'label':t['label'],'scope':t['scope'],'ra':t['ra'],'dec':t['dec'],'catalogues':{}}
 for key in ('vsx','asassn'):
  rec=lookup.get((key,t['tic']),{'status':'unknown'}); hits=parse(pathlib.Path(rec['file'])) if rec['status']=='success' else [];record['catalogues'][key]={'status':rec['status'],'matches':hits,'receipt':rec.get('file')}
 for key,rows in bulk.items():
  near=[]
  for r in rows:
   d=sep(float(t['ra']),float(t['dec']),float(r['RAJ2000']),float(r['DEJ2000']))
   if d<=60 or r['TIC'].strip()==t['tic']: near.append({'separation_arcsec':round(d,3),'row':r})
  record['catalogues'][key]={'status':'success','matches':near,'bulk_sha256':hashlib.sha256((w/(key+'-bulk.tsv')).read_bytes()).hexdigest()}
 result.append(record)
(w/'target-results.json').write_text(json.dumps(result,indent=2));
for t in result:
 findings=[]
 for k,v in t['catalogues'].items():
  for m in v['matches']:
   r=m.get('row',m);dist=m.get('separation_arcsec',r.get('_r'));tic=r.get('TIC','').strip();gaia=r.get('GaiaDR3','').strip();
   if (tic==t['tic'] or (gaia and gaia==next(x['gaia'] for x in targets if x['tic']==t['tic'])) or (dist not in (None,'') and float(dist)<3)):
    findings.append((k,dist,r.get('Type',r.get('Vartype','')),r.get('ASASSN-V',r.get('Name','')),tic,gaia))
 if findings: print(t['label'],t['tic'],findings)
