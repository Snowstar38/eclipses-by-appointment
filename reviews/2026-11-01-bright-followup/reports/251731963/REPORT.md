# TIC 251731963: batch 02 review

**Physical verdict:** probable. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 18; Gaia DR3 source 4238560567095727744; actual DR3 G=12.032766. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 6 usable measured eclipse centers across sectors 54, 81; 6 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 130.91 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=4.733729823 ± 0.000031440 d and reference center BTJD 2772.728456. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=4.733742635 d; difference=-0.000013 d.
- Pixel attribution and alternative reduction: historical TESScut sector 81 stacked 4 eclipse windows; the flux-deficit centroid is 0.024 pixel from the Gaia target and the peak deficit pixel is [8, 7] versus target pixel [8, 7]. Custom 1×1/3×3/5×5 pixel apertures give 63.0/69.0/66.6 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 73 Gaia neighbors within 60 arcsec were tested for flux capability; 1 is capable. Nearest capable: G=12.27, 3.69 arcsec, requiring 27.5% intrinsic eclipse, 0.18 pixel from the deficit.
- Gaia geometry: selected edge-on conjunction offset +0.01300 in orbital phase, linear covariance scale 0.108 d. Approximate central duration 6.03 h versus observed median 4.40 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

A G=12.27 Gaia star 3.69 arcsec away can produce the dip with a ~27% intrinsic eclipse; the TESS pixel centroid cannot resolve the pair.

Resolve the two stars in higher-spatial-resolution time-series photometry at predicted eclipse times.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/251731963/diff_s81.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet251731963/tesscut_s081.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.


Stable review key: R427. Public evidence files: [diff_s81.json](../../evidence/251731963/historical/diff_s81.json), [diff_s81.png](../../evidence/251731963/historical/diff_s81.png), [gaia.json](../../evidence/251731963/historical/gaia.json), [measurements.json](../../evidence/251731963/measurements.json), [pixel-evidence.json](../../evidence/251731963/pixel-evidence.json), [raw-events.png](../../evidence/251731963/raw-events.png), [raw-windows.csv](../../evidence/251731963/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
