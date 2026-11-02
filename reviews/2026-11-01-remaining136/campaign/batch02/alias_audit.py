import csv,json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).parent;out={}
for r in csv.DictReader(open(B/'queue.csv')):
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));ev=[e for e in m['events'] if e.get('timing_usable')];p=m['period_days'];ep=m['primary_epoch_btjd'];dur=np.median([e['duration_days'] for e in ev]);cover=[];parity={}
 for sec in sorted(set(e['sector'] for e in ev)):
  z=[e for e in ev if e['sector']==sec];parity[str(sec)]={str(k):[e['depth_ppt'] for e in z if e['cycle']%2==k] for k in [0,1]}
 for src in m['sources']:
  with fits.open(src['path']) as h:
   a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']);ident={'ticid':h[0].header.get('TICID'), 'sector':h[0].header.get('SECTOR')}
  assert str(ident['ticid'])==tic
  valid=np.isfinite(t)&np.isfinite(f)&(f>0);clean=valid&(q==0)
  for n in range(math.floor((np.nanmin(t)-ep)/p)-1,math.ceil((np.nanmax(t)-ep)/p)+1):
   for phase in [0,.5]:
    center=ep+(n+phase)*p
    if not np.nanmin(t)<=center<=np.nanmax(t):continue
    dt=abs(t-center);core=clean&(dt<.25*dur);pre=clean&(t<center-.75*dur)&(t>center-1.75*dur);post=clean&(t>center+.75*dur)&(t<center+1.75*dur);flag=valid&(q!=0)&(dt<.25*dur)
    z=dict(sector=src['sector'],cycle=n,phase=phase,predicted_center_btjd=center,n_core=int(sum(core)),n_flagged_core=int(sum(flag)),n_pre=int(sum(pre)),n_post=int(sum(post)))
    if min(sum(core),sum(pre),sum(post))>=3:
     baseline=(np.median(f[pre])+np.median(f[post]))/2;z['raw_depth_ppt']=float(1000*(1-np.median(f[core])/baseline));z['status']='covered core with both baselines'
    else:z['status']='flagged/gap/insufficient baseline; not clean null'
    if phase==.5 and tic in ('300339443','260765760','464680877'):
     z['interpretation_warning']='Actual other-kind eclipse is near this half-phase window or baseline. This local ratio is not a clean eclipse depth or clean null; use secondary-timing.json and full raw fold.'
    cover.append(z)
 pairs=[dict(sector=a['sector'],cycles=[a['cycle'],b['cycle']],measured_spacing_days=b['mid_btjd']-a['mid_btjd']) for a,b in zip(ev,ev[1:]) if a['sector']==b['sector'] and b['cycle']-a['cycle']==1]
 out[tic]=dict(measured_period_days=p,within_sector_consecutive_pairs=pairs,sector_parity_depths=parity,coverage=cover,interpretation='Adjacent measured events test cycle spacing. Half-phase raw windows test P/2 and alternating-depth parity tests2P; sparse/flagged windows are not nulls. Equal-depth eclipses can retain an exact2P ambiguity; orbital association additionally uses Gaia but Gaia does not supply measured photometric timing. No exhaustive all-alias search.')
 (B/tic/'alias-coverage.json').write_text(json.dumps(out[tic],indent=2));print(tic,'pairs',len(pairs),'half',[(z['sector'],round(z['raw_depth_ppt'],1)) for z in cover if z['phase']==.5 and 'raw_depth_ppt' in z],flush=True)
(B/'alias-audit.json').write_text(json.dumps(out,indent=2))
