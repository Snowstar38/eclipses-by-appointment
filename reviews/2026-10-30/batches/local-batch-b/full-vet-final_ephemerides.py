import pathlib,json,numpy as np
from astropy.time import Time
r=pathlib.Path(__file__).parent
for tic in ['295945076','372376841','416525506','451493289','348737250']:
 m=json.loads((r/f'{tic}_measurements.json').read_text());s=json.loads((r/f'{tic}_secondary_timing.json').read_text());a=[e for e in s['events'] if not e['center_edge']];k=np.array([e['cycle'] for e in a]);t=np.array([e['tc'] for e in a]);err=np.array([e['error_d'] for e in a]);mid=int(np.median(k));X=np.column_stack([np.ones(len(k)),k-mid]);wt=1/err**2;C=np.linalg.inv(X.T@(wt[:,None]*X));coef=C@(X.T@(wt*t));res=t-X@coef;C*=max(1,float(sum((res/err)**2)/max(1,len(k)-2)));secs=set(e['sector'] for e in a);jack=[]
 for sec in secs:
  ix=np.array([e['sector']!=sec for e in a]);xx=X[ix];ww=wt[ix]
  if ix.sum()>2:
   b=np.linalg.inv(xx.T@(ww[:,None]*xx))@(xx.T@(ww*t[ix]));jack.append(float(b[0]))
 now=Time('2026-10-30T00:00:00',scale='tdb').jd-2457000;P=coef[1];cycle=int(np.ceil((now-coef[0])/P)); ep=m['ephemeris'];pc=int(np.ceil((now-ep['T0'])/ep['P']));out={'secondary_T0':float(coef[0]),'secondary_P':float(P),'covariance':C.tolist(),'cycle_zero':mid,'oc_d':res.tolist(),'cycles':k.tolist(),'sector_jackknife_T0_scatter_d':float(np.std(jack,ddof=1)) if len(jack)>1 else None,'period_difference_d':float(P-ep['P']),'period_difference_formal_error_d':float(np.sqrt(C[1,1]+ep['covariance'][1][1])),'now_BTJD':now,'next_secondary_BTJD':[float(coef[0]+(cycle+j)*P) for j in range(4)],'next_primary_BTJD':[float(ep['T0']+(pc+j)*ep['P']) for j in range(4)],'caveat':'Conditional covariance; common systematics and independently fitted depths may correlate primary and secondary; uncertainty at future epochs may be underestimated.'};(r/f'{tic}_secondary_ephemeris.json').write_text(json.dumps(out,indent=2))
 census=json.loads((r/f'{tic}_blind_census.json').read_text());phase=s['weighted_phase'];off=[]
 for e in census['peaks']:
  ph=e['phase'];d1=min(ph,1-ph)*ep['P'];ds=abs((ph-phase+.5)%1-.5)*ep['P'];e['classification']='primary' if d1<census['width_d'] else ('secondary' if ds<census['width_d'] else 'off_ephemeris')
  if e['classification']=='off_ephemeris':off.append(e)
 (r/f'{tic}_blind_census.json').write_text(json.dumps(census,indent=2));print(tic,'Ps',P,'off',len(off),'next',out['next_primary_BTJD'][0],out['next_secondary_BTJD'][0])
 if tic=='416525506':
  ev=[e for e in m['events'] if e['background_fractional_change'] is not None];bad=max(ev,key=lambda e:abs(e['background_fractional_change']));print('416 background worst',bad)
