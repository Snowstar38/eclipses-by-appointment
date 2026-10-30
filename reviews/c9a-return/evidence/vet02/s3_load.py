# Load all QLP and TESS-SPOC files; keep SAP flux with QUALITY==0; save per-star npz; print sector summary.
import glob, numpy as np
from astropy.io import fits
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet02'
for tic in ['470235665','379251709']:
    files=sorted(glob.glob(f'{D}/{tic}/**/*.fits',recursive=True))
    T=[];F=[];E=[];S=[];P=[];DF=[];B=[];CX=[];CY=[]
    print('TIC',tic)
    for f in files:
        h=fits.open(f); hd=h[0].header; d=h[1].data
        sec=hd['SECTOR']; pipe='QLP' if 'qlp' in f.lower() else 'SPOC'
        t=d['TIME']; q=d['QUALITY']; sap=d['SAP_FLUX']
        dn='PDCSAP_FLUX' if pipe=='SPOC' else ('KSPSAP_FLUX' if 'KSPSAP_FLUX' in d.names else 'DET_FLUX')
        det=d[dn]
        en='SAP_FLUX_ERR' if 'SAP_FLUX_ERR' in d.names else dn+'_ERR'
        e=d[en]
        bkg=d['SAP_BKG']
        cx=d['SAP_X'] if pipe=='QLP' else d['MOM_CENTR1']; cy=d['SAP_Y'] if pipe=='QLP' else d['MOM_CENTR2']
        m=(q==0)&np.isfinite(t)&np.isfinite(sap)&(sap>0)
        med=np.nanmedian(sap[m])
        T.append(t[m]);F.append(sap[m]/med);E.append(e[m]/med);S.append(np.full(m.sum(),sec));P.append(np.full(m.sum(),pipe))
        dd=det[m]/np.nanmedian(det[m]); DF.append(dd); B.append(bkg[m]/med); CX.append(cx[m]); CY.append(cy[m])
        cad=np.nanmedian(np.diff(t[m]))*1440
        print(f'  {pipe:4s} {dn:11s} s{sec:2d} cam{hd.get("CAMERA")} ccd{hd.get("CCD")} n_all={len(t)} n_q0={m.sum()} cad={cad:.1f}min span={t[m].min():.2f}-{t[m].max():.2f} rms_ppt={1e3*np.nanstd(np.diff(sap[m]/med))/np.sqrt(2):.2f}')
    np.savez(f'{D}/{tic}/lc_sap_q0.npz',t=np.concatenate(T),f=np.concatenate(F),e=np.concatenate(E),s=np.concatenate(S),p=np.concatenate(P),det=np.concatenate(DF),bkg=np.concatenate(B),cx=np.concatenate(CX),cy=np.concatenate(CY))
