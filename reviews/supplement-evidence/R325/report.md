# TIC 115048464: CONFIRMED

Full bounded review: COMPLETE. All five checks were performed; scientific uncertainty is retained separately from execution completeness. Catalogue novelty is supplied by the shared scoped catalogue receipts and is not inferred from this physical classification.

1. **Raw repeated events: pass.** 7 usable free-center trapezoid fits to quality-zero raw QLP SAP_FLUX in sectors[19, 45, 86] show localized eclipse morphology. Numeric raw-windows.csv and raw-events.png are deciding artifacts. Initial selection uses up to three widely separated available sectors; the two apparent two-event cases received bounded extra earlier-sector checks. Flagged and uncovered windows are never called clean negatives. A local linear baseline, depth, center, duration and ingress are fitted; no Gaia-fixed center is used as a measured midpoint.
2. **Eclipse timing: pass at the retained photometric cycle assignment.** P=8.0142430574 +/-0.0000142842d, epoch BTJD1832.46809862; epoch kind: Selected phase-zero eclipse; not assumed deepest primary. The legacy CSV name primary_epoch_btjd does not assert this is the deeper eclipse. Cycle assignments start from the historical photometric branch; an independently recomputed weighted linear fit reproduces all numbers. Representative raw events support same event kind at retained photometric period; no persistent unequal alternating sequence seen. The measured period is seeded by the historical photometric branch, not an exhaustive alias search. This is a bounded recurrence/morphology audit, not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS resolution with limitations below.** Identity: Gaia DR3183073672486786048; cutout WCS and selected target agree. Lost-light centroid is0.201px from target; peak[7, 8] versus target pixel[7, 8]. Historical PSF residual0.791. Capable-neighbour review: Gaia183073775565996672 at51.03arcsec, required intrinsic fractional eclipse0.682, distance from deficit2.572px Required intrinsic eclipse fractions and observed blended-pixel fractional losses have different dilution and are not compared as a veto. No calibrated centroid confidence ellipse or precise exclusion probability is claimed.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut S19 gives1x1/3x3/5x5 aperture depths37.833/39.394/37.099ppt from4 stacked event(s). QLP fitted selected-event median is37.720ppt. These are reductions of the same TESS photons, not independent observations. Different apertures, dilution and possible mixed eclipse-kind stacks preclude a claim of equal intrinsic depth.
5. **Gaia orbital geometry: consistent within the stated bounded approximations.** Full NSS orbit: P=8.0157041322+/-0.0019466464d, e=0.050791, omega=286.7691deg, periastron BTJD386.221698. Measured-Gaia period difference-0.00146107d. Closest edge-on conjunction offset-0.176019d (-0.021959phase); full covariance linear propagated error0.411170d at the measured epoch. Both conjunction branches and covariance details are retained in gaia-geometry.json. Mass function0.0445999solar masses; assumed primary mass1.150, minimum companion mass0.494. Approximate central duration8.19h versus fitted median4.70h uses TIC radius and an assumed main-sequence minimum-mass companion, not a fitted geometry. There is no arbitrary sigma veto, and neither this duration estimate nor the formal timing error establishes precision orbital association.

**Limitations:** Fitted duration and depth change across cadence/sector apertures; no precision intrinsic depth or common duration is claimed. The capable neighbour at51.03arcsec is separated from the target-core deficit.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Fit-input error d|Depth ppt|
|---|---|---|---|---|
|19|1|1832.46619041|0.01041680|34.249|
|19|2|1840.48508416|0.01041680|34.439|
|45|88|2529.70702596|0.00347237|37.720|
|45|89|2537.72076455|0.00347237|36.060|
|45|90|2545.73653228|0.00347237|38.423|
|86|227|3643.68701982|0.00115743|37.903|
|86|229|3659.71553079|0.00115743|38.378|

Provenance: measurements.json, raw-windows.csv, raw-events.png, historical/diff_s19.json and matching PNG/gaia.json; ../download-receipts.json, ../extra-downloads.json, ../alias-audit.json, ../recurrence-coverage.json, ../pixel-audit.json, ../gaia-geometry.json, ../HELPER-AUDIT.md, ../LEAD-AUDIT.md and ../SHA256SUMS.json. Original cutout: [local path omitted] Catalogue evidence: ../../catalogues/coverage-matrix.csv. Historical extraction definitions: [local path omitted] 5/made/sb1-scale/diffimg/diffstack.py. This reviewed evidence does not claim exhaustive literature priority.


Stable review key: R325. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/115048464) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
