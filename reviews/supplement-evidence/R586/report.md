# TIC 152876230: CONFIRMED

Full bounded physical review: COMPLETE. Physical verdict and scoped catalogue novelty are separate. The epoch column names the selected repeating eclipse kind; deeper-primary rank is not assumed.

**Deciding evidence:** Four deep selected-kind events in S68/S95 and three measured secondaries near0.71238phase support eccentric12.21853d orbit and reject a half-period interpretation. Fresh target-centered deficit has no capable Gaia neighbor within60arcsec. S1 lacks an accepted selected-center fit but has secondary coverage, not a clean null. Selected depths347ppt in S68 versus300ppt S95 show sector dilution changes; reported median is a pipeline-dependent quantity.

4 free-center quality-zero raw QLP SAP_FLUX timings in sectors[68, 95] give P=12.2185346745 +/-0.0000192876d and selected-kind reference BTJD=3156.9500050. Median fitted diluted QLP depth=324.118ppt. Predicted windows guide the fit; they are not measured timings. Flagged/uncovered windows are not clean nulls. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Zero-degree-of-freedom reduced chi square is null, and singular center covariance is rejected. Representative raw plots and full raw phase plots were visually inspected. Within-sector consecutive same-kind counts and parity are recorded in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/alias-audit.json); half/double alternatives were checked against actual recurrence/secondary morphology. A double orbit with identical unseen labels cannot be exhaustively excluded; no exhaustive blind alias search is claimed.

Observed secondary check: 3 accepted secondary-candidate free-center fits, median actual phase0.7123817. Eccentric Gaia other conjunction is phase0.683747 +/-0.017816 descriptive linear allowance. This is evaluated at its actual phase, never assumed0.5. Weak/noisy box maxima in phase-review.json are search candidates, not detections.

Fresh TESScut S28 difference stack contains1 actually covered events. Deficit minus target=[-0.021333781357664172, 0.15011624243996202]pixel (radial0.152); target pixel coordinate=[7.872770821080806, 7.3841402672423655]; deficit=[7.851437039723142, 7.5342565096823275]. Global PSF residual=0.367 is not a localization uncertainty. Actual target rounded-pixel signed deficit/baseline=155.17/539.52 electron/s. All0 capable Gaia neighbors within60arcsec are assessed below from real pixels. Required intrinsic loss is a pairwise Gaia G passband proxy; it must not be compared directly with diluted fractional pixel loss. Actual deficit and baseline are reported in common electron/s units. Colors, aperture response, PSF overlap, and unlisted faint/unresolved sources limit this screen; no calibrated centroid confidence or full PSF deblend is claimed.

|Gaia source|sep arcsec|G|required intrinsic loss proxy|signed pixel deficit e/s|pixel baseline e/s|distance to deficit px|attribution assessment|
|---|---:|---:|---:|---:|---:|---:|---|
|None capable within60arcsec||||||||

Alternative background-subtracted fixed target-centered TESScut1x1/3x3/5x5 depths=287.599/294.633/293.055ppt. Faintest40percent per-cadence background, symmetric local pre/post windows and actual covered cores provide an alternative extraction. Retained pixel-arrays.npz contains actual deficit/baseline. This is a reused numerical primitive with fresh ephemeris/duration, not independent-code replication. QLP and custom extractions share TESS photons in overlapping sectors; differing sectors are separate observing occasions on one instrument. Aperture/sector depth differences are dilution and reduction limitations, not intrinsic depth agreement.

Gaia DR3 source6593293356532115712 has P=12.217595220d, e=0.305264, omega=17.1561deg, Tp=394.254310BTJD. Both edge-on eccentric conjunctions and source-specific full NSS covariance are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/gaia-geometry.json). Closest selected-kind offset=0.094190d (0.007709phase), linear covariance allowance=0.445736d. The SB1 lower triangle uses P,gamma,K,e,omega,Tp, and selected subindices0,3,4,5; minimum full correlation eigenvalue=0.023911. This descriptive linear approximation is not a calibrated rejection threshold. Mass function=0.0497709solar masses; assumed TIC/adopted M1=0.750, minimum M2=0.405; TIC/adopted radius=0.908solar radii. Approximate central duration=4.849h versus measured3.308h. Main-sequence minimum-mass companion and TIC mass/radius make this a plausibility screen, not a fitted geometry. Orbital agreement alone cannot establish source ownership.

|Sector|same-kind search cycle|measured midpoint BTJD|formal center error d|timing input allowance d|depth ppt|
|---|---:|---:|---:|---:|---:|
|68|149|3156.9499806|5.55939e-05|0.00115742|347.109|
|68|150|3169.1685645|6.10773e-05|0.00115742|347.685|
|95|209|3890.0620792|4.70031e-05|0.00115742|299.412|
|95|210|3902.2806258|5.79582e-05|0.00115742|301.127|

**Limitations and next check:** Optional resolved follow-up and physical binary modeling. Representative events suffice for this bounded review; no all-sector/all-event precision campaign is claimed. Sector-dependent dilution, finite cadence, baseline choice, color proxy, and linear Gaia propagation remain material limitations.

Catalogue checks use [../../shared-catalogues/coverage-matrix.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/shared-catalogues/coverage-matrix.csv) and the shared receipt manifest; known recovery is separated from physical classification and no exhaustive priority claim is made. Evidence: measurements.json/raw-windows.csv/raw-events.png; fresh-pixels/diff_fresh.json/png/pixel-arrays.npz; [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/neighbor-assessment.json); batch phase, secondary, alias, identity/source receipts, methods snapshot and audits. SHA256SUMS.json freezes exact sources and outputs.


Stable review key: R586.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/fresh-pixels/run.log)
- [historical/diff_s28.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/historical/diff_s28.json)
- [historical/diff_s28.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/historical/diff_s28.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/measurements.json)
- [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/neighbor-assessment.json)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/152876230/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
