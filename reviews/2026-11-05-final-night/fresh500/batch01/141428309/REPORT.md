# E005 — TIC 141428309

Review complete. Physical tier: **CONFIRMED**. Gaia DR3 4650833167861993600; selection P=54.51093607459538d, G=11.837272.

Deep primary S2/S98 gives54.524695d; shallow S1/S93 independently gives54.524665d across46cycles and excludes primary-pair integer aliases. S94 gap-edge and outlier flags excluded from timing. Centered source deficit and independent aperture confirm target; source-specific Gaia conjunctions consistent.

## Raw events and timing

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
| 1 | 1331.9977648318632 | 0.0016915456274282507 | 11.321332300630491 | 0.3527731044564813 | True |
| 2 | 1359.646589411705 | 0.0002199735170072199 | 124.03293337902502 | 0.3770998818573957 | True |
| 93 | 3840.132335699092 | 0.0017142346293907678 | 11.341833055261297 | 0.3222581560028019 | True |
| 94 | 3866.643442775806 | 0.0001312331944056319 | 65.8828146545656 | 0.05000000000000944 | False |
| 94 | 3873.1018318276006 | 0.00018191615947952725 | 54.93833419079491 | 0.05000000000097668 | False |
| 98 | 4031.3566542430913 | 0.00016611434212190522 | 111.01933438794507 | 0.37448347579534397 | True |

Photometric period: 54.52469520064056 d; error: 0.0002164662749564641 d. Midpoint fit errors are local formal fit errors, not precision ephemeris guarantees. The reported clock uses cadence/2 and .002d floors; E004 additionally uses .06d allowance for broad-event scatter. E006 exploratory clock is deliberately absent from the result period.

Raw quality-zero finite positive SAP is primary evidence. KSPSAP and custom 3x3 TESScut extraction reuse the same photons. Representative available events, all cached sector contexts and covered same-kind predictions were reviewed; missing/flagged windows are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods roughly5–100d and preserves survivors in lead-alias-summary.json. Geometry uses this source's full SB1 covariance and edge-on conjunction approximation; it is not a Gaia period-only match.

## Source and independent extraction

TESScut7x7, sector2, targetxy=[3.5698281080571777, 3.5989565641346593]; positive-deficit centroid offset=0.03206201935217012 pixels; 3x3 aperture core loss=0.12698698013219267. Numerical centroid alone does not establish source attribution: the pixel morphology and Gaia neighbors were inspected, including competing bright sources.

## Catalogue status

No target prior EB found in shared scoped checks. Shared successful checks cover the seven specified source groups with exact identifiers/cones; nearby matches are distinct unless attribution proves otherwise. Shared sealed receipts and source-specific extracts are retained. Bounded literature comparison is not exhaustive priority proof.

## Limitation and next check

Additional complete primary can improve timing; partial S94 is not a measured midpoint.

Evidence: lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-allsectors.png, helper-localization.json/png, helper-tesscut.fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, alias-covered windows, Gaia covariance, current-sector inventory and helper audit. Exact frozen7 reviewed without substitution. No ledger or manuscript edit.
