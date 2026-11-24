"""Rule-consistency audit of the November 23 additions (R946-R1701).
Reads only files in the repository. Run from the repository root."""
import csv, re, math, json, collections, glob, sys
D='reviews/2026-11-23-pipeline-and-survey-review/'
H=list(csv.DictReader(open(D+'host-stars.csv',encoding='utf-8')))
RS=list(csv.DictReader(open(D+'reviewed-stars.csv',encoding='utf-8')))
ACC=list(csv.DictReader(open('accepted-systems.csv',encoding='utf-8')))
flags=collections.defaultdict(list)   # review_id -> list of (code, detail)
def flag(x,code,detail=''): flags[x['review_id']].append((code,detail))
def f(v):
    try: return float(v)
    except: return None
def sectors(a): return re.findall(r's(\d+):([a-z_]+)',a)
GENERIC='Companions within about 10 arcsec cannot be excluded.'
TWO_RED='Second look from two TESS reductions'
WEAK2='Weak second look'
for x in H:
    t=x['physical_tier']; P=f(x['adopted_period_days']); Palt=f(x['period_alternative_days'])
    dep=f(x['depth_ppt']); dur=f(x['duration_h']); sd=f(x['secondary_depth_ppt']); sp=f(x['secondary_phase'])
    ne=f(x['n_events_prim']); ns=f(x['n_sectors']); ep=f(x['adopted_epoch_btjd'])
    sec=sectors(x['attribution']); on=sum(1 for _,s in sec if s=='on_target')
    lim=x['limitation']; pres=x['period_resolution']; psrc=x['period_source']
    text=' '.join([x['reason'],x['visual_reason'],pres]).lower()
    # ---- confirmed criteria (methods.md) ----
    if t=='confirmed':
        if on<2: flag(x,'C1 attribution: fewer than two on-target sectors',f"{on} on-target; {x['attribution'][:110]}")
        if any(s=='neighbour_preferred' for _,s in sec): flag(x,'C1 attribution: a sector prefers a neighbour',x['attribution'][:110])
        if x['attribution'].startswith('unresolved'): flag(x,'C1 attribution: overall unresolved',x['attribution'][:110])
        if not x['ground_survey_detection'].strip():
            if WEAK2 in lim or 'one TESS reduction' in lim: flag(x,'C4 second look: one TESS reduction only',lim[:110])
            elif TWO_RED not in lim: flag(x,'C4 second look: none recorded',lim[:110])
        if 'cycle count not fixed' in psrc or 'cycle count' in lim.lower(): flag(x,'C2 period: cycle count not fixed by the data',psrc)
        for phrase,code in [('Source attribution limited','C1 limitation says attribution limited'),
                            ('Eclipse shape not cleanly discrete','C0 limitation says shape not cleanly discrete'),
                            ('Eclipses measured in one sector only','C0 limitation says eclipses in one sector only'),
                            ('Gaia DR3 orbital period differs','C2 limitation says Gaia period differs')]:
            if phrase in lim: flag(x,code,lim[:110])
    # ---- probable must carry one named limitation ----
    if t=='probable':
        rest=lim.replace(GENERIC,'').strip()
        if not rest: flag(x,'P1 probable with no named limitation',lim)
        if rest.startswith("Limitation as stated in the host table's reason column") and 'limitation' not in x['reason'].lower() and 'visual review' not in rest.lower():
            flag(x,'P1 limitation points to reason column, which names none',x['reason'][:110])
    # ---- exclusions ----
    if P and dur:
        duty=dur/(24*P)
        if duty>0.2: flag(x,'X1 eclipse lasts over 20% of the orbit (contact-like?)',f'duty={duty:.2f}, P={P}, dur={dur} h')
    for w in ['contact','ellipsoidal','w uma','sinusoid','eclipse-like but','not discrete','pulsat','rotation','spot']:
        if w in text: flag(x,'X2 text mentions '+w,re.sub(r'\s+',' ',text)[max(0,text.find(w)-70):text.find(w)+70])
    # P<0.5 d with two equal minima per orbit (adopted period is twice a photometric period with equal dips)
    equal='equal alternate dips' in pres and 'unequal' not in pres
    if t in('confirmed','probable') and P and P<0.5:
        half=[float(n) for n in re.findall(r'P=([\d.]+)',pres)]
        if equal and any(abs(P/(2*h)-1)<0.005 for h in half):
            flag(x,'X3 twin equal minima on an orbit under 0.5 d (rule: never above candidate)',f'P={P}')
        elif re.search(r'two (near-)?equal',x['visual_reason'].lower()):
            flag(x,'X3b visual note describes two equal minima under 0.5 d',x['visual_reason'][:110])
    # ---- data sanity ----
    if P is None or P<=0: flag(x,'D1 period missing or non-positive',x['adopted_period_days'])
    if dep is None or dep<=0 or dep>=1000: flag(x,'D2 depth outside 0-1000 ppt',x['depth_ppt'])
    if sd and dep and sd>dep*1.02: flag(x,'D3 secondary deeper than primary',f'prim {dep}, sec {sd}')
    if sp is not None and not (0<sp<1): flag(x,'D4 secondary phase outside 0-1',x['secondary_phase'])
    if ep is None or not (1300<ep<4500): flag(x,'D5 epoch outside TESS range',x['adopted_epoch_btjd'])
    if ne is not None and ne<2: flag(x,'D6 fewer than two primary eclipses (not repeating)',x['n_events_prim'])
    if ne is not None and ns and P:
        pass
    if dur is not None and dur<=0: flag(x,'D7 non-positive duration',x['duration_h'])
    if x['visual_review']=='first read agrees' and x['numeric_tier']!=t: flag(x,'V1 tier differs from numeric with no adjudication',f"{x['numeric_tier']}->{t}")
    if x['numeric_tier'] in('refuted','candidate') and t=='confirmed': flag(x,'V2 confirmed although numeric review said '+x['numeric_tier'],x['visual_reason'][:110])
    if not re.fullmatch(r'\d+',x['tic']): flag(x,'D9 TIC not an integer',x['tic'])
    if x['gaia_dr3'] and not re.fullmatch(r'\d{6,19}',x['gaia_dr3']): flag(x,'D9 Gaia id malformed',x['gaia_dr3'])
    if 'gaia dr3 nss' in text and 'ground' in x['search'].lower():
        m=re.search(r'nss \w+ orbit p=([\d.]+)',text)
        if m and float(m.group(1))<60: flag(x,'S1 ground-survey row has a Gaia orbit under 60 d (search excluded these)',m.group(0))
