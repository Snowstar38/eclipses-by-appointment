# H087 — TIC 433693445

Physical verdict: **NON_ECLIPSE_VARIABLE** for the selected brightening lead. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four VizieR gates remain unavailable in the central catalogue check.

Gaia DR3 2211707771448719232 (SB1) has spectroscopic period 52.322326 d. Selection from Gaia SB systems does not prove a photometric binary signal. All cached sector raw SAP, QUALITY=0, was inspected: 17 [1766.18, 1788.45], 18 [1791.60, 1814.49], 24 [1955.86, 1982.15], 57 [2853.41, 2882.06], 58 [2882.39, 2910.01], 77 [3395.51, 3423.50], 78 [3434.35, 3449.48], 84 [3584.63, 3610.29], 85 [3610.60, 3635.99]. The screening windows are predictions, not event centers.

## Deciding raw evidence

The sector-17 +20.0 ppt impulse near BTJD 1783.64 rises abruptly over three quality-zero cadences and decays over about 0.2 d, a flare-like morphology in both SAP and KSPSAP. Local SAP_BKG fluctuates around 200–600 counts without a monotonic ramp matching the impulse; SAP_X/Y shift only a few millipixels. TESSCut peak-minus-pre positive-pixel moment is (5.80,4.99) close to target WCS (5.78,5.09), with +452.9 counts in the nearest-pixel-centered target 3×3. Eight other sectors do not show the same impulse.

Selected-window measurements: s17 BTJD 1783.638, brightening, core +20.0 ppt, pre/post +3.1 ppt, max gap 0.062 d. These local medians describe observed aperture flux, not fitted event depths. `raw-context.png` shows every full sector and every selected window; `raw-inspection.json` records cadence coverage, gaps, alternate FITS columns and source hashes. `period-scan.json` contains per-sector diagnostic 0.5–15 d Lomb–Scargle peaks after linear detrending; they are not orbital periods. For the deciding pixel check, `tesscut-receipt.json` binds the fetched cutout and `pixel-difference.json`/`.png` give the target WCS, exact frame intervals, nearest-integer-centered apertures and unregistered image difference. This is a same-sector reduction, not an independent observing occasion.

## Limits and next check

The target-centered excess supports non-eclipse variability consistent with a stellar flare, but same-sector pixels cannot resolve a subpixel blend or prove flare physics. The image moment is descriptive, not a fitted PSF position. KSPSAP uses the same exposures. No orbital timing inference. No eclipse epoch or depth is promoted. Same photons in KSPSAP are a reduction check, not a new observing occasion. Higher resolution source photometry if the flare source matters.

## Provenance

The frozen packet at `../../source-packets/433693445/sources.json` binds the Gaia metadata, FITS identities and original bulk/fold receipts. `../SOURCE-HASHES.json` rechecks them; `../SHA256SUMS.json` seals this review.
