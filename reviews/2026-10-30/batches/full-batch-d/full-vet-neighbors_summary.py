import csv,json,pathlib,math
D=pathlib.Path(__file__).parent; T=json.loads((D.parent/'targets-selected.json').read_text()); res={r['tic']:float(r['screen_depth_median_ppt'])/1000 for r in csv.DictReader((D.parent/'RESULTS.csv').open())}
with (D/'neighbors_summary.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['tic','source_id','sep_arcsec','Gmag','BP-RP','required_fraction_G_approx','capable'])
 for p in D.glob('*_neighbors_ari.csv'):
  tic=p.name.split('_')[0];tg=float(T[tic]['gaia']['phot_g_mean_mag']); rows=list(csv.DictReader(p.open()))
  for r in rows:
   if r['source_id']==T[tic]['gaia']['source_id']:continue
   req=res[tic]*10**(.4*(float(r['phot_g_mean_mag'])-tg));w.writerow([tic,r['source_id'],round(float(r['sep']),2),r['phot_g_mean_mag'],r['bp_rp'],round(req,3),req<=1])
print((D/'neighbors_summary.csv').read_text())
