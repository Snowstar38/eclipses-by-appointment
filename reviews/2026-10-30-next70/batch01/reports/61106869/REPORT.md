# TIC 61106869: CONFIRMED

Repeated deep eclipses localized to the target, a period measured from raw flux and independent photometric extraction support a target eclipsing binary. Review completed under `../../../BRIEF.md`; characterization limitations below do not erase this evidence.

Raw QLP SAP_FLUX, QUALITY=0, representative local quadratic-plus-trapezoid fits: 6 accepted events in sectors [45, 46, 72]; depths 74.83 to 77.12 ppt, durations 3.26 to 3.34 h. Eclipse-derived period 4.68300741 d, epoch 2528.126165 BTJD; timing residual RMS 0.29 min. No precision period error inferred. Lead inspected the first/last raw event panels; repeat eclipse structure survives local baselines. Underlying individual times, depths, fit edges and method: `../../raw-evidence/raw-events.json`; full20-event panel: plot ../../raw-evidence/raw-event-panels.png (excluded from this export).

Independent SPOC sector 45 raw SAP_FLUX reproduces depths 72.52, 71.66 ppt at the QLP event times. FITS TIC/sector and product URI were checked; QUALITY=0 where supplied. Product `mast:TESS/product/tess2021310001228-s0045-0000000061106869-0216-s_lc.fits`, SHA256 `e9466ed93ee390da900622a909075619a203070b8b73a24ee19840fa3aef301c`. Fixed QLP shape; reported product errors are uninflated formal errors, with aperture/dilution differences retained. Same TESS photons, independent reduction.

Difference imaging: cached sector45, 5 events, deficit-target distance3.24arcsec and peak[7, 7] versus target pixel[7, 7]. Lead visually inspected target and neighbour maps. No Gaia neighbour within the tested60arcsec cone can supply the eclipse at its catalogue G flux under a total-eclipse upper bound. See `../../source-review.json` and original pixel receipts in `../../raw-evidence/61106869/`; PSF residual0.216 is descriptive and includes field contamination.

Exact Gaia DR3 source3888846561563641088: SB1 P=4.68303722 +/- 0.000287749d, e=0.0376, omega=293.95deg. Closest conjunctionA at first fitted epoch: observed-minus-Gaia-0.0042d, linear full-covariance error0.1482d. The eclipse period projected back near BTJD389 gives offset+0.0094d. Conditional duration feasibility: observed median3.30h is below the central crossing estimate3.77h using TIC R1=1.00162Rsun, M1=1.134Msun and minimum companion mass0.255Msun with a main-sequence radius approximation. Shorter grazing chords are feasible. This is a consistency check, not a unique geometry fit. See `../../gaia-geometry.json` for covariance assumptions and alternatives.

No target prior EB established in the seven scoped checks; coverage limited to recorded services, identifiers and catalogue versions. SIMBAD primary is SB*, Gaia DR3 EB has no exact row; VSX exact rows: `[]`; ASAS-SN exact rows: `[]`. Prsa, IJspeert and vetted Kostov tables3/4 have recorded original five-arcsec negative checks; Kostov table2 candidates do not establish prior EB. Nearby catalogue variables are separate sources.  Provenance and limits: `../../../shared-catalogues/coverage-matrix.csv` and README.

Representative events use the original search cycle counts, native cadence without integration, and local quadratic baselines. Depths/durations are conditional measurements, not precision stellar parameters. Two-event ephemerides have no empirical residual uncertainty. Colour, aperture throughput, unresolved companions and untested faint/distant sources limit localization; no calibrated centroid error is claimed.

Next check: joint RV/eclipse analysis with improved stellar dimensions; revisit Gaia orbit drift where noted.


Public evidence: [Raw event measurements](../../raw-evidence/raw-events.json); [QLP provenance](../../raw-evidence/qlp-manifest.json); [Source review](../../source-review.json); [Gaia geometry](../../gaia-geometry.json); [Shared catalogue coverage](../../../shared-catalogues/README.md); [Export manifest](../../EXPORT-MANIFEST.json).
