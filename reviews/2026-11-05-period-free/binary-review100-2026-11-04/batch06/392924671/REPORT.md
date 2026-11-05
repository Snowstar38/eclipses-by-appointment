# H060 — TIC 392924671

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 3714017375159903872, SB1, orbital period 24.400960693261304 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 23,50. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

The sector-23 raw SAP trough around BTJD 1934.287 is broad and coincides with continuous SAP_X/Y image-position drift. In the same QLP FITS, KSPSAP_FLUX is flat through the raw trough; that alternate reduction suppresses it. A WCS-located TESSCut aperture also varies strongly with pixel selection and has a large post-gap level change. Terra’s independent difference image between 1933.0–1933.8 and 1934.1–1935.2 shows a signed core/adjacent-pixel dipole rather than uniform PSF dimming (helper-h060-difference.json/png). Together these are positive pixel-redistribution evidence against the selected eclipse. Sector 50 contains no resolved counterpart.

## Limits and next check

Pixel redistribution, centroid drift and the reduction discrepancy support an instrumental origin of the selected trough; a reduction alone can suppress real signals. TESSCut is not a separate observing occasion. Only reconsider on a distinct resolved event in stable photometry. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory. TESSCut receipt, WCS aperture numbers/plot, and the QLP SAP/KSPSAP/background/position comparison are in this target directory. The independent pixel difference is in ../helper-h060-difference.json/png.
