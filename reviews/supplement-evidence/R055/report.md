# TIC 435190459: CONFIRMED

Eight deep repeated primary eclipses at the RV clock survive independent TESS-SPOC reduction and target-centred localization. Secondary non-detection does not veto a target EB. Its pointwise limits are conditional on phase and width; radius/light-ratio assumptions are not measurements.

Full review: COMPLETED_WITH_ARCHIVE_LIMITATION. Physical verdict is separate from novelty. Novelty: LIMITED_PRIOR_ART_COVERAGE; no prior target EB was established by the available current sources. New nine-catalog passes to both IDIA and Harvard timed out and are not negative matches.

## Raw SAP and event measurements

Primary P=6.638903127 +/- 0.000005260 d; Tref=3202.1243494 +/- 0.0002894 BTJD at cycle56; T0=2830.3457742. 8 fitted primary events, O-C RMS=0.995 min; chi2/dof=5.70/6. Shape T14=6.547h, profile range=[0.26736206896551723, 0.27822413793103445], ingress fraction=0.25; T12=fr*T14 and nominal T23=T14-2*T12. Trapezoid flat time is not totality for grazing systems.

|sector|mid BTJD|error d|depth ppt|error ppt|O-C min|flagged core|
|---|---:|---:|---:|---:|---:|---:|
|56|2830.3454897|0.000818|58.570|0.617|-0.410|0|
|56|2836.9859477|0.000818|58.471|0.593|1.829|1|
|56|2843.6231322|0.000818|59.030|0.458|-0.646|0|
|56|2850.2619535|0.000818|59.401|0.564|-0.763|0|
|83|3560.6240116|0.000818|60.439|0.478|-1.594|6|
|83|3567.2644696|0.000818|59.945|0.492|0.646|2|
|83|3573.9032909|0.000818|59.343|0.542|0.528|0|
|83|3580.5421121|0.000818|59.051|0.484|0.410|0|

Primary median depth=59.197ppt; maximum absolute background-regression fake depth=1.438ppt. Background native units were not treated as normalized flux. 0 event timing fits hit a scan edge. Quality-zero fits use exposure integration, local quadratic baselines, red-noise beta and grid floors; flagged-core counts and centroid/background regressions are retained in fit-results.json. Source variability and shape errors may exceed these conditional errors.

Blind rolling-median census covers all available sectors without the old post-gap trim. No off-eclipse census dip exceeds30%of the primary depth outside0.08phase of either fitted eclipse kind. Smaller candidates, gaps, sector edges and all threshold details remain in fit-results.json; this is a diagnostic census, not a calibrated false-positive probability.

## Gaia and physical feasibility

Own-source SB1 covariance verified: bit_index=127,15 correlations in P,gamma,K1,e,omega,Tp order; omega-Tp correlation=0.9946027. Primary assigned conjunctionA; period discrepancy=-0.119sigma.
ConjunctionA at Gaia epoch: offset=0.157191d, Gaia-only sigma=0.090549d; including photometric extrapolation sigma=0.090577d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.
ConjunctionB at Gaia epoch: offset=-3.001407d, Gaia-only sigma=0.071989d; including photometric extrapolation sigma=0.072024d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.

Mass-function/assumed-stellar-radius checks (not measured binary parameters):

```json
[
  {
    "m1": 1.04,
    "m2_min": 0.3096944634559846,
    "f_mass": 0.016305322433816067,
    "a_rsun": 16.42797739824315,
    "r1_rsun": 1.59862,
    "r2_approx_rsun": 0.3915135101641129,
    "central_T14_hours": {
      "A": 7.434438724894848,
      "B": 5.069938347239261
    },
    "observed_T14_hours": 6.547034482758621
  }
]
```

Limb-darkened two-sphere feasibility permits free primary/secondary flux scales and fixed TIC stellar dimensions. It does not identify the foreground component from eclipse depth alone. Using Gaia primary spectroscopic omega and positive RV away from the observer, at A (nu+omega=90deg) the RV primary is behind and the companion is foreground; at B (270deg) the primary is foreground. The deeper eclipse is assigned A here; luminosity and component labeling remain conditional. Minimum RV companion mass and eclipse luminosity/shape jointly allow a stellar companion.

```json
{
  "status": "insufficient secondary shape"
}
```

## Secondary evidence

