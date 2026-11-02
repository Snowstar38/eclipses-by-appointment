# TIC 93862657: CONFIRMED

Full bounded physical review: **COMPLETE**. Twelve deep repeated raw eclipses and shallower secondary near0.4977. Compact lost flux favors target over capable24.17/48.03arcsec neighbors. Nearby known EB Gaia3041697316497710720 at29.83arcsec has G19.73955 and0.282338d catalog period; its intrinsic-loss proxy74.05 exceeds unity and its period differs from4.80345d. It cannot plausibly make the100ppt target eclipse under this brightness model. Crowding raises whole-field PSF residual; no calibrated localization precision claimed.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/phase-review.png), including P and2P parity views. 12 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=4.80345242294 +/- 0.00000502307 d; reference BTJD=1494.19541099. Epoch kind: Deeper primary eclipse, established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.044408305858084765; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/half-period-coverage.json). For138080650, orbital cycles are half the even historical SAP cycles; excluded odd-cycle secondaries remain in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; TIC138854818 instead has sampled opposite-phase coverage without a comparable11ppt primary; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Narrow shallower secondary visible in raw pooled windows. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.4977257, formal phase covariance error=0.00036205; depth=5.821 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Gaia conjunction search guide, adjusted from raw phase morphology for435209690 and58825156. Final phase is a free-center fit to observed raw flux..

Fresh difference image: sector88, 4 complete core/sideband events. Target pixel=[7.164710660216459, 7.202969317919431]; deficit centroid=[7.250045207399978, 7.244594980093872]; deficit-target distance=0.0949 pixel. Deficit-light offset=4.695 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.7715 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Twelve deep repeated raw eclipses and shallower secondary near0.4977. Compact lost flux favors target over capable24.17/48.03arcsec neighbors. Nearby known EB Gaia3041697316497710720 at29.83arcsec has G19.73955 and0.282338d catalog period; its intrinsic-loss proxy74.05 exceeds unity and its period differs from4.80345d. It cannot plausibly make the100ppt target eclipse under this brightness model. Crowding raises whole-field PSF residual; no calibrated localization precision claimed.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 3041697320797166976 | 24.174 | 14.834 | 0.9065 | [6.239707037601738, 6.315112664808126] | 0.05535194808893887 |
| 3041697355156898688 | 48.030 | 14.754 | 0.8493 | [9.584789177028378, 6.968494324832848] | 0.015637403803996478 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 95.172/88.814/80.060 ppt versus fitted raw QLP median100.078 ppt. Individual cutout event depths are retained in the pixel JSON. Same-sector QLP and cutout extraction share TESS photons and test processing robustness. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source3041697320797163008: P=4.80289401 +/-0.00049369 d, e=0.022247, omega=126.14374 degrees, periastron BTJD=389.8784640. Closest edge-on conjunction offset=0.113738 d (0.023681 phase), source-specific full-covariance linear uncertainty=0.130976 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/gaia-geometry.json). Mass function=0.0170011 solar masses, assumed M1=1.216, minimum M2=0.34619; approximate central duration=4.266 h versus observed3.857 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 7 | 0 | 1494.19621137 | 0.00023147443 | 0.01041666 | 99.924 |
| 7 | 1 | 1499.00231337 | 0.00022773688 | 0.01041666 | 100.233 |
| 7 | 3 | 1508.60796321 | 0.00013453829 | 0.01041666 | 99.596 |
| 7 | 4 | 1513.41043282 | 0.00033842665 | 0.01041666 | 102.922 |
| 61 | 307 | 2968.85502793 | 0.0002520966 | 0.0011573863 | 103.371 |
| 61 | 308 | 2973.65852945 | 0.00029558135 | 0.0011573863 | 105.159 |
| 61 | 309 | 2978.46229288 | 0.00029281513 | 0.0011573863 | 103.412 |
| 61 | 310 | 2983.26580917 | 0.00025892572 | 0.0011573863 | 103.715 |
| 88 | 458 | 3694.17666187 | 0.00027727402 | 0.0011573846 | 99.227 |
| 88 | 459 | 3698.97975723 | 0.00027533348 | 0.0011573846 | 99.110 |
| 88 | 461 | 3708.58719011 | 0.00027445641 | 0.0011573846 | 97.822 |
| 88 | 462 | 3713.39067289 | 0.00021702488 | 0.0011573846 | 99.589 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/helper-audit.md).


Stable review key: R624.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/fresh-pixels/run.log)
- [historical/diff_s88.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/historical/diff_s88.json)
- [historical/diff_s88.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/historical/diff_s88.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/93862657/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
