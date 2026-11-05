# H089 — TIC 58171740

Physical verdict: **UNRESOLVED** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 149900032284377856 (SB1) has spectroscopic period 31.561245 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 43 [2474.25, 2498.42], 44 [2500.54, 2524.27], 70 [3208.80, 3232.79]. The screening windows are predictions, not event centers.

## Deciding raw evidence

Sector 44 has a narrow +3.3 ppt symmetric-looking impulse around BTJD 2523.05, on a slow downward baseline. Sectors 43 and 70 show unrelated trends and no matched impulse. Both SAP and KSPSAP contain the local peak.

Selected-window measurements: s44 BTJD 2523.050, brightening, core +3.3 ppt, pre/post -1.1 ppt, max gap 0.014 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods.

## Limits and next check

A real aperture excursion is possible, but its stellar origin and classification are insecure. No eclipse interpretation or period is supported. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Pixel-level source check for the sector-44 impulse.

## Provenance

The frozen packet at `../../source-packets/58171740/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
