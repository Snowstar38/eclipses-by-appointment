# T012  -  TIC 323458448

**Verdict:** CONFIRMED; bounded review COMPLETE. **Catalogue novelty:** UNKNOWN (shared catalogue review has four unavailable VizieR gates; see `../../shared-catalogues/REPORT.md`). The selection stratum is cross_method_dip; queue rank is not physical evidence.

## Deciding evidence

Raw SAP shows distinct deep eclipses S37 2326.1261 and S65 3075.9936, with S11 partial ingress; shallow events recur at S12 1646.5686, S64 3052.5299 and S93 3849.3225. Same-kind integer cycles are deep 0,16 and shallow 0,30,47. Independent fits give P_deep=46.866717+/-0.000229 d and P_shallow=46.866905+/-0.001243 d; the latter has up to 0.034 d residual from shape/sector variation. The S64 shallow-to-S65 deep spacing is 0.50065 of the measured full period; a P/2 timestamp interpretation would alternate stable ~60 and ~90 ppt depths, while the full period matches Gaia. S37 raw SAP is 90.58 ppt deep and an independent target-centered TESSCut raw-pixel aperture gives 89.16 ppt, with its difference centroid 0.089 px from target WCS. The sole ideal-G capable Gaia neighbor within 120 arcsec is 87.24 arcsec away, ~4.8 px from the deficit. Gaia edge-on conjunction phase offsets of measured events are about -0.004 to -0.013, compatible at the bounded approximation level. The initial pixel check baseline lay inside this 2.9 d eclipse and was corrected; it was not a null.

Raw SAP quality-zero local plots are `lead-raw-*.png`; the independent full-data diagnostic is `lead-fold.png`. `lead-numeric.json` records all screened flags and file/cadence hashes, `lead-timing.json` records curated same-kind clocks, `lead-coverage.json` records tested actual windows where applicable, and `lead-geometry.json` records the approximate Gaia conjunction comparison. Source-packet and shared-catalogue receipts are outside this batch folder; `../helper-audit.md` and helper artifacts document alternative reduction and source attribution where material. A corrected QLP flux and a custom TESSCut aperture share the same TESS photons.

## Limits and next check

The S11 deep event is partial and excluded from the precision fit. QLP corrected variants suppress the broad eclipse; period errors are conditional on selected cycle labels and uncalibrated sector systematics.

Acquire future raw photometry at both conjunctions to refine depths and the clock.
