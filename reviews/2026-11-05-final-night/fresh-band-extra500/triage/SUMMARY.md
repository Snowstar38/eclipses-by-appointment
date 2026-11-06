# Extra 500 visual screening

Inspected all 62 sheets and all 494 displayed rows, in frozen numeric TIC science order followed by two controls. The full row table retains 492 mapped science targets including 12 no-data rows. The frozen selection contains 500 science sources: 8 identity failures are outside the mapped display and remain in identity-outcomes.json; 480 mapped science targets have QLP data. No target was removed based on its result.

Science morphology counts: {'step_gap_or_instrumental': 244, 'broad_variability': 67, 'ambiguous': 92, 'repeated_discrete': 26, 'noise': 43, 'single_discrete': 8, 'no_data': 12}. Controls: {'repeated_discrete': 2}. Strong screen flags: 34 science rows (26 repeated, 8 single). review-queue.csv includes every strong science flag at priority 1/2 and all 92 ambiguous science rows separately at priority 3. Controls are excluded from the science queue and retained in controls.csv and the full table.

These are visual screening flags, not physical classifications or full-review passes. Review used the rendered quality-zero raw SAP local windows only, up to three distinct sectors per target. A displayed repeated depression does not establish phase coherence, source attribution, astrophysical nature, or an occurrence rate. Sparse sampling, gaps, baseline drift, settling, steps and positive excursions are stated in individual reasons. No threshold automatically determined a visual verdict. No fetch or full review was performed.

All 494 rows have a category and concrete reason; no unreviewed rows remain. Incremental per-sheet records are in visual-sheet-records.json. Each sheet has eight rows except sheet 62, which has six.

Integrity: population bytes match screen-seal.json; selection and downloads manifest bytes match population references. Independently hashed every successful download listed in downloads.json, including control products: 2340 successful records, 1016870400 bytes, zero mismatches. This is the selected local product scope, not all archive holdings or the entire Gaia parent catalogue. Exact SHA-256 values for input manifests, all 62 sheets and output tables are in coverage-and-hashes.json.
