# TIC 416525506 (TYC 3566-1556-1): full attempted and adjudicated review

Verdict: CONFIRMED physical eclipsing target/system associated with the Gaia SB1. Repeated primary and secondary eclipses, orbital timing, independent photometry and localization support this classification. Exact component properties remain uncertain; this is not a catalogue edit or publication action.

## Deciding light-curve evidence

51 primary event fits pass the stated basic fit/coverage screen; the stricter cadence/gap screen retains 49. Median fitted primary depth is 33.54 ppt, with median conditional per-event depth error 0.60 ppt. Median T14/T12/T23 are 3.00/1.05/0.83 hours. These are fitted trapezoid descriptors; partial eclipses do not imply physical totality. Individual profile ranges, counts and gaps are in 416525506_measurements.json. Shape grids and baseline systematics limit errors, especially at profile boundaries.

49 secondary timing fits give median depth 2.52 ppt and phase 0.499824 +/- 0.00250 cycles. The latter is a conservative heuristic envelope from phase-grid resolution, width alternatives and leave-one-sector scatter, not a calibrated confidence interval. Fixed-phase/alternate-width controls and covered windows are preserved in secondary JSONs. Approximate small-e e*cos(omega) = -0.0003 +/- 0.0039; no trapezoid duration-ratio estimate of e*sin(omega) is claimed.

## Timing and Gaia

Primary T0 = 2840.07978816 +/- 0.00013162 BTJD, P = 4.895374455 +/- 0.000001051 d. Primary O-C rms 1.35 min. Covariance is scaled by max(1, chi-square/dof); stricter-mask P = 4.895374539 d. Secondary P = 4.895396424 +/- 0.000011483 d, O-C rms 16.93 min; primary-secondary difference +1.90 +/- 1.00 seconds/cycle. Covariances and all O-C values remain in JSON.

The Gaia comparison uses this source's full SB1 row, bit_index 127, its own 15-element correlation vector and the documented six-parameter order. The primary is +0.25 sigma from conjunction A near the Gaia epoch; photometric-Gaia period difference is -0.19 sigma. Per-sector A/B timing comparisons are saved. Physical-e rejection fraction 33.9% means the Gaussian orbit approximation is conditional and small-e priors remain soft.

## Independence, systematics and attribution

TESS-SPOC sector 15 independently recovers time-aligned dips: SAP 31.9 to 37.0 ppt and PDCSAP 32.9 to 39.3 ppt. Their difference is a dilution/detrending uncertainty, not evidence of absent eclipses. Raw QLP SAP with QUALITY=0 is the primary source; no post-gap trim was used. Flags, raw centroids, native-unit background excursions and gap coverage were examined. Background regression changes primary depths by at most 14.4%; this is a unit-free sensitivity check and does not convert SAP_BKG to fractional stellar flux. S55 cycle 232 is background-sensitive: raw 32.55 versus background-regressed 37.23 ppt. Excluding it changes P by only 0.0048 seconds. It is retained as an affected event, not pristine evidence.

The blind coarse-box census retains 45 peaks, 0 gap-flagged, and 0 classified off the two eclipse ephemerides. Its max(3 ppt, three flank-MAD) threshold is not a significance calibration or exhaustive shallow-event census. The valid prior difference-image receipt is reused, with on-target peak and small deficit-to-target offset (0.87 arcsec for 416525506, 1.63 for 451493289, 2.50 for 348737250). No new pixel cube was needed; this is explicitly prior attribution evidence. Fresh 60-arcsec Gaia neighbours and G-proxy dilution requirements are in neighbours-dilution.csv; aperture throughput, colour and unresolved companions remain limitations.

## Physics and archives

RV mass function 0.0091 Msun; using catalog M1=1.117, edge-on M2min=0.258 Msun and a=13.49 Rsun. A shared limb-darkened two-disc model was actually tested against both eclipse shapes, with finite-exposure sampling, radius/impact/e*sin(omega)/light-ratio freedom. Illustrative best k=0.214, b_A=0.88, R1 scale=1.00, R2=0.289 Rsun; diagnostic score 50.0 for 120 bins. Correlated bins, fixed limb darkening, local trends, no third light and coarse bounds prevent precision physical inference. This is a plausible geometry family, not independently measured masses/radii.

Fresh SIMBAD identifies the target SB*. ExoFOP has no TOI/CTOI. Successful IDIA cones find no target entry in ASAS-SN, SB9, WDS, Prsa, IJspeert or vetted Kostov table3/4. Kostov table2 is unvetted and is not prior confirmation; 372376841 appears there. Root's successful 60-arcsec VSX sweep returns 0 rows here: no eclipsing entry at this target. The 372 cone's known EB is the different 58-arcsec neighbour. Gaia vari_eclipsing_binary has no target row in the successful shared query. Exact TIC/main-name web searches found no relevant prior eclipsing record; 416's KIC11418931 is absent from the Kepler EB catalogue. This supports novelty only within the queried sources. Initial failed CDS queries were superseded by working mirrors, not treated as null results.

## Next eclipses and follow-up

After 2026-10-30: primary BTJD 4347.85512, 4352.75049, 4357.64587; secondary 4345.41192, 4350.30732, 4355.20272. Linear-covariance prediction errors can be optimistic; secondary scheduling allowance is at least about 18 minutes from the heuristic phase envelope, plus accumulated ephemeris uncertainty. Primary covariance propagation and sampling sensitivity are retained in the ephemeris files. Follow-up priorities are robust component radii/light ratios, baseline-sensitive events and calibrated multi-sector localization; they do not negate the repeated attributed eclipses.

Provenance: parent acquisition.csv/selected.json/prior-receipts.txt; full-vet scripts and per-target JSONs; successful archive response hashes; shared Gaia/VSX receipts. Sol lead reviewed code and compact evidence plus exactly two new pixel maps; Terra performed bulk extraction/model attempts. Original catalogue and work directories remain unchanged.
