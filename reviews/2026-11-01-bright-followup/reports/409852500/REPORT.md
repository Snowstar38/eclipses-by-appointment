# TIC 409852500: batch 02 review

**Physical verdict:** probable. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 16; Gaia DR3 source 6445307372129779072; actual DR3 G=12.026384. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 5 usable measured eclipse centers across sectors 13, 94, 104; 5 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 7.44 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=8.643951250 ± 0.000025003 d and reference center BTJD 1659.414449. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=8.642794775 d; difference=+0.001156 d.
- Pixel attribution and alternative reduction: historical TESScut sector 13 stacked 2 eclipse windows; the flux-deficit centroid is 0.107 pixel from the Gaia target and the peak deficit pixel is [7, 8] versus target pixel [7, 8]. Custom 1×1/3×3/5×5 pixel apertures give 7.9/7.6/6.9 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 11 Gaia neighbors within 60 arcsec were tested for flux capability; 2 are capable. Nearest capable: G=16.33, 7.31 arcsec, requiring 41.0% intrinsic eclipse, 0.43 pixel from the deficit.
- Gaia geometry: selected edge-on conjunction offset -0.00905 in orbital phase, linear covariance scale 0.421 d. Approximate central duration 11.27 h versus observed median 9.70 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

Two G~16.3 neighbors at 7.3 and 9.5 arcsec are capable in flux and share a TESS pixel; the deficit centroid favors the target but does not securely resolve them. The sector-104 cycle-294 egress gap excludes that center from timing.

Obtain spatially resolved eclipse photometry, or a stronger difference image in a suitable sector.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/409852500/diff_s13.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet409852500/tesscut_s013.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.


Stable review key: R425. Public evidence files: [diff_s13.json](../../evidence/409852500/historical/diff_s13.json), [diff_s13.png](../../evidence/409852500/historical/diff_s13.png), [gaia.json](../../evidence/409852500/historical/gaia.json), [measurements.json](../../evidence/409852500/measurements.json), [pixel-evidence.json](../../evidence/409852500/pixel-evidence.json), [raw-events.png](../../evidence/409852500/raw-events.png), [raw-windows.csv](../../evidence/409852500/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
