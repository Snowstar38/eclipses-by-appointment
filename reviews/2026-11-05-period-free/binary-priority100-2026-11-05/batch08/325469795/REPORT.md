# T076: TIC 325469795

Physical verdict **PROBABLE**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 6350855788547394304 (SB2).

## Raw evidence and timing

7 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 12 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

Selected A minima give P = **26.459431 d**, epoch BTJD **1346.120893**, and median selected raw trapezoid depth **345.6 ppt**. The tabulated +/-0.000043 d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.

| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |
|---:|---:|---:|---:|---:|
| 1 | 1346.120891 | 0 | 347.1 | -0.0000 |
| 13 | 1663.633508 | 12 | 345.1 | -0.0006 |
| 67 | 3145.362214 | 68 | 360.3 | +0.0000 |
| 93 | 3833.307393 | 94 | 346.2 | +0.0000 |
| 94 | 3859.766729 | 95 | 312.0 | -0.0001 |
| 95 | 3886.226330 | 96 | 292.0 | +0.0001 |

## Gaia orbit and aliases

Gaia NSS reports P = 26.491788040 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the measured selected epoch, the nearest nominal conjunction is offset -0.799 d with 0.096 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The comparable photometric period (selected P) is 26.459431 d; difference from Gaia is -11.9 Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.

Adjacent deep A events in sectors 93, 94 and 95 at BTJD 3833.307, 3859.767 and 3886.226 secure the 26.459-d same-kind interval. Shallower B events near BTJD 1328.660, 1672.633 and 3127.901 occupy a different phase; they are not counted as A minima.

Bounded shorter-harmonic checks (`lead-alias-checks.json`) test predicted interleaving same-kind events in actual quality-zero windows, with time-bin core coverage and local side baselines. Representative covered windows (coverage fractions are shown explicitly):

| Alias | Sector | Predicted BTJD | Core time coverage | Core deficit (ppt) |
|---:|---:|---:|---:|---:|
| P/2 | 93 | 3846.537 | 1.00 | -0.1 |
| P/3 | 93 | 3850.947 | 1.00 | -0.1 |

These near-flat windows argue against P/2 and P/3 aliases at the representative sensitivity shown; they are not a calibrated detection probability or an exhaustive integer-alias proof.

## Source and alternative extraction

Independent TESSCut sector 27 raw-pixel extraction measured a **258.1 ppt** target-centered 3x3 aperture loss, with positive target-pixel median 6369.0 counts and positive corrected baseline 17613.3 counts. The difference peak is 0.37 pixel from the WCS target position; 53 valid positive sky pixels were used and 0 median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.

The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.

## Coverage, status and next check

Current TESSCut footprint returned 8 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: Deep same-kind eclipses establish a clock, but Gaia SB2 period and conjunction differ beyond formal errors.
Next check: Obtain spectroscopy and new minima to determine whether the eclipses share the Gaia SB2 orbit.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 6a12e8d59f5c4af4e88f08da5440d56119d57fc4910520739fa2bf6d21223988.
- Bulk detector result: `[local-path-redacted]`; SHA256 8f033c3447d677b3531242689d92ae2d9ae3d69da5355e247b2139b3bea09b45.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
