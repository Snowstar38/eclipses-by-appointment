# H008 — TIC 322217134

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 2635952928569503232, SB1 period 32.39435 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 42, 70, 92.

## Deciding evidence

The s70 SAP event is a complete ~79 ppt flat-bottom eclipse with local fitted center BTJD 3232.1065. s92 descends around BTJD 3814.56–3814.79 and remains low to ~3815.3, consistent with another eclipse, but its egress is lost to quality-bit 1073741824 censoring; its fitted center is model-dependent. An 18-cycle assignment gives ~32.392 d, close to Gaia 32.39435 d, and the Gaia B conjunction is 0.0228 phase away. Other N15–N21 aliases have no independent sensitive nulls in cached sectors. TESSCut s70 aperture recovers 63.97 ppt from the same photons; difference flux peaks 0.036 pixel from target. A G=12.153 neighbor at 54.66 arcsec is in principle flux-capable but at a different WCS position.

## Limits and next check

Two-event cycle count remains untested by an independent clean occasion; no established period or precision epoch in result row. Source attribution is supported but lacks full PRF deblend. Observe a complete third same-kind event to settle cycle count and timing; deblend if publication depends on attribution.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/322217134/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.

`local-fits.json`, `cycle-coverage.json`, `alias-tests.json`, and helper attribution artifacts document the complete s70 event and censored s92 event. The conditional 18-cycle estimate is intentionally omitted from the result period field.

Current TESScut sector inventory returned HTTP 200 with sectors [42, 70, 92]; it lists no additional sector beyond the cached set. The query receipt and response hash are in `sector-availability.json` and `sector-availability.raw`.
