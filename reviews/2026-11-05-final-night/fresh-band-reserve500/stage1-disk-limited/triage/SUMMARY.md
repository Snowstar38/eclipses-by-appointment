# Reserve 500 visual screening

Visually inspected all 62 sheets and all 495 display-row positions in frozen numeric TIC science order followed by two controls. All available raw-window panels were inspected; blank positions were retained as no_data/download_unavailable. All original screening-summary.csv columns are preserved. The frozen selection has 500 science sources, 493 mapped science rows and 7 identity failures outside the mapped display; 485 mapped science targets have QLP availability. Availability does not imply a successful local download.

Science morphology counts: {'no_data': 321, 'step_gap_or_instrumental': 103, 'ambiguous': 41, 'broad_variability': 10, 'noise': 8, 'repeated_discrete': 8, 'single_discrete': 2}. Controls: {'repeated_discrete': 2}. Science review queue contains 10 strong visual flags at priority 1/2 and 41 ambiguous rows at priority 3. Controls remain separate and are excluded from the science queue.

Disk-floor interruption left 1450 products unavailable; the retained downloads manifest has 2276 records, 826 successful products across 174 TICs. No-data rows are availability failures, never physical negatives. No population member was removed based on its result. All download and population receipts remain intact.

These are morphology screening flags, not physical classifications or full-review passes. Review used rendered quality-zero raw SAP local windows, up to three sectors per target. Repeated discrete shape does not establish phase coherence, source attribution, astrophysical nature, or occurrence rates. Gaps, steps, settling, slopes, positive excursions and sparse sampling are recorded in row reasons. No new download, full physical review, ledger or public edit was performed.

Incremental per-sheet observations were saved during review and expanded to complete row records in visual-sheet-records.json. Every row has a classification and concrete reason. Sheet 62 has seven positions; other sheets have eight. Inspection crops in inspection/ were made solely from existing sheet bytes for legibility; no plots were regenerated from flux or new data.

Integrity: population hash matches screen-seal.json, and selection/downloads manifest hashes match population references. Independently hashed every one of the 826 successful manifest products (354381120 bytes); zero mismatches. Scope is these successful retained local products, not missing archive products or the full parent catalogue. Input, all 62 original sheet, and output SHA-256 receipts are in coverage-and-hashes.json.
