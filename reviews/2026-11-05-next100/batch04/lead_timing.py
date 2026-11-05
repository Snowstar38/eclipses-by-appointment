"""Local diagnostic timing for the two recurring-dip targets; not precision ephemerides."""
import json,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent

def model(p,x):
    a,b,d,c,s=p
    return a+b*x-d*np.exp(-.5*((x-c)/s)**2)

for tic in ('209429773','250561084'):
    D=B/tic;context=json.loads((D/'lead-context.json').read_text())
    npanels=sum(len([z for z in s['flags'] if z['kind']=='dip']) for s in context['sectors'])+(1 if tic=='250561084' else 0)
    out=[];fig,axs=plt.subplots(npanels,1,figsize=(9,2.1*npanels),squeeze=False)
    j=0
    for s in context['sectors']:
        events=[z for z in s['flags'] if z['kind']=='dip']
        if tic=='250561084' and s['sector']==85:
            events.append({'screen_center_btjd':3624.14,'kind':'dip','unflagged_followup':True})
        if not events:continue
        fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        valid=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[valid];f=f[valid]
        for ev in events:
            c=float(ev['screen_center_btjd']);rad=.34 if tic=='250561084' else (.65 if s['sector'] in (30,31) else 1.2)
            sel=np.abs(t-c)<rad;x=t[sel]-c;y=f[sel]/np.median(f[sel]);edge=np.abs(x)>rad*.65
            if edge.sum()<5:continue
            bb=np.polyfit(x[edge],y[edge],1);noise=max(1.4826*np.median(np.abs(y[edge]-np.polyval(bb,x[edge]))),1e-5)
            p0=[bb[1],bb[0],max(.001,bb[1]-np.min(y)),0,.04 if tic=='250561084' else .17]
            lo=[.8,-.2,0,-.25,.007];hi=[1.2,.2,.3,.25,.5]
            fit=least_squares(lambda p:(y-model(p,x))/noise,p0,bounds=(lo,hi),max_nfev=3000)
            p=fit.x;condition=float(np.linalg.cond(fit.jac.T@fit.jac));bounds=bool(any(abs(p[i]-lo[i])<1e-4 or abs(p[i]-hi[i])<1e-4 for i in range(5)))
            rec=dict(sector=s['sector'],screen_center_btjd=c,unflagged_followup=ev.get('unflagged_followup',False),diagnostic_center_btjd=float(c+p[3]),gaussian_sigma_days=float(p[4]),depth_ppt=float(p[2]*1000),sideband_mad_ppt=float(noise*1000),points=int(sel.sum()),left_sideband=int(np.count_nonzero(x<-rad*.65)),right_sideband=int(np.count_nonzero(x>rad*.65)),fit_condition=condition,fit_at_boundary=bounds,local_gap_endpoints=[[float(t[i]),float(t[i+1])] for i in np.where((np.diff(t)>3*s['cadence_days'])&(t[:-1]>c-rad)&(t[1:]<c+rad))[0]],source_sha256=s['source_sha256'])
            out.append(rec);ax=axs[j,0];j+=1;ax.plot(x,y,'.',ms=3);xx=np.linspace(-rad,rad,300);ax.plot(xx,model(p,xx),'r-',lw=1);ax.set_title(f"S{s['sector']} center {rec['diagnostic_center_btjd']:.5f} depth {rec['depth_ppt']:.1f} ppt; gap {bool(rec['local_gap_endpoints'])}",fontsize=9)
    fig.tight_layout();fig.savefig(D/'lead-timing.png',dpi=120);plt.close(fig)
    (D/'lead-timing.json').write_text(json.dumps(out,indent=2)+'\n')
    print(tic,[(x['sector'],round(x['diagnostic_center_btjd'],5),round(x['depth_ppt'],2),x['fit_at_boundary']) for x in out])
