# H082 — TIC 155173365

Physical verdict: **UNRESOLVED** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 1936432670225676288 (SB1) has spectroscopic period 50.257365 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 16 [1739.18, 1759.74], 17 [1766.18, 1787.87], 57 [2853.41, 2882.06], 83 [3559.44, 3584.34], 84 [3584.63, 3610.29]. The screening windows are predictions, not event centers.

## Deciding raw evidence

The sector-84 selected +3.0 ppt core is a short rise and decay near BTJD 3605.25, superposed on a large sector trend and post-gap level changes. Other sectors have broad drifts, with no matching discrete positive occasion.

Selected-window measurements: s84 BTJD 3605.248, brightening, core +3.0 ppt, pre/post +3.7 ppt, max gap 0.002 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods.

## Limits and next check

A flare-like positive event is present in SAP, but its source and whether it is stellar are insecure. No eclipse period is measured. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Inspect pixel-level difference image and nearby light curves for the sector-84 impulse.

## Provenance

The frozen packet at `../../source-packets/155173365/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
