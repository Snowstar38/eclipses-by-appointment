from pathlib import Path
import json,csv,hashlib,os
B=Path('Astra/made/remaining136-2026-11-01/batch01').resolve()
(B/'LEAD-AUDIT.md').write_text('''# Batch01 lead audit

Exact frozen queue of ten identities reviewed without substitutions. Outcome: six CONFIRMED, four PROBABLE, all ten bounded physical reviews COMPLETE. Catalogue novelty remains centrally reconciled; these are physical outcomes only.

Raw quality-zero QLP SAP_FLUX free-center fitting was freshly executed after changing c6 to c7 cache and removing all inherited target-specific branches. QLP FITS TICID, coordinates and sectors match exact targets; source hashes match prefetched bytes. No screening judgment was reused. The timing input error is max(formal local trapezoid covariance, half cadence); covariance is scatter inflated above reduced chi-square one. These are conservative allowances rather than calibrated coverage. Singular center covariance is rejected. Selected epoch is not assumed deeper primary.

Representative repeated raw eclipses, full source-specific NSS covariance geometry, all capable neighbors and alternative cutout reductions were checked. All ten historical pixel originals were visually inspected by lead and helper; fresh ephemeris/duration difference stacks were rerun for all ten and inspected independently by Terra. Lead additionally inspected fresh deciding 123220066 and 371665307 images. Cutout IDs, source astrometry and sector headers match; cutouts do not carry TICID. The historical extraction recipe was read: quality-zero full images, faintest-40-percent median background, local symmetric side windows, fixed target-centered apertures. It is a reused tested primitive, not an independent-code replication. Image residual is not a localization uncertainty; required intrinsic neighbor loss is never equated with diluted pixel loss.

Deciding exceptions: 150008480 (11 capable neighbors/noisy shallow deficit), 370553309 (16.6 arcsec near-equal blend), 1804347444 (3.45 arcsec brighter blend) remain PROBABLE for unresolved attribution. 371665307 remains PROBABLE for crowding plus a factor-two period ambiguity: measured 2.49543-day dips have inconclusive parity, while the reported 4.99086-day candidate ephemeris uses even parity only. The latter is not asserted to be a uniquely identified same-kind orbital period.

123220066 current MAST receipt identifies only five QLP sectors; missing S35/S89 were downloaded and measured, giving five actual centers. The bounded integer alias scan over 0.8-40d rejects all alternate candidates with sampled nulls; half period has four. The thresholds and 0.04-day timing tolerance are heuristic, not confidence levels. Terra inspected null windows and noted S35 interspersed flagged points and a shifted S89 feature: we claim sampled quality-zero cores, not entirely clean windows or exclusion of shallower secondaries. Its target-centered single-event difference favors the target over two capable separated neighbors, with noise/localization caveats.

78886343 and 65709882 have bright field sources that displace the light centroid but compact target-centered deficits distinct from capable neighbors. They are confirmed at TESS resolution with explicit limitations, not rejected merely for neighbor presence. The alternative-pipeline provenance is sector conditioned: same-sector reductions share photons; distinct cutout sectors are distinct observing occasions on one instrument and have no direct same-sector QLP comparison here.

No canonical/public files changed. Anonymous contributor note: Thanks to the project coordinator for the kind appreciation; the review team valued the opportunity to make the evidence and its limits clear.
''',encoding='utf8')
# All local and exact deciding external inputs; relative paths make manifest portable within repository layout.
H={}
def add(p):
 p=Path(p).resolve();H[Path(os.path.relpath(p,B)).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for rec in json.load(open(B/'measurement-source-receipts.json')):add(rec['path'])
for rec in json.load(open(B/'terra/pixel-audit.json')):
 for p in rec['files']:add(p)
for p in [B.parent/'targets-selected.json',B.parent/'shared-catalogues/gaia-nss-full.csv',B.parent/'shared-catalogues/123220066-mast-availability.json',Path('Fable 5/made/sb1-scale/search.jsonl'),Path('Fable 5/made/sb1-scale/c7-sapdepth.json'),Path('Fable 5/made/sb1-scale/diffimg/diffstack.py'),B/'methods-read-snapshot.html']:add(p)
for p in B.rglob('*'):
 if p.is_file() and p.name not in ['SHA256SUMS.json','root-verification.json'] and '__pycache__' not in str(p):add(p)
(B/'SHA256SUMS.json').write_text(json.dumps(dict(sorted(H.items())),indent=2)+'\n',encoding='utf8')
print(len(H))
