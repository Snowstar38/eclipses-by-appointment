import json,hashlib,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from pathlib import Path
B=Path(__file__).parent;p=B/'helper-255912894-s66.fits'; c=3100.2737469
with fits.open(p,memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME']);q=np.array(d['QUALITY']);f=np.array(d['FLUX'],float);w=WCS(h[2].header)
x,y=map(float,w.all_world2pix(258.80305873874653,-68.89193314417133,0));yy,xx=np.indices(f.shape[1:]); mask=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1);outer=np.hypot(xx-x,yy-y)>4
ok=np.isfinite(t)&(q==0);core=ok&(abs(t-c)<.055);side=ok&(abs(t-c)>.18)&(abs(t-c)<.4);diff=np.nanmedian(f[side],axis=0)-np.nanmedian(f[core],axis=0); bg=np.nanmedian(f[:,outer],axis=1); valid=np.isfinite(bg)&(bg!=0);lc=np.nansum(f[:,mask],axis=1); bglc=lc-9*bg
rec=dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),target_pixel=[x,y],core_n=int(core.sum()),side_n=int(side.sum()),outer_zero_fraction=float(np.mean(f[:,outer]==0)),background_zero_fraction=float(np.mean(bg==0)),outer_finite_fraction=float(np.mean(np.isfinite(f[:,outer]))),aperture_median=float(np.nanmedian(lc[side])),raw_depth_ppt=float(1000*(1-np.nanmedian(lc[core])/np.nanmedian(lc[side]))),background_subtracted_depth_ppt=float(1000*(1-np.nanmedian(bglc[core])/np.nanmedian(bglc[side]))),diff_image=np.round(diff,3).tolist())
ns=json.loads((B.parent/'shared-catalogues/gaia-neighbors.json').read_text())['targets']['T042'];rec['neighbors']=[]
for n in ns:
 nx,ny=map(float,w.all_world2pix(float(n['ra']),float(n['dec']),0));g=float(n['phot_g_mean_mag']) if n['phot_g_mean_mag'] not in [None,''] else np.nan;ratio=10**(-.4*(g-11.249632));
 if ratio>=.001: rec['neighbors'].append(dict(id=n['source_id'],g=g,pixel=[nx,ny],ratio=ratio))
fig,ax=plt.subplots(1,3,figsize=(14,4));ax[0].imshow(np.nanmedian(f[side],axis=0),origin='lower');ax[0].plot(x,y,'rx');ax[0].set_title('baseline raw');im=ax[1].imshow(diff,origin='lower',cmap='coolwarm');ax[1].plot(x,y,'kx');fig.colorbar(im,ax=ax[1]);ax[1].set_title('side minus core');win=ok&(abs(t-c)<.6);ax[2].plot(t[win]-c,lc[win]/np.nanmedian(lc[side]),'.',ms=3,label='raw');ax[2].plot(t[win]-c,bglc[win]/np.nanmedian(bglc[side]),'.',ms=2,label='outer bg');ax[2].legend();ax[2].set_title('3x3 local light curve');fig.tight_layout();fig.savefig(B/'helper-T042-pixels.png',dpi=130)
# conjunction phase assuming edge-on, Gaia t_periastron BJD - 2457389; omega convention may swap conjunction labels.
e=.5271739175298287;om=np.deg2rad(136.97576564562698);P=47.35116416322056;tp=7389-7000+11.390479343381033
con=[]
for u in [90,270]:
 ftrue=np.deg2rad(u)-om;E=2*np.arctan2(np.sqrt(1-e)*np.sin(ftrue/2),np.sqrt(1+e)*np.cos(ftrue/2));M=(E-e*np.sin(E))%(2*np.pi);pred=tp+P*M/(2*np.pi);phase=((c-pred)/P+.5)%1-.5;con.append(dict(u=u,reference_btjd=pred,event_minus_conjunction_phase=phase,event_minus_conjunction_days=phase*P))
rec['geometry']=dict(gaia_period=P,gaia_period_error=.023940172,t_periastron_btjd=tp,e=e,omega_deg=136.97576564562698,edge_on_conjunctions=con,caveat='Nominal values only; Gaia covariance and epoch propagation needed to assess uncertainty. Omega convention swaps labels.')
(B/'helper-T042-numeric.json').write_text(json.dumps(rec,indent=2));print(json.dumps({k:v for k,v in rec.items() if k!='diff_image'},indent=2))
