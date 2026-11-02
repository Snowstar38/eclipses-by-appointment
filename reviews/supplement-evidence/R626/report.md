# TIC 138854818: CONFIRMED

Full bounded physical review: **COMPLETE**. Eleven consistent shallow raw eclipse timings across three sectors; representative windows show narrow repeatable11ppt dips despite substantial sector98 baseline noise. Compact sector98 deficit favors target over capable33.33/53.79arcsec neighbors. No secure secondary; opposite-phase coverage lacks a comparable primary, without excluding shallow dips.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/phase-review.png), including P and2P parity views. 11 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=5.78696892497 +/- 0.00000555101 d; reference BTJD=1472.15551942. Epoch kind: Selected repeating eclipse; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=1.0123785624289992; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/half-period-coverage.json). For138080650, orbital cycles are half the even historical SAP cycles; excluded odd-cycle secondaries remain in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; TIC138854818 instead has sampled opposite-phase coverage without a comparable11ppt primary; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

No secure secondary; noisy low-amplitude exploratory fit not interpreted as eclipse. A fitted low-amplitude pooled model is not evidence of a secondary; flagged and missing coverage are not clean nulls.

Fresh difference image: sector98, 6 complete core/sideband events. Target pixel=[7.272864382234976, 7.6262271300283455]; deficit centroid=[7.214408618368344, 7.7652239760118125]; deficit-target distance=0.1508 pixel. Deficit-light offset=2.381 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.3766 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Eleven consistent shallow raw eclipse timings across three sectors; representative windows show narrow repeatable11ppt dips despite substantial sector98 baseline noise. Compact sector98 deficit favors target over capable33.33/53.79arcsec neighbors. No secure secondary; opposite-phase coverage lacks a comparable primary, without excluding shallow dips.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 3236840942297477248 | 33.328 | 15.492 | 0.1756 | [6.154179124252758, 8.77044276259647] | 0.00978607236496007 |
| 3236840976662227840 | 53.787 | 17.315 | 0.8925 | [8.41092364713651, 9.92785875424227] | 0.03427849783888747 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 13.106/13.815/15.933 ppt versus fitted raw QLP median11.145 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source3236840946592866560: P=5.78750160 +/-0.00395146 d, e=0.133831, omega=16.58694 degrees, periastron BTJD=388.7994091. Closest edge-on conjunction offset=0.142155 d (0.024562 phase), source-specific full-covariance linear uncertainty=0.449613 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/gaia-geometry.json). Mass function=0.00156602 solar masses, assumed M1=1.34, minimum M2=0.1516; approximate central duration=5.575 h versus observed5.671 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 6 | 0 | 1472.15283776 | 0.0029376235 | 0.010416469 | 12.351 |
| 6 | 2 | 1483.72011146 | 0.0020186356 | 0.010416469 | 11.145 |
| 32 | 122 | 2178.16667013 | 0.0022593999 | 0.003472288 | 11.283 |
| 32 | 123 | 2183.95550115 | 0.0021561917 | 0.003472288 | 11.042 |
| 32 | 124 | 2189.73546800 | 0.0016507744 | 0.003472288 | 11.806 |
| 32 | 125 | 2195.52903866 | 0.0014345975 | 0.003472288 | 11.878 |
| 98 | 436 | 3995.27508629 | 0.0011266372 | 0.0011574276 | 10.472 |
| 98 | 437 | 4001.06030630 | 0.0012774144 | 0.0012774144 | 10.212 |
| 98 | 439 | 4012.63323179 | 0.00092731601 | 0.0011574276 | 10.997 |
| 98 | 442 | 4029.99431863 | 0.0019931673 | 0.0019931673 | 11.495 |
| 98 | 444 | 4041.57138881 | 0.00122994 | 0.00122994 | 11.084 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/helper-audit.md).


Stable review key: R626.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/fresh-pixels/run.log)
- [historical/diff_s98.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/historical/diff_s98.json)
- [historical/diff_s98.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/historical/diff_s98.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/138854818/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
