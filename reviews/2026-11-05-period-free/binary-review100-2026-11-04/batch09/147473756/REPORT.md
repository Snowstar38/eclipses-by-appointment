# H083 — TIC 147473756

Physical verdict: **NON_ECLIPSE_VARIABLE** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 1043537002634418432 (SB2) has spectroscopic period 34.337118 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 20 [1842.81, 1868.56], 47 [2580.33, 2606.88], 60 [2938.31, 2962.56], 74 [3312.98, 3339.54]. The screening windows are predictions, not event centers.

## Deciding raw evidence

Sector 47 selected +5.2 ppt crest is part of a repeated rounded wave. Sector 20 has multiple similar waves; sectors 60 and 74 show broad recurring modulation. Diagnostic peaks are 5.912, 2.910 (harmonic), 6.494 and 5.829 d.

Selected-window measurements: s47 BTJD 2586.834, brightening, core +5.2 ppt, pre/post -1.1 ppt, max gap 0.194 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods.

## Limits and next check

Quasi-periodic non-eclipse modulation is clear; its coherence, physical class and aperture source are not established. The 34.337 d Gaia SB2 orbit is context only. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Source-localized aperture photometry and longer-baseline mode analysis.

## Provenance

The frozen packet at `../../source-packets/147473756/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
