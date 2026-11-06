"""Retain all fresh-source scores and render raw windows for independent triage."""
from pathlib import Path
import json,csv,hashlib
from collections import Counter
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parent/'fresh-band-next1000';O=W/'triage';O.mkdir(exist_ok=True)
pop=json.loads((W/'population.json').read_text())['targets'];out=[]
for tic,tg in pop.items():
    ap=json.loads((W/'appointment-results'/f'{tic}.json').read_text());bulk=json.loads((W/'bulk-results'/f'{tic}.json').read_text())
    b=ap.get('best') or {};n=ap.get('null') or {};reasons=[]
    if not b:reasons=['no_window_best']
    else:
        if b['snr']<8:reasons.append('snr<8')
        if b['far'] is None or not .6<=b['far']<=1.6:reasons.append('far_ratio')
        if not b['halves']:reasons.append('halves')
        if not ((b.get('dt_sigma') is not None and abs(b['dt_sigma'])<=3) or abs(b['dphase'])<=.03):reasons.append('conjunction_offset')
        if n.get('exceed',0)>0:reasons.append('null_exceedance')
        if ap.get('z') is not None and ap['z']<8 and n:reasons.append('low_empirical_z')
        if b['dur_h']>=14 and (b['far'] is None or abs(b['far']-1)>.25):reasons.append('maximum_box_shape')
    wins=[dict(w,sector=f['sector'],path=f['path']) for f in bulk['files'] if f['status']=='ok' for w in f['windows'] if w['kind']=='dip']
    flagged=[w for w in wins if w['flag']]
    row={'tic':tic,'control':tg['control'],'gaia_dr3':tg['gaia']['source_id'],'gaia_period':tg['gaia']['period'],'gaia_G':tg['gaia']['phot_g_mean_mag'],'files':len(tg['files']),'appointment_shape_pass':not reasons,'appointment_reasons':';'.join(reasons),'appointment_common_mode':'NOT_CHECKED; shape pass is not original full triage pass','appointment_snr':b.get('snr'),'appointment_z':ap.get('z'),'dip_flag_sectors':len({w['sector'] for w in flagged}),'best_contrast':max([w['contrast'] for w in wins],default=0),'classification':'UNREVIEWED'}
    out.append(row)
    # Three distinct-sector raw windows ranked only for display, all sources retained.
    picks=[]
    for w in sorted(wins,key=lambda w:(w['flag'],w['contrast']),reverse=True):
        if w['sector'] not in [x['sector'] for x in picks]:picks.append(w)
        if len(picks)==3:break
    row['_picks']=picks
science=[r for r in out if not r['control']]
# Display order is frozen by TIC, not outcome; controls separately at end.
science.sort(key=lambda r:int(r['tic']));ordered=science+[r for r in out if r['control']]
for start in range(0,len(ordered),8):
    chunk=ordered[start:start+8];fig,axs=plt.subplots(len(chunk),3,figsize=(15,2.25*len(chunk)),squeeze=False)
    for rr,r in enumerate(chunk):
        for cc,ax in enumerate(axs[rr]):
            if cc>=len(r['_picks']):ax.set_axis_off();continue
            w=r['_picks'][cc]
            with fits.open(w['path']) as hd:
                d=hd[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'])
            m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-w['time'])<max(4*w['duration'],1))
            if m.any():ax.plot(t[m]-w['time'],f[m]/np.median(f[m]),'.',ms=1.7)
            ax.axvspan(-w['duration']/2,w['duration']/2,color='r',alpha=.1)
            ax.set_title(f"TIC{r['tic']} S{w['sector']} t={w['time']:.3f}, box={w['duration']:.2f}d",fontsize=9)
            ax.tick_params(labelsize=7)
    fig.suptitle('Raw SAP quality0; selected local windows, not fitted eclipses. Sheet '+str(start//8+1),fontsize=11)
    fig.tight_layout();fig.savefig(O/f'sheet-{start//8+1:02d}.png',dpi=110);plt.close(fig)
    for r in chunk:r['sheet']=f'triage/sheet-{start//8+1:02d}.png'
for r in out:r.pop('_picks')
with (W/'screening-summary.csv').open('w',encoding='utf8',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=list(out[0]));wr.writeheader();wr.writerows(out)
summary={'science':len(science),'controls':len(out)-len(science),'science_appointment_shape_pass':sum(r['appointment_shape_pass'] for r in science),'science_any_event_dip':sum(r['dip_flag_sectors']>0 for r in science),'science_multisector_dips':sum(r['dip_flag_sectors']>=2 for r in science),'controls_results':[r for r in out if r['control']],'qualifications':'Shape-pass omits original common-mode veto; event flags are not classifications. Every target remains in summary. Limited8-sector subset selected without flux inspection. No occurrence/completeness inference.'}
(W/'screening-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8');print(json.dumps(summary,indent=2))


