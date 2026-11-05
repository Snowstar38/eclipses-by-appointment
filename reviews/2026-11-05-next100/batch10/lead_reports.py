import csv,json
from pathlib import Path
B=Path(__file__).resolve().parent
D={
'Q091':('REFUTED','Forty-two cached sectors contain 36 flagged windows. Representative windows are broad slopes and evolving baselines, with many split by gaps: S27 2049.18 and S33 2215.57 contain only about half their nominal cores. S64 3050.83 is a broad smooth trough rather than a discrete eclipse profile. Many other flags follow changes of sector baseline.','No repeatable isolated eclipse center is measured; the many screen times do not establish a cycle or Gaia association.','Selected multi-sector dips are explained by broad trends and gap interruptions; this does not exclude an unobserved weaker binary eclipse.','Seek a complete isolated repeated event with a stable local baseline.'),
'Q092':('REFUTED','Six sectors: S11 1602.95 is a broad valley leading into a multi-day rise, S38 2358.38 and 2344.20 are parts of long slopes, and S65 3075.25 is a monotonic decline across its window. S101 4106.32 and S102 4132.58 sit on rising baselines with gap steps; no coherent same-kind eclipse profile appears.','No measured eclipse centers or tested orbital cycle follow from those broad structures.','The selected repeat-sector interpretation fails on raw morphology; a weaker event elsewhere is not ruled out.','Obtain a complete isolated dip and an independently repeated occurrence.'),
'Q093':('PLAUSIBLE','Seven sectors. S101 shows a sharp entry and approximately 7-9 ppt asymmetric depression near BTJD 4112.1; it is distinct from the later large S101 gap. S94 3874.97 is a broad interrupted trough and S103 4165.05 is truncated by a gap.','The S101 feature has no secure same-kind recurrence or integer-cycle test; the screening center is not its measured center. Its asymmetry and baseline variations leave an instrumental or non-eclipse alternative. The sharp onset near 4112.02 coincides with a drop in Q099, although their recoveries differ; see lead-S101-control.png and numeric series.','One candidate event does not establish an eclipse or source ownership.','Inspect new sector coverage and obtain an isolated repeat with spatial localization.'),
'Q094':('PLAUSIBLE','Seven sectors. S93 near 3849.84 shows an approximately 10-ppt ingress and low points followed by a large gap that removes egress; S103 4172.17 is near the edge of available data and has no comparable complete event.','One partial feature cannot define an eclipse midpoint or test integer cycle counts. The S93 shape may be astrophysical or a gap-associated disturbance.','The evidence is a partial candidate, with recurrence and source attribution unestablished.','Obtain uninterrupted coverage of a comparable event and repeat.'),
'Q095':('PROBABLE','S8, S9, S62 and S89 show matching flat-bottom dips at measured centers 1528.1410, 1549.1704, 3000.0675 and 3736.0319 BTJD; independent trapezoids give 3.85, 3.97, 4.69 and 4.69 ppt depths. S99 is an extreme gap/baseline step, not an event.','A linear fit with cycles 0, 1, 70, 105 gives P=21.0275198 d and residuals under 0.0011 d. Tested P/2, P/3 and P/4 same-kind aliases predict well-covered nulls; S62 at 3010.582 has 172 core, 64+64 baseline points, maximum internal gap 0.00232 d and 0.276 ppt measured depth versus 3.686 ppt at the actual S62 event. See lead-alias.json for others. These are bounded tests, not an exhaustive alias proof. Gaia SB1 P=21.0288706 d; a source-specific edge-on approximation gives S8 conjunction 1528.873 versus measured 1528.141, phase offset -0.0348, without propagated covariance. This is not a full orbital-geometry test.','Repeated real eclipses are supported; definitive source attribution and Gaia association remain unresolved.','Obtain spatially resolved eclipse photometry and a covariance-aware Gaia conjunction test.'),
'Q096':('PLAUSIBLE','Two sectors show many rapid, rounded troughs and brightenings with varying shape and baseline. For example S23 1933.27 and 1933.97 are about 0.7 d apart, and S50 contains multiple comparable troughs; KSPSAP retains some of the short-timescale variations.','Multiple candidate minima do not establish same-kind eclipses or a stable cycle. Multiperiodic or evolving stellar variability is a serious alternative.','Eclipse interpretation, source ownership and orbital association remain insecure.','Model and localize the variability, then test whether a stable eclipse-shaped same-kind clock remains.'),
'Q097':('PLAUSIBLE','Sixteen sectors. S86 has a deep asymmetric trough of roughly 18 ppt near 3637.6 with a pre-event bump and slow recovery; the much shallower S25 feature near 1984.8 does not establish a same-kind repeat.','A single asymmetric candidate does not measure an orbital cycle; variability and instrumental alternatives remain.','Source ownership, eclipse interpretation and recurrence remain unresolved.','Obtain a second well-covered event with source localization.'),
'Q098':('REFUTED','S94 3874.94 is a broad trough with only 26% nominal core coverage across a gap. S101 4113.23 has roughly half its core and lies on a long decline ending in a gap and about 18-ppt post-gap step.','The shared gap-associated profiles are not discrete measured eclipses, and their timing cannot establish a cycle.','The selected flags are explained by interrupted baseline/systematic structures, without ruling out weaker unseen eclipses.','Seek a complete repeat away from spacecraft gaps.'),
'Q099':('REFUTED','S94 3874.87 is an interrupted broad depression; S101 4113.22 is a decline terminating in a gap with a roughly 11.5-ppt step; S103 4166.21 begins immediately after a gap with a roughly -13.3-ppt reset and recovery.','No measured complete same-kind eclipse is supported by these windows.','The selected repeat interpretation is refuted by gap and reset morphology; weaker independent events are not excluded.','Seek a complete repeat away from gap resets.'),
'Q100':('REFUTED','S89 3732.38 is a broad falling baseline ending at a gap and about 3.6-ppt step; S94 3875.02 is a broad interrupted trough with only 40% nominal core coverage. Similar S94 structure appears in Q093, Q098 and Q099.','Neither window provides a measured eclipse center or a same-kind cycle.','The selected flags are better explained by baseline changes and shared interrupted structure; weaker independent events remain possible.','Seek an isolated complete repeat outside the shared structure.')}
rows=[]
for q in csv.DictReader((B/'queue.csv').open(encoding='utf8')):
 sid=q['sample_id'];tic=q['tic'];v,raw,timing,limits,nxt=D[sid];d=B/tic;n=len(json.loads((d/'lead-context.json').read_text())['sectors'])
 extra = 'For Q095, TESSCut S62 and S89 deficit peaks lie on the WCS target pixel, with positive target-region baseline and 3x3 depths 5.95 and 4.31 ppt. MAST TIC identifies capable neighbors 23.42, 29.94 and 30.11 arcsec away with approximate T-band flux ratios 0.0338, 0.00627 and 0.182. Coarse pixels do not uniquely exclude blended origins. ' if sid=='Q095' else ''
 if sid=='Q093': extra += 'The S101 cutout shows a 2.84-ppt target-aperture deficit, but the common onset in Q099 makes source interpretation mixed. '
 if sid=='Q094': extra += 'The S93 difference image is speckled and its gap-limited post-event control is not a sensitive null. Direct VSX contains the positional match ASAS J164431-6315.0, typed MISC|SR, not an eclipsing-binary type. '
 if sid=='Q097': extra += 'The S86 cutout has a strong off-target spatial ramp and a positive target-region baseline; its target-centered aperture does not reproduce the QLP dip (-1.16 ppt deficit). The unstable cutout is not a clean null, but strongly weakens source ownership of the QLP trough. '
 if sid in ('Q093','Q094','Q097'): extra += 'On 2026-11-05 the MAST TESSCut coordinate sector inventory returned no sector later than the cached maximum, though it lists additional uncached earlier sectors; this availability result is not a photometric null. '
 text=f'''# {sid} - TIC {tic}

**Physical verdict:** {v}. **Review completion:** COMPLETE. **Catalogue novelty:** UNKNOWN.

## Raw morphology and coverage

{raw}

## Timing and interpretation

{timing}

## Source and reduction

{extra}See the independent helper audit for image and attribution checks. SAP and, where available, KSPSAP are displayed in the zoom plots; detrending may suppress long events, so suppression alone is not a refutation. Same photons in different reductions do not create another occasion. Screening centers are predictions rather than measurements.

## Limits and next check

{limits}

{nxt}

## Provenance

The batch lead-context script verifies source-packet, bulk-result and FITS hashes. Numeric `lead-context.json`, `lead-local-series.json` and `lead-flag-diagnostics.json` record raw times, fluxes, endpoints and gaps across {n} sectors; `lead-raw-context.png` and `lead-dip-zooms.png` show raw morphology. See batch `LEAD-SOURCE-HASHES.json`, `helper-audit.md`, and exact direct VSX receipt `../../tap-recovery/vsx-{sid}.json`. Other required catalogue scopes remain unavailable, so novelty is UNKNOWN; a generic variability type is not an eclipsing-binary classification.
'''
 (d/'REPORT.md').write_text(text,encoding='utf8')
 rows.append(dict(sample_id=sid,tic=tic,sample_stratum=q['sample_stratum'],physical_verdict=v,full_review_completion='COMPLETE',novelty_status='UNKNOWN',period_days='21.02752' if sid=='Q095' else '',period_error_days='',primary_epoch_btjd='1528.1410' if sid=='Q095' else '',depth_ppt='3.85' if sid=='Q095' else '',limitations=limits+' Catalogue novelty remains unknown.',next_check=nxt,report=str((d/'REPORT.md').resolve())))
with (B/'RESULTS.csv').open('w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)

