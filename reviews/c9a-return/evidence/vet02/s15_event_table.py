# Markdown event tables for REPORT.md from events_<tic>.csv (raw SAP fits, s5) and the TESScut fits (s9).
# Mid-time: TESS-SPOC if that pipeline has a full fit, else QLP. Depths in ppt. Lost/partial events listed after.
import pandas as pd, numpy as np, re, glob
for tic in ['470235665', '379251709']:
    d = pd.read_csv(f'events_{tic}.csv')
    tc = {}
    for fn in glob.glob(f's9_tesscut_{tic}_s*.txt'):
        for l in open(fn):
            m = re.match(r'\s+(pri|sec) E(-?\d+) tc=(\S+)\+-\S+ \(pred.*depth=([-\d.]+)\+-([\d.]+)', l)
            if m: tc[(m.group(1), int(m.group(2)))] = (float(m.group(3)), float(m.group(4)), float(m.group(5)))
    print(f'### TIC {tic}\n\n| Event | Sector | Mid BTJD | Depth QLP / SPOC / TESScut (ppt) | T14 / T23 (h) | pipelines |\n|---|---|---|---|---|---|')
    kinds = ['pri', 'sec'] if tic == '470235665' else ['pri']
    notes = []
    for kind in kinds:
        for n in sorted(set(d[d.kind == kind].epoch)):
            x = d[(d.kind == kind) & (d.epoch == n)]; f = x[(x.status == 'full') & (x.e_tc < 0.005)]
            T = tc.get((kind, n))
            if len(f) == 0 and T is None:
                notes.append(f'{kind} E{n} (s{x.sector.iloc[0]}, pred {x.pred.iloc[0]:.3f}): ' + ', '.join(f'{r.pipe} {r.status}' for r in x.itertuples())); continue
            best = f[f['pipe'] == 'SPOC'] if (f['pipe'] == 'SPOC').any() else f
            if len(best):
                b = best.iloc[0]; mid = f'{b.tc:.4f} ± {b.e_tc:.4f}'; dur = f'{b.T14_h:.2f} / {b.T23_h:.2f}'; sec = b.sector
            else:
                mid = f'{T[0]:.4f} (TESScut)'; dur = '(fixed)'; sec = x.sector.iloc[0]
            dq = f[f['pipe'] == 'QLP'].depth_ppt; ds = f[f['pipe'] == 'SPOC'].depth_ppt
            dep = f'{dq.iloc[0]:.1f}' if len(dq) else '–'; dep += ' / ' + (f'{ds.iloc[0]:.1f}' if len(ds) else '–'); dep += ' / ' + (f'{T[1]:.1f}' if T else '–')
            pip = '+'.join(list(f['pipe']) + (['TESScut'] if T else []))
            part = [f'{r.pipe} {r.status if r.status != "full" else "noisy, e_tc>0.005 d"}' for r in x.itertuples() if r.status != 'full' or r.e_tc >= 0.005]
            print(f'| {"P" if kind=="pri" else "S"} E{n} | {sec} | {mid} | {dep} | {dur} | {pip}{" (" + ", ".join(part) + ")" if part else ""} |')
    print('\nNot measured (gap / flagged / too little coverage):', '; '.join(notes) if notes else 'none', '\n')
