"""MAST lookup (CAOM cone, 10"): every TESS / HLSP light-curve observation of the target, by pipeline.
python -X utf8 archives.py <tic> <ra> <dec> <outdir>   -> <outdir>/archives.json"""
import json, os, sys, urllib.parse, urllib.request
tic, ra, de, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
def mast(req):
    d = urllib.parse.urlencode({'request': json.dumps(req)}).encode()
    for k in range(2):
        try: return json.loads(urllib.request.urlopen('http[local path omitted]', d, timeout=300).read())
        except Exception as e: print('retry', e)
    raise SystemExit('MAST failed twice')
r = mast({'service': 'Mast.Caom.Cone', 'params': {'ra': ra, 'dec': de, 'radius': 10 / 3600},
          'format': 'json', 'pagesize': 5000})
rows = [dict(coll=x['obs_collection'], prov=x['provenance_name'], target=x['target_name'], seq=x['sequence_number'],
             obsid=x['obsid'], texp=x['t_exptime'], dp=x['dataproduct_type'], obs_id=x['obs_id'])
        for x in r['data'] if x['obs_collection'] in ('TESS', 'HLSP') and str(tic) in str(x['target_name']) + str(x['obs_id'])]
rows.sort(key=lambda r: (str(r['prov']), r['seq'] or 0))
for x in rows: print(x['coll'], x['prov'], x['seq'], x['texp'], x['obs_id'])
json.dump(rows, open(os.path.join(out, 'archives.json'), 'w'), indent=1)
