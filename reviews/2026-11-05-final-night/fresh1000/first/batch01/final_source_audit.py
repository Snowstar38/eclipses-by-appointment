import csv,json,re
from pathlib import Path
b=Path(__file__).resolve().parent;rows=list(csv.DictReader((b/'RESULTS.csv').open()));holds={'1269035','71295367','92872537'}
for r in rows:
 tic=r['tic'];r['source_eligibility']='HOLD' if tic in holds else ('REFUTED' if tic=='98941880' else 'SUPPORTED_AT_TESS_RESOLUTION')
 if tic in holds:r['association']='UNRESOLVED_CLOSE_SOURCE_HOLD'
 if tic in ['1269035','92872537']:r['limitations']+=' A flux-capable subpixel Gaia neighbor remains unresolved; selected-source eligibility HOLD.'
 p=b/tic/'REPORT.md';s=p.read_text();s=re.sub(r'Association: [A-Z_]+\.',f"Association: {r['association']}.",s,count=1);s+='\n\n## Final neighbor audit\n\n'
 g=json.loads((b/tic/'helper-gaia-neighbors.json').read_text());s+=f"Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 {g['response_sha256']}. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.\n\n"
 for n in g['neighbors_sorted'][:8]:s+=f"Gaia{n['source_id']}, separation{n['sep_arcsec']:.3f}arcsec,G{n['G']:.3f}, idealized intrinsic loss{n['idealized_required_intrinsic_loss']:.3f}, WCS{n['wcs_xy']}.\n\n"
 if tic in holds:s+='Source eligibility HOLD: a capable subpixel neighbor cannot be distinguished securely. P describes repeated aperture eclipses; a selected-target claim is not accepted. For Z001 the centroid shifts toward the neighbor; for Z004 similarly; for Z005 it is mildly opposite, but separation0.68pixel remains unresolved without a deblended fit.\n'
 if tic=='98160330':s+='The capable neighbor38.65arcsec away is2.03pixels from target and opposite the observed small deficit-centroid displacement. The deficit peak is at target pixel(5,5), centroid(5.208,5.386) versus target(5.216,5.256). This resolved neighbor is strongly disfavored as main eclipse source. Close unresolved companions remain possible.\n'
 aa=json.loads((b/'lead-alias-covered-windows.json').read_text())[tic]
 for z in aa[:6]:s=re.sub(rf"\| {z['label']} \| ([^|]+) \| ([^|]+) \| [^|]+ \|",f"| {z['label']} | {z['period_d']:.8f} | {z['covered']} | {len(z['nulls'])} |",s)
 s+='\nA clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.\n'
 p.write_text(s,encoding='utf8')
with (b/'RESULTS.csv').open('w',newline='',encoding='utf8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
p=b/'LEAD-AUDIT.md';s=p.read_text();s+='\n\nFinal source audit: successful Gaia60arcsec cones for all eight. Z001,Z004,Z005 retain source eligibility HOLD due capable subpixel neighbors. Z007 remains C: its capable resolved neighbor is2.03pixels away opposite the tiny centroid offset, and the deficit is tightly target-centered. Z008 remains positively off source. Physical tiers remain1C,5P,1PLAUSIBLE,1REFUTED; three P cases are source holds and cannot be silently counted as selected-target claims. Null sensitivity was tightened before freeze: depth+4noise <0.5 representative depth; insufficient sensitivity is ambiguous.\n';p.write_text(s,encoding='utf8')
print('final source holds and sensitivity updated')
