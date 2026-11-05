"""Bound 54494046 cycle aliases with observed partial and full trough contacts."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter

B=Path(__file__).resolve().parent;tic='54494046'
packet=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())
settings={
 43:('ingress',(2496.6,2498.05),(2495.0,2496.8)),
 45:('egress',(2527.8,2529.3),(2529.3,2531.0)),
 71:('egress',(3235.3,3236.5),(3236.5,3238.0)),
 72:('ingress',(3262.8,3264.2),(3262.0,3262.8)),
}
curves={};meta=[]
for sector,(direction,search,base) in settings.items():
 entry=next(e for e in packet['target']['files'] if f'_s{sector:03d}.fits' in e['path']);fp=Path(entry['path'])
 sha=hashlib.sha256(fp.read_bytes()).hexdigest()
 if sha!=entry['sha256']:raise RuntimeError('FITS hash mismatch '+str(fp))
 with fits.open(fp,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
 baseline=float(np.median(f[good&(t>base[0])&(t<base[1])]))
 sel=good&(t>search[0])&(t<search[1]);x=t[sel];y=median_filter(f[sel]/baseline,size=9)
 curves[sector]=(x,y,direction)
 meta.append({'sector':sector,'direction':direction,'search_btjd':search,'baseline_interval_btjd':base,
              'baseline_flux':baseline,'quality_zero_search_samples':len(x),'fits_sha256':sha})

def crossing(x,y,direction,level):
 s=y-level
 changes=np.where(s[:-1]*s[1:]<=0)[0]
 if direction=='ingress':changes=[i for i in changes if y[i]>y[i+1]]
 else:changes=[i for i in changes if y[i]<y[i+1]]
 if not changes:raise RuntimeError(f'no crossing {direction} {level}')
 i=changes[0]
 return float(x[i]+(level-y[i])*(x[i+1]-x[i])/(y[i+1]-y[i]))

levels=[]
for level in [.965,.970,.975]:
 c={s:crossing(*curves[s],level) for s in settings}
 # s43 and s72 share the near-eclipse-kind ingress; s45 and s71
 # share the opposite-kind egress. Phase of two kinds is not forced to P/2.
 p1=(c[72]-c[43])/13;p2=(c[71]-c[45])/12
 levels.append({'relative_flux_level':level,'crossings_btjd':c,
                's43_to_s72_13_cycles_days':p1,'s45_to_s71_12_cycles_days':p2,
                'adjacent_aliases_s43_s72_days':[(c[72]-c[43])/n for n in [12,14]],
                'adjacent_aliases_s45_s71_days':[(c[71]-c[45])/n for n in [11,13]]})
out={'tic':tic,'contacts':meta,'levels':levels,'caution':'Threshold contacts compare analogous limbs across four raw observing occasions. Broad-event shape and local baselines limit precision; crossing-derived values are alias diagnostics, not a formal eclipse ephemeris.'}
(B/tic/'partial-contact-aliases.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(levels,indent=2))
