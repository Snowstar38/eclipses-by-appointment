# TIC 70241645: CONFIRMED

Full bounded physical review: **COMPLETE**. Four narrow repeated eclipses in three sectors, including consecutive sector81 same-kind events. No secure secondary. All five capable neighbors at25.25-49.41arcsec are displaced from compact target deficit; crowded field light centroid is descriptive. Custom cutout reduction in sector40 recovers one event, a distinct observing occasion from the retained QLP sectors.

Raw morphology was inspected in [raw-events.png](../../campaign/batch11/70241645/raw-events.png) and [phase-review.png](../../campaign/batch11/70241645/phase-review.png), including P and2P parity views. 4 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=18.31468255723 +/- 0.00007003110 d; reference BTJD=1695.67009353. Epoch kind: Selected repeating narrow eclipse; deeper-primary identity unestablished because no secure secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.7283698884494509; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch11/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](../../campaign/batch11/half-period-coverage.json). For265092213, orbital cycles=(historical cycle-1)/2 use deeper odd events; shallower even-cycle secondaries remain in [measurements.json](../../campaign/batch11/70241645/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; systems without secure secondaries retain sampled opposite-phase coverage rather than a claimed clean null; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

No secure secondary; noisy low-amplitude exploratory fit not interpreted as eclipse. A fitted low-amplitude pooled model is not evidence of a secondary; flagged and missing coverage are not clean nulls.

Fresh difference image: sector40, 1 complete core/sideband events. Target pixel=[7.950635389498599, 7.59246590910835]; deficit centroid=[8.068951890397704, 7.720586638946299]; deficit-target distance=0.1744 pixel. Deficit-light offset=8.992 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.7753 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Four narrow repeated eclipses in three sectors, including consecutive sector81 same-kind events. No secure secondary. All five capable neighbors at25.25-49.41arcsec are displaced from compact target deficit; crowded field light centroid is descriptive. Custom cutout reduction in sector40 recovers one event, a distinct observing occasion from the retained QLP sectors.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 2047234339629598848 | 25.255 | 15.205 | 0.5481 | [9.24748653772242, 7.557210838700486] | 0.029144313299321458 |
| 2047234129153105920 | 28.847 | 13.061 | 0.1157 | [6.5067065971801075, 7.857127756560375] | 0.01783167185123211 |
| 2047234064751686912 | 35.794 | 14.998 | 0.4609 | [6.284061131625569, 8.269869821427656] | 0.0005537097429362335 |
| 2047234167830903168 | 47.232 | 15.581 | 0.7560 | [5.617765024736477, 8.139778795246515] | 0.0005537097429362335 |
| 2047234335311560832 | 49.415 | 15.344 | 0.6170 | [9.963426898186825, 6.185879131617189] | 0.0026425706979882296 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch11/70241645/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 35.690/26.576/16.909 ppt versus fitted raw QLP median46.002 ppt. Individual cutout event depths are retained in the pixel JSON. Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source2047234129153107328: P=18.30387003 +/-0.02060793 d, e=0.138705, omega=46.05718 degrees, periastron BTJD=393.9868668. Closest edge-on conjunction offset=0.394804 d (0.021569 phase), source-specific full-covariance linear uncertainty=1.674045 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch11/gaia-geometry.json). Mass function=0.00274715 solar masses, assumed M1=0.812, minimum M2=0.13507; approximate central duration=4.146 h versus observed3.234 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 14 | 0 | 1695.66807769 | 0.00096081319 | 0.010416903 | 47.464 |
| 55 | 61 | 2812.86653178 | 0.00065822503 | 0.003472144 | 47.553 |
| 81 | 99 | 3508.82267861 | 0.00074764861 | 0.0011574063 | 44.539 |
| 81 | 100 | 3527.13927307 | 0.00060391125 | 0.0011574063 | 44.376 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch11/identity-check.json) and [../source-hashes.json](../../campaign/batch11/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch11/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch11/helper-audit.md).


Stable review key: R643.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch11/70241645/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch11/70241645/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch11/70241645/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch11/70241645/fresh-pixels/run.log)
- [historical/diff_s40.json](../../campaign/batch11/70241645/historical/diff_s40.json)
- [historical/diff_s40.png](../../campaign/batch11/70241645/historical/diff_s40.png)
- [historical/gaia.json](../../campaign/batch11/70241645/historical/gaia.json)
- [measurements.json](../../campaign/batch11/70241645/measurements.json)
- [phase-review.png](../../campaign/batch11/70241645/phase-review.png)
- [raw-events.png](../../campaign/batch11/70241645/raw-events.png)
- [raw-windows.csv](../../campaign/batch11/70241645/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch11/70241645/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch11/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
