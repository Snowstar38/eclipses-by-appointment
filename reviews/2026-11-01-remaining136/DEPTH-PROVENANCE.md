# Depth correction provenance

Current accepted measurements are under campaign/batch01 through campaign/batch14 and current reports under reports/. These use realized central trapezoid depth.

The separate [correction audit](campaign/depth-audit/README.md) records the exact replay and authorized correction. Its original/ and originals/ trees preserve superseded historical bytes; they are not current measurements. Its corrected/ tree is an intermediate staging overlay and is also not authoritative current output. applied-manifest.json gives the final before/after mapping. post-correction-verification.json verifies the applied correction. Eleven events in eight targets changed, with two target median changes; timing and physical verdicts did not change.

MANIFEST.csv labels historical snapshots and intermediate overlays separately. Source/export hashes remain exact despite anonymous public wording and usable relative links. Original source locations are retained privately; public SOURCE-RESOLVER.json uses logical aliases and expected/resolved hashes. Only the original search-log path plus its exact original hash resolves to the immutable identical original-prefix snapshot. FITS and bulk search logs are not distributed; source hashes and acquisition receipts remain available here.
