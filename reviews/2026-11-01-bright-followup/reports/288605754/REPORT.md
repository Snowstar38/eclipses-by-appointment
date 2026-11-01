# TIC 288605754: batch 02 review

**Physical verdict:** confirmed. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 17; Gaia DR3 source 5894485208091053056; actual DR3 G=12.027896. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 14 usable measured eclipse centers across sectors 11, 65, 99, 102; 14 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 72.32 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=5.334347769 ± 0.000004228 d and reference center BTJD 1608.607034. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=5.334169975 d; difference=+0.000178 d.
- Pixel attribution and alternative reduction: historical TESScut sector 65 stacked 5 eclipse windows; the flux-deficit centroid is 0.059 pixel from the Gaia target and the peak deficit pixel is [7, 7] versus target pixel [7, 7]. Custom 1×1/3×3/5×5 pixel apertures give 76.6/64.3/47.6 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 164 Gaia neighbors within 60 arcsec were tested for flux capability; 2 are capable. Nearest capable: G=13.72, 29.39 arcsec, requiring 41.2% intrinsic eclipse, 1.38 pixel from the deficit.
- Gaia geometry: selected edge-on conjunction offset +0.01007 in orbital phase, linear covariance scale 0.130 d. Approximate central duration 6.51 h versus observed median 4.38 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

Representative-sector timing and pixel evidence; period uncertainty is formal fit/cadence with scatter inflation where needed, not calibrated total coverage.

Additional independent observations can refine the ephemeris and source attribution.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/288605754/diff_s65.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet288605754/tesscut_s065.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.


Stable review key: R426. Public evidence files: [diff_s65.json](../../evidence/288605754/historical/diff_s65.json), [diff_s65.png](../../evidence/288605754/historical/diff_s65.png), [gaia.json](../../evidence/288605754/historical/gaia.json), [measurements.json](../../evidence/288605754/measurements.json), [pixel-evidence.json](../../evidence/288605754/pixel-evidence.json), [raw-events.png](../../evidence/288605754/raw-events.png), [raw-windows.csv](../../evidence/288605754/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
