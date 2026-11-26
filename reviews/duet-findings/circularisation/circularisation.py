"""|e cos w| from measured secondary-eclipse phases against period, for the
November 23 host table, with run 6a's flagged rows removed.  Writes ecosw-vs-period.csv and
ecosw-vs-period.svg.  Run from the repo root, after secondary_columns.py:
    python3 reviews/duet-findings/circularisation/circularisation.py"""
import csv,sys,math
import os
HERE=os.path.dirname(os.path.abspath(__file__))
repo=sys.argv[1] if len(sys.argv)>1 else os.path.normpath(os.path.join(HERE,'../../..'))
flagfile=sys.argv[2] if len(sys.argv)>2 else os.path.join(HERE,'..','host-table','secondary-column-flags.csv')
rows=list(csv.DictReader(open(repo+'/reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv')))
# Drop only rows flagged on non-physical grounds (the sheet, the visual note or a mirrored
# phase).  Rows flagged solely because their phase needs a high e are KEPT, otherwise the
# circularisation test would be circular.
flagged=set(x['review_id'] for x in csv.DictReader(open(flagfile))
            if x['visual_reading'] or x['sheet_panel6'] or 'text phase' in x['flags'])
pts=[]
for x in rows:
    if not x['secondary_phase']: continue
    P=float(x['adopted_period_days']); ph=float(x['secondary_phase'])
    ec=math.pi/2*abs(ph-0.5)                       # first order; exact for e sin w = 0 to O(e^3)
    pts.append(dict(review_id=x['review_id'],tier=x['physical_tier'],P_d=P,secondary_phase=ph,
        abs_ecosw=round(ec,4),secondary_depth_ppt=x['secondary_depth_ppt'],depth_ppt=x['depth_ppt'],
        dropped_6a=x['review_id'] in flagged,visual_reason=x['visual_reason'][:120]))
w=csv.DictWriter(open(os.path.join(HERE,'ecosw-vs-period.csv'),'w',newline=''),fieldnames=list(pts[0])); w.writeheader(); w.writerows(pts)
clean=[p for p in pts if not p['dropped_6a']]
print('secondaries',len(pts),'after removing 6a flags',len(clean))
bins=[0,1,2,3,5,8,12,20,40,200]
print('P bin (d)     n   frac>0.01 frac>0.05  max|ecosw|   [all rows incl. flagged: n, frac>0.05]')
for a,b in zip(bins,bins[1:]):
    s=[p['abs_ecosw'] for p in clean if a<=p['P_d']<b]; t=[p['abs_ecosw'] for p in pts if a<=p['P_d']<b]
    if not s: continue
    print('%5g-%-5g %5d   %5.2f    %5.2f     %6.3f      [%d, %.2f]'%(a,b,len(s),sum(e>0.01 for e in s)/len(s),
          sum(e>0.05 for e in s)/len(s),max(s),len(t),sum(e>0.05 for e in t)/len(t)))
# SVG: log P (0.3-100 d) vs |e cos w| (0-0.7)
W,H,L,B,T,R=640,400,60,50,20,20
X=lambda P:L+(math.log10(P)-math.log10(0.3))/(math.log10(100)-math.log10(0.3))*(W-L-R)
Y=lambda e:H-B-e/0.7*(H-B-T)
s=['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" font-family="sans-serif" font-size="12">'%(W,H),
   '<rect width="100%" height="100%" fill="white"/>',
   '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="black"/>'%(L,H-B,W-R,H-B),
   '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="black"/>'%(L,T,L,H-B)]
for P in [0.3,1,3,10,30,100]:
    s.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="black"/><text x="%.1f" y="%d" text-anchor="middle">%g</text>'%(X(P),H-B,X(P),H-B+5,X(P),H-B+20,P))
for e in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7]:
    s.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="black"/><text x="%d" y="%.1f" text-anchor="end">%.1f</text>'%(L-5,Y(e),L,Y(e),L-8,Y(e)+4,e))
s.append('<text x="%d" y="%d" text-anchor="middle">period (d)</text>'%((L+W-R)/2,H-12))
s.append('<text x="15" y="%d" transform="rotate(-90 15 %d)" text-anchor="middle">|e cos ω| from secondary phase</text>'%((T+H-B)/2,(T+H-B)/2))
for p in pts:
    if p['dropped_6a']:
        s.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="none" stroke="#c0392b"/>'%(X(p['P_d']),Y(min(p['abs_ecosw'],0.7))))
    else:
        s.append('<circle cx="%.1f" cy="%.1f" r="2.5" fill="#2c6fbb" fill-opacity="0.7"/>'%(X(p['P_d']),Y(min(p['abs_ecosw'],0.7))))
s.append('<text x="%d" y="%d">filled: secondaries kept; open red: dropped (sheet / visual note / mirrored phase, run 6a)</text>'%(L+10,T+12))
s.append('</svg>')
open(os.path.join(HERE,'ecosw-vs-period.svg'),'w').write('\n'.join(s))
print('short-period (<5 d) eccentric, kept, |ecosw|>0.1:')
for p in sorted(clean,key=lambda p:p['P_d']):
    if p['P_d']<5 and p['abs_ecosw']>0.1: print(' ',p['review_id'],p['tier'],p['P_d'],p['secondary_phase'],p['abs_ecosw'],p['secondary_depth_ppt'],'|',p['visual_reason'][:70])
