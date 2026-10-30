# TIC 150696021: CONFIRMED

Seven primaries and five independently detected secondaries recur with the RV period. The G13.86 neighbor19.3 arcsec away is capable in a dilution-only test, but per-pixel regression in four events favors the target every time, with the free centroid on target. Physical EB is confirmed; geometry and component luminosities remain conditional.

Full review: COMPLETED_WITH_ARCHIVE_LIMITATION. Physical verdict is separate from novelty. Novelty: LIMITED_PRIOR_ART_COVERAGE; no prior target EB was established by the available current sources. New nine-catalog passes to both IDIA and Harvard timed out and are not negative matches.

## Raw SAP and event measurements

Primary P=7.760015435 +/- 0.000012413 d; Tref=3154.8847230 +/- 0.0006042 BTJD at cycle42; T0=2828.9640747. 7 fitted primary events, O-C RMS=3.173 min; chi2/dof=17.66/5. Shape T14=5.765h, profile range=[0.2347758620689655, 0.24563793103448273], ingress fraction=0.35; T12=fr*T14 and nominal T23=T14-2*T12. Trapezoid flat time is not totality for grazing systems.

|sector|mid BTJD|error d|depth ppt|error ppt|O-C min|flagged core|
|---|---:|---:|---:|---:|---:|---:|
|56|2828.9633588|0.000721|62.666|0.443|-1.031|0|
|56|2836.7219254|0.001441|61.393|1.591|-3.117|0|
|56|2844.4848157|0.000721|62.243|0.498|1.023|0|
|56|2852.2491472|0.002162|59.027|2.534|7.238|0|
|83|3566.1655448|0.000721|61.404|0.443|0.005|0|
|83|3573.9269939|0.000721|62.146|0.524|2.070|0|
|83|3581.6841192|0.000721|62.052|0.436|-2.092|0|

Primary median depth=62.052ppt; maximum absolute background-regression fake depth=0.459ppt. Background native units were not treated as normalized flux. 0 event timing fits hit a scan edge. Quality-zero fits use exposure integration, local quadratic baselines, red-noise beta and grid floors; flagged-core counts and centroid/background regressions are retained in fit-results.json. Source variability and shape errors may exceed these conditional errors.

Blind rolling-median census covers all available sectors without the old post-gap trim. No off-eclipse census dip exceeds30%of the primary depth outside0.08phase of either fitted eclipse kind. Smaller candidates, gaps, sector edges and all threshold details remain in fit-results.json; this is a diagnostic census, not a calibrated false-positive probability.

## Gaia and physical feasibility

Own-source SB1 covariance verified: bit_index=127,15 correlations in P,gamma,K1,e,omega,Tp order; omega-Tp correlation=0.9998698. Primary assigned conjunctionA; period discrepancy=1.585sigma.
ConjunctionA at Gaia epoch: offset=-0.027202d, Gaia-only sigma=0.045108d; including photometric extrapolation sigma=0.045329d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.
ConjunctionB at Gaia epoch: offset=-3.836545d, Gaia-only sigma=0.032742d; including photometric extrapolation sigma=0.033046d. Full epoch-by-epoch comparisons are retained in orbit-gates.json.

Mass-function/assumed-stellar-radius checks (not measured binary parameters):

```json
[
  {
    "m1": 1.04,
    "m2_min": 0.5761781061580149,
    "f_mass": 0.07323046921808257,
    "a_rsun": 19.35622502108516,
    "r1_rsun": 2.21953,
    "r2_approx_rsun": 0.6433471796556982,
    "central_T14_hours": {
      "A": 8.690817982022358,
      "B": 8.841584787207033
    },
    "observed_T14_hours": 5.764965517241379
  }
]
```

Limb-darkened two-sphere feasibility permits free primary/secondary flux scales and fixed TIC stellar dimensions. It does not identify the foreground component from eclipse depth alone. Using Gaia primary spectroscopic omega and positive RV away from the observer, at A (nu+omega=90deg) the RV primary is behind and the companion is foreground; at B (270deg) the primary is foreground. The deeper eclipse is assigned A here; luminosity and component labeling remain conditional. Minimum RV companion mass and eclipse luminosity/shape jointly allow a stellar companion.

