# Batch02 lead audit: T011-T020

All ten fixed queue identities are present in RESULTS.csv in queue order. The
Sol lead inspected representative raw SAP quality-zero windows for every
target, produced per-target numeric and plot artifacts, and verified all 103
cached FITS against the source packets. The queue is priority-selected; these
two confirmed and eight refuted eclipse claims are not a yield estimate.

T012 and T014 have repeated, visually coherent raw eclipses. T012 deep and
shallow clocks are 46.866717 and 46.866905 d, respectively. The S64 shallow
and S65 deep centers are separated by 0.50065 of the full period. T014 has
five same-kind centers with cycles 0,4,18,22,33 at 49.327372 d; actual S40,
S53 and S60 half-cycle windows cover the entire +/-0.1 d core with both
baselines and show no 7-9 ppt eclipse. `lead-half-alias.png` was inspected.
The table rounds period/error display while the numeric artifacts retain fits,
cycles, residuals and source-specific error meanings. The single-kind T014
epoch is an observed kind, not a physically assigned primary.

Terra helper independently reduced T012 S37 and T014 S19 raw TESSCut pixels,
checked WCS difference centroids and all ideal-G capable Gaia neighbors
within 120 arcsec, and compared corrected QLP channels. Their audit and
scripts are `helper-audit.md` and `helper-*`. The T012 initial baseline sat
inside the broad eclipse; the helper corrected it and documented the false
near-zero result. T012/T014 target offsets are 0.089/0.127 pixels; nearest
capable neighbor separations are 87.24/42.95 arcsec, respectively. Alternative
reductions share TESS photons. Gaia conjunction offsets are small in the
edge-on approximation but were not treated as a statistical covariance test.

After the helper completed, the Sol lead performed additional checks. Newly
available S105 TESSCut pixels were fetched for T011 and T019, with URLs and
hashes in `lead-s105-fetch.json`. The T019 conditional +1 Gaia window in S105
begins only 0.16 d before center and has no full pre-ingress coverage, so it
is not claimed as a strict sensitive null. T011's next +6 conditional center
falls beyond S105. More decisive are target-centered raw-pixel extractions at
four ambiguous older QLP flags, documented in `lead-exception-pixels.json`
and plot pairs. T011 S96 is a brightening/recovery in pixels despite a QLP
dip; T016 S19 rises through the flag; T018 S104 is a smooth drift with no
localized pixel deficit; T019 S103 is a sloped variation, bright cusp and
gap-associated level step. The specified core-to-baseline comparisons are
-54.7, -2.0, -0.11 and -3.37 ppt, respectively. These contrary shapes refute
the selected eclipse claims; they do not refute the Gaia binary identities or
exclude unrelated hidden eclipses. T013, T015, T017 and T020 are separately
refuted by broad noncoherent oscillation, smooth/gap variability, an upward
step and a strong positive pulse, as described in their reports.

The helper's completed `helper-audit.md` was CP1252. The Sol lead preserved
its original bytes as `helper-audit.cp1252.raw`, converted text/symbols to
UTF-8/ASCII and recorded both hashes in `lead-helper-encoding.json`; no new
scientific helper claim was inserted. The lead generator and result text were
repaired to ASCII, with before/after hash and relative-link correction in
`lead-text-conversion.json`. The lead's subsequent exception revision is
recorded in `lead-exception-revision.json`. Source packet, original bulk/fold
receipts, and 103 FITS hashes are in `SOURCE-HASHES.json`; batch-owned hashes
are in `SHA256SUMS.json`.

All novelty statuses remain UNKNOWN because four VizieR gates in the shared
catalogue audit were unavailable after failed positive controls. No duplicate
novelty query, existing evidence revision, ledger edit, paper change or
external message was made. Root alone accepts this batch.
