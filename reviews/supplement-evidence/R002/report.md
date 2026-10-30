# TIC 270181578: full adversarial review, 2026-10-30

**Physical verdict: CONFIRMED.** Repeated primary and secondary eclipses match the SB1 ephemeris, an independent pipeline recovers the deficits, the historical deficit is centered on target and no capable resolved G<15 neighbor exists. RUWE 7.688 and conditional dilution limit stellar characterization, not the supported eclipsing-target classification.

**Review completion:** all required gates were attempted and adjudicated below; unavailable services and inconclusive models are explicit limitations. This is not automatic confirmation of novelty. No catalogue/paper edits or commits.

## Deciding measurements

- Raw QLP SAP, QUALITY=0, no gap trimming: 8 primary fits. Median trapezoid depth 27.56 ppt (event range 25.78 to 28.16; median formal/red-noise error 0.30 ppt). Sector medians: {55: 27.66, 82: 27.55}.
- Primary T14 5.76 h, conditional profile/grid range 5.63 to 5.90 h; T12 1.44 h; T23 2.88 h. These are trapezoid shape summaries, not a claim of true totality in grazing events.
- P = 5.573958606 +/- 0.000005421 d; Tref = 3179.434865 +/- 0.000356 BTJD at cycle 68. T0 = 2800.405680 BTJD. Chi2/dof 11.70/6; O-C rms 1.26 min. Per-event timing/errors/O-C are in fit-results.json.
- Conditional secondary: 6 fitted windows, 6 individual >3-sigma fits; depth 2.56 +/- 0.08 ppt after between-event scatter; phase 0.500343 +/- 0.000461. T14 6.03 h (range 5.63 to 6.16), T12 1.51 h, T23 3.01 h. Weak/modulated shape uncertainty can exceed these conditional errors.
- Gaia SB1 P offset +0.82 sigma. At BTJD389, primary minus conjunction A = +0.43 h versus Gaia sigma 0.64 h. Full per-event conjunction comparison uses this source's covariance. Bit index127 and 15 correlations asserted against [ESA's SB1 ordering](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_non--single_stars_tables/ssec_dm_nss_two_body_orbit.html); omega-Tp correlation +0.999825.
- First-order e cos(omega) = +0.0005 +/- 0.0007; for eccentric systems compare exact Gaia conjunction separation rather than treating this expansion as exact. Gaia e=0.0218 +/- 0.0127, omega=341.15 +/- 45.66 degrees.

## Gate adjudication

| Gate | Status | Evidence and limits |
|---|---|---|
| Own archives/prior art | completed; no target prior EB match | ExoFOP HTTP200, TOI=0/CTOI=0; SIMBAD CFA exact Gaia ID is SB*. Shared ARI Gaia variability cache has no EB rows among70 sources. CDS and Harvard timed out, then IDIA succeeded: fresh 60arcsec cones in VSX, ASAS-SN, SB9, WDS, Kostov table2/3/4, IJspeert and Prsa. All nine table sections returned; no target EB prior-art match. Neighbor ROT/unvetted table2 matches are distinct sources. Raw responses and hashes in *_idia.tsv/idia-receipts.json. Identifier web searches have no pertinent hit, not proof of novelty. |
| Individual events/ephemerides | measured | fit-results.json, secondary-fit.json: integrated-exposure trapezoids, local quadratic baselines, fixed shared shape per kind, profile timing error with cadence/grid floors; primary residual bin-beta range 1.25 to 1.78; ephemeris errors inflated when chi2/dof>1. Secondary ephemeris stored when >=3 strong events; two-event cases use primary P. |
| Flags/background/centroids | tested; conditional | Each fit records flagged core counts, OR bits, template centroids/errors, background regression and refitted depth. Maximum predicted fake-background primary depth 1.53 ppt. Native background units never treated as flux. Sparse flags/gaps remain exclusions, not clean nulls. |
| Blind census | measured; coverage limited | 17 candidate dip groups at max(4 robust per-cadence sigma,3ppt), including 1 away from measured eclipses. Thresholded rolling median can detect intrinsic modulation/gap edges. For straightforward objects the lone off-phase group lacks sufficient clean baseline for event fitting (offphase-checks.json); no claim it is an eclipse. |
| Other eclipse/controls | measured; conditional | Gaia-fixed-phase tests and off-phase controls in orbit-gates.json; optimized secondary timing/shape separately in secondary-fit.json. Any quoted null upper limit is primary-shape/Gaia-phase conditional, not general exclusion. |
| Independent pipeline | passed for aperture events | TESS-SPOC SAP/PDCSAP retrieval and QUALITY=0 core estimates in indep_measure.txt; different reduction of same TESS data, not a separate observatory. Amplitude differences include dilution/sampling. |
| Neighbors/localization | supports target | Fresh ARI G<15 cone within60arcsec; required fractional dip estimates in neighbors_summary.csv are G-band proxies without aperture throughput. Historical difference-image deficit-target offset 1.47arcsec, peak on target. See star-specific verdict and limitations. |
| Physics/e sin(omega) | modeled; conditional | RV mass function 0.02443 Msun; minimum m2 0.334 to 0.472 Msun for listed M1 hypotheses. Predicted central primary T14 6.96 to 7.88 h versus observed 5.76 h, compatible with a noncentral chord. Numerical limb-darkened two-disk fits in geometry.json explore both shapes with fixed TIC dimensions, free depth scales and physical scale<=1; degeneracies prevent a robust independent e sin(omega) measurement. Do not interpret the coarse-grid profile interval as a calibrated orbital confidence interval. |

Next predictions (BTJD, from 2026-10-30 noon): primary [np.float64(4344.39221), np.float64(4349.96617)]; secondary [np.float64(4347.18111), np.float64(4352.75506)]. Timing extrapolations inherit ephemeris and secondary-shape systematics; no precise future uncertainty for the modulated system.

**Next deciding check:** Characterize high-RUWE multiplicity with high-resolution imaging and better primary mass/radius; then joint light/RV fit.

Provenance: ../downloads.json and ../receipts.json; shared-full-review Gaia receipts; independent CAOM responses and indep_sha256.txt. Scripts fit_batch.py/orbit_gates.py/secondary_fit.py/geometry.py reproduce numeric results. Optional Terra personal note was not supplied; its scientific contribution is preserved verbatim in INDEPENDENT-NOTE.md. Lead: Sol batch A.

Specific caution: no other G<15 resolved neighbor within60arcsec, but this does not exclude unresolved light. RUWE7.688 and conditional geometry primary scale~0.45 motivate multiplicity/dilution follow-up rather than a unique binary geometry.
