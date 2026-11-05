"""Bounded integer-alias nulls and source-specific Gaia conjunctions."""
import json, math, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;ROOT=B.parent

def conjunction(P,e,w,tp,kind):
    nu=(math.pi/2 if kind=='A' else 3*math.pi/2)-w
    E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
    return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P

for tic in ('209429773','250561084'):
    D=B/tic; packet=json.loads((ROOT/'source-packets'/tic/'sources.json').read_text());ctx=json.loads((D/'lead-context.json').read_text());m=json.loads((D/'lead-timing.json').read_text());g=packet['target']['gaia']
    if tic=='209429773':
        ev=sorted([z for z in m if z['sector'] in (30,97)],key=lambda x:x['diagnostic_center_btjd']);a=ev[0]['diagnostic_center_btjd'];b=ev[-1]['diagnostic_center_btjd'];P=(b-a)/43; integer=43
        # S31 main event is a same-kind timing crosscheck, not an input to P.
        cross=next(z for z in m if z['sector']==31 and z['diagnostic_center_btjd']>2160)
        cross_offset=cross['diagnostic_center_btjd']-(a+P)
        adjacent=[dict(long_baseline_cycles=n,conditional_period_days=(b-a)/n,S31_main_offset_days=cross['diagnostic_center_btjd']-(a+(b-a)/n)) for n in (42,43,44)]
    else:
        ev=sorted([z for z in m if z['sector']==18],key=lambda x:x['diagnostic_center_btjd']);a=ev[0]['diagnostic_center_btjd'];b=ev[-1]['diagnostic_center_btjd'];integer=297
        later=sorted([z for z in m if z['sector']==85],key=lambda x:x['diagnostic_center_btjd'])
        P=(later[0]['diagnostic_center_btjd']-a)/297
        cross_offset=[z['diagnostic_center_btjd']-(a+n*P) for n,z in zip((297,298,299),later)]
        adjacent=[dict(long_baseline_cycles=n,conditional_period_days=(later[0]['diagnostic_center_btjd']-a)/n,S18_fourth_offset_days=b-(a+3*(later[0]['diagnostic_center_btjd']-a)/n),S85_third_offset_days=later[2]['diagnostic_center_btjd']-(a+(n+2)*(later[0]['diagnostic_center_btjd']-a)/n)) for n in (296,297,298)]
    P_gaia=float(g['period']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=389+float(g['t_periastron'])
    geo=[]
    for kind in ('A','B'):
        base=conjunction(P_gaia,e,w,tp,kind)
        n=round((a-base)/P_gaia);pred=base+n*P_gaia
        geo.append(dict(kind=kind,cycle=n,predicted_btjd=pred,observed_minus_predicted_days=a-pred,phase_offset=(a-pred)/P_gaia))
    nulls=[]
    # Shorter aliases imply same-depth occultations at intermediate centers.
    for divisor in (2,3,4):
        pa=P/divisor
        for s in ctx['sectors']:
            fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
            with fits.open(fp,memmap=False) as h:
                dat=h[1].data;t=np.asarray(dat['TIME'],float);f=np.asarray(dat['SAP_FLUX'],float);q=np.asarray(dat['QUALITY'],int)
            good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
            nlo=math.ceil((s['time_start_btjd']-a)/pa);nhi=math.floor((s['time_end_btjd']-a)/pa)
            for n in range(nlo,nhi+1):
                # Existing main events cannot be nulls.
                c=a+n*pa
                if any(abs(c-z['diagnostic_center_btjd'])<(.35 if tic=='209429773' else .12) for z in m):continue
                width=.1 if tic=='250561084' else .32
                core=(t>=c-width/2)&(t<=c+width/2)
                left=(t>=c-3*width)&(t<c-width);right=(t>c+width)&(t<=c+3*width)
                core_t=t[core]
                actual_gap=float(np.max(np.diff(core_t))) if len(core_t)>1 else None
                expected=max(1,round(width/s['cadence_days']))
                covered=bool(core.sum()>=.8*expected and left.sum()>=5 and right.sum()>=5 and (actual_gap is not None and actual_gap<3*s['cadence_days']))
                if not covered:continue
                side=np.concatenate([f[left],f[right]]);side_t=np.concatenate([t[left],t[right]]);coef=np.polyfit(side_t-c,side,1)
                norm=f[core]/np.polyval(coef,core_t-c);res=side/np.polyval(coef,side_t-c)
                depth=float((1-np.median(norm))*1000);noise=float(1.4826*np.median(np.abs(res-np.median(res)))*1000)
                nulls.append(dict(divisor=divisor,sector=s['sector'],predicted_btjd=c,core_actual=int(core.sum()),core_expected=expected,left_actual=int(left.sum()),right_actual=int(right.sum()),core_max_gap_days=actual_gap,local_depth_ppt=depth,side_mad_ppt=noise,source_sha256=s['source_sha256']))
    out=dict(tic=tic,reference_event_btjd=a,conditional_photometric_period_days=P,reference_cycle_span=integer,crosscheck_offset_days=cross_offset,adjacent_integer_aliases=adjacent,gaia=dict(source_id=g['source_id'],period_days=P_gaia,period_error_days=float(g['period_error']),eccentricity=e,omega_deg=math.degrees(w),periastron_btjd=tp,conjunctions=geo),short_alias_actual_covered_windows=nulls,
             caution='Same-kind period conditional on morphology and integer cycles. Nulls require actual cadence endpoints, core and sidebands; local depth is diagnostic. Gaia edge-on conjunction is geometric context, not source ownership or a precision ephemeris.')
    (D/'lead-alias-geometry.json').write_text(json.dumps(out,indent=2)+'\n')
    print(tic,'P',P,'crosscheck',cross_offset,'conjunctions',geo,'covered nulls',[(d,sum(z['divisor']==d for z in nulls),sum(z['divisor']==d and abs(z['local_depth_ppt'])<3 for z in nulls)) for d in (2,3,4)])
