# TIC 335862015: CONFIRMED

Three deep primary and two secondary events in sector91, recovered by TARS and localized to target against a capable49.5arcsec neighbor in all three events, establish a physical EB. The short baseline, poor fixed-TIC geometry and discrepant Gaia-median secondary phase require future orbit/stellar characterization; they do not erase the localized eclipses.

Full review: COMPLETED_WITH_ARCHIVE_LIMITATION. Physical verdict is separate from novelty. Novelty: LIMITED_PRIOR_ART_COVERAGE; no prior target EB was established by the available current sources. New nine-catalog passes to both IDIA and Harvard timed out and are not negative matches.

## Raw SAP and event measurements

Primary P=6.577232276 +/- 0.000439950 d; Tref=3790.2187995 +/- 0.0005680 BTJD at cycle2; T0=3777.0643350. 3 fitted primary events, O-C RMS=0.422 min; chi2/dof=0.29/1. Shape T14=7.603h, profile range=[0.30892499999999995, 0.324675], ingress fraction=0.25; T12=fr*T14 and nominal T23=T14-2*T12. Trapezoid flat time is not totality for grazing systems.

|sector|mid BTJD|error d|depth ppt|error ppt|O-C min|flagged core|
|---|---:|---:|---:|---:|---:|---:|
|91|3777.0641992|0.000950|64.194|0.609|-0.196|0|
|91|3790.2192068|0.000950|64.158|0.556|0.587|0|
|91|3796.7957603|0.000950|64.514|0.565|-0.391|0|

Primary median depth=64.194ppt; maximum absolute background-regression fake depth=0.017ppt. Background native units were not treated as normalized flux. 0 event timing fits hit a scan edge. Quality-zero fits use exposure integration, local quadratic baselines, red-noise beta and grid floors; flagged-core counts and centroid/background regressions are retained in fit-results.json. Source variability and shape errors may exceed these conditional errors.

Blind rolling-median census covers all available sectors without the old post-gap trim. No off-eclipse census dip exceeds30%of the primary depth outside0.08phase of either fitted eclipse kind. Smaller candidates, gaps, sector edges and all threshold details remain in fit-results.json; this is a diagnostic census, not a calibrated false-positive probability.

## Gaia and physical feasibility

Own-source SB1 covariance verified: bit_index=127,15 correlations in P,gamma,K1,e,omega,Tp order; omega-Tp correlation=0.9971951. Primary assigned conjunctionA; period discrepancy=-0.676sigma.
ConjunctionA at Gaia epoch: offset=0.403832d, Gaia-only sigma=0.067549d; including photometric extrapolation sigma=0.237324d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.
ConjunctionB at Gaia epoch: offset=-3.120511d, Gaia-only sigma=0.101962d; including photometric extrapolation sigma=0.249311d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.

Mass-function/assumed-stellar-radius checks (not measured binary parameters):

```json
[
  {
    "m1": 1.03,
    "m2_min": 0.5133488316115586,
    "f_mass": 0.05679492608907814,
    "a_rsun": 17.073422623562458,
    "r1_rsun": 2.27928,
    "r2_approx_rsun": 0.5865837968306765,
    "central_T14_hours": {
      "A": 8.28802641296841,
      "B": 8.557267064253015
    },
    "observed_T14_hours": 7.603199999999999
  }
]
```

Limb-darkened two-sphere feasibility permits free primary/secondary flux scales and fixed TIC stellar dimensions. It does not identify the foreground component from eclipse depth alone. Using Gaia primary spectroscopic omega and positive RV away from the observer, at A (nu+omega=90deg) the RV primary is behind and the companion is foreground; at B (270deg) the primary is foreground. The deeper eclipse is assigned A here; luminosity and component labeling remain conditional. Minimum RV companion mass and eclipse luminosity/shape jointly allow a stellar companion.

```json
{
  "status": "conditional shape feasibility",
  "best": {
    "chi2": 956.7807932435624,
    "dof": 121,
    "k": 0.24999999999999997,
    "b_A": 0.23500000000000001,
    "e_sin_omega": 0.04999999999999993,
    "primary_scale": 0.9129607255190911,
    "secondary_scale": 0.008347226128724176
  },
  "profile_interval_approx_95": {
    "k": [
      0.24999999999999997,
      0.24999999999999997
    ],
    "b_A": [
      0.2,
      0.23500000000000001
    ],
    "e_sin_omega": [
      0.04999999999999993,
      0.04999999999999993
    ]
  },
  "error_inflation": 7.907279283004647,
  "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
  "primary_profile_n": 64,
  "secondary_profile_n": 64
}
```

