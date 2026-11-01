# TIC 37531624: batch 02 review

**Physical verdict:** confirmed. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 14; Gaia DR3 source 5654299985347511552; actual DR3 G=12.022275. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 12 usable measured eclipse centers across sectors 35, 61, 62, 99; 12 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 121.06 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=6.308135631 ± 0.000005140 d and reference center BTJD 2273.441351. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=6.308348116 d; difference=-0.000212 d.
- Pixel attribution and alternative reduction: historical TESScut sector 61 stacked 4 eclipse windows; the flux-deficit centroid is 0.224 pixel from the Gaia target and the peak deficit pixel is [8, 7] versus target pixel [8, 7]. Custom 1×1/3×3/5×5 pixel apertures give 116.4/114.2/107.2 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 13 Gaia neighbors within 60 arcsec were tested for flux capability; 0 are capable. No Gaia neighbor is flux-capable.
- Gaia geometry: selected edge-on conjunction offset -0.00871 in orbital phase, linear covariance scale 0.079 d. Approximate central duration 4.47 h versus observed median 2.85 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

Representative-sector timing and pixel evidence; period uncertainty is formal fit/cadence with scatter inflation where needed, not calibrated total coverage.

Additional independent observations can refine the ephemeris and source attribution.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/37531624/diff_s61.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet37531624/tesscut_s061.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.


Stable review key: R423. Public evidence files: [diff_s61.json](../../evidence/37531624/historical/diff_s61.json), [diff_s61.png](../../evidence/37531624/historical/diff_s61.png), [gaia.json](../../evidence/37531624/historical/gaia.json), [measurements.json](../../evidence/37531624/measurements.json), [pixel-evidence.json](../../evidence/37531624/pixel-evidence.json), [raw-events.png](../../evidence/37531624/raw-events.png), [raw-windows.csv](../../evidence/37531624/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
