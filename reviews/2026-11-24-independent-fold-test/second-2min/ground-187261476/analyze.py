import pandas as pd,numpy as np,pathlib,json,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=pathlib.Path(__file__).parent;d=pd.read_csv(p/'asassn.csv');good=d[(d.quality=='G')&(d.mag_err<.2)&np.isfinite(d.mag)].copy();P=1.178992420;t0=2912.2224825;good['btjd_approx']=good.jd-2457000; good['phase']=((good.btjd_approx-t0)/P+.5)%1-.5
print('all',len(d),'good',len(good),'band',good.phot_filter.value_counts().to_dict(),'times',good.jd.min(),good.jd.max());print('faintest',good.nlargest(12,'mag')[['jd','mag','mag_err','phot_filter','camera','quality','phase']].to_string(index=False))
for band,g in good.groupby('phot_filter'):
 inside=abs(g.phase)<(.3*2.63/24/P); outside=abs(g.phase)>(2.63/24/P);print(band,'in',inside.sum(),'out',outside.sum(),'median',g.mag.median(),'inmed',g.mag[inside].median(),'outmed',g.mag[outside].median(),'scatter',1.4826*np.median(abs(g.mag[outside]-g.mag[outside].median())))
 fig,ax=plt.subplots(figsize=(8,4));ax.scatter(g.phase,g.mag,s=8,alpha=.65);ax.invert_yaxis();ax.set(xlabel='phase at TESS 1.17899242 d',ylabel='ASAS-SN magnitude',title=f'{band}: quality G, mag error <0.2');fig.tight_layout();fig.savefig(p/f'fold_{band}.png',dpi=160)
good.to_csv(p/'asassn_good.csv',index=False)
