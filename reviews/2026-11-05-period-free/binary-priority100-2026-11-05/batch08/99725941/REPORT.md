# T078: TIC 99725941

Physical verdict **PROBABLE**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 1097717538333601408 (SB2).

## Raw evidence and timing

6 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 7 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

Selected A minima give P = **44.924411 d**, epoch BTJD **2020.307013**, and median selected raw trapezoid depth **200.5 ppt**. The tabulated +/-0.000196 d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.

| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |
|---:|---:|---:|---:|---:|
| 26 | 2020.307631 | 0 | 200.5 | +0.0006 |
| 47 | 2604.324232 | 13 | 198.0 | -0.0001 |
| 74 | 3323.114940 | 29 | 201.4 | +0.0000 |

## Gaia orbit and aliases

Gaia NSS reports P = 44.955850147 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the measured selected epoch, the nearest nominal conjunction is offset -2.027 d with 0.274 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The comparable photometric period (selected P) is 44.924411 d; difference from Gaia is -5.5 Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.

A events at 2020.308, 2604.324 and 3323.115 imply 13 and 16 cycles over the two intervals; B events at 2032.716, 2751.508 and 3335.525 recur at a different phase with shallower raw depths (~84-86 ppt versus A ~198-200 ppt in well sampled sectors). The two consecutive integer spacings and opposite-kind pattern constrain nearby aliases.

Bounded shorter-harmonic checks (`lead-alias-checks.json`) test predicted interleaving same-kind events in actual quality-zero windows, with time-bin core coverage and local side baselines. Representative covered windows (coverage fractions are shown explicitly):

| Alias | Sector | Predicted BTJD | Core time coverage | Core deficit (ppt) |
|---:|---:|---:|---:|---:|
| P/2 | 47 | 2581.862 | 0.90 | +0.0 |
| P/3 | 47 | 2589.350 | 0.90 | +0.0 |

These near-flat windows argue against P/2 and P/3 aliases at the representative sensitivity shown; they are not a calibrated detection probability or an exhaustive integer-alias proof.

## Source and alternative extraction

Independent TESSCut sector 26 raw-pixel extraction measured a **180.7 ppt** target-centered 3x3 aperture loss, with positive target-pixel median 11095.7 counts and positive corrected baseline 52202.3 counts. The difference peak is 0.66 pixel from the WCS target position; 52 valid positive sky pixels were used and 0 median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.

The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.

## Coverage, status and next check

Current TESSCut footprint returned 7 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: Two-kind target-centered eclipses recur, but measured period and Gaia SB2 conjunction disagree beyond formal errors.
Next check: Time further eclipses and reconcile the Gaia spectroscopy.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 dd8a95ca0024de7cdd5fbab6b92d1710c5c2c9317442d1c11f01cd048178df6e.
- Bulk detector result: `[local-path-redacted]`; SHA256 a2ae0a5f8ca312f168746535f3528d595ba58ae8fe70503b790a7f1c1e46e400.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
