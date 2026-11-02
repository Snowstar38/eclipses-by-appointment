# TIC 380616368: PROBABLE

Full bounded physical review: **COMPLETE**. Six deep repeated raw eclipses and unequal secondary near0.5185 are real. A capable Gaia neighbor only13.06 arcsec away overlaps the TESS footprint; target ownership remains unresolved. Five farther capable neighbors were also inspected.

Raw morphology was inspected in [raw-events.png](../../campaign/batch08/380616368/raw-events.png) and [phase-review.png](../../campaign/batch08/380616368/phase-review.png), including P and2P parity views. 6 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=8.15650892898 +/- 0.00002369015 d; reference BTJD=1605.92938782. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.8107763251608298; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Measured secondary-like narrow feature; pooled shape and baseline systematics limit precision. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.5184862, formal phase covariance error=9.0402e-05; depth=56.034 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Source-specific Gaia conjunction separation search guide; fitted center is free.

Fresh difference image: sector102, 3 complete core/sideband events. Target pixel=[7.984219910855064, 7.151055731001835]; deficit centroid=[7.982266569395521, 7.192986553144256]; deficit-target distance=0.0420 pixel. Deficit-light offset=13.263 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.8995 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Six deep repeated raw eclipses and unequal secondary near0.5185 are real. A capable Gaia neighbor only13.06 arcsec away overlaps the TESS footprint; target ownership remains unresolved. Five farther capable neighbors were also inspected.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 5865932540392223744 | 13.062 | 13.383 | 0.3044 | [7.413797724135005, 7.4745392776389465] | 0.04293014794640035 |
| 5865932574751971968 | 31.123 | 14.215 | 0.5430 | [6.7043858440504325, 6.32825893447743] | 0.03388007637647905 |
| 5865932471672737152 | 39.075 | 14.471 | 0.6613 | [7.618816880269076, 9.033259925387112] | 0.025731756152021248 |
| 5865932501713536384 | 45.970 | 14.244 | 0.5551 | [5.704934176142195, 6.976021740059235] | 0.014972571479630815 |
| 5865932746550668288 | 51.176 | 12.688 | 0.2065 | [9.401522646121027, 5.035736722321651] | 0.001722808540661632 |
| 5865932780910412672 | 59.835 | 14.911 | 0.9431 | [6.996712839276932, 4.424907704445629] | -0.0017383728775638878 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch08/380616368/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 76.349/56.561/35.455 ppt versus fitted raw QLP median97.305 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source5865932540392225536: P=8.15520713 +/-0.00076285 d, e=0.011737, omega=263.75442 degrees, periastron BTJD=386.4956175. Closest edge-on conjunction offset=0.085477 d (0.010481 phase), source-specific full-covariance linear uncertainty=0.165039 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch08/gaia-geometry.json). Mass function=0.10988 solar masses, assumed M1=1.82, minimum M2=0.94314; approximate central duration=7.835 h versus observed5.951 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 11 | 0 | 1605.92702547 | 0.0025402268 | 0.010416736 | 98.019 |
| 11 | 2 | 1622.24095491 | 0.0012529065 | 0.010416736 | 101.632 |
| 99 | 302 | 4069.19679886 | 0.00039615136 | 0.0011574787 | 101.247 |
| 102 | 310 | 4134.44627395 | 0.00042510217 | 0.0011574068 | 95.492 |
| 102 | 311 | 4142.60293711 | 0.000427648 | 0.0011574068 | 96.223 |
| 102 | 312 | 4150.76011592 | 0.00068975804 | 0.0011574068 | 96.591 |

Next check: Resolved eclipse photometry or multi-source PRF localization for target and13.06-arcsec neighbor.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch08/identity-check.json) and [../source-hashes.json](../../campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch08/helper-audit.md).


Stable review key: R619.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch08/380616368/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch08/380616368/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch08/380616368/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch08/380616368/fresh-pixels/run.log)
- [historical/diff_s102.json](../../campaign/batch08/380616368/historical/diff_s102.json)
- [historical/diff_s102.png](../../campaign/batch08/380616368/historical/diff_s102.png)
- [historical/gaia.json](../../campaign/batch08/380616368/historical/gaia.json)
- [measurements.json](../../campaign/batch08/380616368/measurements.json)
- [phase-review.png](../../campaign/batch08/380616368/phase-review.png)
- [raw-events.png](../../campaign/batch08/380616368/raw-events.png)
- [raw-windows.csv](../../campaign/batch08/380616368/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch08/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
