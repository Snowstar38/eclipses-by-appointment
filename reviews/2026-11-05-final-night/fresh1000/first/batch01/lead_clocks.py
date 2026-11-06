import json,csv,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
trials={'1269035':20.484,'22210159':34.874,'34308477':49.3168,'71295367':.8711,'92872537':32.81625,'95324628':10.3567,'98160330':30.224,'98941880':4.398}
pop=json.loads((b.parent.parent.parent/'fresh-band-next1000/population.json').read_text())['targets']
out={}
for tic,p in trials.items():
 ev=json.loads((b/tic/'lead-timing.json').read_text());ev=[e for e in ev if e.get('fit_usable')]
 if tic=='98160330':ev=[e for e in ev if e['depth_ppt']>40]
 if tic=='95324628':ev=[e for e in ev if e['depth_ppt']>300]
 if tic=='71295367': ev=[e for e in ev if e['sector']>20]
 t=np.array([e['center_btjd'] for e in ev]);n=np.round((t-t[0])/p).astype(int);err=np.array([max(e['center_formal_error_d'],e['cadence_d']/2,.002) for e in ev]);X=np.array([np.ones(len(n)),n]).T;W=1/err**2;cv=np.linalg.inv(X.T@(W[:,None]*X));v=cv@(X.T@(W*t));res=t-X@v
 out[tic]=dict(period_d=v[1],epoch_btjd=v[0],formal_period_error_d=cv[1,1]**.5,cycles=n.tolist(),times=t.tolist(),residuals=res.tolist(),duration_d=float(np.median([e['duration_d'] for e in ev])),depth_ppt=float(np.median([e['depth_ppt'] for e in ev])),max_residual_d=float(max(abs(res))),gaia_period_d=float(pop[tic]['gaia']['period']),note='Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors.')
 print(tic,v,'res',res)
(b/'lead-clocks.json').write_text(json.dumps(out,indent=2))
