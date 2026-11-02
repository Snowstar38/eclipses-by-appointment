# TIC 58825156: PROBABLE

Full bounded physical review: **COMPLETE**. Twelve repeated raw eclipses and shallower secondary near0.50704 are real. Capable Gaia2776848815318667392 at12.4345arcsec overlaps the TESS footprint; the0.227pixel deficit offset and broad fractional-loss pattern do not securely separate ownership. Attribution remains unresolved.

Raw morphology was inspected in [raw-events.png](../../campaign/batch09/58825156/raw-events.png) and [phase-review.png](../../campaign/batch09/58825156/phase-review.png), including P and2P parity views. 12 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=5.33586901784 +/- 0.00001143038 d; reference BTJD=1770.59913511. Epoch kind: Deeper primary eclipse, established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.15085620427980728; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch09/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](../../campaign/batch09/half-period-coverage.json). For138080650, orbital cycles are half the even historical SAP cycles; excluded odd-cycle secondaries remain in [measurements.json](../../campaign/batch09/58825156/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; TIC138854818 instead has sampled opposite-phase coverage without a comparable11ppt primary; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Narrow shallower secondary visible in raw pooled windows. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.5070393, formal phase covariance error=0.00014634; depth=18.854 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Gaia conjunction search guide, adjusted from raw phase morphology for435209690 and58825156. Final phase is a free-center fit to observed raw flux..

Fresh difference image: sector70, 4 complete core/sideband events. Target pixel=[7.237332270066636, 7.353260504601428]; deficit centroid=[7.010190963174136, 7.354613303020761]; deficit-target distance=0.2271 pixel. Deficit-light offset=1.631 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.0923 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Twelve repeated raw eclipses and shallower secondary near0.50704 are real. Capable Gaia2776848815318667392 at12.4345arcsec overlaps the TESS footprint; the0.227pixel deficit offset and broad fractional-loss pattern do not securely separate ownership. Attribution remains unresolved.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 2776848815318667392 | 12.435 | 14.390 | 0.3864 | [6.978450099330313, 7.899198860435133] | 0.04285828942480618 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch09/58825156/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 50.749/47.409/46.482 ppt versus fitted raw QLP median60.933 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source2776848815318667264: P=5.33616672 +/-0.00070417 d, e=0.074586, omega=42.56272 degrees, periastron BTJD=387.9881972. Closest edge-on conjunction offset=-0.069542 d (-0.013032 phase), source-specific full-covariance linear uncertainty=0.210857 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch09/gaia-geometry.json). Mass function=0.0687954 solar masses, assumed M1=1.06, minimum M2=0.56677; approximate central duration=5.286 h versus observed3.519 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 17 | 0 | 1770.59887260 | 0.00083411997 | 0.010416416 | 57.923 |
| 17 | 2 | 1781.27370302 | 0.0010413178 | 0.010416416 | 53.411 |
| 17 | 3 | 1786.60773263 | 0.0010929274 | 0.010416416 | 52.386 |
| 43 | 132 | 2474.93378733 | 0.00040812712 | 0.0034723019 | 63.424 |
| 43 | 133 | 2480.26991828 | 0.00062222378 | 0.0034723019 | 65.203 |
| 43 | 135 | 2490.94111524 | 0.00051675384 | 0.0034723019 | 63.548 |
| 43 | 136 | 2496.27673503 | 0.00041133702 | 0.0034723019 | 62.456 |
| 70 | 270 | 3211.28374948 | 0.00044686273 | 0.0011574215 | 61.086 |
| 70 | 271 | 3216.61897133 | 0.00043502559 | 0.0011574215 | 59.135 |
| 70 | 272 | 3221.95665668 | 0.00048004204 | 0.0011574215 | 60.781 |
| 70 | 273 | 3227.29116055 | 0.00046978257 | 0.0011574215 | 60.315 |
| 70 | 274 | 3232.62704426 | 0.00044153643 | 0.0011574215 | 62.692 |

Next check: Resolved eclipse photometry or multi-source PRF localization for target and12.43-arcsec neighbor.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch09/identity-check.json) and [../source-hashes.json](../../campaign/batch09/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch09/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch09/helper-audit.md).


Stable review key: R628.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch09/58825156/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch09/58825156/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch09/58825156/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch09/58825156/fresh-pixels/run.log)
- [historical/diff_s70.json](../../campaign/batch09/58825156/historical/diff_s70.json)
- [historical/diff_s70.png](../../campaign/batch09/58825156/historical/diff_s70.png)
- [historical/gaia.json](../../campaign/batch09/58825156/historical/gaia.json)
- [measurements.json](../../campaign/batch09/58825156/measurements.json)
- [phase-review.png](../../campaign/batch09/58825156/phase-review.png)
- [raw-events.png](../../campaign/batch09/58825156/raw-events.png)
- [raw-windows.csv](../../campaign/batch09/58825156/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch09/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
