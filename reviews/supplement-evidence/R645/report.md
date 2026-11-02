# TIC 257773097: CONFIRMED

Full bounded physical review: **COMPLETE**. Fourteen measured deep repeated eclipses and shallower secondary near0.49823. Sector94 aperture depths are shallower than12/66; differences remain visible. No capable Gaia neighbor within60arcsec; compact deficit favors target.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/phase-review.png), including P and2P parity views. 14 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=4.94533220820 +/- 0.00000470980 d; reference BTJD=1627.37051641. Epoch kind: Deeper primary eclipse, established relative to observed shallower secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.010326549866140703; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/half-period-coverage.json). For265092213, orbital cycles=(historical cycle-1)/2 use deeper odd events; shallower even-cycle secondaries remain in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; systems without secure secondaries retain sampled opposite-phase coverage rather than a claimed clean null; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Narrow shallower secondary visible in raw pooled windows. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.4982304, formal phase covariance error=0.00010666; depth=15.164 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Gaia conjunction search guide, adjusted from observed raw phase morphology for this batch. Final phase is a free-center fit to observed raw flux..

Fresh difference image: sector39, 6 complete core/sideband events. Target pixel=[7.335648074406331, 7.706993323946454]; deficit centroid=[7.315448577715157, 7.831164066193662]; deficit-target distance=0.1258 pixel. Deficit-light offset=5.528 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.8594 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Fourteen measured deep repeated eclipses and shallower secondary near0.49823. Sector94 aperture depths are shallower than12/66; differences remain visible. No capable Gaia neighbor within60arcsec; compact deficit favors target.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| None | | | | | |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 180.771/176.371/155.583 ppt versus fitted raw QLP median178.046 ppt. Individual cutout event depths are retained in the pixel JSON. Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source4613765126197369216: P=4.94523453 +/-0.00047074 d, e=0.035622, omega=226.21868 degrees, periastron BTJD=387.9539663. Closest edge-on conjunction offset=-0.005669 d (-0.001146 phase), source-specific full-covariance linear uncertainty=0.133088 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/gaia-geometry.json). Mass function=0.042412 solar masses, assumed M1=1.16, minimum M2=0.4862; approximate central duration=4.556 h versus observed3.902 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 12 | -1 | 1627.37028903 | 0.00087201221 | 0.010416812 | 178.107 |
| 12 | 1 | 1637.26035930 | 0.00017161622 | 0.010416812 | 175.709 |
| 12 | 2 | 1642.20654603 | 0.00083444681 | 0.010416812 | 178.356 |
| 12 | 3 | 1647.15191278 | 0.00049640907 | 0.010416812 | 178.472 |
| 12 | 4 | 1652.09652065 | 0.0003637752 | 0.010416812 | 178.658 |
| 66 | 297 | 3101.07942961 | 0.00016473736 | 0.0011574188 | 180.337 |
| 66 | 298 | 3106.02468827 | 0.00013578836 | 0.0011574188 | 177.985 |
| 66 | 299 | 3110.97025362 | 0.00018385347 | 0.0011574188 | 178.243 |
| 66 | 300 | 3115.91575577 | 0.00011855295 | 0.0011574188 | 177.772 |
| 66 | 301 | 3120.86083290 | 0.00015328137 | 0.0011574188 | 182.143 |
| 94 | 450 | 3857.71513400 | 0.00015036786 | 0.0011574009 | 162.920 |
| 94 | 452 | 3867.60606593 | 0.00010292629 | 0.0011574009 | 160.399 |
| 94 | 453 | 3872.55136247 | 0.00011065621 | 0.0011574009 | 159.397 |
| 94 | 454 | 3877.49675070 | 0.00010486983 | 0.0011574009 | 158.688 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/helper-audit.md).


Stable review key: R645.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/fresh-pixels/run.log)
- [historical/diff_s39.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/historical/diff_s39.json)
- [historical/diff_s39.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/historical/diff_s39.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/raw-windows.csv)
- [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/257773097/secondary-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
