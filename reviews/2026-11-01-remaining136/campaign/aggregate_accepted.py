"""Freeze this campaign's exact accepted scientific outcomes; never count reservations."""
import csv,json,hashlib
from pathlib import Path
from collections import Counter
W=Path(__file__).resolve().parent
rows=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
q=rows(W/'queue.csv');b=json.loads((W/'baseline.json').read_text())
assert sha(W/'queue.csv')==b['queue_sha256']
accepted=json.loads((W/'accepted-batches.json').read_text())
cats={r['tic']:r for r in rows(W/'shared-catalogues/coverage-matrix.csv')}
targets=json.loads((W/'targets-selected.json').read_text());found={}
for name in b['batch_counts']:
 a=accepted[name];assert a['accepted']
 assert sha(W/name/'RESULTS.csv')==a['results_sha256']
 assert sha(W/name/'SHA256SUMS.json')==a['manifest_sha256']
 rr=rows(W/name/'RESULTS.csv');expected=rows(W/name/'queue.csv')
 assert len(rr)==len(expected)==len({r['tic'] for r in rr})
 assert {r['tic'] for r in rr}=={r['tic'] for r in expected}
 for r in rr:
  assert r['tic'] not in found
  assert r['full_review_completion'].upper().startswith('COMPLETE')
  r['physical_verdict']=r['physical_verdict'].upper()
  rp=Path(r['report']);rp=rp if rp.is_absolute() else W/name/rp
  assert rp.is_file();r['report']=str(rp.resolve());found[r['tic']]=r
out=[]
for i,item in enumerate(q,540):
 r=found[item['tic']];c=cats[item['tic']]
 eligible=c['coverage_complete']=='yes' and c['scoped_prior_eb_status']=='no identified prior EB'
 r.update(review_id=f'R{i:03d}',batch=f"batch{int(item['batch']):02d}",search_method='Gaia spectroscopic-orbit period fold',population='G '+item['magnitude_group']+' spectroscopic-orbit population',magnitude_group=item['magnitude_group'],inventory_g=item['inventory_gaia_g'],gaia_g=targets[item['tic']]['gaia']['phot_g_mean_mag'],novelty_status=c['scoped_prior_eb_status'],count_addition=str(eligible and r['physical_verdict'] in ('CONFIRMED','PROBABLE')).lower(),full_review_completion='COMPLETE_BOUNDED_REVIEW')
 out.append(r)
assert len(out)==136
fields=list(dict.fromkeys(k for r in out for k in r))
with (W/'FULL-RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
 writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(out)
c=Counter(r['physical_verdict'] for r in out if r['count_addition']=='true');base=b['baseline']
summary={'reviewed':len(out),'outcomes':dict(Counter(r['physical_verdict'] for r in out)),'additions':sum(c.values()),'confirmed_additions':c['CONFIRMED'],'probable_additions':c['PROBABLE'],'physical':base['systems']+sum(c.values()),'confirmed':base['confirmed']+c['CONFIRMED'],'probable':base['probable']+c['PROBABLE'],'total_review_rows':base['reviews']+len(out),'remaining_screened':0,'methods':{'conjunction_windows':base['appointments'],'period_folds':base['period_folds']+sum(c.values()),'M_dwarf_selected':base['m_dwarfs'],'astrometric':base['astrometric']},'catalogue_incomplete':[r['tic'] for r in out if cats[r['tic']]['coverage_complete']!='yes'],'excluded':[{'tic':r['tic'],'physical_verdict':r['physical_verdict'],'novelty_status':r['novelty_status']} for r in out if r['count_addition']!='true']}
(W/'accepted-counts.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
