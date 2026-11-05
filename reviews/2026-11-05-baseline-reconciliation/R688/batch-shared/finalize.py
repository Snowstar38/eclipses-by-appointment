"""Build the exact one-row result and hash manifest after helper final audit."""
import csv,hashlib,json
from pathlib import Path
H=Path(__file__).parent; T=H/'412639100'
q=list(csv.DictReader(open(H/'queue.csv')))
assert len(q)==1 and q[0]['tic']=='412639100' and q[0]['gaia_dr3_source_id']=='2204160934098817280'
sap=json.load(open(H/'sap-measurements.json')); geo=json.load(open(H/'gaia-geometry.json'))
alt=json.load(open(H/'alternative-measurements.json'));nb=json.load(open(H/'gaia-neighbors.json'));px=json.load(open(H/'pixel-check.json'))
measurement=dict(tic='412639100',gaia_dr3_source_id='2204160934098817280',physical_verdict='PLAUSIBLE',full_review_completion='COMPLETE',counted_eb=False,measured_eclipse_period_days=None,measured_eclipse_period_error_days=None,measured_eclipse_epoch_btjd=None,measured_central_eclipse_depth_ppt=None,screening_bls_period_days=sap['screening_period_days'],screening_bls_epoch_btjd=sap['screening_epoch_btjd'],screening_bls_width_days=sap['screening_width_days'],screening_bls_depth_ppm=154.7406483363364,conditional_fixed_window_median_depth_ppm=120.25002886212333,conditional_depth_note='Fixed screening windows after local linear shoulder normalization; not a central eclipse depth or per-event timing.',raw_sap=sap,gaia_geometry=geo,alternative_reduction=alt,gaia_neighbors=nb,pixel_check=px,limitations='Broad roughly day-long trough without stable eclipse contacts; free minima wander; no secure measured eclipse period, epoch, depth or source. Heartbeat-like periastron modulation and neighbor/systematic contributions remain possible.',next_check='Resolved high-precision photometry at both Gaia conjunction kinds, with contacts and pixel attribution.')
(T/'measurements.json').write_text(json.dumps(measurement,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
fields=['tic','physical_verdict','full_review_completion','period_days','period_error_days','primary_epoch_btjd','depth_ppt','limitations','next_check','source_report','report']
row=dict(tic='412639100',physical_verdict='PLAUSIBLE',full_review_completion='COMPLETE',period_days='',period_error_days='',primary_epoch_btjd='',depth_ppt='',limitations=measurement['limitations'],next_check=measurement['next_check'],source_report=str(T/'measurements.json'),report=str(T/'REPORT.md'))
with (H/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerow(row)
files=[H/x for x in ['queue.csv','queue-seal.json','analyze_sap.py','sap-measurements.json','raw-events.png','raw-stacked.png','gaia_geometry.py','gaia-geometry.json','query_gaia_photometry.py','query_gaia_neighbors.py','gaia-neighbors-source.xml','gaia-photometry-source.xml','gaia-neighbors.json','mast_availability.py','mast-availability.json','fetch_alternative.py','alternative-receipts.json','tess-spoc-s056.fits','tess-spoc-s084.fits','analyze_alternative.py','alternative-measurements.json','alternative-events.png','fetch_pixels.py','pixel-receipts.json','tess-spoc-s056-tp.fits','tess-spoc-s084-tp.fits','pixel_check.py','pixel-check.json','pixel-check.png','helper-local-depth.py','helper-local-depth.json','helper-audit.md','LEAD-AUDIT.md','RESULTS.csv','finalize.py']]
files += [T/'REPORT.md',T/'measurements.json']
pilot=H.parent/'pilot48'
files += [pilot/'pilot.json',pilot/'screening.jsonl',pilot/'triage'/'full-review-queue.csv',pilot/'triage'/'REPORT.md',pilot/'triage'/'raw-event-samples.json',pilot/'shared-catalogues'/'REPORT.md',pilot/'shared-catalogues'/'verification.json',pilot/'shared-catalogues'/'raw'/'gaia_nss.txt']
files += [Path(r'[local-path-redacted] 5.1/made/paper/short/sec_methods.html')]
files += [Path(x['path']) for x in sap['source_receipts']]
files += [Path(x['path']) for x in json.load(open(H/'alternative-receipts.json'))+json.load(open(H/'pixel-receipts.json'))]
files=list(dict.fromkeys(files))
assert all(p.exists() for p in files)
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(H/'SHA256SUMS.json').write_text(json.dumps(hashes,indent=2)+'\n')
print('result rows',len(list(csv.DictReader(open(H/'RESULTS.csv')))),'manifest files',len(hashes))
