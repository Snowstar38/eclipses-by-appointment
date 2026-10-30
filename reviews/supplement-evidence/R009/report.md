# TIC 451493289 (HD 142624): full attempted and adjudicated review

Verdict: CONFIRMED physical eclipsing target/system associated with the Gaia SB1. Repeated primary and secondary eclipses, orbital timing, independent photometry and localization support this classification. Exact component properties remain uncertain; this is not a catalogue edit or publication action.

## Deciding light-curve evidence

23 primary event fits pass the stated basic fit/coverage screen; the stricter cadence/gap screen retains 20. Median fitted primary depth is 33.18 ppt, with median conditional per-event depth error 0.16 ppt. Median T14/T12/T23 are 8.76/1.75/5.26 hours. These are fitted trapezoid descriptors; partial eclipses do not imply physical totality. Individual profile ranges, counts and gaps are in 451493289_measurements.json. Shape grids and baseline systematics limit errors, especially at profile boundaries.

25 secondary timing fits give median depth 3.16 ppt and phase 0.500165 +/- 0.00250 cycles. The latter is a conservative heuristic envelope from phase-grid resolution, width alternatives and leave-one-sector scatter, not a calibrated confidence interval. Fixed-phase/alternate-width controls and covered windows are preserved in secondary JSONs. Approximate small-e e*cos(omega) = +0.0003 +/- 0.0039; no trapezoid duration-ratio estimate of e*sin(omega) is claimed.

## Timing and Gaia

Primary T0 = 3106.41985304 +/- 0.00023937 BTJD, P = 6.940427624 +/- 0.000002516 d. Primary O-C rms 2.52 min. Covariance is scaled by max(1, chi-square/dof); stricter-mask P = 6.940428228 d. Secondary P = 6.940422652 +/- 0.000010554 d, O-C rms 8.17 min; primary-secondary difference -0.43 +/- 0.94 seconds/cycle. Covariances and all O-C values remain in JSON.

The Gaia comparison uses this source's full SB1 row, bit_index 127, its own 15-element correlation vector and the documented six-parameter order. The primary is +0.17 sigma from conjunction A near the Gaia epoch; photometric-Gaia period difference is -0.11 sigma. Per-sector A/B timing comparisons are saved. Physical-e rejection fraction 28.1% means the Gaussian orbit approximation is conditional and small-e priors remain soft.

## Independence, systematics and attribution

TESS-SPOC sector 12 independently recovers time-aligned dips: SAP 32.4 to 32.8 ppt and PDCSAP 35.1 to 35.5 ppt. Their difference is a dilution/detrending uncertainty, not evidence of absent eclipses. Raw QLP SAP with QUALITY=0 is the primary source; no post-gap trim was used. Flags, raw centroids, native-unit background excursions and gap coverage were examined. Background regression changes primary depths by at most 1.4%; this is a unit-free sensitivity check and does not convert SAP_BKG to fractional stellar flux. The joint model fits poorly near the catalog dimensions. A refined illustrative fit needs R1 about 2.52 Rsun, 0.75 times TIC 3.355 +/- 0.144 Rsun. This is a large unresolved stellar-dimension/model tension, not a measured correction to the catalogue. S93/S101 have extreme flagged excursions and S100/S102 depth/baseline changes.

The blind coarse-box census retains 28 peaks, 5 gap-flagged, and 0 classified off the two eclipse ephemerides. Its max(3 ppt, three flank-MAD) threshold is not a significance calibration or exhaustive shallow-event census. The valid prior difference-image receipt is reused, with on-target peak and small deficit-to-target offset (0.87 arcsec for 416525506, 1.63 for 451493289, 2.50 for 348737250). No new pixel cube was needed; this is explicitly prior attribution evidence. Fresh 60-arcsec Gaia neighbours and G-proxy dilution requirements are in neighbours-dilution.csv; aperture throughput, colour and unresolved companions remain limitations.

## Physics and archives

RV mass function 0.0240 Msun; using catalog M1=1.240, edge-on M2min=0.401 Msun and a=18.06 Rsun. A shared limb-darkened two-disc model was actually tested against both eclipse shapes, with finite-exposure sampling, radius/impact/e*sin(omega)/light-ratio freedom. Illustrative best k=0.170, b_A=0.16, R1 scale=0.75, R2=0.428 Rsun; diagnostic score 84.5 for 120 bins. Correlated bins, fixed limb darkening, local trends, no third light and coarse bounds prevent precision physical inference. This is a plausible geometry family, not independently measured masses/radii.

Fresh SIMBAD identifies the target SB*. ExoFOP has no TOI/CTOI. Successful IDIA cones find no target entry in ASAS-SN, SB9, WDS, Prsa, IJspeert or vetted Kostov table3/4. Kostov table2 is unvetted and is not prior confirmation; 372376841 appears there. Root's successful 60-arcsec VSX sweep returns 0 rows here: no eclipsing entry at this target. The 372 cone's known EB is the different 58-arcsec neighbour. Gaia vari_eclipsing_binary has no target row in the successful shared query. Exact TIC/main-name web searches found no relevant prior eclipsing record; 416's KIC11418931 is absent from the Kepler EB catalogue. This supports novelty only within the queried sources. Initial failed CDS queries were superseded by working mirrors, not treated as null results.

## Next eclipses and follow-up

After 2026-10-30: primary BTJD 4348.75640, 4355.69683, 4362.63725; secondary 4345.28679, 4352.22722, 4359.16764. Linear-covariance prediction errors can be optimistic; secondary scheduling allowance is at least about 25 minutes from the heuristic phase envelope, plus accumulated ephemeris uncertainty. Primary covariance propagation and sampling sensitivity are retained in the ephemeris files. Follow-up priorities are robust component radii/light ratios, baseline-sensitive events and calibrated multi-sector localization; they do not negate the repeated attributed eclipses.

Provenance: parent acquisition.csv/selected.json/prior-receipts.txt; full-vet scripts and per-target JSONs; successful archive response hashes; shared Gaia/VSX receipts. Sol lead reviewed code and compact evidence plus exactly two new pixel maps; Terra performed bulk extraction/model attempts. Original catalogue and work directories remain unchanged.
