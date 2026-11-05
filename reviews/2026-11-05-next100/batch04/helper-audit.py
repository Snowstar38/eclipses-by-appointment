"""Independent sealed-source, cadence, and local-depth audit of Q031-Q040."""
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from astropy.io import fits

B = Path(__file__).resolve().parent
ROOT = B.parent
INDEX = json.loads((ROOT / 'source-packet-index.json').read_text())['targets']
records = []
for row in csv.DictReader((B / 'queue.csv').open(newline='', encoding='utf8')):
    tic = row['tic']
    packet_path = ROOT / 'source-packets' / tic / 'sources.json'
    packet = json.loads(packet_path.read_text(encoding='utf8'))
    assert packet['queue_row']['sample_id'] == row['sample_id']
    assert hashlib.sha256(packet_path.read_bytes()).hexdigest() == INDEX[tic]['sha256']
    assert hashlib.sha256(Path(packet['bulk_result']).read_bytes()).hexdigest() == packet['bulk_result_sha256']
    detector = json.loads(Path(packet['bulk_result']).read_text())
    rec = {'sample_id': row['sample_id'], 'tic': tic, 'packet_sha256': INDEX[tic]['sha256'],
           'bulk_sha256': packet['bulk_result_sha256'], 'gaia_period_days': float(row['gaia_period_days']), 'sectors': []}
    for source, det in zip(packet['verified_files'], detector['files']):
        fp = Path(source['path'])
        assert hashlib.sha256(fp.read_bytes()).hexdigest() == source['sha256']
        assert int(source['sector']) == int(det['sector'])
        with fits.open(fp, memmap=False) as h:
            a = h[1].data
            t0 = np.asarray(a['TIME'], float)
            f0 = np.asarray(a['SAP_FLUX'], float)
            q0 = np.asarray(a['QUALITY'], int)
            alt0 = np.asarray(a['KSPSAP_FLUX'], float) if 'KSPSAP_FLUX' in h[1].columns.names else None
        ok = np.isfinite(t0) & np.isfinite(f0) & (f0 > 0) & (q0 == 0)
        t, f = t0[ok], f0[ok]
        alt = alt0[ok] if alt0 is not None else None
        sec = {'sector': int(source['sector']), 'source_sha256': source['sha256'],
               'quality0_positive_points': int(ok.sum()), 'all_rows': len(t0),
               'start_btjd': float(t.min()), 'end_btjd': float(t.max()),
               'cadence_days': float(np.median(np.diff(t))), 'windows': []}
        for w in det.get('windows', []):
            if not w.get('flag'):
                continue
            c = float(w['time'])
            width = float(w['duration'])
            core = np.abs(t-c) <= width/4
            side = (np.abs(t-c) >= width*.75) & (np.abs(t-c) <= width*1.5)
            if core.sum() < 2 or side.sum() < 6:
                continue
            local = np.abs(t-c) <= width*1.5
            diffs = np.diff(t[local])
            gaps = [[float(t[local][i]), float(t[local][i+1])] for i in np.where(diffs > 3*sec['cadence_days'])[0]]
            v = {'kind': w['kind'], 'screen_center_btjd': c, 'screen_duration_days': width,
                 'core_n': int(core.sum()), 'side_n': int(side.sum()),
                 'core_first_btjd': float(t[core].min()), 'core_last_btjd': float(t[core].max()),
                 'raw_sap_loss_ppt': float(1000*(1-np.median(f[core])/np.median(f[side]))),
                 'raw_side_mad_ppt': float(1000*1.4826*np.median(np.abs(f[side]/np.median(f[side])-1))),
                 'local_gaps_over_3cadences': gaps}
            if alt is not None:
                valid_alt = np.isfinite(alt) & (alt > 0)
                if np.sum(valid_alt & core) >= 2 and np.sum(valid_alt & side) >= 6:
                    v['kspsap_loss_ppt'] = float(1000*(1-np.median(alt[valid_alt & core])/np.median(alt[valid_alt & side])))
            sec['windows'].append(v)
        rec['sectors'].append(sec)
    records.append(rec)
    print(rec['sample_id'], tic, [(s['sector'], [(round(w['screen_center_btjd'],2),round(w['raw_sap_loss_ppt'],2)) for w in s['windows']]) for s in rec['sectors']], flush=True)
(B / 'helper-raw-metrics.json').write_text(json.dumps(records, indent=2)+'\n', encoding='utf8')
