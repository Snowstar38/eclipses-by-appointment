# T072: TIC 298307278

Physical verdict **REFUTED**; bounded review **COMPLETE**. Catalogue novelty **UNKNOWN**. The fixed queue identity is Gaia DR3 1989111887224781056 (SB1).

## Raw evidence and timing

5 hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained 1 dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.

No reliable same-kind repeated eclipse times or orbital period follow from the retained feature. `lead-single-context.png` compares the actual Gaia-period windows in SAP, alternative flux and background; `lead-fold-coverage.json` records time-bin coverage rather than row counts.

## Gaia orbit and aliases

Gaia NSS reports P = 37.530993749 d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the screening time, the nearest nominal conjunction is offset +7.530 d with 0.897 d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.

Positive refutation of the selected feature: sector-84 SAP varies smoothly through a several-thousand-count background excursion; the selected dip vanishes in DET_FLUX. Sector-16 raw ramp also accompanies a severe background drift and is flat in DET_FLUX. These are direct signal/background and reduction contradictions, rather than a conclusion based on lack of repeats.

## Source and alternative reduction

The event morphology was assessed against available QLP processed flux, background and other raw-sector windows in `lead-single-context.png`. A decisive eclipse source was not established, so no target-host claim is made.

## Coverage, status and next check

Current TESSCut footprint returned 5 sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.

Limitation: The retained sector-84 feature follows a strong background excursion and disappears in the alternative corrected flux; no eclipse clock.
Next check: Revisit only if a new raw event independent of the background transient appears.

## Source receipts

- Queue row: `[local-path-redacted]`; exact source packet `[local-path-redacted]`; SHA256 b6dc5f81defe2a96b0208282761e800b69b320aa48adcb0a25add4693cdb22c7.
- Bulk detector result: `[local-path-redacted]`; SHA256 c8b50d453ce7fb86777215815f4323086029941a9b55cdd13e4ac5285bd23289.
- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.
