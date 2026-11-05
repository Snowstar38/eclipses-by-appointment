# H039 — TIC 454228598

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates were unavailable; a primary-table nonmatch is not novelty clearance.

Gaia DR3 5873154098409671296, SB1, orbital P=29.72893 d. Frozen stratum `repeat_sector_dip`; sample ID is not a physical acceptance. Raw SAP with QUALITY=0 inspected for sectors 12, 38, 39, 65, 99, 100, 101, 102.

## Deciding evidence

A single asymmetric ~15 ppt sector-12 raw dip reaches a minimum near BTJD 1625.85 and recovers over several days. A separate TESSCut 5x5 aperture preserves the feature, while the QLP corrected KSPSAP flux suppresses it. The raw series starts at 1624.97, only ~0.9 d before minimum, so there is no secure pre-event baseline; the eight currently available sectors equal the eight cached sectors and show no comparable repeat. The event is ~9 days from the Gaia 29.729 d conjunction prediction, so Gaia does not supply a secure eclipse clock.

## Limits and next check

A single event near sector start could be a real eclipse or startup/systematic. A Gaia G=13.72 source 5.96 arcsec away is flux-capable at approximate G flux ratio 0.053; WCS/aperture evidence does not locate the source. No period, epoch or depth is promoted to a system measurement. Obtain a complete repeat with pre- and post-event baseline and resolved photometry.

## Sources

`raw-inspection.json` includes verified bulk/FITS SHA-256 receipts and representative flagged-window numbers; `raw-windows.png` plots those windows. `orbit-context.json` and `.png` show every cached sector with approximate Gaia edge-on conjunctions. Screening centers are not measured eclipse centers. The frozen [source packet](../../source-packets/454228598/sources.json), [central catalogue record](../../shared-catalogues/target-evidence.json), batch scripts and manifest preserve provenance.

`alternate-s12.json`/`.png` compare SAP with QLP corrected KSPSAP and background/centroid diagnostics. [Helper pixel extraction](../helper-pixels/454228598/) and [Gaia neighbors](../helper-h039-neighbors.json) preserve the independent aperture and close-source assessment. `sector-availability.raw` records the current TESSCut sector response.
