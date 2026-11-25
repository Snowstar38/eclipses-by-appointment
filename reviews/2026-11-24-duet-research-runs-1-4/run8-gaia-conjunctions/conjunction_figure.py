"""Run 8a figure: which conjunction holds the primary eclipse. Writes conjunction-kind.svg.
Left: share of primaries on the companion's conjunction (kind 1) by minimum mass ratio, split by TIC radius.
Right: share of primaries at the conjunction nearer periastron, by |e sin w| (0.5 = no preference).
Usage: python3 conjunction_figure.py [repo=.] [conjunction-kind.csv] [out.svg]"""
import csv,json,os,sys,collections
root=sys.argv[1] if len(sys.argv)>1 else '.'
ck=sys.argv[2] if len(sys.argv)>2 else 'conjunction-kind.csv'
out=sys.argv[3] if len(sys.argv)>3 else 'conjunction-kind.svg'
R=[r for r in csv.DictReader(open(ck)) if r['tier'] in('confirmed','probable') and float(r['z_other'])>3 and float(r['z_closest'])<3]
cell=collections.defaultdict(lambda:[0,0]); ecc=collections.defaultdict(lambda:[0,0])
QB=['< 0.6','0.6–0.8','≥ 0.8']; EB=['< 0.05','0.05–0.15','0.15–0.3','≥ 0.3']
for r in R:
    m=json.load(open(os.path.join(root,r['source']))).get(r['tic'],{})
    m1=m.get('assumed_m1_solar',m.get('m1_assumed')); m2=m.get('minimum_m2_solar',m.get('m2_min')); rad=m.get('tic_radius_solar',m.get('r1_tic'))
    if m1 and m2 and rad:
        q=m2/m1; qb=QB[0] if q<0.6 else QB[1] if q<0.8 else QB[2]
        c=cell[(qb,rad>=2)]; c[0]+=r['kind']=='1'; c[1]+=1
    a=abs(float(r['esinw'])); eb=EB[0] if a<0.05 else EB[1] if a<0.15 else EB[2] if a<0.3 else EB[3]
    c=ecc[eb]; c[0]+=r['kind']==r['near_periastron_kind']; c[1]+=1
W,H=820,390; PL=(70,60,330,250); PR=(470,60,330,250)  # x,y,w,h of plot areas
BLUE,ORANGE='#257de0','#f47230'; TXT,TXT2,GRID='#191919','#666666','#e5e5e5'
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif" font-size="12">',
   f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
def axes(P,title,ylab):
    x,y,w,h=P
    s.append(f'<text x="{x}" y="{y-28}" fill="{TXT}" font-size="13" font-weight="bold">{title}</text>')
    for t in (0,0.25,0.5,0.75,1.0):
        yy=y+h-t*h
        s.append(f'<line x1="{x}" x2="{x+w}" y1="{yy:.1f}" y2="{yy:.1f}" stroke="{GRID}" stroke-width="1"/>')
        s.append(f'<text x="{x-8}" y="{yy+4:.1f}" fill="{TXT2}" text-anchor="end">{int(t*100)}%</text>')
    s.append(f'<text transform="translate({x-48},{y+h/2}) rotate(-90)" fill="{TXT2}" text-anchor="middle">{ylab}</text>')
def bar(x0,bw,frac,col,y,h,label):
    bh=max(frac*h,1); top=y+h-bh; r=min(4,bw/2,bh)
    s.append(f'<path d="M{x0},{y+h} V{top+r} Q{x0},{top} {x0+r},{top} H{x0+bw-r} Q{x0+bw},{top} {x0+bw},{top+r} V{y+h} Z" fill="{col}"/>')
    s.append(f'<text x="{x0+bw/2}" y="{top-5}" fill="{TXT}" text-anchor="middle" font-size="11">{label}</text>')
# left panel
x,y,w,h=PL; axes(PL,'Primary on the companion’s conjunction','share of primaries')
gw=w/3; bw=34
for i,qb in enumerate(QB):
    cx=x+gw*i+gw/2
    for j,(big,col) in enumerate(((False,BLUE),(True,ORANGE))):
        k,n=cell[(qb,big)]; bar(cx-bw-1+j*(bw+2),bw,k/n if n else 0,col,y,h,f'{k}/{n}')
    s.append(f'<text x="{cx}" y="{y+h+18}" fill="{TXT2}" text-anchor="middle">{qb.replace('<','&lt;')}</text>')
s.append(f'<text x="{x+w/2}" y="{y+h+38}" fill="{TXT2}" text-anchor="middle">minimum mass ratio m₂/m₁</text>')
lx=x+10; ly=y-12
for col,lab in ((BLUE,'TIC radius &lt; 2 solar'),(ORANGE,'TIC radius ≥ 2 solar')):
    s.append(f'<rect x="{lx}" y="{ly-9}" width="10" height="10" rx="2" fill="{col}"/><text x="{lx+15}" y="{ly}" fill="{TXT}">{lab}</text>'); lx+=150
# right panel
x,y,w,h=PR; axes(PR,'Primary at the conjunction nearer periastron','share of primaries')
yy=y+h-0.5*h
s.append(f'<line x1="{x}" x2="{x+w}" y1="{yy}" y2="{yy}" stroke="{TXT2}" stroke-width="1" stroke-dasharray="4 3"/>')
s.append(f'<line x1="{x+10}" x2="{x+34}" y1="{y-16}" y2="{y-16}" stroke="{TXT2}" stroke-width="1" stroke-dasharray="4 3"/><text x="{x+40}" y="{y-12}" fill="{TXT}">no preference (50%)</text>')
gw=w/4; bw=40
for i,eb in enumerate(EB):
    cx=x+gw*i+gw/2; k,n=ecc[eb]; bar(cx-bw/2,bw,k/n,BLUE,y,h,f'{k}/{n}')
    s.append(f'<text x="{cx}" y="{y+h+18}" fill="{TXT2}" text-anchor="middle">{eb.replace('<','&lt;')}</text>')
s.append(f'<text x="{x+w/2}" y="{y+h+38}" fill="{TXT2}" text-anchor="middle">|e sin ω| from Gaia</text>')
s.append(f'<text x="{W/2}" y="{H-8}" fill="{TXT2}" text-anchor="middle" font-size="11">{len(R)} accepted Gaia-fold systems with unambiguous conjunction timing (left: the {sum(v[1] for v in cell.values())} with TIC radius and mass); labels are counts.</text>')
s.append('</svg>')
open(out,'w').write('\n'.join(s)); print('wrote',out)
