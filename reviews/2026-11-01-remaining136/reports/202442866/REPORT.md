# TIC 202442866: CONFIRMED

Full bounded physical review: **COMPLETE**. Nine deep repeated raw eclipses plus a broad shallower secondary near0.4988. Target-centered deficit; no capable Gaia neighbor within60 arcsec.

Raw morphology was inspected in [raw-events.png](../../campaign/batch08/202442866/raw-events.png) and [phase-review.png](../../campaign/batch08/202442866/phase-review.png), including P and2P parity views. 9 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=4.03223527947 +/- 0.00001182526 d; reference BTJD=1928.78976127. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.06663373816751848; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Measured secondary-like narrow feature; pooled shape and baseline systematics limit precision. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.4987686, formal phase covariance error=0.0010538; depth=6.856 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Source-specific Gaia conjunction separation search guide; fitted center is free.

Fresh difference image: sector41, 6 complete core/sideband events. Target pixel=[7.983382444673236, 7.309586675452248]; deficit centroid=[8.056274517227141, 7.306475444829257]; deficit-target distance=0.0730 pixel. Deficit-light offset=0.778 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.1180 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Nine deep repeated raw eclipses plus a broad shallower secondary near0.4988. Target-centered deficit; no capable Gaia neighbor within60 arcsec.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| None | | | | | |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch08/202442866/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 85.836/86.043/85.018 ppt versus fitted raw QLP median81.623 ppt. Individual cutout event depths are retained in the pixel JSON. Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source1619728688122974976: P=4.03203511 +/-0.00027623 d, e=0.072469, omega=267.67105 degrees, periastron BTJD=390.5189958. Closest edge-on conjunction offset=0.019291 d (0.004784 phase), source-specific full-covariance linear uncertainty=0.115781 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch08/gaia-geometry.json). Mass function=0.0227813 solar masses, assumed M1=1.05, minimum M2=0.35574; approximate central duration=4.650 h versus observed3.029 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 23 | 53 | 1928.79142984 | 0.00057061555 | 0.01041657 | 84.437 |
| 23 | 54 | 1932.82322607 | 0.00028051283 | 0.01041657 | 85.989 |
| 23 | 55 | 1936.85439171 | 0.00011644339 | 0.01041657 | 80.986 |
| 23 | 57 | 1944.91812446 | 0.00055373564 | 0.01041657 | 81.623 |
| 23 | 58 | 1948.95009449 | 0.0008325492 | 0.01041657 | 84.913 |
| 23 | 59 | 1952.98178436 | 0.00085721226 | 0.01041657 | 80.294 |
| 77 | 417 | 3396.52286105 | 0.00027399421 | 0.001157393 | 83.127 |
| 77 | 419 | 3404.58836192 | 0.00050463372 | 0.001157393 | 80.031 |
| 77 | 423 | 3420.71686521 | 0.0003910175 | 0.001157393 | 81.556 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch08/identity-check.json) and [../source-hashes.json](../../campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch08/helper-audit.md).


Stable review key: R616.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch08/202442866/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch08/202442866/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch08/202442866/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch08/202442866/fresh-pixels/run.log)
- [historical/diff_s41.json](../../campaign/batch08/202442866/historical/diff_s41.json)
- [historical/diff_s41.png](../../campaign/batch08/202442866/historical/diff_s41.png)
- [historical/gaia.json](../../campaign/batch08/202442866/historical/gaia.json)
- [measurements.json](../../campaign/batch08/202442866/measurements.json)
- [phase-review.png](../../campaign/batch08/202442866/phase-review.png)
- [raw-events.png](../../campaign/batch08/202442866/raw-events.png)
- [raw-windows.csv](../../campaign/batch08/202442866/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch08/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
