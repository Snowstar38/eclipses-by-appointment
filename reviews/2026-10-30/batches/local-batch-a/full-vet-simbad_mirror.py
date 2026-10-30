import urllib.request,urllib.parse,json,pathlib,concurrent.futures,re
D=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-a\full-vet');T=json.loads((D.parent/'targets-selected.json').read_text())
def task(item):
 tic,t=item;id='Gaia DR3 '+t['gaia']['source_id'];q=f"SELECT b.main_id,b.otype,b.ra,b.dec FROM basic AS b JOIN ident AS i ON b.oid=i.oidref WHERE i.id='{id}'";u='https://simbad.cfa.harvard.edu/simbad/sim-tap/sync?'+urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q})
 try:
  with urllib.request.urlopen(u,timeout=20) as r:o=r.read().decode()
 except Exception as e:o='ERROR '+repr(e)
 (D/f'{tic}_simbad_mirror.csv').write_text(o)
 print(tic,repr(o[:300]),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as x:list(x.map(task,T.items()))
for p in D.glob('*_exofop.txt'):
 s=p.read_text(encoding='utf8');print(p.name,re.findall(r'<a href="#(?:tois|ctois)">[^<]*<span class="super">(\d+)',s))
