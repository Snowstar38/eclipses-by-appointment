"""Summarize all historically flux-capable Gaia neighbors in cached TESScut stacks."""
import csv, glob, hashlib, json, math
from pathlib import Path

B=Path(__file__).resolve().parent
SB=Path('[local-path-redacted] 5/made/sb1-scale/diffimg')
out={}
for row in csv.DictReader((B/'queue.csv').open()):
    tic=row['tic'];stacks=[];adopted_depth=json.loads((B/tic/'measurements.json').read_text())['depth_ppt']/1000
    for p in sorted((SB/tic).glob('diff_s*.json')):
        d=json.loads(p.read_text());target=d['target_px'];centroid=d['deficit_centroid']
        capable=[]
        for n in d['neighbours_60']:
            adjusted=n['depth_needed']*adopted_depth/d['depth_ap3']
            if adjusted>1.05: continue
            capable.append(dict(source_id=n['source_id'],G=n['G'],target_sep_arcsec=n['sep'],cached_intrinsic_required_eclipse_fraction=n['depth_needed'],required_fraction_at_adopted_depth=adjusted,deficit_sep_arcsec=math.dist(centroid,n['px'])*21,position_px=n['px'],borderline=adjusted>1))
        capable.sort(key=lambda x:x['target_sep_arcsec'])
        stacks.append(dict(sector=d['sector'],source_path=str(p),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),n_events=d['n_events'],target_pixel=d['target_pixel'],peak_pixel=d['peak_deficit_px'],deficit_target_arcsec=math.dist(target,centroid)*21,psf_fractional_residual=d['psf_fit_frac_resid'],ap3_fractional_depth=d['depth_ap3'],adopted_qlp_depth_fraction=adopted_depth,gaia_limit_G=d['G_limit_for_depth'],cached_n_capable=d['n_possible'],n_capable_at_adopted_depth=sum(n['required_fraction_at_adopted_depth']<=1 for n in capable),capable_and_borderline=capable))
    out[tic]=dict(stacks=stacks,threshold_meaning='Cached diffstack approximate Gaia-G flux-ratio intrinsic eclipse fraction needed to explain observed blended deficit, scaled linearly to adopted QLP depth. This is not observed pixel fractional loss and ignores TESS color and actual aperture throughput. Capable threshold <=1, borderline to 1.05 included. Configured search radius 60 arcsec except 187202091 historical manual stack 90 arcsec. Pixel scale 21 arcsec. Source-centroid distances lack calibrated covariance and do not by themselves exclude close neighbors.')
(B/'neighbor-inspection.json').write_text(json.dumps(out,indent=2))
