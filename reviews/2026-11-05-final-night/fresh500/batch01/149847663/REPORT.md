# E008 — TIC 149847663

Review complete. Physical tier: **PROBABLE**. Gaia DR3 5089212645744372992; selection P=31.501604109530476d, G=11.628131.

Adjacent deep primaries at1431.01504/1462.56192 give31.546878d; shallow secondary pair independently31.548486d. Divisor alternatives have covered nulls. Independent aperture shows deep centered eclipse. Full nonlinear Gaia covariance retains primary conjunction beyond the3sigma interval while secondary is within; repeated target eclipser is real but selected Gaia-orbit association is unresolved.

## Raw events and timing

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
| 4 | 1431.0150393408244 | 0.00010962918986734406 | 129.14793801699244 | 0.22391258030394948 | True |
| 5 | 1462.5619170631178 | 0.0001659349913287867 | 133.9315476573895 | 0.22804270831129678 | True |
| 5 | 1449.2917239745127 | 0.001825939066811789 | 9.090346662652403 | 0.267321752754716 | True |
| 4 | 1417.7432375188203 | 0.0009107616519841761 | 9.660991107798463 | 0.2796390392994916 | True |

Photometric period: 31.546877722293996 d; error: 0.014731213917888087 d. Midpoint fit errors are local formal fit errors, not precision ephemeris guarantees. The reported clock uses cadence/2 and .002d floors; E004 additionally uses .06d allowance for broad-event scatter. E006 exploratory clock is deliberately absent from the result period.

Raw quality-zero finite positive SAP is primary evidence. KSPSAP and custom 3x3 TESScut extraction reuse the same photons. Representative available events, all cached sector contexts and covered same-kind predictions were reviewed; missing/flagged windows are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods roughly5–100d and preserves survivors in lead-alias-summary.json. Geometry uses this source's full SB1 covariance and edge-on conjunction approximation; it is not a Gaia period-only match.

## Source and independent extraction

TESScut7x7, sector5, targetxy=[3.8943645883690605, 3.748986651046499]; positive-deficit centroid offset=0.11394808926637486 pixels; 3x3 aperture core loss=0.12611285669529737. Numerical centroid alone does not establish source attribution: the pixel morphology and Gaia neighbors were inspected, including competing bright sources.

## Catalogue status

No target prior EB found in shared scoped checks. Shared successful checks cover the seven specified source groups with exact identifiers/cones; nearby matches are distinct unless attribution proves otherwise. Shared sealed receipts and source-specific extracts are retained. Bounded literature comparison is not exhaustive priority proof.

## Limitation and next check

Revisit source-specific spectroscopic orbit/conjunction geometry; do not erase measured primary tension.

Evidence: lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-allsectors.png, helper-localization.json/png, helper-tesscut.fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, alias-covered windows, Gaia covariance, current-sector inventory and helper audit. Exact frozen7 reviewed without substitution. No ledger or manuscript edit.
