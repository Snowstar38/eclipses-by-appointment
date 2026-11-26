"""Join every accepted system to its Gaia DR3 orbital period (any repository table that carries
gaia_period_days or a Gaia NSS copy, via TIC or Gaia source_id) and its eclipse period, and classify the ratio.
Usage: python3 gaia_vs_eclipse.py [repo=.] [out.csv]"""
import csv,glob,os,sys,collections,re
root=sys.argv[1] if len(sys.argv)>1 else '.'; os.chdir(root)
csv.field_size_limit(10**8)
gp_t=collections.defaultdict(set); gp_s=collections.defaultdict(set); t2s=collections.defaultdict(set); ep=collections.defaultdict(set)
ecc_s={}
for f in glob.glob('**/*.csv',recursive=True):
    if 'release-sha256' in f: continue
    try:
        fh=open(f,newline='',encoding='utf-8',errors='replace'); r=csv.DictReader(fh); h=r.fieldnames or []
    except: continue
    tk=next((k for k in h if k.lower() in('tic','tic_id','ticid')),None)
    sk=next((k for k in h if k.lower() in('gaia_dr3','source_id','gaia_source_id','dr3_source_id')),None)
    gk=[k for k in h if k in('gaia_period_days','gaia_period','period_gaia','gaia_period_d')]
    nssp = 'period' in h and sk and ('eccentricity' in h or 'nss_solution_type' in h)
    ek=[k for k in h if k in('period_days','period_days_reported','P_days','eclipse_period_days','adopted_period_days')]
    try:
     for row in r:
        t=(row.get(tk) or '').strip().split('.')[0] if tk else ''
        s=(row.get(sk) or '').strip().split('.')[0] if sk else ''
        if t.isdigit() and s.isdigit(): t2s[t].add(s)
        for k in gk:
            try:
                v=float(row[k])
                if t.isdigit(): gp_t[t].add(round(v,4))
                if s.isdigit(): gp_s[s].add(round(v,4))
            except: pass
        if nssp and s.isdigit():
            try:
                gp_s[s].add(round(float(row['period']),4))
                if row.get('eccentricity'): ecc_s[(s,round(float(row['period']),4))]=(row.get('eccentricity'),row.get('eccentricity_error'),row.get('nss_solution_type'))
            except: pass
        if t.isdigit():
            for k in ek:
                try:
                    v=float(row[k])
                    if v>0: ep[t].add((round(v,5),f))
                except: pass
    except Exception as e: print('ERR',f,e)
acc=list(csv.DictReader(open('accepted-systems.csv')))
for a in acc:
    if a['gaia_dr3'].strip(): t2s[a['tic']].add(a['gaia_dr3'].strip())
def gaiaP(t):
    s=set(gp_t.get(t,()))
    for sid in t2s.get(t,()): s|=gp_s.get(sid,set())
    return sorted(s)
n=sum(bool(gaiaP(a['tic'])) for a in acc)
print('accepted',len(acc),'gaiaP',n,'eclP',sum(a['tic'] in ep for a in acc))
out=csv.writer(open(sys.argv[2] if len(sys.argv)>2 else 'gaia-vs-eclipse.csv','w',newline=''))
out.writerow(['review_id','tic','tier','gaia_source','gaia_period_days','gaia_ecc','gaia_ecc_err','nss_type','eclipse_period_days','ratio_gaia_over_ecl','class'])
cnt=collections.Counter()
for a in acc:
    t=a['tic']; g=gaiaP(t)
    if not g or t not in ep: continue
    es=sorted({p for p,_ in ep[t]}); e=es[len(es)//2]
    # choose gaia period closest to harmonic
    best=None
    for G in g:
        r=G/e; near=min([1,2,0.5,3,1/3,4,0.25],key=lambda k:abs(r/k-1))
        sc=abs(r/near-1)
        if best is None or sc<best[0]: best=(sc,G,r,near)
    sc,G,r,near=best
    if sc<0.03: c='harmonic %g'%near
    elif r>3: c='gaia_longer'
    elif r<1/3: c='gaia_shorter'
    else: c='mismatch'
    cnt[c]+=1
    ec=next((ecc_s[(s,G)] for s in t2s.get(t,()) if (s,G) in ecc_s),('','',''))
    out.writerow([a['review_id'],t,a['tier'],'|'.join(sorted(t2s.get(t,()))),G,ec[0],ec[1],ec[2],'|'.join(map(str,es)),round(r,4),c])
print(cnt)
