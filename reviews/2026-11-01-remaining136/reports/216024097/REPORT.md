# TIC 216024097: CONFIRMED

Full bounded physical review: **COMPLETE**. Nine repeated flat-bottomed raw eclipses and shallower secondary near0.5051. Three capable neighbors at38-56 arcsec are displaced from target deficit core.

Raw morphology was inspected in [raw-events.png](../../campaign/batch08/216024097/raw-events.png) and [phase-review.png](../../campaign/batch08/216024097/phase-review.png), including P and2P parity views. 9 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=5.96437448476 +/- 0.00000611621 d; reference BTJD=1630.79881660. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.7097269260367367; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Measured secondary-like narrow feature; pooled shape and baseline systematics limit precision. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.5051097, formal phase covariance error=0.00047603; depth=6.899 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Source-specific Gaia conjunction separation search guide; fitted center is free.

Fresh difference image: sector39, 3 complete core/sideband events. Target pixel=[7.497936311428383, 7.174649541884262]; deficit centroid=[7.58127932623185, 7.273839325942381]; deficit-target distance=0.1296 pixel. Deficit-light offset=4.279 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.8327 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Nine repeated flat-bottomed raw eclipses and shallower secondary near0.5051. Three capable neighbors at38-56 arcsec are displaced from target deficit core.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 5935133465769258112 | 37.871 | 15.512 | 0.7516 | [8.281782290671122, 8.987011854435043] | 0.006501992137497622 |
| 5935133461448421888 | 38.776 | 14.461 | 0.3144 | [7.129309021508924, 9.104486966453447] | 0.010425004404331329 |
| 5935133500128999936 | 55.644 | 13.210 | 0.1311 | [8.083067741218498, 9.995769686459242] | 0.0015192198659098976 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch08/216024097/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 49.785/46.399/32.701 ppt versus fitted raw QLP median46.468 ppt. Individual cutout event depths are retained in the pixel JSON. Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source5935133362690040704: P=5.96452661 +/-0.00080035 d, e=0.038954, omega=355.59763 degrees, periastron BTJD=388.6437177. Closest edge-on conjunction offset=0.043380 d (0.007273 phase), source-specific full-covariance linear uncertainty=0.183879 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch08/gaia-geometry.json). Mass function=0.0361226 solar masses, assumed M1=1.77, minimum M2=0.58516; approximate central duration=8.049 h versus observed6.958 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 12 | 0 | 1630.79097924 | 0.0020556164 | 0.01041668 | 43.043 |
| 12 | 1 | 1636.75878957 | 0.001223965 | 0.01041668 | 44.116 |
| 12 | 3 | 1648.68792966 | 0.0010864261 | 0.01041668 | 42.724 |
| 65 | 242 | 3074.17578402 | 0.0010002406 | 0.0011574385 | 48.579 |
| 65 | 243 | 3080.14282493 | 0.0011720439 | 0.0011720439 | 46.468 |
| 65 | 244 | 3086.10641379 | 0.00097879867 | 0.0011574385 | 49.422 |
| 65 | 245 | 3092.07150924 | 0.0010332578 | 0.0011574385 | 49.648 |
| 103 | 423 | 4153.72777968 | 0.0019533922 | 0.0019533922 | 49.120 |
| 103 | 424 | 4159.69381325 | 0.00059218528 | 0.0011574068 | 42.679 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch08/identity-check.json) and [../source-hashes.json](../../campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch08/helper-audit.md).


Stable review key: R618.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch08/216024097/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch08/216024097/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch08/216024097/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch08/216024097/fresh-pixels/run.log)
- [historical/diff_s39.json](../../campaign/batch08/216024097/historical/diff_s39.json)
- [historical/diff_s39.png](../../campaign/batch08/216024097/historical/diff_s39.png)
- [historical/gaia.json](../../campaign/batch08/216024097/historical/gaia.json)
- [measurements.json](../../campaign/batch08/216024097/measurements.json)
- [phase-review.png](../../campaign/batch08/216024097/phase-review.png)
- [raw-events.png](../../campaign/batch08/216024097/raw-events.png)
- [raw-windows.csv](../../campaign/batch08/216024097/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch08/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
