"""Write reviewable Q031-Q040 reports from verified numeric evidence and visual review."""
import csv,json
from pathlib import Path
B=Path(__file__).resolve().parent
DATA={
'Q031':dict(v='CONFIRMED',p='42.54',ep='2123.10',depth='5.6',
 finding='Three same-kind raw SAP dips at BTJD 2123.0984 (S30), 2165.6410 (S31), and 3952.2486 (S97) support a conditional 43-cycle period of 42.5384 d. The middle event misses that prediction by only +0.0042 d, whereas the adjacent 42/44 long-baseline aliases miss it by -1.009/+0.971 d. S31 also has a distinct shallower event near 2146.48, which is treated as another eclipse kind rather than a half-cycle constraint. The S97 main event retains a full measured core and baseline; S31 main event is close to a gap, so its Gaussian timing is diagnostic. A covered S97 P/2 prediction at 3973.518 has -0.15 ppt local depth with 138 of 138 expected core cadences, versus ~5.6 ppt in the observed S97 event; covered P/3 and P/4 predictions are also flat.',
 physics='Gaia SB1 P42.54056 d agrees with the conditional eclipse clock. Source-specific edge-on A conjunction is BTJD 2123.1794, 0.0810 d after the measured S30 center (phase -0.0019). Fresh 11x11 TESSCut target-centered extractions retain 5.26, 4.28, and 6.17 ppt losses in S30/S31/S97, with difference centroids 0.26, 0.14, and 0.11 pixel from target WCS. The nearest other Gaia source in 120 arcsec is G16.67 at 31.6 arcsec, with nominal G flux ratio only ~0.0006 to this G8.61 target; this favors target ownership.',
 limits='Same-photon KSPSAP and TESSCut extractions are alternate reductions, not new observing occasions. The S31 ingress is near a 0.153-day gap and local Gaussian centers depend on baseline and morphology; the catalogue period column is rounded to 42.54 d and no precision period error is justified. Gaia G flux contrast is bandpass dependent, while the WCS evidence supplies the stronger source-location check.',
 next='Obtain a later clean target-centered main eclipse to refine the timing and check for an unresolved close companion.'),
'Q032':dict(v='REFUTED',p='',ep='',depth='',
 finding='S94 selected windows at 3869.644 and 3874.878 land exactly at actual data-gap boundaries; the former has a -7.42 ppt median step across its nearest gap, and the latter covers only 38% of its nominal core. S104 4197.371 likewise has only 44% nominal core coverage and an abrupt gap-associated recovery. S102 4144.319 is a shallow ripple/step on a changing baseline. The S94 3874.9 trough occurs at nearly the same time and shape in Q035/Q037/Q038/Q039 on multiple CCDs, so the selected repeat-sector pattern is common instrumental structure.',
 physics='No stable same-kind eclipse train or source-specific Gaia conjunction timing can be measured from these flagged windows.',
 limits='Refutes the selected eclipse interpretation, not the possibility of a separate binary signal elsewhere in the target light curve.',
 next='Require a fully observed isolated trough in another sector before reopening an eclipse claim.'),
'Q033':dict(v='REFUTED',p='',ep='',depth='',
 finding='The S101 4113.263 flag ends in a gap after a monotonic decline, with only 49% nominal core coverage. S102 4133.117 follows a -7.41 ppt gap step and separate segment baseline; S103 4165.057 precedes a +29.15 ppt gap step and covers only 40% nominal core. The dramatic S94 unflagged trough near 3869 also coincides with the cross-target S94 segment break, so it is not a hidden clean recurrence.',
 physics='The three selected dips do not supply measured eclipse centers or a repeat clock for the Gaia SB1 orbit.',
 limits='Other low-amplitude stellar variability may coexist with the documented gap/step artifacts.',
 next='Find an event with continuous ingress, core, egress, and two-sided baseline.'),
'Q034':dict(v='REFUTED',p='',ep='',depth='',
 finding='The S9 1557.346 window begins at a segment gap and has 50% nominal core coverage; the raw series rises monotonically from the segment start. S10 1571.492 is a smooth decline flattening into a new level, while the alternate KSPSAP reduction is nearly flat. These are not two repeated eclipse profiles. Other sectors show large raw brightening spikes and boundary behavior, confirming this target has reduction/systematics complications.',
 physics='The 14.146 d separation of two flagged windows is not a measured eclipse period or a secure half-cycle of Gaia SB1 P27.309 d.',
 limits='The diagnostics refute these selected windows as an eclipse train; they do not rule out a separate weak binary signal.',
 next='Review a fully covered event away from segment boundaries with target-centered pixels.'),
'Q035':dict(v='REFUTED',p='',ep='',depth='',
 finding='S64 3054.743 runs directly into a gap (45% nominal core); S64 3060.986 is a shallow broad sag without the same narrow morphology. The S94 3874.870 flag sits at a gap with only 30% nominal core coverage and is synchronous with the common multi-target 3874.9 feature. S96 3913.957 and S97 3966.607 are rising/declining segment baselines beside gaps rather than repeated symmetric cores. All 41 sector light curves were viewed in raw context.',
 physics='No consistent eclipse kind or source-specific period emerges from the five selected windows.',
 limits='A smaller isolated event may be hidden under the substantial sector-to-sector variability; the refutation is of the selected repeat-sector evidence.',
 next='Search for a complete event in a stable segment, then assess spatial ownership.'),
'Q036':dict(v='REFUTED',p='',ep='',depth='',
 finding='Four sharp ~10 ppt raw SAP dips occur in S18 at BTJD 1792.5226, 1798.6643, 1804.8080, and 1810.9590, each with ingress and egress visible in SAP and KSPSAP. S85 adds three similarly deep events at 3618.0014, 3624.1476, and 3630.2890; the middle one was not retained by the screening flags and was recovered in raw context. The long separation is conditional on 297, 298, and 299 cycles at ~6.1464 d, with later S85 residuals -0.0002 and -0.0052 d. Adjacent integer aliases shift the four S18 events relative to the narrow profiles. Covered P/3 predictions in S18/S85 are generally flat, while P/2 windows can have shallow structure but not matching ~10 ppt same-kind dips.',
 physics='The photometric period is grossly inconsistent with Gaia SB1 P20.14331 d; the observed S18 center is ~0.18 Gaia orbital phase from either edge-on conjunction. Fresh S18 and S85 TESSCut WCS cutouts identify Gaia DR3 358527789513614336 (G15.339, 28.90 arcsec north) as the favored dimming source. After corner-sky subtraction and per-pixel local sideband detrending, both difference maps peak at the neighbor WCS pixel (5,7). Positive deficit centroids are 0.29/0.10 pixel from the neighbor and 1.12/1.31 pixels from the queued target. Disjoint target-side and neighbor-side x4..6 stripes lose 8.43 versus 37.69 e/s in S18 and 4.00 versus 39.99 e/s in S85, despite the target-side baseline being brighter. The G flux ratio 0.0281 makes the blended loss feasible for a deep neighbor eclipse. This refutes attribution of the selected eclipse train to the queued target, while preserving a real neighboring EB lead.',
 limits='The ~6.1464 d period and ~10 ppt depth describe the off-target lead and are omitted from the queued target RESULTS fields. Target and neighbor are separated by ~1.4 TESS pixels; PRF overlap and similar S18/S85 WCS orientation limit precision localization, but both corrected maps and disjoint aperture strips favor the neighbor. One S85 event lies close to a gap, and local Gaussian timing is diagnostic; no precision period uncertainty is supplied. This does not exclude unrelated binarity of TIC 250561084.',
 next='Review Gaia DR3 358527789513614336 as a separate eclipsing object and obtain a resolved next event.'),
'Q037':dict(v='REFUTED',p='',ep='',depth='',
 finding='S94 3874.939 is exactly at a data-gap boundary with only 26% nominal core coverage; its asymmetric decline/recovery matches the simultaneous S94 feature in several other targets. S104 4185.390 is a segment onset step, followed by a slow trend rather than an eclipse-shaped return. The two flagged windows therefore do not establish recurrence.',
 physics='No measured same-kind period or Gaia conjunction association follows from the flagged structures.',
 limits='An unflagged independent eclipse elsewhere is not excluded.',
 next='Require an isolated two-sided event with a valid target-centered extraction.'),
'Q038':dict(v='REFUTED',p='',ep='',depth='',
 finding='S94 3874.807 sits at a gap endpoint with only 28% nominal core coverage and the same asymmetric common feature as Q032/Q035/Q037/Q039. S94 3867.605 is a long monotonic segment decline rather than a closed trough. S103 4159.656 begins after a large baseline step, and 4166.538 is the start of a rising segment after a gap; neither reproduces an eclipse profile. S13 shows other shallow variability, but no secure repeated dip kind.',
 physics='The four flags do not yield event-derived orbital timing for Gaia SB1 P40.662 d.',
 limits='The selected eclipse interpretation is refuted; unrelated low-level astrophysical variability is unresolved.',
 next='Use an independent continuous eclipse profile before assigning a binary period.'),
'Q039':dict(v='REFUTED',p='',ep='',depth='',
 finding='S94 3874.893 is at a gap (29% nominal core), coincident with the S94 feature in several other targets. S101 4119.117 is a small sag touching a segment break, and S102 4145.375 terminates at a gap with only 29% nominal core. The latter two do not repeat the S94 asymmetry or supply same-kind eclipse centers.',
 physics='No measured eclipse clock supports associating the selected windows with Gaia SB1 P27.688 d.',
 limits='A separate weak eclipse is not disproved; the selected detector windows are inadequate.',
 next='Obtain complete ingress/core/egress away from the observed gaps.'),
'Q040':dict(v='REFUTED',p='',ep='',depth='',
 finding='Across ten sectors the raw light curve has smooth high-amplitude waves and long monotonic slopes; the five retained dip flags at 2431.832, 3325.324, 3352.302, 3380.106, and 3564.256 sample those slopes or discontinuities. S74/S75/S76 centers are about 27–28 d apart, but their local traces are still declining at the flagged time, without an isolated core and egress. Numerous bright flags mark the same oscillatory wave and segment jumps.',
 physics='The selected windows do not demonstrate detached eclipses or a measured eclipse period. S41 SAP slope is largely suppressed by KSPSAP, so the broad modulation cannot be positively classified as astrophysical from these reductions alone.',
 limits='The mechanism of the smooth SAP modulation is unresolved; broad eclipses beneath it are not mathematically excluded. This verdict refutes the selected repeat-dip evidence only.',
 next='Check independent reductions and pixels for the broad modulation; revisit residuals if an isolated eclipse appears.'),
}

