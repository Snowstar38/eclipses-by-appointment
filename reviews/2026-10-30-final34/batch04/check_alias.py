import pathlib,json,numpy as np
from astropy.io import fits
B=pathlib.Path('.'); R=B/'raw-evidence';raw=json.load(open(R/'raw-events.json'));out={}
for tic,r in raw.items():
 with fits.open(R/tic/('qlp_s%03d.fits'%r['sector'])) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(a['QUALITY']==0);t=t[ok];f=f[ok]
 P=r['representative_ephemeris']['period_d'];ep=r['events'][0]['tc'];D=np.median([e['duration_d'] for e in r['events']]);rows=[]
 for phase in [0,.5]:
  for n in range(int(np.floor((min(t)-ep)/P))-1,int(np.ceil((max(t)-ep)/P))+1):
   c=ep+(n+phase)*P;core=abs(t-c)<D*.3;side=(abs(t-c)>D*.8)&(abs(t-c)<D*1.6)
   if sum(core)>=3 and sum(side)>=8:rows.append(dict(phase=phase,cycle=n,center=float(c),n_core=int(sum(core)),loss=float(1-np.median(f[core])/np.median(f[side]))))
 out[tic]={'period_d':P,'checks':rows,'interpretation':'At-period repeating deep eclipses; half-period intervening windows test simple P/2 alias. P*2 remains mathematically possible for equal-depth eclipses, but Gaia orbital period near P supports P. Sparse two-event case retains precision/cycle-count limitations; not an exhaustive alias search.'}
(B/'alias-check.json').write_text(json.dumps(out,indent=2))
for t,v in out.items():print(t,[(ph,round(float(np.median([x['loss'] for x in v['checks'] if x['phase']==ph])),5),sum(x['phase']==ph for x in v['checks'])) for ph in [0,.5]])
