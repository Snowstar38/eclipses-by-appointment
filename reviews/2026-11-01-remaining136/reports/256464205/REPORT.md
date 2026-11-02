# TIC 256464205: CONFIRMED

Full bounded physical review: **COMPLETE**. Nine measured narrow repeated eclipses across three sectors. No secure secondary. Both capable Gaia neighbors at28.53/41.16arcsec lie away from compact target deficit. Nearby known EB Gaia6067018781690100608 at43.74arcsec has G18.650408 and0.309493d period versus target7.706608d; intrinsic required-loss proxy exceeds10 and its location is displaced. It cannot plausibly make the target eclipse under the brightness model. Whole-field light offset40.8arcsec reflects crowding, not eclipse localization.

Raw morphology was inspected in [raw-events.png](../../campaign/batch11/256464205/raw-events.png) and [phase-review.png](../../campaign/batch11/256464205/phase-review.png), including P and2P parity views. 9 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=7.70660758985 +/- 0.00000628165 d; reference BTJD=1605.97630895. Epoch kind: Selected repeating narrow eclipse; deeper-primary identity unestablished because no secure secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.8709509226856547; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](../../campaign/batch11/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](../../campaign/batch11/half-period-coverage.json). For265092213, orbital cycles=(historical cycle-1)/2 use deeper odd events; shallower even-cycle secondaries remain in [measurements.json](../../campaign/batch11/256464205/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; systems without secure secondaries retain sampled opposite-phase coverage rather than a claimed clean null; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

No secure secondary; noisy low-amplitude exploratory fit not interpreted as eclipse. A fitted low-amplitude pooled model is not evidence of a secondary; flagged and missing coverage are not clean nulls.

Fresh difference image: sector65, 4 complete core/sideband events. Target pixel=[7.21212923557348, 7.465688916102241]; deficit centroid=[7.16706361275627, 7.431256301760108]; deficit-target distance=0.0567 pixel. Deficit-light offset=40.832 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.9743 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Nine measured narrow repeated eclipses across three sectors. No secure secondary. Both capable Gaia neighbors at28.53/41.16arcsec lie away from compact target deficit. Nearby known EB Gaia6067018781690100608 at43.74arcsec has G18.650408 and0.309493d period versus target7.706608d; intrinsic required-loss proxy exceeds10 and its location is displaced. It cannot plausibly make the target eclipse under the brightness model. Whole-field light offset40.8arcsec reflects crowding, not eclipse localization.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 6067018923439625088 | 28.533 | 14.446 | 0.2489 | [6.130814959063191, 6.553025691538066] | 0.01744809743716953 |
| 6067018751640930304 | 41.164 | 14.723 | 0.3096 | [7.475529642511301, 9.447495172304116] | 0.021543108665424797 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](../../campaign/batch11/256464205/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 34.602/26.610/10.403 ppt versus fitted raw QLP median39.827 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source6067018747329099008: P=7.70553073 +/-0.00138362 d, e=0.029079, omega=318.10385 degrees, periastron BTJD=385.5804366. Closest edge-on conjunction offset=0.152747 d (0.019823 phase), source-specific full-covariance linear uncertainty=0.269646 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](../../campaign/batch11/gaia-geometry.json). Mass function=0.0335501 solar masses, assumed M1=1.2, minimum M2=0.45043; approximate central duration=7.073 h versus observed4.660 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 11 | 0 | 1605.96382449 | 0.00056789322 | 0.010416635 | 37.486 |
| 11 | 2 | 1621.38179176 | 0.00049097598 | 0.010416635 | 38.712 |
| 65 | 190 | 3070.23212690 | 0.0010261945 | 0.0011573928 | 43.794 |
| 65 | 191 | 3077.93725219 | 0.0010391507 | 0.0011573928 | 45.744 |
| 65 | 192 | 3085.64450935 | 0.00099660011 | 0.0011573928 | 42.091 |
| 65 | 193 | 3093.35336767 | 0.0011541044 | 0.0011573928 | 42.647 |
| 102 | 328 | 4133.74414745 | 0.00079484598 | 0.0011574068 | 37.016 |
| 102 | 329 | 4141.44973578 | 0.00066256467 | 0.0011574068 | 36.227 |
| 102 | 330 | 4149.15637792 | 0.00080854852 | 0.0011574068 | 39.827 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](../../campaign/batch11/identity-check.json) and [../source-hashes.json](../../campaign/batch11/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](../../campaign/batch11/SHA256SUMS.json); independent helper review is [../helper-audit.md](../../campaign/batch11/helper-audit.md).


Stable review key: R646.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch11/256464205/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch11/256464205/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch11/256464205/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch11/256464205/fresh-pixels/run.log)
- [historical/diff_s65.json](../../campaign/batch11/256464205/historical/diff_s65.json)
- [historical/diff_s65.png](../../campaign/batch11/256464205/historical/diff_s65.png)
- [historical/gaia.json](../../campaign/batch11/256464205/historical/gaia.json)
- [measurements.json](../../campaign/batch11/256464205/measurements.json)
- [phase-review.png](../../campaign/batch11/256464205/phase-review.png)
- [raw-events.png](../../campaign/batch11/256464205/raw-events.png)
- [raw-windows.csv](../../campaign/batch11/256464205/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch11/256464205/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch11/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
