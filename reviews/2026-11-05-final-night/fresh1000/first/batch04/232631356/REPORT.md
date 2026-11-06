# Z032: TIC 232631356

Full review completion: COMPLETE_BOUNDED. Physical verdict: P. Association: GAIA_CONSISTENT_HOST_PROBABLE.

Three same-kind bounded shallow eclipses appear at1716.471304,3549.324643 and3592.967669BTJD, with5.1–5.4ppt depths and1.17–1.24d durations. Their free clock is43.639409777d on cycles0,42,43; changing the fitting half-window from2.5 to1.8d shifts each midpoint by<0.004d. S83 has a broad unlike trough with a boundary-limited fit and is excluded from the clock.

## Selection, completion and provenance

Exact frozen queue row; Gaia DR3 1418553760008251648, nestedG=11.909782, selectionP=43.67396245812431d. Parent fresh-band-next1000, operational first/batch04. No substitutions. This visually selected single_discrete stratum is not an unbiased occurrence or completeness denominator. Queue descriptions are historical triage and may be contradicted by raw review.

Canonical bounded criteria were read from [workspace]/Fable 5.1/made/paper/short/sec_methods.html Section2.7 and2.9, with candidate-review-delegation.txt. Completion and physical outcome are separate; completed noise-limited uncertainty is retained. Identity-audit.json checks exact Gaia identity, actual nestedG, every raw FITS TIC/sector header and SHA256. Parent bulk and appointment results preserve every saved score, trial duration, mask, nonflag and exclusion for revisiting near-threshold leads. No new selection threshold is imposed.

## Representative raw measurements

Quality-zero finite TIME, finite positive rawSAP flux. Full-sector, raw-window and selected-event panels were visually inspected by the lead. A local linear-baseline trapezoid uses ±2.5d, baseline outside±1.5d, duration bounds0.05–3d. Formal fit errors assume local point scatter and are conditional; boundary/partial/low-depth fits are excluded. Fits marked usable describe morphology and do not alone prove an eclipse.

|Sector|Kind|Center proxy BTJD|Depth ppt|Duration d|Usable fit|
|---|---|---:|---:|---:|---|
|15|broad|1716.471304|5.13|1.244|True|
|82|broad|3549.324643|5.21|1.197|True|
|83|broad|3574.776600|3.17|3.000|False|
|84|broad|3592.967669|5.38|1.169|True|

## Recurrence and coverage

Measured same-kind epoch1716.47126180BTJD and period43.639409777d; formal period error0.000288115d after0.01d/event floor. Cycles0,42,43; residuals[4.254232158018567e-05, -0.0018293198454557569, 0.0017867775227387028]. No generic primary label is assigned. The S83 trough is excluded from precise recurrence and cannot count as a fourth same-kind eclipse.

Bounded alternatives include divisors2–6, double and neighboring long-gap counts38–46. Divisors2–6 have covered nulls; double and neighboring counts other than42 fail the third-event timing. Native-point scatter and0.1d binned side scatter are retained. A clean-null rule requires>=75% core sampling, no large interior gap, both sidebands, and depth+4*binned-side-scatter <half the characteristic5.21ppt depth. This is a conservative empirical audit, not a calibrated detection probability. Missing/flagged/noisy predictions are not nulls.

|Trial|Period d|Timing compatible|Covered|Clean nulls|
|---|---:|---|---:|---:|
|measured|43.6394098|True|3|0|
|divisor2|21.8197049|True|8|4|
|divisor3|14.5464699|True|12|9|
|divisor4|10.9098524|True|14|7|
|divisor5|8.7278820|True|16|8|
|divisor6|7.2732350|True|23|16|
|long-gap-cycles38|48.2329826|False|3|1|
|long-gap-cycles39|46.9962395|False|2|0|
|long-gap-cycles40|45.8213335|False|2|0|
|long-gap-cycles41|44.7037400|False|4|0|
|long-gap-cycles42|43.6393652|True|3|0|
|long-gap-cycles43|42.6244963|False|4|1|
|long-gap-cycles44|41.6557577|False|4|2|
|long-gap-cycles45|40.7300742|False|5|2|
|long-gap-cycles46|39.8446378|False|5|1|
|double|87.2788196|False|2|0|
|Gaia|43.6739625|False|4|3|

