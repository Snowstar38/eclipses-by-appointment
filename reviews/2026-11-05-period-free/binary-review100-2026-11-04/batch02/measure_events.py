"""Measure selected raw-SAP minima; screening centers are only search seeds."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares

B = Path(__file__).resolve().parent
CASES = {
    '467963921': [(66,3119.89,.18),(94,3865.63,.18),(103,4163.93,.18)],
    '54494046': [(45,2527.8,2.2),(72,3264.4,2.2)],
}
for tic, events in CASES.items():
    src=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())
    output=[]
    for sector, seed, half in events:
        entry=next(x for x in src['target']['files'] if f'_s{sector:03d}.fits' in x['path'])
        fp=Path(entry['path']); digest=hashlib.sha256(fp.read_bytes()).hexdigest()
        if digest != entry['sha256']:raise ValueError('FITS hash mismatch '+str(fp))
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-seed)<half)
        x=t[good]-seed;y=f[good]/np.median(f[good]);
        # Local sloped baseline plus Gaussian dip. This is a descriptive center,
        # not a physical eclipse model or calibrated timing covariance.
        def model(p):
            level,slope,depth,center,width=p
            return level+slope*x-depth*np.exp(-.5*((x-center)/width)**2)
        init=[np.percentile(y,80),0,max(.001,np.percentile(y,80)-min(y)),0,.04 if half<1 else .8]
        lo=[.8,-.2,0,-half/2,.008 if half<1 else .15]
        hi=[1.2,.2,.2,half/2,.15 if half<1 else 2.0]
        fit=least_squares(lambda p:model(p)-y,init,bounds=(lo,hi),loss='soft_l1',f_scale=.002)
        p=fit.x
        output.append({'sector':sector,'seed_btjd':seed,'fit_center_btjd':float(seed+p[3]),
                       'gaussian_depth_ppt':float(1000*p[2]),'gaussian_sigma_days':float(p[4]),
                       'n_quality0':len(x),'residual_mad_ppt':float(1482.6*np.median(abs(fit.fun-np.median(fit.fun)))),
                       'fit_window_half_days':half,'fit_method':'local sloped baseline + Gaussian, robust least squares',
                       'fits_path':str(fp),'fits_sha256':digest})
    (B/tic/'measured-events.json').write_text(json.dumps({'tic':tic,'events':output,'caution':'Gaussian centers are descriptive; reported widths and fit residuals are not formal eclipse timing uncertainties.'},indent=2)+'\n')
    print(tic,[(v['sector'],round(v['fit_center_btjd'],5),round(v['gaussian_depth_ppt'],2)) for v in output])
