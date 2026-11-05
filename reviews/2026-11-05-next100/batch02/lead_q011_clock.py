"""Measure Q011 raw eclipse centers and bounded 3.28/6.55/13.11 d alias windows."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='246892556';O=B/tic
inv=json.loads((O/'lead-inventory.json').read_text(encoding='utf-8'))
raw={}; sources=[]
for s in inv['sectors']:
    p=Path(s['file']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
    with fits.open(p,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    v=(q==0)&np.isfinite(t)&np.isfinite(f)&(f>0);raw[s['sector']]=(t[v],f[v]);sources.append(dict(path=str(p),sha256=s['sha256']))
seed={29:[2089.59,2096.15,2109.27],69:[3184.64,3191.19,3197.74,3204.32]}
events=[];fig,axs=plt.subplots(7,1,figsize=(8,14))
for ax,(sec,guess) in zip(axs,[(s,x) for s,xx in seed.items() for x in xx]):
    t,f=raw[sec];radius=.45;loc=np.abs(t-guess)<radius;x=t[loc]-guess;y=f[loc]
    side=(np.abs(x)>.17)&(np.abs(x)<.45);coef=np.polyfit(x[side],y[side],1);baseline=np.polyval(coef,x)
    resid=(y-baseline)/np.median(baseline[side]);search=np.abs(x)<.12
    sm=median_filter(resid,size=3);ix=np.where(search)[0][np.argmin(sm[search])];center=float(t[loc][ix])
    core=np.abs(t[loc]-center)<.035;depth=float(-np.median(resid[core]));noise=float(1.4826*np.median(np.abs(resid[side]-np.median(resid[side]))))
    ev=dict(sector=sec,screen_guess_btjd=guess,measured_minimum_btjd=center,core_depth_ppt=1000*depth,local_side_mad_ppt=1000*noise,n_core=int(core.sum()),n_side=int(side.sum()))
    events.append(ev)
    ax.plot(t[loc],resid*1000,'k.',ms=2);ax.axvline(center,color='C3');ax.set_ylabel(f'S{sec}\nppt');ax.set_xlim(guess-.3,guess+.3);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(O/'lead-q011-event-zooms.png',dpi=140);plt.close(fig)
times=np.array([e['measured_minimum_btjd'] for e in events]);n=np.rint((times-times[0])/6.55).astype(int)
p,epoch=np.polyfit(n,times,1);resid=(times-(epoch+p*n))*24*60
for e,ni,ri in zip(events,n,resid):e['cycle_index_at_6p55d']=int(ni);e['ephemeris_residual_minutes']=float(ri)

def metric(sec,c):
    t,f=raw[sec];dt=float(np.median(np.diff(t)));x=t-c
    core=np.abs(x)<.06;left=(x>-.5)&(x<-.18);right=(x>.18)&(x<.5)
    def coverage(sel,lo,hi):
        z=np.sort(t[sel]);edges=np.r_[lo,z,hi];return dict(n=int(len(z)),largest_gap_days=float(np.max(np.diff(edges))) if len(z) else hi-lo,first_btjd=float(z[0]) if len(z) else None,last_btjd=float(z[-1]) if len(z) else None)
    cov=dict(core=coverage(core,c-.06,c+.06),left=coverage(left,c-.5,c-.18),right=coverage(right,c+.18,c+.5))
    valid=(all(cov[k]['n']>=4 and cov[k]['largest_gap_days']<.035 for k in cov))
    if not valid:return dict(center_btjd=float(c),sector=sec,covered=False,coverage=cov)
    sides=left|right;coef=np.polyfit(x[sides],f[sides],1);base=np.polyval(coef,x)
    loss=float((np.median(base[core]-f[core]))/np.median(base[sides])*1000)
    scatter=float(1.4826*np.median(np.abs((f[sides]-base[sides])-np.median(f[sides]-base[sides])))/np.median(base[sides])*1000)
    return dict(center_btjd=float(c),sector=sec,covered=True,coverage=cov,loss_ppt=loss,side_mad_ppt=scatter)

tests=[]
for s in inv['sectors']:
    sec=s['sector'];lo,hi=s['time_start'],s['time_end']
    for factor,label in [(0.5,'half_step_extra'),(1.0,'full_step'),(2.0,'double_step')]:
        step=p*factor
        for j in range(int(np.floor((lo-epoch)/step))-1,int(np.ceil((hi-epoch)/step))+2):
            c=epoch+j*step
            if not lo+.5<c<hi-.5:continue
            if any(abs(c-v)<.25 for v in times):continue
            m=metric(sec,c);m['test']=label;m['j']=j;tests.append(m)
result=dict(tic=tic,sources=sources,events=events,photometric_step_days=float(p),step_epoch_btjd=float(epoch),step_fit_rms_minutes=float(np.sqrt(np.mean(resid**2))),aliases_tested=['P/2 extra windows','P step','2P same-kind alternative'],window_tests=tests,note='Window losses are local SAP metrics, not an orbital fit. A 2P orbit can alternate indistinguishable eclipse kinds; source-specific Gaia orbit remains a separate hypothesis.')
(O/'lead-q011-clock.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('P',p,'epoch',epoch,'events',[(e['measured_minimum_btjd'],e['core_depth_ppt']) for e in events]);print('covered half-extra',[(x['center_btjd'],x['loss_ppt']) for x in tests if x['test']=='half_step_extra' and x['covered']][:30]);print('uncovered count',sum(not x['covered'] for x in tests))
