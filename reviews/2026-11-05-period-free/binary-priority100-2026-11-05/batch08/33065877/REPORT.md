# T075: TIC 33065877

Physical verdict **CONFIRMED**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 2910877118083564416 (SB2).

## Raw evidence and timing

5 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 9 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

Selected A minima give P = **30.092022 d**, epoch BTJD **2182.434898**, and median selected raw trapezoid depth **334.5 ppt**. The tabulated +/-0.000055 d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.

| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |
|---:|---:|---:|---:|---:|
| 32 | 2182.434952 | 0 | 330.2 | +0.0001 |
| 33 | 2212.526865 | 1 | 339.3 | -0.0001 |
| 87 | 3687.036015 | 50 | 334.5 | +0.0000 |

## Gaia orbit and aliases

Gaia NSS reports P = 30.091367448 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the measured selected epoch, the nearest nominal conjunction is offset +0.145 d with 0.324 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The comparable photometric period (selected P) is 30.092022 d; difference from Gaia is +0.1 Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.

The opposite-kind sector-32 B eclipse at BTJD 2194.931 (raw trapezoid ~280 ppt) follows A at 2182.435 (~330 ppt); sector-33 B at 2225.023 (~287 ppt) likewise follows A at 2212.527 (~339 ppt). Both A and B independently recur after 30.092 d, while their unequal depth and ~12.496-d separation reject treating opposite conjunctions as two same-kind repetitions.

## Source and alternative extraction

Independent TESSCut sector 32 raw-pixel extraction measured a **332.1 ppt** target-centered 3x3 aperture loss, with positive target-pixel median 4478.9 counts and positive corrected baseline 20170.3 counts. The difference peak is 0.48 pixel from the WCS target position; 53 valid positive sky pixels were used and 0 median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.

The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.

## Coverage, status and next check

Current TESSCut footprint returned 8 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: Repeated two-kind eclipses are target-centered, reduction-robust and consistent with the Gaia SB2 orbit; catalogue novelty remains unverified.
Next check: Complete the four unavailable VizieR novelty gates before any new-system claim.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 2f8d8e7d90415c3ceaba4248e14b8860699adc093b66e9c7c68581e212f3e737.
- Bulk detector result: `[local-path-redacted]`; SHA256 b7106be9464d9131aa993f50f2e6959e12207e73cc91de0d9c8d8444f48064ec.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