Successful current TESScut availability check2026-11-06T04:58:37.553645+00:00: sectors[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 40, 41, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]. Original QLP available inventory[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 40, 41, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]. Reviewed cached sectors[14, 15, 81, 82, 83, 84, 85, 86]. Availability does not prove usable event coverage; this is bounded representative review, not exhaustive all-sector fitting.

## Reduction and source attribution

lead-reduction-comparison.json preserves SAP and KSPSAP core/side depths where available. KSPSAP can remove a day-long event; for TIC232631356 S15 it retains only0.038ppt versus5.13ppt rawSAP, a material reduction difference resolved through helper custom aperture evidence rather than treated as independent confirmation. Independent extractions reuse the same photons; different sectors are separate observing occasions. HELPER-AUDIT.md and per-target helper artifacts retain actual custom-aperture, deficit, neighbor and newer-sector results and failures. No unavailable check is treated as a success.

## Source-specific Gaia geometry

P=43.673962458 +/-0.027789872d, e=0.192433, omega=45.55593deg, Tp=403.781815BTJD; mass function=0.0330619solar masses. lead-gaia-covariance.json propagates the source SB1 P,e,omega,Tp submatrix (Gaia lower-triangle parametersP,gamma,K,e,omega,Tp). lead-nonlinear-gaia.json adds100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Unusable shape proxies are excluded from nonlinear inference. Edge-on conjunctions are assumptions, not measured inclination. Broad consistency does not establish ownership.

S84 helper7x7 raw-pixel difference image peaks atpixel(4,3), near targetWCS(3.555,3.225), with approximately6.8 electrons/s compact excess above the diffuse background. Successful MAST TIC90arcsec cone retains capable neighbors TIC232631357,T=16.1514 at(2.22,2.70),29.46arcsec and TIC232631352,T=15.9363 at(3.51,1.76),30.50arcsec, versus targetT=11.2916. Their locations differ from the compact deficit; peak proximity supports the target vicinity but is not a calibrated PRF/centroid separation. Their possible eclipse amplitudes are not excluded by comparing intrinsic neighbor losses with blended aperture fractions. The residual uncertainty motivates probable rather than confirmed.

TIC232631356: measured period differs fromGaia by0.03455d, about1.24Gaia sigma; three selected same-kind events are approximately1.27sigma early in the local covariance calculation. Duration/period˜0.0274, giving a circular central proxy(R1+R2)/a˜0.086; this is a scale check, not a measured radius/inclination or full orbit fit.

## Catalogue status

Root-owned sealed first/shared-catalogues covers VSX/ASAS-SN successful cones, source-specific SIMBAD/Gaia EB/variability/NSS, vetted Prsa/IJspeert/Kostov tables, bounded Kepler/K2/TOI and identity/literature checks. Target-specific rows and any neighbors remain in those receipts. A scoped no-target-prior-EB result is distinct from physical classification and does not establish exhaustive priority. Failed queries remain unknown. SOURCE-MANIFEST.json snapshots the catalogue seal and sources.

## Limitations and next check

S84 custom pixels recover a compact deficit near the target, supporting a probable target eclipse. Two capable faint neighbors about1.3-1.5pixels away remain an uncalibrated attribution limitation; no quantitative PRF/centroid significance is established. The0.000288d period error is formal conditional on the0.01d/event floor and adopted cycles, not calibrated long-term accuracy.

Obtain another resolved eclipse and improve spatial/spectroscopic characterization.

## Evidence and contributors

Target lead-context.json, lead-series.json, lead-timing.json, raw/context/full-sector panels and helper artifacts; batch identity audit, source hashes, reduction comparison, covariance/nonlinear covariance, conditional coverage, clocks/aliases, LEAD-AUDIT.md, HELPER-AUDIT.md and SOURCE-MANIFEST.json. Lead reviewed every frozen row; helper independently audited deciding morphology, sources and availability. No ledger or public file edits.