## Secondary evidence

Optimized secondary phase=0.500277; pooled depth=8.230ppt, empirical error=0.157ppt; 2/2 individually>3sigma. This scan optimizes phase and does not provide a calibrated phase error or global significance. Repeat events, independent reduction, and off-phase controls are more informative than its raw peak S/N.

```json
{
  "bit_index": 127,
  "gaia_primary": "A",
  "gaia_relative_phase_nominal": 0.53597893199964,
  "gaia_relative_phase_quantiles_16_50_84": [
    0.5136469640922227,
    0.5354260178365298,
    0.562769152758785
  ],
  "gaia_relative_phase_sigma": 0.023913737021386976,
  "gaia_e_cos_omega_quantiles": [
    0.021436106625961644,
    0.05563908995520599,
    0.09866611237134963
  ],
  "gaia_e_sin_omega_quantiles": [
    -0.008708233389776276,
    0.01219100172992036,
    0.04755889384437401
  ],
  "photometric_phase": null,
  "photometric_e_cos_omega_first_order": null,
  "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
  "geometry_status": "conditional shape feasibility",
  "geometry_e_sin_omega_conditional_range": [
    0.04999999999999993,
    0.04999999999999993
  ],
  "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
}
```

|sector|secondary mid BTJD|error d|depth ppt|error ppt|
|---|---:|---:|---:|---:|
|91|3780.3529676|0.000903|8.407|0.241|
|91|3793.5074322|0.000903|8.098|0.208|

Secondary ephemeris: null. Two-event periods and optimized shapes are not precise independent orbit constraints. Covered/uncovered/flagged secondary windows are enumerated individually in orbit-gates.json secondary_windows, and null-secondary.json when applicable.

## Independence and source attribution

TARS sector91, exact FITS identity validated=True. Same TESS pixels through a different reduction, not another observatory. Exact product/time coverage/URLs/SHA256 are in independent manifests; every measured event and degree1/2 background/baseline comparison is in independent-summary.json (alternate summary for345589621).

```json
{
  "tc": 3777.0641992,
  "qlp": {
    "1": {
      "depth": 0.06546150571224707,
      "error": 0.0006033190373236466,
      "red_noise_beta": 2.432778713279399,
      "n_core": 137,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06547532501264686,
      "background_template_native_sigma": 0.3822669075696377
    },
    "2": {
      "depth": 0.06462614598179718,
      "error": 0.0006250413303067231,
      "red_noise_beta": 2.322741905576321,
      "n_core": 137,
      "baseline_degree": 2,
      "background_regressed_depth": 0.06461390899878607,
      "background_template_native_sigma": -0.06196644739084536
    }
  },
  "independent": {
    "FLUX": {
      "1": {
        "depth": 0.07345961536855511,
        "error": 0.0006693451269136685,
        "red_noise_beta": 1.600139362680759,
        "n_core": 137,
        "baseline_degree": 1,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      },
      "2": {
        "depth": 0.07350565707457783,
        "error": 0.0007473369010430314,
        "red_noise_beta": 1.5994856115880274,
        "n_core": 137,
        "baseline_degree": 2,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      }
    }
  }
}
```

```json
{
  "tc": 3790.21920683697,
  "qlp": {
    "1": {
      "depth": 0.06477067923744757,
      "error": 0.0005382538618033496,
      "red_noise_beta": 2.193099247993015,
      "n_core": 136,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06476844559500948,
      "background_template_native_sigma": -0.02349672625315945
    },
    "2": {
      "depth": 0.06409101255483318,
      "error": 0.0005622363902128375,
      "red_noise_beta": 2.0834206013445185,
      "n_core": 136,
      "baseline_degree": 2,
      "background_regressed_depth": 0.064092635290639,
      "background_template_native_sigma": 0.01983459784663881
    }
  },
  "independent": {
    "FLUX": {
      "1": {
        "depth": 0.06733148627972271,
        "error": 0.0007295288358141654,
        "red_noise_beta": 1.7134792410314077,
        "n_core": 136,
        "baseline_degree": 1,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      },
      "2": {
        "depth": 0.06696502653416919,
        "error": 0.0008114734167832886,
        "red_noise_beta": 1.6993420484511348,
        "n_core": 136,
        "baseline_degree": 2,
        "background_regressed_depth": null,
        "background_template_native_sigma": null
      }
    }
  }
}
```

