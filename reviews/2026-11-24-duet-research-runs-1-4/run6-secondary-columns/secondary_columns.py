"""Run 6 (Duet): secondary-eclipse columns in the Nov 23 host table that disagree
with the row's own text, and secondaries that imply implausible eccentricities.
Reruns from repo files only.  Run from the repo root:
    python3 reviews/2026-11-24-duet-research-runs-1-4/run6-secondary-columns/secondary_columns.py
Writes secondary-column-flags.csv next to this script."""
import csv,sys,math,re
import os
HERE=os.path.dirname(os.path.abspath(__file__))
repo=sys.argv[1] if len(sys.argv)>1 else os.path.normpath(os.path.join(HERE,'../../..'))
rows=list(csv.DictReader(open(repo+'/reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv')))

def sep(ecosw):
    """Phase from primary to secondary eclipse, i=90 deg, e*sin(w)=0 (Sterne 1939)."""
    e=abs(ecosw); w=0.0 if ecosw>=0 else math.pi
    def M(f):
        E=2*math.atan(math.sqrt((1-e)/(1+e))*math.tan(f/2)); return E-e*math.sin(E)
    return ((M(1.5*math.pi-w)-M(0.5*math.pi-w))/(2*math.pi))%1.0
def e_min(phase):
    """Smallest eccentricity that puts the secondary at this phase (|phase-0.5| is
    largest at fixed e when sin w = 0, so this is a strict lower bound)."""
    t=abs(phase%1.0-0.5)
    lo,hi=0.0,0.9999
    for _ in range(60):
        m=(lo+hi)/2
        lo,hi=(lo,m) if abs(sep(m)-0.5)>=t else (m,hi)
    return hi
def e_env(P,E=0.98,Pcut=2.0):
    """Crude Mazeh (2008)-style upper envelope of close-binary eccentricity; screening only."""
    return 0.0 if P<=Pcut else E*(1-(P/Pcut)**(-2/3))
def text_says_no_secondary(x):
    t=(x['period_resolution']+' '+x['reason']+' '+x['limitation']).lower()
    return bool(re.search(r'no secondary|equal alternate dips|no other dip|twin',t))

# Hand reading (Duet, run 6) of the visual-review text of each refitted row whose
# secondary columns are filled.  methods.md says these columns "are blank where
# the refit and the visual reading disagree".
VISUAL={
 # reviewer says outright there is no secondary
 **{k:'visual: no secondary' for k in 'R947 R1663 R1765 R1329 R1665'.split()},
 # reviewer reads equal alternate dips / twin 2P, which presumes no secondary at P
 **{k:'visual: equal dips at 2P, no secondary mentioned' for k in 'R1498 R1604 R1716 R1519 R1236 R1774 R1782 R1770 R1789'.split()},
 # three-event long-period rows; visual silent; numeric fold was at another period
 **{k:'visual: silent (few events); column from fold at another period' for k in 'R1643 R1798 R1724 R1778'.split()},
 'R1611':'visual: secondary at 0.5, column elsewhere',
 'R1621':'visual: no secondary; ephemeris does not link epochs',
 'R1796':'visual: secondary at 0.79 (column = 1 - 0.79)',
 **{k:'visual agrees with column' for k in 'R1772 R1667 R1752 R1745 R1549 R1555 R1694 R1717 R1603 R1783 R1639 R956 R1093 R1557 R1756'.split()},
}
# What panel (6) of the house's review sheet (sheets/TIC-<tic>.png, "phase <table
# secondary>, +/- 3 durations") shows at the table's secondary phase (Duet, by eye).
SHEET={
 **{k:'primary eclipse fills the window (table secondary is the primary wing)' for k in 'R1643 R1611 R1498 R1765 R1604 R1665 R1621'.split()},
 'R1329':'primary egress at window edge',
 'R1724':'primary-depth dip from s19 only (cycle count across the gap is open)',
 **{k:'flat' for k in 'R947 R1716 R1519 R1236 R1770'.split()},
 'R1663':'sheet panel drawn at phase 0.5 instead; flat there',
 **{k:'flat median; dip in one sector only' for k in 'R1798 R1782 R1778 R1774'.split()},
 'R1789':'flat median; s59 scattered-light ramp only',
 'R1796':'panel drawn at 0.7932: real secondary there',
 'R997':'no dip at 0.754; rise into the pre-eclipse hump',
}
out=[]
for x in rows:
    if not x['secondary_phase']: continue
    P=float(x['adopted_period_days']); ph=float(x['secondary_phase'])
    refit='Refit after visual review' in x['period_resolution']
    em=e_min(ph); ev=e_env(P)
    g=re.search(r'secondary at phase ([0-9.]+)',x['period_resolution'])
    flags=[]
    vis=VISUAL.get(x['review_id'],'')
    if refit and vis and not vis.startswith('visual agrees'): flags.append(vis)
    if g and abs(float(g.group(1))-ph)>0.01:
        flags.append('text phase %s vs column %s%s'%(g.group(1),ph,' (= 1 - column)' if abs(float(g.group(1))+ph-1)<0.01 else ''))
    if em-ev>0.05: flags.append('needs e >= %.2f at P = %.3f d (envelope %.2f)'%(em,P,ev))
    if not flags: continue
    gnum=re.search(r'P=([0-9.]+) d',x['reason'])
    out.append(dict(review_id=x['review_id'],tic=x['tic'],tier=x['physical_tier'],
        search=x['search'].split(' ')[0],adopted_period_d=P,
        numeric_review_period_d=gnum.group(1) if gnum else '',refit_after_visual=refit,visual_reading=VISUAL.get(x['review_id'],''),sheet_panel6=SHEET.get(x['review_id'],''),
        offset_box_widths=round(min(ph,1-ph)*P*24/float(x['duration_h']),2) if x['duration_h'] else '',
        secondary_phase=ph,secondary_depth_ppt=x['secondary_depth_ppt'],depth_ppt=x['depth_ppt'],
        e_min=round(em,3),e_envelope=round(ev,3),flags='; '.join(flags)))
out.sort(key=lambda d:(not d['refit_after_visual'],-d['e_min']))
w=csv.DictWriter(open(os.path.join(HERE,'secondary-column-flags.csv'),'w',newline=''),fieldnames=list(out[0]))
w.writeheader(); w.writerows(out)
n_refit=sum('Refit after visual review' in x['period_resolution'] for x in rows)
n_refit_sec=sum('Refit after visual review' in x['period_resolution'] and bool(x['secondary_phase']) for x in rows)
allsec=[(min(float(x['secondary_phase']),1-float(x['secondary_phase']))*float(x['adopted_period_days'])*24/float(x['duration_h']),x['review_id']) for x in rows if x['secondary_phase'] and x['duration_h']]
allsec.sort(); print('secondaries closest to the primary, in box widths:',[(round(a,2),b) for a,b in allsec[:10]])
print('rows',len(rows),'with secondary column',sum(bool(x['secondary_phase']) for x in rows))
print('visual-refit rows',n_refit,'of which secondary column filled',n_refit_sec)
print('flagged',len(out),      '| refit rows against visual',sum(d['refit_after_visual'] and d['visual_reading'] and not d['visual_reading'].startswith('visual agrees') for d in out),
      '| phase mismatch',sum('text phase' in d['flags'] for d in out),
      '| implausible e',sum('needs e' in d['flags'] for d in out),
      '| confirmed',sum(d['tier']=='confirmed' for d in out))
