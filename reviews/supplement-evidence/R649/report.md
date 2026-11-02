# TIC 274795477: CONFIRMED

Full bounded physical review: **COMPLETE**. Six deep repeated eclipses with shallower eccentric secondary near0.63234. All four capable neighbors at31.82-47.57arcsec lie away from compact target deficit; aperture depth dilution remains explicit.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/phase-review.png), including P and2P parity views. 6 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=9.69535645819 +/- 0.00001613144 d; reference BTJD=1548.89564693. Epoch kind: Deeper primary eclipse, established relative to observed shallower secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.16442273333957583; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/half-period-coverage.json). For265092213, orbital cycles=(historical cycle-1)/2 use deeper odd events; shallower even-cycle secondaries remain in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; systems without secure secondaries retain sampled opposite-phase coverage rather than a claimed clean null; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Narrow shallower secondary visible in raw pooled windows. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.6323483, formal phase covariance error=6.2394e-05; depth=47.634 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Gaia conjunction search guide, adjusted from observed raw phase morphology for this batch. Final phase is a free-center fit to observed raw flux..

Fresh difference image: sector64, 3 complete core/sideband events. Target pixel=[7.980715264746166, 7.626836464579224]; deficit centroid=[7.801219714231831, 7.689320497886531]; deficit-target distance=0.1901 pixel. Deficit-light offset=3.952 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.8310 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Six deep repeated eclipses with shallower eccentric secondary near0.63234. All four capable neighbors at31.82-47.57arcsec lie away from compact target deficit; aperture depth dilution remains explicit.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 5259205668929810688 | 31.818 | 14.431 | 0.5861 | [8.903004837651865, 8.86491556285581] | 0.014393374665472861 |
| 5259205600210331904 | 42.653 | 14.782 | 0.7729 | [6.386844141470037, 9.041071013832473] | 0.02798814488154601 |
| 5259211510085340288 | 43.206 | 13.320 | 0.2717 | [7.941539222011265, 5.525272826128213] | 0.015615574191644119 |
| 5259205600210333312 | 47.568 | 14.552 | 0.6440 | [5.655941750787015, 8.149159313232119] | 0.03696982995669122 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 79.050/61.011/43.973 ppt versus fitted raw QLP median95.239 ppt. Individual cutout event depths are retained in the pixel JSON. Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source5259205634570074624: P=9.69714320 +/-0.00171315 d, e=0.232096, omega=8.50958 degrees, periastron BTJD=393.5430881. Closest edge-on conjunction offset=-0.117910 d (-0.012159 phase), source-specific full-covariance linear uncertainty=0.200328 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/gaia-geometry.json). Mass function=0.100484 solar masses, assumed M1=2.68, minimum M2=1.1351; approximate central duration=8.235 h versus observed7.321 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 9 | 0 | 1548.89367396 | 0.00082871694 | 0.010416851 | 84.551 |
| 37 | 79 | 2314.82978554 | 0.00059145824 | 0.0034721796 | 94.593 |
| 37 | 80 | 2324.52358737 | 0.00055646813 | 0.0034721796 | 95.613 |
| 90 | 227 | 3749.74100202 | 0.00052973271 | 0.0011574132 | 97.044 |
| 90 | 228 | 3759.43685130 | 0.00072583741 | 0.0011574132 | 96.369 |
| 90 | 229 | 3769.13288451 | 0.00065048961 | 0.0011574132 | 94.866 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/helper-audit.md).


Stable review key: R649.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/fresh-pixels/run.log)
- [historical/diff_s64.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/historical/diff_s64.json)
- [historical/diff_s64.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/historical/diff_s64.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/raw-windows.csv)
- [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/274795477/secondary-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch11/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
