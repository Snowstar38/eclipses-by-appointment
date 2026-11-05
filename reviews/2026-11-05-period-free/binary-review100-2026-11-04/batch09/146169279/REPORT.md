# H088 — TIC 146169279

Physical verdict: **UNRESOLVED** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 5368027530167193856 (SB1) has spectroscopic period 34.901746 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 9 [1544.56, 1568.41], 10 [1571.72, 1595.64], 36 [2282.72, 2305.56], 63 [3014.48, 3039.18], 90 [3747.40, 3774.93], 99 [4046.42, 4070.73], 100 [4074.58, 4098.25]. The screening windows are predictions, not event centers.

## Deciding raw evidence

The sector-90 +3.9 ppt broad mound at BTJD 3759.39 is cut by a 1.005 d internal gap; its raw background median shifts by about 2147 counts relative to local sides. Sector 99 instead shows a segment level reset and sector 100 no corresponding event.

Selected-window measurements: s90 BTJD 3759.385, brightening, core +3.9 ppt, pre/post -0.7 ppt, max gap 1.005 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods.

## Limits and next check

The gap hides part of the event, while the background change raises contamination as an alternative. Neither establishes that the pre-gap mound is instrumental. Its source and physical class remain insecure; no repeat period or eclipse interpretation is supported. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Resolve the sector-90 mound with pixel photometry or an independent well-covered recurrence.

## Provenance

The frozen packet at `../../source-packets/146169279/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
