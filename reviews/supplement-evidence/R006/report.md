# TIC 295945076 (TYC 5969-485-1): full attempted and adjudicated review

Verdict: CONFIRMED physical eclipsing target/system associated with the Gaia SB1. Repeated primary and secondary eclipses, orbital timing, independent photometry and localization support this classification. Exact component properties remain uncertain; this is not a catalogue edit or publication action.

## Deciding light-curve evidence

13 primary event fits pass the stated basic fit/coverage screen; the stricter cadence/gap screen retains 10. Median fitted primary depth is 32.32 ppt, with median conditional per-event depth error 0.51 ppt. Median T14/T12/T23 are 3.12/1.25/0.65 hours. These are fitted trapezoid descriptors; partial eclipses do not imply physical totality. Individual profile ranges, counts and gaps are in 295945076_measurements.json. Shape grids and baseline systematics limit errors, especially at profile boundaries.

16 secondary timing fits give median depth 21.64 ppt and phase 0.521923 +/- 0.00250 cycles. The latter is a conservative heuristic envelope from phase-grid resolution, width alternatives and leave-one-sector scatter, not a calibrated confidence interval. Fixed-phase/alternate-width controls and covered windows are preserved in secondary JSONs. Approximate small-e e*cos(omega) = +0.0344 +/- 0.0039; no trapezoid duration-ratio estimate of e*sin(omega) is claimed.

## Timing and Gaia

Primary T0 = 2217.12888360 +/- 0.00030392 BTJD, P = 5.908926218 +/- 0.000002164 d. Primary O-C rms 1.37 min. Covariance is scaled by max(1, chi-square/dof); stricter-mask P = 5.908927003 d. Secondary P = 5.908926897 +/- 0.000002068 d, O-C rms 1.65 min; primary-secondary difference +0.06 +/- 0.26 seconds/cycle. Covariances and all O-C values remain in JSON.

The Gaia comparison uses this source's full SB1 row, bit_index 127, its own 15-element correlation vector and the documented six-parameter order. The primary is +1.41 sigma from conjunction A near the Gaia epoch; photometric-Gaia period difference is -0.35 sigma. Per-sector A/B timing comparisons are saved. Physical-e rejection fraction 0.0% means the Gaussian orbit approximation is conditional and small-e priors remain soft.

## Independence, systematics and attribution

TESS-SPOC sector 34 independently recovers time-aligned dips: SAP 29.1 to 31.1 ppt and PDCSAP 33.5 to 35.3 ppt. Their difference is a dilution/detrending uncertainty, not evidence of absent eclipses. Raw QLP SAP with QUALITY=0 is the primary source; no post-gap trim was used. Flags, raw centroids, native-unit background excursions and gap coverage were examined. Background regression changes primary depths by at most 1.2%; this is a unit-free sensitivity check and does not convert SAP_BKG to fractional stellar flux. The secondary is at phase 0.52192, not the Gaia median 0.53683. The difference is about 1.7 sigma after the heuristic timing envelope; the Gaia orbit is not contradicted. Sector 87 has baseline/depth shifts. The grazing solution has no securely measured totality.

The blind coarse-box census retains 29 peaks, 3 gap-flagged, and 0 classified off the two eclipse ephemerides. Its max(3 ppt, three flank-MAD) threshold is not a significance calibration or exhaustive shallow-event census. Fresh TESScut template fitting in sector 34 uses two events. The target is preferred to all listed neighbours; free and split-event PSF centroids lie within about 0.07 pixel of the catalogue position. These are unweighted Gaussian-PSF/WCS diagnostics, not calibrated localization sigma. Fresh 60-arcsec Gaia neighbours and G-proxy dilution requirements are in neighbours-dilution.csv; aperture throughput, colour and unresolved companions remain limitations.

## Physics and archives

RV mass function 0.1309 Msun; using catalog M1=1.188, edge-on M2min=0.804 Msun and a=17.31 Rsun. A shared limb-darkened two-disc model was actually tested against both eclipse shapes, with finite-exposure sampling, radius/impact/e*sin(omega)/light-ratio freedom. Illustrative best k=0.390, b_A=1.12, R1 scale=0.85, R2=0.602 Rsun; diagnostic score 98.4 for 120 bins. Correlated bins, fixed limb darkening, local trends, no third light and coarse bounds prevent precision physical inference. This is a plausible geometry family, not independently measured masses/radii.

Fresh SIMBAD identifies the target SB*. ExoFOP has no TOI/CTOI. Successful IDIA cones find no target entry in ASAS-SN, SB9, WDS, Prsa, IJspeert or vetted Kostov table3/4. Kostov table2 is unvetted and is not prior confirmation; 372376841 appears there. Root's successful 60-arcsec VSX sweep returns 0 rows here: no eclipsing entry at this target. The 372 cone's known EB is the different 58-arcsec neighbour. Gaia vari_eclipsing_binary has no target row in the successful shared query. Exact TIC/main-name web searches found no relevant prior eclipsing record; 416's KIC11418931 is absent from the Kepler EB catalogue. This supports novelty only within the queried sources. Initial failed CDS queries were superseded by working mirrors, not treated as null results.

## Next eclipses and follow-up

After 2026-10-30: primary BTJD 4344.34232, 4350.25125, 4356.16017; secondary 4347.42653, 4353.33546, 4359.24439. Linear-covariance prediction errors can be optimistic; secondary scheduling allowance is at least about 21 minutes from the heuristic phase envelope, plus accumulated ephemeris uncertainty. Primary covariance propagation and sampling sensitivity are retained in the ephemeris files. Follow-up priorities are robust component radii/light ratios, baseline-sensitive events and calibrated multi-sector localization; they do not negate the repeated attributed eclipses.

Provenance: parent acquisition.csv/selected.json/prior-receipts.txt; full-vet scripts and per-target JSONs; successful archive response hashes; shared Gaia/VSX receipts. Sol lead reviewed code and compact evidence plus exactly two new pixel maps; Terra performed bulk extraction/model attempts. Original catalogue and work directories remain unchanged.