# ---- stated totals ----
tot={}
C=[x for x in H if x['physical_tier']=='confirmed']
tot['confirmed']=len(C); tot['probable']=len(H)-len(C)
tot['confirmed_with_ground_detection']=sum(1 for x in C if x['ground_survey_detection'].strip())
tot['confirmed_with_factor_two_alternative']=sum(1 for x in C if x['period_alternative_days'].strip())
tot['visual_first_read_agrees']=sum(1 for x in H if x['visual_review']=='first read agrees')
tot['numeric_not_accepting_then_added']=sum(1 for x in H if x['numeric_tier'] in('refuted','candidate'))
tot['period_refit']=sum(1 for x in H if 'refit' in x['period_source'])
tot['period_doubled_on_visual']=sum(1 for x in H if 'doubled' in x['period_source'])
tot['superwasp_flag_nonblank']=sum(1 for x in H if x['superwasp_schanche2019'].strip())
# ---- reviewed-stars consistency ----
added=collections.defaultdict(list)
for s in RS:
    m=re.search(r'added as (R\d+)',s['outcome'])
    if m: added[m.group(1)].append(s)
hid={x['review_id']:x for x in H}
rs_issues=[]
for rid,x in hid.items():
    if rid not in added: rs_issues.append((rid,'host row not marked added in reviewed-stars'))
    else:
        for s in added[rid]:
            if s['tic']!=x['tic']: rs_issues.append((rid,f"reviewed-stars TIC {s['tic']} != host TIC {x['tic']}"))
for rid in added:
    if rid not in hid: rs_issues.append((rid,'reviewed-stars says added but no host row'))
outc=collections.Counter(re.sub(r'R\d+','R…',re.sub(r'TIC \d+','TIC …',s['outcome']))[:80] for s in RS)
neigh=[s for s in RS if 'neighbour' in s['outcome'].lower() or 'neighbor' in s['outcome'].lower()]
# ---- spatial duplicates/blends over the whole accepted catalogue ----
per={}
def addp(tic,p):
    p=f(p)
    if tic and p and p>0: per.setdefault(str(tic).strip(),p)
for x in H: addp(x['tic'],x['adopted_period_days'])
for x in csv.DictReader(open('reviews/2026-11-22-eclipse-review/host-stars.csv',encoding='utf-8')): addp(x['tic'],x['adopted_period_days'])
for fn in ['period-free-review.csv','faint-band-review.csv','remaining-screened-review.csv','bright-followup-review.csv','magnitude-review.csv','bright73-review.csv','gap-review.csv','appointments-review.csv','reviews/2026-11-05-next100/reconciled-results.csv']:
    for x in csv.DictReader(open(fn,encoding='utf-8')): addp(x.get('tic'),x.get('period_days'))
