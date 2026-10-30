import csv,json,pathlib
P=pathlib.Path(r'C:\Home\Fable 5.1\made\paper\work\novelty-reconciliation'); E=P/'chopard-evidence'; base=next((E/'extracted').iterdir()); tmp=pathlib.Path(r'C:\Home\tmp\eba-astra-20261030')
def rows(p):
 with open(p,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
track=rows(base/'track3_detail.csv'); dossier=rows(base/'vetting/dossier.csv'); td={x['source_id']:x for x in track}; dg={x['source_id']:x for x in dossier}; dt={x['TIC']:x for x in dossier}; ticdata=json.loads((P.parent/'figs-other/tic_rows.json').read_text(encoding='utf-8')); targets={x['tic']:x for x in rows(tmp/'reviews/c9a-return/batch/targets.csv')}
identities={x['tic']:x.get('target_identity',{}).get('gaia_dr3','') for fn in ['r01-50.json','r51-70.json'] for x in json.loads((P/fn).read_text(encoding='utf-8'))['objects']}
ours=[]
for x in rows(P.parent.parent/'tables/objects.csv'):
 t=x['TIC']; ours.append(dict(group='A',label=x['label'],tic=t,gaia=str(ticdata.get(t,{}).get('GAIA') or ''),ra=x['RA'],dec=x['Dec']))
for x in rows(tmp/'reviewed-extension.csv'):
 if x['physical_verdict'].upper()!='CONFIRMED':continue
 t=x['tic']; path=tmp/'reviews/2026-10-30/evidence'/t/'gaia-nss.json'; g=str(json.loads(path.read_text())['source_id']) if path.exists() else identities.get(t,''); ours.append(dict(group='R',label=x['review_id'],tic=t,gaia=g,ra='',dec=''))
for x in rows(tmp/'returned-review.csv'):
 if x['count_addition'].lower()!='true' or x['physical_verdict'].upper()!='CONFIRMED':continue
 t=x['tic']; v=targets.get(t,{}); ours.append(dict(group='C',label=x['review_id'],tic=t,gaia=v.get('gaia_source_id',''),ra=v.get('tic_ra',''),dec=v.get('tic_dec','')))
for o in ours:
 g=o['gaia']; t=o['tic']; a=td.get(g); d=dg.get(g); d2=dt.get(t); o.update(track=bool(a),dossier_gaia=bool(d),dossier_tic=bool(d2),track_period=a['period'] if a else '',dossier_source=(d or d2 or {}).get('source_id',''))
with (P/'chopard-coverage.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=ours[0].keys());w.writeheader();w.writerows(ours)
for group in 'ARC':
 v=[x for x in ours if x['group']==group];print(group,len(v),'gaia',sum(bool(x['gaia']) for x in v),'track',[(x['label'],x['tic'],x['gaia']) for x in v if x['track']],'dossier',[(x['label'],x['tic']) for x in v if x['dossier_gaia'] or x['dossier_tic']])
print('track',len(track),'dossier',len(dossier)); print('missing',[(x['label'],x['tic']) for x in ours if not x['gaia']])

