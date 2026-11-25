"""Run 8b: at which Gaia conjunction do the catalogue's primary-epoch eclipses fall?
House convention (every geometry script in the repo): kind 0 / 'A' is nu = 90 deg - omega, where the
Gaia-orbit (visible) star is farthest from us, i.e. it is the star eclipsed; kind 1 / 'B' is nu = 270 deg - omega.
Separation at conjunction: r_0 ∝ 1/(1 + e sin w), r_1 ∝ 1/(1 - e sin w).
Physics: (i) the deeper eclipse is usually the visible (higher surface brightness) star's -> kind 0;
(ii) in eccentric orbits the conjunction nearer periastron is likelier to eclipse at all.
Reads every gaia-geometry.json in the repository. Usage: python3 conjunction_kind.py <repo> [out.csv]"""
import json,glob,os,sys,csv,math,collections
root=sys.argv[1] if len(sys.argv)>1 else '.'
reg={}
for r in csv.DictReader(open(os.path.join(root,'scientific-review-register.csv'))): reg.setdefault(r['tic'],r)
acc={r['tic']:r for r in csv.DictReader(open(os.path.join(root,'accepted-systems.csv')))}
K={0:0,1:1,'A':0,'B':1,'0':0,'1':1}
def norm(tic,m,f):
    e=m.get('eccentricity',m.get('e')); w=m.get('omega_deg')
    if e is None or w is None: return None
    conj=m.get('conjunction',m.get('conjunctions'))
    if isinstance(conj,dict): conj=[dict(v,kind=k) for k,v in conj.items()]
    if not conj: return None
    c={}
    for x in conj:
        k=K.get(x.get('kind'))
        if k is None: return None
        off=x.get('offset_days',x.get('offset_d'))
        err=x.get('gaia_covariance_linear_error_days',x.get('gaia_linear_covariance_error_days',x.get('diagonal_linear_error_d')))
        c[k]=(off,err)
    if len(c)<2: return None
    if 'closest' in m: k=K[m['closest']['kind']]
    elif 'closest_kind' in m: k=K[m['closest_kind']]
    else: k=min(c,key=lambda q:abs(c[q][0]))
    P=m.get('period_days',m.get('gaia_P',m.get('gaia_period_days')))
    wr=math.radians(w); esw=e*math.sin(wr)
    zc=abs(c[k][0])/max(c[k][1] or 1e-9,1e-9); zo=abs(c[1-k][0])/max(c[1-k][1] or 1e-9,1e-9)
    near=0 if esw>0 else 1
    return dict(tic=str(m.get('tic',tic)),review_id=reg.get(str(tic),{}).get('review_id',''),tier=acc.get(str(tic),{}).get('tier','not accepted'),
        method=reg.get(str(tic),{}).get('search_method',''),P=round(P,5),e=round(e,4),omega_deg=round(w,2),esinw=round(esw,4),ecosw=round(e*math.cos(wr),4),
        kind=k,near_periastron_kind=near,
        r_obs_over_r_other=round((1+(esw if k==1 else -esw))/(1+(esw if k==0 else -esw)),4) if True else None,
        offset_closest_d=round(c[k][0],4),err_closest_d=round(c[k][1] or 0,4),z_closest=round(zc,2),
        offset_other_d=round(c[1-k][0],4),err_other_d=round(c[1-k][1] or 0,4),z_other=round(zo,2),source=os.path.relpath(f,root))
R={}
for f in sorted(glob.glob(os.path.join(root,'reviews/**/gaia-geometry.json'),recursive=True)):
    d=json.load(open(f))
    for tic,m in d.items():
        if isinstance(m,dict):
            n=norm(tic,m,f)
            if n: R[n['tic']]=n   # later files win (re-reviews)
R=list(R.values())
print('distinct systems with usable Gaia conjunction geometry:',len(R),' accepted:',sum(r['tier'] in('confirmed','probable') for r in R))
def tab(sel,label):
    k0=sum(r['kind']==0 for r in sel); near=sum(r['near_periastron_kind']==r['kind'] for r in sel)
    print(f"{label:48s} n={len(sel):4d}  kind0={k0:4d} ({k0/max(len(sel),1):.2f})  near-periastron={near:4d} ({near/max(len(sel),1):.2f})")
acc_=[r for r in R if r['tier'] in('confirmed','probable')]
clean=[r for r in acc_ if r['z_other']>3 and r['z_closest']<3]
tab(acc_,'accepted, all')
tab(clean,'accepted, closest <3 sig, other >3 sig')
for lo,hi in((0,0.05),(0.05,0.15),(0.15,0.3),(0.3,1)):
    tab([r for r in clean if lo<=abs(r['esinw'])<hi],f'   |e sin w| in [{lo},{hi})')
