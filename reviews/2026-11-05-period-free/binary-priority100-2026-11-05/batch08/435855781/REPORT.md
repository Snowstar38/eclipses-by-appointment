# T074: TIC 435855781

Physical verdict **CONFIRMED**; bounded review **COMPLETE**. Catalogue novelty **KNOWN**. The fixed queue identity is Gaia DR3 2801675306837672704 (SB2).

## Raw evidence and timing

3 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 5 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

Selected A minima give P = **22.450616 d**, epoch BTJD **1783.059032**, and median selected raw trapezoid depth **444.4 ppt**. The tabulated +/-0.000047 d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.

| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |
|---:|---:|---:|---:|---:|
| 17 | 1783.058786 | 0 | 444.4 | -0.0002 |
| 57 | 2860.688609 | 48 | 438.4 | +0.0000 |
| 84 | 3601.558927 | 81 | 449.8 | -0.0000 |

## Gaia orbit and aliases

Gaia NSS reports P = 22.443983388 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the measured selected epoch, the nearest nominal conjunction is offset +0.348 d with 0.199 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The comparable photometric period (selected P) is 22.450616 d; difference from Gaia is +2.0 Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.

The earlier comprehensive `Fable 5.1/made/appointments/vet15/REPORT.md` (SHA256 bc3ca1f0fec4e63165b88a4c0f0d114e460b6abb54d350a73813ba4c80aa8e9b) finds A P = 22.450574 +/- 0.000054 d and B P = 22.450619 d, five clean eclipses, TESS-SPOC and TARS agreement, on-target TPF deficits and a joint SB2 model. The present selected raw fit independently agrees within its limitations. This target was already reported as EA/EB by Thiemann et al. (2021), 1SWASP J004527.74+210427.9, with P = 1.66 d. Failed contemporary catalogue gates cannot erase that positive prior identification.

## Source and alternative extraction

Independent TESSCut sector 17 raw-pixel extraction measured a **402.7 ppt** target-centered 3x3 aperture loss, with positive target-pixel median 5581.1 counts and positive corrected baseline 18852.5 counts. The difference peak is 0.43 pixel from the WCS target position; 52 valid positive sky pixels were used and 0 median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.

The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.

## Coverage, status and next check

Current TESSCut footprint returned 3 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: Previously identified as EA/EB in Thiemann et al. 2021 SuperWASP, with erroneous 1.66-day period; this is a period revision, not a new eclipser.
Next check: Update the known-system ephemeris with further timing and cite the prior EA/EB identification.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 2b0aa493c3ad9c9677327c3c9943b0c01d7283640ddef20ecf1827edfcf0ecee.
- Bulk detector result: `[local-path-redacted]`; SHA256 83b07654f277cbac3f9e721f2061ecbd419a40742914017a92e5e58760be825a.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