Optimized secondary phase=0.446979; pooled depth=3.931ppt, empirical error=0.117ppt; 0/8 individually>3sigma. This scan optimizes phase and does not provide a calibrated phase error or global significance. Repeat events, independent reduction, and off-phase controls are more informative than its raw peak S/N.

```json
{
  "bit_index": 127,
  "gaia_primary": "A",
  "gaia_relative_phase_nominal": 0.47498018379158913,
  "gaia_relative_phase_quantiles_16_50_84": [
    0.45396318485306825,
    0.47535980638116565,
    0.5001577700582943
  ],
  "gaia_relative_phase_sigma": 0.02341750040402469,
  "gaia_e_cos_omega_quantiles": [
    -0.07126936460425878,
    -0.03802967769626962,
    0.00024259385537845393
  ],
  "gaia_e_sin_omega_quantiles": [
    -0.21455364141512775,
    -0.18643453512332384,
    -0.15686729176544462
  ],
  "photometric_phase": null,
  "photometric_e_cos_omega_first_order": null,
  "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
  "geometry_status": "insufficient secondary shape",
  "geometry_e_sin_omega_conditional_range": null,
  "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
}
```

No individual secondary exceeds3sigma. null-secondary.json tests covariance phases and widths: pointwise limits span0.58–4.81ppt and are not a uniform global upper bound. A faint companion and uncertain chord/radius/light ratio can account for a missing secondary; the assumed main-sequence radius is not a measured exclusion.

|sector|secondary mid BTJD|error d|depth ppt|error ppt|
|---|---:|---:|---:|---:|
|56|2826.6185530|0.000558|3.846|0.292|
|56|2833.2574562|0.000558|3.475|0.340|
|56|2839.8963593|0.000558|3.777|0.276|
|56|2846.5352624|0.000558|3.717|0.299|
|83|3563.5368001|0.000558|3.828|0.294|
|83|3570.1757032|0.000558|4.091|0.318|
|83|3576.8146064|0.000558|4.060|0.267|
|83|3583.4535095|0.000558|4.667|0.320|

Secondary ephemeris: null. Two-event periods and optimized shapes are not precise independent orbit constraints. Covered/uncovered/flagged secondary windows are enumerated individually in orbit-gates.json secondary_windows, and null-secondary.json when applicable.

## Independence and source attribution

TESS-SPOC sector83, exact FITS identity validated=True. Same TESS pixels through a different reduction, not another observatory. Exact product/time coverage/URLs/SHA256 are in independent manifests; every measured event and degree1/2 background/baseline comparison is in independent-summary.json (alternate summary for345589621).

```json
{
  "tc": 3560.624011591666,
  "qlp": {
    "1": {
      "depth": 0.06012117241347394,
      "error": 0.0004531036642680692,
      "red_noise_beta": 1.8548437651913054,
      "n_core": 112,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06011361050771707,
      "background_template_native_sigma": -0.006016107745134231
    },
    "2": {
      "depth": 0.06069633534156806,
      "error": 0.00047602965132843394,
      "red_noise_beta": 1.7826363128129086,
      "n_core": 112,
      "baseline_degree": 2,
      "background_regressed_depth": 0.06057489869015148,
      "background_template_native_sigma": -0.11219312738923046
    }
  },
  "independent": {
    "SAP_FLUX": {
      "1": {
        "depth": 0.056157528859484794,
        "error": 0.00042751522208951524,
        "red_noise_beta": 2.0022585199597454,
        "n_core": 111,
        "baseline_degree": 1,
        "background_regressed_depth": 0.05618919598670773,
        "background_template_native_sigma": 0.10016136529383748
      },
      "2": {
        "depth": 0.0566511291081388,
        "error": 0.0004515883115895924,
        "red_noise_beta": 1.9351016888237207,
        "n_core": 111,
        "baseline_degree": 2,
        "background_regressed_depth": 0.05665526765619395,
        "background_template_native_sigma": -0.022070966496170075
      }
    },
    "PDCSAP_FLUX": {
      "1": {
        "depth": 0.056322813326895094,
        "error": 0.00040148148018327224,
        "red_noise_beta": 1.9482825628797609,
        "n_core": 111,
        "baseline_degree": 1,
        "background_regressed_depth": 0.05636947658600153,
        "background_template_native_sigma": 0.10016136529383748
      },
      "2": {
        "depth": 0.056598059559810905,
        "error": 0.00043586077020426093,
        "red_noise_beta": 1.9136993168726697,
        "n_core": 111,
        "baseline_degree": 2,
        "background_regressed_depth": 0.05659311114950755,
        "background_template_native_sigma": -0.022070966496170075
      }
    }
  }
}
```

