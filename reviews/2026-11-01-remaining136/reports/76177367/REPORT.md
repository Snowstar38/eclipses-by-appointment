# TIC 76177367: CONFIRMED

Full bounded physical review: **COMPLETE**. Six narrow raw eclipses and another eclipse near phase0.5930; two capable neighbors at35 and57 arcsec lie away from the deficit. Very bright field light shifts the full-light centroid and dilutes aperture photometry; the compact lost flux remains near target. No deeper-primary assignment is claimed; baseline/extraction differences limit the depth comparison.

Raw morphology was inspected in [raw-events.png](../../campaign/batch08/76177367/raw-events.png) and [phase-review.png](../../campaign/batch08/76177367/phase-review.png), including P and2P parity views. 6 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=13.26495765588 +/- 0.00002177053 d; reference BTJD=1527.46272784. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.41562881010383534; zero degrees of freedom would be null. All selected timings follow the selected repeating eclipse family. The epoch is conventional and does not assert that this is the deeper primary; pooled alternate-event depths may differ with baseline/extraction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch08/alias-audit.json). Unequal secondary depths exclude mixing eclipse kinds into P/2; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Measured secondary-like narrow feature; pooled shape and baseline systematics limit precision. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.5930130, formal phase covariance error=0.0001232; depth=16.216 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Raw full-phase visual estimate.

Fresh difference image: sector8, 2 complete core/sideband events. Target pixel=[7.563215722630424, 7.651744180695784]; deficit centroid=[7.598339832431389, 7.769204946763786]; deficit-target distance=0.1226 pixel. Deficit-light offset=5.692 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.8641 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Six narrow raw eclipses and another eclipse near phase0.5930; two capable neighbors at35 and57 arcsec lie away from the deficit. Very bright field light shifts the full-light centroid and dilutes aperture photometry; the compact lost flux remains near target. No deeper-primary assignment is claimed; baseline/extraction differences limit the depth comparison.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 5424386262828551552 | 35.233 | 16.426 | 0.8077 | [9.082740538577367, 8.750204087613891] | 0.0059154210284210204 |
| 5424385884870330496 | 57.334 | 14.917 | 0.2177 | [9.321208969503672, 10.13745805945126] | 0.001694577936812823 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch08/76177367/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 16.949/15.181/9.312 ppt versus fitted raw QLP median21.935 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source5424386228467707136: P=13.26088266 +/-0.00263410 d, e=0.113680, omega=212.70463 degrees, periastron BTJD=385.1635715. Closest edge-on conjunction offset=0.138052 d (0.010410 phase), source-specific full-covariance linear uncertainty=0.278416 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch08/gaia-geometry.json). Mass function=0.134944 solar masses, assumed M1=1.66, minimum M2=0.97968; approximate central duration=7.727 h versus observed4.282 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 8 | 0 | 1527.46328093 | 0.0012865388 | 0.010416905 | 18.624 |
| 8 | 1 | 1540.73209786 | 0.0013638842 | 0.010416905 | 19.011 |
| 36 | 57 | 2283.56253654 | 0.0011303854 | 0.0034721717 | 23.796 |
| 36 | 58 | 2296.83219227 | 0.0012485756 | 0.0034721717 | 22.155 |
| 89 | 166 | 3729.44631186 | 0.0012700206 | 0.0012700206 | 21.715 |
| 89 | 167 | 3742.70980708 | 0.0015471833 | 0.0015471833 | 22.572 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch08/identity-check.json) and [../source-hashes.json](../../campaign/batch08/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch08/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch08/helper-audit.md).


Stable review key: R612.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch08/76177367/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch08/76177367/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch08/76177367/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch08/76177367/fresh-pixels/run.log)
- [historical/diff_s08.json](../../campaign/batch08/76177367/historical/diff_s08.json)
- [historical/diff_s08.png](../../campaign/batch08/76177367/historical/diff_s08.png)
- [historical/gaia.json](../../campaign/batch08/76177367/historical/gaia.json)
- [measurements.json](../../campaign/batch08/76177367/measurements.json)
- [phase-review.png](../../campaign/batch08/76177367/phase-review.png)
- [raw-events.png](../../campaign/batch08/76177367/raw-events.png)
- [raw-windows.csv](../../campaign/batch08/76177367/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch08/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
