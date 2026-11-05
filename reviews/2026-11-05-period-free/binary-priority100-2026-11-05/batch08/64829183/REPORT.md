# T080: TIC 64829183

Physical verdict **PROBABLE**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 2006904218754946048 (SB2).

## Raw evidence and timing

6 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 7 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

Selected A minima give P = **43.141264 d**, epoch BTJD **2881.157743**, and median selected raw trapezoid depth **167.6 ppt**. The tabulated +/-0.000281 d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.

| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |
|---:|---:|---:|---:|---:|
| 57 | 2881.158470 | 0 | 167.6 | +0.0007 |
| 24 | 1975.169779 | -21 | 167.2 | -0.0214 |
| 77 | 3398.852454 | 12 | 170.3 | -0.0005 |

## Gaia orbit and aliases

Gaia NSS reports P = 43.172158051 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the measured selected epoch, the nearest nominal conjunction is offset -1.674 d with 0.192 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The comparable photometric period (selected P) is 43.141264 d; difference from Gaia is -8.7 Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.

The sector-16 A-like event near BTJD 1759.446 is truncated by a gap and excluded from the precision fit; it supplies partial recurrence support only. The selected fit uses sectors 24, 57 and 77. The sector-16/24 shallower B-like events near 1745.410 and 1960.973 support an unequal opposite kind, with sector-84 B near 3600.363. Early 30-min cadence and shape differences keep the stated conditional error from being a total prediction uncertainty.

Bounded shorter-harmonic checks (`lead-alias-checks.json`) test predicted interleaving same-kind events in actual quality-zero windows, with time-bin core coverage and local side baselines. Representative covered windows (coverage fractions are shown explicitly):

| Alias | Sector | Predicted BTJD | Core time coverage | Core deficit (ppt) |
|---:|---:|---:|---:|---:|
| P/2 | 57 | 2859.587 | 1.00 | -0.1 |
| P/2 | 77 | 3420.424 | 1.00 | -0.0 |
| P/3 | 17 | 1773.865 | 0.92 | +0.0 |

These near-flat windows argue against P/2 and P/3 aliases at the representative sensitivity shown; they are not a calibrated detection probability or an exhaustive integer-alias proof.

## Source and alternative extraction

Independent TESSCut sector 16 raw-pixel extraction measured a **95.5 ppt** target-centered 3x3 aperture loss, with positive target-pixel median 25302.2 counts and positive corrected baseline 90056.8 counts. The difference peak is 0.10 pixel from the WCS target position; 54 valid positive sky pixels were used and 0 median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.

The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.

## Coverage, status and next check

Current TESSCut footprint returned 7 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: Repeated target-centered eclipses survive alternate extraction; Gaia SB2 period and conjunction disagree, and early timing is cadence/gap limited.
Next check: Time a complete new eclipse with independent spectroscopy to test the orbit link.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 a45aa94f22c12ea7391d53f2161d44d3deebb293541b76f18c642264055e9c62.
- Bulk detector result: `[local-path-redacted]`; SHA256 b65a0c3a1dd6637c494e8a24fc3247c1b0b0f91351edf9863226cf6c05cea3e7.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
