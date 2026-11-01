# TIC 142427408: batch 02 review

**Physical verdict:** confirmed. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 12; Gaia DR3 source 5711508945433894656; actual DR3 G=12.021337. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 19 usable measured eclipse centers across sectors 61, 88; 9 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 85.74 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=5.066684108 ± 0.000005802 d and reference center BTJD 2964.448321. Epoch kind: Selected deeper repeating eclipse; odd historical half-period cycles. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=5.066415582 d; difference=+0.000269 d.
- Pixel attribution and alternative reduction: historical TESScut sector 88 stacked 8 eclipse windows; the flux-deficit centroid is 0.172 pixel from the Gaia target and the peak deficit pixel is [8, 7] versus target pixel [8, 7]. Custom 1×1/3×3/5×5 pixel apertures give 53.3/37.1/18.8 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 71 Gaia neighbors within 60 arcsec were tested for flux capability; 7 are capable. Nearest capable: G=13.77, 27.00 arcsec, requiring 23.3% intrinsic eclipse, 1.42 pixel from the deficit.
- Gaia geometry: selected edge-on conjunction offset +0.03100 in orbital phase, linear covariance scale 0.240 d. Approximate central duration 8.26 h versus observed median 5.38 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

Representative-sector timing and pixel evidence; period uncertainty is formal fit/cadence with scatter inflation where needed, not calibrated total coverage. Alternating half-period events were separated by eclipse kind before orbital timing. Crowded pixel PSF fit is poor, but all flux-capable neighbors are at least 27 arcsec from the target and farther from the deficit.

Additional independent observations can refine the ephemeris and source attribution.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/142427408/diff_s88.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet142427408/tesscut_s088.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.


Stable review key: R421. Public evidence files: [diff_s88.json](../../evidence/142427408/historical/diff_s88.json), [diff_s88.png](../../evidence/142427408/historical/diff_s88.png), [gaia.json](../../evidence/142427408/historical/gaia.json), [measurements.json](../../evidence/142427408/measurements.json), [pixel-evidence.json](../../evidence/142427408/pixel-evidence.json), [raw-events.png](../../evidence/142427408/raw-events.png), [raw-windows.csv](../../evidence/142427408/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
