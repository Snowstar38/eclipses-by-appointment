# Uncertainty-symbol repair

The current public copies repair encoding damage in 54 text files and 40 uncertainty separators on 22 pages of Supplement 2. All numeric tokens are mechanically unchanged, including every page of the 762-page PDF. Only the malformed symbol rectangles were replaced in the PDF, preserving pagination and scientific content. Rendered-page quality checks are recorded with the release.

The [receipt](receipt.json) records original and corrected SHA-256 hashes, exact text substitutions and PDF rectangles. Original private evidence and historical releases remain unchanged. Export manifests now bind the corrected public bytes while preserving their original source hashes. Future exports of historical sources must reapply this documented normalization.


The first PDF repair was rejected by independent visual QA because the glyph size and baseline differed from surrounding text. It was rebuilt from the pristine backup using matching Georgia 10.5 pt. All40 glyphs on22pages then passed visual inspection; all762pages retain identical numeric-token sequences and pagination. The [final repair receipt](repair-receipt.json) and [visual QA report](CORRECTED-REPORT.md) supersede the first repair hash while preserving it in the audit trail.
