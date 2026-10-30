# Merge per-event measurements into one markdown table per star (numbers from s04 free fits, s08 fixed-shape fits, s11 TESScut aperture)
import json, numpy as np
s04=json.load(open('s04_events.json')); s08=json.load(open('s08_shape_oddeven.json'))
for tic in ('283532878','407877153'):
    s11=json.load(open(f's11_pixels_{tic}.json')); eph=json.load(open(f's05_ephem_{tic}.json')); P=eph['P']
    print(f'### {tic}\n| Event | Mid BTJD (free fit) | Depth ppt QLP SAP (free / fixed shape) | Depth ppt TESS-SPOC SAP | Depth ppt own TESScut ap. | T14 / T23 h (free fit) | pipelines |\n|---|---|---|---|---|---|---|')
    keys=sorted({(r['kind'],r['n']) for r in s04 if r['tic']==tic},key=lambda k:(k[1]+(eph['ph2'] if k[0]=='S' else 0)))
    for kind,n in keys:
        R=[r for r in s04 if r['tic']==tic and r['kind']==kind and r['n']==n]
        q=[r for r in R if r['author']=='QLP']; sp=[r for r in R if r['author']=='TESS-SPOC']
        sec=R[0]['sector']
        fq=[o for o in s08[tic]['fixed'] if o['author']=='QLP' and o['kind']==kind and o['n']==n]
        fs=[o for o in s08[tic]['fixed'] if o['author']=='TESS-SPOC' and o['kind']==kind and o['n']==n]
        ap=[o for o in s11 if o['kind']==kind and o['n']==n]
        def fr(r): return r.get('status') in ('ok','partial') and 't0' in r
        best=(sp[0] if sp and fr(sp[0]) and sp[0]['status']=='ok' else (q[0] if q and fr(q[0]) else None))
        mid=f"{best['t0']:.4f} ± {best['et0']:.4f}" if best else ('gap (%s)'%('; '.join(f"{r['author']} {r['status']}, {r['nflag']} flagged" for r in R)))
        dq=(f"{1e3*q[0]['d']:.1f}±{1e3*q[0]['ed']:.1f}" if q and fr(q[0]) else 'gap')+' / '+(f"{1e3*fq[0]['d']:.1f}±{1e3*fq[0]['ed']:.1f}" if fq else '–')
        ds=(f"{1e3*fs[0]['d']:.1f}±{1e3*fs[0]['ed']:.1f}" if fs else (f"{1e3*sp[0]['d']:.1f}±{1e3*sp[0]['ed']:.1f} (free)" if sp and fr(sp[0]) else ('gap' if sp else 'n/a')))
        da=f"{1e3*ap[0]['depth']:.1f}±{1e3*ap[0]['edep']:.1f}" if ap else '–'
        dur=f"{24*best['T14']:.2f} / {24*best['T14']*best['r23']:.2f}" if best else '–'
        pl=[]
        if q and fr(q[0]): pl.append('QLP'+('(partial)' if q[0]['status']=='partial' else ''))
        if sp and fr(sp[0]): pl.append('SPOC-FFI')
        if ap: pl.append('TESScut')
        print(f"| {kind} n={n} s{sec} | {mid} | {dq} | {ds} | {da} | {dur} | {', '.join(pl) or 'none'} |")
    print()
