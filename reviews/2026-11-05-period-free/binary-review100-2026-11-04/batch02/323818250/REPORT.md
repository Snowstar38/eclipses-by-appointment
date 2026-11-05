# H019 — TIC 323818250

**Physical verdict:** PLAUSIBLE. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN; four shared VizieR gates were unqueried after a positive-control timeout.

Selected as `cross_method_dip` from the sealed queue. Gaia DR3 source 5203021415006207744 has a spectroscopic period 58.65080398491257 d; that is a selection orbit, not an eclipse period.

Two weak s11 flagged windows near 1600.4 and 1603.95 are only ~2 ppt and blend into a slowly varying baseline; 30-min cadence and sparse samples limit morphology. Seven other cached QLP sectors supply no comparable secure event, while some predicted windows touch sector boundaries. The live MAST inventory adds s10 and s65; both TESSCut pixel cubes have near-zero local-background net target counts despite WCS placement, so they provide no valid photometric null. There is no positive artifact demonstration that refutes the insecure event.

**Limitations:** No measured eclipse period, epoch, or depth. Missing-sector receipts and unusable local-background TESSCut diagnostics in missing-cutout-review.json. The full available cached raw SAP sectors and representative flagged windows are documented in [raw-inspection.json](raw-inspection.json) and [orbit-context.json](orbit-context.json). The panel centers are screening predictions, not measured eclipse times. The [source packet](../../source-packets/323818250/sources.json) records Gaia metadata and FITS hashes; `inspect_raw.py` independently checked every used FITS hash.

**Next check:** If additional photometry becomes available, verify the s11 shape through an alternate extraction and target pixel attribution.
