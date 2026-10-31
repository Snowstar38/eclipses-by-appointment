import numpy as np, importlib.util
p=r'[local path omitted] 5.1/made/appointments/ground/kelt/'
s=importlib.util.spec_from_file_location('kf',p+'keltfold.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
t,f=m.load(p+'tic277542587_kelt.txt'); T=2457000+3488.8242; P=np.arange(24.325,24.338,0.00005)
d,z,n=m.scan(t,f,P,T,12.4/24,True); j=np.nanargmax(z); q=((t-T+P[j]/2)%P[j])-P[j]/2; inside=np.abs(q)<12.4/24/4
print('best',P[j], 'SNR',z[j], 'depth',d[j], 'n',n[j], 'nights',len(np.unique(np.floor(t[inside]))))
for lo,hi in [(2455000,2456658),(2456658,2458100)]:
 k=(t>=lo)&(t<hi); a,b,c=m.scan(t[k],f[k],np.array([P[j]]),T,12.4/24,True); print(lo,hi,'SNR',b[0],'depth',a[0],'n',c[0])
print('within one max:',P[z>=z[j]-1].min(),P[z>=z[j]-1].max())
