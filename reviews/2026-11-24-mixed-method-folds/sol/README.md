# Timing audit of the ten archived fold-only leads

No target has a secure repeating eclipse at the sampled Gaia or archived photometric period. TIC 197243461 is the strongest **weak timing watch**, with two shallow in-sample features and an untested third event. TIC 244201152 has the strongest isolated dip with a sensitive QLP non-repeat at the archived phase.

Positive depths indicate dimming. Depth pairs below are SAP / QLP detrended flux in ppt. TESS epochs are BTJD (BJD TDB − 2,457,000). Periods and box widths in the outcome table are in days. The epoch in the table refers to the original fitted fold phase and may predate the strongest observed measurement. This audit supplies photometric timing only. Source attribution and physically predicted Gaia conjunctions are separate evidence.

| TIC | Timing outcome and decisive windows |
|---|---|
| 135180054 | S23 BTJD 1930.4598 yields +67.69 / −242.40 ppt in a badly distorted baseline. SAP and detrended flux both have a near-total one-cadence loss at 1930.4320, among many other excursions. S50 has no right flank at 2691.4188. Gaia and both full-period phase refits select a different S23 excursion, while the half-period can align two excursions in that same unstable sector. |
| 347447876 | S34 BTJD 2252.6766 straddles two interleaved flux levels and strong local slope. The archive-phase S99 prediction at 4056.8916 is unsampled. Exact archived half-period produces a formal 13.22 / 11.95 ppt in the same contaminated S34 feature and just 1.17 / 1.15 ppt in S88. Gaia's free-phase fit has 1.37 / 1.37, 5.40 / 5.41 and 0.64 / 0.63 ppt in S8, S34 and S88. The shapes and depths do not support an eclipse train. |
| 302399892 | S26 BTJD 2029.173747 has one −139.18 ppt detrended point (signed offset from median), with −0.89 ppt SAP. At the archive period S40 at 2397.7627 has +0.69 / +0.74 ppt and S59 at 2936.4894 has −0.74 / −0.88 ppt. These well-sampled windows exclude repeats at the reported screen depth. |
| 14832729 | S75 BTJD 3340.6167 has +2.73 / +0.05 ppt, variable with the SAP background and stable around zero in detrended flux. The S82 prediction is gapped for the nominal window, but shorter valid flanks give −0.10 to +0.08 ppt SAP and approximately −0.15 ppt detrended flux. Gaia P at the archived epoch yields small or negative depths in S41, S75 and S82. |
| 191231056 | S17 BTJD 1773.2887 gives +34.25 / +15.97 ppt, embedded in an irregular series of sharp losses and recovery. The nominal repeat at S57 ends against a gap, and S84 is internally gapped. Shorter S84 windows are quiet. With Gaia P at the S17 phase, S84 BTJD 3606.3452 is covered and gives −0.49 / −0.23 ppt. |
| 197243461 | At 56.33242698 d, S45 BTJD 2545.37635 (1.09 / 1.48 ppt) and S72 BTJD 3277.69790 (0.53 / 0.51 ppt) are individually covered. S45 has a shallow core and a rising SAP baseline. S72 has weaker, asymmetric structure and the depth decreases as the window broadens. The 0.12 d refit to local centers at 2545.35135 and 3277.72790 gives 56.33665775 d over 13 cycles, entirely in-sample. The archived-phase score outranks 3,522 comparable shifted phases, but those phases are correlated and the archive chose its period and phase from these data. Using Gaia P at the archived epoch instead samples S72 1.464 d earlier, at 0.38 / 0.17 ppt. The archived half-period fit returns other small positives of unequal shape and a different period (27.76163 d) from half the full-period fit. A new clean event would materially change the result. |
| 390126467 | S26 BTJD 2029.346747 is one −174.36 ppt detrended point with −3.46 ppt SAP, surrounded by ordinary neighboring flux. S41 2434.0972, S54 2781.0264, S81 3532.7064 give +0.38 / +0.40, −0.58 / −0.60, +0.81 / +0.94 ppt, respectively. These covered predictions exclude repeats at the archive screen depth. |
| 388584591 | S26 BTJD 2029.175214 is one −144.17 ppt detrended point (+0.77 ppt SAP) at nearly the same time as the anomalous TIC 302399892 cadence. S58 BTJD 2895.6537, S73 3303.4135, S79 3456.3234 give −0.11 / −0.20, −0.34 / −0.37, +0.21 / +0.30 ppt. The weak 1.71055 to 1.72657 d modulation alternatives have varying sector-by-sector fits and lack eclipse-like repeats. |
| 244201152 | S42 BTJD 2471.0741 gives +4.65 / +4.92 ppt and remains approximately 3–5 ppt under reasonable width and baseline changes. Its profile is noisy, with several depressed samples. The covered S3 BTJD 1404.1709 gives +0.41 / +0.37 ppt and stays within about 0.5 ppt of zero across baseline choices. S30 BTJD 2139.9662 lacks continuous bracket coverage and cannot decide the repeat. |
| 323600657 | S72 BTJD 3263.8951 gives +1.14 / −0.10 ppt, consistent with SAP curvature. The other archive predictions lack continuous baselines. A broad exploratory 0.82994 d peak fits low-amplitude variability (detrended sinusoidal semiamplitude 0.05 to 0.09 ppt). S34/44/45/46 minimum phases are 0.26 to 0.30 relative to BTJD 2000, with lower coherence across S8 and S72 and no sharp eclipse profile. |

