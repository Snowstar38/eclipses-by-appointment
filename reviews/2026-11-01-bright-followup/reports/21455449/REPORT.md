# TIC 21455449: batch 02 review

**Physical verdict:** confirmed. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 13; Gaia DR3 source 254615934869825920; actual DR3 G=12.021999. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 4 usable measured eclipse centers across sectors 73, 86; 4 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 10.61 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=11.596027763 ± 0.000084033 d and reference center BTJD 3288.685159. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=11.595182256 d; difference=+0.000846 d.
- Pixel attribution and alternative reduction: historical TESScut sector 73 stacked 2 eclipse windows; the flux-deficit centroid is 0.080 pixel from the Gaia target and the peak deficit pixel is [7, 8] versus target pixel [7, 8]. Custom 1×1/3×3/5×5 pixel apertures give 10.6/9.4/8.0 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 43 Gaia neighbors within 60 arcsec were tested for flux capability; 7 are capable. Nearest capable: G=16.92, 44.98 arcsec, requiring 87.2% intrinsic eclipse, 2.17 pixel from the deficit.
- Gaia geometry: selected edge-on conjunction offset +0.01425 in orbital phase, linear covariance scale 0.610 d. Approximate central duration 14.66 h versus observed median 4.72 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

Representative-sector timing and pixel evidence; period uncertainty is formal fit/cadence with scatter inflation where needed, not calibrated total coverage. Gaia duration estimate is crude and exceeds the observed narrow event; geometry phase and period remain consistent.

Additional independent observations can refine the ephemeris and source attribution.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/21455449/diff_s73.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet21455449/tesscut_s073.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.


Stable review key: R422. Public evidence files: [diff_s73.json](../../evidence/21455449/historical/diff_s73.json), [diff_s73.png](../../evidence/21455449/historical/diff_s73.png), [gaia.json](../../evidence/21455449/historical/gaia.json), [measurements.json](../../evidence/21455449/measurements.json), [pixel-evidence.json](../../evidence/21455449/pixel-evidence.json), [raw-events.png](../../evidence/21455449/raw-events.png), [raw-windows.csv](../../evidence/21455449/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
