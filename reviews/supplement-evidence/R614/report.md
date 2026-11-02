# TIC 157367278: CONFIRMED

Full bounded physical review: **COMPLETE**. Sixteen deep flat-bottomed eclipses, shallower secondary near0.5000. No capable Gaia neighbor within60 arcsec. Bright displaced field light shifts the light centroid; target-centered deficit remains distinct.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/phase-review.png), including P and2P parity views. 16 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=4.11664108081 +/- 0.00000246441 d; reference BTJD=1575.08062436. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.13093186766783096; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Measured secondary-like narrow feature; pooled shape and baseline systematics limit precision. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.5000308, formal phase covariance error=0.00013859; depth=22.687 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Source-specific Gaia conjunction separation search guide; fitted center is free.

Fresh difference image: sector63, 6 complete core/sideband events. Target pixel=[7.891244786908853, 7.714420930394285]; deficit centroid=[8.125236690968716, 7.856333000849923]; deficit-target distance=0.2737 pixel. Deficit-light offset=16.640 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.9345 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Sixteen deep flat-bottomed eclipses, shallower secondary near0.5000. No capable Gaia neighbor within60 arcsec. Bright displaced field light shifts the light centroid; target-centered deficit remains distinct.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| None | | | | | |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 160.874/140.012/95.959 ppt versus fitted raw QLP median169.094 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source3465408557646425216: P=4.11659407 +/-0.00027865 d, e=0.043913, omega=216.54607 degrees, periastron BTJD=390.9441198. Closest edge-on conjunction offset=-0.042675 d (-0.010367 phase), source-specific full-covariance linear uncertainty=0.126053 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/gaia-geometry.json). Mass function=0.0409336 solar masses, assumed M1=1.09, minimum M2=0.46197; approximate central duration=4.025 h versus observed3.161 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 10 | 0 | 1575.07377736 | 6.0978187e-05 | 0.010416558 | 159.994 |
| 10 | 1 | 1579.19347892 | 5.255786e-05 | 0.010416558 | 171.644 |
| 10 | 3 | 1587.42394779 | 6.9696811e-05 | 0.010416558 | 169.193 |
| 10 | 4 | 1591.54598238 | 7.8304556e-05 | 0.010416558 | 168.994 |
| 63 | 350 | 3015.90514294 | 0.00013084214 | 0.0011574261 | 184.567 |
| 63 | 351 | 3020.02151782 | 0.00013071038 | 0.0011574261 | 185.266 |
| 63 | 352 | 3024.13829371 | 0.00013254933 | 0.0011574261 | 185.397 |
| 63 | 353 | 3028.25491332 | 0.00012609587 | 0.0011574261 | 184.542 |
| 63 | 354 | 3032.37177871 | 0.00011738906 | 0.0011574261 | 183.605 |
| 63 | 355 | 3036.48850502 | 8.8715478e-05 | 0.0011574261 | 184.381 |
| 101 | 614 | 4102.69887311 | 0.00010522697 | 0.0011574069 | 165.983 |
| 101 | 615 | 4106.81517977 | 9.7537424e-05 | 0.0011574069 | 166.105 |
| 101 | 616 | 4110.93138092 | 0.00015661737 | 0.0011574069 | 166.054 |
| 101 | 617 | 4115.04805393 | 0.0001106234 | 0.0011574069 | 166.078 |
| 101 | 618 | 4119.16423910 | 0.00013221227 | 0.0011574069 | 165.205 |
| 101 | 619 | 4123.28108551 | 0.00013911241 | 0.0011574069 | 163.462 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/helper-audit.md).


Stable review key: R614.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/fresh-pixels/run.log)
- [historical/diff_s63.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/historical/diff_s63.json)
- [historical/diff_s63.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/historical/diff_s63.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/157367278/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
