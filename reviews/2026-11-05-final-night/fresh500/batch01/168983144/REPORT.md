# E009 — TIC 168983144

Review complete. Physical tier: **CONFIRMED**. Gaia DR3 3066938564417349888; selection P=35.65868509739297d, G=11.915627.

Three flat-bottom raw events give35.641094d with cycles0/21/51. Covered divisors rejected; residual integer53.4617d/26.7309d aliases are explicitly retained by photometry but disagree strongly with source Gaia35.6587d orbit. Same-kind measured clock selected jointly with source-specific Gaia conjunction consistency. Centered pixel deficit and independent aperture support target.

## Raw events and timing

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
| 34 | 2232.883928908423 | 0.0017999777443793246 | 15.176699191664472 | 0.7020255578280971 | True |
| 61 | 2981.35217944421 | 0.002399083739908257 | 16.93279844344094 | 0.7210171408236444 | True |
| 99 | 4050.5819772999257 | 0.0014479561994866796 | 12.182475766839929 | 0.7004911024795296 | True |

Photometric period: 35.64109442958256 d; error: 7.140364751848311e-05 d. Midpoint fit errors are local formal fit errors, not precision ephemeris guarantees. The reported clock uses cadence/2 and .002d floors; E004 additionally uses .06d allowance for broad-event scatter. E006 exploratory clock is deliberately absent from the result period.

Raw quality-zero finite positive SAP is primary evidence. KSPSAP and custom 3x3 TESScut extraction reuse the same photons. Representative available events, all cached sector contexts and covered same-kind predictions were reviewed; missing/flagged windows are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods roughly5–100d and preserves survivors in lead-alias-summary.json. Geometry uses this source's full SB1 covariance and edge-on conjunction approximation; it is not a Gaia period-only match.

## Source and independent extraction

TESScut7x7, sector61, targetxy=[3.822061024643837, 3.270438620878064]; positive-deficit centroid offset=0.2227815996986796 pixels; 3x3 aperture core loss=0.017996706292606746. Numerical centroid alone does not establish source attribution: the pixel morphology and Gaia neighbors were inspected, including competing bright sources.

## Catalogue status

No target prior EB found in shared scoped checks. Shared successful checks cover the seven specified source groups with exact identifiers/cones; nearby matches are distinct unless attribution proves otherwise. Shared sealed receipts and source-specific extracts are retained. Bounded literature comparison is not exhaustive priority proof.

## Limitation and next check

Another event outside3-cycle spacing would resolve the purely photometric integer ambiguity independently of Gaia.

Evidence: lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-allsectors.png, helper-localization.json/png, helper-tesscut.fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, alias-covered windows, Gaia covariance, current-sector inventory and helper audit. Exact frozen7 reviewed without substitution. No ledger or manuscript edit.
