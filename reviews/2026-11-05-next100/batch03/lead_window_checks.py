"""Actual cadence endpoints, gaps and flux positivity near every selected dip."""
import csv, json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
for row in csv.DictReader((B/'queue.csv').open(encoding='utf8',newline='')):
    tic=row['tic']; D=B/tic; d=json.loads((D/'lead-measurements.json').read_text(encoding='utf8'))
    src={int(Path(x['path']).stem.split('_s')[-1]):x for x in d['source_receipts']}
    out=[]
    for sec in sorted({x['sector'] for x in d['screen_flagged_dips']}):
        rec=src[sec];fp=Path(rec['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==rec['sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        valid=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[valid];f=f[valid]
        cad=float(np.median(np.diff(t)))
        for ev in [x for x in d['screen_flagged_dips'] if x['sector']==sec]:
            c=ev.get('measured_center_btjd',ev['screen_center_btjd']);dur=ev['screen_duration_days']
            radius=max(.15,min(.8,dur/2)); core=(t>=c-radius)&(t<=c+radius)
            l=(t>=c-3*radius)&(t<c-radius);r=(t>c+radius)&(t<=c+3*radius)
            tw=t[(t>=c-3*radius)&(t<=c+3*radius)]
            gap=[(float(tw[i]),float(tw[i+1])) for i in np.where(np.diff(tw)>3*cad)[0]]
            expected=lambda lo,hi:max(1,int(round((hi-lo)/cad))+1)
            out.append({'sector':sec,'screen_center_btjd':ev['screen_center_btjd'],'fit_center_btjd':c,'core_halfwidth_days':radius,'cadence_days':cad,'core_actual':int(core.sum()),'core_expected':expected(c-radius,c+radius),'left_actual':int(l.sum()),'left_expected':expected(c-3*radius,c-radius),'right_actual':int(r.sum()),'right_expected':expected(c+radius,c+3*radius),'local_gaps_over_three_cadences':gap,'flux_median':float(np.median(f)),'flux_positive':bool(np.all(f>0)),'source_sha256':rec['sha256']})
    (D/'lead-window-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print(row['sample_id'],len(out))
