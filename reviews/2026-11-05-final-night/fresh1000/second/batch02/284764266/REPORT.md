# Z109 TIC 284764266

Lead verdict: PLAUSIBLE. Gaia DR3 669955803723072128; actual G=11.670815. Association: Gaia association uncertain; full versus half clock retained. Catalogue status: NO_EXACT_EB_IDENTIFICATION_IN_FINAL_CENTRAL_SCOPE.

Broad flat-bottomed source-localized events repeat in consecutive sectors71/72 at3257.41732 and3283.52353. Widened local fits recover43.5/43.7ppt; original0.9d-bound fits were unusable and superseded. Period26.10621889d; covered half-clock windows contain shallower depressions and do not supply clean nulls. Difference Gaussian0.067pixel from target; independently widened source-window centroid0.146pixel confirms source attribution. Gaia conjunction offsets3.95/3.98d exceed local covariance1.19/1.20d, so Gaia association remains uncertain. Exact VSX ROT period13.041d is a non-eclipsing prior classification retained as context, not an EB recovery.

Limitations: Occultations are not established over rotational minima: only two broad same-kind losses, curved surroundings, exact prior ROT13.041d, half-period ambiguity and Gaia3.3sigma discrepancy. Spatial localization establishes source, not eclipse physics;2-event formal period precision is conditional.

Next check: Measure another same-kind broad eclipse, discriminate half clock and reassess Gaia orbit.

Bounded review follows paper Section2.7: representative quality0 raw SAP events, fitted same-kind timings, covered integer alternatives, alternate extraction, deciding pixels, Gaia neighbors and source-specific covariance. Independent reductions reuse the same TESS photons. Missing coverage is never a null. G flux is an approximate capability screen, not a TESS aperture-throughput model. Central sealed shared-catalogues supply dated catalogue scope; nonmatch is not exhaustive novelty proof. No queue replacement, ledger or public edits.

Numeric evidence: lead-context.json, lead-series.json, lead-timing.json, helper-localization.json/png, lead-neighbors.json, lead-capability-audit.json; batch-level clocks/aliases/Gaia-covariance/identity-audit and source hashes. See helper-independent-audit.md for independent source adjudication.

```json
{
  "clock": {
    "period_d": 26.106218890484804,
    "epoch_btjd": 3257.417315816375,
    "formal_period_error_d": 0.006300507378514793,
    "cycles": [
      0,
      1
    ],
    "times": [
      3257.417315816375,
      3283.5235347068597
    ],
    "residuals": [
      0.0,
      0.0
    ],
    "duration_d": 1.8930188962012964,
    "depth_ppt": 43.613522957704525,
    "max_residual_d": 0.0,
    "gaia_period_d": 26.081158006652863,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "gaia_geometry": {
    "source_id": "669955803723072128",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 26.081158006652863,
    "gaia_period_error_d": 0.010120179,
    "eccentricity": 0.04141391330919141,
    "omega_deg": 273.9398641979539,
    "tp_btjd": 384.80186434163807,
    "mass_function_solar": 0.15921877081598834,
    "events": [
      {
        "sector": 71,
        "event_kind": "candidate",
        "observed_btjd": 3257.417315816375,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 110,
            "predicted_btjd": 3266.4600139849895,
            "offset_d": -9.042698168614606,
            "phase_offset": -0.3467138294360997,
            "linear_covariance_sigma_d": 1.2714133164067103
          },
          {
            "kind": 1,
            "cycle": 109,
            "predicted_btjd": 3253.4667217873166,
            "offset_d": 3.9505940290582657,
            "phase_offset": 0.1514731066791795,
            "linear_covariance_sigma_d": 1.191317060583368
          }
        ]
      },
      {
        "sector": 72,
        "event_kind": "candidate",
        "observed_btjd": 3283.5235347068597,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 111,
            "predicted_btjd": 3292.5411719916424,
            "offset_d": -9.017637284782722,
            "phase_offset": -0.34575294864140904,
            "linear_covariance_sigma_d": 1.2814347145753473
          },
          {
            "kind": 1,
            "cycle": 110,
            "predicted_btjd": 3279.5478797939695,
            "offset_d": 3.9756549128901497,
            "phase_offset": 0.1524339874738701,
            "linear_covariance_sigma_d": 1.2013257561348538
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
