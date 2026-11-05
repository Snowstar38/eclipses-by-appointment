# H021 — TIC 299187993

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates were unavailable after a positive-control timeout. A primary-table nonmatch is not novelty clearance.

Gaia DR3 source 5865636118916411008, SB1 period 37.32650 d. Frozen stratum `cross_method_dip`; sample ID is not a new-system acceptance. Quality-zero raw SAP sectors inspected: 11, 38, 65, 100, 102.

## Deciding evidence

s38 has a complete shallow flat-bottomed raw dip near BTJD 2337.43. s65 captures a narrow ingress near 3082.66 before a long gap and is an additional observing occasion without a center. s100 has a deeper irregular dip on a strongly evolving baseline near 4088.3–4088.5. The rough 20/47-cycle ~37.25–37.26 d clock is conditional on all three being the same eclipse kind and source. Independent s38 TESSCut aperture recovers ~12.6 ppt, but its difference centroid is 0.63 pixel from target toward a G 11.09 star 35.7 arcsec away that could supply the signal; s100 difference centroid is instead 0.085 pixel from target.

## Limits and next check

Recurring eclipse and target attribution remain insecure; the two difference positions do not establish a shared source. No precision period, epoch, or depth assigned. Obtain resolved/difference-image photometry for a complete future event and compare the nearby bright star.

## Reproducibility

`raw-inspection.json` verifies original bulk-result and FITS SHA-256 values and tabulates representative screening windows. `raw-windows.png` shows these raw windows; `orbit-context.json` and `.png` show full cached-sector SAP and Gaia edge-on conjunction predictions. Screening/conjunction times are not measured event centers. The frozen [source packet](../../source-packets/299187993/sources.json), [central novelty evidence](../../shared-catalogues/target-evidence.json), batch scripts and SHA256SUMS.json preserve receipts.

[Independent helper audit](../helper-audit.md), [source attribution](../helper-source-attribution.json), and the s100 pixel `../helper-pixels/299187993-s100/analysis.json` document the two different difference positions and partial s65 occasion.
