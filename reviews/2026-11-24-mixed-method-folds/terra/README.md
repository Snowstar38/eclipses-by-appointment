# Independent visual assessment

Reviewed all ten apertures on original QLP time axes and on the archived screening ephemeris. No target shows a convincing pair of matching, discrete, well-bracketed eclipses by visual inspection. This is a morphology assessment of these available aperture curves, not proof that the Gaia SB1 systems do not eclipse. No source localization was attempted because no sufficiently compelling repeated event survived this review.

| TIC | Visual reading |
|---|---|
| 135180054 | S23 near BTJD 1930.46 has enormous bipolar scatter, not a resolved, bracketing eclipse; the S50 predicted window is cut off at the sector boundary. Not a repeat. |
| 347447876 | S34 at 2252.68 has large bipolar scatter at the sector edge, with different SAP/corrected excursions. S8 and S61 predicted windows are incomplete. No resolved repeat. |
| 302399892 | Eight sectors have no obvious discrete deep event. Predicted windows show noise, incomplete coverage or a gap; S59 window is at the edge. |
| 14832729 | Seven sectors mostly quiet. The S75 predicted window shows a shallow, noisy depression, but S41 is disturbed and S15, S55 and S82 are incomplete; no convincing repeat. |
| 191231056 | S17 at 1773.29 shows large bipolar disturbed scatter near a long gap, not a clean eclipse. S57 prediction is quiet, S84 has a gap. |
| 197243461 | S45 predicted window has a small corrected dip with a SAP brightening immediately after, amid a disturbance; S72 has no clear match. No compelling repeat. |
| 390126467 | Nine sectors show no obvious deep discrete event; predicted S26, S41, S54 and S81 windows are noisy/quiet without matching morphology. |
| 388584591 | Eleven sectors show no obvious deep discrete event; several predicted windows are covered but lack a convincing repeated shape. |
| 244201152 | S42 predicted window lies in an unstable sector end; S3 and S30 do not show matching events. Fold around phase 0.2 is not visually established as a repeat. |
| 323600657 | S34 and S44 predictions are incompletely covered; S72 is noisy and shows no convincing discrete dip. No repeated event. |

`<tic>.png` plots the quality-filtered original time series by sector and folded at the archived period with arbitrary phase zero. `<tic>-windows.png` displays all predicted windows with at least three simultaneous finite positive SAP and corrected measurements within 0.7 days; red shading is the original box duration. `archived_clocks.csv` records the period, epoch, duration and plotted-window count derived from the shared `../ground/archived-clocks.csv`; that table records the frozen archive input hashes. Black is corrected QLP (KSPSAP or DET_FLUX), blue is SAP. Each flux column was independently normalized with a two-day running median. This can suppress broad changes and creates edge effects. Plots clip vertical axes at robust percentiles, and retain only positive flux in both columns; thus they do not display every extreme or invalid point. Window count does not imply complete eclipse coverage. Time BTJD, residual ppt. No independent short-period search was undertaken, and a shallow or differently phased event is not excluded.

Run `python review.py --cache /path/to/cadences` and `python windows.py --cache /path/to/cadences`. Alternatively set `MIXED_FOLD_CACHE`; the default is `../sol/cadences`. The cache contains per-sector NPZ files with `t`, `sap`, `pdc` arrays, and can be rebuilt using `../sol/build_cache.py` as described in the sol README. Source files and hashes are maintained in the companion sol manifest. The archival JSON stores fit measurements rather than a saved folded array; the plots reconstruct the screening-period fold from the available original series, not a verbatim historical folded product. This analysis includes later sectors in addition to archive inputs, as available on the cache date.
