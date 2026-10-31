# TIC 47653432: CONFIRMED

Full bounded review: COMPLETE. All five checks were performed; scientific uncertainty is retained separately from execution completeness. Catalogue novelty is supplied by the shared scoped catalogue receipts and is not inferred from this physical classification.

1. **Raw repeated events: pass.** 10 usable free-center trapezoid fits to quality-zero raw QLP SAP_FLUX in sectors[65, 102] show localized eclipse morphology. Numeric raw-windows.csv and raw-events.png are deciding artifacts. Initial selection uses up to three widely separated available sectors; the two apparent two-event cases received bounded extra earlier-sector checks. Flagged and uncovered windows are never called clean negatives. A local linear baseline, depth, center, duration and ingress are fitted; no Gaia-fixed center is used as a measured midpoint.
2. **Eclipse timing: pass at the retained photometric cycle assignment.** P=4.1981909010 +/-0.0000097735d, epoch BTJD3071.05142551; epoch kind: Selected phase-zero eclipse; not assumed deepest primary. The legacy CSV name primary_epoch_btjd does not assert this is the deeper eclipse. Cycle assignments start from the historical photometric branch; an independently recomputed weighted linear fit reproduces all numbers. Representative raw events support same event kind at retained photometric period; no persistent unequal alternating sequence seen. The measured period is seeded by the historical photometric branch, not an exhaustive alias search. This is a bounded recurrence/morphology audit, not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS resolution with limitations below.** Identity: Gaia DR36215660903952193536; cutout WCS and selected target agree. Lost-light centroid is0.148px from target; peak[7, 7] versus target pixel[7, 7]. Historical PSF residual0.358. Capable-neighbour review: Gaia6215657949014886144 at43.41arcsec, required intrinsic fractional eclipse0.060, distance from deficit2.162px; Gaia6215657949014692480 at44.25arcsec, required intrinsic fractional eclipse0.395, distance from deficit2.101px; Gaia6215666779467456384 at48.79arcsec, required intrinsic fractional eclipse0.599, distance from deficit2.434px; Gaia6215663824529954048 at52.66arcsec, required intrinsic fractional eclipse0.368, distance from deficit2.626px Required intrinsic eclipse fractions and observed blended-pixel fractional losses have different dilution and are not compared as a veto. No calibrated centroid confidence ellipse or precise exclusion probability is claimed.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut S38 gives1x1/3x3/5x5 aperture depths4.853/4.373/4.511ppt from6 stacked event(s). QLP fitted selected-event median is5.090ppt. These are reductions of the same TESS photons, not independent observations. Different apertures, dilution and possible mixed eclipse-kind stacks preclude a claim of equal intrinsic depth.
5. **Gaia orbital geometry: consistent within the stated bounded approximations.** Full NSS orbit: P=4.1924134926+/-0.0013497127d, e=0.059512, omega=347.9732deg, periastron BTJD390.987237. Measured-Gaia period difference0.00577741d. Closest edge-on conjunction offset0.002164d (0.000516phase); full covariance linear propagated error0.827753d at the measured epoch. Both conjunction branches and covariance details are retained in gaia-geometry.json. Mass function0.0131992solar masses; assumed primary mass1.120, minimum companion mass0.298. Approximate central duration5.17h versus fitted median1.54h uses TIC radius and an assumed main-sequence minimum-mass companion, not a fitted geometry. There is no arbitrary sigma veto, and neither this duration estimate nor the formal timing error establishes precision orbital association.

**Limitations:** Shallow4–7ppt locally normalized events recur with resolved localized shape; the whole-sector raw fold is dominated by baseline trends. Four capable neighbours are43arcsec or farther away from the compact target deficit. Observed duration about1.54h versus approximate central5.17h can arise from projected chord/radius assumptions; no measured central-duration match is claimed.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

|Sector|Historical photometric cycle|Measured midpoint BTJD|Fit-input error d|Depth ppt|
|---|---|---|---|---|
|65|350|3071.04936256|0.00145452|6.443|
|65|351|3075.25496995|0.00144651|4.476|
|65|352|3079.44977713|0.00323568|5.037|
|65|354|3087.83567116|0.00255968|4.452|
|65|355|3092.04090879|0.00174376|6.818|
|102|602|4128.99742687|0.00211025|4.569|
|102|603|4133.18963558|0.00185280|5.143|
|102|604|4137.39225828|0.00153892|4.359|
|102|605|4141.59166940|0.00215224|6.258|
|102|607|4149.98812063|0.00235392|5.212|

Provenance: measurements.json, raw-windows.csv, raw-events.png, historical/diff_s38.json and matching PNG/gaia.json; ../download-receipts.json, ../extra-downloads.json, ../alias-audit.json, ../recurrence-coverage.json, ../pixel-audit.json, ../gaia-geometry.json, ../HELPER-AUDIT.md, ../LEAD-AUDIT.md and ../SHA256SUMS.json. Original cutout: [local path omitted] Catalogue evidence: ../../catalogues/coverage-matrix.csv. Historical extraction definitions: [local path omitted] 5/made/sb1-scale/diffimg/diffstack.py. This reviewed evidence does not claim exhaustive literature priority.


Stable review key: R321. [Deciding evidence](../../evidence/47653432/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
