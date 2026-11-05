# T079: TIC 150429807

Physical verdict **PROBABLE**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 5478130253750687872 (SB2).

## Raw evidence and timing

39 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 47 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

Selected A minima give P = **44.383604 d**, epoch BTJD **1355.244383**, and median selected raw trapezoid depth **262.0 ppt**. The tabulated +/-0.000036 d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.

| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |
|---:|---:|---:|---:|---:|
| 2 | 1355.244653 | 0 | 263.5 | +0.0003 |
| 6 | 1488.395257 | 3 | 256.4 | +0.0001 |
| 10 | 1577.162984 | 5 | 257.4 | +0.0006 |
| 11 | 1621.546480 | 6 | 259.4 | +0.0005 |
| 28 | 2065.382364 | 16 | 274.8 | +0.0003 |
| 29 | 2109.765451 | 17 | 267.3 | -0.0002 |
| 32 | 2198.532641 | 19 | 253.1 | -0.0002 |
| 36 | 2287.299927 | 21 | 264.7 | -0.0001 |
| 37 | 2331.683874 | 22 | 263.0 | +0.0002 |
| 62 | 2997.437719 | 37 | 261.9 | -0.0000 |
| 64 | 3041.821248 | 38 | 262.0 | -0.0001 |
| 67 | 3130.588605 | 40 | 263.8 | +0.0001 |
| 88 | 3707.575524 | 53 | 262.5 | +0.0001 |
| 90 | 3751.958989 | 54 | 262.0 | -0.0000 |
| 95 | 3885.109865 | 57 | 239.9 | +0.0000 |
| 96 | 3929.493327 | 58 | 239.6 | -0.0001 |

## Gaia orbit and aliases

Gaia NSS reports P = 44.432572524 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the measured selected epoch, the nearest nominal conjunction is offset -1.140 d with 0.376 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The comparable photometric period (selected P) is 44.383604 d; difference from Gaia is -3.2 Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.

## Source and alternative extraction

Independent TESSCut sector 6 raw-pixel extraction measured a **242.5 ppt** target-centered 3x3 aperture loss, with positive target-pixel median 8357.2 counts and positive corrected baseline 18914.6 counts. The difference peak is 0.16 pixel from the WCS target position; 55 valid positive sky pixels were used and 0 median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.

The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.

## Coverage, status and next check

Current TESSCut footprint returned 43 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: Many target-centered eclipses fix the photometric clock; Gaia SB2 period and conjunction are in tension at formal precision.
Next check: Obtain independent RVs or updated Gaia orbit, preserving the measured eclipse clock.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 3b38933a6ca97ac28e0b6e9684ad89cf1bac5a777eb6a6f856368e4dee436120.
- Bulk detector result: `[local-path-redacted]`; SHA256 b47fecffeb33b224389de41d1a2e563c89441fbf211d9ff2c002f51f28226d42.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
