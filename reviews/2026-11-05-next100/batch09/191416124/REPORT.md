# Q083 - TIC 191416124

**Physical verdict:** PLAUSIBLE. **Review completion:** COMPLETE. **Catalogue novelty:** UNKNOWN.

## Raw morphology and coverage

Three cached sectors. S57 has multiple locally symmetric troughs, notably near 2872.425 and 2877.295; S84 shows a related train near 3600.055, 3602.601, 3605.141 and 3607.620. S17 also varies. Raw SAP and DET_FLUX retain the waves, while SYS_RM_FLUX suppresses them. One S57 core at 2874.61-2874.83 is gapped, but other troughs are nearly fully covered. Variable width, depth and baseline leave oscillation as a serious alternative to eclipses.

## Timing and orbital interpretation

Smoothed descriptive minima in S57 are 2869.832, 2872.425, 2874.872, 2877.295 and 2879.540 BTJD; adjacent intervals vary 2.245-2.593 d. S84 intervals are about 2.48-2.55 d. The waveform Lomb-Scargle maximum is 2.46652374 d across all sectors; this is not a measured eclipse ephemeris. Alternating eclipse kinds near a roughly 5-d orbit remain possible, with untested long-baseline integer aliases. Neither interpretation links securely to Gaia SB1 P22.4183 d.

## Source and alternative reduction

S57 and S84 TESSCut have positive target-region flux and difference centroids 0.159 and 0.081 pixel from the target. A G15.236 neighbor 0.885 pixel away has approximate G flux ratio 0.00549, comparable with the few-ppt deficit. The blended image does not resolve target versus neighbor ownership. The raw SAP/DET_FLUX comparison and separate SYS_RM_FLUX reduction show extraction dependence; the latter can suppress broad astrophysical signals and is not a null. No independent observing occasion beyond the three cached TESS sectors is claimed.

## Limits and next check

Eclipse-like troughs survive, but their source, eclipse versus oscillation interpretation, same-kind cycle count and Gaia association remain unsettled. MAST availability on 2026-11-05 returned only the three cached sectors. No period, epoch, formal error or depth is adopted.

Obtain high-angular-resolution time-series photometry across two predicted troughs to identify the variable star and test a stable same-kind clock.

## Provenance

`lead-context.json`, `lead-local-series.json` and `lead-flag-diagnostics.json` preserve raw quality-zero time/flux, actual endpoints and gaps for all 3 cached sectors and selected windows. `lead-raw-context.png` and `lead-dip-zooms.png` show the morphology. Batch-level cross-target, alternate-reduction and exception receipts and independent `helper-audit.md` support the source findings. The context script checks the sealed source-packet, bulk-result and FITS SHA-256 receipts. Screening window centers are predictions, never measured eclipse times. Exact target VSX query receipts are in `../../tap-recovery/vsx-Q083.json`; remaining ASAS-SN and Kostov gates are unavailable, so novelty stays UNKNOWN.
