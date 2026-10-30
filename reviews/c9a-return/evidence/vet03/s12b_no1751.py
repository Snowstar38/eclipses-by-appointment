# SPOC primary/secondary period without the single s1751 events (does the s1751 point drive the SPOC-QLP period difference?)
import numpy as np, json
ev=[e for e in json.load(open('s3_events_70665829.json')) if e['pipe']=='SPOC' and e['D']>0.02 and e['eD']<0.01 and e['sector']!=1751 and e['fill']>0.9 and e['npre']>=5 and e['npost']>=5]
P0=3.4657658
for lab,sel in [('primaries',[e for e in ev if e['D']>0.15]),('secondaries',[e for e in ev if e['D']<=0.15])]:
    ts=np.array([e['t0'] for e in sel]); es=np.array([e['et0'] for e in sel]); n=np.round((ts-ts[0])/P0)
    A=np.vstack([np.ones_like(n),n]).T; W=1/es**2; C=np.linalg.inv(A.T@(A*W[:,None])); p=C@(A.T@(W*ts)); r=ts-A@p; chi=np.sum(r**2*W)/(len(ts)-2)
    print(f'SPOC no-s1751 {lab}: N={len(ts)} P={p[1]:.7f}+-{np.sqrt(C[1,1]*max(chi,1)):.7f} chi2r={chi:.2f}; predicted s1751 primary 4060.0822 O-C if this P: {(4060.08215-(p[0]+np.round((4060.08215-p[0])/p[1])*p[1]))*1440:+.2f} min' if lab=='primaries' else f'SPOC no-s1751 {lab}: N={len(ts)} P={p[1]:.7f}+-{np.sqrt(C[1,1]*max(chi,1)):.7f} chi2r={chi:.2f}')
