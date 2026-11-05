import json
T={'N004':[2510.8138483392595,2531.2636837694886],'N010':[1607.486149552709,3084.9013907983926,4050.9236667222526,4107.659595017292]};out={}
a=T['N010']; rows=[]
for n in (43,44,45):
 p=(a[-1]-a[0])/n; ks=[round((t-a[0])/p) for t in a];res=[t-(a[0]+k*p) for t,k in zip(a,ks)];rows.append({'cycles':n,'period_days':p,'integers':ks,'residual_days':res})
out['N010']=rows;out['N004']={'deep_event_separation_days':T['N004'][1]-T['N004'][0],'S72_fit_width_depth_ingress_nonidentifiable':True};open('batch01/helper-timing-audit.json','w').write(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))

