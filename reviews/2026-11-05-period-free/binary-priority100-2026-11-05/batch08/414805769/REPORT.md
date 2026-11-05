# T077: TIC 414805769

Physical verdict **PROBABLE**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 2780911442064038144 (SB2).

## Raw evidence and timing

4 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 9 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

Selected A minima give P = **14.291385 d**, epoch BTJD **2469.622046**, and median selected raw trapezoid depth **332.1 ppt**. The tabulated +/-0.000129 d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.

| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |
|---:|---:|---:|---:|---:|
| 42 | 2469.622041 | 0 | 297.3 | -0.0000 |
| 57 | 2855.489449 | 27 | 332.1 | +0.0000 |
| 57 | 2869.780807 | 28 | 332.6 | -0.0000 |

## Gaia orbit and aliases

Gaia NSS reports P = 28.557001460 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the measured selected epoch, the nearest nominal conjunction is offset -4.768 d with 0.279 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The comparable photometric period (2x selected P) is 28.582770 d; difference from Gaia is +6.2 Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.

Two deep sector-57 A minima are only 14.291 d apart; shallower B minima recur with the same separation, ~6.17 d displaced. Thus the Gaia 28.557 d orbit cannot be assigned to the eclipses merely by calling it a harmonic. A second orbit, Gaia solution error or an incorrect alias remains open.

## Source and alternative extraction

Independent TESSCut sector 57 raw-pixel extraction measured a **304.7 ppt** target-centered 3x3 aperture loss, with positive target-pixel median 6517.3 counts and positive corrected baseline 31528.1 counts. The difference peak is 0.70 pixel from the WCS target position; 49 valid positive sky pixels were used and 0 median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.

The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.

## Coverage, status and next check

Current TESSCut footprint returned 5 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: Deep eclipses repeat at 14.291 d, nearly half Gaia 28.557 d, but twice the measured period and conjunction disagree with the Gaia formal orbit; a harmonic is unproven.
Next check: Obtain independent spectroscopy and resolved imaging to identify the eclipsing orbit.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 61e203a499181052fa5dff1593cab295b420dcab36e70426855988e49d23fd7f.
- Bulk detector result: `[local-path-redacted]`; SHA256 941d8828da569ff4d57f64db7be18b5cebdc09d75c08071b295ce9ed87069086.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
