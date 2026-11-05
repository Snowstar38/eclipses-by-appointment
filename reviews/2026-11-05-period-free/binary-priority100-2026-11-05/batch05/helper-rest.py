import json,hashlib,numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.timeseries import LombScargle
B=Path(__file__).parent;out=[]
for tic,sector,c in [('21743048',78,3446.923794),('307018189',6,1484.829159),('319604640',67,3147.362053),('251325499',85,3623.794025),('320414796',7,1496.57897),('142119008',26,2011.757787),('334142514',61,2974.774045),('269941080',27,2047.301078)]:
 p=Path(r'[local-path-redacted]')/f'{tic}_s{sector:03d}.fits'
 with fits.open(p) as h:
  d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY']);
 m=np.isfinite(t)&np.isfinite(f)&(q==0)&(abs(t-c)<2);t=t[m];f=f[m];med=np.median(f);idx=np.argsort(t);t=t[idx];f=f[idx];dt=np.diff(t);df=np.diff(f)/med*1000; cadence=np.median(dt);j=np.argmax(abs(df)*(dt<2*cadence));core=abs(t-c)<.06
 rec=dict(tic=tic,sector=sector,center=c,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),n=len(t),nominal_cadence_days=float(cadence),largest_gap_days=float(dt.max()),largest_gap_endpoints=[float(t[np.argmax(dt)]),float(t[np.argmax(dt)+1])],largest_adjacent_jump_ppt=float(df[j]),jump_endpoints=[float(t[j]),float(t[j+1])],core_points=int(core.sum()),core_times=t[core].tolist(),core_relative_ppt=np.round((f[core]/med-1)*1000,3).tolist())
 if tic=='320414796':
  freq=np.linspace(.4,4,10000);pw=LombScargle(t,f/med-1).power(freq);i=np.argmax(pw);rec['local_period_days']=float(1/freq[i]);rec['local_power']=float(pw[i])
 out.append(rec);print(tic, 'gap',round(dt.max(),3),'jump',round(df[j],2),'core',core.sum(), 'period',rec.get('local_period_days'))
(B/'helper-rest-numeric.json').write_text(json.dumps(out,indent=2))
