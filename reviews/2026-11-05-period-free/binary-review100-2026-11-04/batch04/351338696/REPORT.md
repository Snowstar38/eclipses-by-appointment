# H031 — TIC 351338696

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates were unavailable; a primary-table nonmatch is not novelty clearance.

Gaia DR3 6428584079448787072, SB2, orbital P=28.21991 d. Frozen stratum `repeat_sector_dip`; sample ID is not a physical acceptance. Raw SAP with QUALITY=0 inspected for sectors 13, 27, 67, 94, 101, 102, 103, 104.

## Deciding evidence

The sector-94 dip at BTJD 3874.77 is simultaneous and similarly shaped in widely separated TIC 320328447 (H040): half-day bins put both about 6 ppt low near 3874.5-3875.0. The sector-103 dip and brightening are opposite sides of a large gap/offset followed by a decay, rather than a second resolved eclipse. Full raw sectors 13,27,67,94,101-104 show no repeat of the s94 event at either Gaia edge-on conjunction kind.

## Limits and next check

This refutes the selected repeat-eclipse interpretation; common-mode coincidence is diagnostic, not a proof of the exact instrument mechanism. It does not rule out a weaker unrelated eclipse. Reinspect with independent photometry only if a distinct repeat emerges.

## Sources

`raw-inspection.json` includes verified bulk/FITS SHA-256 receipts and representative flagged-window numbers; `raw-windows.png` plots those windows. `orbit-context.json` and `.png` show every cached sector with approximate Gaia edge-on conjunctions. Screening centers are not measured eclipse centers. The frozen [source packet](../../source-packets/351338696/sources.json), [central catalogue record](../../shared-catalogues/target-evidence.json), batch scripts and manifest preserve provenance.

[Shared sector-94 raw comparison](../common-event.json) gives matched timestamps and bin medians. `alternate-s94.json`/`.png` show local raw SAP diagnostics.

`sector-availability.raw` records the current TESSCut sector response.
