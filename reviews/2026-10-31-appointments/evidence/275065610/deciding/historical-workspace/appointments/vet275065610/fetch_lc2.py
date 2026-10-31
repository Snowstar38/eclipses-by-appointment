r"""Download light-curve FITS for the archives.json rows of chosen pipelines into %TEMP%\vet-a8a11\<tic>\.
python -X utf8 fetch_lc.py <tic> <prov1,prov2> [sectors comma list]   (data only; never executed)"""
import json, os, sys, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
tic, provs = sys.argv[1], sys.argv[2].split(',')
secs = [int(s) for s in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
C = '[local path omitted]' + tic; os.makedirs(C, exist_ok=True)
rows = json.load(open(os.path.join(HERE, 'archives.json')))
def mast(req):
    d = urllib.parse.urlencode({'request': json.dumps(req)}).encode()
    for k in range(2):
        try: return json.loads(urllib.request.urlopen('http[local path omitted]', d, timeout=300).read())
        except Exception as e: print('retry', e)
    raise SystemExit('MAST failed twice')
for r in rows:
    if r['prov'] not in provs or (secs and int(r['seq']) not in secs): continue
    pass
    pr = mast({'service': 'Mast.Caom.Products', 'params': {'obsid': r['obsid']}, 'format': 'json'})['data']
    for p in pr:
        fn = p['productFilename']
        if not (fn.endswith('lc.fits') or fn.endswith('llc.fits') or (r['prov'] == 'TARS' and fn.endswith('.fits'))): continue
        if 'fast' in fn: continue
        dst = os.path.join(C, fn)
        if os.path.exists(dst): print('have', fn); continue
        u = 'http[local path omitted]' + urllib.parse.quote(p['dataURI'])
        for k in range(2):
            try: open(dst, 'wb').write(urllib.request.urlopen(u, timeout=600).read()); print('got', fn, os.path.getsize(dst)); break
            except Exception as e: print('retry', fn, e)
