# Reuse for the next fresh lead

Batch A finished five full gate reviews: four physical CONFIRMED, one PLAUSIBLE (298645930). RESULTS.json/CSV separate physical verdict, novelty and review completion. Do not repeat the raw pilot.

## Portable computation

Copy the scripts into a new batch's full-vet folder. `fit_batch.py` reads parent `targets-selected.json`, `receipts.json` (search P/P2 rows), and parent `data/<tic>_sNNN.fits`; ROOT derives from the script path. Verify the resolved CSV period before trusting P. This batch's P won by z for all five; other batches may require P2/resolved-period handling.

Minimal numeric order:

1. `python fit_batch.py` (or explicit TICs): primary shared-shape exposure-integrated trapezoids, individual timing/depth/errors, beta inflation, ephemeris/O-C and blind census.
2. `python orbit_gates.py`: source-ID+SB1 selection from shared-full-review/gaia-nss-ari.csv, covariance and Gaia-fixed secondary/control tests, RV mass function/central durations. Hard asserts bit_index127 and corr_vec15; not generic for SB2/astrometric solutions.
3. `python secondary_fit.py`, `python shape_secondary.py`, then `python secondary_fit.py` again: conditional phase, per-kind shape and individual secondary timings.
4. `python geometry.py`: numerical limb-darkened two-disk feasibility, fixed TIC dimensions, free physical flux scales. Coarse profile intervals are NOT calibrated orbital uncertainties; never infer e sin(omega) from a grazing trapezoid's flat duration.

Inspect event-level errors, scan-edge fits, coverage/gaps, and fit residuals. Timing red-noise beta and ephemeris chi2 scaling are implemented, but source variability/model uncertainty can exceed them. Blind census uses a rolling-median threshold, not a proof that every event is astrophysical. Null secondary limits are conditional on tested phase/shape. Two-event secondary cases cannot provide an independent reliable period. No images were required for this batch.

## Working primary-service routes

- `idia_archives.py`: one 45s-bounded VizieR IDIA request per target, **nine comma-separated catalogs in one query** (VSX, ASAS-SN, SB9, WDS, Kostov2/3/4, IJspeert, Prsa), 60arcsec cones. IDIA returned all nine table sections for all five in about5s. Parse raw TSV carefully: header, units, dashed line, then rows; empty sections mean no match only after successful table response. Table2 is unvetted and not EB prior art. Compare coordinates/TIC exactly, not just cone presence.
- ARI Gaia TAP sync worked for NSS/covariance, variability tables and neighbor cones. Root's shared caches now cover70 targets; reuse exact source rows and provenance rather than repeat queries.
- SIMBAD CFA TAP sync worked for exact Gaia identifiers; CDS timed out. ExoFOP target HTML worked (HTTP200, captured TOI/CTOI counters). MAST CAOM found TESS-SPOC for all five, one product each ~2MB total. Helper scripts have Batch A absolute paths: adapt those before reuse.
- CDS/Harvard VizieR timeouts were overcome by IDIA; do not repeat the dead endpoints by default.

## Star-specific work, not a generic verdict engine

`pixel298.py` and `pixel362.py` read existing hashed TESScut cubes, regress a quadratic plus eclipse per pixel, and compare Gaia-source Gaussian fits after OOT calibration. They are specific to their input cubes and cones. 362 localized well (0.23arcsec target; nearest capable neighbor worse by delta chi2~14709); 298's PSF calibration hit a boundary and free centroid~10arcsec, so its precise localization remains unresolved despite favoring target over neighbor. Formal chi2 ignores PSF covariance.

`tide298.py` tests a smooth equilibrium tide+five orbital harmonics against the same+narrow primary. It establishes a sharp component beyond that smooth model; it does not establish its secondary or full host assignment. `make_reports.py` contains explicit reviewed verdicts/reasons and is **not** reusable automatic classification logic. Preserve helper credit in INDEPENDENT-NOTE.md; no optional personal contributor note was supplied for the full-vet helper.

Keep downloaded FITS ignored and record hashes/URLs. Old source catalogues/paper files remain untouched.
