from pathlib import Path
import csv,json
b=Path(__file__).resolve().parent;p=b/'RESULTS.csv';rows=list(csv.DictReader(p.open()))
for r in rows:
 r['source_eligibility']='REFUTED' if r['tic']=='98941880' else ('HOLD' if r['tic']=='71295367' else 'PENDING_FINAL_HELPER_AUDIT')
 if r['tic']=='71295367':
  r['association']='UNRESOLVED_CLOSE_SOURCE_HOLD';r['limitations']+=' Gaia neighbor1096049201238750976 at9.21arcsec,G15.7005 is flux-capable and the deficit centroid lies toward it; selected-source attribution is on hold.'
with p.open('w',newline='',encoding='utf8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
p=b/'71295367/REPORT.md';s=p.read_text();s=s.replace('Association: SHORT_PERIOD_BYCATCH.','Association: UNRESOLVED_CLOSE_SOURCE_HOLD. Publication/source eligibility: HOLD.');s+='\n\nGaia neighbor1096049201238750976 is9.21arcsec from target, G15.7005 versus target11.992. Relative G flux0.03285 would require about63.2% intrinsic loss in an idealized fully captured target+neighbor blend to explain the2.01% custom3x3 loss. This budget is approximate because G differs from TESS and throughput is unknown. Target WCS(5.066,5.536), neighbor(5.504,5.654), positive deficit centroid(5.315,5.675): the centroid lies toward the capable neighbor. This is not calibrated/deblended astrometry; the neighbor remains a credible alternate source. P describes real repeated aperture eclipses; the selected Gaia source is not established.\n';p.write_text(s,encoding='utf8')
p=b/'LEAD-AUDIT.md';s=p.read_text();s+='\n\nZ004 source eligibility HOLD: a flux-capable Gaia neighbor9.21arcsec away aligns with the deficit-centroid displacement; aperture eclipse P is retained but selected-source attribution cannot be accepted from these pixels.\n';p.write_text(s,encoding='utf8')
