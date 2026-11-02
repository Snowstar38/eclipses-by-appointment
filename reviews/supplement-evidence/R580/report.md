# TIC 153711481: CONFIRMED

Full bounded physical review: COMPLETE. Physical verdict and scoped catalogue novelty are separate. The epoch column names the selected repeating eclipse kind; deeper-primary rank is not assumed.

**Deciding evidence:** Five shallow but sharp recurring eclipses, including consecutive cycles in S31 and S98. Fresh S97 four-event deficit is centered on target (0.068pixel). Both capable neighbors, at33.4/54.0arcsec, are spatially distinct from the compact positive core; their pixels show weak target-wing/noise losses rather than distinct matching deficit peaks. A bright remote field source distorts the total light image, explaining high global PSF residual; it does not move the eclipse core. The shallow stack is noisy (target pixel deficit3.13e/s versus0.14e/s at closer capable source); this supports target attribution but no calibrated localization confidence is claimed. Raw per-point scatter is about2ppt, so coherent recurrence and multiple in-event samples, rather than any individual point, establish eclipse morphology.

5 free-center quality-zero raw QLP SAP_FLUX timings in sectors[31, 98] give P=11.6662342053 +/-0.0000164527d and selected-kind reference BTJD=2149.1561521. Median fitted diluted QLP depth=6.271ppt. Predicted windows guide the fit; they are not measured timings. Flagged/uncovered windows are not clean nulls. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Zero-degree-of-freedom reduced chi square is null, and singular center covariance is rejected. Representative raw plots and full raw phase plots were visually inspected. Within-sector consecutive same-kind counts and parity are recorded in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/alias-audit.json); half/double alternatives were checked against actual recurrence/secondary morphology. A double orbit with identical unseen labels cannot be exhaustively excluded; no exhaustive blind alias search is claimed.

Observed secondary check: No secure secondary timing is claimed; absence of a claim is not a clean null. Eccentric Gaia other conjunction is phase0.474648 +/-0.028672 descriptive linear allowance. This is evaluated at its actual phase, never assumed0.5. Weak/noisy box maxima in phase-review.json are search candidates, not detections.

Fresh TESScut S97 difference stack contains4 actually covered events. Deficit minus target=[0.03275525987827077, -0.06002281259825537]pixel (radial0.068); target pixel coordinate=[7.3102808916018756, 7.519448094808194]; deficit=[7.343036151480146, 7.4594252822099385]. Global PSF residual=0.981 is not a localization uncertainty. Actual target rounded-pixel signed deficit/baseline=3.1311/542.87 electron/s. All2 capable Gaia neighbors within60arcsec are assessed below from real pixels. Required intrinsic loss is a pairwise Gaia G passband proxy; it must not be compared directly with diluted fractional pixel loss. Actual deficit and baseline are reported in common electron/s units. Colors, aperture response, PSF overlap, and unlisted faint/unresolved sources limit this screen; no calibrated centroid confidence or full PSF deblend is claimed.

|Gaia source|sep arcsec|G|required intrinsic loss proxy|signed pixel deficit e/s|pixel baseline e/s|distance to deficit px|attribution assessment|
|---|---:|---:|---:|---:|---:|---:|---|
|4788880945834740352|33.44|17.622|0.7301|0.1427|66.088|1.711|spatially distinct from compact target deficit; wings/noise may contribute|
|4788892696865262080|53.96|16.503|0.2644|0.056773|50.341|2.683|spatially distinct from compact target deficit; wings/noise may contribute|

Alternative background-subtracted fixed target-centered TESScut1x1/3x3/5x5 depths=5.768/4.837/3.405ppt. Faintest40percent per-cadence background, symmetric local pre/post windows and actual covered cores provide an alternative extraction. Retained pixel-arrays.npz contains actual deficit/baseline. This is a reused numerical primitive with fresh ephemeris/duration, not independent-code replication. QLP and custom extractions share TESS photons in overlapping sectors; differing sectors are separate observing occasions on one instrument. Aperture/sector depth differences are dilution and reduction limitations, not intrinsic depth agreement.

Gaia DR3 source4788880941537833984 has P=11.666078802d, e=0.393535, omega=275.3435deg, Tp=387.767812BTJD. Both edge-on eccentric conjunctions and source-specific full NSS covariance are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/gaia-geometry.json). Closest selected-kind offset=-0.120223d (-0.010305phase), linear covariance allowance=0.330198d. The SB1 lower triangle uses P,gamma,K,e,omega,Tp, and selected subindices0,3,4,5; minimum full correlation eigenvalue=0.028969. This descriptive linear approximation is not a calibrated rejection threshold. Mass function=0.0623192solar masses; assumed TIC/adopted M1=1.030, minimum M2=0.534; TIC/adopted radius=1.077solar radii. Approximate central duration=3.943h versus measured1.559h. Main-sequence minimum-mass companion and TIC mass/radius make this a plausibility screen, not a fitted geometry. Orbital agreement alone cannot establish source ownership.

|Sector|same-kind search cycle|measured midpoint BTJD|formal center error d|timing input allowance d|depth ppt|
|---|---:|---:|---:|---:|---:|
|31|65|2149.1555851|0.00235452|0.00347223|6.394|
|31|66|2160.8230012|0.00288377|0.00347223|5.144|
|98|225|4015.7527976|0.00232604|0.00232604|6.849|
|98|226|4027.4194406|0.00121109|0.00121109|5.463|
|98|227|4039.0883756|0.00229222|0.00229222|6.271|

**Limitations and next check:** Optional resolved follow-up and physical binary modeling. Representative events suffice for this bounded review; no all-sector/all-event precision campaign is claimed. Sector-dependent dilution, finite cadence, baseline choice, color proxy, and linear Gaia propagation remain material limitations.

Catalogue checks use [../../shared-catalogues/coverage-matrix.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/shared-catalogues/coverage-matrix.csv) and the shared receipt manifest; known recovery is separated from physical classification and no exhaustive priority claim is made. Evidence: measurements.json/raw-windows.csv/raw-events.png; fresh-pixels/diff_fresh.json/png/pixel-arrays.npz; [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/neighbor-assessment.json); batch phase, secondary, alias, identity/source receipts, methods snapshot and audits. SHA256SUMS.json freezes exact sources and outputs.


Stable review key: R580.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/fresh-pixels/run.log)
- [historical/diff_s97.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/historical/diff_s97.json)
- [historical/diff_s97.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/historical/diff_s97.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/measurements.json)
- [neighbor-assessment.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/neighbor-assessment.json)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/153711481/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch05/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
