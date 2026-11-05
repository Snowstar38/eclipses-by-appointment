# Independent helper audit: Q025, Q027, Q029

The helper examined fresh STScI TESSCut FFI cutouts using quality-zero frames and WCS pixel coordinates. The scripts and JSON in this directory contain precise aperture definitions, cadence counts, source ZIP SHA-256 hashes, and per-sector measurements. A loss image is median off-dip flux minus median in-dip flux, with local baselines. Positive centroids are diagnostic, not formal PSF fits; the TESS pixel scale leaves close or unresolved stars ambiguous.

## Q029 TIC 168657537

A Gaia DR3 cone query within 0.05 degrees (raw response `helper-q029-gaia.csv`) finds Gaia 4883892013333719680, G=12.869085, at 61.0113511652, -31.7568322887, approximately four pixels from target Gaia 4883891772815552000. Stacking 12 individually baseline-subtracted events per sector gives loss peaks at (9,10), (8,11), (9,11) in sectors 4, 5, 31 respectively, matching the neighbor's WCS (9.08,10.65), (8.18,11.47), (9.27,11.09), rather than the target at (7.09,7.20), (7.21,7.31), (7.45,7.56). Images and hashes: `helper-q029-difference.png`, `.json`, `.py`. WCS coordinates use Gaia catalog positions without a proper-motion propagation; the offset is multiple pixels.

Independent 3x3 apertures centered on each star give parity median depths in the neighbor aperture of 96.7/131.0 ppt (S4), 86.1/114.2 ppt (S5), and 83.4/91.5 ppt (S31). Target aperture corresponding values are -0.13/+0.04, -0.18/-0.11, +0.12/+0.12 ppt. See `helper-q029-apertures.py` and `.json`. The recurrent signal clearly favors the neighbor and does not establish eclipses of the selected Gaia source. Alternating depths are compatible with a 3.9269-day EB but are not a formal odd/even significance test and cannot independently exclude a 1.96345-day transit sequence. No claim that the selected star cannot have other eclipses follows.

## Q025 TIC 70887357

The single-event difference images in S5 and S32 peak at the target WCS pixel; positive centroids are 0.05 and 0.22 pixel from target respectively. They support target localization at TESS resolution, without excluding unresolved companions. `helper-q025-difference.py`, `.json`, `.png` give the event windows, 6/21 and 17/66 in/out cadence counts, and hashes. No independent alias/null analysis was completed. Published identity claims remain as separately documented in shared catalogue receipts.

## Q027 TIC 94255849

S10 and S100 single-event difference images peak at the target WCS pixel, with positive centroids 0.15 and 0.22 pixel from target, respectively. This supports target localization at TESS resolution, not exclusion of unresolved companions. `helper-q027-difference.py`, `.json`, `.png` give the event windows, 6/22 and 52/198 in/out cadence counts, and hashes. No independent alias/null or S101 analysis was completed.

Source cutouts were requested from `https://mast.stsci.edu/tesscut/api/v0.1/astrocut` for the exact target coordinates and sector, 15 by 15 pixels. Gaia CSV was obtained using ESA Gaia TAP DR3 cone query. Raw cutout ZIP hashes are in the associated JSON files.

## S94 common waveform

Independent quality-zero SAP comparison across Q021/Q024/Q026/Q028/Q030 shows a shared 0.241–0.255-day gap approximately BTJD 3875.79–3876.05 and normalized flux rising 2.4–4.5 ppt across it (adjacent 0.3-day medians). The common shape and step support a gap-linked artifact interpretation for those flagged features. Exact values, raw FITS hashes, and the overlay are in `helper-s94-comparison.json`, `.py`, `.png`. This does not rule out other source-specific eclipses.

Gaia cone response SHA-256: `d43406ae895ea9b9f7330634159954c8a4188f6bc2f7ee49088d02378bb4f80a`.

