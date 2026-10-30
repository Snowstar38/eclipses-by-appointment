# TIC 470235665: is the P_sec - P_pri difference (s6, s12) real apsidal motion or a pipeline/cadence effect?
# Secondary phase per observing season and per pipeline, each relative to the primary ephemeris of the same pipeline.
import numpy as np, pandas as pd
d = pd.read_csv('events_470235665.csv'); d = d[(d.status == 'full') & (d.e_tc < 0.005)]
seasons = {'2019-20 (s18-26, 30 min)': range(18, 27), '2022 (s52-53, 10 min)': range(52, 54), '2022-24 (s58-85, 200 s)': range(58, 86)}
for pipe in ['QLP', 'SPOC']:
    x = d[d['pipe'] == pipe]; p = x[x.kind == 'pri']
    A = np.vstack([np.ones(len(p)), p.epoch]).T; W = 1 / p.e_tc ** 2
    T0, P = np.linalg.solve(A.T @ (A * W.values[:, None]), A.T @ (W * p.tc))
    for lab, secs in seasons.items():
        s = x[(x.kind == 'sec') & (x.sector.isin(list(secs)))]
        if len(s) < 2: continue
        ph = (s.tc - T0) / P - s.epoch
        print(f'{pipe} {lab}: N={len(s)} secondary phase = {ph.mean():.5f} +- {ph.std(ddof=1)/np.sqrt(len(s)):.5f}  ({ph.mean()*P*1440:.1f} min after phase 0.5*P offset {((ph.mean()-0.5)*P*24):.3f} h)')
