# TIC 165779351: CONFIRMED

Full bounded physical review: COMPLETE. Physical verdict and scoped catalogue novelty are separate. The epoch column names the selected repeating eclipse kind; deeper-primary rank is not assumed.

**Deciding evidence:** Four measured deep flat-bottomed eclipses establish same-kind recurrence. Fresh compact target deficit is distinct from all three capable neighbors at36.8-58.4arcsec. A weak recurring secondary candidate lies near0.72phase, consistent with eccentric Gaia0.7297 +/-0.0483; free-center secondary fits are not secure, so no secondary precision timing is claimed.

4 free-center quality-zero raw QLP SAP_FLUX timings in sectors[15, 75, 83] give P=11.7908244002 +/-0.0000512392d and selected-kind reference BTJD=1712.5564938. Median fitted diluted QLP depth=51.982ppt. Predicted windows guide the fit; they are not measured timings. Flagged/uncovered windows are not clean nulls. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Zero-degree-of-freedom reduced chi square is null, and singular center covariance is rejected. Representative raw plots and full raw phase plots were visually inspected. Within-sector consecutive same-kind counts and parity are recorded in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/alias-audit.json); half/double alternatives were checked against actual recurrence/secondary morphology. A double orbit with identical unseen labels cannot be exhaustively excluded; no exhaustive blind alias search is claimed.

Observed secondary check: No secure secondary timing is claimed; absence of a claim is not a clean null. Eccentric Gaia other conjunction is phase0.729723 +/-0.048314 descriptive linear allowance. This is evaluated at its actual phase, never assumed0.5. Weak/noisy box maxima in phase-review.json are search candidates, not detections.

Fresh TESScut S55 difference stack contains2 actually covered events. Deficit minus target=[-0.18050831937875778, 0.011143796944930173]pixel (radial0.181); target pixel coordinate=[7.024316492655553, 7.3960086776671545]; deficit=[6.843808173276795, 7.407152474612085]. Global PSF residual=0.413 is not a localization uncertainty. Actual target rounded-pixel signed deficit/baseline=28.893/531.88 electron/s. All3 capable Gaia neighbors within60arcsec are assessed below from real pixels. Required intrinsic loss is a pairwise Gaia G passband proxy; it must not be compared directly with diluted fractional pixel loss. Actual deficit and baseline are reported in common electron/s units. Colors, aperture response, PSF overlap, and unlisted faint/unresolved sources limit this screen; no calibrated centroid confidence or full PSF deblend is claimed.

|Gaia source|sep arcsec|G|required intrinsic loss proxy|signed pixel deficit e/s|pixel baseline e/s|distance to deficit px|attribution assessment|
|---|---:|---:|---:|---:|---:|---:|---|
|1969426952599000192|36.83|14.987|0.5786|3.6473|175|2.044|spatially distinct from compact target deficit; wings/noise may contribute|
|1969426746440569472|47.49|15.216|0.7021|0.25984|97.189|2.599|spatially distinct from compact target deficit; wings/noise may contribute|
|1969426918239256832|58.37|15.420|0.8368|0.08416|70.138|2.722|spatially distinct from compact target deficit; wings/noise may contribute|

Alternative background-subtracted fixed target-centered TESScut1x1/3x3/5x5 depths=54.323/50.265/44.087ppt. Faintest40percent per-cadence background, symmetric local pre/post windows and actual covered cores provide an alternative extraction. Retained pixel-arrays.npz contains actual deficit/baseline. This is a reused numerical primitive with fresh ephemeris/duration, not independent-code replication. QLP and custom extractions share TESS photons in overlapping sectors; differing sectors are separate observing occasions on one instrument. Aperture/sector depth differences are dilution and reduction limitations, not intrinsic depth agreement.

Gaia DR3 source1969426948296573312 has P=11.789661906d, e=0.483596, omega=43.9817deg, Tp=391.507140BTJD. Both edge-on eccentric conjunctions and source-specific full NSS covariance are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/gaia-geometry.json). Closest selected-kind offset=0.113792d (0.009652phase), linear covariance allowance=0.436573d. The SB1 lower triangle uses P,gamma,K,e,omega,Tp, and selected subindices0,3,4,5; minimum full correlation eigenvalue=0.015695. This descriptive linear approximation is not a calibrated rejection threshold. Mass function=0.0592116solar masses; assumed TIC/adopted M1=1.220, minimum M2=0.576; TIC/adopted radius=3.238solar radii. Approximate central duration=8.644h versus measured7.339h. Main-sequence minimum-mass companion and TIC mass/radius make this a plausibility screen, not a fitted geometry. Orbital agreement alone cannot establish source ownership.

|Sector|same-kind search cycle|measured midpoint BTJD|formal center error d|timing input allowance d|depth ppt|
|---|---:|---:|---:|---:|---:|
|15|0|1712.5530976|0.000854059|0.0104171|53.087|
|75|139|3351.4814696|0.000741592|0.00115739|51.949|
|83|157|3563.7152488|0.000490021|0.00115736|51.622|
|83|158|3575.5070826|0.000491709|0.00115736|52.016|

**Limitations and next check:** Optional resolved follow-up and physical binary modeling. Representative events suffice for this bounded review; no all-sector/all-event precision campaign is claimed. Sector-dependent dilution, finite cadence, baseline choice, color proxy, and linear Gaia propagation remain material limitations.

Catalogue checks use [../../shared-catalogues/coverage-matrix.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/shared-catalogues/coverage-matrix.csv) and the shared receipt manifest; known recovery is separated from physical classification and no exhaustive priority claim is made. Evidence: measurements.json/raw-windows.csv/raw-events.png; fresh-pixels/diff_fresh.json/png/pixel-arrays.npz; [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/neighbor-assessment.json); batch phase, secondary, alias, identity/source receipts, methods snapshot and audits. SHA256SUMS.json freezes exact sources and outputs.


Stable review key: R582.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/fresh-pixels/run.log)
- [historical/diff_s55.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/historical/diff_s55.json)
- [historical/diff_s55.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/historical/diff_s55.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/measurements.json)
- [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/neighbor-assessment.json)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/165779351/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
