"""Fit Q068 unflagged raw minima and plot every distinct observing occasion."""
import hashlib,json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; tic='341419787';D=B/tic
ctx=json.loads((D/'lead-context.json').read_text());sects={s['sector']:s for s in ctx['sectors']}
rec=json.loads((D/'lead-recurrence.json').read_text())['windows'];selected=[x for x in rec if x['best_nearby_depth_ppt'] is not None and x['best_nearby_depth_ppt']>2.2]
out=[];fig,axs=plt.subplots(len(selected),1,figsize=(10,2.5*len(selected)),squeeze=False)
for ax,r in zip(axs[:,0],selected):
    s=sects[r['sector']];p=Path(s['source_path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['source_sha256']
    with fits.open(p,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        alt=np.asarray(a['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in h[1].columns.names else None
    g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g];alt=alt[g] if alt is not None else None
    guess=r['best_nearby_center_btjd'];m=np.abs(t-guess)<.18;x=t[m]-guess;y=f[m]/np.median(f[m])
    def res(v):
        base,slope,depth,center,width=v
        return y-(base+slope*x-depth*np.exp(-.5*((x-center)/width)**2))
    lo=np.array([.95,-.05,0,-.08,.005]);hi=np.array([1.05,.05,.03,.08,.09])
    fit=least_squares(res,[1,0,.004,0,.03],bounds=(lo,hi),loss='soft_l1',f_scale=.001)
    v=fit.x;center=guess+v[3]
    ax.plot(x,y,'.',ms=3,label='SAP')
    xx=np.linspace(x.min(),x.max(),300);ax.plot(xx,v[0]+v[1]*xx-v[2]*np.exp(-.5*((xx-v[3])/v[4])**2),'-',lw=1,label='local fit')
    if alt is not None:
        aa=alt[m];good=np.isfinite(aa)&(aa>0)
        if good.sum()>5:ax.plot(x[good],aa[good]/np.median(aa[good]),'.',ms=2,alpha=.5,label='KSPSAP')
    ax.set_title(f"S{r['sector']} cycle {r['cycle']} center {center:.5f}, depth {v[2]*1000:.1f} ppt")
    ax.legend(fontsize=7);ax.set_ylabel('relative flux')
    out.append(dict(sector=r['sector'],cycle=r['cycle'],screen_predicted_btjd=r['predicted_btjd'],measured_center_btjd=float(center),depth_ppt=float(1000*v[2]/v[0]),sigma_days=float(v[4]),points=int(m.sum()),residual_rms_ppt=float(1000*np.std(fit.fun)),fit_at_bound=bool(np.any(np.isclose(v,lo,atol=1e-5)|np.isclose(v,hi,atol=1e-5)))))
fig.tight_layout();fig.savefig(D/'lead-extended-zooms.png',dpi=130);plt.close(fig)
good=[z for z in out if not z['fit_at_bound'] and z['depth_ppt']>1.5]
n=np.array([z['cycle'] for z in good]);c=np.array([z['measured_center_btjd'] for z in good]);coef=np.polyfit(n,c,1);oc=c-(coef[1]+coef[0]*n)
summary=dict(period_days=float(coef[0]),epoch_btjd=float(coef[1]),oc_days=oc.tolist(),oc_rms_days=float(np.std(oc)),fit_events=len(good))
(D/'lead-extended-timing.json').write_text(json.dumps(dict(events=out,summary=summary),indent=2)+'\n',encoding='utf8')
print(summary)
print(out)
