# TIC 159499138: batch 02 review

**Physical verdict:** confirmed. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 19; Gaia DR3 source 967967877695470848; actual DR3 G=12.033017. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 5 usable measured eclipse centers across sectors 20, 60, 73; 5 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 155.52 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=7.883525722 ± 0.000024373 d and reference center BTJD 1864.487494. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=7.883934523 d; difference=-0.000409 d.
- Pixel attribution and alternative reduction: historical TESScut sector 60 stacked 2 eclipse windows; the flux-deficit centroid is 0.135 pixel from the Gaia target and the peak deficit pixel is [8, 8] versus target pixel [8, 8]. Custom 1×1/3×3/5×5 pixel apertures give 147.0/139.6/127.9 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 10 Gaia neighbors within 60 arcsec were tested for flux capability; 0 are capable. No Gaia neighbor is flux-capable.
- Gaia geometry: selected edge-on conjunction offset -0.01428 in orbital phase, linear covariance scale 0.133 d. Approximate central duration 9.62 h versus observed median 6.48 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

Representative-sector timing and pixel evidence; period uncertainty is formal fit/cadence with scatter inflation where needed, not calibrated total coverage.

Additional independent observations can refine the ephemeris and source attribution.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/159499138/diff_s60.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet159499138/tesscut_s060.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.


Stable review key: R428. Public evidence files: [diff_s60.json](../../evidence/159499138/historical/diff_s60.json), [diff_s60.png](../../evidence/159499138/historical/diff_s60.png), [gaia.json](../../evidence/159499138/historical/gaia.json), [measurements.json](../../evidence/159499138/measurements.json), [pixel-evidence.json](../../evidence/159499138/pixel-evidence.json), [raw-events.png](../../evidence/159499138/raw-events.png), [raw-windows.csv](../../evidence/159499138/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
