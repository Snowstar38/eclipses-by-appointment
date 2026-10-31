import urllib.request,urllib.parse,pathlib,json,concurrent.futures
O=pathlib.Path(__file__).parent
t=json.load(open('[local path omitted] 5/made/sb1-scale/targets.json'));t.update(json.load(open(O/'fresh-targets-48.json')))
def one(k):
 v=t[k];u='http[local path omitted]'+urllib.parse.urlencode({'-source':'I/357/tbosb1','-c':str(v['ra'])+' '+str(v['dec']),'-c.rs':5,'-out.all':'','-out.max':10})
 try:
  raw=urllib.request.urlopen(u,timeout=25).read();(O/k/'nss-vizier.tsv').write_bytes(raw);s=raw.decode('latin1');lines=[l for l in s.splitlines() if l and not l.startswith('#')];head=[x.strip() for x in lines[0].split('\t')];rows=[dict(zip(head,[x.strip() for x in l.split('\t')])) for l in lines[3:]];(O/k/'nss-vizier.json').write_text(json.dumps(rows,indent=1));print(k,rows,flush=True)
 except Exception as e:print(k,repr(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(3) as ex:list(ex.map(one,['167178300','325573958','155303130']))