for x in csv.DictReader(open('CHECKCARD.csv',encoding='utf-8')): addp(x['TIC'],x['P_days'])
for x in csv.DictReader(open('returned-review.csv',encoding='utf-8')):
    m=re.search(r'[\d.]+',x['period_days_reported'] or ''); addp(x['tic'],m.group(0) if m else None)
for fn in ['batch-candidates.csv']:
    for x in csv.DictReader(open(fn,encoding='utf-8')): addp(x['tic'],x['period_d'])
pos=[(x['review_id'],x['tic'],float(x['ra_deg']),float(x['dec_deg']),x['tier'],x['release_cohort']) for x in ACC]
def sep(a,b):
    r1,d1,r2,d2=map(math.radians,(a[2],a[3],b[2],b[3]))
    c=math.sin(d1)*math.sin(d2)+math.cos(d1)*math.cos(d2)*math.cos(r1-r2)
    return math.degrees(math.acos(max(-1,min(1,c))))*3600
pos.sort(key=lambda p:p[3])
pairs=[]
for i,a in enumerate(pos):
    j=i+1
    while j<len(pos) and pos[j][3]-a[3]<300/3600:
        b=pos[j]; s=sep(a,b)
        if s<300:
            pa,pb=per.get(a[1]),per.get(b[1]); rel=None
            if pa and pb:
                rel=min(abs(pa/pb*k-1) for k in (1,2,0.5,3,1/3))
            pairs.append((round(s,1),a,b,pa,pb,rel))
        j+=1
cov=sum(1 for p in pos if p[1] in per)
out={'flags':{k:v for k,v in sorted(flags.items(),key=lambda kv:int(kv[0][1:]))},'totals':tot,'reviewed_stars_issues':rs_issues,
     'reviewed_outcome_kinds':outc.most_common(40),'neighbour_outcomes':len(neigh),'period_coverage':f'{cov}/{len(pos)}',
     'pairs':[{'sep':s,'a':a[:2]+a[4:],'b':b[:2]+b[4:],'Pa':pa,'Pb':pb,'period_match':rel} for s,a,b,pa,pb,rel in sorted(pairs)]}
json.dump(out,open(sys.argv[1],'w'),indent=1)
cnt=collections.Counter(c for v in flags.values() for c,_ in v)
for c,n in sorted(cnt.items()): print(n,c)
print(json.dumps(tot,indent=1)); print('rs issues',len(rs_issues),rs_issues[:5]); print('period coverage',out['period_coverage'])
print('pairs <300":',len(pairs),' <21":',sum(1 for p in pairs if p[0]<21),' period-matched (<0.2%):',sum(1 for p in pairs if p[5] is not None and p[5]<0.002))

# ---- second pass: checks added after reading the first-pass flags ----
print('\nSecond pass')
def sec_offsets(x):
    sec=re.findall(r'(s\d+):([a-z_]+)',x['attribution'])
    m=re.search(r'free-fit offsets \[([^\]]*)\]',x['attribution'])
    offs=[float(t) for t in m.group(1).split(',')] if m and m.group(1).strip() else []
    return list(zip(sec,offs)) if len(offs)==len(sec) else None
for x in H:
    so=sec_offsets(x)
    if so is None: continue
    on_px=sum(1 for (s,l),o in so if l=='on_target' and o<=21)
    far=[(s,o) for (s,l),o in so if l=='on_target' and o>21]
    if x['physical_tier']=='confirmed' and on_px<2: print(x['review_id'],'confirmed with',on_px,'on-target sectors within one pixel',far)
    elif far: print(x['review_id'],x['physical_tier'],'on_target label with free-fit offset over one pixel',far)
for x in H:
    m=re.search(r'secondary at phase ([\d.]+)',x['period_resolution'])
    if m and x['secondary_phase'] and abs(float(m.group(1))-float(x['secondary_phase']))>0.02:
        print(x['review_id'],'secondary_phase',x['secondary_phase'],'vs period_resolution',m.group(1))
for x in H:
    p=x['period_resolution']
    if ('degenerate' in p or 'ambiguous' in p) and not any(k in p for k in ('settled','agrees with','literature:','SB2 (two luminous stars)')) and not x['period_alternative_days'].strip():
        print(x['review_id'],x['physical_tier'],'factor-of-two choice open but no alternative period listed')
for x in H:
    if 'refit' in x['period_source']:
        P=float(x['adopted_period_days']); nums=[float(n) for n in re.findall(r'P=([\d.]+)',x['period_resolution'])]
        if nums and not any(abs(P/n*k-1)<0.005 for n in nums for k in (1,2,0.5)): print(x['review_id'],'refit period',P,'but period_resolution describes',nums[:2])
