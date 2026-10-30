"""Bounded archive mirror retries; no failed query is a null catalogue result."""
import archives as a
import concurrent.futures,json
jobs=[]
for tic,t in a.selected['targets'].items():
 ra,de=t['ra'],t['dec'];sid=t['gaia']['source_id'];cone=f"CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{de},{60/3600}))=1"
 q=f"SELECT main_id,otype,ra,dec FROM basic WHERE {cone}"
 jobs.append((tic,'simbad_harvard',lambda q=q:a.tap('https://simbad.cfa.harvard.edu/simbad/sim-tap/sync',q)))
 for table in ['vari_eclipsing_binary','vari_summary']:
  q=f'SELECT * FROM gaiadr3.{table} WHERE source_id={sid}'
  jobs.append((tic,'ari_'+table,lambda q=q:a.tap('https://gaia.ari.uni-heidelberg.de/tap/sync',q)))
 q=f'SELECT source_id,ra,dec,phot_g_mean_mag,bp_rp,phot_variable_flag,ruwe,ipd_frac_multi_peak,DISTANCE(POINT(\'ICRS\',ra,dec),POINT(\'ICRS\',{ra},{de}))*3600 AS sep FROM gaiadr3.gaia_source WHERE {cone} AND phot_g_mean_mag<17 ORDER BY phot_g_mean_mag'
 jobs.append((tic,'ari_neighbours',lambda q=q:a.tap('https://gaia.ari.uni-heidelberg.de/tap/sync',q)))
 q=f'SELECT Name,Type,Period FROM "B/vsx/vsx" WHERE CONTAINS(POINT(\'ICRS\',RAJ2000,DEJ2000),CIRCLE(\'ICRS\',{ra},{de},{60/3600}))=1'
 jobs.append((tic,'vsx_harvard_tap',lambda q=q:a.tap('https://tapvizier.cfa.harvard.edu/TAPVizieR/tap/sync',q)))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rows=list(ex.map(a.work,jobs))
(a.R/'mirror-query-log.json').write_text(json.dumps(rows,indent=2))
