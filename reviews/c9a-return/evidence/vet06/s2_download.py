# Direct MAST Download/file fetch of QLP and TESS-SPOC HLSP light curves (lightkurve's search hung at MAST;
# archive.stsci.edu serves an incomplete TLS chain). Saves SAP QUALITY==0 arrays per star.
import requests, numpy as np, os, sys, time
from astropy.io import fits
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet06'
S={'468827621':([19,20,59,60,73],[19,20]),'416285595':([14,40,54,80,81],[40])}
def path(tic):
    t=f'{int(tic):016d}'; return f'{t[0:4]}/{t[4:8]}/{t[8:12]}/{t[12:16]}'
def fetch(uri,out):
    if os.path.exists(out) and os.path.getsize(out)>10000: return True
    for k in range(4):
        try:
            r=requests.get('https://mast.stsci.edu/api/v0.1/Download/file',params={'uri':uri},timeout=120)
            if r.ok and r.content[:6]==b'SIMPLE': open(out,'wb').write(r.content); return True
            print('  bad',r.status_code,uri[-60:])
        except Exception as ex: print('  retry',k,str(ex)[:120])
        time.sleep(5)
    return False
for tic,(qs,ss) in S.items():
    os.makedirs(f'{D}/{tic}',exist_ok=True); T=[];F=[];E=[];SS=[];P=[]
    items=[('QLP',s,f'mast:HLSP/qlp/s{s:04d}/{path(tic)}/hlsp_qlp_tess_ffi_s{s:04d}-{int(tic):016d}_tess_v01_llc.fits') for s in qs]
    items+=[('SPOC',s,f'mast:HLSP/tess-spoc/s{s:04d}/target/{path(tic)}/hlsp_tess-spoc_tess_phot_{int(tic):016d}-s{s:04d}_tess_v1_lc.fits') for s in ss]
    for pipe,s,uri in items:
        out=f'{D}/{tic}/{os.path.basename(uri)}'
        if not fetch(uri,out): print(tic,pipe,s,'FAILED'); continue
        h=fits.open(out); d=h[1].data; hd=h[0].header
        t=np.array(d['TIME'],float); f=np.array(d['SAP_FLUX'],float); q=np.array(d['QUALITY'])
        fe=np.array(d['SAP_FLUX_ERR'],float) if 'SAP_FLUX_ERR' in d.columns.names else np.full(len(t),np.nan)
        g=(q==0)&np.isfinite(f)&np.isfinite(t)&(f>0); med=np.median(f[g])
        print(f'{tic} {pipe} s{s} cam{hd.get("CAMERA")} n={len(t)} q0={g.sum()} cad={np.nanmedian(np.diff(t))*1440:.1f}min {t[g].min():.2f}-{t[g].max():.2f}')
        T.append(t[g]);F.append(f[g]/med);E.append(fe[g]/med);SS.append(np.full(g.sum(),s));P.append(np.full(g.sum(),pipe))
    np.savez(f'{D}/{tic}/lc_sap_q0.npz',t=np.concatenate(T),f=np.concatenate(F),e=np.concatenate(E),s=np.concatenate(SS),p=np.concatenate(P))
