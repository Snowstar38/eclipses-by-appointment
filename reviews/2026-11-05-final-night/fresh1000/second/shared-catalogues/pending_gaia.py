import csv,json,urllib.request,urllib.parse,concurrent.futures,hashlib,datetime,pathlib
w=pathlib.Path(__file__).parent;t=[x for x in json.load(open(w/'targets.json')) if x['scope']=='pending'];ids=[x['gaia'] for x in t]
jobs=[('gaia_'+lab,'https://gaia.ari.uni-heidelberg.de/tap/sync','SELECT * FROM gaiadr3.'+tb+' WHERE source_id IN ('+','.join(ids)+')') for lab,tb in [('eb','vari_eclipsing_binary'),('summary','vari_summary'),('nss','nss_two_body_orbit')]]
query='SELECT ident.id,basic.main_id,basic.otype,basic.ra,basic.dec FROM ident JOIN basic ON ident.oidref=basic.oid WHERE ident.id IN ('+','.join("\'Gaia DR3 "+x+"\'" for x in ids)+')';jobs.append(('simbad','https://simbad.cfa.harvard.edu/simbad/sim-tap/sync',query))
def run(j):
 name,url,q=j;body=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q}).encode();rec={'url':url,'query':q,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,data=body,headers={'User-Agent':'astronomy-audit/1.0'}),timeout=20).read(3000000); text=raw.decode('utf-8-sig');rows=list(csv.DictReader(text.splitlines())); assert text and ('source_id' in text.splitlines()[0].lower() if name!='simbad' else 'id' in text.splitlines()[0].lower());(w/(name+'-pending.csv')).write_bytes(raw);rec.update(status='success',rows=len(rows),sha256=hashlib.sha256(raw).hexdigest())
 except Exception as e:rec.update(status='unknown',error=repr(e))
 return name,rec
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:r=dict(ex.map(run,jobs))
(w/'pending-gaia-simbad-receipts.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))


