import csv,json,hashlib
from pathlib import Path
b=Path(__file__).resolve().parent;q=list(csv.DictReader((b/'queue.csv').open()));cl=json.load(open(b/'lead-clocks.json'));geo=json.load(open(b/'lead-gaia-covariance.json'));cat={r['tic']:r for r in json.load(open(b.parent/'shared-catalogues/target-results.json'))};local={r['tic']:r for r in json.load(open(b.parent/'shared-catalogues/local-table-matches-60arcsec.json'))}
dec={
'39053050':('UNRESOLVED','no-credible-eclipse-source','not-established','Only S51 has usable cached QLP. Whole-sector raw SAP shows sparse roughly5ppt scatter and a long central gap; the selected compact feature is not securely distinguished from noise. No high-confidence eclipse morphology or clock is established. This is a completed noise-limited review, not an unperformed check or a physical proof of non-eclipsing behavior.','Higher precision or another discrete event is needed; no target addition is warranted.'),
'48099288':('CONFIRMED','target-supported','consistent-within-covariance','A narrow S6 raw eclipse repeats in newly retrieved S107 and S108 at BTJD 4275.577562 and 4313.440381. Local custom pixel extraction recovers the same-kind approximately 9 ppt, 0.13 d events, separate from broad S107 spacecraft bowls. Three times give 37.859888d with cycles 0/74/75. Adjacent later events reject all tested longer integer aliases by timing; divisors 2-6 fail covered predictions. All three events lie within the full nonlinear covariance of conjunction A. Independent per-pixel local detrending and Gaussian-plus-plane difference fits in two detector orientations support target ownership: S107 center (2.052,2.274) vs target (2.226,2.258), S108 center (2.570,2.685) vs target (2.535,2.596). All 200 independent core/side frame bootstrap positions in each sector are closer to target than either capable G14.61/G14.72 neighbor. The bootstrap is a bounded model check, not calibrated astrometry or exclusion of unresolved companions.','Another complete event can refine timing and source association; the representative formal period error does not include all systematic timing errors.'),
'179293951':('PLAUSIBLE','target-supported','unresolved-clock','The bounded deep S11 eclipse has resolved ingress, flat bottom and recovery, centered on the target in a fresh pixel extraction. S38 has a shallower partial dip emerging from a gap, without a valid midpoint or demonstrated same-kind recurrence. Its fitted midpoint is explicitly unusable despite a numerically finite covariance. Fresh S65/S102 cutouts contain no stellar PSF and near-zero flux, so they are unavailable evidence, not clean nulls. No period is assigned.','Another complete same-kind event is required; obtain usable later-sector stellar photometry and test integer cycles.'),
'309259409':('REFUTED','off-target-signal','not-associated','The S45 compact depression is real in the blended QLP aperture but comes from a northern neighbor. The deficit peaks at pixel(2,6), aligned with Gaia3454968832182263168,G14.16355 at(1.882,5.863); the selected target lies near(3.1,3.6). Target-peak pixel(3,4) has loss-0.000584, while northern pixels(2,6)/(2,5) show3.23%/1.77% losses. Thus the target eclipse interpretation is refuted. A possible single eclipse on the neighbor remains separate from the target and the selected Gaia orbit.','A wider extraction or follow-up can classify the northern variable; do not count the selected target.'),
'338482866':('REFUTED','smooth-variable-selected-feature','not-established','Whole-sector S53 raw SAP shows two broad smooth troughs separated by about13d, with multi-day changing slopes rather than a compact bounded eclipse. S54/S80 show scatter and instrumental baseline changes. This refutes the selected compact-eclipse interpretation; the broad variability is not assigned a physical class. The missing S40 was not pursued because no credible discrete event motivated another-sector search.','A new genuinely discrete event could reopen eclipse review; broad variability alone does not justify a target eclipse claim.'),
'365657271':('CONFIRMED','target-supported','consistent-within-covariance','Three resolved flat-bottom raw events in S13/S93/S104 give41.659387d with cycles0/52/60. The partial S39 terminal event is qualitatively consistent but excluded from midpoint fitting. Target-centered S93 difference image and custom3x3 extraction confirm eclipse morphology. Divisors2–6 have covered nulls; photometry retains83.31883,55.54589 and27.77294d alternatives. Source-specific Gaia41.648936d orbit and full nonlinear conjunction covariance uniquely select the41.659387d clock among tested aliases. The joint Gaia-assisted cycle choice is stated explicitly; photometry alone is not unique.','An eclipse outside the common4-cycle spacing would remove purely photometric integer ambiguity; additional sectors can refine representative timing.')}
rows=[]
for r in q:
 t=r['tic'];tier,src,ga,reason,nxt=dec[t];d=json.load(open(b/t/'lead-context.json'));ti=json.load(open(b/t/'lead-timing.json'));pix=json.load(open(b/t/'helper-localization.json')) if (b/t/'helper-localization.json').exists() else {};c=cl.get(t);period=c['period_d'] if c and tier=='CONFIRMED' else '';perr=c['formal_period_error_d'] if period else ''
 receipt=dict(seven_source_scope='VSX,SIMBAD primary,GaiaDR3 EB,Prsa,IJspeert,Kostov vetted3/4,ASAS-SN',target_receipt=cat[t],local_tables=local[t],shared_root_seal='../shared-catalogues/ROOT-CATALOGUE-SEAL.json',novelty_adjudication='No prior target EB found in scoped shared checks; this is not exhaustive priority proof.')
 (b/t/'lead-central-catalogue-receipts.json').write_text(json.dumps(receipt,indent=2))
 row=dict(sample_id=r['sample_id'],tic=t,gaia_dr3=r['gaia_dr3'],completion='complete',tier=tier,period_d=period,period_error_d=perr,source_association=src,gaia_association=ga,catalogue_status='scoped-no-target-prior-EB',publication_eligible=str(tier in ['CONFIRMED','PROBABLE']).lower(),report=f'{t}/REPORT.md',limitation=nxt);rows.append(row)
 ev='\n'.join(f"|{e['sector']}|{e.get('center_btjd','')}|{e.get('center_formal_error_d','')}|{e.get('depth_ppt','')}|{e.get('duration_d','')}|{e.get('fit_usable',False)}|" for e in ti)
 text=f"""# {r['sample_id']} — TIC {t}

Review complete. Physical tier: **{tier}**. Gaia DR3 {r['gaia_dr3']}; selection P={r['gaia_period']}d,G={r['gaia_G']}.

{reason}

## Representative raw measurements

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|usable midpoint|
|---|---|---|---|---|---|
{ev}

Reported period={period or 'unresolved'}d; local formal error={perr or 'not assigned'}d. Clock and cycle choices are in lead-clocks.json. Timing uncertainties are local formal fit errors; clock fits use cadence/2 or .004d floor for E034. They do not incorporate all systematics. Gap-cut midpoints are excluded explicitly. E029 has three events including adjacent S107/S108 eclipses; tested photometric timing alternatives do not survive. E034 representative residuals reach.0086d.

## Method and source attribution

Quality-zero finite positive raw SAP is primary evidence; all cached sector contexts and representative discrete events were inspected. KSPSAP and custom TESScut apertures reuse the same photons. Missing/gap-cut or flagged windows are not clean nulls. Aliases test divisors2–6 and endpoint integer alternatives over approximately5–100d; lead-alias-summary.json and lead-alias-covered-windows.json preserve each compatible alternative and covered raw evidence. Geometry uses this source's SB1 full covariance with edge-on conjunction assumptions, both conjunction kinds and a fixed integer cycle. Nonlinear draws unwrap base conjunction about nominal before propagating the fixed cycle; seed50701 and100000draws. Geometry is an association check, not an inclination measurement or exact physical model.

Pixel result: {json.dumps({k:pix.get(k) for k in ['status','target_xy','positive_diff_centroid_xy','centroid_offset_pixels','aperture_loss']})}. Pixels and Gaia-neighbor geometry are considered together. E032's target aperture alone is contaminated and does not establish ownership. E029 S107/S108 source and event shapes pass a separate helper audit, with two-orientation Gaussian image bootstrap retained. E028/E033 have no credible discrete eclipse to localize; omitting pixel extraction does not manufacture a negative source test.

## Current availability and catalogue scope

lead-current-sector-inventory.json records successful current MAST sector responses. Bounded extras: E029S87/107/108/109 and E031S65/102 are preserved in lead-extra-sector-receipts.json and per-sector FITS/NPZ/plots. E029S87 and E031S65/S102 have near-zero flux/no target PSF and are unusable. E029 S107 contains broad spacecraft-like bowls that are excluded, plus a separate narrow eclipse at BTJD 4275.578; S108 has another narrow eclipse on a sloping baseline.

Scoped shared checks find no prior target eclipsing identification in the seven required sources; per-target receipt and shared seal are retained. No negative claim is made from a failed request. Literature checks and scoped catalogue nonmatches do not establish exhaustive priority.

## Limitation and next check

{nxt}

Physical tier, Gaia association, source ownership and novelty are recorded separately. Completion means the bounded deciding review is performed, not that every selected lead is a detection. Exact6 reviewed without substitution; previously published E030 excluded upstream. No ledger or publication edit. Evidence/scripts and helper final audit are sealed at batch level.
"""
 (b/t/'REPORT.md').write_text(text,encoding='utf8')
with (b/'RESULTS.csv').open('w',newline='',encoding='utf8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print([(x['sample_id'],x['tier']) for x in rows])

