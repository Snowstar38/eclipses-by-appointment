"""Write bounded scientific decisions for frozen batch06 after raw-sector inspection."""
from pathlib import Path
import csv,json
B=Path(__file__).resolve().parent
cases={
'H051':('The sector-80 screening dip at BTJD 3491.303 follows a multi-day downward drift into the midsector data gap. Its supposed recovery is the offset at the start of the next observing segment; the pre-gap flux does not show a resolved eclipse egress. Sector 49 has a similar reset and settling curve at a gap, while the other thirteen raw sectors show smaller changing baselines rather than a coherent 47.214 d eclipse kind. The screening window is therefore a gap/trend feature.', 'The selected sector-80 feature is refuted; these data do not rule out a weaker separate eclipse.', 'Only reconsider on a new resolved repeat with complete ingress and egress.'),
'H052':('Sector 96 shows a broad, changing wave through BTJD 3926.333 with irregular scatter in its trough; the raw curve continues to decline again after BTJD 3930. The selected trough tracks H057 in the same sector: an independent 0.1-day binned comparison over BTJD 3923–3929 has correlation 0.9755 across 58 paired bins (helper-common-s96.json). These are widely separated targets and the synchronized shape is positive contrary evidence for an individual eclipse. Earlier sectors 2, 29 and 69 show broad dips and rises at differing phases and widths.', 'The selected sector-96 eclipse interpretation is refuted; synchronized behavior does not identify a unique instrument mechanism or the source of the broader modulation.', 'Study the modulation with stable independent photometry if useful.'),
'H053':('The sector-94 dip near BTJD 3874.887 sits in a broad decline and recovery at BTJD 3874–3877 that also occurs in sector-94 raw SAP of H055 and H059, targets widely separated on the sky. The common-s94.json bins show all three low around 3875 and recovering by 3876. Earlier sectors 12 and 13 have smooth multi-day waves, and sector 67 has another gradual downturn, not isolated eclipse contacts. The common timed feature and changing baseline refute this selected eclipse.', 'A common feature is diagnostic, without identifying a unique instrumental mechanism or excluding an unrelated weaker eclipse.', 'Seek a new isolated complete event before timing or source analysis.'),
'H054':('The two sector-96 dip flags at BTJD 3921.793 and 3925.981 mark a large flux reset and subsequent settling across a sector gap. The raw sequence starts low after the gap and rises slowly, then jumps to a different level; there is no bounded dip with ingress and egress at either screening center. Sectors 2 and 29 lack a comparable eclipse feature.', 'The selected features are positive gap and step artifacts, so the eclipse interpretation is refuted.', 'Only revisit if a distinct complete repeat appears.'),
'H055':('The sector-94 candidate around BTJD 3875.079 is the same-time decline and rebound found in H053 and H059 at widely separated coordinates; common-s94.json records the synchronized minima and recovery. The bright flags in sectors 12 and 28 are strong upward ramps ending at data gaps, rather than opposite eclipse kinds. The 28-sector raw overview shows no coherent 24.962 d eclipse sequence matching these selected features.', 'Refutation applies to the selected dip and brightening interpretation; the target could host a weaker unrelated signal.', 'Look for a separate complete eclipse in future photometry before assigning a period.'),
'H056':('The sector-58 selected 0.06 d dip is one trough in rapid irregular oscillation of comparable amplitude. Similar oscillatory texture appears in sectors 18 and 85, with both dip and bright flags picking alternating extrema rather than separated eclipse contacts. The narrow local statistic does not trace a repeat of one eclipse kind.', 'The selected eclipse interpretation is refuted; the non-eclipse variability is not physically classified here.', 'Analyze the rapid variability separately if useful.'),
'H057':('Sector 96 has a broad wave and changing scatter around BTJD 3926.040, then another downward trend toward its end. Its selected trough tracks H052 at the same time: an independent 0.1-day binned comparison over BTJD 3923–3929 has correlation 0.9755 across 58 paired bins (helper-common-s96.json), positive contrary evidence for an individual eclipse. Sector 69 contains a much larger broad wave, sector 29 contains a large upward ramp, and sectors 103–104 show level changes around gaps. These are not a stable same-kind eclipse sequence at the Gaia 45.464 d period.', 'The selected eclipse feature is refuted; synchronized behavior does not assign a unique mechanism or exclude an unrelated eclipse.', 'Obtain stable independent photometry only if a distinct contact-shaped event emerges.'),
'H058':('The sector-102 screening dip near BTJD 4134.256 is actually the low plateau after an abrupt level change at a data gap; it persists for days without an eclipse egress. Sector 104 has another gap-reset low level, while sectors 28, 68 and 95 show rising ramps or edge decays. The bright flags pick those ramps, not a second eclipse kind.', 'The selected dip and brightenings are positive step/gap morphology, refuting an eclipse interpretation.', 'Reinspect only if a complete isolated repeat is observed.'),
'H059':('The sector-94 flagged dip at BTJD 3874.940 is embedded in the broad decline and rebound shared at nearly the same time by H053 and H055. The numeric common-s94.json comparison has all three low near BTJD 3875 and back up by 3876, despite distant sky positions. Sector 27 instead has another many-day variable trend, and sector 67 has a broad mild trough; neither gives a clean same-kind repeat.', 'The selected sector-94 eclipse is refuted; a weaker separate eclipse remains possible.', 'Require a new isolated complete event before source or timing work.'),
'H060':('The sector-23 raw SAP trough around BTJD 1934.287 is broad and coincides with continuous SAP_X/Y image-position drift. In the same QLP FITS, KSPSAP_FLUX is flat through the raw trough; that alternate reduction suppresses it. A WCS-located TESSCut aperture also varies strongly with pixel selection and has a large post-gap level change. Terra’s independent difference image between 1933.0–1933.8 and 1934.1–1935.2 shows a signed core/adjacent-pixel dipole rather than uniform PSF dimming (helper-h060-difference.json/png). Together these are positive pixel-redistribution evidence against the selected eclipse. Sector 50 contains no resolved counterpart.', 'Pixel redistribution, centroid drift and the reduction discrepancy support an instrumental origin of the selected trough; a reduction alone can suppress real signals. TESSCut is not a separate observing occasion.', 'Only reconsider on a distinct resolved event in stable photometry.'),
}
rows=[]
for q in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
 sid=q['sample_id'];tic=q['tic'];evidence,lim,nxt=cases[sid]
 src=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())
 sectors=','.join(str(x['sector']) for x in src['verified_files'])
 extras=''
 if sid in ('H053','H055','H059'):extras=' The cross-target numeric comparison is in ../common-s94.json and the independent fine-bin audit is in ../helper-common-s94.json/png.'
 if sid in ('H052','H057'):extras=' The independent same-time comparison is in ../helper-common-s96.json/png.'
 if sid=='H060':extras=' TESSCut receipt, WCS aperture numbers/plot, and the QLP SAP/KSPSAP/background/position comparison are in this target directory. The independent pixel difference is in ../helper-h060-difference.json/png.'
 report=f'''# {sid} — TIC {tic}

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 {q['gaia_dr3']}, {q['nss_type']}, orbital period {q['gaia_period_days']} d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: {sectors}. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

{evidence}

## Limits and next check

{lim} {nxt} No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory.{extras}
'''
 path=B/tic/'REPORT.md';path.write_text(report,encoding='utf-8')
 rows.append({'sample_id':sid,'tic':tic,'sample_stratum':q['sample_stratum'],'physical_verdict':'REFUTED','full_review_completion':'COMPLETE','novelty_status':'UNKNOWN','period_days':'','period_error_days':'','primary_epoch_btjd':'','depth_ppt':'','limitations':lim,'next_check':nxt,'report':str(path)})
with (B/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows),'COMPLETE reports/rows')
