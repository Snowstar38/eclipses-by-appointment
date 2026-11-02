# TIC 290749976: PLAUSIBLE

Full bounded physical review: COMPLETE. Physical verdict is separate from catalogue novelty. The epoch is a fitted variability-dip reference, not a validated eclipse ephemeris.

**Deciding evidence and limitation:** Shallow recurring broad dips have variable baselines and a noisy offset deficit (0.62pixel). Three capable neighbors lie36-49arcsec away. Smooth morphology and variable fitted duration versus approximate central4.85h do not establish eclipse geometry; rotational, tidal or baseline modulation remains possible. No convincing sharp eclipse component is established, so this is PLAUSIBLE, not a demonstrated repeating eclipser. TIC radius2.113 solar radii is already used; broad shape/baseline and attribution remain unresolved. Period describes dip recurrence; trapezoid centers are model-dependent.

Raw QLP SAP_FLUX representative windows contain 13 accepted free-center measurements in sectors [1, 34, 97]. Predicted windows are search guides, not timings. Quality-zero points enter fits; flagged or uncovered windows are not clean nulls. Rejected fits remain visible in numerical artifacts. Raw event plots and full recurrence phase plots were inspected; fitted dips alone do not establish eclipse morphology (TIC290749976 remains plausible).

Measured variability-dip recurrence P=4.3790689451 +/- 0.0000392056 days; variability-dip reference BTJD=1331.6582646; fitted median depth=2.383ppt. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Singular/unidentifiable timing covariance is excluded. Within-sector cycle counts/parity are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/alias-audit.json). Full-phase inspection tests secondary structure at its observed phase, without imposing phase0.5; unequal secondaries do not halve same-kind periods. Half/double ambiguity is described explicitly above where material. No exhaustive alias search is claimed. Sparse349452680 additionally has current availability and bounded sampled-null receipts.

Fresh TESScut sector97 stacks 11 actual covered events. Deficit-target offset=0.627pixel, target pixel=[7.169999815834171, 7.179607561524339], deficit centroid=[7.533701991063821, 7.690829547989072]. The image-model residual=0.958 is not a calibrated location error. Actual target pixel deficit=0.50129 electron/s and baseline=621.52 electron/s. All flux-capable Gaia neighbors within60arcsec are below; their actual signed deficit and baseline are evaluated in common electron/s units at each source's rounded pixel. Overlapping PSFs prevent deblended ownership. Intrinsic required eclipse fraction uses pairwise Gaia G brightness; it is not directly comparable with diluted fractional pixel loss. Color, aperture response and unlisted faint/unresolved sources limit this approximate screen.

| Gaia source | separation arcsec | G | intrinsic required loss proxy | actual signed pixel deficit e/s | pixel baseline e/s |
|---|---:|---:|---:|---:|---:|
| 4769034211197334912 | 36.22 | 13.012 | 0.0065 | -0.047586 | 477.99 |
| 4769034211197335040 | 43.00 | 14.900 | 0.0258 | 0.63077 | 226.3 |
| 4769034206900744064 | 48.76 | 18.008 | 0.4120 | 0.63077 | 226.3 |

Alternative background-subtracted target-centered TESScut1x1/3x3/5x5 depths=0.807/1.477/1.291ppt. These custom extractions test reduction robustness. All QLP and cutouts use TESS photons; same-sector extractions are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth changes can be dilution/aperture/background effects; these numbers are not intrinsic eclipse depths. Pixel-arrays.npz preserves actual stacked images.

Gaia DR3 source=4769034314276549632, P=4.378737543d, e=0.26791. Closest edge-on conjunction offset=0.01461d (0.00334phase); source-specific full covariance linear timing allowance=0.12464d. This descriptive linear allowance is not a calibrated significance veto. Geometry code retains both eccentric conjunctions. Mass function=0.022273 solar masses; TIC/adopted primary mass=1.490, minimum secondary mass=0.435, TIC radius=2.113 solar radii. Approximate central duration=4.850h versus measured median=10.845h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility screen, not a fitted binary model. Orbit agreement alone does not establish target ownership.

| Sector | Search cycle | midpoint BTJD | formal center error d | timing input error d | depth ppt | status |
|---|---:|---:|---:|---:|---:|---|
|1|0|1327.2900745|9.483e+05|9.483e+05|1.531|rejected: Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris.|
|1|1|1331.6545971|0.0073051|0.010417|3.312|used|
|1|2|1335.9809144|0.041468|0.041468|1.457|used|
|1|4|1344.8274905|4.5622e+05|4.5622e+05|1.077|rejected: Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris.|
|34|207|2233.7636333|0.01971|0.01971|2.007|used|
|34|208|2238.1042212|0.025499|0.025499|2.746|used|
|34|210|2246.8722219|0.02951|0.02951|2.383|used|
|34|211|2251.2772694|0.011554|0.011554|1.742|used|
|97|597|3941.4618385|0.027857|0.027857|3.520|used|
|97|598|3945.9380403|0.0092929|0.0092929|1.899|used|
|97|600|3954.7704792|0.023275|0.023275|2.430|used|
|97|601|3959.1374038|0.014618|0.014618|2.046|used|
|97|603|3967.9584083|0.035959|0.035959|1.141|used|
|97|604|3972.2320568|0.017947|0.017947|2.999|used|
|97|607|3985.3957278|0.018042|0.018042|2.407|used|

**Next check:** Establish sharp eclipse morphology against rotational/tidal/baseline modulation, then resolve source ownership with eclipse photometry.

Seven-group catalogue receipts are in [../../shared-catalogues/coverage-matrix.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/shared-catalogues/coverage-matrix.csv); known recovery and physical outcome are separate. No exhaustive priority claim. Evidence: [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/measurements.json), [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/raw-windows.csv), [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/raw-events.png), [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/fresh-pixels/diff_fresh.json)/png and pixel-arrays.npz; batch identity/hash receipts, geometry, phase and alias artifacts, helper audit. Source hashes and SHA256SUMS.json cover retained sources and outputs. Methods are preserved in a read snapshot rather than mutable manuscript hashes.

Depth correction audit (2026-11-02): realized trapezoid decrement replaces its unconstrained amplitude parameter. Original input windows, fitted centers/widths, timing selections and physical verdict are retained; capable-neighbor membership is unchanged. See [../../depth-audit/README.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).


Stable review key: R565.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/fresh-pixels/run.log)
- [historical/diff_s97.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/historical/diff_s97.json)
- [historical/diff_s97.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/historical/diff_s97.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/measurements.json)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/290749976/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch03/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
