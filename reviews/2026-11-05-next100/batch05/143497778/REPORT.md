# Q044 TIC 143497778: CONFIRMED

Sealed priority rank 194; repeat_sector_dip. Gaia DR3 5531321533932247936, catalogue novelty UNKNOWN because four positive-control gates failed.

Raw SAP has recurring asymmetric troughs in S7/8, S61/62 and S88/89; S89 contains two separate troughs 23.395 days apart. Independent QLP and TESSCut 3x3 extractions both show rapid ingress near -0.35 d, a ~0.35 d flat core, and rapid egress near +0.3 to +0.4 d on both S89 occasions (lead-shape.json/png); this contact-like notch is distinct from the broad sector-wide wave. Target-centered WCS losses recur in S61 (0.134 pixel; 7.04 ppt 3x3) and S89 (0.091 pixel; 9.75 ppt). Actual covered P/2, P/3, P/4 alias windows are flat. Conditional multievent P=23.400623 d agrees within about 1.4 Gaia standard errors with SB1 P=23.417146 d; source-specific A conjunction is about 0.16 day from the broad S8 diagnostic center.

Limitations: A broad orbital/tidal wave may coexist and complicates baseline/depth. Bound-hitting S61/S62 Gaussian centers limit timing precision. S34 is a trend, and S88 broad-window pixel comparison is invalid; neither is used to establish source attribution. No formal period error or primary designation is adopted.

Next check: Fit a physical eclipse plus orbital-wave model to the S61/S89 occasions and complete novelty gates.

Evidence: `lead-context.json` (whole-sector raw SAP coverage, source FITS SHA256 and source packet SHA256), `lead-local-series.json`, `lead-raw-context.png`, `lead-dip-zooms.png`, and `lead-flag-diagnostics.json`. See batch `LEAD-AUDIT.md` and `helper-audit.txt` for the deciding WCS, alternate extraction, recurrence, and null checks. All computations use the hashed original files or hashed fresh TESSCut cutouts.