```json
{
  "status": "conditional shape feasibility",
  "best": {
    "chi2": 159.6936691260499,
    "dof": 121,
    "k": 0.27499999999999997,
    "b_A": 0.7950000000000002,
    "e_sin_omega": 0.09999999999999992,
    "primary_scale": 0.965047812455021,
    "secondary_scale": 0.03576951779831132
  },
  "profile_interval_approx_95": {
    "k": [
      0.27499999999999997,
      0.27499999999999997
    ],
    "b_A": [
      0.7950000000000002,
      0.7950000000000002
    ],
    "e_sin_omega": [
      0.09999999999999992,
      0.09999999999999992
    ]
  },
  "error_inflation": 1.3197823894714868,
  "assumptions": "Circular projected chord with eccentric speed factors; fixed TIC R1/M1, u1=.4 u2=.6, free depth scales per kind, event-scatter bin errors and 0.15ppt floor. Contact shape and dilution degeneracies persist. No claim of precise e sin omega.",
  "primary_profile_n": 64,
  "secondary_profile_n": 64
}
```

## Secondary evidence

Optimized secondary phase=0.500334; pooled depth=18.164ppt, empirical error=0.291ppt; 5/5 individually>3sigma. This scan optimizes phase and does not provide a calibrated phase error or global significance. Repeat events, independent reduction, and off-phase controls are more informative than its raw peak S/N.

```json
{
  "bit_index": 127,
  "gaia_primary": "A",
  "gaia_relative_phase_nominal": 0.48795244650292313,
  "gaia_relative_phase_quantiles_16_50_84": [
    0.48208999389226315,
    0.49135494381916045,
    0.49861539131737936
  ],
  "gaia_relative_phase_sigma": 0.008786686515241409,
  "gaia_e_cos_omega_quantiles": [
    -0.028132585905592058,
    -0.013577905964244942,
    -0.0021748370861388523
  ],
  "gaia_e_sin_omega_quantiles": [
    -0.006122724569791174,
    0.0064428506808386935,
    0.023589563952668976
  ],
  "photometric_phase": 0.500334220666431,
  "photometric_e_cos_omega_first_order": 0.0005249925951686977,
  "photometric_note": "First-order small-e approximation; fitted profile phase is optimized and conditional on eclipse shape, with no calibrated uncertainty. Omitted without three individual secondary detections.",
  "geometry_status": "conditional shape feasibility",
  "geometry_e_sin_omega_conditional_range": [
    0.09999999999999992,
    0.09999999999999992
  ],
  "geometry_note": "Coarse conditional feasibility range, fixed TIC properties and simplified limb-darkened shape; not a calibrated posterior. Check chi2 and grid boundaries in geometry.json."
}
```

|sector|secondary mid BTJD|error d|depth ppt|error ppt|
|---|---:|---:|---:|---:|
|56|2832.8452347|0.000721|17.713|0.357|
|56|2840.6052502|0.000721|18.322|0.267|
|56|2848.3638244|0.000721|19.407|0.312|
|83|3562.2881269|0.000721|18.111|0.284|
|83|3570.0452598|0.000721|17.567|0.235|

Secondary ephemeris: {"P": 7.760020297125379, "P_error": 1.3299521850682019e-05, "Tref": 3127.725531071351, "Tref_error": 0.000609286499375676, "reference_cycle": 38, "T0": 2832.844759780586, "chi2": 10.722296342587057, "dof": 3, "n": 5, "oc_rms_minutes": 1.519595923750579}. Two-event periods and optimized shapes are not precise independent orbit constraints. Covered/uncovered/flagged secondary windows are enumerated individually in orbit-gates.json secondary_windows, and null-secondary.json when applicable.

## Independence and source attribution

TESS-SPOC sector56, exact FITS identity validated=True. Same TESS pixels through a different reduction, not another observatory. Exact product/time coverage/URLs/SHA256 are in independent manifests; every measured event and degree1/2 background/baseline comparison is in independent-summary.json (alternate summary for345589621).

