import pathlib,json,urllib.request,concurrent.futures
r=pathlib.Path(__file__).parent; out=r/'data';out.mkdir(exist_ok=True);(out/'.gitignore').write_text('*\n!.gitignore\n')
def one(t):
 d=json.loads((r/f'{t}_mast_pipelines.txt').read_text())['data']; q=[x for x in d if x['provenance_name']=='TESS-SPOC'] or [x for x in d if x['provenance_name']=='TARS']
 if not q:return (t,'no listed product')
 x=q[0]; url='https://mast.stsci.edu/api/v0.1/Download/file?uri='+x['dataURL']; path=out/f"{t}_{x['provenance_name']}_s{x['sequence_number']}.fits"
 try:
  with urllib.request.urlopen(url,timeout=30) as f:
   b=f.read(40000001)
  if len(b)>40000000: return (t,'over 40 MB cap')
  path.write_bytes(b);return (t,str(path),len(b))
 except Exception as e:return (t,repr(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: print(list(ex.map(one,['295945076','372376841','416525506','451493289','348737250'])))
