# H085 — TIC 52152553

Physical verdict: **NON_ECLIPSE_VARIABLE** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 4687637876494156928 (SB1) has spectroscopic period 54.067233 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 2 [1354.18, 1381.39], 27 [2036.30, 2060.60], 28 [2061.92, 2086.62], 68 [3154.68, 3180.01]. The screening windows are predictions, not event centers.

## Deciding raw evidence

Repeated sharp-rise/slow-decay sawteeth occur throughout sectors 2, 27, 28 and 68. Diagnostic SAP peaks are 3.064, 3.050, 3.064 and 3.056 d; selected positive cores are +3.5 to +4.0 ppt. The 54.067 d Gaia spectroscopic orbit does not explain this shape or establish an eclipse.

Selected-window measurements: s2 BTJD 1378.200, brightening, core +4.0 ppt, pre/post +2.5 ppt, max gap 0.187 d; s2 BTJD 1372.096, brightening, core +3.5 ppt, pre/post +2.2 ppt, max gap 0.062 d; s27 BTJD 2050.596, brightening, core +3.8 ppt, pre/post +2.4 ppt, max gap 0.014 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods.

## Limits and next check

Strong non-eclipse variability is present in the aperture; subtype and varying Gaia source remain unresolved. KSPSAP suppression and small centroid offsets are not source proof. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Difference imaging or stable alternate-aperture photometry to localize the 3.06 d signal.

## Provenance

The frozen packet at `../../source-packets/52152553/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
