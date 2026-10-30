import json,pathlib,numpy as np,collections
D=pathlib.Path(__file__).parent;p=D/'independent-summary.json';a=json.load(open(p))
for tic,row in a.items():
 if 'events' not in row:continue
 stats={}
 for name in ['qlp']+list(row['events'][0]['independent']):
  vals=[];err=[];change=[];bkg=[]
  for e in row['events']:
   series=e['qlp'] if name=='qlp' else e['independent'][name];v=series['2'];u=series['1']
   if v:
    vals.append(v['depth']*1000);err.append(v['error']*1000)
    if u:change.append((u['depth']-v['depth'])*1000)
    if v['background_regressed_depth'] is not None:bkg.append((v['background_regressed_depth']-v['depth'])*1000)
  if vals: stats[name]=dict(depth_ppt_range=[min(vals),max(vals)],error_ppt_range=[min(err),max(err)],linear_minus_quadratic_ppt_range=[min(change),max(change)] if change else None,background_regressed_minus_original_ppt_range=[min(bkg),max(bkg)] if bkg else None)
 row['measurement_ranges']=stats
loc=json.load(open(D/'240360239/pixel-localization.json'));aa=[e['fits'] for e in loc['aperture_photometry']];a['240360239']=dict(sector=56,provenance='TESScut independently constructed aperture',source_receipt='240360239/pixel-localization.json',events=len(aa),quadratic_depth_ppt_range=[min(z[1]['depth'] for z in aa)*1000,max(z[1]['depth'] for z in aa)*1000],linear_depth_ppt_range=[min(z[0]['depth'] for z in aa)*1000,max(z[0]['depth'] for z in aa)*1000],note='No exact-target SPOC/TESS-SPOC/TARS product in shared MAST inventory. Same TESS pixels; 3-pixel-diameter aperture plus outer-pixel median background. Strong baseline sensitivity; conditional fixed-shape fit, formal errors in pixel-localization.json; no quality issues admitted in TESScut.')
json.dump(a,open(p,'w'),indent=2,allow_nan=False)
for tic,row in a.items():print(tic, row.get('measurement_ranges',row))
