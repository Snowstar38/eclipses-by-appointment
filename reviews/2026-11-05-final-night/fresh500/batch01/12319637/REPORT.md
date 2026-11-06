# E001 — TIC 12319637

Review complete. Physical tier: **CONFIRMED**. Gaia DR3 514772377553055104; selection P=25.017566331609274d, G=11.645523.

Three narrow raw eclipses, measured 37/44-cycle clock and covered divisor nulls; target-centered deficit survives independent 3x3 TESScut extraction. Gaia conjunction offsets are within source covariance.

## Raw events and timing

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
| 18 | 1800.9115119361968 | 0.008720960225425945 | 67.60496361568958 | 0.21975516241388457 | True |
| 52 | 2726.3792540436375 | 0.0010961312470300056 | 52.2236917843067 | 0.15933392172680952 | True |
| 58 | 2901.4694265493504 | 0.0005730457951179434 | 57.478829887648146 | 0.16244501688791932 | True |

Photometric period: 25.01270519965353 d; error: 0.00022902894037020352 d. Midpoint fit errors are local formal fit errors, not precision ephemeris guarantees. The reported clock uses cadence/2 and .002d floors; E004 additionally uses .06d allowance for broad-event scatter. E006 exploratory clock is deliberately absent from the result period.

Raw quality-zero finite positive SAP is primary evidence. KSPSAP and custom 3x3 TESScut extraction reuse the same photons. Representative available events, all cached sector contexts and covered same-kind predictions were reviewed; missing/flagged windows are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods roughly5–100d and preserves survivors in lead-alias-summary.json. Geometry uses this source's full SB1 covariance and edge-on conjunction approximation; it is not a Gaia period-only match.

## Source and independent extraction

TESScut7x7, sector18, targetxy=[3.3199574889548265, 3.438139540075965]; positive-deficit centroid offset=0.07773827285160875 pixels; 3x3 aperture core loss=0.018816470493209003. Numerical centroid alone does not establish source attribution: the pixel morphology and Gaia neighbors were inspected, including competing bright sources.

## Catalogue status

VSX EB55.94arcsec has P1.76684d, distinct from25.0127d target clock and centered deficit; not prior target EB. Shared successful checks cover the seven specified source groups with exact identifiers/cones; nearby matches are distinct unless attribution proves otherwise. Shared sealed receipts and source-specific extracts are retained. Bounded literature comparison is not exhaustive priority proof.

## Limitation and next check

Longer-baseline timing can refine the bounded representative ephemeris.

Evidence: lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-allsectors.png, helper-localization.json/png, helper-tesscut.fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, alias-covered windows, Gaia covariance, current-sector inventory and helper audit. Exact frozen7 reviewed without substitution. No ledger or manuscript edit.
