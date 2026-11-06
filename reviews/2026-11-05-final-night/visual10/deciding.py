from pathlib import Path
import csv,json,math,hashlib,requests
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())};H=B.parent.parent/'binary-exploration-2026-11-04/bulk-results';cl=json.loads((B/'lead-clocks.json').read_text());N={r['source_id']:r for r in csv.DictReader((B/'shared-catalogues/gaia_nss-pending.csv').open())};out={}
for tic,sec,c,iw,b0,b1 in [('233405109',76,3385.51,.2,.65,1.1),('27681485',44,2505.60,.65,1.4,2.4)]:
 r=Q[tic];p=B/tic/f'lead-cut-s{sec}.fits';a=fits.open(p);d=a[1].data;t=np.array(d['TIME']);f=np.array(d['FLUX']);q=np.array(d['QUALITY']);xy=WCS(a[2].header).all_world2pix([[float(r['ra_deg']),float(r['dec_deg'])]],0)[0];a.close();ok=(q==0)&np.isfinite(t);inn=ok&(abs(t-c)<iw);base=ok&(abs(t-c)>b0)&(abs(t-c)<b1);med=np.nanmedian(f[base],axis=0);diff=med-np.nanmedian(f[inn],axis=0);yy,xx=np.indices(med.shape);aper=(xx-xy[0])**2+(yy-xy[1])**2<1.6**2;bg=(xx-xy[0])**2+(yy-xy[1])**2>3**2;flux=np.nansum(f[:,aper],axis=1)-np.nanmedian(f[:,bg],axis=1)*sum(aper.ravel());norm=flux/np.median(flux[base]);peak=list(map(int,np.unravel_index(np.nanargmax(diff),diff.shape)[::-1]));depth=float(1-np.median(norm[inn]));
 fig,ax=plt.subplots(1,3,figsize=(12,3.5));im=ax[0].imshow(med,origin='lower');fig.colorbar(im,ax=ax[0]);im=ax[1].imshow(diff,origin='lower');fig.colorbar(im,ax=ax[1]);
 for aa in ax[:2]:aa.plot(*xy,'rx',ms=12);aa.grid(alpha=.2)
 ax[2].plot(t[ok]-c,norm[ok],'.',ms=1);ax[2].set_xlim(-b1,b1);ax[2].set_ylim(1-max(.02,depth*2),1+max(.01,depth));ax[2].set_title('custom 1.6px SAP, same photons');fig.suptitle(f'{tic} S{sec}; target red X');fig.tight_layout();fig.savefig(B/tic/'lead-pixels.png',dpi=140);plt.close(fig)
 pix=dict(target_xy=xy.tolist(),peak_deficit_xy=peak,custom_depth=depth,n_in=int(sum(inn)),n_baseline=int(sum(base)),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),interpretation='static local baseline difference; long-term variable slopes/background limit exact centroid')
 # preserve full Gaia row and mean conjunction offsets; no bogus independent covariance
 g=N[r['gaia_dr3']];P=float(g['period']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=float(g['t_periastron'])+389;epoch=cl[tic]['epoch_btjd'];cc=[]
 for kind in [0,1]:
  nu=(math.pi/2 if kind==0 else 3*math.pi/2)-w;E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));tc=tp+((E-e*math.sin(E))%(2*math.pi))*P/(2*math.pi);cy=round((epoch-tc)/P);cc.append(dict(kind=kind,reference=tc,cycle=cy,offset_d=epoch-tc-cy*P,period_accumulation_formal_d=abs(cy)*float(g['period_error'])))
 # actual predicted intermediate cycles for integer aliases; q0 sampled centered core and bilateral sidebands
 series=[]
 for rr in json.loads((H/f'{tic}.json').read_text())['files']:
  with fits.open(rr['path']) as h:
   d=h[1].data;tt=np.array(d['TIME']);ff=np.array(d['SAP_FLUX']);qq=np.array(d['QUALITY'])
  z=(qq==0)&np.isfinite(tt)&np.isfinite(ff)&(ff>0);series.append((rr['sector'],tt[z],ff[z]))
 aliases=[];dur=.7 if tic=='233405109' else 2.1
 for div in range(1,11):
  pp=cl[tic]['period_d']/div;wins=[]
  for sector,tt,ff in series:
   for n in range(math.ceil((min(tt)-epoch)/pp),math.floor((max(tt)-epoch)/pp)+1):
    cen=epoch+n*pp;core=abs(tt-cen)<dur*.3;side=(abs(tt-cen)>dur*.7)&(abs(tt-cen)<dur*1.1);left=(tt<cen-dur*.7)&side;right=(tt>cen+dur*.7)&side
    cov=core.sum()>5 and left.sum()>3 and right.sum()>3 and (max(tt[core])-min(tt[core])>dur*.45 if core.any() else False)
    depth=float(1-np.median(ff[core])/np.median(ff[side])) if cov else None
    wins.append(dict(sector=sector,cycle=n,center=cen,core_n=int(sum(core)),covered=bool(cov),depth=depth,intermediate=(n%div!=0)))
  aliases.append(dict(divisor=div,period_d=pp,windows=wins))
 out[tic]=dict(pixels=pix,gaia_row=g,mean_conjunctions=cc,alias_coverage=aliases,geometry_limit='Mean edge-on conjunction approximation only; Gaia covariance not yet propagated. Period match alone does not establish association.')
 print(tic,pix,cc,flush=True)
(B/'lead-deciding-checks.json').write_text(json.dumps(out,indent=2))
