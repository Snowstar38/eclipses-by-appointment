"""Queue-locked, resumable public catalogue screening for the November 3 campaign."""
import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import re
import tarfile
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
VIZIER = 'https://vizier.cfa.harvard.edu/viz-bin/asu-tsv'
GAIA = 'https://gaia.ari.uni-heidelberg.de/tap/sync'
SIMBAD = 'https://simbad.cfa.harvard.edu/simbad/sim-tap/sync'
TABLES = [('vsx', 'B/vsx/vsx', 60), ('asassn', 'II/366/catv2021', 60),
          ('prsa2022', 'J/ApJS/258/16/tess-ebs', 5),
          ('ijspeert2024', 'J/A+A/691/A242/obaf-eb1', 5),
          ('kostov2025_table3', 'J/ApJS/279/50/table3', 5),
          ('kostov2025_table4', 'J/ApJS/279/50/table4', 5)]
CHOPARD = Path('[local-path-redacted] 5.1/made/paper/work/novelty-reconciliation/chopard-evidence/extracted/gaia-dr3-edge-on-orbits-tess-eclipses-v1.2.0')
HEARTBEATS = Path(os.environ.get('TEMP', '[local-path-redacted]')) / 'heartbeats/vet365670788/arxiv'
PAPERS = {'2506.14869': 'Callahan+2025', '2608.12474': 'Callahan+2026',
          '2407.18621': 'Li+2024a', '2408.01019': 'Li+2024b',
          '2508.01156': 'Li+2025', '2505.04067': 'Li+2025rnn',
          '2407.14421': 'Solanki+2025', '2012.11559': 'Kolaczek-Szymanski+2021',
          '2109.14616': 'Wrona+2022'}

def sha(raw): return hashlib.sha256(raw).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()
def write_json(path, value): path.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding='utf-8')

def pick(row, *names):
    norm = {re.sub('[^a-z0-9]', '', str(k).lower()): v for k, v in row.items()}
    for name in names:
        v = norm.get(re.sub('[^a-z0-9]', '', name.lower()))
        if v is not None and str(v).strip(): return v
    return None

def load_queue(path):
    if path.suffix.lower() == '.csv':
        rows = list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))
    else:
        obj = json.loads(path.read_text(encoding='utf-8-sig'))
        rows = list(obj.values()) if isinstance(obj, dict) else obj
        if isinstance(obj, dict):
            rows = [dict(v, tic=k) if isinstance(v, dict) else {'tic': k} for k, v in obj.items()]
    assert isinstance(rows, list) and rows, 'empty queue'
    out = []
    for r in rows:
        tic = str(pick(r, 'tic', 'tic_id', 'ticid', 'TIC ID') or '').removeprefix('TIC ').strip()
        gobj = r.get('gaia') if isinstance(r.get('gaia'), dict) else {}
        gaia = str(pick(r, 'gaia_dr3', 'gaia_source_id', 'source_id', 'gaia_dr3_source_id') or gobj.get('source_id') or '').removeprefix('Gaia DR3 ').strip()
        ra = pick(r, 'ra', 'ra_deg', 'ra_degrees')
        dec = pick(r, 'dec', 'dec_deg', 'dec_degrees')
        if ra is None or dec is None:
            coords = r.get('coordinates') if isinstance(r.get('coordinates'), dict) else {}
            ra, dec = ra or coords.get('ra'), dec or coords.get('dec')
        assert tic.isdigit() and gaia.isdigit(), f'missing TIC/Gaia identity: {r}'
        ra, dec = float(ra), float(dec)
        assert 0 <= ra < 360 and -90 <= dec <= 90, f'bad coordinates for {tic}'
        out.append(dict(tic=tic, gaia_dr3=gaia, ra=ra, dec=dec))
    assert len({r['tic'] for r in out}) == len(out), 'duplicate TIC'
    assert len({r['gaia_dr3'] for r in out}) == len(out), 'duplicate Gaia DR3 source ID'
    return out

