# TIC 334608511: CONFIRMED

Full bounded physical review: **COMPLETE**. Twenty-two repeated narrow V-shaped eclipses and unequal eccentric secondary near0.54790. Deficit is near target; capable51.33arcsec neighbor is separated from deficit core. Bright field source shifts overall field light; whole-field PSF residual is descriptive.

Raw morphology was inspected in [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/raw-events.png) and [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/phase-review.png), including P and2P parity views. 22 free-center trapezoid timings survive finite, identifiable center-covariance checks. Quality-zero raw QLP SAP_FLUX was used; predictions only guide fitting windows. This is representative available evidence, not an all-event/all-sector census.

Measured same-kind eclipse ephemeris: P=2.59575932638 +/- 0.00000455178 d; reference BTJD=1741.53103860. Epoch kind: Deeper primary eclipse, established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced timing chi-square=0.23274659979143536; zero degrees of freedom would be null. All selected timings follow the named repeating eclipse family. Epoch kind above identifies the deeper primary only where an unequal secondary is established. Model depth is the realized central loss d*min(1,w/(2*k)); extrapolated amplitude and ingress are retained separately. The reference is the fitted first selected cycle, not a Gaia prediction. Within-sector cycle recurrence and parity depths are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/alias-audit.json). Opposite-phase sampled coverage, quality-zero core/sideband counts and flagged counts are in [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/half-period-coverage.json). For138080650, orbital cycles are half the even historical SAP cycles; excluded odd-cycle secondaries remain in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/measurements.json). Unequal observed secondary depths exclude mixing eclipse kinds into P/2 where established; TIC138854818 instead has sampled opposite-phase coverage without a comparable11ppt primary; the P/2 and2P raw views were inspected. No exhaustive blind alias search is asserted.

Narrow shallower secondary visible in raw pooled windows. Depth is the realized center deficit of the fitted shape, with its amplitude parameter retained separately in the JSON. Measured pooled secondary phase=0.5478983, formal phase covariance error=0.00017364; depth=18.366 ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Search-guide provenance: Gaia conjunction search guide, adjusted from raw phase morphology for435209690 and58825156. Final phase is a free-center fit to observed raw flux..

Fresh difference image: sector56, 10 complete core/sideband events. Target pixel=[7.001818234095108, 7.791746622719696]; deficit centroid=[6.662260698458553, 7.90808961222017]; deficit-target distance=0.3589 pixel. Deficit-light offset=13.255 arcsec is a descriptive field-light displacement, not an arbitrary veto. Fractional PSF-model residual=0.5150 is not a calibrated localization uncertainty. Every flux-capable Gaia source in the60-arcsec list was inspected against the image. Attribution conclusion: Twenty-two repeated narrow V-shaped eclipses and unequal eccentric secondary near0.54790. Deficit is near target; capable51.33arcsec neighbor is separated from deficit core. Bright field source shifts overall field light; whole-field PSF residual is descriptive.

| Capable Gaia source | Separation arcsec | G | Intrinsic required eclipse proxy | Pixel coordinate | Diluted loss at pixel |
|---|---:|---:|---:|---|---:|
| 2203352174579254016 | 51.330 | 13.995 | 0.6676 | [8.337374232597103, 5.624844474329464] | 0.007768325820668174 |

The pairwise G-band required intrinsic loss is an approximate brightness screen, with passband, aperture and blend assumptions. It cannot be directly compared to the diluted fractional loss in a pixel. Noncapable neighbors and all coordinates remain in [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/fresh-pixels/diff_fresh.json) and gaia.json. TESS resolution does not exclude unlisted unresolved companions.

Alternative reduction: fresh background-subtracted TESScut1x1/3x3/5x5 target apertures have depths 118.830/112.145/91.764 ppt versus fitted raw QLP median141.395 ppt. Individual cutout event depths are retained in the pixel JSON. Cutout sector is a distinct observing occasion on the same TESS instrument relative to retained QLP sectors. This alternative reduction shares the FFI photons of that sector; no same-sector QLP comparison claimed. Distinct sectors are observing occasions on one instrument. Aperture/depth differences reflect dilution, background and extraction response; no intrinsic depth inferred.