Batch difference image: sector91, deficit-minus-light=5.5arcsec; deficit-minus-WCS=3.09arcsec; PSF fractional residual=0.308. Duplicate legacy/new-schema rows are a single observation. Relative light/deficit offsets receive more weight than uncalibrated WCS offsets.

Neighbor dilution within60arcsec, G<15 (Gaia G approximates TESS; not a color-corrected flux ratio):

```json
[
  {
    "source_id": "6310152241747719552",
    "ra": "224.22186487079426",
    "dec": "-15.146044956835752",
    "phot_g_mean_mag": "12.536925",
    "bp_rp": "0.82973576",
    "sep": "49.53926082922907",
    "required_fraction_G_approx": 0.18294415583788728,
    "capable": true
  }
]
```

pixel-localization.json:
```json
{
  "calibration": {
    "sigma_pixels": 0.7500000000000001,
    "dx_pixels": -0.10000000000000009,
    "dy_pixels": -1.1102230246251565e-16
  },
  "free_best": {
    "chi2": 16231.41189742049,
    "pixel_x": 7.205778292784393,
    "pixel_y": 7.461464210057608,
    "distance_from_target_arcsec": 2.1102042644709938e-13,
    "fractional_residual": 0.12311846200098397
  },
  "fixed_fits": [
    {
      "source_id": "6310152211684175104",
      "sep_arcsec": 0.0,
      "G": 11.399861,
      "chi2": 16231.411897420277,
      "amplitude": 107.5616393356673,
      "fractional_residual": 0.12311846200098274
    },
    {
      "source_id": "6310152241747719552",
      "sep_arcsec": 49.53926082922907,
      "G": 12.536925,
      "chi2": 260189.39519202718,
      "amplitude": 5.9570387695799445,
      "fractional_residual": 0.9881512892252862
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```
Individual event source comparisons are in pixel-localization.json; approximate PSF chi-square excludes model/correlated-noise errors and is not formal localization significance.

## Current archives and novelty

SIMBAD exact Gaia-ID: [{"id": "Gaia DR3 6310152211684175104", "main_id": "TYC 6168-1001-1", "otype": "SB*", "ra": "224.21401891473", "dec": "-15.157451048150003"}]. This SB* classification establishes spectroscopy, not a prior eclipse discovery. Gaia vari_eclipsing_binary rows=0; vari_summary=[]; current ExoFOP={"toi_count": 0, "ctoi_count": 0}.
Fresh shared VSX60arcsec result: {"B_vsx_vsx": []}. ROT is not prior eclipse classification. A cone neighbor must not be assigned to target.

Nine-catalog IDIA and Harvard cone requests each timed out (idia-receipts.json and idia-mirror-receipts.json). Consequently ASAS-SN, SB9, WDS, Kostov2/3/4, IJspeert and Prsa current per-object coverage is unavailable, not empty. Batched exact-name web queries on2026-10-30 returned no relevant source and do not prove novelty. Shared source receipts preserve current Gaia/VSX/SIMBAD/ExoFOP query provenance. The original paper/source records were checked live and remain unchanged.

## Follow-up and predictions

Refine stellar radii, light ratio and RV/eclipsing joint orbit with resolved photometry or spectroscopy; retry unavailable catalogs before any novelty claim.
Next fitted primary after2026-10-30: BTJD4349.28354, conditional linear-ephemeris1sigma=0.03740d. Next secondary template phase: BTJD4345.99675; phase/systematic uncertainty is uncalibrated, so do not use it as a precise scheduling window. For undetected secondary kinds use the Gaia covariance windows, not this optimized scan prediction.

Reviewed by fresh Sol lead G with fresh GPT-6.1 Terra numerical helper; measurements and script assumptions were independently inspected.