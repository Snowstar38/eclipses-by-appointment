import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent
downloads=json.loads((here/'alternative-downloads.json').read_text())
summary=[]
for r in downloads:
    if r['status']!='ok':continue
    tic=r['tic'];sector=r['sector'];path=Path(r['path'])
    assert hashlib.sha256(path.read_bytes()).hexdigest()==r['sha256']
    m=json.loads((here/tic/'measurements.json').read_text())
    ev=next(e for e in m['events'] if e.get('timing_usable') and e['sector']==sector
            and e['kind']==('B' if tic=='109560492' else 'A'))
    tc=ev['mid_btjd'];width=ev['fit_parameters'][4];ingress=ev['fit_parameters'][5]
    with fits.open(path) as h:
        d=h[1].data;t=np.array(d['TIME'],float)
        cols=d.columns.names;quality=np.array(d['QUALITY'],int) if 'QUALITY' in cols else np.zeros(len(t),int)
        series={k:np.array(d[k],float) for k in ('SAP_FLUX','PDCSAP_FLUX','FLUX') if k in cols}
    fig,ax=plt.subplots(figsize=(8,4));measure=[]
    for name,f in series.items():
        valid=np.isfinite(t)&np.isfinite(f)&(f>0)&(quality==0)&(abs(t-tc)<max(1.,3*width))
        x=t[valid]-tc;y=f[valid];far=abs(x)>max(width,.2)
        if len(x)<25 or far.sum()<12:continue
        y=y/np.median(y[far]);shape=np.clip((width/2-abs(x))/ingress,0,1)
        design=np.column_stack((np.ones(len(x)),x,-shape))
        coef=np.linalg.lstsq(design,y,rcond=None)[0];res=y-design@coef
        err=np.std(res[far])*np.sqrt(np.linalg.inv(design.T@design)[2,2])
        realized=coef[2]*min(1,width/(2*ingress))
        measure.append(dict(flux_column=name,depth_ppt=float(realized*1000),
                            conditional_error_ppt=float(err*1000),n_points=len(x),
                            quality_flags_available='QUALITY' in cols))
        ax.plot(x,y,'.',ms=2,alpha=.5,label=f'{name} {realized*1000:.1f} ppt')
    ax.set_xlim(-.8,.8);ax.set_title(f'TIC {tic} {r["provenance"]} s{sector}; QLP {ev["depth_ppt"]:.1f} ppt')
    ax.set_xlabel(f'Days from QLP measured {ev["kind"]} center');ax.set_ylabel('normalized flux')
    ax.legend(fontsize=8);fig.tight_layout();fig.savefig(here/tic/'alternative-event.png',dpi=140);plt.close(fig)
    summary.append(dict(tic=tic,sector=sector,provenance=r['provenance'],
                        same_photons_independent_reduction=True,
                        qlp_depth_ppt=ev['depth_ppt'],columns=measure,
                        limitation='Template shape and timing fixed to QLP fit; conditional error omits correlated noise and aperture blending. TARS lacks QUALITY column.' if r['provenance']=='TARS' else 'Template shape and timing fixed to QLP fit; conditional error omits correlated noise and aperture blending.'))
(here/'alternative-comparison.json').write_text(json.dumps(summary,indent=2))
for s in summary:print(s['tic'],s['provenance'],s['columns'])
