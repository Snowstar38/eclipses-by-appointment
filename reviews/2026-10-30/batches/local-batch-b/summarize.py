import csv,collections,numpy as np,os
r=os.path.dirname(__file__); ev=list(csv.DictReader(open(r+'/events.csv'))); sec=list(csv.DictReader(open(r+'/sectors.csv'))); out=[]
for tic in sorted({x['tic'] for x in ev}):
 a=[x for x in ev if x['tic']==tic]; z=[x for x in a if x['classification']!='incomplete']; ss=[x for x in sec if x['tic']==tic]; med=lambda key: round(float(np.nanmedian([float(x[key]) for x in z])),2); ds=[float(x['median_depth_ppt']) for x in ss if x['median_depth_ppt']!='nan'];
 out.append(dict(tic=tic,sectors=len(ss),predicted_windows=len(a),covered_windows=len(z),descriptive_dips=sum(x['classification']=='descriptive_dip' for x in a),median_depth_ppt=med('depth_ppt'),median_wide_depth_ppt=med('depth_wide_ppt'),sector_median_range_ppt=f'{min(ds):.2f} to {max(ds):.2f}',flagged_in_window=sum(int(x['flagged_in']) for x in a),bit32_in_window=sum(int(x['bit32_in']) for x in a),robust_sampled_windows=sum(x.get('robust_sampling')=='True' for x in a),completed_gates='selected QLP raw SAP descriptive windows; sampling and baseline sensitivity checks; prior receipts',missing_gates='full archive checks; Gaia covariance timing; second pipeline; fresh pixels and neighbours; physical geometry; secondary limits; fitted events; blind off-ephemeris census',next_step='Fit individual events and Gaia covariance timing; independently check pipeline and pixels/neighbours'))
with open(r+'/RESULTS.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0]); w.writeheader(); w.writerows(out)
print(out)
