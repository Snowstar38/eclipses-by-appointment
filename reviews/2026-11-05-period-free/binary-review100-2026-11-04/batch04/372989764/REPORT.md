# H032 — TIC 372989764

Physical verdict: **PROBABLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates were unavailable; a primary-table nonmatch is not novelty clearance.

Gaia DR3 5923328421736888704, SB1, orbital P=28.24902 d. Frozen stratum `repeat_sector_dip`; sample ID is not a physical acceptance. Raw SAP with QUALITY=0 inspected for sectors 12, 39, 66, 93, 103, 104.

## Deciding evidence

Deep flat-bottomed events recur in raw SAP sectors 12,39,66,93,103,104; a shallower kind occurs about 14 days away in several sectors. Independent local centers of the deep kind at 2379.6308,3113.9838,4159.0606,4187.2683 BTJD fit cycles 0,26,63,64 at about 28.24465 d; adjacent sectors 103/104 rule out nearby integer-cycle alternatives from the long baseline. Both kinds approximately match Gaia eccentric-orbit conjunctions for P=28.249018 d. A separate 5x5 TESSCut sector-66 extraction recovers a 29.53 ppt deep dip and an 8.15 ppt shallow dip.

## Limits and next check

Target attribution is unresolved: Gaia DR3 5923328421736889728, G=14.81, lies 6.36 arcsec away, approximate G flux ratio 0.045, and could supply a 30 ppt blended dip with a deep intrinsic eclipse. Difference centroids 0.108 and 0.264 pixel from the target do not deblend at 0.31 pixel separation. Clock and depth are exploratory, without calibrated errors; TESSCut shares photons with QLP. The bulk fold screen attempted P=28.24275 d but did not flag it (z=1.485); this review does not establish why. Obtain resolved photometry of both eclipse kinds or a calibrated pixel-level blend fit.

## Sources

`raw-inspection.json` includes verified bulk/FITS SHA-256 receipts and representative flagged-window numbers; `raw-windows.png` plots those windows. `orbit-context.json` and `.png` show every cached sector with approximate Gaia edge-on conjunctions. Screening centers are not measured eclipse centers. The frozen [source packet](../../source-packets/372989764/sources.json), [central catalogue record](../../shared-catalogues/target-evidence.json), batch scripts and manifest preserve provenance.

[Helper timing and alias audit](../helper-clock.json), [local fits](../helper-local-fits.json), [pixel attribution](../helper-source-attribution.json), [shallow-kind attribution](../helper-shallow-attribution.json), and `../helper-pixels/372989764/` contain independent extraction and WCS receipts. `alternate-s66.json` adds raw local diagnostics.