cols=['sample_id','tic','sample_stratum','physical_verdict','full_review_completion','novelty_status','period_days','period_error_days','primary_epoch_btjd','depth_ppt','limitations','next_check','report']
rows=[]
for q in csv.DictReader((B/'queue.csv').open(encoding='utf8',newline='')):
    sid=q['sample_id'];tic=q['tic'];d=DATA[sid];D=B/tic
    context=json.loads((D/'lead-context.json').read_text());flags=json.loads((D/'lead-flag-diagnostics.json').read_text())
    assert len(context['sectors'])==int(q['usable_files'])
    report=f"""# {sid} — TIC {tic}\n\n**Physical verdict:** {d['v']}. **Novelty:** UNKNOWN. **Completion:** COMPLETE.\n\n## Evidence\n\n{d['finding']}\n\n{d['physics']}\n\n## Scope and uncertainty\n\n{d['limits']} The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all {len(context['sectors'])} cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all {len(flags)} selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.\n\n## Reproduction and next check\n\nRun `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.\n\n{d['next']}\n"""
    (D/'REPORT.md').write_text(report,encoding='utf8')
    rows.append(dict(sample_id=sid,tic=tic,sample_stratum=q['sample_stratum'],physical_verdict=d['v'],full_review_completion='COMPLETE',novelty_status='UNKNOWN',period_days=d['p'],period_error_days='',primary_epoch_btjd=d['ep'],depth_ppt=d['depth'],limitations=d['limits'],next_check=d['next'],report=str((D/'REPORT.md').resolve())))
