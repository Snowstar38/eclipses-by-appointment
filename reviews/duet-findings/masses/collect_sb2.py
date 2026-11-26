"""Collect every Gaia DR3 SB2 orbit in the repository's NSS copies (deduplicated by solution) and join it to
accepted systems whose eclipse period matches Gaia's. Writes reviews/duet-findings/masses/sb2-eclipsing.csv.
Run from the repository root."""
import csv,glob,collections
csv.field_size_limit(10**8)
rows={}
for f in glob.glob('reviews/**/*.csv',recursive=True):
    try: r=csv.DictReader(open(f,newline='',encoding='utf-8',errors='replace')); h=r.fieldnames or []
    except Exception: continue
    if 'semi_amplitude_secondary' not in h or 'source_id' not in h: continue
    for row in r:
        if not (row.get('nss_solution_type') or '').startswith('SB2'): continue
        if not row.get('semi_amplitude_secondary'): continue
        key=(row['source_id'].split('.')[0],row.get('solution_id',''),round(float(row['period']),5))
        rows.setdefault(key,dict(row,_file=f))
print('SB2 solutions found',len(rows),'unique sources',len({k[0] for k in rows}))
g=list(csv.DictReader(open('reviews/duet-findings/gaia-geometry/gaia-vs-eclipse.csv')))
fab={}
for row in csv.DictReader(open('reviews/duet-findings/gaia-errors/fable51-nss-appointments.csv')):
    fab.setdefault(row['review_id'],set()).add(row['source_id'])
out=[]
for a in g:
    sids=set(a['gaia_source'].split('|'))|fab.get(a['review_id'],set())
    if not a['class'].startswith('harmonic'): continue
    ecl=[float(x) for x in a['eclipse_period_days'].split('|')]; e=sorted(ecl)[len(ecl)//2]
    for k,row in rows.items():
        if k[0] in sids:
            P=float(row['period']); ratio=P/e
            out.append(dict(review_id=a['review_id'],tic=a['tic'],tier=a['tier'],source_id=k[0],P=P,P_err=row['period_error'],
              e=row['eccentricity'] or '0',e_err=row.get('eccentricity_error',''),omega=row.get('arg_periastron',''),
              K1=row['semi_amplitude_primary'],K1_err=row['semi_amplitude_primary_error'],K2=row['semi_amplitude_secondary'],
              K2_err=row['semi_amplitude_secondary_error'],q=row.get('mass_ratio',''),type=row['nss_solution_type'],
              eclipse_P=e,ratio=round(ratio,4),src=row['_file']))
w=csv.DictWriter(open('reviews/duet-findings/masses/sb2-eclipsing.csv','w',newline=''),fieldnames=list(out[0]))
w.writeheader(); [w.writerow(o) for o in out]
print('accepted systems with an SB2 at a harmonic of the eclipse period:',len({o['review_id'] for o in out}))
print(collections.Counter(round(o['ratio']) if o['ratio']>=1 else round(o['ratio'],1) for o in out))
