# TIC 298796659: PROBABLE

Full bounded physical review: COMPLETE. Physical verdict and scoped catalogue novelty are separate. The epoch column names the selected repeating eclipse kind; deeper-primary rank is not assumed.

**Deciding evidence:** Six sharp repeated selected eclipses establish10.36267d. Target-centered deficit favors target, but three capable sources at16.2-21.6arcsec overlap the core within roughly onepixel. Two farther capable sources43.7/47.5arcsec are spatially distinct. Unresolved close-source ownership prevents confirmation; large variable raw baselines are kept separate from selected eclipses.

6 free-center quality-zero raw QLP SAP_FLUX timings in sectors[35, 63, 90] give P=10.3626720256 +/-0.0000312949d and selected-kind reference BTJD=2260.7394561. Median fitted diluted QLP depth=31.102ppt. Predicted windows guide the fit; they are not measured timings. Flagged/uncovered windows are not clean nulls. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Zero-degree-of-freedom reduced chi square is null, and singular center covariance is rejected. Representative raw plots and full raw phase plots were visually inspected. Within-sector consecutive same-kind counts and parity are recorded in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/alias-audit.json); half/double alternatives were checked against actual recurrence/secondary morphology. A double orbit with identical unseen labels cannot be exhaustively excluded; no exhaustive blind alias search is claimed.

Observed secondary check: No secure secondary timing is claimed; absence of a claim is not a clean null. Eccentric Gaia other conjunction is phase0.484133 +/-0.034816 descriptive linear allowance. This is evaluated at its actual phase, never assumed0.5. Weak/noisy box maxima in phase-review.json are search candidates, not detections.

Fresh TESScut S89 difference stack contains3 actually covered events. Deficit minus target=[-0.04559348445274036, -0.0041249336369126866]pixel (radial0.046); target pixel coordinate=[7.661210992027399, 7.689106870375202]; deficit=[7.615617507574659, 7.684981936738289]. Global PSF residual=0.812 is not a localization uncertainty. Actual target rounded-pixel signed deficit/baseline=14.463/525.57 electron/s. All5 capable Gaia neighbors within60arcsec are assessed below from real pixels. Required intrinsic loss is a pairwise Gaia G passband proxy; it must not be compared directly with diluted fractional pixel loss. Actual deficit and baseline are reported in common electron/s units. Colors, aperture response, PSF overlap, and unlisted faint/unresolved sources limit this screen; no calibrated centroid confidence or full PSF deblend is claimed.

|Gaia source|sep arcsec|G|required intrinsic loss proxy|signed pixel deficit e/s|pixel baseline e/s|distance to deficit px|attribution assessment|
|---|---:|---:|---:|---:|---:|---:|---|
|5410277295264120320|16.19|15.769|0.6667|8.5665|346.83|0.782|unresolved overlapping core|
|5410277295264120832|20.11|16.076|0.8745|12.21|502.28|1.001|unresolved overlapping core|
|5410277295264120448|21.62|14.817|0.2955|12.21|502.28|1.078|unresolved overlapping core|
|5410089588017992832|43.73|15.502|0.5280|-0.066141|1763.7|2.147|spatially distinct from compact target deficit; wings/noise may contribute|
|5410277363983597312|47.46|15.919|0.7608|-0.74326|9.0855|2.344|spatially distinct from compact target deficit; wings/noise may contribute|

Alternative background-subtracted fixed target-centered TESScut1x1/3x3/5x5 depths=27.519/21.555/3.541ppt. Faintest40percent per-cadence background, symmetric local pre/post windows and actual covered cores provide an alternative extraction. Retained pixel-arrays.npz contains actual deficit/baseline. This is a reused numerical primitive with fresh ephemeris/duration, not independent-code replication. QLP and custom extractions share TESS photons in overlapping sectors; differing sectors are separate observing occasions on one instrument. Aperture/sector depth differences are dilution and reduction limitations, not intrinsic depth agreement.

Gaia DR3 source5410277295264120064 has P=10.361888573d, e=0.413866, omega=273.1440deg, Tp=385.199903BTJD. Both edge-on eccentric conjunctions and source-specific full NSS covariance are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/gaia-geometry.json). Closest selected-kind offset=0.071883d (0.006937phase), linear covariance allowance=0.939139d. The SB1 lower triangle uses P,gamma,K,e,omega,Tp, and selected subindices0,3,4,5; minimum full correlation eigenvalue=0.096082. This descriptive linear approximation is not a calibrated rejection threshold. Mass function=0.0941635solar masses; assumed TIC/adopted M1=1.000, minimum M2=0.630; TIC/adopted radius=2.107solar radii. Approximate central duration=6.062h versus measured6.750h. Main-sequence minimum-mass companion and TIC mass/radius make this a plausibility screen, not a fitted geometry. Orbital agreement alone cannot establish source ownership.

|Sector|same-kind search cycle|measured midpoint BTJD|formal center error d|timing input allowance d|depth ppt|
|---|---:|---:|---:|---:|---:|
|35|0|2260.7427276|0.00391782|0.00391782|28.958|
|63|73|3017.2160093|0.00215781|0.00215781|31.861|
|63|75|3037.9361340|0.00221555|0.00221555|31.765|
|90|144|3752.9614589|0.00253884|0.00253884|31.066|
|90|145|3763.3275831|0.0020492|0.0020492|29.890|
|90|146|3773.6940954|0.0030345|0.0030345|31.138|

**Limitations and next check:** Resolved eclipse photometry to establish ownership. Representative events suffice for this bounded review; no all-sector/all-event precision campaign is claimed. Sector-dependent dilution, finite cadence, baseline choice, color proxy, and linear Gaia propagation remain material limitations.

Catalogue checks use [../../shared-catalogues/coverage-matrix.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/shared-catalogues/coverage-matrix.csv) and the shared receipt manifest; known recovery is separated from physical classification and no exhaustive priority claim is made. Evidence: measurements.json/raw-windows.csv/raw-events.png; fresh-pixels/diff_fresh.json/png/pixel-arrays.npz; [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/neighbor-assessment.json); batch phase, secondary, alias, identity/source receipts, methods snapshot and audits. SHA256SUMS.json freezes exact sources and outputs.


Stable review key: R589.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/fresh-pixels/run.log)
- [historical/diff_s89.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/historical/diff_s89.json)
- [historical/diff_s89.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/historical/diff_s89.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/measurements.json)
- [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/neighbor-assessment.json)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/298796659/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
