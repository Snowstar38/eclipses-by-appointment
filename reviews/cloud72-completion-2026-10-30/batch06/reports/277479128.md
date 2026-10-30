# TIC 277479128: REFUTED

Queue position 54; batch06. Review credits: GPT-6.1 Sol, fresh GPT-6.1 Terra review, supervised by Astra. This is AI review, not human validation.

1. Raw morphology and repeat assessment

QLP sectors 13,92,94 contain broad multi-day variability and large segment changes. The sharp-looking S94 minimum is a distorted edge on broad variability: the distinct fresh aperture shows a multi-day minimum rather than a short detached eclipse. Covered nominal phases have negative short-window signed deficits; the strong S94 template fit hits its timing bound. No repeating detached event establishes an eclipse period.

Three cached QLP SAP_FLUX FITS sectors were checked with QUALITY=0 and target/sector header verification. Local quadratic baseline plus trapezoid fits are in raw-events.json, including failed or boundary fits. No non-boundary fit exceeds three local residual RMS; no repeat eclipse series establishes a period. Original search period 19.667413548 d is retained only as a conditional alias, not a derived ephemeris. The full morphology overview explicitly checks features away from that alias; raw-event fits alone do not decide the result. Covered conditional phases: [{"sector": 13, "cycle": 0, "nominal_tc": 1667.3914, "n_in": 7, "n_pre": 12, "n_post": 4, "covered": true, "signed_depth": -0.0013865232467651367, "local_rms": 0.005576646886765957}, {"sector": 92, "cycle": 109, "nominal_tc": 3811.139476703976, "n_in": 67, "n_pre": 113, "n_post": 113, "covered": true, "signed_depth": -0.000667572021484375, "local_rms": 0.004877484869211912}, {"sector": 94, "cycle": 112, "nominal_tc": 3870.1417173472046, "n_in": 67, "n_pre": 113, "n_post": 113, "covered": true, "signed_depth": -0.04576444625854492, "local_rms": 0.07903945446014404}].

2. Source and independent reduction

Fresh 11x11 TESScut images and TIC 60-arcsec cones were obtained in two sectors. Signed candidate-phase difference images and fixed-coordinate target/capable-neighbour comparisons were attempted using the original search phase. Since no real repeating eclipse exists to localize, these candidate-only fits do not establish an eclipse host or an off-target EB. They are retained as failed candidate tests, not localization detections. Capability limits use the original claimed depth and ignore aperture throughput/bandpass uncertainty.

Fresh cutout sectors: 92,94. Candidate capability counts: 92: 8,94: 8. Source comparisons are descriptive signed-image Gaussian fits, with no calibrated PRF confidence. Neighbour catalogue identity can include unresolved or duplicate records. The independent extraction subtracts each frame's lowest-30-pixel median background then sums a central 3x3 aperture, with QUALITY=0. It uses the same TESS photons through a distinct reduction, and is not SPOC. custom-morphology.png and custom-extraction.json preserve its deciding morphology.

3. Gaia orbit

Gaia NSS orbit metadata were inspected, but no photometric eclipse ephemeris was established; an eclipse/conjunction geometry comparison is therefore inapplicable. Nearness of the original search alias to the Gaia period cannot establish eclipses.

Gaia source 6760248154216144512; NSS P=19.660672814 +/- 0.014125655 d; e=0.08876, omega=128.5857 degrees. No eclipse timing or geometry is inferred from this metadata. No photometric eclipse orbit established; Gaia spectroscopic binarity not refuted.

4. Scoped prior EB coverage

no identified prior EB; coverage complete: yes. Reused centrally completed seven scopes: VSX, SIMBAD primary type, Gaia DR3 eclipsing binaries, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* and ROT alone are not EB identifications; Kostov table2 is unvetted. This is a scoped catalogue result, not an exhaustive discovery claim. Physical and novelty verdicts are separate.

5. Completion and limitations

The representative full review is complete. Scientific outcome: submitted eclipse interpretation refuted by a demonstrated smooth/systematic explanation. Missing eclipse geometry reflects the absence of a valid eclipse series, not unfinished execution. Representative three QLP sectors and two independent custom-extraction sectors; no exhaustive all-sector search, calibrated PRF/noise model, physical fit or sensitivity upper limit. Refutation applies to the submitted eclipse interpretation, not to binarity or all possible shallow eclipses.

Next check: No missing deciding gate for this candidate. Reopen only if new data supply distinct, repeated detached events.

Provenance: raw-evidence/cache-manifest.json preserves original cache paths and SHA256; identity-checks.json verifies all 15 QLP inputs; tesscut-downloads.json stores fresh URLs and zip hashes; TIC raw cones and adapted scripts are retained. manifest.json hashes deliverables. No paper edits, commits or publication were performed.