def cached_or_query(key, url, body=None, limit=1000000):
    dest = HERE / 'raw' / (key + '.txt')
    receipt = HERE / 'receipts' / (key + '.json')
    dest.parent.mkdir(exist_ok=True); receipt.parent.mkdir(exist_ok=True)
    prior = json.loads(receipt.read_text()) if receipt.exists() else {}
    if os.environ.get('ASTRA_REUSE_FAILED_RECEIPTS') == '1' and prior.get('queue_sha256') == QUEUE_HASH and prior.get('url') == url and prior.get('body') == body and prior.get('status') == 'unavailable':
        return prior, b''
    if prior.get('queue_sha256') == QUEUE_HASH and prior.get('url') == url and prior.get('body') == body and prior.get('status') == 'success' and dest.exists() and sha(dest.read_bytes()) == prior.get('sha256'):
        return prior, dest.read_bytes()
    r = {'key': key, 'queue_sha256': QUEUE_HASH, 'url': url, 'body': body, 'queried_at_utc': now()}
    try:
        req = urllib.request.Request(url, data=body.encode() if body else None, headers={'User-Agent': 'Astra-EB-catalogue-screen/1.0'})
        with urllib.request.urlopen(req, timeout=8) as response: raw = response.read(limit + 1)
        assert len(raw) <= limit, 'response exceeds limit'
        s = raw.decode('latin-1')
        assert '<html' not in s.lower() and '#ERROR' not in s and 'QUERY_STATUS=ERROR' not in s, 'service error'
        dest.write_bytes(raw)
        r.update(status='success', sha256=sha(raw), file=str(dest.relative_to(HERE)), bytes=len(raw))
    except Exception as exc:
        raw = b''; r.update(status='unavailable', error=repr(exc))
    write_json(receipt, r)
    time.sleep(0.25)
    return r, raw

def parse_tsv(raw, table):
    s = raw.decode('latin-1')
    assert 'VizieR' in s and table in s, 'unexpected VizieR response'
    lines = [x for x in s.splitlines() if x and not x.startswith('#')]
    if not lines:
        assert 'No object found' in s or '#INFO' in s, 'empty response unclear'
        return []
    h = [x.strip() for x in lines[0].split('\t')]
    assert '_r' in h and len(lines) >= 3, 'unknown VizieR layout'
    rows = [dict(zip(h, [v.strip() for v in line.split('\t')])) for line in lines[3:]]
    assert len(rows) < 100, 'possible truncated cone'
    return rows

def texts_of(path):
    raw = path.read_bytes(); texts = {}
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode='r:*') as archive:
            for m in archive.getmembers():
                if m.isfile() and not re.search(r'\.(png|jpe?g|pdf|eps|ps|gif)$', m.name, re.I):
                    texts[m.name] = archive.extractfile(m).read().decode('latin-1')
    except tarfile.TarError:
        try: texts['main'] = gzip.decompress(raw).decode('latin-1')
        except OSError: texts['main'] = raw.decode('latin-1')
    return texts

