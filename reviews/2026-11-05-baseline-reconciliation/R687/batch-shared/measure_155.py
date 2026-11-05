"""Bounded raw-SAP measurements for TIC 155346713, without imputing s7 A center."""
import hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

W=Path(__file__).resolve().parent
S=W.parent/'search256'
snap=json.loads((W/'SOURCE-SNAPSHOT.json').read_text())['targets']['155346713']
old={r['sector']:r for r in json.loads((S/'followups'/'downloads-155346713.json').read_text())['products']}
inputs={r['sector']:r for r in snap['raw_fits']}
inputs.update(old)
P_GAIA=33.63348396287843

def load(sec):
    r=inputs[sec]; p=Path(r['path'])
    assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
    with fits.open(p) as h:
        assert int(h[0].header['TICID'])==155346713
        assert int(h[0].header['SECTOR'])==sec
        d=h[1].data
        t=np.asarray(d['TIME'],float); f=np.asarray(d['SAP_FLUX'],float); q=np.asarray(d['QUALITY'],int)
    m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
    return t[m],f[m],r['sha256']

def model(t,b,s,amp,c,width,ing):
    return b+s*(t-c)-amp*np.clip((width/2-np.abs(t-c))/ing,0,1)

out={'tic':155346713,'gaia_dr3_source_id':'5694314546391164032','gaia_period_days':P_GAIA,
     'method':'QLP QUALITY=0 raw SAP, local linear baseline plus trapezoid; point estimates are descriptive, covariance statistical only',
     'events':[]}
fig,axs=plt.subplots(1,3,figsize=(15,4))
for ax,(sec,c,radius,p0,bounds) in zip(axs,[
    (7,1502.50,.75,[1,0,.057,1502.50,.23,.04],([.8,-.2,0,1502.4,.12,.01],[1.2,.2,.25,1502.6,.5,.12])),
    (88,3702.33,1.5,[1,0,.13,3702.33,1.03,.36],([.8,-.2,0,3702.1,.5,.1],[1.2,.2,.3,3702.55,1.5,.7]))]):
    t,f,h=load(sec); sel=abs(t-c)<radius; x=t[sel]; y=f[sel]
    base=abs(x-c)>(.2 if sec==7 else .8)
    y=y/np.median(y[base])
    p,cov=curve_fit(model,x,y,p0=p0,bounds=bounds,maxfev=50000)
    err=np.sqrt(np.diag(cov)); cadence=float(np.median(np.diff(t)))
    realized=float(p[2]*min(1,p[4]/(2*p[5]))*1000)
    out['events'].append(dict(kind='B' if sec==7 else 'A',sector=sec,center_btjd=float(p[3]),
      formal_center_error_days=float(err[3]),half_cadence_days=cadence/2,
      depth_ppt=realized,duration_days=float(p[4]),ingress_days=float(p[5]),
      n_fit_points=len(x),source_sha256=h,
      limitation='Trapezoid and local linear baseline on pulsating flux; aperture-dependent depth and model-systematic timing not in covariance'))
    ax.plot(x,y,'.',ms=2,label='QLP Q0 SAP'); xx=np.linspace(x.min(),x.max(),500)
    ax.plot(xx,model(xx,*p),'r-',lw=1.5,label='local trapezoid')
    ax.set_title(f's{sec} {"B" if sec==7 else "A"} {p[3]:.5f} BTJD; {realized:.1f} ppt')
    ax.set_xlabel('BTJD'); ax.set_ylabel('relative raw SAP'); ax.legend(fontsize=8)

# Sector-7 A has ingress but no center/egress. Compare endpoint and orbital forecast only.
t,f,h=load(7); sel=(t>1515.4)&(t<1516.04); x=t[sel];y=f[sel]
# Local baseline from immediately preceding oscillation maximum/minimum is uncertain.
baseline=np.median(f[(t>1514.8)&(t<1515.4)])
yy=y/baseline
pred=out['events'][1]['center_btjd']-65*P_GAIA
out['sector7_A_partial']={'first_ingress_btjd_approximately':1515.75,'last_qlp_q0_btjd':float(t.max()),
  'last_segment_min_relative_to_preceding_median':float(yy.min()),
  'forecast_center_btjd_from_s88_and_65_gaia_cycles':pred,
  'cycle_alias_test':'65 cycles is compatible with a partial ingress, but center and egress are not observed; no photometric same-kind period measured',
  'source_sha256':h}
ax=axs[2];ax.plot(x,yy,'.',ms=4,label='s7 partial A ingress');ax.axvline(pred,ls=':',color='green',label='65-cycle Gaia forecast')
ax.set_xlabel('BTJD');ax.set_ylabel('SAP / preceding median');ax.legend(fontsize=8)
ax.set_title('s7 A: center/egress unobserved')

# QLP quality-zero gap around s61 B forecast.
t,f,h=load(61); bcenter=out['events'][0]['center_btjd']+44*P_GAIA
left=t[t<bcenter].max();right=t[t>bcenter].min()
out['sector61_B_forecast']={'from_s7_B_plus_44_gaia_cycles_btjd':bcenter,
  'bracketing_q0_btjd':[float(left),float(right)],'gap_days':float(right-left),
  'status':'predicted B core lies within quality-zero cadence gap; not a clean null','source_sha256':h}
out['same_kind_period_days']=None
out['same_kind_period_reason']='Only one complete center for each eclipse kind; s7 A is ingress-only; s61 B core falls in a quality-zero gap.'
(W/'measurements-155346713.json').write_text(json.dumps(out,indent=2))
fig.tight_layout();fig.savefig(W/'events-155346713.png',dpi=140)
print(json.dumps(out,indent=2))
