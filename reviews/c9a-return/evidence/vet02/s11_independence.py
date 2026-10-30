# Per-sector depth comparison: QLP SAP vs TESS-SPOC SAP (events_<tic>.csv, full events, e_tc<0.005) vs own
# TESScut r<=1.5 px aperture (s9_tesscut_<tic>_s<sec>.txt). Mean +- standard error (or formal error if N=1).
import numpy as np, pandas as pd, re, glob
for tic in ['470235665', '379251709']:
    d = pd.read_csv(f'events_{tic}.csv'); d = d[(d.status == 'full') & (d.e_tc < 0.005)]
    tc = {}
    for fn in glob.glob(f's9_tesscut_{tic}_s*.txt'):
        sec = int(re.findall(r'_s(\d+)\.txt', fn)[0])
        for l in open(fn):
            m = re.match(r'\s+(pri|sec) E(-?\d+) tc=\S+ \(pred.*depth=([-\d.]+)\+-([\d.]+)', l)
            if m: tc.setdefault((m.group(1), sec), []).append((float(m.group(3)), float(m.group(4))))
    print('=' * 8, 'TIC', tic, '(depths in ppt; N events)')
    for kind in ['pri', 'sec']:
        allq, alls = [], []
        if tic == '379251709' and kind == 'sec':
            print('  sec: not measurable per event in QLP/SPOC (see s7); TESScut per-event values in s9_tesscut_379251709_s18.txt (1.3+-0.9, 2.5+-0.7 ppt)'); continue
        for sec in sorted(set(d.sector) | {k[1] for k in tc}):
            row = f'  {kind} s{sec:2d}:'
            for pipe in ['QLP', 'SPOC']:
                x = d[(d.kind == kind) & (d.sector == sec) & (d['pipe'] == pipe)]
                if tic == '379251709' and kind == 'sec': x = x.iloc[0:0]  # secondary of 379 not measurable per event (s7)
                if len(x): 
                    m = x.depth_ppt.mean(); e = x.depth_ppt.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else x.e_depth_ppt.iloc[0]
                    row += f'  {pipe} {m:6.1f}+-{e:4.1f} (N={len(x)})'
                    (allq if pipe == 'QLP' else alls).append((sec, m))
                else: row += f'  {pipe:4s}      --       '
            if (kind, sec) in tc:
                v = np.array(tc[(kind, sec)]); m = v[:, 0].mean(); e = v[:, 0].std(ddof=1) / np.sqrt(len(v)) if len(v) > 1 else v[0, 1]
                row += f'  TESScut {m:6.1f}+-{e:4.1f} (N={len(v)})'
            print(row)
        q = dict(allq); s = dict(alls); com = sorted(set(q) & set(s))
        if com:
            r = np.array([q[k] / s[k] for k in com])
            print(f'  {kind}: QLP/SPOC SAP depth ratio over {len(com)} shared sectors = {r.mean():.3f} +- {r.std(ddof=1)/np.sqrt(len(r)) if len(r)>1 else 0:.3f} (range {r.min():.3f}-{r.max():.3f})')
        allv = d[(d.kind == kind)]
        if not (tic == '379251709' and kind == 'sec'):
            for pipe in ['QLP', 'SPOC']:
                x = allv[allv['pipe'] == pipe]
                print(f'  {kind} all {pipe}: mean {x.depth_ppt.mean():.1f} ppt, sd {x.depth_ppt.std(ddof=1):.1f}, N={len(x)}; T14 mean {x.T14_h.mean():.2f} h sd {x.T14_h.std(ddof=1):.2f}; T23 mean {x.T23_h.mean():.2f} h')