def heartbeat(rows):
    claims = {r['tic'] for r in rows}; out = {'scope': 'exact TIC-number token in nine locally cached arXiv sources; OGLE/KIC-only identities not cleared', 'sources': [], 'targets': {t: [] for t in sorted(claims)}}
    for aid, name in PAPERS.items():
        path = HEARTBEATS / (aid + '.src')
        assert path.is_file(), f'missing cached heartbeat source {path}'
        texts = texts_of(path)
        src = {'paper': name, 'arxiv': aid, 'path': str(path), 'sha256': sha(path.read_bytes()), 'files': len(texts)}
        if aid == '2506.14869':
            tx = texts['ANC/SBTABLE.full.tex']
            matches = re.findall(r'^(\d{3,12})\s+(SB[12])\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(True|False)\s+(True|False)\s+(True|False|--)', tx, re.M)
            assert len(matches) == 112 and len({m[0] for m in matches}) == 112, 'Callahan table parse changed'
            src['parsed_rows'] = 112
            for m in matches:
                if m[0] in claims:
                    out['targets'][m[0]].append({'paper': name, 'table': 'ANC/SBTABLE.full.tex', 'SB': m[1], 'period_days': m[5], 'match_flag': m[11], 'eclipses_flag': m[12], 'TEOs_flag': m[13], 'interpretation': 'prior eclipse alert' if m[12] == 'True' else 'no eclipse flag; does not refute current photometry'})
        else:
            ids = set()
            for tx in texts.values(): ids.update(re.findall(r'(?<!\d)\d{5,12}(?!\d)', tx))
            for tic in claims & ids: out['targets'][tic].append({'paper': name, 'match': 'exact TIC-number token; identity/context needs review'})
        out['sources'].append(src)
    write_json(HERE / 'heartbeat-overlaps.json', out)
    return out

def chopard(rows):
    out = {'scope': 'cached public Chopard v1.2.0 only; later releases not searched; embargoed identities unknown', 'sources': [], 'targets': {r['tic']: [] for r in rows}}
    for name in ('track3_detail.csv', 'vetting/dossier.csv'):
        path = CHOPARD / name
        assert path.is_file(), f'missing Chopard table {path}'
        data = list(csv.DictReader(path.open(encoding='utf-8-sig', newline='')))
        out['sources'].append({'path': str(path), 'sha256': sha(path.read_bytes()), 'rows': len(data)})
        for r in rows:
            matches = [x for x in data if str(x.get('source_id', '')).strip() == r['gaia_dr3'] or str(x.get('TIC', '')).strip().lstrip('0') == r['tic']]
            if matches: out['targets'][r['tic']].append({'table': name, 'rows': matches})
    write_json(HERE / 'chopard-overlaps.json', out)
    return out

def tarrants_mendes(rows):
    """Reuse the documented same-parent cross-match; verify both TIC and Gaia ID."""
    path = Path('[local-path-redacted] 5.1/made/gate-xm/t2023-hits.json')
    primary = Path('[local-path-redacted]')
    primary_text = primary.read_text(encoding='utf-8')
    # These newly searched stars were not necessarily in the old claim set.
    primary_matches = [r['tic'] for r in rows if r['gaia_dr3'] in primary_text]
    assert not primary_matches, ('Primary-source identity requires explicit review', primary_matches)
    hits = json.loads(path.read_text(encoding='utf-8'))
    out = {'scope': 'Tarrants & Mendes 2023 cached same-parent cross-match; EB and Blend rows both require review; Yu 2018 and Kruse 2019 cited cases are represented only through this cross-match',
           'source': {'path': str(path), 'sha256': sha(path.read_bytes())}, 'primary_html_exact_gaia_check': {'path': str(primary), 'sha256': sha(primary.read_bytes()), 'matches': primary_matches}, 'targets': {}}
    for r in rows:
        h = hits.get(r['tic'])
        if h:
            assert str(h['row'][1]) == r['gaia_dr3'], f'Tarrants/Gaia identity mismatch {r["tic"]}'
            out['targets'][r['tic']] = h
        else: out['targets'][r['tic']] = None
    write_json(HERE/'tarrants-mendes-overlaps.json', out)
    return out

