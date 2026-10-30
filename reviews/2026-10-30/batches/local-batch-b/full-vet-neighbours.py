"""Fresh ARI neighbour dilution table, G-band proxy explicitly not aperture-weighted TESS."""
import csv,json,pathlib
R=pathlib.Path(__file__).parent;s=json.loads((R.parent/'selected.json').read_text());depth={x['tic']:float(x['median_depth_ppt'])/1000 for x in csv.DictReader((R.parent/'RESULTS.csv').open())};out=[]
for tic,t in s['targets'].items():
 rows=list(csv.DictReader((R/f'{tic}_ari_neighbours.txt').open())); target=next(x for x in rows if str(x['source_id'])==str(t['gaia']['source_id'])); gm=float(target['phot_g_mean_mag'])
 for x in rows:
  if str(x['source_id'])==str(t['gaia']['source_id']):continue
  dg=float(x['phot_g_mean_mag'])-gm; req=depth[tic]*10**(.4*dg)
  out.append(dict(tic=tic,source_id=x['source_id'],sep_arcsec=x['sep'],G=x['phot_g_mean_mag'],delta_G=dg,required_fraction_G_proxy=req,can_eclipse_under_proxy=req<=1,variability=x['phot_variable_flag'],caveat='G not TESS; assumes equal aperture throughput; unresolved sources not tested'))
with (R/'neighbours-dilution.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(out)
for tic in s['targets']:
 rows=[x for x in out if x['tic']==tic and x['can_eclipse_under_proxy']]
 print(tic,'potential',[(x['source_id'],round(float(x['sep_arcsec']),1),round(x['required_fraction_G_proxy'],3)) for x in rows])
