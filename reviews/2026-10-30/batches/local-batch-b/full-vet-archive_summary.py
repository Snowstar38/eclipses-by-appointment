"""Compact adjudication of attempted archive gates, not novelty by failed query."""
import pathlib,csv,json,hashlib,datetime
R=pathlib.Path(__file__).parent;d=json.loads((R.parent/'selected.json').read_text());out=[]
for tic,t in d['targets'].items():
 ex=json.loads((R/f'{tic}_exofop.txt').read_text());sb=list(csv.DictReader((R/f'{tic}_simbad_harvard.txt').open()));nb=list(csv.DictReader((R/f'{tic}_ari_neighbours.txt').open()));target=min(sb,key=lambda x:(float(x['ra'])-t['ra'])**2+(float(x['dec'])-t['dec'])**2)
 out.append(dict(tic=tic,name=target['main_id'],simbad_type=target['otype'],simbad_cone_rows=len(sb),exofop_tois=len(ex['tois']),exofop_ctois=len(ex['ctois']),neighbours_G17_in60arcsec=len(nb)-1,gaia_eb='none in successful shared70 source query',gaia_vari_summary='see successful shared query',vsx='successful shared VSX70 IDIA receipts; no target match;372 neighbour58arcsec E',asas_sn='successful IDIA II/366; no rows',sb9='successful IDIA B/sb9/main; no rows',wds='successful IDIA B/wds/wds; no rows',eb_tables='successful IDIA; vetted tables no rows; Kostov unvetted table2 entries separate',web_names='fresh exact TIC and main-name searches: no relevant hits',novelty='no target eclipsing classification in successfully queried vetted sources; unvetted flags not prior confirmation'))
with (R/'archive-summary.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
paths=list(R.glob('*.txt'))+list(R.glob('*query-log.json'))+[R/'archive-outage.md',R/'web-search-log.md',R/'mirror-probes.json']
manifest=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths if p.exists()]
(R/'archive-response-hashes.json').write_text(json.dumps(dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=manifest),indent=2))
print('archive adjudication rows',len(out),'hashed responses',len(manifest))
