# TIC 165793290: CONFIRMED

Full bounded physical review: **COMPLETE**. Sixteen deep V-shaped repeated eclipses plus unequal secondary near0.49975. No capable Gaia neighbor within60arcsec; compact deficit is on target. Gaia conjunction offset0.0644d exceeds the linear0.0196d propagation; its phase0.0267 offset is explicitly retained rather than treated as a Gaussian rejection.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/phase-review.png), including P and2P parity views. 16 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=2.41024796316 +/- 0.00000370217 d; reference BTJD=1716.29832455. Epoch kind: Deeper primary eclipse, established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.12877466262314283; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/half-period-coverage.json). For138080650, orbital cycles are half the even historical SAP cycles; excluded odd-cycle secondaries remain in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; TIC138854818 instead has sampled opposite-phase coverage without a comparable11ppt primary; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Narrow shallower secondary visible in raw pooled windows. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.4997470, formal phase covariance error=2.5813e-05; depth=97.765 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Gaia conjunction search guide, adjusted from raw phase morphology for435209690 and58825156. Final phase is a free-center fit to observed raw flux..

Fresh difference image: sector49, 10 complete core/sideband events. Target pixel=[7.490314781863615, 7.03628368763723]; deficit centroid=[7.52809403705176, 7.015776526008011]; deficit-target distance=0.0430 pixel. Deficit-light offset=2.399 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.1413 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Sixteen deep V-shaped repeated eclipses plus unequal secondary near0.49975. No capable Gaia neighbor within60arcsec; compact deficit is on target. Gaia conjunction offset0.0644d exceeds the linear0.0196d propagation; its phase0.0267 offset is explicitly retained rather than treated as a Gaussian rejection.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| None | | | | | |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 271.231/264.840/263.933 ppt versus fitted raw QLP median345.935 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source1603058197763982976: P=2.41018569 +/-0.00003382 d, e=0.020577, omega=293.54421 degrees, periastron BTJD=389.5907569. Closest edge-on conjunction offset=0.064371 d (0.026708 phase), source-specific full-covariance linear uncertainty=0.019609 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/gaia-geometry.json). Mass function=0.0614391 solar masses, assumed M1=0.642, minimum M2=0.40751; approximate central duration=3.247 h versus observed2.117 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 15 | 1 | 1716.28481936 | 1.2994336e-05 | 0.010416386 | 326.658 |
| 49 | 384 | 2639.42349198 | 4.0342443e-05 | 0.0034722583 | 354.398 |
| 49 | 385 | 2641.83398946 | 5.9956282e-05 | 0.0034722583 | 351.614 |
| 49 | 386 | 2644.24415560 | 4.1698749e-05 | 0.0034722583 | 352.045 |
| 49 | 387 | 2646.65435683 | 4.8072475e-05 | 0.0034722583 | 352.256 |
| 49 | 388 | 2649.06470313 | 2.4148114e-05 | 0.0034722583 | 350.310 |
| 49 | 391 | 2656.29548137 | 3.6395356e-05 | 0.0034722583 | 351.990 |
| 49 | 392 | 2658.70564485 | 3.2303797e-05 | 0.0034722583 | 349.856 |
| 49 | 393 | 2661.11595156 | 5.4806834e-05 | 0.0034722583 | 345.629 |
| 49 | 394 | 2663.52606188 | 3.2295967e-05 | 0.0034722583 | 346.242 |
| 78 | 714 | 3434.80518341 | 4.7033273e-05 | 0.001157382 | 329.927 |
| 78 | 715 | 3437.21531055 | 4.2687536e-05 | 0.001157382 | 328.526 |
| 78 | 716 | 3439.62550700 | 5.0725206e-05 | 0.001157382 | 327.894 |
| 78 | 717 | 3442.03579911 | 5.4758169e-05 | 0.001157382 | 328.753 |
| 78 | 719 | 3446.85635604 | 5.2975202e-05 | 0.001157382 | 328.724 |
| 78 | 720 | 3449.26659568 | 4.8323437e-05 | 0.001157382 | 330.895 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/helper-audit.md).


Stable review key: R623.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/fresh-pixels/run.log)
- [historical/diff_s49.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/historical/diff_s49.json)
- [historical/diff_s49.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/historical/diff_s49.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/165793290/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
