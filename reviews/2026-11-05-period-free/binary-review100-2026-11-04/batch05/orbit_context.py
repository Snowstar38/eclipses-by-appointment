"""Full cached-sector SAP context with Gaia predicted conjunctions."""
import json, math
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
for d in sorted(B.iterdir()):
    if not d.is_dir() or not (d/'raw-inspection.json').exists():continue
    tic=d.name;src=json.loads((d/'raw-inspection.json').read_text())
    g=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())['target']['gaia']
    P=float(g['period'])
    if not all(g.get(k) not in (None,'') for k in ('eccentricity','arg_periastron','t_periastron')):
        (d/'orbit-context.json').write_text(json.dumps({'tic':tic,'gaia_period_days':P,'gaia_conjunction_predictions':[], 'note':'Gaia orbital phase elements absent; period only.'},indent=2)+'\n')
        print(tic,'no Gaia phase',flush=True)
        continue
    e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=389+float(g['t_periastron'])
    bases=[]
    for kind,nu in [('A',math.pi/2-w),('B',3*math.pi/2-w)]:
        E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
        bases.append((kind,tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*P))
    panels=[];preds=[]
    for s in src['sectors']:
        if 'path' not in s:continue
        with fits.open(s['path'],memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
        f=f/np.median(f);panels.append((s['sector'],t,f))
        for kind,base in bases:
            for n in range(math.ceil((min(t)-base)/P),math.floor((max(t)-base)/P)+1):
                pred=base+n*P
                near=abs(t-pred)<.5;side=(abs(t-pred)>.8)&(abs(t-pred)<1.8)
                rec={'sector':s['sector'],'kind':kind,'predicted_btjd':pred,'n_core_quality0':int(sum(near)),
                     'n_side_quality0':int(sum(side))}
                if sum(near)>5 and sum(side)>10:
                    rec['core_side_delta_ppt']=float(1000*(np.median(f[near])-np.median(f[side])))
                preds.append(rec)
    fig,axes=plt.subplots(len(panels),1,figsize=(10,max(3,1.85*len(panels))),squeeze=False)
    for ax,(sector,t,f) in zip(axes[:,0],panels):
        skip=max(1,len(t)//1500);ax.scatter(t[::skip],f[::skip],s=2,alpha=.6)
        ax.set_title(f's{sector} raw SAP quality0',fontsize=8)
        for p in preds:
            if p['sector']==sector:ax.axvline(p['predicted_btjd'],color='r' if p['kind']=='A' else 'purple',lw=.7)
    fig.tight_layout();fig.savefig(d/'orbit-context.png',dpi=105);plt.close(fig)
    (d/'orbit-context.json').write_text(json.dumps({'tic':tic,'gaia_period_days':P,'gaia_conjunction_predictions':preds,'note':'Red=A, purple=B Gaia edge-on conjunction approximation. Diagnostic phase windows, not measured eclipse centers. Entire cached sectors shown in raw SAP QUALITY=0; gaps can hide events.'},indent=2)+'\n')
    print(tic,len(panels),len(preds),flush=True)
