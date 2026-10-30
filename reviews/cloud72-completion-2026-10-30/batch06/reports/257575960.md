# TIC 257575960: PLAUSIBLE

Queue position 55; batch06. Review credits: GPT-6.1 Sol, fresh GPT-6.1 Terra review, supervised by Astra. This is AI review, not human validation.

1. Raw morphology and repeat assessment

QLP sectors 12,67,102 show orbit-segment ramps, noisy low-amplitude variation and repeated plateaus/steps. Original nominal phases in sectors12/67 have no coherent short eclipse; fitted positive depths are below local residual scatter. The fresh independent aperture reproduces the sector102 segment plateaus/steps and noisy S67 curve without detached recurring dips. Independent Terra audit retains PLAUSIBLE: the available representative data fail to establish recurring eclipses, but sparse/compromised coverage does not tie the original search detection to a specific demonstrated artifact. This is not a secure eclipse identification.

Three cached QLP SAP_FLUX FITS sectors were checked with QUALITY=0 and target/sector header verification. Local quadratic baseline plus trapezoid fits are in raw-events.json, including failed or boundary fits. No non-boundary fit exceeds three local residual RMS; no repeat eclipse series establishes a period. Original search period 13.410727098 d is retained only as a conditional alias, not a derived ephemeris. The full morphology overview explicitly checks features away from that alias; raw-event fits alone do not decide the result. Covered conditional phases: [{"sector": 12, "cycle": 1, "nominal_tc": 1644.6230270979095, "n_in": 8, "n_pre": 12, "n_post": 13, "covered": true, "signed_depth": -0.00010025501251220703, "local_rms": 0.0011402764357626438}, {"sector": 67, "cycle": 113, "nominal_tc": 3146.624462063768, "n_in": 48, "n_pre": 108, "n_post": 71, "covered": true, "signed_depth": -0.0006230473518371582, "local_rms": 0.003330210456624627}].

2. Source and independent reduction

Fresh 11x11 TESScut images and TIC 60-arcsec cones were obtained in two sectors. Signed candidate-phase difference images and fixed-coordinate target/capable-neighbour comparisons were attempted using the original search phase. Since no real repeating eclipse exists to localize, these candidate-only fits do not establish an eclipse host or an off-target EB. They are retained as failed candidate tests, not localization detections. Capability limits use the original claimed depth and ignore aperture throughput/bandpass uncertainty.

Fresh cutout sectors: 67,102. Candidate capability counts: 67: 2,102: 2. Source comparisons are descriptive signed-image Gaussian fits, with no calibrated PRF confidence. Neighbour catalogue identity can include unresolved or duplicate records. The independent extraction subtracts each frame's lowest-30-pixel median background then sums a central 3x3 aperture, with QUALITY=0. It uses the same TESS photons through a distinct reduction, and is not SPOC. custom-morphology.png and custom-extraction.json preserve its deciding morphology.

3. Gaia orbit

Gaia NSS orbit metadata were inspected, but no photometric eclipse ephemeris was established; an eclipse/conjunction geometry comparison is therefore inapplicable. Nearness of the original search alias to the Gaia period cannot establish eclipses.

Gaia source 6347331991219882624; NSS P=13.428262096 +/- 0.005767776 d; e=0.41266, omega=352.3530 degrees. No eclipse timing or geometry is inferred from this metadata. No photometric eclipse orbit established; Gaia spectroscopic binarity not refuted.

4. Scoped prior EB coverage

no identified prior EB; coverage complete: yes. Reused centrally completed seven scopes: VSX, SIMBAD primary type, Gaia DR3 eclipsing binaries, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* and ROT alone are not EB identifications; Kostov table2 is unvetted. This is a scoped catalogue result, not an exhaustive discovery claim. Physical and novelty verdicts are separate.

5. Completion and limitations

The representative full review is complete. Scientific outcome: eclipse morphology and repetition remain unresolved; this is not a secure eclipse identification. Missing eclipse geometry reflects the absence of a valid eclipse series, not unfinished execution. Representative three QLP sectors and two independent custom-extraction sectors; no exhaustive all-sector search, calibrated PRF/noise model, physical fit or sensitivity upper limit. No secure eclipse identification or exclusion of all possible shallow eclipses follows. Repetition and eclipse morphology remain scientifically uncertain; no calibrated sensitivity or propagated ephemeris-error analysis was performed.

Next check: Obtain a well-covered predicted candidate event in a distinct reduction and establish a second coherent detached eclipse before claiming an eclipse period or host.

Provenance: raw-evidence/cache-manifest.json preserves original cache paths and SHA256; identity-checks.json verifies all 15 QLP inputs; tesscut-downloads.json stores fresh URLs and zip hashes; TIC raw cones and adapted scripts are retained. manifest.json hashes deliverables. No paper edits, commits or publication were performed.
