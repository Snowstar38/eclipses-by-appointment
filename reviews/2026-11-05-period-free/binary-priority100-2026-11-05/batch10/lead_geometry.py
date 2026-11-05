"""Recompute Gaia conjunction geometry/covariance with batch08 audited code."""
from pathlib import Path
B=Path(__file__).resolve().parent
for name in ('lead_gaia_geometry.py','lead_gaia_covariance.py'):
 src=B.parent/'batch08'/name
 code=src.read_text(encoding='utf-8')
 if name=='lead_gaia_geometry.py':
  code=code.replace("p=B.parent/'source-packets'/r['tic']/'sources.json';s=", "p=B.parent/'source-packets'/r['tic']/'sources.json';s=")
  code=code.replace("P=float(g['period']);e=", "P=float(g['period']);\n if not g['arg_periastron']:\n  out.append({'sample_id':r['sample_id'],'tic':r['tic'],'status':'AstroSpectroSB1 omega absent from cached table; edge-on conjunction unavailable'});continue\n e=")
 else:
  code=code.replace("rows={r['source_id']:r for r in csv.DictReader(p.open())}","rows={};\nfor r in csv.DictReader(p.open()):rows.setdefault(r['source_id'],[]).append(r)")
  code=code.replace("r=rows[g['source_id']];assert", "r=next(z for z in rows[g['source_id']] if z['nss_solution_type']==g['nss_solution_type'] and abs(float(z['period'])-float(g['period']))<1e-8);assert")
  code=code.replace("s=json.loads((B.parent/'source-packets'/x['tic']/'sources.json').read_text());g=", "\n if 'closest' not in [local-path-redacted]  out.append(x);continue\n s=json.loads((B.parent/'source-packets'/x['tic']/'sources.json').read_text());g=")
 exec(compile(code,str(src),'exec'),{'__file__':str(B/name),'__name__':'__main__'})
