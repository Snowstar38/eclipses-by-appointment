# Pilot photometric screen

The frozen screen processed all 37 reserved two-minute products from 20 TICs. There were no qualifying windows in the background, retained-loss or unexplained channels. No new events went to pixel follow-up. This was a convenience sample and the count applies only to the rule and coverage described here.

## Rule

The detector searches shared, finite, positive SAP and PDCSAP samples with finite SAP_BKG at QUALITY=0. It tests approximately 0.16–16 hour cores. A window needs at least 72% sampling of the core and each shoulder, at least five points per shoulder, and three truly consecutive SAP points deeper than 10 ppt and five local shoulder scatter estimates. The measured mean SAP loss must also exceed both thresholds. The search can bridge small gaps, while the consecutive-point requirement cannot.

The FITS units of SAP and SAP_BKG must agree. Individual linear baselines use robust block medians from the same shoulders. Restored-flux loss is the negative of the sum of the measured SAP and SAP_BKG residuals, normalized to the local SAP baseline. SAP is the normalization because the un-subtracted flux includes sky and does not represent the stellar baseline. The effective uncertainty uses point and short-block scatter combined with the difference between the shoulders. It is an operational scale rather than a calibrated confidence interval.

A background excess must exceed five estimated uncertainties and 5 ppt of baseline SAP. A retained-loss run takes priority over a background label, allowing a real source dip with a simultaneous background excess to survive. A formal background-closure event needs an excess and restored-loss magnitude plus three estimated uncertainties within max(5 ppt, 12% of the SAP loss). A restored gain exceeding 5 ppt receives an overclosure flag. For an overclosure or noisy window, source effects can be masked. Events with substantial residual flux loss have a retained-loss classification even with a simultaneous background excess. Ambiguous windows retain their own labels.

## Controls and revision

| Control | Frozen outcome |
| --- | --- |
| TIC 113655666, sector 43, Phocaea | Recovered in the core that includes the prior BTJD 2491.27973 center. The automatic window centers at 2491.29779, with SAP loss 83.71 and restored loss −3.85 ppt. Background closure in that automated window. The separate native pixel control shows a small positive restored gain with the original fixed core and different shoulders. |
| TIC 356752132, sector 42, Brixia | Recovered at BTJD 2454.76369 with SAP loss 397.54 and restored loss −21.50 ppt. Background overclosure. |
| HD 276904, sector 59 short clock | All 17 published primary times have an automatic retained-loss window within 0.10 d, with restored losses of 19.6–29.9 ppt. |
| HD 276904, sector 59 separate deep event | Retained loss at BTJD 2917.72819. SAP loss 332.23 ppt and restored loss 333.66 ppt. |

The initial detector split on any missing cadence and missed Phocaea because gaps occur immediately after its core. It recovered Brixia and the HD 276904 deep event. The v2 revision was led by the control results and widened the minimum shoulders, allowed brief quality gaps under the explicit coverage tests, and added the overclosure label. The project lead saw v1 fresh-sample output before v2 was frozen. The photometry analyst did not inspect fresh-sample event classifications during tuning, so the event-level result should be read as a pilot rather than a fully blinded holdout. The six v1-only fresh windows are retained for a sensitivity audit. All had just three consecutive points at the smallest tested scale, all were unexplained in v1, and none met frozen v2 fixed-window remeasurement. Only the native sector 59 product was used for HD 276904. Its sector 73 and 86 confirmations are full-frame products outside this pilot.

Synthetic pure background and background with 45 and 90 ppt coincident source eclipses were separately passed through the complete detector. The background-only injection closed and both mixed injections retained source loss. A fixed-noise follow-up grid retained coincident source peaks from 5 ppt for equal widths and 6 ppt for a 0.35-width eclipse. Smaller source dips could be classified as background closure under this setup. This grid describes one clean noise realization for each profile and gives no completeness estimate for real products.

## Coverage and receipts

The 37 products contain 709,789 archive rows and 410,840 usable quality-zero cadences. At the shortest scale, 401,373 usable centers have nominal core and shoulder geometric support before detailed fractional coverage checks, equivalent to about 557.5 aperture-days at the native cadence. At 16 hours there are 224,512 eligible centers. These are cadence-based exposures, not independent trials.

- Frozen v2 analysis source SHA-256 16a8c39aca6a70e777b3003eca7939a69e394a01acf81a9d32cc5c9c8f09dc69
- Portable screen.py SHA-256 69052864d584815222a13eb05275e9b94ace54608347933eede94c09f606ba36
- Reserved batch.csv SHA-256 20a5e343c0689c763a73fc2067e6f354ae2f3c0849b1e93eed72c8a1c244a27
- pilot-coverage.json contains every archive and replay URL, FITS SHA-256, units and scale-dependent coverage.
- controls-events.csv and controls-coverage.json contain the automatic control measurements.
- pilot-pixel-candidates.csv contains the schema and zero candidate rows. diagnostic-v1-only.csv is a separate sensitivity table with replay links.
- injection.json and injection-grid.csv contain the synthetic recovery measurements.

## Replay

The portability update changes the input, cache and output handling. It verifies replayed FITS against published SHA-256 hashes and writes schema headers even when no events are found. Detection, classification, numerical helpers, constants, timing conversion and synthetic controls were compared directly with the frozen source and remain identical. Published event and coverage files are preserved.

From the directory containing screen.py and the coverage receipts, run the following commands. Python requires numpy, pandas, requests, astropy and scipy.

```text
python screen.py --output-dir replay
python screen.py --controls --output-dir replay
```

Receipt lookup defaults to pilot-coverage.json or controls-coverage.json beside the script. Use `--coverage PATH` for a receipt stored elsewhere. A new roster can be run with `--index PATH --batch PATH`, using a SPOC LC CSV or CSV.gz index with tic, sector and file columns. Use `--cache PATH` or set `TESS_BACKGROUND_CACHE` to override the cache. The default is under LOCALAPPDATA on Windows, under XDG_CACHE_HOME on supported systems when set, or under the current user's .cache directory otherwise. Importing screen.py creates no directories.
