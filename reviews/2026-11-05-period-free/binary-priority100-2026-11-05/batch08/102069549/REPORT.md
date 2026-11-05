# T073: TIC 102069549

Physical verdict **PROBABLE**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 4933562966514402176 (SB2).

## Raw evidence and timing

6 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 8 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

Selected B minima give P = **24.592168 d**, epoch BTJD **1374.087198**, and median selected raw trapezoid depth **169.3 ppt**. The tabulated +/-0.000080 d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.

| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |
|---:|---:|---:|---:|---:|
| 2 | 1374.088616 | 0 | 190.2 | +0.0014 |
| 96 | 3931.672497 | 104 | 152.3 | -0.0002 |
| 104 | 4202.186694 | 115 | 169.3 | +0.0002 |

## Gaia orbit and aliases

Gaia NSS reports P = 24.600491462 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the measured selected epoch, the nearest nominal conjunction is offset -0.205 d with 0.050 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The comparable photometric period (selected P) is 24.592168 d; difference from Gaia is -11.1 Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.

The s2 deep A and shallow B events are different eclipse kinds. The s96 A is partly lost in a gap; B in s2, s96 and s104 supplies the 104+11-cycle clock. The shallow s96/s104 non-eclipse flags were not used as timing points.

The 104- and 11-cycle B spacings jointly constrain nearby integer counts. Assigning 10 or 12 cycles to the s96-to-s104 interval gives ~27.051 or ~22.543 d, neither of which gives an integer count for the earlier s2-to-s96 B interval.

Bounded shorter-harmonic checks (`lead-alias-checks.json`) test predicted interleaving same-kind events in actual quality-zero windows, with time-bin core coverage and local side baselines. Representative covered windows (coverage fractions are shown explicitly):

| Alias | Sector | Predicted BTJD | Core time coverage | Core deficit (ppt) |
|---:|---:|---:|---:|---:|
| P/2 | 96 | 3919.377 | 1.00 | -0.0 |
| P/3 | 96 | 3923.475 | 1.00 | -0.3 |

These near-flat windows argue against P/2 and P/3 aliases at the representative sensitivity shown; they are not a calibrated detection probability or an exhaustive integer-alias proof.

## Source and alternative extraction

Independent TESSCut sector 2 raw-pixel extraction measured a **421.4 ppt** target-centered 3x3 aperture loss, with positive target-pixel median 21100.9 counts and positive corrected baseline 79982.8 counts. The difference peak is 0.46 pixel from the WCS target position; 51 valid positive sky pixels were used and 0 median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.

The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.

## Coverage, status and next check

Current TESSCut footprint returned 8 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: Target-centered repeated eclipses; photometric period and Gaia SB2 orbit disagree beyond their formal errors, leaving orbital association unresolved.
Next check: Obtain new eclipse timing and spectroscopy to test the Gaia SB2 association.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 e6d2fbc2ae092302d9b4915b71b9d90500feecdc179f1598b16b7e909a59fc8c.
- Bulk detector result: `[local-path-redacted]`; SHA256 4b166de371471a4d33f9811dfd750bc60d9b9fe062737c417bc6f5a901be0c07.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
