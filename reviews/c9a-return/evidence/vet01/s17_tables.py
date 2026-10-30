# s17: per-sector event summaries from events_qlp.csv (s6) and full per-event markdown tables (events_table_<tic>.md)
import csv, numpy as np, json
R=list(csv.DictReader(open('events_qlp.csv'))); D11=json.load(open('s11_depths.json'))
for tic in ['195865529','468181994']:
    print('='*20,tic)
    lines=['| Type | Sector | Epoch | Mid BTJD | Depth (ppt) | T14 / T23 (h) | status |','|---|---|---|---|---|---|---|']
    for typ in ('P','S'):
        rr=[r for r in R if r['tic']==tic and r['type']==typ]
        for s in sorted({int(r['sector']) for r in rr}):
            x=[r for r in rr if int(r['sector'])==s]; ok=[r for r in x if r['status']=='ok' and r['e_t0'] not in ('','nan') and float(r['e_t0'])<0.03]
            bad=[r for r in x if r not in ok]
            if typ=='S' and tic=='468181994':
                print(f'  S s{s}: {len(ok)} fitted at fixed shape (individually {np.mean([float(r["depth"]) for r in ok])*1e3:.2f} ppt mean), {len(bad)} lost; mids {min(float(r["t0"]) for r in ok):.2f}-{max(float(r["t0"]) for r in ok):.2f}')
            else:
                d=np.array([float(r['depth']) for r in ok])*1e3; T14=np.array([float(r['T14_h']) for r in ok]); T23=np.array([float(r['T23_h']) for r in ok])
                print(f'  {typ} s{s}: n_ok {len(ok)}, lost/partial {len(bad)}; mids {min(float(r["t0"]) for r in ok):.3f}-{max(float(r["t0"]) for r in ok):.3f}; depth {d.mean():.1f} (sd {d.std(ddof=1):.1f}) ppt; T14 {np.median(T14):.2f} h, T23 {np.median(T23):.2f} h; lost: {[ (r["epoch"],r["t_pred"]) for r in bad]}')
            for r in x:
                if r in ok: lines.append(f"| {typ} | {s} | {r['epoch']} | {float(r['t0']):.5f} ± {float(r['e_t0']):.5f} | {float(r['depth'])*1e3:.2f} ± {float(r['e_depth'])*1e3:.2f} | {float(r['T14_h']):.2f} / {float(r['T23_h']):.2f} | ok |")
                else: lines.append(f"| {typ} | {s} | {r['epoch']} | pred {float(r['t_pred']):.3f} | – | – | {r['status']} (good pts in T14 {r['n_in_good']}, flagged {r['n_in_flagged']}) |")
    open(f'events_table_{tic}.md','w').write(f'# QLP SAP (QUALITY==0) individual events, TIC {tic} (from events_qlp.csv, s6)\n\n'+'\n'.join(lines)+'\n')
    n=sum(1 for r in R if r['tic']==tic and r['status']=='ok'); print('  total ok events (P+S) in events_qlp.csv:',n)
