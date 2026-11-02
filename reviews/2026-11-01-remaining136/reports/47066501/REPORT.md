# TIC 47066501: CONFIRMED

Full bounded physical review: COMPLETE. Physical verdict and scoped catalogue novelty are separate. The epoch column names the selected repeating eclipse kind; deeper-primary rank is not assumed.

**Deciding evidence:** Eighteen sharp selected eclipses across three sectors establish3.03829d. Brighter G10.68 neighbor34.7arcsec away dominates the baseline image but the compact deficit is on target, spatially displaced from that neighbor. The1x1/3x3/5x5 depth dilution progression and the26.1arcsec light-to-deficit displacement are expected for that blend; source ownership follows actual deficit morphology. No secure secondary is claimed.

18 free-center quality-zero raw QLP SAP_FLUX timings in sectors[42, 43, 70] give P=3.0382901257 +/-0.0000064772d and selected-kind reference BTJD=2450.2999227. Median fitted diluted QLP depth=22.508ppt. Predicted windows guide the fit; they are not measured timings. Flagged/uncovered windows are not clean nulls. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Zero-degree-of-freedom reduced chi square is null, and singular center covariance is rejected. Representative raw plots and full raw phase plots were visually inspected. Within-sector consecutive same-kind counts and parity are recorded in [../alias-audit.json](../../campaign/batch05/alias-audit.json); half/double alternatives were checked against actual recurrence/secondary morphology. A double orbit with identical unseen labels cannot be exhaustively excluded; no exhaustive blind alias search is claimed.

Observed secondary check: No secure secondary timing is claimed; absence of a claim is not a clean null. Eccentric Gaia other conjunction is phase0.449798 +/-0.056911 descriptive linear allowance. This is evaluated at its actual phase, never assumed0.5. Weak/noisy box maxima in phase-review.json are search candidates, not detections.

Fresh TESScut S70 difference stack contains8 actually covered events. Deficit minus target=[-0.044238690131201075, 0.020629504697470047]pixel (radial0.049); target pixel coordinate=[7.454940439580826, 7.154530424464195]; deficit=[7.410701749449625, 7.175159929161665]. Global PSF residual=0.858 is not a localization uncertainty. Actual target rounded-pixel signed deficit/baseline=7.7313/893.81 electron/s. All1 capable Gaia neighbors within60arcsec are assessed below from real pixels. Required intrinsic loss is a pairwise Gaia G passband proxy; it must not be compared directly with diluted fractional pixel loss. Actual deficit and baseline are reported in common electron/s units. Colors, aperture response, PSF overlap, and unlisted faint/unresolved sources limit this screen; no calibrated centroid confidence or full PSF deblend is claimed.

|Gaia source|sep arcsec|G|required intrinsic loss proxy|signed pixel deficit e/s|pixel baseline e/s|distance to deficit px|attribution assessment|
|---|---:|---:|---:|---:|---:|---:|---|
|2586915362805716608|34.72|10.682|0.0268|3.2814|3081.1|1.777|spatially distinct from compact target deficit; wings/noise may contribute|

Alternative background-subtracted fixed target-centered TESScut1x1/3x3/5x5 depths=8.650/4.378/2.628ppt. Faintest40percent per-cadence background, symmetric local pre/post windows and actual covered cores provide an alternative extraction. Retained pixel-arrays.npz contains actual deficit/baseline. This is a reused numerical primitive with fresh ephemeris/duration, not independent-code replication. QLP and custom extractions share TESS photons in overlapping sectors; differing sectors are separate observing occasions on one instrument. Aperture/sector depth differences are dilution and reduction limitations, not intrinsic depth agreement.

