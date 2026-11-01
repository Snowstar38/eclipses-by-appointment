# TIC 247204810: batch 02 review

**Physical verdict:** confirmed. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 20; Gaia DR3 source 1842700536609008000; actual DR3 G=12.034502. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 12 usable measured eclipse centers across sectors 15, 41, 82; 7 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 17.16 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=9.593093220 ± 0.000017436 d and reference center BTJD 1730.740727. Epoch kind: Selected deeper repeating eclipse; odd historical half-period cycles. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=9.594030212 d; difference=-0.000937 d.
- Pixel attribution and alternative reduction: historical TESScut sector 41 stacked 6 eclipse windows; the flux-deficit centroid is 0.192 pixel from the Gaia target and the peak deficit pixel is [8, 7] versus target pixel [8, 7]. Custom 1×1/3×3/5×5 pixel apertures give 15.4/15.3/14.4 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 42 Gaia neighbors within 60 arcsec were tested for flux capability; 5 are capable. Nearest capable: G=15.90, 17.29 arcsec, requiring 57.7% intrinsic eclipse, 1.07 pixel from the deficit.
- Gaia geometry: selected edge-on conjunction offset -0.01414 in orbital phase, linear covariance scale 0.111 d. Approximate central duration 10.53 h versus observed median 4.53 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

Representative-sector timing and pixel evidence; period uncertainty is formal fit/cadence with scatter inflation where needed, not calibrated total coverage. Alternating half-period events were separated by eclipse kind before orbital timing.

Additional independent observations can refine the ephemeris and source attribution.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/247204810/diff_s41.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet247204810/tesscut_s041.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.


Stable review key: R429. Public evidence files: [diff_s41.json](../../evidence/247204810/historical/diff_s41.json), [diff_s41.png](../../evidence/247204810/historical/diff_s41.png), [gaia.json](../../evidence/247204810/historical/gaia.json), [measurements.json](../../evidence/247204810/measurements.json), [pixel-evidence.json](../../evidence/247204810/pixel-evidence.json), [raw-events.png](../../evidence/247204810/raw-events.png), [raw-windows.csv](../../evidence/247204810/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
