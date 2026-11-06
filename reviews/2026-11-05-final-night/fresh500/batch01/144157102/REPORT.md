# E006 — TIC 144157102

Review complete. Physical tier: **PLAUSIBLE**. Gaia DR3 6147285123378224512; selection P=47.568570586019874d, G=11.649431.

S64 shallow and S100 deep bounded target eclipse shapes are real; S10 shallow event is sparsely gap-cut and its fit is unusable. Opposite eclipse depths must remain separate kinds. Nominal shallow47.5452d clock uses the unusable S10 fit only as exploratory guide: many integer alternatives survive observed coverage. Completed review does not establish a unique photometric clock.

## Raw events and timing

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
| 10 | 1579.3857144256367 | 0.003308663335855774 | 10.584535319256396 | 0.6727357677866054 | False |
| 64 | 3053.2874510215192 | 0.0012922358277401142 | 18.363490911312077 | 0.4508310612466871 | True |
| 100 | 4077.4683268150798 | 0.00012576412836888507 | 131.37114699106786 | 0.2975079236597657 | True |

Photometric period: unresolved d; error: not assigned d. Midpoint fit errors are local formal fit errors, not precision ephemeris guarantees. The reported clock uses cadence/2 and .002d floors; E004 additionally uses .06d allowance for broad-event scatter. E006 exploratory clock is deliberately absent from the result period.

Raw quality-zero finite positive SAP is primary evidence. KSPSAP and custom 3x3 TESScut extraction reuse the same photons. Representative available events, all cached sector contexts and covered same-kind predictions were reviewed; missing/flagged windows are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods roughly5–100d and preserves survivors in lead-alias-summary.json. Geometry uses this source's full SB1 covariance and edge-on conjunction approximation; it is not a Gaia period-only match.

## Source and independent extraction

TESScut7x7, sector100, targetxy=[3.166817260133249, 3.449754658830063]; positive-deficit centroid offset=0.35962043777966124 pixels; 3x3 aperture core loss=0.17970882972329272. Numerical centroid alone does not establish source attribution: the pixel morphology and Gaia neighbors were inspected, including competing bright sources.

## Catalogue status

No target prior EB found in shared scoped checks. Shared successful checks cover the seven specified source groups with exact identifiers/cones; nearby matches are distinct unless attribution proves otherwise. Shared sealed receipts and source-specific extracts are retained. Bounded literature comparison is not exhaustive priority proof.

## Limitation and next check

Obtain another complete same-kind raw event to settle integer cycles; use source-specific Gaia only as an association guide.

Evidence: lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-allsectors.png, helper-localization.json/png, helper-tesscut.fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, alias-covered windows, Gaia covariance, current-sector inventory and helper audit. Exact frozen7 reviewed without substitution. No ledger or manuscript edit.
