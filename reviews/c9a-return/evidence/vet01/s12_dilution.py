# s12: undiluted depths for TIC 195865529 (TESS contamination ratio 0.37): divide each pipeline's measured depth (s11) by the
# target's flux fraction in that pipeline's aperture: TESScut = catalogue scene model (s9 method) and fitted scene (s8);
# TASOC = 1 - AP_CONT (header); QLP = unknown -> if the corrected TESScut/TASOC depths equal QLP, QLP SAP is effectively deblended.
import json, csv, glob, numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from scipy.special import erf
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet01'
def gpsf(X,Y,x0,y0,s):
    a=lambda u,c:0.5*(erf((u+0.5-c)/(np.sqrt(2)*s))-erf((u-0.5-c)/(np.sqrt(2)*s)))
    return a(X,x0)*a(Y,y0)
R=json.load(open('s11_depths.json'))
for tic in ['195865529','468181994']:
    J=json.load(open(f'pix/pix_{tic}.json'))
    TIC=[r for r in csv.DictReader(open(f'tic_neighbours_{tic}.csv')) if r['disposition']!='DUPLICATE']
    print('='*20,tic,' (contratio in TIC v8.2 for target:',TIC[0]['contratio'],')')
    cP=[];cS=[];qP=[];qS=[]
    for s in J:
        f=glob.glob(f'{D}/{tic}/tesscut/tess-s{int(s):04d}-*.fits')[0]; w=WCS(fits.getheader(f,2)); img=np.load(f'pix/img_{tic}_s{s}.npz'); ap=img['ap']
        x0,y0=w.world_to_pixel_values(float(TIC[0]['ra']),float(TIC[0]['dec'])); dx,dy=float(img['xT'])-x0,float(img['yT'])-y0
        Y,X=np.mgrid[0:ap.shape[0],0:ap.shape[1]]; sig=J[s]['sigma']
        fl=[10**(-0.4*float(r['Tmag']))*gpsf(X,Y,*[v+o for v,o in zip(w.world_to_pixel_values(float(r['ra']),float(r['dec'])),(dx,dy))],sig)[ap].sum() for r in TIC]
        fc=fl[0]/sum(fl); ff=J[s]['frac_target']
        dP,eP,_=R[f'{tic}_P_TESScut-ap_{s}']; dS,eS,_=R[f'{tic}_S_TESScut-ap_{s}']
        q=R.get(f'{tic}_P_QLP-SAP_{s}'); qs=R.get(f'{tic}_S_QLP-SAP_{s}')
        print(f'  s{s}: target fraction in r=1.5px aperture: catalogue {fc:.3f}, fitted scene {ff:.3f} | TESScut depth P {dP*1e3:.1f} S {dS*1e3:.1f} ppt -> undiluted (catalogue) P {dP/fc*1e3:.1f} S {dS/fc*1e3:.1f}; (fitted) P {dP/ff*1e3:.1f} S {dS/ff*1e3:.1f} | QLP SAP P {q[0]*1e3 if q else float("nan"):.1f} S {qs[0]*1e3 if qs else float("nan"):.1f}')
        cP.append(dP/fc); cS.append(dS/fc)
        if q: qP.append(q[0]); qS.append(qs[0])
    print(f'  TESScut undiluted (catalogue frac): P mean {np.mean(cP)*1e3:.1f} sd {np.std(cP,ddof=1)*1e3:.1f} ppt; S mean {np.mean(cS)*1e3:.1f} sd {np.std(cS,ddof=1)*1e3:.1f} ppt; S/P {np.mean(cS)/np.mean(cP):.3f}')
    print(f'  QLP SAP: P mean {np.mean(qP)*1e3:.1f} sd {np.std(qP,ddof=1)*1e3:.1f}; S mean {np.mean(qS)*1e3:.1f} sd {np.std(qS,ddof=1)*1e3:.1f}; S/P {np.mean(qS)/np.mean(qP):.3f}')
    if tic=='195865529':
        f=glob.glob(f'{D}/{tic}/**/hlsp_tasoc*cbv-lc.fits',recursive=True)[0]; apc=fits.getheader(f,0)['AP_CONT']
        dP=R[f'{tic}_P_TASOC-raw_15'][0]; dS=R[f'{tic}_S_TASOC-raw_15'][0]
        print(f'  TASOC s15: AP_CONT {apc:.3f} -> target fraction {1-apc:.3f}; raw depth P {dP*1e3:.1f} S {dS*1e3:.1f} -> undiluted P {dP/(1-apc)*1e3:.1f} S {dS/(1-apc)*1e3:.1f} ppt')
