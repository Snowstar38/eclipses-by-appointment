# Q047 TIC 96270957: PLAUSIBLE

Sealed priority rank 197; repeat_sector_dip. Gaia DR3 5921382045628109312, catalogue novelty UNKNOWN because four positive-control gates failed.

S12 flags are isolated single-cadence ~5% lows. S93 SAP shows a long low level bounded by gaps, while a valid target-centered TESSCut 3x3 extraction gives only ~1.6 ppt loss versus about 27 ppt in QLP SAP. Two capable G~12.9 Gaia neighbors lie within ~13 arcsec; WCS centroid is offset and cannot securely assign the large SAP loss. Fresh S104 has near-zero target flux and supplies no null.

Limitations: The S93 extraction discrepancy and source ownership remain unresolved. A single eclipse-like occasion could be target, neighbor, or reduction artifact; no period or depth is adopted.

Next check: Use resolved pixel or PSF photometry around S93 to determine source ownership and explain the QLP aperture discrepancy.

Evidence: `lead-context.json` (whole-sector raw SAP coverage, source FITS SHA256 and source packet SHA256), `lead-local-series.json`, `lead-raw-context.png`, `lead-dip-zooms.png`, and `lead-flag-diagnostics.json`. See batch `LEAD-AUDIT.md` and `helper-audit.txt` for the deciding WCS, alternate extraction, recurrence, and null checks. All computations use the hashed original files or hashed fresh TESSCut cutouts.
