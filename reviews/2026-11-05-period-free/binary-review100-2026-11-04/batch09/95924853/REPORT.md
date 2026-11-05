# H081 — TIC 95924853

Physical verdict: **NON_ECLIPSE_VARIABLE** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 5922002715631296512 (SB1) has spectroscopic period 25.028722 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 39 [2361.88, 2386.81], 66 [3097.71, 3121.44], 103 [4152.91, 4177.33], 104 [4179.05, 4204.30]. The screening windows are predictions, not event centers.

## Deciding raw evidence

Sector 39 contains four rounded brightenings around BTJD 2363–2372; two selected cores are +8.4 and +7.6 ppt. A 2.743 d diagnostic peak describes this short modulation. Sector 66 has a much larger broad excursion with data gaps, while sectors 103–104 have unstable raw scales. No detached eclipse shape or secure cross-sector period emerges.

Selected-window measurements: s39 BTJD 2368.953, brightening, core +8.4 ppt, pre/post +1.0 ppt, max gap 0.347 d; s39 BTJD 2366.245, brightening, core +7.6 ppt, pre/post -0.6 ppt, max gap 0.042 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods.

## Limits and next check

Short-sector modulation is evident in SAP; physical class and exact source remain unresolved. Corrected-flux suppression and centroid shifts alone do not localize it. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Independent aperture and difference imaging if the modulation is pursued.

## Provenance

The frozen packet at `../../source-packets/95924853/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