Gaia DR3 source2203352243298726912: P=2.59568478 +/-0.00015863 d, e=0.129273, omega=284.67670 degrees, periastron BTJD=388.0359118. Closest edge-on conjunction offset=-0.018830 d (-0.007254 phase), source-specific full-covariance linear uncertainty=0.080700 d. Full correlation ordering P,gamma,K,e,omega,Tp, selected indices0,3,4,5. This linear approximation is descriptive, not a sigma veto. Both conjunctions and near-reference projection are retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/gaia-geometry.json). Mass function=0.0572205 solar masses, assumed M1=1.75, minimum M2=0.70039; approximate central duration=5.556 h versus observed3.456 h. TIC radius and main-sequence companion scaling are assumptions, not a geometry fit; impact parameter and stellar evolution affect duration. Agreement cannot establish ownership among unresolved sources.

| Sector | Same-kind cycle | Measured midpoint BTJD | Formal center error d | Input error d | Depth ppt |
|---|---:|---:|---:|---:|---:|
| 16 | 0 | 1741.52521058 | 0.00030794435 | 0.010416753 | 120.833 |
| 16 | 2 | 1746.71382496 | 0.00016839445 | 0.010416753 | 119.157 |
| 16 | 5 | 1754.50434004 | 0.00027836181 | 0.010416753 | 122.973 |
| 16 | 7 | 1759.69275330 | 0.00046011885 | 0.010416753 | 123.890 |
| 16 | 8 | 1762.29455994 | 0.0002646679 | 0.010416753 | 125.505 |
| 76 | 627 | 3369.07263641 | 0.0002829565 | 0.0011573825 | 137.073 |
| 76 | 628 | 3371.66828502 | 0.0002836135 | 0.0011573825 | 139.278 |
| 76 | 630 | 3376.85968927 | 0.00028324199 | 0.0011573825 | 141.714 |
| 76 | 631 | 3379.45518699 | 0.00022791105 | 0.0011573825 | 141.248 |
| 76 | 632 | 3382.05149735 | 0.00029170389 | 0.0011573825 | 140.104 |
| 76 | 633 | 3384.64727709 | 0.00027322329 | 0.0011573825 | 142.531 |
| 76 | 634 | 3387.24272512 | 0.00026346396 | 0.0011573825 | 142.595 |
| 76 | 635 | 3389.83839201 | 0.00028862973 | 0.0011573825 | 144.844 |
| 76 | 636 | 3392.43415991 | 0.00027730629 | 0.0011573825 | 140.217 |
| 85 | 721 | 3613.07328881 | 0.00034635021 | 0.0011573807 | 144.257 |
| 85 | 722 | 3615.66889466 | 0.00027313689 | 0.0011573807 | 142.000 |
| 85 | 723 | 3618.26432332 | 0.00022790018 | 0.0011573807 | 142.042 |
| 85 | 724 | 3620.86012557 | 0.00019450237 | 0.0011573807 | 141.541 |
| 85 | 726 | 3626.05290437 | 0.00030272713 | 0.0011573807 | 141.865 |
| 85 | 727 | 3628.64799536 | 0.00025530399 | 0.0011573807 | 142.111 |
| 85 | 728 | 3631.24305151 | 0.00021575833 | 0.0011573807 | 140.212 |
| 85 | 729 | 3633.83923152 | 0.00021016811 | 0.0011573807 | 142.893 |

Next check: Optional resolved photometry and spectroscopy to refine physical parameters.

Catalogue status is separate from physical verdict; shared-catalogues/coverage-matrix.csv retains the seven scoped groups. Known recoveries are not new additions; no exhaustive priority claim. Sources and identity are checked in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/source-hashes.json). Numeric artifacts, original receipts and outputs are frozen in [../SHA256SUMS.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/SHA256SUMS.json); independent helper review is [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/helper-audit.md).


Stable review key: R625.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/fresh-pixels/run.log)
- [historical/diff_s56.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/historical/diff_s56.json)
- [historical/diff_s56.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/historical/diff_s56.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/334608511/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch09/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
