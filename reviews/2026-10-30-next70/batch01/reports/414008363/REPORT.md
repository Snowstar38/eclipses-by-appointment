# TIC 414008363: CONFIRMED

Repeated deep eclipses localized to the target, a period measured from raw flux and independent photometric extraction support a target eclipsing binary. Review completed under `../../../BRIEF.md`; characterization limitations below do not erase this evidence.

Raw QLP SAP_FLUX, QUALITY=0, representative local quadratic-plus-trapezoid fits: 2 accepted events in sectors [91]; depths 78.79 to 79.39 ppt, durations 3.48 to 3.48 h. Eclipse-derived period 2.92040346 d, epoch 3778.236942 BTJD; timing residual RMS 0.00 min. No precision period error inferred. Lead inspected the first/last raw event panels; repeat eclipse structure survives local baselines. Underlying individual times, depths, fit edges and method: `../../raw-evidence/raw-events.json`; full20-event panel: plot ../../raw-evidence/raw-event-panels.png (excluded from this export).

Independent custom TESScut pixel extraction was rerun from `[local working path omitted; see provenance receipts]` using the new eclipse period and duration. Six quality-filtered events at cycles [0, 1, 4, 5, 6, 7] reproduce 3x3 aperture depths 69.50, 68.83, 69.93, 68.00, 68.15, 68.02 ppt. WCS places the exact Gaia target inside the 15x15 cutout, sector91; file hash and identity checks are in `414008363-pixel-provenance.json`. This is a distinct pixel extraction from QLP, not a separate archive SPOC product. Direct TESS-SPOC91 returned404; inventory requests timed out.

Difference imaging: cached sector91, 6 events, deficit-target distance1.91arcsec and peak[7, 8] versus target pixel[7, 8]. Lead visually inspected target and neighbour maps. No Gaia neighbour within the tested60arcsec cone can supply the eclipse at its catalogue G flux under a total-eclipse upper bound. See `../../source-review.json` and original pixel receipts in `../../raw-evidence/414008363/`; PSF residual0.332 is descriptive and includes field contamination.

Exact Gaia DR3 source4330700736708121216: SB1 P=2.92041761 +/- 6.44376e-05d, e=0.0119, omega=6.94deg. Closest conjunctionA at first fitted epoch: observed-minus-Gaia-0.0073d, linear full-covariance error0.0731d. The eclipse period projected back near BTJD389 gives offset+0.0091d. Conditional duration feasibility: observed median3.48h is below the central crossing estimate5.49h using TIC R1=1.83895Rsun, M1=1.118Msun and minimum companion mass0.687Msun with a main-sequence radius approximation. Shorter grazing chords are feasible. This is a consistency check, not a unique geometry fit. See `../../gaia-geometry.json` for covariance assumptions and alternatives.

No target prior EB established in the seven scoped checks; coverage limited to recorded services, identifiers and catalogue versions. SIMBAD primary is SB*, Gaia DR3 EB has no exact row; VSX exact rows: `[]`; ASAS-SN exact rows: `[]`. Prsa, IJspeert and vetted Kostov tables3/4 have recorded original five-arcsec negative checks; Kostov table2 candidates do not establish prior EB. Nearby catalogue variables are separate sources.  Provenance and limits: `../../../shared-catalogues/coverage-matrix.csv` and README.

Representative events use the original search cycle counts, native cadence without integration, and local quadratic baselines. Depths/durations are conditional measurements, not precision stellar parameters. Two-event ephemerides have no empirical residual uncertainty. Colour, aperture throughput, unresolved companions and untested faint/distant sources limit localization; no calibrated centroid error is claimed.

Next check: joint RV/eclipse analysis with improved stellar dimensions; revisit Gaia orbit drift where noted.


Public evidence: [Raw event measurements](../../raw-evidence/raw-events.json); [QLP provenance](../../raw-evidence/qlp-manifest.json); [Source review](../../source-review.json); [Gaia geometry](../../gaia-geometry.json); [Shared catalogue coverage](../../../shared-catalogues/README.md); [Export manifest](../../EXPORT-MANIFEST.json).
