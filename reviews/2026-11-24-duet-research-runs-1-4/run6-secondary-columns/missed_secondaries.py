"""Run 6b (Duet): secondary eclipses visible in the house's review sheets for rows whose
host-table entry says "no secondary found".  Panel 3 of sheets/TIC-<tic>.png is the light
curve folded at P with its binned median (black line), phase -0.25..0.75.  This digitises
the median line, measures the primary dip at phase 0 and the deepest other dip, and
reports the other dip's phase and depth in units of the line's out-of-eclipse scatter.
Pixel depths are relative (the y axis is autoscaled; a clipped primary makes the ratio an
upper bound).  Needs numpy and Pillow.  Run from the repo root:
    python3 reviews/2026-11-24-duet-research-runs-1-4/run6-secondary-columns/missed_secondaries.py
Writes missed-secondaries.csv and secondary-seen-not-tabled.csv next to this script."""
import csv,sys,os
import numpy as np
from PIL import Image
import os
HERE=os.path.dirname(os.path.abspath(__file__))
repo=sys.argv[1] if len(sys.argv)>1 else os.path.normpath(os.path.join(HERE,'../../..'))
d=repo+'/reviews/2026-11-23-pipeline-and-survey-review/'
host={x['tic']:x for x in csv.DictReader(open(d+'host-stars.csv'))}
X0,X1,Y0,Y1=80,789,447,589
def line(im):
    a=np.asarray(im.convert('RGB')).astype(int)[Y0+2:Y1-1,X0+2:X1-1]
    blk=a.sum(2)<150
    ys=np.array([np.nonzero(blk[:,j])[0].mean() if blk[:,j].any() else np.nan for j in range(blk.shape[1])])
    ph=-0.25+(np.arange(len(ys))+2)/(X1-X0)
    return ph,ys
out=[]
for f in sorted(os.listdir(d+'sheets')):
    x=host.get(f[4:-4])
    if x is None or 'Refit after visual review' in x['period_resolution']: continue
    if x['secondary_phase']: continue            # table already has a secondary
    ph,ys=line(Image.open(d+'sheets/'+f))
    ok=np.isfinite(ys)
    if ok.sum()<300: continue                     # median line not found (flat-scaled panel)
    P=float(x['adopted_period_days']); hw=max(float(x['duration_h'] or 1)/24/P/2,0.004)
    far=lambda c,w:np.abs(((ph-c+0.5)%1)-0.5)>w
    base=np.nanmedian(ys[far(0,4*hw)]); res=ys-base
    sig=1.4826*np.nanmedian(np.abs(res[far(0,4*hw)]))
    prim=np.nanmax(res[~far(0,1.5*hw)])
    m=far(0,2.5*hw)&ok
    # smooth over the box width before picking the other dip, to resist single-pixel noise
    k=max(int(hw*(X1-X0)),2); sm=np.convolve(np.nan_to_num(res,nan=0.0),np.ones(k)/k,mode='same')
    j=np.argmax(np.where(m,sm,-1e9)); sd=sm[j]
    out.append(dict(review_id=x['review_id'],tic=x['tic'],tier=x['physical_tier'],P_d=P,
       primary_px=round(prim,1),other_dip_phase=round(ph[j]%1,3),other_dip_px=round(sd,1),
       other_over_primary=round(sd/prim,3) if prim>0 else '',line_sigma_px=round(sig,2),
       other_dip_snr=round(sd/max(sig,0.3),1),period_resolution=x['period_resolution'][:100]))
out.sort(key=lambda r:-r['other_dip_snr'])
w=csv.DictWriter(open(os.path.join(HERE,'missed-secondaries.csv'),'w',newline=''),fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for r in out: print(r['review_id'],r['tier'][:4],r['P_d'],r['primary_px'],r['other_dip_phase'],r['other_dip_px'],r['other_over_primary'],r['line_sigma_px'],r['other_dip_snr'],'|',r['period_resolution'][:50])

# ---- Part 2: rows whose own visual note describes a secondary the table says is absent.
# Hand reading (Duet, run 6) of visual_reason; sheet phases from the digitisation above.
import math
def sep(ecosw):
    e=abs(ecosw); w=0.0 if ecosw>=0 else math.pi
    M=lambda f:(lambda E:E-e*math.sin(E))(2*math.atan(math.sqrt((1-e)/(1+e))*math.tan(f/2)))
    return ((M(1.5*math.pi-w)-M(0.5*math.pi-w))/(2*math.pi))%1.0
def e_min(p):
    t=abs(p%1-0.5); lo,hi=0.0,0.9999
    for _ in range(60):
        m=(lo+hi)/2; lo,hi=(lo,m) if abs(sep(m)-0.5)>=t else (m,hi)
    return hi
SEEN={  # review_id: (where the note puts it, sheet phase if measured here)
 'R1022':('P fold, 200 ppt vs 330 ppt primary',0.292),'R1029':('P fold, ~40% vs ~45% primary',0.839),
 'R1034':('P fold, deeper than the primary, phase ~0.54',0.544),'R1038':('P fold, phase 0.6',None),
 'R1634':('P fold, 16% at phase 0.46',0.462),'R1727':('P fold, ~25% vs ~27%',0.771),
 'R1757':('P fold, phase 0.75',0.746),'R987':('P fold, phase 0.5',None),'R1080':('P fold, weak, phase 0.5',None),
 'R1294':('P fold, small',None),'R1579':('P fold, shallow, phase 0.5',None),
 'R1040':('first read: weaker feature at the secondary phase',None),'R1042':('first read: weaker secondary',None),
 'R1202':('first read: weaker secondary feature',None),'R1253':('first read: shallow secondary',None),
 'R1279':('first read: shallow secondary feature',None),'R1352':('first read: shallower secondary between primaries',None),
 'R1356':('first read: much weaker secondary',None),'R1405':('first read: smaller secondary feature',None),
 'R1488':('first read: shallower secondary feature',None),'R1518':('first read: weaker secondary feature',None),
 'R1580':('first read: shallower secondary in the fold',None),'R1697':('first read: the secondary is shallower',None),
 'R1684':('first read: shallower secondary in the 2P fold (favours 2P)',None),
 'R1692':('first read: shallower intervening minima (P or 2P unclear)',None),
}
byid={x['review_id']:x for x in host.values()}
rows2=[]
for k,(note,ph) in SEEN.items():
    x=byid[k]
    rows2.append(dict(review_id=k,tic=x['tic'],tier=x['physical_tier'],adopted_period_d=x['adopted_period_days'],
        table_period_resolution=x['period_resolution'][:60],secondary_columns_blank=not x['secondary_phase'],
        visual_note=note,sheet_phase=ph if ph is not None else '',e_min=round(e_min(ph),2) if ph is not None else '',
        visual_reason=x['visual_reason'][:200]))
w=csv.DictWriter(open(os.path.join(HERE,'secondary-seen-not-tabled.csv'),'w',newline=''),fieldnames=list(rows2[0])); w.writeheader(); w.writerows(rows2)
print('\nrows whose visual note describes a secondary the table lacks:',len(rows2),
      'confirmed:',sum(r['tier']=='confirmed' for r in rows2),
      '| all blank secondary columns:',all(r['secondary_columns_blank'] for r in rows2),
      '| all say "no secondary found":',sum(r['table_period_resolution'].startswith('P: no secondary found') for r in rows2))
for r in rows2:
    if r['e_min']!='': print(' ',r['review_id'],r['adopted_period_d'],r['sheet_phase'],'e >=',r['e_min'])
