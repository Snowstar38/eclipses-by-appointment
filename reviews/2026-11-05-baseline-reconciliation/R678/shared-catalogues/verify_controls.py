"""Fresh positive cone controls and hash/identity audit for the frozen queue."""
import csv
import hashlib
import io
import json
import urllib.parse
from pathlib import Path

import run_catalogues as c

HERE=Path(__file__).resolve().parent
OLD=Path('[local-path-redacted]')
queue=json.loads((HERE/'queue-lock.json').read_text())
c.QUEUE_HASH=queue['sha256']
controls=json.loads((OLD/'service-controls.json').read_text())
out=[]
for control in controls:
    table=control['table']
    if 'file' not in control: continue
    oldraw=(OLD/control['file']).read_bytes()
    assert c.sha(oldraw)==control['sha256'],f'old control hash mismatch: {table}'
    lines=[x for x in oldraw.decode('latin-1').splitlines() if x and not x.startswith('#')]
    header=[x.strip() for x in lines[0].split('\t')]
    source=dict(zip(header,[x.strip() for x in lines[3].split('\t')]))
    assert 'RAJ2000' in source and 'DEJ2000' in source
    params={'-source':table,'-c':source['RAJ2000']+' '+source['DEJ2000'],'-c.rs':60 if table in ('B/vsx/vsx','II/366/catv2021') else 5,'-out.max':100,'-out.all':'','-out.add':'_r'}
    label=next(l for l,t,_ in c.TABLES if t==table)
    rec,raw=c.cached_or_query('positive-control-'+label,c.VIZIER+'?'+urllib.parse.urlencode(params))
    expected_key='TIC' if 'TIC' in source else 'Name' if 'Name' in source else 'ASASSN-V'
    try:
        rows=c.parse_tsv(raw,table) if rec['status']=='success' else []
        assert any(x.get(expected_key,'').strip()==source[expected_key].strip() for x in rows), 'expected source absent'
        status='success'
    except Exception as exc:
        status='unavailable';rec['status']=status;rec['error']='positive-control: '+repr(exc)
        c.write_json(HERE/'receipts'/(rec['key']+'.json'),rec)
    out.append({'table':table,'status':status,'expected_key':expected_key,'expected_value':source[expected_key],'old_control_sha256':control['sha256'],'receipt':str(HERE/'receipts'/(rec['key']+'.json'))})

source_ids={x['gaia_dr3'] for x in queue['targets']}
raw=json.loads((HERE/'catalogue-results.json').read_text())
for r in raw:
    rec=json.loads((HERE/r['receipt']).read_text())
    assert rec['queue_sha256']==queue['sha256'] and rec['status']==r['status']
    assert c.sha((HERE/rec['file']).read_bytes())==rec['sha256']
    if r['catalogue']=='gaia_nss':
        assert {x['source_id'] for x in r['rows']}==source_ids
    elif r['catalogue']=='simbad':
        assert {x['id'].removeprefix('Gaia DR3 ') for x in r['rows']}==source_ids
    elif r['catalogue']=='gaia_eb':
        assert {x['source_id'] for x in r['rows']}<=source_ids

matrix=list(csv.DictReader((HERE/'coverage-matrix.csv').open(encoding='utf-8',newline='')))
assert {x['tic'] for x in matrix}=={x['tic'] for x in queue['targets']}
assert all(x['coverage_complete']=='True' for x in matrix)
audit={'queue_sha256':queue['sha256'],'targets':len(queue['targets']),'positive_controls':out,'positive_controls_success':sum(x['status']=='success' for x in out),'raw_receipts_verified':len(raw),'gaia_nss_full_rows':len(next(x for x in raw if x['catalogue']=='gaia_nss')['rows']),'matrix_rows':len(matrix)}
c.write_json(HERE/'verification.json',audit)
print(json.dumps({k:v for k,v in audit.items() if k!='positive_controls'}))
