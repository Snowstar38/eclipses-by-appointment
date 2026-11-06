# E007 — TIC 149477061

Review complete. Physical tier: **PLAUSIBLE**. Gaia DR3 4660070646084855168; selection P=56.979446767033025d, G=11.957549.

One credible ~5ppt S2 dip is centered on target. Other reviewed sectors contain smooth broad minima, gap edges and steps, without a demonstrated same-kind bounded repeat. Source attribution does not create recurrence.

## Raw events and timing

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
| 2 | 1357.6949724195174 | 0.006101023277823546 | 4.8663832879082385 | 0.799024169122393 | True |

Photometric period: unresolved d; error: not assigned d. Midpoint fit errors are local formal fit errors, not precision ephemeris guarantees. The reported clock uses cadence/2 and .002d floors; E004 additionally uses .06d allowance for broad-event scatter. E006 exploratory clock is deliberately absent from the result period.

Raw quality-zero finite positive SAP is primary evidence. KSPSAP and custom 3x3 TESScut extraction reuse the same photons. Representative available events, all cached sector contexts and covered same-kind predictions were reviewed; missing/flagged windows are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods roughly5–100d and preserves survivors in lead-alias-summary.json. Geometry uses this source's full SB1 covariance and edge-on conjunction approximation; it is not a Gaia period-only match.

## Source and independent extraction

TESScut7x7, sector2, targetxy=[3.0731068612477364, 3.963906473091618]; positive-deficit centroid offset=0.16866077073622235 pixels; 3x3 aperture core loss=0.004209104676802133. Numerical centroid alone does not establish source attribution: the pixel morphology and Gaia neighbors were inspected, including competing bright sources.

## Catalogue status

No target prior EB found in shared scoped checks. Shared successful checks cover the seven specified source groups with exact identifiers/cones; nearby matches are distinct unless attribution proves otherwise. Shared sealed receipts and source-specific extracts are retained. Bounded literature comparison is not exhaustive priority proof.

## Limitation and next check

A complete same-kind repeat and tested clock are required; broad minima retain unresolved physical origin.

Evidence: lead-context.json, lead-series.json, lead-timing.json, lead-raw-context.png, lead-allsectors.png, helper-localization.json/png, helper-tesscut.fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, alias-covered windows, Gaia covariance, current-sector inventory and helper audit. Exact frozen7 reviewed without substitution. No ledger or manuscript edit.
