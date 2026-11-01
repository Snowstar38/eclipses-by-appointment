# TIC 368260545: batch 02 review

**Physical verdict:** confirmed. **Full bounded review:** complete. **Catalogue scope:** no identified prior EB; seven-group coverage complete. Catalogue status is separate from physical classification.

Frozen queue position 11; Gaia DR3 source 4556083135603641856; actual DR3 G=12.021002. No replacement was made.

## Deciding evidence

- Raw QLP SAP flux: 8 usable measured eclipse centers across sectors 53, 80; 8 selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median 23.20 ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.
- Timing: measured same-kind centers give P=6.582836723 ± 0.000016330 d and reference center BTJD 2746.170982. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P=6.583413245 d; difference=-0.000577 d.
- Pixel attribution and alternative reduction: historical TESScut sector 53 stacked 4 eclipse windows; the flux-deficit centroid is 0.206 pixel from the Gaia target and the peak deficit pixel is [8, 8] versus target pixel [8, 8]. Custom 1×1/3×3/5×5 pixel apertures give 17.3/14.4/14.0 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. All 18 Gaia neighbors within 60 arcsec were tested for flux capability; 1 is capable. Nearest capable: G=12.30, 22.87 arcsec, requiring 5.4% intrinsic eclipse, 0.92 pixel from the deficit.
- Gaia geometry: selected edge-on conjunction offset -0.02615 in orbital phase, linear covariance scale 0.220 d. Approximate central duration 5.80 h versus observed median 5.57 h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.

## Limitations and next check

A similarly bright G=12.30 Gaia neighbor 22.87 arcsec away is flux-capable, but the deficit is 0.206 pixel from the target versus 0.92 pixel from that neighbor and peaks on the target pixel. A targeted recomputation of all four stacked windows puts every event deficit closer to the target (0.13–0.47 pixel) than the neighbor (0.75–1.07 pixel). Positional uncertainty remains descriptive rather than calibrated.

Additional pixel orientations or spatially resolved photometry can strengthen attribution and refine the ephemeris.

## Source provenance

Historical screening: `Fable 5\made\sb1-scale\c6-catrows.md` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `../../../../Fable 5/made/sb1-scale/diffimg/368260545/diff_s53.json` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `../../../../sky/data/sb1-scale-c3/vet368260545/tesscut_s053.fits`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`. Targeted four-window centroid audit: `pixel-event-audit.json`, reproduced by `../audit_368_pixels.py`.


Stable review key: R420. Public evidence files: [diff_s53.json](../../evidence/368260545/historical/diff_s53.json), [diff_s53.png](../../evidence/368260545/historical/diff_s53.png), [gaia.json](../../evidence/368260545/historical/gaia.json), [measurements.json](../../evidence/368260545/measurements.json), [pixel-event-audit.json](../../evidence/368260545/pixel-event-audit.json), [pixel-evidence.json](../../evidence/368260545/pixel-evidence.json), [raw-events.png](../../evidence/368260545/raw-events.png), [raw-windows.csv](../../evidence/368260545/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch02/INDEX.md). 
