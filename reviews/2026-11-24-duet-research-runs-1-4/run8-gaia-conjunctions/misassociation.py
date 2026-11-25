"""Run 8a(iii): how many probable Gaia-fold systems are not the Gaia binary?
Calibrate the kind-0 share (primary on the Gaia star's conjunction) on confirmed systems in cells of minimum
mass ratio (<0.6, 0.6-0.8, >=0.8) and TIC radius (<2, >=2 Rsun). A mis-associated eclipse (a blend, or a
different binary) lands on either conjunction at random (kind-0 share 0.5). Solve
observed = (1-f)*expected + f*0.5*n for f, with a bootstrap over both samples.
Usage: python3 misassociation.py [repo=.] [conjunction-kind.csv]"""
import csv,json,os,sys,collections,random
root=sys.argv[1] if len(sys.argv)>1 else '.'
ck=sys.argv[2] if len(sys.argv)>2 else 'conjunction-kind.csv'
R=[r for r in csv.DictReader(open(ck)) if float(r['z_other'])>3 and float(r['z_closest'])<3]
rows=[]
for r in R:
    m=json.load(open(os.path.join(root,r['source']))).get(r['tic'],{})
    m1=m.get('assumed_m1_solar',m.get('m1_assumed')); m2=m.get('minimum_m2_solar',m.get('m2_min')); rad=m.get('tic_radius_solar',m.get('r1_tic'))
    if not(m1 and m2 and rad): continue
    q=m2/m1; rows.append((r['tier'],('<0.6' if q<0.6 else '0.6-0.8' if q<0.8 else '>=0.8', rad>=2), r['kind']=='0'))
def estimate(conf,test):
    rate=collections.defaultdict(lambda:[0,0])
    for _,c,k in conf: rate[c][0]+=k; rate[c][1]+=1
    obs=exp=n=0
    for _,c,k in test:
        if rate[c][1]==0: continue
        obs+=k; exp+=rate[c][0]/rate[c][1]; n+=1
    return (exp-obs)/(exp-0.5*n) if exp-0.5*n>0 else float('nan'), obs, exp, n
conf=[x for x in rows if x[0]=='confirmed']
random.seed(8)
for grp in ('probable','not accepted'):
    test=[x for x in rows if x[0]==grp]
    f,obs,exp,n=estimate(conf,test)
    bs=sorted(estimate([random.choice(conf) for _ in conf],[random.choice(test) for _ in test])[0] for _ in range(2000))
    lo,hi=bs[int(0.16*len(bs))],bs[int(0.84*len(bs))]; lo95,hi95=bs[int(0.025*len(bs))],bs[int(0.975*len(bs))]
    print(f'{grp}: n={n}, kind-0 observed {obs}, expected {exp:.1f} if all were the Gaia binary; mis-associated fraction f = {f:.2f} (68%: {lo:.2f} to {hi:.2f}; 95%: {lo95:.2f} to {hi95:.2f})')
