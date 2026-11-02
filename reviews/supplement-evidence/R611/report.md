# TIC 176048490: CONFIRMED

Full bounded physical review: **COMPLETE**. Four deep, flat-bottomed raw eclipses and an unequal secondary near phase0.3683 support eccentric binary morphology. The capable neighbor at56.6 arcsec is separated from the deficit.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/phase-review.png), including P and2P parity views. 4 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=12.77337644993 +/- 0.00002030227 d; reference BTJD=2973.25954728. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.12471103186425339; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Measured secondary-like narrow feature; pooled shape and baseline systematics limit precision. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.3682844, formal phase covariance error=0.00010924; depth=9.490 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Raw full-phase visual estimate.

Fresh difference image: sector34, 2 complete core/sideband events. Target pixel=[7.5557581337728354, 7.089043736515528]; deficit centroid=[7.63828595577322, 7.0682956753274535]; deficit-target distance=0.0851 pixel. Deficit-light offset=8.049 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.6804 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Four deep, flat-bottomed raw eclipses and an unequal secondary near phase0.3683 support eccentric binary morphology. The capable neighbor at56.6 arcsec is separated from the deficit.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 5713290296012427648 | 56.597 | 13.816 | 0.6214 | [5.412614306915825, 5.475570709494404] | 0.00051227519517977 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 154.207/154.320/132.096 ppt versus fitted raw QLP median145.938 ppt. Individual cutout event depths are retained in the pixel JSON. Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source5713288814241556864: P=12.76704696 +/-0.00327314 d, e=0.287234, omega=192.33598 degrees, periastron BTJD=383.0046519. Closest edge-on conjunction offset=0.994810 d (0.077920 phase), source-specific full-covariance linear uncertainty=0.630871 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/gaia-geometry.json). Mass function=0.0296587 solar masses, assumed M1=0.947, minimum M2=0.37236; approximate central duration=5.915 h versus observed5.292 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 61 | 115 | 2973.25975420 | 0.0001805511 | 0.0011574051 | 146.096 |
| 61 | 116 | 2986.03271941 | 0.00017673385 | 0.0011574051 | 145.781 |
| 88 | 172 | 3701.34165039 | 0.00022051984 | 0.0011574096 | 147.355 |
| 88 | 173 | 3714.11573332 | 0.00020133648 | 0.0011574096 | 145.095 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/helper-audit.md).


Stable review key: R611.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/fresh-pixels/run.log)
- [historical/diff_s34.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/historical/diff_s34.json)
- [historical/diff_s34.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/historical/diff_s34.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/176048490/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch08/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