def network(rows, hb, chop, tm):
    results = []
    for r in rows:
        for label, table, radius in TABLES:
            params = {'-source': table, '-c': f"{r['ra']} {r['dec']}", '-c.rs': radius, '-out.max': 100, '-out.all': '', '-out.add': '_r', '-sort': '_r'}
            url = VIZIER + '?' + urllib.parse.urlencode(params)
            receipt, raw = cached_or_query(f"{r['tic']}-{label}", url)
            try: hits = parse_tsv(raw, table) if receipt['status'] == 'success' else []
            except Exception as exc: receipt['status'] = 'unavailable'; receipt['error'] = 'parse: '+repr(exc); hits = []; write_json(HERE / 'receipts' / (receipt['key']+'.json'), receipt)
            results.append({'tic': r['tic'], 'catalogue': label, 'table': table, 'status': receipt['status'], 'rows': hits, 'receipt': str((HERE/'receipts'/(receipt['key']+'.json')).relative_to(HERE))})
    ids = sorted({r['gaia_dr3'] for r in rows})
    for label, table in [('gaia_eb', 'vari_eclipsing_binary'), ('gaia_summary', 'vari_summary'), ('gaia_nss', 'nss_two_body_orbit')]:
        query = f"SELECT * FROM gaiadr3.{table} WHERE source_id IN (" + ','.join(ids) + ')'
        body = urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query})
        receipt, raw = cached_or_query(label, GAIA, body, 2000000)
        try:
            data = list(csv.DictReader(io.StringIO(raw.decode()))) if raw else []
            assert receipt['status'] != 'success' or (data or 'source_id' in raw.decode().splitlines()[0])
            assert {x['source_id'] for x in data} <= set(ids)
        except Exception as exc: receipt['status'] = 'unavailable'; receipt['error'] = 'parse: '+repr(exc); data = []; write_json(HERE/'receipts'/(label+'.json'),receipt)
        results.append({'catalogue': label, 'status': receipt['status'], 'rows': data, 'receipt': f'receipts/{label}.json'})
    identifiers = ['Gaia DR3 ' + g for g in ids]
    query = 'SELECT ident.id,basic.main_id,basic.otype,basic.ra,basic.dec FROM ident JOIN basic ON ident.oidref=basic.oid WHERE ident.id IN (' + ','.join("'"+x+"'" for x in identifiers) + ')'
    body = urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query})
    receipt, raw = cached_or_query('simbad', SIMBAD, body)
    try:
        data = list(csv.DictReader(io.StringIO(raw.decode()))) if raw else []
        assert receipt['status'] != 'success' or 'main_id' in raw.decode().splitlines()[0]
        assert {x['id'] for x in data} <= set(identifiers)
    except Exception as exc: receipt['status'] = 'unavailable'; receipt['error'] = 'parse: '+repr(exc); data = []; write_json(HERE/'receipts/simbad.json',receipt)
    results.append({'catalogue': 'simbad', 'status': receipt['status'], 'rows': data, 'receipt': 'receipts/simbad.json'})
    write_json(HERE/'catalogue-results.json', results)
    matrix = []
    for r in rows:
        by = {x['catalogue']: x for x in results if x.get('tic') == r['tic']}
        for label in ('gaia_eb','gaia_summary','gaia_nss','simbad'): by[label] = next(x for x in results if x['catalogue'] == label)
        exact = []; exact_other = []; nearby = []; nearby_close = []
        for label in ('vsx','asassn','prsa2022','ijspeert2024','kostov2025_table3','kostov2025_table4'):
            for x in by[label]['rows']:
                tic_match = str(x.get('TIC','')).lstrip('0') == r['tic']
                gaia_match = str(x.get('Name','')).strip() == 'Gaia DR3 '+r['gaia_dr3'] or str(x.get('GaiaDR3','')).strip() == r['gaia_dr3']
                eb_type = bool(re.search(r'(^|[/ :])(E|EA|EB|EW)(:|$|[/ ])', str(x.get('Type','')), re.I))
                if tic_match or gaia_match:
                    (exact if eb_type or label not in ('vsx','asassn') else exact_other).append({'catalogue':label,'row':x})
                elif eb_type or label not in ('vsx','asassn'):
                    alert={'catalogue':label,'row':x};nearby.append(alert)
                    if float(x.get('_r','999')) < 5: nearby_close.append(alert)
        eb = by['gaia_eb']; sim = by['simbad']
        if any(str(x.get('source_id')) == r['gaia_dr3'] for x in eb['rows']): exact.append({'catalogue':'gaia_eb','source_id':r['gaia_dr3']})
        for x in sim['rows']:
            if x.get('id') == 'Gaia DR3 '+r['gaia_dr3'] and x.get('otype') in ('EB*','Al*','bL*','WU*'): exact.append({'catalogue':'simbad','row':x})
        statuses = {label:by[label]['status'] for label in by}
        complete = all(x == 'success' for x in statuses.values())
        hbr=hb['targets'][r['tic']];tmr=tm['targets'][r['tic']];chopr=chop['targets'][r['tic']]
        callahan_eclipse=any(x.get('paper')=='Callahan+2025' and x.get('eclipses_flag')=='True' for x in hbr)
        tm_eb=bool(tmr and tmr['row'][5]=='EB');tm_blend=bool(tmr and tmr['row'][5]=='Blend')
        prior=bool(exact or callahan_eclipse or tm_eb or chopr)
        matrix.append({'tic':r['tic'],'gaia_dr3':r['gaia_dr3'],'coverage_complete':complete,'catalogue_statuses':json.dumps(statuses),'exact_prior_eb_identifications':json.dumps(exact),'exact_other_variable_counterparts':json.dumps(exact_other),'nearby_eb_rows_all_60arcsec':json.dumps(nearby),'nearby_eb_identity_alerts_under_5arcsec':json.dumps(nearby_close),'callahan_eclipses_flag':callahan_eclipse,'tarrants_mendes_row':json.dumps(tmr),'tarrants_mendes_blend_attribution_alert':tm_blend,'chopard_public_v1_2_overlap':bool(chopr),'scoped_prior_eb_status':'known prior EB in queried scope' if prior else 'nearby EB identity unresolved' if nearby_close else 'no identified prior EB in queried scope' if complete else 'unknown: incomplete query','heartbeat_overlap':json.dumps(hbr),'physical_verdict':'pending independent review'})
    with (HERE/'coverage-matrix.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=matrix[0].keys());w.writeheader();w.writerows(matrix)
    print(json.dumps({'targets':len(rows),'complete':sum(x['coverage_complete'] for x in matrix),'exact_eb_alerts':sum(bool(json.loads(x['exact_prior_eb_identifications'])) for x in matrix),'nearby_under_5arcsec_alerts':sum(bool(json.loads(x['nearby_eb_identity_alerts_under_5arcsec'])) for x in matrix)}))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--queue',type=Path,required=True);ap.add_argument('--queue-sha256',required=True);ap.add_argument('--local-only',action='store_true');a=ap.parse_args()
    global QUEUE_HASH
    QUEUE_HASH=sha(a.queue.read_bytes()); assert QUEUE_HASH.lower()==a.queue_sha256.lower(), 'queue hash mismatch'
    rows=load_queue(a.queue)
    lock=HERE/'queue-lock.json'
    if lock.exists(): assert json.loads(lock.read_text())['sha256']==QUEUE_HASH, 'different queue already locked in this directory'
    write_json(lock, {'queue':str(a.queue.resolve()),'sha256':QUEUE_HASH,'rows':len(rows),'locked_at_utc':now(),'targets':rows})
    hb=heartbeat(rows);chop=chopard(rows);tm=tarrants_mendes(rows)
    print(json.dumps({'queue_sha256':QUEUE_HASH,'targets':len(rows),'callahan_overlaps':sum(any(x['paper']=='Callahan+2025' for x in v) for v in hb['targets'].values()),'chopard_overlaps':sum(bool(v) for v in chop['targets'].values()),'tarrants_mendes_overlaps':sum(bool(v) for v in tm['targets'].values()),'network':not a.local_only}))
    if not a.local_only: network(rows,hb,chop,tm)

if __name__=='__main__': main()
