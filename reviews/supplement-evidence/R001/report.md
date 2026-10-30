# TIC 373138363: full adversarial review, 2026-10-30

**Physical verdict: CONFIRMED.** Repeated primary and secondary eclipses, matching SB1 period/conjunction, independent reduction, target-centered prior image and no capable resolved G<15 neighbor establish an eclipsing target. Stellar dimensions remain model dependent.

**Review completion:** all required gates were attempted and adjudicated below; unavailable services and inconclusive models are explicit limitations. This is not automatic confirmation of novelty. No catalogue/paper edits or commits.

## Deciding measurements

- Raw QLP SAP, QUALITY=0, no gap trimming: 9 primary fits. Median trapezoid depth 29.71 ppt (event range 25.47 to 30.13; median formal/red-noise error 0.29 ppt). Sector medians: {5: 29.85, 32: 30.07, 98: 25.83}.
- Primary T14 4.19 h, conditional profile/grid range 4.10 to 4.28 h; T12 1.47 h; T23 1.26 h. These are trapezoid shape summaries, not a claim of true totality in grazing events.
- P = 7.240208264 +/- 0.000001939 d; Tref = 2671.293626 +/- 0.000328 BTJD at cycle 170. T0 = 1440.458221 BTJD. Chi2/dof 0.55/7; O-C rms 0.62 min. Per-event timing/errors/O-C are in fit-results.json.
- Conditional secondary: 9 fitted windows, 9 individual >3-sigma fits; depth 2.92 +/- 0.07 ppt after between-event scatter; phase 0.500031 +/- 0.000145. T14 4.19 h (range 3.93 to 4.28), T12 1.47 h, T23 1.26 h. Weak/modulated shape uncertainty can exceed these conditional errors.
- Gaia SB1 P offset -0.73 sigma. At BTJD389, primary minus conjunction A = +0.21 h versus Gaia sigma 0.89 h. Full per-event conjunction comparison uses this source's covariance. Bit index127 and 15 correlations asserted against [ESA's SB1 ordering](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_non--single_stars_tables/ssec_dm_nss_two_body_orbit.html); omega-Tp correlation +0.999976.
- First-order e cos(omega) = +0.0000 +/- 0.0002; for eccentric systems compare exact Gaia conjunction separation rather than treating this expansion as exact. Gaia e=0.0104 +/- 0.0142, omega=292.96 +/- 90.22 degrees.

## Gate adjudication

| Gate | Status | Evidence and limits |
|---|---|---|
| Own archives/prior art | completed; no target prior EB match | ExoFOP HTTP200, TOI=0/CTOI=0; SIMBAD CFA exact Gaia ID is SB*. Shared ARI Gaia variability cache has no EB rows among70 sources. CDS and Harvard timed out, then IDIA succeeded: fresh 60arcsec cones in VSX, ASAS-SN, SB9, WDS, Kostov table2/3/4, IJspeert and Prsa. All nine table sections returned; no target EB prior-art match. Neighbor ROT/unvetted table2 matches are distinct sources. Raw responses and hashes in *_idia.tsv/idia-receipts.json. Identifier web searches have no pertinent hit, not proof of novelty. |
| Individual events/ephemerides | measured | fit-results.json, secondary-fit.json: integrated-exposure trapezoids, local quadratic baselines, fixed shared shape per kind, profile timing error with cadence/grid floors; primary residual bin-beta range 1.00 to 1.22; ephemeris errors inflated when chi2/dof>1. Secondary ephemeris stored when >=3 strong events; two-event cases use primary P. |
| Flags/background/centroids | tested; conditional | Each fit records flagged core counts, OR bits, template centroids/errors, background regression and refitted depth. Maximum predicted fake-background primary depth 0.22 ppt. Native background units never treated as flux. Sparse flags/gaps remain exclusions, not clean nulls. |
| Blind census | measured; coverage limited | 19 candidate dip groups at max(4 robust per-cadence sigma,3ppt), including 1 away from measured eclipses. Thresholded rolling median can detect intrinsic modulation/gap edges. For straightforward objects the lone off-phase group lacks sufficient clean baseline for event fitting (offphase-checks.json); no claim it is an eclipse. |
| Other eclipse/controls | measured; conditional | Gaia-fixed-phase tests and off-phase controls in orbit-gates.json; optimized secondary timing/shape separately in secondary-fit.json. Any quoted null upper limit is primary-shape/Gaia-phase conditional, not general exclusion. |
| Independent pipeline | passed for aperture events | TESS-SPOC SAP/PDCSAP retrieval and QUALITY=0 core estimates in indep_measure.txt; different reduction of same TESS data, not a separate observatory. Amplitude differences include dilution/sampling. |
| Neighbors/localization | supports target | Fresh ARI G<15 cone within60arcsec; required fractional dip estimates in neighbors_summary.csv are G-band proxies without aperture throughput. Historical difference-image deficit-target offset 0.39arcsec, peak on target. See star-specific verdict and limitations. |
| Physics/e sin(omega) | modeled; conditional | RV mass function 0.03001 Msun; minimum m2 0.436 to 0.436 Msun for listed M1 hypotheses. Predicted central primary T14 7.85 to 7.85 h versus observed 4.19 h, compatible with a noncentral chord. Numerical limb-darkened two-disk fits in geometry.json explore both shapes with fixed TIC dimensions, free depth scales and physical scale<=1; degeneracies prevent a robust independent e sin(omega) measurement. Do not interpret the coarse-grid profile interval as a calibrated orbital confidence interval. |

Next predictions (BTJD, from 2026-10-30 noon): primary [np.float64(4351.02194), np.float64(4358.26215)]; secondary [np.float64(4347.40207), np.float64(4354.64227)]. Timing extrapolations inherit ephemeris and secondary-shape systematics; no precise future uncertainty for the modulated system.

**Next deciding check:** Obtain stellar-radius constraints and joint RV/eclipse characterization.

Provenance: ../downloads.json and ../receipts.json; shared-full-review Gaia receipts; independent CAOM responses and indep_sha256.txt. Scripts fit_batch.py/orbit_gates.py/secondary_fit.py/geometry.py reproduce numeric results. Optional Terra personal note was not supplied; its scientific contribution is preserved verbatim in INDEPENDENT-NOTE.md. Lead: Sol batch A.
