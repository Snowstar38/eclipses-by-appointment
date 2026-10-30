import json,pathlib,urllib.request
r=pathlib.Path(__file__).parent; d=json.loads((r.parent/'selected.json').read_text())
for tic,sec in [('295945076',34),('372376841',10)]:
 t=d['targets'][tic]; g=t['gaia'];url=f"https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra={g['ra']}&dec={g['dec']}&y=11&x=11&units=px&sector={sec}";p=r/'data'/f'{tic}_s{sec}_tesscut.zip'
 try:
  with urllib.request.urlopen(url,timeout=30) as f:b=f.read(40000001)
  if len(b)>40000000:raise Exception('size cap exceeded')
  p.write_bytes(b);print(tic,len(b))
 except Exception as e:print(tic,repr(e))
