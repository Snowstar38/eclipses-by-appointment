# Next 70 binary reviews: evidence export

This is a sanitized evidence export of the seven accepted batches. The original paper's review standard applies. Analysis scripts reuse existing analysis primitives; these reviews are not independently written replications. Custom TESScut extraction uses the same TESS photons with a different extraction, not an independent observation.

The campaign contains 67 confirmed and three plausible systems. One confirmed system, TIC 432482170, is a known prior eclipsing-binary recovery; the other 66 confirmed systems are new headline additions under the paper's scoped standard.

`FULL-RESULTS.csv` indexes the 70 reports using paths relative to this directory. Each batch retains compact numerical results, provenance, analysis scripts, contributor notes and a manifest. The shared catalogue directory includes original query receipts and the previous 26-target ASAS-SN coverage recovery. Catalogue coverage and its limits are explained in `shared-catalogues/README.md`.

Raw FITS and image cubes, plot images and transient logs are excluded. Product URIs and identifiers are retained in the provenance and search receipts when originally recorded; SHA-256 values for excluded files are in the batch export manifests. Excluded plots mentioned in reports were inspected during review but are not included here. Local workstation paths have been removed; provenance records and manifests provide portable identifiers or hashes where available. Scripts record the analysis and may require path configuration and retrieval of omitted archive data before rerunning.

`MANIFEST.json` lists source hashes and exported hashes separately. Sanitization may change text and hashes. The public manifest does not claim that an excluded raw product is included.
