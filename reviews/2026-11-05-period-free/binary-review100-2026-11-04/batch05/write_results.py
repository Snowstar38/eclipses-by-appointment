"""Write bounded, individually assessed batch05 reports and result rows."""
import csv, json
from pathlib import Path
B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))

R={
'312968253':('REFUTED','','','','',
 'The selected s102/s103 dips are discontinuities and changing baselines, not repeatable eclipse profiles. This refutes these flags, not every possible binary signal.',
 'If useful, inspect a future continuous event with a stable aperture.',
 's102 at 4133.85 BTJD jumps down at a data break and climbs for days; s103 at 4170.35 falls into a break and resumes higher. The screen centers are 36.50 d apart, versus Gaia SB1 29.43568 d. s38 has a small notch near 2353.16 amid variable baseline and s11 is noisy, but neither forms a matching clock. Gaia conjunction predictions in the cached sectors do not trace the two selected steps. No eclipse epoch/depth is assigned.'),
'313617927':('CONFIRMED','38.5','','','',
 'The result period 38.5 d is the rounded 38.5098-d separation of two measured same-kind events, not a calibrated long-baseline ephemeris. Gaia P=38.431544 d is separate orbital context. Broad eclipses lie on strong varying baselines; local centers have uncalibrated systematic errors. Pixel and aperture checks share TESS photons.',
 'Obtain an independent future event and precision timing to characterize the orbit.',
 'Deep A-like troughs occur around BTJD 1730 (s15), 1768.4 (s17), 2845.5 (s56), 3383.5 (s76), 3422 (s77), and 3576 (s83). An independent local trapezoid fit measures the first two centers at 1729.9242 and 1768.4340 BTJD, separated by 38.5098 d; changing baseline and morphology dominate uncalibrated error. Other sectors and Gaia SB1 P=38.431544 d support one same-kind cycle, with opposite-kind events around 1749 (s16, partial), 1788 (s17), 2827 (s56), 3402 (s77). Tested n=3–8 aliases of the two measured events predict additional same-kind troughs in well-covered s16 windows: e.g. n=3 at 1755.60 has 24/24 expected core cadences and both baselines covered, with only +0.49 ppt core-minus-side rather than a ~30-ppt dip; n=4 at 1758.81 is also covered without a matching dip. n=2 falls near the observed opposite-kind conjunction; the two distinct eclipse kinds and near-circular Gaia geometry favor the full period. Gaia e=0.0129 predicts conjunctions about 19 d apart and places s56/s76/s77 events near expected windows. Gaia t_periastron has a 2.05-d marginal error, so ~1-d absolute offsets are not a clean contradiction. An independent 5-pixel cutout aperture detects the s15 dimming by about 32.6 ppt and places its positive difference centroid 0.18 pixel from target WCS. The nearest substantial Gaia neighbor (G14.71, 19.8 arcsec) would need roughly 1.93 times its G flux to explain that aperture loss under generous full-inclusion assumptions. This bandpass-dependent support is not a strict exclusion.'),
'154809818':('REFUTED','','','','',
 'The selected shallow dips track irregular oscillatory variability; the Gaia AstroSpectroSB1 orbit has no phase elements in the source packet. Refutation is limited to the screened eclipse interpretation.',
 'Use higher cadence stable-aperture data if the short-timescale variability itself is of interest.',
 'Representative s14, s40, s53 and s79 raw SAP panels show multiple rounded troughs and peaks of similar scale that move across each sector without flat-bottom or repeated contact structure. The screen reports 11 retained dips across six sectors, but s40 2417.38, s53 2756.99 and s79 3462.24 occur amid the same oscillatory pattern. Gaia period 59.09572 d alone supplies no conjunction phase and does not turn these variable troughs into repeated eclipses. The broad all-sector plots were checked; no defensible eclipse center/depth is assigned.'),
'198182954':('REFUTED','','','','',
 'The selected flags are smooth, evolving short-timescale stellar variability. This does not exclude a separate unrecognized eclipsing system.',
 'Characterize the oscillation/rotation signal separately if scientifically useful.',
 'All 42 cached sectors were examined in raw SAP context. The s15/s19/s23 and s74 troughs recur on a roughly several-day wave whose shape, amplitude and phase evolve; many comparable troughs and peaks occur between Gaia SB1 23.37508-d conjunction windows. The s74 3324.49 cutout has a target-centered difference within about 0.60 pixel and an 8.46-ppt broad dimming, so the variability is real at the target but is not an eclipse-shaped contact event. A single faint G20.04 neighbor at 18 arcsec is not a useful explanation for this broad target signal. No eclipse timing, depth, or cycle count is inferred from selected smooth minima.'),
'289989985':('REFUTED','','','','',
 'Selected events are edge/gap and baseline features; no repeated eclipse clock is established. This does not decide whether the SB1 star is otherwise variable.',
 'Reobserve a continuous predicted conjunction if the spectroscopic binary merits photometry.',
 's64 3054.73 drops into an interruption after a broad hump, and s101 4119.42 is a small decline at a break followed by an offset level. s90 3768.16 and s10 1580.33 are lower-amplitude short structures on changing baselines. Their separations and shapes do not repeat at Gaia SB1 25.62156 d. The full raw sector plots reveal no consistent ingress, bottom and egress for the selected flags. A core median at a gap edge cannot supply a depth or a null.'),
'246124257':('PROBABLE','3.419619','','2362.416','6',
 'Target attribution is limited by a capable G14.35 neighbor 32.6 arcsec away; the Gaia SB2 orbit is 42.40901 d and does not describe the 3.41962-d photometric clock. The quoted clock is exploratory with no calibrated error; the 6-ppt depth is representative.',
 'Resolve the target and nearby G14.35 star during a narrow eclipse; then determine whether the 3.42-d and 42.41-d orbits form a hierarchical system.',
 'This is a real alternating deep/shallow eclipse train. Deep narrow minima in s12/s39/s66/s93/s103/s104 give 32 selected raw SAP minima spanning 2572 d; fitting their integer cycles gives P=3.41961896 d and epoch BTJD 2362.41582, with 0.00985-d residual scatter. Same-sector 3.42-d deep repeats and intermediate shallow minima constrain long-baseline aliases. The s66 3101.04 cutout independently recovers a ~5.94-ppt dimming with difference centroid 0.20 pixel from the target WCS. A pattern fit to the difference image favors target PSF over the offset G14.35 neighbor (RMS 1.19 vs 21.78 counts/pixel), but is empirical and uncalibrated. Gaia DR3 reports an SB2 42.409012-d orbit, not compatible with this eclipse clock if it is the same pair. The G14.35 source 32.6 arcsec away is flux-capable under a generous Gaia-G bound (~85% intrinsic disappearance required); its WCS pixel lies ~1.7 pixels from the target. The unresolved blend and orbital conflict prevent a confirmed association.'),
'101107570':('PLAUSIBLE','','','','',
 'The shallow events are near the raw noise and changing baseline, so the eclipse interpretation is insecure; this is not a physical null on the SB1 star.',
 'Acquire a continuous high signal-to-noise conjunction light curve and check difference pixels if a coherent event appears.',
 'The s8/s34/s61/s99 flagged windows have local core medians only about 2–4 ppt from flanks and show inconsistent shapes. s8 1523.49 has few points; s34 2249.81 sits amid spikes and low-level fluctuations; s61 2978–2984 is a broad wandering baseline; s99 4050.73 is a diffuse trough in evolving scatter. The full raw sector context has similar unflagged excursions. No positive instrumental signature proves every dip false, but these selected features do not yet trace a secure repeatable eclipse at Gaia SB1 P=23.93198 d. No center or physical depth is justified.'),
'174187654':('REFUTED','','','','',
 'The selected s93/s102/s103 features are dominated by aperture/source contamination and sector discontinuities; the target might still have unrelated variability.',
 'Use resolved photometry to determine the bright neighboring star’s variability if desired.',
 'Raw SAP s93 has a broad asymmetric drop near 3837.15 amid strong secular variation. s102/s103 have very large jumps at sector breaks and slopes over many days, not recurring contact profiles at Gaia SB1 24.8894 d. The s93 TESSCut WCS shows a much brighter off-target source near pixel (2,6); the difference is dominated by that source while the target aperture gives only ~0.06 ppt under the chosen in/out windows and a poorly defined 0.99-pixel centroid. This extraction is not a trustworthy eclipse depth or localization. The selected dip interpretation is positively contradicted by the pixel and gap morphology.'),
'299397214':('REFUTED','','','','',
 'Two selected flags are level changes on broad trends. Neither provides a complete eclipse profile or a two-event timing baseline.',
 'Inspect a future uninterrupted Gaia conjunction if orbital eclipses remain of interest.',
 'At s101 4108.24, the light curve descends over days into a small level step and flat segment; the screen core median is essentially zero relative to flanks. At s102 4146.24, a gap precedes an abrupt ~1–2% level change, then a slow slope. Full s39/s103 contexts also show strong broad nonstationary trends. The two selected centers differ by ~38 d, close to Gaia SB1 P=37.72190 d, but they are gap-associated level changes rather than measured eclipse centers. Numerical proximity alone cannot establish recurrence.'),
'424916690':('REFUTED','','','','',
 'Selected windows are data-break steps and slopes, without repeatable eclipse contacts. This verdict applies to the selected claim only.',
 'If still needed, observe a continuous predicted conjunction with a stable aperture.',
 's27 2047.53 falls into a gap after a long decline; s94 3874.87 is a short shelf and step on a steep trend; s104 4185.09 is an abrupt level reset at a break with recovery over days. The other cached sectors show similarly changing long baselines. No three-part eclipse profile or same-kind repetition on Gaia SB1 P=39.45197 d follows from the flags. Gap-edge medians are not physical depths, and no period/epoch is assigned.'),
}

