# TIC 370138999: CONFIRMED

Full bounded physical review: **COMPLETE**. Shallow repeated narrow raw eclipses; compact deficit near target. Three capable neighbors at31-59 arcsec are spatially separated from the deficit core. No secure secondary.

Raw morphology was inspected in [raw-events.png](../../campaign/batch08/370138999/raw-events.png) and [phase-review.png](../../campaign/batch08/370138999/phase-review.png), including P and2P parity views. 6 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=11.45212692602 +/- 0.00005868963 d; reference BTJD=1334.75715304. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=2.0463176264230576; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

No secure secondary established; numeric fit is a noise/variability description and not a detection or clean null. A fitted low-amplitude pooled model is not evidence of a secondary; flagged and missing coverage are not clean nulls.

Fresh difference image: sector2, 3 complete core/sideband events. Target pixel=[7.499832159344923, 7.69979626752945]; deficit centroid=[7.487886595322388, 7.820271053517303]; deficit-target distance=0.1211 pixel. Deficit-light offset=0.717 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.5707 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Shallow repeated narrow raw eclipses; compact deficit near target. Three capable neighbors at31-59 arcsec are spatially separated from the deficit core. No secure secondary.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 4639398934128295552 | 31.142 | 17.052 | 0.1707 | [7.335900214530367, 6.083904978865475] | 0.001042400878428005 |
| 4639398521811431936 | 49.989 | 15.749 | 0.0532 | [4.965076105923685, 7.876679048281579] | -0.0008962551083115956 |
| 4639399002847056512 | 59.272 | 17.574 | 0.2745 | [9.77374381387321, 9.899616852717259] | 0.01929205621903543 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch08/370138999/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 1.465/2.654/2.805 ppt versus fitted raw QLP median2.613 ppt. Individual cutout event depths are retained in the pixel JSON. Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source4639398560466507904: P=11.45073775 +/-0.00260474 d, e=0.259664, omega=310.63921 degrees, periastron BTJD=385.2158212. Closest edge-on conjunction offset=-0.110346 d (-0.009637 phase), source-specific full-covariance linear uncertainty=0.277266 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch08/gaia-geometry.json). Mass function=0.0138353 solar masses, assumed M1=1.19, minimum M2=0.31532; approximate central duration=5.516 h versus observed2.919 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 1 | 0 | 1334.77544164 | 0.0059817868 | 0.010416629 | 3.832 |
| 1 | 1 | 1346.20509536 | 0.0063566414 | 0.010416629 | 2.921 |
| 66 | 154 | 3098.37366519 | 0.0087793895 | 0.0087793895 | 1.965 |
| 66 | 155 | 3109.83880780 | 0.018654846 | 0.018654846 | 2.306 |
| 66 | 156 | 3121.28650236 | 0.0029436131 | 0.0029436131 | 3.071 |
| 96 | 225 | 3911.49486190 | 0.0056136962 | 0.0056136962 | 2.283 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch08/identity-check.json) and [../source-hashes.json](../../campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch08/helper-audit.md).


Stable review key: R610.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch08/370138999/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch08/370138999/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch08/370138999/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch08/370138999/fresh-pixels/run.log)
- [historical/diff_s02.json](../../campaign/batch08/370138999/historical/diff_s02.json)
- [historical/diff_s02.png](../../campaign/batch08/370138999/historical/diff_s02.png)
- [historical/gaia.json](../../campaign/batch08/370138999/historical/gaia.json)
- [measurements.json](../../campaign/batch08/370138999/measurements.json)
- [phase-review.png](../../campaign/batch08/370138999/phase-review.png)
- [raw-events.png](../../campaign/batch08/370138999/raw-events.png)
- [raw-windows.csv](../../campaign/batch08/370138999/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch08/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