Gaia DR3 source2586915392870164224 has P=3.038142919d, e=0.081953, omega=195.6368deg, Tp=388.144755BTJD. Both edge-on eccentric conjunctions and source-specific full NSS covariance are retained in [../gaia-geometry.json](../../campaign/batch05/gaia-geometry.json). Closest selected-kind offset=0.070101d (0.023074phase), linear covariance allowance=0.293388d. The SB1 lower triangle uses P,gamma,K,e,omega,Tp, and selected subindices0,3,4,5; minimum full correlation eigenvalue=0.0031323. This descriptive linear approximation is not a calibrated rejection threshold. Mass function=0.00422369solar masses; assumed TIC/adopted M1=1.320, minimum M2=0.215; TIC/adopted radius=1.624solar radii. Approximate central duration=4.452h versus measured2.443h. Main-sequence minimum-mass companion and TIC mass/radius make this a plausibility screen, not a fitted geometry. Orbital agreement alone cannot establish source ownership.

|Sector|same-kind search cycle|measured midpoint BTJD|formal center error d|timing input allowance d|depth ppt|
|---|---:|---:|---:|---:|---:|
|42|0|2450.2899789|0.0232971|0.0232971|27.200|
|42|1|2453.3368357|0.00638327|0.00638327|31.715|
|42|4|2462.4512290|0.00642456|0.00642456|18.476|
|42|5|2465.4847177|0.00662085|0.00662085|26.696|
|43|8|2474.6079732|0.00319346|0.00347235|23.105|
|43|9|2477.6473411|0.00405423|0.00405423|21.306|
|43|10|2480.6800797|0.00184336|0.00347235|24.006|
|43|13|2489.7951346|0.00249847|0.00347235|21.636|
|43|14|2492.8435885|0.00408437|0.00408437|24.336|
|43|15|2495.8730218|0.00176639|0.00347235|26.037|
|70|250|3209.8757498|0.0014423|0.0014423|20.043|
|70|251|3212.9100979|0.00226656|0.00226656|22.406|
|70|252|3215.9486560|0.00215097|0.00215097|22.609|
|70|253|3218.9866121|0.00163928|0.00163928|22.320|
|70|254|3222.0237686|0.00238726|0.00238726|22.230|
|70|255|3225.0648092|0.00310524|0.00310524|23.172|
|70|256|3228.0981332|0.00229693|0.00229693|20.547|
|70|257|3231.1398479|0.00267587|0.00267587|21.301|

**Limitations and next check:** Optional resolved follow-up and physical binary modeling. Representative events suffice for this bounded review; no all-sector/all-event precision campaign is claimed. Sector-dependent dilution, finite cadence, baseline choice, color proxy, and linear Gaia propagation remain material limitations.

Catalogue checks use [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv) and the shared receipt manifest; known recovery is separated from physical classification and no exhaustive priority claim is made. Evidence: measurements.json/raw-windows.csv/raw-events.png; fresh-pixels/diff_fresh.json/png/pixel-arrays.npz; [neighbor-assessment.json](../../campaign/batch05/47066501/neighbor-assessment.json); batch phase, secondary, alias, identity/source receipts, methods snapshot and audits. SHA256SUMS.json freezes exact sources and outputs.

Depth correction audit (2026-11-02): realized trapezoid decrement replaces its unconstrained amplitude parameter. Original input windows, fitted centers/widths, timing selections and physical verdict are retained; capable-neighbor membership is unchanged. See [../../depth-audit/README.md](../../campaign/depth-audit/README.md).


Stable review key: R587.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch05/47066501/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch05/47066501/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch05/47066501/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](../../campaign/batch05/47066501/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](../../campaign/batch05/47066501/fresh-pixels/run.log)
- [historical/diff_s70.json](../../campaign/batch05/47066501/historical/diff_s70.json)
- [historical/diff_s70.png](../../campaign/batch05/47066501/historical/diff_s70.png)
- [historical/gaia.json](../../campaign/batch05/47066501/historical/gaia.json)
- [measurements.json](../../campaign/batch05/47066501/measurements.json)
- [neighbor-assessment.json](../../campaign/batch05/47066501/neighbor-assessment.json)
- [raw-events.png](../../campaign/batch05/47066501/raw-events.png)
- [raw-windows.csv](../../campaign/batch05/47066501/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch05/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
