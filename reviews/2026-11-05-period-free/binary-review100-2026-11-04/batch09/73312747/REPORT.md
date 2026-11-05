# H090 — TIC 73312747

Physical verdict: **UNRESOLVED** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 1083946670591127808 (SB1) has spectroscopic period 48.368456 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 20 [1842.79, 1868.77], 47 [2580.48, 2606.90], 60 [2938.29, 2962.56], 74 [3312.97, 3339.57]. The screening windows are predictions, not event centers.

## Deciding raw evidence

Sector 20 has a +3.6 ppt sharp impulse at BTJD 1862.18; sector 47 has a smaller +2.2 ppt bump at BTJD 2590.23 while its baseline rises by +5.1 ppt across the window. Other sectors show large secular trends rather than clean events.

Selected-window measurements: s20 BTJD 1862.182, brightening, core +3.6 ppt, pre/post +0.2 ppt, max gap 0.042 d; s47 BTJD 2590.230, brightening, core +2.2 ppt, pre/post +5.1 ppt, max gap 0.021 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods.

## Limits and next check

The two spikes need not be the same phenomenon or source. Neither is an eclipse and the long separation does not yield a measured recurrence period. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Localize each impulse with image-level photometry before classifying them as stellar flares.

## Provenance

The frozen packet at `../../source-packets/73312747/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