```json
{
  "tc": 2828.963358758621,
  "qlp": {
    "1": {
      "depth": 0.06318850663584949,
      "error": 0.00041747144977343105,
      "red_noise_beta": 1.7296763722544908,
      "n_core": 104,
      "baseline_degree": 1,
      "background_regressed_depth": 0.06324672190506934,
      "background_template_native_sigma": 0.13955170518400567
    },
    "2": {
      "depth": 0.06292773318870623,
      "error": 0.0004512306029557722,
      "red_noise_beta": 1.6938440822198069,
      "n_core": 104,
      "baseline_degree": 2,
      "background_regressed_depth": 0.0629704148190884,
      "background_template_native_sigma": 0.10126210262284988
    }
  },
  "independent": {
    "SAP_FLUX": {
      "1": {
        "depth": 0.05669834430782072,
        "error": 0.00037498421791336116,
        "red_noise_beta": 1.8061769624469866,
        "n_core": 104,
        "baseline_degree": 1,
        "background_regressed_depth": 0.05672563580678699,
        "background_template_native_sigma": 0.34741947025150316
      },
      "2": {
        "depth": 0.05656965951709012,
        "error": 0.0004130892078825761,
        "red_noise_beta": 1.7976618721637025,
        "n_core": 104,
        "baseline_degree": 2,
        "background_regressed_depth": 0.056591328924534445,
        "background_template_native_sigma": 0.2502854431842343
      }
    },
    "PDCSAP_FLUX": {
      "1": {
        "depth": 0.0631983945458318,
        "error": 0.0007024024432912891,
        "red_noise_beta": 2.6691119853672465,
        "n_core": 104,
        "baseline_degree": 1,
        "background_regressed_depth": 0.06303200093126982,
        "background_template_native_sigma": 0.34741947025150316
      },
      "2": {
        "depth": 0.06258498316350793,
        "error": 0.0007396150306909728,
        "red_noise_beta": 2.586373262416255,
        "n_core": 104,
        "baseline_degree": 2,
        "background_regressed_depth": 0.06247346276822013,
        "background_template_native_sigma": 0.2502854431842343
      }
    }
  }
}
```

```json
{
  "tc": 2836.7219253572894,
  "qlp": {
    "1": {
      "depth": 0.05779548979003091,
      "error": 0.0016914676725034198,
      "red_noise_beta": 3.260992815015399,
      "n_core": 104,
      "baseline_degree": 1,
      "background_regressed_depth": 0.059677131334476795,
      "background_template_native_sigma": -1.1402130119008185
    },
    "2": {
      "depth": 0.06048425963833052,
      "error": 0.0015860016817420789,
      "red_noise_beta": 3.068950849767196,
      "n_core": 104,
      "baseline_degree": 2,
      "background_regressed_depth": 0.060855541728110155,
      "background_template_native_sigma": -0.33848661278126757
    }
  },
  "independent": {
    "SAP_FLUX": {
      "1": {
        "depth": 0.05629363327148408,
        "error": 0.0004109561110479489,
        "red_noise_beta": 1.9079512047866956,
        "n_core": 104,
        "baseline_degree": 1,
        "background_regressed_depth": 0.05612608951901542,
        "background_template_native_sigma": -0.9355152621273938
      },
      "2": {
        "depth": 0.05639880386723798,
        "error": 0.00045394519266711894,
        "red_noise_beta": 1.903115475189127,
        "n_core": 104,
        "baseline_degree": 2,
        "background_regressed_depth": 0.05631892450001077,
        "background_template_native_sigma": -0.25821173226487065
      }
    },
    "PDCSAP_FLUX": {
      "1": {
        "depth": 0.0573290979749512,
        "error": 0.0014905494147139015,
        "red_noise_beta": 3.6557481348981473,
        "n_core": 104,
        "baseline_degree": 1,
        "background_regressed_depth": 0.06025255682689771,
        "background_template_native_sigma": -0.9355152621273938
      },
      "2": {
        "depth": 0.059568478937806174,
        "error": 0.0014216459275203017,
        "red_noise_beta": 3.5510603280767636,
        "n_core": 104,
        "baseline_degree": 2,
        "background_regressed_depth": 0.06035714104162983,
        "background_template_native_sigma": -0.25821173226487065
      }
    }
  }
}
```