with (B/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['sample_id','tic','sample_stratum','physical_verdict','full_review_completion','novelty_status','period_days','period_error_days','primary_epoch_btjd','depth_ppt','limitations','next_check','report']
    wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader()
    for q in Q:
        tic=q['tic'];ver,p,pe,epoch,depth,limit,nxt,body=R[tic]
        d=B/tic; raw=json.loads((d/'raw-inspection.json').read_text())
        report=d/'REPORT.md'
        extras=[]
        if (d/'deep-clock.json').exists():extras.append('[deep-clock.json](deep-clock.json)')
        if (d/'a-timing.json').exists():extras.append('[A-event timing](a-timing.json)')
        if tic=='313617927' and (B/'helper-timing-audit.json').exists():extras.append('[independent timing and alias coverage](../helper-timing-audit.json)')
        if tic in ('313617927','246124257') and (B/'helper-spatial-audit.json').exists():extras.append('[independent difference-pattern audit](../helper-spatial-audit.json)')
        if tic in json.loads((B/'lead-source-attribution.json').read_text()):extras.append('[TESSCut receipt](../lead-pixels/'+tic+'/receipt.json) and [difference image](../lead-pixels/'+tic+'/difference.png)')
        report.write_text(f"# {q['sample_id']} - TIC {tic}\n\n**Physical verdict: {ver}. Bounded review: COMPLETE. Catalogue novelty: UNKNOWN.** This is one frozen {q['sample_stratum']} lead, not a new counted acceptance.\n\n{body}\n\n**Limits and next check.** {limit} {nxt}\n\n**Evidence and method.** Examined all {len(raw['sectors'])} cached sectors in raw SAP with quality=0, including [representative window data](raw-inspection.json), [raw panels](raw-windows.png), and [full sector / Gaia orbit context](orbit-context.json). Screen windows are predictions, not measured centers. Source [packet](../../source-packets/{tic}/sources.json) and the original bulk JSON/FITS SHA-256 values are preserved in raw-inspection.json. {', '.join(extras)}. Gaia flux ratios are approximate. The central catalogue review could not query four required novelty gates, so UNKNOWN remains regardless of cached primary nonmatch.\n",encoding='utf-8')
        wr.writerow({'sample_id':q['sample_id'],'tic':tic,'sample_stratum':q['sample_stratum'],'physical_verdict':ver,'full_review_completion':'COMPLETE','novelty_status':'UNKNOWN','period_days':p,'period_error_days':pe,'primary_epoch_btjd':epoch,'depth_ppt':depth,'limitations':limit,'next_check':nxt,'report':str(report)})
print('wrote',len(Q),'reports')

