"""Run 8a(ii): do eclipse durations follow Gaia's eccentric geometry at the observed conjunction?
Uses the house's central_duration_hours_approx (TIC radius, minimum-mass main-sequence companion,
separation at the conjunction, factor sqrt(1-e^2)/(1 ± e sin w)) and the observed median duration.
A central eclipse is the longest possible, so observed/predicted should be <= 1 (mean pi/4 for random impact).
Usage: python3 durations.py [repo=.] [conjunction-kind.csv from conjunction_kind.py]"""
import csv,statistics,json,math,sys,os
root=sys.argv[1] if len(sys.argv)>1 else '.'
ck=sys.argv[2] if len(sys.argv)>2 else 'conjunction-kind.csv'
R=[r for r in csv.DictReader(open(ck)) if r['tier'] in('confirmed','probable')]
rows=[]
for r in R:
    m=json.load(open(os.path.join(root,r['source']))).get(r['tic'],{})
    o=m.get('observed_duration_hours',m.get('observed_duration_hours_median')); p=m.get('central_duration_hours_approx')
    if not(o and p): continue
    esw=float(r['esinw']); e=float(r['e']); s=1 if r['kind']=='0' else -1
    rows.append(dict(review_id=r['review_id'],tier=r['tier'],e=e,esinw=esw,kind=r['kind'],obs_h=round(o,3),pred_h=round(p,3),
        ratio=o/p, ratio_other=o/(p*(1+s*esw)/(1-s*esw)), ratio_circ=o/(p*(1+s*esw)/math.sqrt(1-e*e))))
def st(x):
    l=[math.log(v) for v in x]; return f"n={len(x):3d} median={statistics.median(x):.3f} above 1: {sum(v>1 for v in x):2d}  sd(ln)={statistics.pstdev(l):.3f}"
print('all accepted with durations:',st([r['ratio'] for r in rows]))
for lab,f in (('|e sin w| < 0.05',lambda r:abs(r['esinw'])<0.05),('|e sin w| >= 0.15',lambda r:abs(r['esinw'])>=0.15)):
    print(f'{lab}: observed conjunction   ',st([r['ratio'] for r in rows if f(r)]))
hi=[r for r in rows if abs(r['esinw'])>=0.15]
print('|e sin w| >= 0.15: other conjunction      ',st([r['ratio_other'] for r in hi]))
print('|e sin w| >= 0.15: eccentricity ignored   ',st([r['ratio_circ'] for r in hi]))
print('longest relative to central:',', '.join(f"{r['review_id']} {r['ratio']:.2f}" for r in sorted(rows,key=lambda r:-r['ratio'])[:6]))