Batch difference image: sector56, deficit-minus-light=2.17arcsec; deficit-minus-WCS=3.82arcsec; PSF fractional residual=0.168. Duplicate legacy/new-schema rows are a single observation. Relative light/deficit offsets receive more weight than uncalibrated WCS offsets.

Neighbor dilution within60arcsec, G<15 (Gaia G approximates TESS; not a color-corrected flux ratio):

```json
[
  {
    "source_id": "1881109883677908224",
    "ra": "338.4257912309341",
    "dec": "26.974684521364487",
    "phot_g_mean_mag": "13.864994",
    "bp_rp": "1.2449017",
    "sep": "19.30089117189746",
    "required_fraction_G_approx": 0.6781701809487413,
    "capable": true
  }
]
```

pixel-localization.json:
```json
{
  "calibration": {
    "sigma_pixels": 0.6500000000000001,
    "dx_pixels": 0.09999999999999987,
    "dy_pixels": -1.1102230246251565e-16
  },
  "free_best": {
    "chi2": 9653.358143825943,
    "pixel_x": 7.099169734214097,
    "pixel_y": 7.023534238890427,
    "distance_from_target_arcsec": 2.1102042644709938e-13,
    "fractional_residual": 0.11270363370544775
  },
  "fixed_fits": [
    {
      "source_id": "1881109883677907584",
      "sep_arcsec": 0.0,
      "G": 11.268545,
      "chi2": 9653.358143825833,
      "amplitude": 145.262575953447,
      "fractional_residual": 0.11270363370544757
    },
    {
      "source_id": "1881109883677908224",
      "sep_arcsec": 19.30089117189746,
      "G": 13.864994,
      "chi2": 100245.0204413415,
      "amplitude": 67.76468725916556,
      "fractional_residual": 0.7806075339091613
    }
  ],
  "caution": "Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity."
}
```
Individual event source comparisons are in pixel-localization.json; approximate PSF chi-square excludes model/correlated-noise errors and is not formal localization significance.

## Current archives and novelty

SIMBAD exact Gaia-ID: [{"id": "Gaia DR3 1881109883677907584", "main_id": "TYC 2227-1936-1", "otype": "SB*", "ra": "338.41975979931", "dec": "26.97456707901"}]. This SB* classification establishes spectroscopy, not a prior eclipse discovery. Gaia vari_eclipsing_binary rows=0; vari_summary=[]; current ExoFOP={"toi_count": 0, "ctoi_count": 0}.
Fresh shared VSX60arcsec result: {"B_vsx_vsx": [{"_r": "19.62", "Name": "Gaia DR3 1881109883677908224", "Type": "ROT", "Period": "", "RAJ2000": "338.42587", "DEJ2000": "26.97467"}]}. ROT is not prior eclipse classification. A cone neighbor must not be assigned to target.

Nine-catalog IDIA and Harvard cone requests each timed out (idia-receipts.json and idia-mirror-receipts.json). Consequently ASAS-SN, SB9, WDS, Kostov2/3/4, IJspeert and Prsa current per-object coverage is unavailable, not empty. Batched exact-name web queries on2026-10-30 returned no relevant source and do not prove novelty. Shared source receipts preserve current Gaia/VSX/SIMBAD/ExoFOP query provenance. The original paper/source records were checked live and remain unchanged.

## Follow-up and predictions

Refine stellar radii, light ratio and RV/eclipsing joint orbit with resolved photometry or spectroscopy; retry unavailable catalogs before any novelty claim.
Next fitted primary after2026-10-30: BTJD4349.92710, conditional linear-ephemeris1sigma=0.00200d. Next secondary template phase: BTJD4346.04969; phase/systematic uncertainty is uncalibrated, so do not use it as a precise scheduling window. For undetected secondary kinds use the Gaia covariance windows, not this optimized scan prediction.

Reviewed by fresh Sol lead G with fresh GPT-6.1 Terra numerical helper; measurements and script assumptions were independently inspected.