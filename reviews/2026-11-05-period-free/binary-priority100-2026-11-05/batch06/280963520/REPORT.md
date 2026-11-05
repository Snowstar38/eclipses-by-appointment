# T057 - TIC 280963520

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 5409169159350357248, Gaia NSS SB1 period 32.953324685414955 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

The s9 short dips at 1552.681, 1553.431 and 1554.910 BTJD are separated by approximately two and four cycles of a 0.37530-d raw-flux periodogram peak. A short-period phase fold shows a coherent depression in raw SAP and the QLP corrected variant, so these cannot be dismissed as isolated noise or artifact. The s62 brightening is a different morphology and is not counted as an eclipse.

## Coverage, timing and attribution

7 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. Short-period variability, potentially a short-period eclipsing by-catch, has no secure source attribution or established orbital/eclipse kind. A raw s9 TESSCut pixel extraction is dominated by a sawtooth trend and does not validate the QLP depression. It does not establish an eclipse on the 32.95-d Gaia spectroscopic period. New s99 coverage exists, but that official TESSCut 5x5 target footprint has effectively zero flux and is not a sensitive recurrence test.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is in `../../shared-catalogues/gaia-neighbors.json`; source attribution and orbital geometry remain unresolved.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=144.7027809786175&dec=-49.51336098047716; newer sectors than cached QLP: [99]. Query response SHA-256: 6528fda2f6cc8166ba1ba50002a59472653b410ccc799c56b969dbc7e717e298.

## Limits and next check

Obtain calibrated target-pixel photometry to test 0.37530/0.75060-d aliases and locate the variable source.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 ee7b42d797b75bc4258e448f48e4e3a9903e5d6d51014f4665bc4d95415deb94). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.

## Additional short-period checks

The helper period search and s99 WCS/pixel audit are in `../helper-T057-numerics.json` and `../helper-T057-s99.json`, with scripts and hashes. The s99 target projects to pixel (2.122, 2.194), whose median flux is about -0.0004; columns 1-4 are near zero. This cutout cannot provide a null. `qlp-variant-fold.png` compares SAP and KSPSAP; the latter is another reduction within QLP of the same s9 photons. A separate s9 TESSCut extraction (`s09-pixels.json`, `s09-pixel-fold.png`) has real target flux but a strong raw sawtooth; it does not independently validate the short-period depression.
