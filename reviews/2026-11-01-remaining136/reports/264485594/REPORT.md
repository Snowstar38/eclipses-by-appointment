# TIC 264485594: CONFIRMED

Full bounded physical review: **COMPLETE**. Eight repeated shallow narrow raw eclipses. Target-centered compact deficit; no capable Gaia neighbor within60 arcsec. No secure secondary; baseline variability limits null claims.

Raw morphology was inspected in [raw-events.png](../../campaign/batch08/264485594/raw-events.png) and [phase-review.png](../../campaign/batch08/264485594/phase-review.png), including P and2P parity views. 8 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=7.16852563280 +/- 0.00000747651 d; reference BTJD=2175.42873529. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.8411913338457286; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

No secure secondary established; numeric fit is a noise/variability description and not a detection or clean null. A fitted low-amplitude pooled model is not evidence of a secondary; flagged and missing coverage are not clean nulls.

Fresh difference image: sector32, 4 complete core/sideband events. Target pixel=[7.46745656519853, 7.721797050156404]; deficit centroid=[7.291515509702744, 7.773924964148958]; deficit-target distance=0.1835 pixel. Deficit-light offset=0.710 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.6040 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Eight repeated shallow narrow raw eclipses. Target-centered compact deficit; no capable Gaia neighbor within60 arcsec. No secure secondary; baseline variability limits null claims.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| None | | | | | |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch08/264485594/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 7.308/7.712/7.995 ppt versus fitted raw QLP median7.816 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source3221888168273909504: P=7.16843382 +/-0.00079101 d, e=0.021215, omega=335.07134 degrees, periastron BTJD=388.2593960. Closest edge-on conjunction offset=-0.014988 d (-0.002091 phase), source-specific full-covariance linear uncertainty=0.216307 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch08/gaia-geometry.json). Mass function=0.0845136 solar masses, assumed M1=1.15, minimum M2=0.64917; approximate central duration=6.946 h versus observed2.057 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 32 | 98 | 2175.43005655 | 0.0012765529 | 0.0034722772 | 8.682 |
| 32 | 99 | 2182.59124170 | 0.0025098289 | 0.0034722772 | 7.549 |
| 32 | 100 | 2189.76810597 | 0.0017068417 | 0.0034722772 | 8.075 |
| 32 | 101 | 2196.93677509 | 0.0015216421 | 0.0034722772 | 6.845 |
| 98 | 352 | 3996.23401385 | 0.0014396463 | 0.0014396463 | 8.160 |
| 98 | 354 | 4010.57054420 | 0.0014119509 | 0.0014119509 | 8.373 |
| 98 | 356 | 4024.90980810 | 0.0018400058 | 0.0018400058 | 7.557 |
| 98 | 358 | 4039.24556011 | 0.0017613392 | 0.0017613392 | 7.346 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch08/identity-check.json) and [../source-hashes.json](../../campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch08/helper-audit.md).


Stable review key: R615.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch08/264485594/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch08/264485594/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch08/264485594/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch08/264485594/fresh-pixels/run.log)
- [historical/diff_s32.json](../../campaign/batch08/264485594/historical/diff_s32.json)
- [historical/diff_s32.png](../../campaign/batch08/264485594/historical/diff_s32.png)
- [historical/gaia.json](../../campaign/batch08/264485594/historical/gaia.json)
- [measurements.json](../../campaign/batch08/264485594/measurements.json)
- [phase-review.png](../../campaign/batch08/264485594/phase-review.png)
- [raw-events.png](../../campaign/batch08/264485594/raw-events.png)
- [raw-windows.csv](../../campaign/batch08/264485594/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch08/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
