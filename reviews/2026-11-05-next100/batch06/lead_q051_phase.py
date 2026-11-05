"""Bounded same-kind phase check for Q051 S32 opening and S98 event."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='373314632';D=B/tic
ctx=json.loads((D/'lead-context.json').read_text());p=37.086203094017314
screen98=4029.1502094603707;screen32=screen98-50*p
out={'gaia_period_days':p,'S98_screen_btjd':screen98,'S32_same_kind_projection_btjd':screen32,
     'approximate_visual_egress_intervals_btjd':{'S32':[2174.68,2174.91],'S98':[4029.73,4030.00]},
     'illustrative_egress_midpoints_btjd':{'S32':2174.795,'S98':4029.865},
     'conditional_periods_from_midpoints_days':{str(n):(4029.865-2174.795)/n for n in (49,50,51)},
     'caution':'Visual intervals are approximate transitions, not precision eclipse centers. Same-kind identity is insecure; projection uses Gaia period and screen time, not a measured photometric ephemeris. S32 opening lacks ingress and left baseline; KSPSAP suppresses its raw rise.'}
fig,axs=plt.subplots(2,1,figsize=(11,7))
for ax,sec,center,lo,hi in [(axs[0],32,screen32,2174.2,2177.0),(axs[1],98,screen98,4027.5,4031.0)]:
    s=next(x for x in ctx['sectors'] if x['sector']==sec);fp=Path(s['source_path'])
    assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
    with fits.open(fp,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int);names=h[1].columns.names
        raw=np.asarray(a['SAP_FLUX'],float)
        good=np.isfinite(t)&np.isfinite(raw)&(raw>0)&(q==0)
        m=good&(t>=lo)&(t<=hi)
        tt=t[m];rec={'sector':sec,'source_sha256':s['source_sha256'],
                    'available_first_btjd':float(t[good].min()),'available_last_btjd':float(t[good].max()),
                    'window_first_btjd':float(tt.min()),'window_last_btjd':float(tt.max()),
                    'projection_btjd':center,'columns':{}}
        for name in ('SAP_FLUX','KSPSAP_FLUX','DET_FLUX','SYS_RM_FLUX'):
            if name not in names:continue
            v=np.asarray(a[name],float)[m];finite=np.isfinite(v)&(v>0)
            if finite.sum()<3:continue
            base=np.median(v[finite]);y=v[finite]/base
            ax.plot(tt[finite],y,'.',ms=2,label=name)
            rec['columns'][name]={'points':int(finite.sum()),'median':float(base),
                                  'first_flux_relative':float(y[0]),'last_flux_relative':float(y[-1])}
        rec['gaps_over_3cadences']=[[float(tt[i]),float(tt[i+1])] for i in np.where(np.diff(tt)>3*s['cadence_days'])[0]]
        out[f'S{sec}']=rec
    ax.axvline(center,color='black',lw=.7,label='Gaia-period projection' if sec==32 else 'screen center')
    ax.set_title(f'Q051 S{sec} actual quality-zero flux; projected/screen time {center:.5f}');ax.set_ylabel('flux/local median');ax.legend(fontsize=8)
axs[1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(D/'lead-phase-followup.png',dpi=150);plt.close(fig)
(D/'lead-phase-followup.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('S32 projection',screen32,'coverage',out['S32']['window_first_btjd'],out['S32']['window_last_btjd'])
