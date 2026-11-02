# TIC 297956126: CONFIRMED

Full bounded physical review: **COMPLETE**. Five measured deep eclipses after adding S66 QLP. Consecutive same-kind S66 eclipses resolve the long-baseline cycle-count ambiguity. Unequal eccentric secondary near0.7244; three capable neighbors are spatially separated from compact deficit.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/phase-review.png), including P and2P parity views. 5 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=19.44125918346 +/- 0.00008930304 d; reference BTJD=3079.12129708. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=17.73047106287078; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Measured secondary-like narrow feature; pooled shape and baseline systematics limit precision. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.7243711, formal phase covariance error=3.3922e-05; depth=65.867 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Source-specific Gaia conjunction separation search guide; fitted center is free.

Fresh difference image: sector66, 2 complete core/sideband events. Target pixel=[7.67363198843382, 7.771735038897283]; deficit centroid=[7.640556238460893, 7.816464341886039]; deficit-target distance=0.0556 pixel. Deficit-light offset=9.645 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.8948 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Five measured deep eclipses after adding S66 QLP. Consecutive same-kind S66 eclipses resolve the long-baseline cycle-count ambiguity. Unequal eccentric secondary near0.7244; three capable neighbors are spatially separated from compact deficit.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 5828914663934337024 | 20.853 | 14.509 | 0.5494 | [6.749142680397109, 8.213817543181115] | 0.059674319508744446 |
| 5828913186465574656 | 47.532 | 13.257 | 0.2266 | [5.647107601520315, 8.927727163659231] | 0.00469858258554853 |
| 5828914732653848704 | 52.734 | 15.074 | 0.8712 | [8.730192586643438, 5.449452288812461] | 0.013509646736525561 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 73.596/63.216/45.498 ppt versus fitted raw QLP median77.858 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source5828914728327457664: P=19.44436463 +/-0.01167201 d, e=0.349916, omega=13.46118 degrees, periastron BTJD=394.1096717. Closest edge-on conjunction offset=-0.498592 d (-0.025642 phase), source-specific full-covariance linear uncertainty=1.659949 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/gaia-geometry.json). Mass function=0.114144 solar masses, assumed M1=1.51, minimum M2=0.86302; approximate central duration=13.883 h versus observed10.066 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 66 | 1 | 3098.56192268 | 0.0009313141 | 0.0011573952 | 81.574 |
| 66 | 2 | 3117.99882726 | 0.00081888804 | 0.0011573952 | 83.830 |
| 65 | 0 | 3079.12938743 | 0.0014235067 | 0.0014235067 | 77.858 |
| 100 | 52 | 4090.06837620 | 0.0013502117 | 0.0013502117 | 74.542 |
| 103 | 56 | 4167.83090804 | 0.00051382724 | 0.0011574068 | 73.654 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/helper-audit.md).


Stable review key: R617.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/fresh-pixels/run.log)
- [historical/diff_s66.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/historical/diff_s66.json)
- [historical/diff_s66.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/historical/diff_s66.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/297956126/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
