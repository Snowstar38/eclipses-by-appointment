# Q041 TIC 352354421: REFUTED

Sealed priority rank 191; repeat_sector_dip. Gaia DR3 6422150355876758144, catalogue novelty UNKNOWN because four positive-control gates failed.

The selected S67/S94/S101 SAP dips are aperture-motion features. WCS differences show adjacent positive/negative pixels; S94 3x3 loss 5.58 ppt falls to 0.30 ppt at 9x9, S67 1.83 to 0.49, S101 0.66 to 0.30. Q049 has an almost simultaneous S94 trough. The S67/S101 flags happen to be 37 Gaia cycles apart, but their pixel dipoles prevent adopting them as repeated eclipses.

Limitations: A residual sub-ppt intrinsic component cannot be excluded. This verdict refutes selected dip evidence, not every possible binary signal.

Next check: Revisit only if resolved motion-corrected photometry shows repeated target-centered losses.

Evidence: `lead-context.json` (whole-sector raw SAP coverage, source FITS SHA256 and source packet SHA256), `lead-local-series.json`, `lead-raw-context.png`, `lead-dip-zooms.png`, and `lead-flag-diagnostics.json`. See batch `LEAD-AUDIT.md` and `helper-audit.txt` for the deciding WCS, alternate extraction, recurrence, and null checks. All computations use the hashed original files or hashed fresh TESSCut cutouts.
