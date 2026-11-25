"""Run 8a: for accepted systems whose Gaia DR3 orbit period is not a harmonic of the eclipse period,
test whether the eclipsing pair could be the inner binary of the Gaia orbit (hierarchical triple),
using the Mardling & Aarseth (2001) criterion. Masses: inner 1+1 Msun, third body 1 Msun (q_out=0.5)
and 0.5 Msun; i_mut = 0. Input: run8 gaia-vs-eclipse.csv (made by gaia_vs_eclipse.py)."""
import csv,sys,math
import os
rows=[r for r in csv.DictReader(open(sys.argv[1])) if not r['class'].startswith('harmonic')]
def ma_ratio(q,e): return 2.8*(1+q)**0.4*(1+e)**0.4*(1-e)**-1.2
print('review tier  Pg     Pecl   ratio  e_out  ratioP_needed(q=0.5,0.25)  verdict')
out=[]
for r in rows:
    Pg=float(r['gaia_period_days']); Pe=float(r['eclipse_period_days'].split('|')[0])
    e=float(r['gaia_ecc']) if r['gaia_ecc'] else 0.3
    need=[]
    for q,m3 in((0.5,1.0),(0.25,0.5)):
        Y=ma_ratio(q,e)  # critical a_out_peri/a_in? MA criterion is on R_p = a_out(1-e_out)/a_in > Y
        # a_out/a_in = (Pg/Pe)^(2/3) * ((2+m3)/2)^(1/3); need a_out/a_in*(1-e)? MA: a_out/a_in > Y*(1-e)^-1? No: MA criterion is a_out/a_in > 2.8(1+q)^(2/5)(1+e)^(2/5)(1-e)^(-6/5)
        Pratio=(Y**1.5)/math.sqrt((2+m3)/2)
        need.append(Pratio)
    ratio=Pg/Pe
    for Pe2,lab in((Pe,'P'),(2*Pe,'2P')):
        pass
    v='inner pair of Gaia orbit allowed' if ratio>need[0] else ('allowed only for a light third body' if ratio>need[1] else 'excluded: EB cannot sit inside the Gaia orbit')
    if ratio<1: v='Gaia period shorter than eclipse period'
    # also test 2P (equal-dips alternative)
    v2='allowed' if Pg/(2*Pe)>need[0] else 'excluded'
    print(f"{r['review_id']:6} {r['tier'][:4]} {Pg:7.2f} {Pe:7.3f} {ratio:6.2f} {e:5.2f}  {need[0]:5.2f} {need[1]:5.2f}   {v}; at 2P {v2}  [{r['nss_type']}]")
    out.append(dict(review_id=r['review_id'],tic=r['tic'],gaia_period_days=Pg,eclipse_period_days=Pe,ratio=round(ratio,3),gaia_ecc=round(e,3),nss_type=r['nss_type'],min_ratio_m3_1=round(need[0],2),min_ratio_m3_05=round(need[1],2),verdict=v,verdict_if_true_period_2P=v2))
if len(sys.argv)>2:
    w=csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(out[0]));w.writeheader();w.writerows(out)
