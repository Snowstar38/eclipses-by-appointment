# H086 — TIC 146516744

Physical verdict: **REFUTED** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 2974839282884152704 (SB1) has spectroscopic period 31.451951 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 5 [1438.12, 1463.45], 32 [2174.29, 2199.97], 98 [3995.27, 4045.86]. The screening windows are predictions, not event centers.

## Deciding raw evidence

The sector-32 +3.7 ppt selected core is driven by a few cadences around BTJD 2199.83–2199.88 at the sector endpoint. The first three positive cadences reach about +18, +15 and +10 ppt, while SAP_BKG climbs from 1688 to 2514 counts and then 9828 by BTJD 2199.931 (versus 81 counts at 2199.779). SAP_Y shifts about 0.025 pixel at onset. The TESSCut peak-minus-pre positive-pixel moment is (5.77,3.24), 2.74 pixels from the target WCS (5.61,5.98); the nearest-pixel-centered target 3×3 gains only +1.7 counts while pixels outside target 5×5 gain +94.7 counts.

Selected-window measurements: s32 BTJD 2199.855, brightening, core +3.7 ppt, pre/post +1.0 ppt, max gap 0.014 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods. For the deciding pixel check, `tesscut-receipt.json` binds the fetched cutout and `pixel-difference.json`/`.png` give the target WCS, exact frame intervals, nearest-integer-centered apertures and unregistered image difference. This is a same-sector reduction, not an independent observing occasion.

## Limits and next check

The selected target brightening is refuted by off-target positive flux plus concurrent background/position disturbance. The image moment is descriptive, not a fitted PSF position. An unmodeled target flare coincident with contamination cannot be excluded absolutely, and this says nothing about weaker separate binary signals. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Only revisit with registered source-resolved pixels or an independent target-localized repeat.

## Provenance

The frozen packet at `../../source-packets/146516744/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
