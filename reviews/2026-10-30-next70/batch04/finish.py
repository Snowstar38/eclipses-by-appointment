from pathlib import Path
import json,csv,hashlib,collections
B=Path(__file__).parent;D=B.parent
exec(compile((B/'make_reports.py').read_text(),str(B/'make_reports.py'),'exec'))
for tic,note in {
 '432482170':'Prior-EB identification: exact TIC/Gaia ASAS-SN EA J000026.84+393855.4, separation 0.28 arcsec, catalogue period 3.5877 d. This is a physically reviewed known EB, not an uncatalogued discovery.',
 '326623940':'The 0.20 arcsec VSX VAR entry GDS_J1400595-632825 may be the target; exact ASAS-SN ROT: and VAR do not classify an EB. Retain the identity caveat without treating it as prior-EB evidence.',
 '364120441':'The independent sector-20 aperture depths are only 35.5–37.7 ppt versus about 101 ppt QLP depths in sectors16/86. The reductions show repeated eclipses at matching phases but do not agree in depth. Aperture/sector dilution, systematics and differing measurement definitions are possible contributors; no cause is established. Core-median depths can underestimate the deepest point of V-shaped events. The spatial deficit test, rather than assumed equal depths, supplies attribution evidence.',
 '39069184':'Physical verdict is PLAUSIBLE because source attribution to the Gaia SB1 remains unresolved against the flux-capable 2.21 arcsec neighbour. Execution is complete if the independent reduction is available; the limitation is scientific ambiguity.'}.items():
 p=B/f'TIC-{tic}.md';p.write_text(p.read_text()+'\n'+note+'\n')
for p in B.glob('TIC-*.md'):
 s=p.read_text().replace('â€“','–')
 s=s.replace('Execution is complete if the independent reduction is available','Execution is complete')
 s+='\nIndependent measurements use core medians rather than the QLP trapezoid depth, so numerical equality of the depths is not assumed. Product-inventory failures are preserved; this check uses an independent aperture extraction, not a separately delivered pipeline product.\n'
 if p.name=='TIC-364120441.md':s+='\nBounded same-sector check: sector20 QLP core depths103.37,98.69,95.98ppt versus3x3 depths37.71,35.73,35.54ppt at the same primary epochs. Pixel1x1 depths69.24–75.92ppt and5x5 depths26.59–27.72ppt demonstrate strong aperture dependence. The G10.43 neighbour is about2.07 times the G flux of the G11.22 target, sufficient to make this dilution plausible. Deficit target/neighbour distances are3.01/35.25arcsec. See DEPTH-SANITY-364120441.md and depth-sanity-364120441.json for counts, provenance and limitations; source/timing evidence supports the target.\n'
 s+='\nSeparate central open-release comparison found no exact Gaia/TIC overlap in the available track3/dossier tables; overlap with the embargoed 93-system release is unknown. This is not an additional EB gate. See ../shared-catalogues/README.md.\n'
 p.write_text(s)
rows=list(csv.DictReader((B/'RESULTS.csv').open()))
expected=[r['tic'] for r in csv.DictReader((D/'queue.csv').open()) if r['batch']=='4']
assert [r['tic'] for r in rows]==expected and len(list(B.glob('TIC-*.md')))==10
for t in expected:
 assert t in (B/f'TIC-{t}.md').read_text()
manifest=json.loads((B/'raw-evidence/qlp-manifest.json').read_text())
for r in manifest:
 p=B/r['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
ind=json.loads((B/'raw-evidence/independent-results.json').read_text())
for r in ind:
 if not r.get('measurements'):continue
 p=Path(r['source_path']) if 'source_path' in r else B/'raw-evidence'/r['tic']/f"indep_s{r['sector']:03d}.fits"
 assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
(B/'VALIDATION.json').write_text(json.dumps(dict(targets=expected,reports=10,result_rows=10,physical_counts=dict(collections.Counter(r['physical_verdict'] for r in rows)),execution_counts=dict(collections.Counter(r['execution_completion'] for r in rows)),qlp_hashes_verified=len(manifest),independent_hashes_verified=sum(bool(r.get('measurements')) for r in ind),lead_review='All ten raw event panels; two capable-neighbour difference panels and numeric source/Gaia diagnostics reviewed.'),indent=2))
(B/'CONTRIBUTORS.md').write_text('The batch lead adjudicated sources, Gaia orbit geometry and reports. A fresh GPT-6.1 Terra helper independently reviewed raw eclipses and measured an independent reduction. The project coordinator set the review scope.\n')
(B/'README.md').write_text('Batch04 reviews queue positions31–40 under ../BRIEF.md. Ten reports and ten result rows separate physical verdict, execution and scoped novelty. TIC39069184 retains unresolved close-neighbour attribution; TIC432482170 is a known ASAS-SN EA. Representative eclipse fits use conditional cycle counts; two-event residuals imply no precision. Adapted scripts, original receipts, product identity checks, input provenance and SHA256 hashes are retained. No source/paper changes or commits.\n')
hashes=[dict(path=str(p.relative_to(B)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in B.rglob('*') if p.is_file() and p.name!='MANIFEST-SHA256.json']
(B/'MANIFEST-SHA256.json').write_text(json.dumps(hashes,indent=2))
print(collections.Counter(r['physical_verdict'] for r in rows),len(hashes))
