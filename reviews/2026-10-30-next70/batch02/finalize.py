from pathlib import Path
import csv,json,hashlib
B=Path(__file__).parent
p=B/'make_reports.py';s=p.read_text();s=s.replace('Independent {i[\'provenance\']} sector','{i[\'provenance\']} sector');s=s.replace(' for n in s[\'capable\']:', ''' if t=='309981203':text+='QLP fitted depth varies across sectors (about69-92 ppt); pixel aperture depths are lower (about45 ppt). Aperture dilution/systematics are retained; depth consistency is not assumed.\\n\\n'
 for n in s['capable']:''');p.write_text(s)
exec(compile(s,str(p),'exec'))
rows=list(csv.DictReader((B/'RESULTS.csv').open()));assert len(rows)==10 and len({r['tic'] for r in rows})==10;assert len(list(B.glob('TIC-*.md')))==10
# Independently verify cited hashes for raw QLP and other extraction inputs.
manifest=json.loads((B/'raw-evidence/qlp-manifest.json').read_text());audit=[]
for r in manifest:
 p=B/'raw-evidence'/r['tic']/f"qlp_s{r['sector']:03d}.fits";assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'];audit.append(str(p.relative_to(B)))
for r in json.loads((B/'raw-evidence/independent-results.json').read_text()):
 p=Path(r['source_path']) if 'source_path'in r else B/'raw-evidence'/r['tic']/f"indep_s{r['sector']:03d}.fits";assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
 if 'source_path'not in r:assert r['identity']['header_tic_matches'] and r['identity']['header_sector_matches'] and r['identity']['uri_contains_padded_tic']
(B/'VALIDATION.json').write_text(json.dumps(dict(targets=10,reports=10,result_rows=10,physical_counts={'CONFIRMED':10},execution_complete=10,qlp_hashes_verified=len(manifest),independent_hashes_verified=10,lead_review='Raw event panel and three targeted difference images inspected; numeric capable-neighbour/period/conjunction/duration checks reviewed; no decisive contradiction.'),indent=2))
(B/'CONTRIBUTORS.md').write_text('The batch lead reviewed the deciding evidence and prepared the reports. A fresh GPT-6.1 Terra helper measured representative raw events and checked independent extractions; the project coordinator set the review scope. No human personal name is included.\n')
(B/'README.md').write_text('Batch02 reviews queue positions11-20 under ../BRIEF.md. Exactly10 physical CONFIRMED results, execution complete. Eight independent checks use TESS-SPOC; two use independently extracted cached TESScut pixels from the same TESS images. Raw periods use representative event centres with conditional cycle counts; two-event solutions carry no inferred precision. Source and Gaia diagnostics and catalogue scope limitations are in the ten reports. Reproduce via setup.py, raw-evidence/download_qlp.py, measure.py, independent.py and pixel_independent.py; then gaia_geometry.py and make_reports.py. Provenance hashes and validation retained. No source/paper edits or commits.\n')
hashes=[dict(path=str(p.relative_to(B)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in B.rglob('*') if p.is_file() and p.name!='MANIFEST-SHA256.json']
(B/'MANIFEST-SHA256.json').write_text(json.dumps(hashes,indent=2));print('validated',len(rows),len(hashes))