with (B/'RESULTS.csv').open('w',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
lead=dict(queued_sample_id='Q036',queued_tic='250561084',queued_gaia_dr3='358526934817572608',
          off_target_gaia_dr3='358527789513614336',off_target_ra_deg=31.72583458789421,off_target_dec_deg=50.74872579645119,
          off_target_G=15.339438,angular_separation_arcsec=28.85427,off_target_to_queued_G_flux_ratio=0.0281492,
          off_target_conditional_photometric_period_days=6.146393212206782,
          off_target_diagnostic_eclipse_centers_btjd=[1792.52262,1798.66425,1804.80804,1810.95895,3618.00141,3624.14759,3630.28896],
          spatial_evidence='Sky-corrected local difference maps in S18 and S85 peak at neighbor WCS pixel y7,x5; disjoint neighbor-side strips lose 37.69/39.99 e/s versus target-side 8.43/4.00 e/s. Similar WCS orientation and PRF overlap limit precision, but repeated spatial pattern favors neighbor.',
          evidence_files=['250561084/lead-timing.json','250561084/lead-alias-geometry.json','helper-Q036-cutout-series.json','helper-pixels.json','helper-Q036-s018-local-difference.png','helper-Q036-s085-local-difference.png'],
          novelty_status='UNKNOWN',public_claim=False)
(B/'OFF-TARGET-LEADS.json').write_text(json.dumps([lead],indent=2)+'\n',encoding='utf8')
print({r['sample_id']:r['physical_verdict'] for r in rows})
