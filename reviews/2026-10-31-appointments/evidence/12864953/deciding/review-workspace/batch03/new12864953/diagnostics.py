from pathlib import Path
import json,numpy as np
from astropy.io import fits
out=Path(__file__).parent
with fits.open(out/'tesscut_s107.fits') as h:
 z=h[1].data;t=np.array(z['TIME']);F=np.array(z['FLUX']);q=np.array(z['QUALITY']);B=np.array(z['FLUX_BKG'])
tc=4271.616860567667;x=t-tc
inn=(abs(x)<.07);outer=(abs(x)>.18)&(abs(x)<.8);valid=np.isfinite(t)&(q==0)
bk=np.nanmedian(np.sort(F.reshape(len(t),-1),axis=1)[:,:32],axis=1)
p=np.polyfit(x[outer&valid],bk[outer&valid],2);res=bk-np.polyval(p,x)
g=json.loads(Path('[local path omitted] 5.1/made/appointments/vet12864953/gaia.json').read_text());nbs=g['nb'];target=float(g['src'][0]['phot_g_mean_mag'])
brightest=min([float(n['phot_g_mean_mag']) for n in nbs if n.get('source_id')!=g['src'][0]['source_id'] and float(n.get('phot_g_mean_mag') or 99)>target+.01])
P=31.632857663754894
result=dict(in_window_cadences=int(inn.sum()),in_window_flagged=int((inn&(q!=0)).sum()),dark_pixel_background_residual_in=float(np.median(res[inn&valid])),dark_pixel_background_residual_oot_sd=float(np.std(res[outer&valid])),gaia_period_sigma=(P-31.62452)/.00589,old_pair_B_minus_A_phase=float(((3196.0997-3204.1016)/P)%1),gaia_phase_mean=.7735,gaia_phase_sd=.0079,gaia_new_B_prediction_btjd=4270.901,gaia_new_B_prediction_sd=.714,new_B_oc_sigma=(tc-4270.901)/.714,brightest_neighbour_G=brightest,neighbour_required_fractional_eclipse_at_10p8ppt=.0108*10**(.4*(brightest-target)),notes='Neighbour list is historical Gaia cone; bright lower-edge source in cutout has no corresponding concentrated eclipse deficit. Background metric uses darkest32 pixels; diagnostic not independent astrophysical evidence. Phase uses new measured period; grazing model radii change <0.02% when period changes0.026%.')
(out/'diagnostics.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
