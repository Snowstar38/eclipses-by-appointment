"""Independent raw QLP event fits for the frozen appointment batch.

Uses screening only to locate candidate windows. Fits QUALITY=0 SAP_FLUX
directly, with local linear baseline and a trapezoid. These are initial
measurements for visual audit, not classification or calibrated ephemerides.
"""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here = Path(__file__).resolve().parent
search = here.parent / 'search256'
queue = list(csv.DictReader((here / 'queue.csv').open()))
manifest = json.loads((here / 'SOURCE-SNAPSHOT.json').read_text())
screen = {r['tic']:r for r in map(json.loads, (search / 'screening.jsonl').open())}

def model(t, b, slope, amp, center, width, ingress):
    shape = np.clip((width/2 - np.abs(t-center))/ingress, 0, 1)
    return b + slope * (t-center) - amp*shape

for row in queue:
    tic = row['tic']
    out = here/tic
    out.mkdir(exist_ok=True)
    rec = screen[tic]
    source = manifest['targets'][tic]
    raw = {}
    for item in source['raw_fits']:
        path = Path(item['path'])
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256']
        sector = int(path.stem.split('_s')[-1])
        with fits.open(path) as h:
            d = h[1].data
            t = np.array(d['TIME'], float)
            f = np.array(d['SAP_FLUX'], float)
            q = np.array(d['QUALITY'], int)
        ok = np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
        raw[sector] = (t[ok], f[ok])
    events=[]
    for w in rec['windows']:
        b = w.get('best') or {}
        if not (b.get('snr') is not None and b['snr']>=8 and b.get('far') is not None
                and .6<=b['far']<=1.6 and b.get('halves')):
            continue
        sector = w['sector']; t, f = raw[sector]
        center0 = b['t']; width0 = b['dur_h']/24
        # Keep event and neighboring baseline; preserve same raw photons.
        radius = max(1.0, 5*width0)
        ix = np.abs(t-center0)<radius
        x=t[ix]; y=f[ix]
        if len(x)<30: continue
        baseline = np.abs(x-center0)>max(width0, .15)
        if baseline.sum()<12: continue
        scale=np.median(y[baseline]); y=y/scale
        noise=max(1.4826*np.median(abs(y[baseline]-np.median(y[baseline]))),1e-6)
        try:
            p0=[1,0,max(b['depth_ppm']/1e6,.0005),center0,width0,max(width0*.2,.015)]
            low=[.75,-1,0,center0-.35,.015,.005]
            high=[1.25,1,1,center0+.35,max(width0*2,.08),max(width0,.1)]
            par,cov=curve_fit(model,x,y,p0=p0,bounds=(low,high),
                              sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=30000)
            err=float(np.sqrt(cov[3,3])) if np.isfinite(cov[3,3]) and cov[3,3]>0 else None
            cadence=float(np.median(np.diff(t)))
            realized=par[2]*min(1,par[4]/(2*par[5]))
            event=dict(kind=w['kind'],sector=sector,predicted_btjd=w['tc'],
                       predicted_sigma_days=w['sig'],screen_center_btjd=center0,
                       screen_snr=b['snr'],screen_duration_hours=b['dur_h'],
                       mid_btjd=float(par[3]),formal_timing_error_days=err,
                       conservative_timing_error_days=max(err or 0,cadence/2),
                       depth_ppt=float(realized*1000),model_amplitude_ppt=float(par[2]*1000),
                       duration_hours=float(par[4]*24),ingress_parameter_hours=float(par[5]*24),
                       cadence_minutes=cadence*1440,oot_scatter_ppt=noise*1000,
                       n_points=len(x),fit_center_shift_from_screen_days=float(par[3]-center0),
                       fit_parameters=par.tolist())
            # A formal covariance at a fit boundary is not usable timing evidence.
            event['timing_usable']=bool(err is not None and err < par[4] and abs(par[3]-center0)<.3
                                        and par[4]<high[4]*.999 and par[5]<high[5]*.999)
            events.append(event)
            fig,ax=plt.subplots(figsize=(8,3.3))
            ax.plot(x,y,'.',ms=2,label='quality-zero raw SAP')
            xx=np.linspace(x.min(),x.max(),1000);ax.plot(xx,model(xx,*par),'r-',lw=1.5,label='local trapezoid')
            ax.axvline(w['tc'],color='green',ls=':',lw=1,label='Gaia prediction')
            ax.set_xlim(center0-.5,center0+.5)
            ax.set_title(f'TIC {tic} s{sector} {w["kind"]}: BTJD {par[3]:.5f}, {realized*1000:.1f} ppt')
            ax.set_xlabel('BTJD');ax.set_ylabel('SAP / local baseline');ax.legend(fontsize=7)
            fig.tight_layout();fig.savefig(out/f'event-{w["kind"]}-s{sector}-{center0:.3f}.png',dpi=140);plt.close(fig)
        except Exception as e:
            events.append(dict(kind=w['kind'],sector=sector,screen_center_btjd=center0,error=str(e)))
    (out/'measurements.json').write_text(json.dumps(dict(tic=tic,gaia_period_days=float(row['gaia_period_days']),
        depth_meaning='Realized central trapezoid loss = amplitude*min(1,width/(2*ingress)); local normalization only',
        timing_meaning='Formal covariance with half-cadence floor; not a calibrated total uncertainty',
        events=events),indent=2))
    print(tic,len(events),sum(e.get('timing_usable',False) for e in events),flush=True)