# 2x2 : kind vs near
c=collections.Counter((r['kind'],r['kind']==r['near_periastron_kind']) for r in clean if abs(r['esinw'])>=0.05)
print('|esinw|>=0.05 (kind, at near-periastron):',dict(c))
if len(sys.argv)>2:
    w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(R[0]));w.writeheader();w.writerows(sorted(R,key=lambda r:(r['review_id'] or 'Z',r['tic'])))

# ---- surface-brightness test: evolved visible stars give kind-1 primaries ----
import statistics
def radius(r):
    m=json.load(open(os.path.join(root,r['source']))).get(r['tic'],{})
    x=m.get('tic_radius_solar',m.get('r1_tic'))
    return float(x) if x else None
rad={0:[],1:[]}
for r in clean:
    x=radius(r)
    if x: rad[r['kind']].append(x)
for k in (0,1):
    v=rad[k]; print(f"kind {k}: n with TIC radius={len(v)}  median R1={statistics.median(v):.2f}  R1>2.5: {sum(x>2.5 for x in v)}")
try:
    from scipy.stats import mannwhitneyu,fisher_exact
    print('Mann-Whitney (kind1 radii larger):',mannwhitneyu(rad[1],rad[0],alternative='greater').pvalue)
    a=sum(x>2.5 for x in rad[1]);b=len(rad[1])-a;c=sum(x>2.5 for x in rad[0]);d=len(rad[0])-c
    print('Fisher R1>2.5:',[[a,b],[c,d]],fisher_exact([[a,b],[c,d]],alternative='greater').pvalue)
except ImportError: print('(scipy not installed: skipping p-values)')
# ---- check list: dwarf visible star, primary on kind 1: where should the visible star's own eclipse be? ----
print('\nKind-1 primaries with TIC R1 < 2.5 (dwarf visible star): phase of the kind-0 conjunction, where the')
print("visible star's eclipse (normally the deeper one) is predicted. FAR = kind 1 is also the far-from-periastron conjunction.")
chk=[]
for r in sorted(clean,key=lambda r:r['review_id']):
    x=radius(r)
    if r['kind']==1 and x and x<2.5:
        ph=(-r['offset_other_d']/r['P'])%1
        sig=r['err_other_d']/r['P']
        flag='FAR' if r['kind']!=r['near_periastron_kind'] else ''
        chk.append(dict(review_id=r['review_id'],tic=r['tic'],P=r['P'],e=r['e'],esinw=r['esinw'],R1=x,kind0_phase=round(ph,4),kind0_phase_err=round(sig,4),flag=flag))
        print(f"  {r['review_id']:6} P={r['P']:<9} e={r['e']:<6} R1={x:<5} kind-0 conjunction at phase {ph:.3f} +- {sig:.3f} {flag}")

# ---- kind-1 share by minimum mass ratio and visible-star radius ----
print('\nkind-1 share by minimum companion/visible-star mass ratio (house m1 and minimum m2; eclipsing, so sin i ~ 1) and TIC radius:')
cell=collections.Counter(); qs={0:[],1:[]}
for r in clean:
    m=json.load(open(os.path.join(root,r['source']))).get(r['tic'],{})
    m1=m.get('assumed_m1_solar',m.get('m1_assumed')); m2=m.get('minimum_m2_solar',m.get('m2_min')); rad=m.get('tic_radius_solar',m.get('r1_tic'))
    if not(m1 and m2): continue
    qs[r['kind']].append(m2/m1)
    if not rad: continue
    qb='q >= 0.8' if m2/m1>=0.8 else ('q 0.6-0.8' if m2/m1>=0.6 else 'q < 0.6')
    cell[(qb,'R1 >= 2' if rad>=2 else 'R1 < 2',r['kind'])]+=1
for qb in ('q < 0.6','q 0.6-0.8','q >= 0.8'):
    for rb in ('R1 < 2','R1 >= 2'):
        a=cell[(qb,rb,0)];b=cell[(qb,rb,1)]
        print(f"  {qb:10s} {rb:8s} kind0={a:3d} kind1={b:3d}  kind-1 share {b/max(1,a+b):.2f}")
print('  median q: kind0 %.3f (n=%d), kind1 %.3f (n=%d)'%(statistics.median(qs[0]),len(qs[0]),statistics.median(qs[1]),len(qs[1])))
try:
    from scipy.stats import mannwhitneyu
    print('  Mann-Whitney (kind1 q larger):',mannwhitneyu(qs[1],qs[0],alternative='greater').pvalue)
except ImportError: pass
if len(sys.argv)>3:
    w=csv.DictWriter(open(sys.argv[3],'w',newline=''),fieldnames=list(chk[0]));w.writeheader();w.writerows(chk)
