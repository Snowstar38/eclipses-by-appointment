# TIC 400671856: PROBABLE

Full bounded physical review: COMPLETE. Physical verdict and scoped catalogue novelty are separate. The epoch column names the selected repeating eclipse kind; deeper-primary rank is not assumed.

**Deciding evidence:** Five sharp repeated selected eclipses establish10.56733d. Target-centered deficit favors target, but two capable sources at10.24/11.31arcsec overlap its PSF within0.54pixel, so ownership cannot be uniquely established. Two additional capable sources at50.7/60.0arcsec are distinct from the compact core. No secure secondary is claimed.

5 free-center quality-zero raw QLP SAP_FLUX timings in sectors[18, 58, 86] give P=10.5673332477 +/-0.0000275715d and selected-kind reference BTJD=1799.3845652. Median fitted diluted QLP depth=16.189ppt. Predicted windows guide the fit; they are not measured timings. Flagged/uncovered windows are not clean nulls. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Zero-degree-of-freedom reduced chi square is null, and singular center covariance is rejected. Representative raw plots and full raw phase plots were visually inspected. Within-sector consecutive same-kind counts and parity are recorded in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/alias-audit.json); half/double alternatives were checked against actual recurrence/secondary morphology. A double orbit with identical unseen labels cannot be exhaustively excluded; no exhaustive blind alias search is claimed.

Observed secondary check: No secure secondary timing is claimed; absence of a claim is not a clean null. Eccentric Gaia other conjunction is phase0.499782 +/-0.009856 descriptive linear allowance. This is evaluated at its actual phase, never assumed0.5. Weak/noisy box maxima in phase-review.json are search candidates, not detections.

Fresh TESScut S58 difference stack contains3 actually covered events. Deficit minus target=[-0.07521918222497614, 0.0561249431541615]pixel (radial0.094); target pixel coordinate=[7.751384817213834, 7.333134434599639]; deficit=[7.676165634988858, 7.389259377753801]. Global PSF residual=0.906 is not a localization uncertainty. Actual target rounded-pixel signed deficit/baseline=11.112/769.02 electron/s. All4 capable Gaia neighbors within60arcsec are assessed below from real pixels. Required intrinsic loss is a pairwise Gaia G passband proxy; it must not be compared directly with diluted fractional pixel loss. Actual deficit and baseline are reported in common electron/s units. Colors, aperture response, PSF overlap, and unlisted faint/unresolved sources limit this screen; no calibrated centroid confidence or full PSF deblend is claimed.

|Gaia source|sep arcsec|G|required intrinsic loss proxy|signed pixel deficit e/s|pixel baseline e/s|distance to deficit px|attribution assessment|
|---|---:|---:|---:|---:|---:|---:|---|
|518555045441696512|10.24|16.102|0.4723|11.112|769.02|0.584|unresolved overlapping core|
|518555045448010112|11.31|15.445|0.2654|11.112|769.02|0.634|unresolved overlapping core|
|518555079807739392|50.70|15.976|0.4225|0.2832|66.347|2.494|spatially distinct from compact target deficit; wings/noise may contribute|
|518554255174025600|59.96|15.015|0.1838|0.064543|216.67|2.784|spatially distinct from compact target deficit; wings/noise may contribute|

Alternative background-subtracted fixed target-centered TESScut1x1/3x3/5x5 depths=14.450/15.326/12.839ppt. Faintest40percent per-cadence background, symmetric local pre/post windows and actual covered cores provide an alternative extraction. Retained pixel-arrays.npz contains actual deficit/baseline. This is a reused numerical primitive with fresh ephemeris/duration, not independent-code replication. QLP and custom extractions share TESS photons in overlapping sectors; differing sectors are separate observing occasions on one instrument. Aperture/sector depth differences are dilution and reduction limitations, not intrinsic depth agreement.

Gaia DR3 source518554976728533760 has P=10.569061492d, e=0.158698, omega=270.1220deg, Tp=393.850304BTJD. Both edge-on eccentric conjunctions and source-specific full NSS covariance are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/gaia-geometry.json). Closest selected-kind offset=-0.148350d (-0.014036phase), linear covariance allowance=0.126004d. The SB1 lower triangle uses P,gamma,K,e,omega,Tp, and selected subindices0,3,4,5; minimum full correlation eigenvalue=0.010093. This descriptive linear approximation is not a calibrated rejection threshold. Mass function=0.12066solar masses; assumed TIC/adopted M1=1.000, minimum M2=0.705; TIC/adopted radius=2.122solar radii. Approximate central duration=8.177h versus measured3.453h. Main-sequence minimum-mass companion and TIC mass/radius make this a plausibility screen, not a fitted geometry. Orbital agreement alone cannot establish source ownership.

|Sector|same-kind search cycle|measured midpoint BTJD|formal center error d|timing input allowance d|depth ppt|
|---|---:|---:|---:|---:|---:|
|18|0|1799.3850205|0.00206159|0.0104167|14.376|
|58|103|2887.8185848|0.0015294|0.0015294|16.937|
|58|104|2898.3858255|0.00154563|0.00154563|16.140|
|58|105|2908.9561447|0.00117193|0.00117193|16.644|
|86|175|3648.6678285|0.00174748|0.00174748|16.189|

**Limitations and next check:** Resolved eclipse photometry to establish ownership. Representative events suffice for this bounded review; no all-sector/all-event precision campaign is claimed. Sector-dependent dilution, finite cadence, baseline choice, color proxy, and linear Gaia propagation remain material limitations.

Catalogue checks use [../../shared-catalogues/coverage-matrix.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/shared-catalogues/coverage-matrix.csv) and the shared receipt manifest; known recovery is separated from physical classification and no exhaustive priority claim is made. Evidence: measurements.json/raw-windows.csv/raw-events.png; fresh-pixels/diff_fresh.json/png/pixel-arrays.npz; [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/neighbor-assessment.json); batch phase, secondary, alias, identity/source receipts, methods snapshot and audits. SHA256SUMS.json freezes exact sources and outputs.


Stable review key: R585.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/fresh-pixels/run.log)
- [historical/diff_s58.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/historical/diff_s58.json)
- [historical/diff_s58.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/historical/diff_s58.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/measurements.json)
- [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/neighbor-assessment.json)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/400671856/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
