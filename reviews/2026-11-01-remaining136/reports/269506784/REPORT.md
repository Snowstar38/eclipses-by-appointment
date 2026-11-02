# TIC 269506784: CONFIRMED

Full bounded physical review: **COMPLETE**. Fourteen deep repeated raw eclipses and shallower secondary near phase0.4849. Strong sector97 baseline excursions were kept visible; local eclipse baselines remain stable. No capable Gaia neighbor within60arcsec; compact deficit favors target.

Raw morphology was inspected in [raw-events.png](../../campaign/batch09/269506784/raw-events.png) and [phase-review.png](../../campaign/batch09/269506784/phase-review.png), including P and2P parity views. 14 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=5.45026009462 +/- 0.00000631346 d; reference BTJD=1387.73929467. Epoch kind: Deeper primary eclipse, established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.04822138918888307; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch09/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](../../campaign/batch09/half-period-coverage.json). For138080650, orbital cycles are half the even historical SAP cycles; excluded odd-cycle secondaries remain in [measurements.json](../../campaign/batch09/269506784/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; TIC138854818 instead has sampled opposite-phase coverage without a comparable11ppt primary; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Narrow shallower secondary visible in raw pooled windows. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.4849101, formal phase covariance error=0.00013979; depth=39.800 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Gaia conjunction search guide, adjusted from raw phase morphology for435209690 and58825156. Final phase is a free-center fit to observed raw flux..

Fresh difference image: sector97, 7 complete core/sideband events. Target pixel=[7.114449550354204, 7.888973013492947]; deficit centroid=[6.995229226613039, 8.044322784281377]; deficit-target distance=0.1958 pixel. Deficit-light offset=3.578 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.3250 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Fourteen deep repeated raw eclipses and shallower secondary near phase0.4849. Strong sector97 baseline excursions were kept visible; local eclipse baselines remain stable. No capable Gaia neighbor within60arcsec; compact deficit favors target.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| None | | | | | |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch09/269506784/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 313.141/302.206/278.755 ppt versus fitted raw QLP median284.165 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source2535953823492249216: P=5.45079570 +/-0.00074945 d, e=0.052840, omega=174.77875 degrees, periastron BTJD=391.5568944. Closest edge-on conjunction offset=-0.120499 d (-0.022107 phase), source-specific full-covariance linear uncertainty=0.150816 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch09/gaia-geometry.json). Mass function=0.0814529 solar masses, assumed M1=0.92, minimum M2=0.56396; approximate central duration=5.703 h versus observed3.920 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 3 | 0 | 1387.73932484 | 0.00067371827 | 0.010416718 | 309.882 |
| 3 | 1 | 1393.19174459 | 0.00017055367 | 0.010416718 | 285.482 |
| 3 | 2 | 1398.64302174 | 0.00010059895 | 0.010416718 | 304.218 |
| 3 | 3 | 1404.08958205 | 0.00016069894 | 0.010416718 | 288.327 |
| 43 | 200 | 2477.79092948 | 0.0001598094 | 0.0034722749 | 331.648 |
| 43 | 202 | 2488.69156595 | 0.00013608874 | 0.0034722749 | 326.991 |
| 43 | 203 | 2494.14188394 | 0.00011938612 | 0.0034722749 | 327.371 |
| 97 | 468 | 3938.46101025 | 6.3283151e-05 | 0.001157396 | 275.610 |
| 97 | 469 | 3943.91082332 | 6.6996935e-05 | 0.001157396 | 279.721 |
| 97 | 471 | 3954.81219824 | 0.00016970938 | 0.001157396 | 277.071 |
| 97 | 472 | 3960.26184065 | 7.9271756e-05 | 0.001157396 | 281.206 |
| 97 | 473 | 3965.71233002 | 8.8570002e-05 | 0.001157396 | 275.447 |
| 97 | 474 | 3971.16251663 | 6.2388828e-05 | 0.001157396 | 280.212 |
| 97 | 477 | 3987.51373110 | 8.1245798e-05 | 0.001157396 | 282.847 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch09/identity-check.json) and [../source-hashes.json](../../campaign/batch09/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch09/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch09/helper-audit.md).


Stable review key: R620.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch09/269506784/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch09/269506784/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch09/269506784/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch09/269506784/fresh-pixels/run.log)
- [historical/diff_s97.json](../../campaign/batch09/269506784/historical/diff_s97.json)
- [historical/diff_s97.png](../../campaign/batch09/269506784/historical/diff_s97.png)
- [historical/gaia.json](../../campaign/batch09/269506784/historical/gaia.json)
- [measurements.json](../../campaign/batch09/269506784/measurements.json)
- [phase-review.png](../../campaign/batch09/269506784/phase-review.png)
- [raw-events.png](../../campaign/batch09/269506784/raw-events.png)
- [raw-windows.csv](../../campaign/batch09/269506784/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch09/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
