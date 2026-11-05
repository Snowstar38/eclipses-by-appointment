# H084 — TIC 43868028

Physical verdict: **UNRESOLVED** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 3208563496094554240 (SB1) has spectroscopic period 54.197983 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 5 [1438.27, 1463.35], 32 [2174.32, 2199.50], 98 [3995.18, 4045.86]. The screening windows are predictions, not event centers.

## Deciding raw evidence

The sector-5 selected +4.1 ppt window lies on a monotonic rise (pre/post step +9.7 ppt), and the same curved sector-scale ramp appears in sector 32. Sector 98 has a separate sharp +20.0 ppt impulse followed by decay and an underlying drifting baseline. The 10.58–10.60 d diagnostic peaks in sectors 5/32 can reflect repeated instrumental or astrophysical shape. TESSCut s98 peak-minus-pre pixels show a positive/negative dipole around the WCS target (5.14,5.06), with +61.6 counts in the nearest-pixel-centered 3×3 but only +84 counts across the whole cutout.

Selected-window measurements: s5 BTJD 1462.245, brightening, core +4.1 ppt, pre/post +9.7 ppt, max gap 0.042 d; s98 BTJD 3996.034, brightening, core +20.0 ppt, pre/post -15.4 ppt, max gap 0.229 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods. For the deciding pixel check, `tesscut-receipt.json` binds the fetched cutout and `pixel-difference.json`/`.png` give the target WCS, exact frame intervals, nearest-integer-centered apertures and unregistered image difference. This is a same-sector reduction, not an independent observing occasion.

## Limits and next check

The sector-5 selected window is a slope false alarm. Sector-98 has an insecure transient: its dipole is consistent with pointing or background structure, yet simple unregistered difference imaging does not exclude concurrent stellar brightening. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Registered image modeling or independent photometry of the sector-98 transient and recurring sector-scale ramp.

## Provenance

The frozen packet at `../../source-packets/43868028/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