```json
{
  "tc": 3567.264469605509,
  "qlp": {
    "1": {
      "depth": 0.05954630061516232,
      "error": 0.0004781889263476012,
      "red_noise_beta": 1.8900433266968115,
      "n_core": 116,
      "baseline_degree": 1,
      "background_regressed_depth": 0.05984374132301949,
      "background_template_native_sigma": 0.4703473954106571
    },
    "2": {
      "depth": 0.06002995156665453,
      "error": 0.000497742952706455,
      "red_noise_beta": 1.780700550382042,
      "n_core": 116,
      "baseline_degree": 2,
      "background_regressed_depth": 0.06018356727163635,
      "background_template_native_sigma": 0.28823204221457865
    }
  },
  "independent": {
    "SAP_FLUX": {
      "1": {
        "depth": 0.05566563057540342,
        "error": 0.00043158129527178776,
        "red_noise_beta": 2.047793012616552,
        "n_core": 116,
        "baseline_degree": 1,
        "background_regressed_depth": 0.0557783919125477,
        "background_template_native_sigma": 0.38792767774618
      },
      "2": {
        "depth": 0.056082314483056735,
        "error": 0.0004533653596821236,
        "red_noise_beta": 1.9485561834976115,
        "n_core": 116,
        "baseline_degree": 2,
        "background_regressed_depth": 0.056121316435812654,
        "background_template_native_sigma": 0.27252607792339284
      }
    },
    "PDCSAP_FLUX": {
      "1": {
        "depth": 0.056072852932239,
        "error": 0.00041384096265338757,
        "red_noise_beta": 1.9727597301765256,
        "n_core": 116,
        "baseline_degree": 1,
        "background_regressed_depth": 0.05614432380168172,
        "background_template_native_sigma": 0.38792767774618
      },
      "2": {
        "depth": 0.05631132951261328,
        "error": 0.0004532596613317053,
        "red_noise_beta": 1.942131211104606,
        "n_core": 116,
        "baseline_degree": 2,
        "background_regressed_depth": 0.056338739826469336,
        "background_template_native_sigma": 0.27252607792339284
      }
    }
  }
}
```

Batch difference image: sector56, deficit-minus-light=0.12arcsec; deficit-minus-WCS=0.8arcsec; PSF fractional residual=0.283. Duplicate legacy/new-schema rows are a single observation. Relative light/deficit offsets receive more weight than uncalibrated WCS offsets.

Neighbor dilution within60arcsec, G<15 (Gaia G approximates TESS; not a color-corrected flux ratio):

```json
[]
```

## Current archives and novelty

SIMBAD exact Gaia-ID: [{"id": "Gaia DR3 2812131799856915968", "main_id": "UCAC4 517-141331", "otype": "SB*", "ra": "349.76188432019666", "dec": "13.285064206886112"}]. This SB* classification establishes spectroscopy, not a prior eclipse discovery. Gaia vari_eclipsing_binary rows=0; vari_summary=[]; current ExoFOP={"toi_count": 0, "ctoi_count": 0}.
Fresh shared VSX60arcsec result: {"B_vsx_vsx": []}. ROT is not prior eclipse classification. A cone neighbor must not be assigned to target.

Nine-catalog IDIA and Harvard cone requests each timed out (idia-receipts.json and idia-mirror-receipts.json). Consequently ASAS-SN, SB9, WDS, Kostov2/3/4, IJspeert and Prsa current per-object coverage is unavailable, not empty. Batched exact-name web queries on2026-10-30 returned no relevant source and do not prove novelty. Shared source receipts preserve current Gaia/VSX/SIMBAD/ExoFOP query provenance. The original paper/source records were checked live and remain unchanged.

## Follow-up and predictions

Refine stellar radii, light ratio and RV/eclipsing joint orbit with resolved photometry or spectroscopy; retry unavailable catalogs before any novelty claim.
Next fitted primary after2026-10-30: BTJD4344.01569, conditional linear-ephemeris1sigma=0.00095d. Next secondary template phase: BTJD4346.98314; phase/systematic uncertainty is uncalibrated, so do not use it as a precise scheduling window. For undetected secondary kinds use the Gaia covariance windows, not this optimized scan prediction.

Reviewed by fresh Sol lead G with fresh GPT-6.1 Terra numerical helper; measurements and script assumptions were independently inspected.