import csv,os
r=os.path.dirname(__file__); p=r+'/RESULTS.csv'; a=list(csv.DictReader(open(p))); e=list(csv.DictReader(open(r+'/events.csv')))
for x in a: x['robust_sampled_windows']=sum(y['robust_sampling']=='True' for y in e if y['tic']==x['tic'])
with open(p,'w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=a[0]);w.writeheader();w.writerows(a)
