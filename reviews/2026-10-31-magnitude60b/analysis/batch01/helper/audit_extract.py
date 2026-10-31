import json,csv,pathlib,math,statistics,hashlib
base=pathlib.Path(r'[local path omitted] 5\made\sb1-scale'); out=pathlib.Path(r'[local path omitted]'); q=list(csv.DictReader(open(out.parent/'queue.csv'))); sp=base/'c5-sapdepth.json'; sap=json.load(open(sp)); rows=[]
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
for x in q:
 t=x['tic']; z=sap[t]; f=next((base/'diffimg'/t).glob('diff*.json')); j=json.load(open(f)); png=f.with_suffix('.png'); gp=f.parent/'gaia.json'; gj=json.load(open(gp)); ns=[]; cent=j['deficit_centroid']
 for n in j['neighbours_60']:
  if n['possible']:
   ns.append({'source_id':n['source_id'],'sep_arcsec':n['sep'],'G':n['G'],'intrinsic_depth_needed_approx':n['depth_needed'],'distance_deficit_px':math.dist(cent,n['px'])})
 ns.sort(key=lambda n:n['distance_deficit_px']); parity=[[],[]]
 for e in z['events']:
  k=round((e['tc']-z['t0'])/z['P']); parity[k%2].append(e['dep']/1000)
 nss=gj.get('nss',[]); ns0=nss[0] if nss else {}
 rows.append({'tic':t,'difference_image':str(png),'image_sha256':sha(png),'difference_data':str(f),'difference_sha256':sha(f),'gaia_data':str(gp),'gaia_sha256':sha(gp),'sector':j['sector'],'n_stacked_predicted_windows':j['n_events'],'target_offset_px':math.dist(j['target_px'],cent),'aperture_fractional_depth_1_3_5':[j.get('depth_ap1'),j.get('depth_ap3'),j.get('depth_ap5')],'capable_neighbors':ns,'search_spacing_days':z['P'],'historical_t0_prediction':z['t0'],'historical_even_odd_n':[len(v) for v in parity],'historical_even_odd_median_depth_ppt':[statistics.median(v) if v else None for v in parity],'queue_period_days':float(x['period_days']),'gaia_nss_period':ns0.get('period'),'gaia_nss_period_error':ns0.get('period_error')})
json.dump({'description':'Independent audit of historical spatial and SAP summary products. Windows and historical tc values are predictions, not fitted times. Possible-neighbor threshold is a rough Gaia brightness test, not a calibrated TESS-band aperture model. Difference centroid is not a formal localization uncertainty. Alternative cutout uses same photons as QLP.','sapdepth_file':str(sp),'sapdepth_sha256':sha(sp),'rows':rows},open(out/'attribution-audit.json','w'),indent=2)
for r in rows: print(r['tic'],round(r['target_offset_px'],3),[(round(n['distance_deficit_px'],2),round(n['sep_arcsec'],1),round(n['intrinsic_depth_needed_approx'],2)) for n in r['capable_neighbors'][:3]],r['gaia_nss_period'])
