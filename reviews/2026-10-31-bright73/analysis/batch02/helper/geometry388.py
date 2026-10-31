import csv,json,math,numpy as np
id='3147149694307614080';n=next(r for r in csv.DictReader(open('../shared-catalogues/gaia-nss-full.csv')) if r['source_id']==id);d=json.load(open('gaia-geometry.json'))['388052602']; v=np.array([float(n['period']),float(n['eccentricity']),math.radians(float(n['arg_periastron'])),float(n['t_periastron'])+389]); er=np.array([float(n['period_error']),float(n['eccentricity_error']),math.radians(float(n['arg_periastron_error'])),float(n['t_periastron_error'])]);c=np.eye(6);vals=[float(x) for x in n['corr_vec'].strip('{}[]()').split(',')];z=0
for i in range(1,6):
 for j in range(i):c[i,j]=c[j,i]=vals[z];z+=1
c=c[np.ix_([0,3,4,5],[0,3,4,5])]
def f(v,k):
 p,e,w,tp=v;nu=math.pi/2-w; E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));return tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*p+k*p
k=round((d['near_reference']['projected_photometric_epoch_btjd']-f(v,0))/v[0]);g=[]
for i in range(4):
 h=max(er[i]*.0001,1e-8);a=v.copy();b=v.copy();a[i]+=h;b[i]-=h;g.append((f(a,k)-f(b,k))/(2*h)*er[i])
print('cycle',k,'near reference covariance sigma',np.sqrt(np.array(g)@c@np.array(g)), 'offset', d['near_reference']['offset_days'], 'eigen',np.linalg.eigvalsh(c))
