"""Raw/processed/background context for the two single-flag targets."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
fold={x['sample_id']:x for x in json.loads((B/'lead-fold-coverage.json').read_text())}
out=[]
for sid in ('T071','T072'):
 r=fold[sid];m=json.loads((B/r['tic']/'lead-numeric.json').read_text());src={s['sector']:s for s in m['sources']};selected=[x for x in r['records'] if x['core_time_bin_coverage']>.6]
 fig,axs=plt.subplots(len(selected),2,figsize=(12,len(selected)*2.8),squeeze=False)
 for (a,b),w in zip(axs,selected):
  with fits.open(src[w['sector']]['path']) as h:
   d=h[1].data; names=d.names;t=np.asarray(d['TIME'],float);q=np.asarray(d['QUALITY'],int);f=np.asarray(d['SAP_FLUX'],float);bkg=np.asarray(d['SAP_BKG'],float); alt=np.asarray(d['KSPSAP_FLUX' if 'KSPSAP_FLUX' in names else 'DET_FLUX'],float)
  c=w['pred_btjd'];span=max(2,6*r['core_half_width_days']);ok=np.isfinite(t)&(abs(t-c)<span)&np.isfinite(f)&(f>0)
  tt=t[ok]-c; ff=f[ok];qq=q[ok];bb=bkg[ok];aa=alt[ok];good=qq==0
  for y,name,alpha in [(ff,'SAP',1),(aa,'alternative',.6)]:
   g=good&np.isfinite(y)&(y>0);base=np.nanmedian(y[g]);a.plot(tt[g],y[g]/base,'.',ms=2,alpha=alpha,label=name)
  a.plot(tt[~good],ff[~good]/np.nanmedian(ff[good]),'x',ms=2,color='red',label='flagged')
  a.axvspan(-r['core_half_width_days'],r['core_half_width_days'],color='red',alpha=.08)
  a.set_title(f'{sid} s{w["sector"]} BTJD{c:.2f} cov{w["core_time_bin_coverage"]:.2f}');a.legend(fontsize=7);a.set_ylabel('relative flux');a.set_xlabel('days')
  b.plot(tt[good],bb[good],'.',ms=2);b.set_title('SAP background');b.set_xlabel('days');b.set_ylabel('background')
  out.append(dict(sample_id=sid,tic=r['tic'],sector=w['sector'],prediction_btjd=c,core_coverage=w['core_time_bin_coverage'],sap_core_minus_baseline_ppt=w.get('raw_core_minus_baseline_ppt'),background_min=float(np.nanmin(bb[good])),background_max=float(np.nanmax(bb[good])),plot=str(B/r['tic']/'lead-single-context.png')))
 fig.tight_layout();fig.savefig(B/r['tic']/'lead-single-context.png',dpi=130);plt.close(fig)
(B/'lead-single-context.json').write_text(json.dumps(out,indent=2)+'\n')
