# TIC 369587471: CONFIRMED

Full bounded physical review: **COMPLETE**. Twelve flat-bottomed repeated raw eclipses and a shallower secondary near0.5009. Sector-dependent baseline variability remains visible. No capable Gaia neighbor within60arcsec; target-centered compact deficit.

Raw morphology was inspected in [raw-events.png](../../campaign/batch09/369587471/raw-events.png) and [phase-review.png](../../campaign/batch09/369587471/phase-review.png), including P and2P parity views. 12 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=5.54117094061 +/- 0.00000904039 d; reference BTJD=1355.29116169. Epoch kind: Deeper primary eclipse, established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.6834212357957399; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch09/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](../../campaign/batch09/half-period-coverage.json). For138080650, orbital cycles are half the even historical SAP cycles; excluded odd-cycle secondaries remain in [measurements.json](../../campaign/batch09/369587471/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; TIC138854818 instead has sampled opposite-phase coverage without a comparable11ppt primary; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Narrow shallower secondary visible in raw pooled windows. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.5008911, formal phase covariance error=0.00035051; depth=7.017 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Gaia conjunction search guide, adjusted from raw phase morphology for435209690 and58825156. Final phase is a free-center fit to observed raw flux..

Fresh difference image: sector2, 5 complete core/sideband events. Target pixel=[7.336606030313423, 7.595824488552353]; deficit centroid=[7.375957634015044, 7.6134326426961385]; deficit-target distance=0.0431 pixel. Deficit-light offset=0.026 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.0870 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Twelve flat-bottomed repeated raw eclipses and a shallower secondary near0.5009. Sector-dependent baseline variability remains visible. No capable Gaia neighbor within60arcsec; target-centered compact deficit.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| None | | | | | |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch09/369587471/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 63.043/57.722/57.064 ppt versus fitted raw QLP median53.480 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source4994770575512682752: P=5.54088544 +/-0.00090485 d, e=0.037971, omega=109.72017 degrees, periastron BTJD=391.4459066. Closest edge-on conjunction offset=0.012703 d (0.002293 phase), source-specific full-covariance linear uncertainty=0.220157 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch09/gaia-geometry.json). Mass function=0.0392495 solar masses, assumed M1=1.02, minimum M2=0.43671; approximate central duration=7.193 h versus observed5.837 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 2 | 0 | 1355.29659037 | 0.0022371914 | 0.010416673 | 51.149 |
| 2 | 1 | 1360.83846762 | 0.0027333243 | 0.010416673 | 53.132 |
| 2 | 3 | 1371.92116599 | 0.003234885 | 0.010416673 | 52.894 |
| 2 | 4 | 1377.46111619 | 0.0034255995 | 0.010416673 | 51.814 |
| 96 | 461 | 3909.77046561 | 0.00038481949 | 0.001157409 | 53.872 |
| 96 | 462 | 3915.31157170 | 0.00037991574 | 0.001157409 | 53.277 |
| 96 | 464 | 3926.39381998 | 0.00042047366 | 0.001157409 | 53.169 |
| 96 | 465 | 3931.93423887 | 0.00036343765 | 0.001157409 | 53.937 |
| 104 | 510 | 4181.29025953 | 0.0007808911 | 0.0011574068 | 53.683 |
| 104 | 511 | 4186.83039986 | 0.00063660293 | 0.0011574068 | 54.988 |
| 104 | 513 | 4197.91192576 | 0.00091269307 | 0.0011574068 | 54.740 |
| 104 | 514 | 4203.45299262 | 0.00052280022 | 0.0011574068 | 55.397 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch09/identity-check.json) and [../source-hashes.json](../../campaign/batch09/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch09/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch09/helper-audit.md).


Stable review key: R621.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch09/369587471/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch09/369587471/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch09/369587471/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch09/369587471/fresh-pixels/run.log)
- [historical/diff_s02.json](../../campaign/batch09/369587471/historical/diff_s02.json)
- [historical/diff_s02.png](../../campaign/batch09/369587471/historical/diff_s02.png)
- [historical/gaia.json](../../campaign/batch09/369587471/historical/gaia.json)
- [measurements.json](../../campaign/batch09/369587471/measurements.json)
- [phase-review.png](../../campaign/batch09/369587471/phase-review.png)
- [raw-events.png](../../campaign/batch09/369587471/raw-events.png)
- [raw-windows.csv](../../campaign/batch09/369587471/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch09/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
