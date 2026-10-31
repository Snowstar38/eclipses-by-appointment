# TIC 314991763: CONFIRMED

Full bounded review: COMPLETE. All five checks were performed; scientific uncertainty is retained separately from execution completeness. Catalogue novelty is supplied by the shared scoped catalogue receipts and is not inferred from this physical classification.

1. **Raw repeated events: pass.** 6 usable free-center trapezoid fits to quality-zero raw QLP SAP_FLUX in sectors[56, 83] show localized eclipse morphology. Numeric raw-windows.csv and raw-events.png are deciding artifacts. Initial selection uses up to three widely separated available sectors; the two apparent two-event cases received bounded extra earlier-sector checks. Flagged and uncovered windows are never called clean negatives. A local linear baseline, depth, center, duration and ingress are fitted; no Gaia-fixed center is used as a measured midpoint.
2. **Eclipse timing: pass at the retained photometric cycle assignment.** P=7.7113830155 +/-0.0000099460d, epoch BTJD2833.13055669; epoch kind: Selected phase-zero eclipse; not assumed deepest primary. The legacy CSV name primary_epoch_btjd does not assert this is the deeper eclipse. Cycle assignments start from the historical photometric branch; an independently recomputed weighted linear fit reproduces all numbers. Deep primary phase0 and shallower secondary phase0.5 establish full orbital period. This is a bounded recurrence/morphology audit, not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS resolution with limitations below.** Identity: Gaia DR31777474556207679872; cutout WCS and selected target agree. Lost-light centroid is0.106px from target; peak[7, 7] versus target pixel[7, 7]. Historical PSF residual0.301. Capable-neighbour review: Gaia1777474590567419776 at56.26arcsec, required intrinsic fractional eclipse0.649, distance from deficit2.718px Required intrinsic eclipse fractions and observed blended-pixel fractional losses have different dilution and are not compared as a veto. No calibrated centroid confidence ellipse or precise exclusion probability is claimed.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut S56 gives1x1/3x3/5x5 aperture depths124.344/116.460/102.295ppt from4 stacked event(s). QLP fitted selected-event median is148.371ppt. These are reductions of the same TESS photons, not independent observations. Different apertures, dilution and possible mixed eclipse-kind stacks preclude a claim of equal intrinsic depth.
5. **Gaia orbital geometry: consistent within the stated bounded approximations.** Full NSS orbit: P=7.7109095009+/-0.0008394808d, e=0.012496, omega=74.8256deg, periastron BTJD388.328610. Measured-Gaia period difference0.00047351d. Closest edge-on conjunction offset0.126569d (0.016414phase); full covariance linear propagated error0.268207d at the measured epoch. Both conjunction branches and covariance details are retained in gaia-geometry.json. Mass function0.101794solar masses; assumed primary mass0.965, minimum companion mass0.640. Approximate central duration6.40h versus fitted median4.56h uses TIC radius and an assumed main-sequence minimum-mass companion, not a fitted geometry. There is no arbitrary sigma veto, and neither this duration estimate nor the formal timing error establishes precision orbital association.

**Limitations:** Unequal phase-zero primary and phase-half secondary establish the retained full orbital period. One capable neighbour at56.26arcsec is separated from the compact target deficit.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Fit-input error d|Depth ppt|
|---|---|---|---|---|
|56|0|2833.13069709|0.00115739|147.947|
|56|1|2840.84190758|0.00115739|149.606|
|56|2|2848.55321125|0.00115739|146.828|
|83|95|3565.71193913|0.00115739|147.737|
|83|96|3573.42338948|0.00115739|148.795|
|83|97|3581.13465312|0.00115739|150.942|

Provenance: measurements.json, raw-windows.csv, raw-events.png, historical/diff_s56.json and matching PNG/gaia.json; ../download-receipts.json, ../extra-downloads.json, ../alias-audit.json, ../recurrence-coverage.json, ../pixel-audit.json, ../gaia-geometry.json, ../HELPER-AUDIT.md, ../LEAD-AUDIT.md and ../SHA256SUMS.json. Original cutout: [local path omitted] Catalogue evidence: ../../catalogues/coverage-matrix.csv. Historical extraction definitions: [local path omitted] 5/made/sb1-scale/diffimg/diffstack.py. This reviewed evidence does not claim exhaustive literature priority.


Stable review key: R323. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/314991763) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
