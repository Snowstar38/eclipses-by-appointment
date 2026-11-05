# T071: TIC 91548233

Physical verdict **PLAUSIBLE**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 887897592669930752 (SB1).

## Raw evidence and timing

6 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 1 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

No reliable same-kind repeated eclipse times or orbital period follow from the retained feature. `lead-single-context.png` compares the actual Gaia-period windows in SAP, alternative flux and background; `lead-fold-coverage.json` records time-bin coverage rather than row counts.

## Gaia orbit and aliases

Gaia NSS reports P = 45.121633286 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the screening time, the nearest nominal conjunction is offset -1.383 d with 1.225 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

The sector-45 0.4-ppt selected core lies immediately before a ~1% brightening; the sector-71 predicted window falls on a broad SAP/background drift removed by KSPSAP. The sector-20 window has no compelling matching eclipse. No positive instrumental cause has been established for the tiny sector-45 feature, so the physical interpretation remains plausible rather than refuted.

## Source and alternative reduction

The event morphology was assessed against available QLP processed flux, background and other raw-sector windows in `lead-single-context.png`. A decisive eclipse source was not established, so no target-host claim is made.

## Coverage, status and next check

Current TESSCut footprint returned 7 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

The availability API also returned `tess-s1751-3-2`, an anomalous sector identifier outside the validated TESS sequence; it was not treated as new sensitive coverage.

Limitation: One shallow selected feature is embedded beside a much larger brightening; no secure repeat or eclipse midpoint.
Next check: Acquire a target-resolved light curve of a future narrow event and establish recurrence.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 83c45c375fcaa0d357b1336894197e8c4c670657e3826cebc836a7fe3b0f0f85.
- Bulk detector result: `[local-path-redacted]`; SHA256 0b017867333e7494b13e9d73439a77e0f5d2066270b9df6e7833dd05a65e0000.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