## Replay

Run from the packet directory with Python, NumPy and Astropy. The frozen `sol/archive-manifest.json` records the MAST URI and SHA-256 of every original QLP product. The sanitized `sol/original-fold-models.json` contains the historical P and P/2 parameters and the path and SHA-256 of each original record for provenance. Both inputs ship with the packet.

```console
python sol/build_cache.py --fetch
python sol/timing.py
python sol/diagnostics.py
python sol/sensitivity.py
python sol/controls.py
```

The first command fetches missing FITS into `fits-cache/` and writes NPZ files to `cadences/`, both beside the packet's `sol/` directory. Existing FITS are reused after verification. To reuse an existing FITS directory, give `--fits-cache PATH`. Each command also accepts invocation by absolute script path from another working directory.

For a different NPZ folder, supply `--out` to `build_cache.py` and `--cache` to the remaining commands. NPZ files are named `TIC-sector.npz` with no sector padding. They hold quality-zero cadences, finite BTJD in `t`, raw QLP `SAP_FLUX` in `sap` and QLP `KSPSAP_FLUX` or newer `DET_FLUX` in `pdc`. The old fold code used SAP when KSPSAP was unavailable. This audit measures both SAP and the available detrended channel.

- `outcomes.csv` records the per-target timing status and exact archived model values to the displayed precision.
- `archive-manifest.json` records FITS identities, SHA-256 hashes, MAST URIs, flux column and coverage.
- `timing.json` measures each in-sector prediction with a median linear flank baseline, core depths, counts, empirical scatter and profile bins. Missing flanks, sparse coverage and gaps remain partial. Exact historical P and P/2 phases are imported. Gaia P, archive P and their halves and doubles are also given independent phase/width searches. The search ranks bracketed dips jointly in both flux channels, whose errors are correlated, with per-sector window scatter and a cap on the leverage of single anomalous windows. It reports no periods outside what the sampling supports.
- `diagnostics.json` records the quality-zero cadences around the exact original predictions and per-sector sinusoidal fits. Broad Lomb–Scargle and box peaks are exploratory, with many sampled frequencies and possible aliases.
- `sensitivity.json` changes the local flank ranges, box widths and event centers. A recentered result uses the prediction's own data.
- `controls.json` compares the exact archived phase with other coverage-matched phases at the same period on a 0.008 d grid, using the nearest review width. Adjacent control phases overlap substantially. The phase ranks are descriptive and do not measure post-selection significance.
