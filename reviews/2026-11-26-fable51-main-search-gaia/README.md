# Gaia DR3 rows for the 6,357 main-search targets (Fable 5.1, Nov 26)

Duet asked (run 20) for parallax, G, BP-RP, K1 and significance for every
star the main appointment search covered, keyed by source_id.

`main-search-gaia-rows.csv`: one row per searched star, 6,357 rows, none
missing. The searched set is `results.jsonl` from the search cache (one line
per star the window test ran on: chunks 1 to 3, G < 11.5). The Gaia fields are
the ones the search itself fetched from `gaiadr3.nss_two_body_orbit` joined to
`gaia_source`, so they are the same numbers the windows were built from.

Columns: `source_id, tic, Tmag, band (G<10 | G10-11 | G11-11.5), nsec (TESS
sectors with QLP), n_windows (conjunction windows covered), z (the search's
best-event excess)`, then the Gaia row: `nss_solution_type, period,
period_error, t_periastron, t_periastron_error, eccentricity,
eccentricity_error, arg_periastron, arg_periastron_error,
semi_amplitude_primary (K1, km/s), semi_amplitude_secondary (K2, SB2 only),
goodness_of_fit (F2), significance, ra, dec, parallax, phot_g_mean_mag, bp_rp,
ruwe, phot_variable_flag, veb (source_id if in vari_eclipsing_binary)`.

Band edges are on Gaia G. `t_periastron` is Gaia's convention (days from
JD 2457389.0, TCB). Blank K2 means SB1.

Also committed to eclipses-by-appointment as
`reviews/2026-11-26-fable51-main-search-gaia/`. Script:
`Fable 5.1\made\appointments\duet_gaia_rows.py`.
