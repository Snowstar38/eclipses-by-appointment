from common import *
for tic in GAIA:
    for s in load(tic):
        dt=np.diff(s['t']); gaps=[(round(s['t'][i],2),round(s['t'][i+1],2)) for i in np.where(dt>0.5)[0]]
        print(tic,s['author'],'s%d'%s['sector'],'cam%s ccd%s'%(s['cam'],s['ccd']),'N=%d'%len(s['t']),'range %.2f-%.2f'%(s['t'].min(),s['t'].max()),
              'rms(ppt,30min-ish)=%.2f'%(1e3*np.nanstd(np.diff(s['f']))/np.sqrt(2)),'gaps>0.5d:',gaps, 'flagged frac=%.2f'%np.mean(s['q_all']!=0))
