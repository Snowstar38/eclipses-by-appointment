"""List MAST products for the SPOC multi-sector (DV) observations of the target; fetch the DV summary/xml.
python -X utf8 dvlist.py"""
import json, os, urllib.parse, urllib.request
rows = json.load(open('archives.json')); C = '[local path omitted]'; os.makedirs(C, exist_ok=True)
def mast(req):
    d = urllib.parse.urlencode({'request': json.dumps(req)}).encode()
    return json.loads(urllib.request.urlopen('http[local path omitted]', d, timeout=300).read())
for r in rows:
    if r['prov'] != 'SPOC': continue
    pr = mast({'service': 'Mast.Caom.Products', 'params': {'obsid': r['obsid']}, 'format': 'json'})['data']
    print(r['obs_id'])
    for p in pr:
        fn = p['productFilename']
        if 'dv' in fn or 'tce' in fn.lower():
            print('   ', fn, p['description'])
            if fn.endswith('.xml') or fn.endswith('dvs.pdf') or fn.endswith('dvm.pdf'):
                dst = os.path.join(C, fn)
                if not os.path.exists(dst):
                    open(dst, 'wb').write(urllib.request.urlopen('http[local path omitted]' + urllib.parse.quote(p['dataURI']), timeout=600).read())
