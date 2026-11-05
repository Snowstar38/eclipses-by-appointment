"""Recover AstroSpectroSB1 orientation from Gaia A,B,F,G with C/H check."""
import csv,json,math
from pathlib import Path
B=Path(__file__).resolve().parent
allrows=list(csv.DictReader((B.parent/'shared-catalogues/gaia_nss.csv').open()))
tim={x['sample_id']:x for x in json.loads((B/'lead-timing.json').read_text())}
out=[]
for sid,tic,source in [('T084','87869692','882872210352301568'),('T086','398402989','6360777231720947328'),('T087','200743349','4749907416157959424')]:
 r=next(x for x in allrows if x['source_id']==source and x['nss_solution_type']=='AstroSpectroSB1')
 A,Bb,F,G,C,H=[float(r[k+'_thiele_innes']) for k in ('a','b','f','g','c','h')]
 plus=math.hypot(A+G,Bb-F);minus=math.hypot(A-G,Bb+F)
 cosi=(plus-minus)/(plus+minus);inc=math.degrees(math.acos(cosi))
 omega=(math.degrees((math.atan2(Bb-F,A+G)-math.atan2(Bb+F,A-G))/2))%180
 omega_ch=math.degrees(math.atan2(C,H))%180
 # C/H removes the 180-degree branch ambiguity if its sign convention matches.
 if abs(((omega-omega_ch+90)%180)-90)>2:raise ValueError((sid,omega,omega_ch))
 P=float(r['period']);ecc=float(r['eccentricity']);tp=389+float(r['t_periastron']);epoch=tim[sid].get('epoch_btjd',float(next(x for x in csv.DictReader((Path(__file__).resolve().parent/'queue.csv').open()) if x['sample_id']==sid)['best_window_btjd']))
 con=[]
 for kind,nu in [('A',math.pi/2-math.radians(omega)),('B',3*math.pi/2-math.radians(omega))]:
  E=2*math.atan2(math.sqrt(1-ecc)*math.sin(nu/2),math.sqrt(1+ecc)*math.cos(nu/2));base=tp+((E-ecc*math.sin(E))%(2*math.pi))/(2*math.pi)*P;cyc=round((epoch-base)/P);pred=base+cyc*P
  con.append(dict(kind=kind,gaia_cycle=cyc,pred_btjd=pred,observed_minus_pred_days=epoch-pred))
 rec=dict(sample_id=sid,tic=tic,gaia_source_id=source,inclination_deg=inc,omega_from_abfg_deg=omega,omega_from_ch_deg=omega_ch,semimajor_abfg=(plus+minus)/2,gaia_period_days=P,eccentricity=ecc,periastron_btjd=tp,evaluation_epoch_btjd=epoch,conjunctions=con,closest=min(con,key=lambda z:abs(z['observed_minus_pred_days'])),caution='Thiele-Innes inversion uses standard astrometric convention; C/H ratio checks omega branch. Point geometry only; full covariance of nonlinear inversion not propagated.')
 out.append(rec);print(sid,'i',round(inc,2),'omega',round(omega,2),'CH',round(omega_ch,2),'closest',rec['closest'])
(Path(__file__).resolve().parent/'lead-thiele.json').write_text(json.dumps(out,indent=2)+'\n')
