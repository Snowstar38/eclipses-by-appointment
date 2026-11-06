# E004 — TIC 55662895

Review complete. Physical tier: **CONFIRMED**. Gaia DR3 4665283533789578496; selection P=36.98093175784594d, G=11.887947.

Three bounded ~1.2d eclipses in S1/S2/S95 repeat at36.9724d. Wide fits replace unsuitable narrow fits. S98 flag is a baseline step and excluded. Pixel deficit is on target, separate from bright neighbor2.39pixels away; independent aperture recovers eclipse. Gaia covariance supports conjunction.

## Raw events and timing

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
| 1 | 1334.4582794274484 | 0.02214514437897174 | 11.044552277361955 | 1.6875654651468939 | True |
| 2 | 1371.3646711929484 | 0.005808724411306633 | 9.751913945084727 | 1.1952126311932827 | True |
| 95 | 3885.520790818375 | 0.0025949909893424883 | 9.499529708263754 | 1.2187340944602338 | True |
| 98 | 4010.570587942434 | 0.013532076268374911 | 11.876484604311027 | 2.9999999999999996 | False |

Photometric period: 36.97238821779973 d; error: 0.0010726835060317222 d. Midpoint fit errors are local formal fit errors, not precision ephemeris guarantees. The reported clock uses cadence/2 and .002d floors; E004 additionally uses .06d allowance for broad-event scatter. E006 exploratory clock is deliberately absent from the result period.

Raw quality-zero finite positive SAP is primary evidence. KSPSAP and custom 3x3 TESScut extraction reuse the same photons. Representative available events, all cached sector contexts and covered same-kind predictions were reviewed; missing/flagged windows are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods roughly5–100d and preserves survivors in lead-alias-summary.json. Geometry uses this source's full SB1 covariance and edge-on conjunction approximation; it is not a Gaia period-only match.

## Source and independent extraction

TESScut7x7, sector2, targetxy=[3.951248819861945, 3.81815798703156]; positive-deficit centroid offset=0.4846460845596437 pixels; 3x3 aperture core loss=0.008697307634494056. Numerical centroid alone does not establish source attribution: the pixel morphology and Gaia neighbors were inspected, including competing bright sources.

## Catalogue status

No target prior EB found in shared scoped checks. Shared successful checks cover the seven specified source groups with exact identifiers/cones; nearby matches are distinct unless attribution proves otherwise. Shared sealed receipts and source-specific extracts are retained. Bounded literature comparison is not exhaustive priority proof.

## Limitation and next check

Fit broader baseline and additional sectors to improve broad-eclipse midpoint precision.

Evidence: lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-allsectors.png, helper-localization.json/png, helper-tesscut.fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, alias-covered windows, Gaia covariance, current-sector inventory and helper audit. Exact frozen7 reviewed without substitution. No ledger or manuscript edit.
