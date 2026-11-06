# Z110 TIC 294833711

Lead verdict: C. Gaia DR3 5811982081764875392; actual G=11.7779045. Association: consistent with Gaia-selected orbit. Catalogue status: NO_EXACT_EB_IDENTIFICATION_IN_FINAL_CENTRAL_SCOPE.

Three usable raw-event fits3107.27232,4108.86535,4167.77965 give58.91714771d. The latter two events are consecutive same-kind cycles. Original S12 event is visibly real but its screen window was offset enough to fail the local fit; it is not used as a timing point. Covered divisor windows2..6 show clean nulls. Difference Gaussian0.170pixel from target; alternative aperture10ppt. Brightest capable neighbor at1.77pixel is1.93pixels from difference Gaussian. Gaia conjunction residuals0.30..0.55d fit covariance0.86..1.21d.

Limitations: Local formal timing model; representative events rather than all-event precision characterization.

Next check: Additional same-kind timings can refine period.

Bounded review follows paper Section2.7: representative quality0 raw SAP events, fitted same-kind timings, covered integer alternatives, alternate extraction, deciding pixels, Gaia neighbors and source-specific covariance. Independent reductions reuse the same TESS photons. Missing coverage is never a null. G flux is an approximate capability screen, not a TESS aperture-throughput model. Central sealed shared-catalogues supply dated catalogue scope; nonmatch is not exhaustive novelty proof. No queue replacement, ledger or public edits.

Numeric evidence: lead-context.json, lead-series.json, lead-timing.json, helper-localization.json/png, lead-neighbors.json, lead-capability-audit.json; batch-level clocks/aliases/Gaia-covariance/identity-audit and source hashes. See helper-independent-audit.md for independent source adjudication.

```json
{
  "clock": {
    "period_d": 58.91714770674514,
    "epoch_btjd": 3107.27240904421,
    "formal_period_error_d": 0.00014856972801350395,
    "cycles": [
      0,
      17,
      18
    ],
    "times": [
      3107.27231512498,
      4108.865352064356,
      4167.779650420944
    ],
    "residuals": [
      -9.391922958457144e-05,
      0.0014320054788186098,
      -0.0014173446788845467
    ],
    "duration_d": 0.6484909574313734,
    "depth_ppt": 9.631260751478761,
    "max_residual_d": 0.0014320054788186098,
    "gaia_period_d": 58.93094058479923,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "gaia_geometry": {
    "source_id": "5811982081764875392",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 58.93094058479923,
    "gaia_period_error_d": 0.019916045,
    "eccentricity": 0.3820510568727869,
    "omega_deg": 46.411816489428205,
    "tp_btjd": 393.6387615287455,
    "mass_function_solar": 0.023305714352998667,
    "events": [
      {
        "sector": 66,
        "event_kind": "candidate",
        "observed_btjd": 3107.27231512498,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 46,
            "predicted_btjd": 3107.5745050878495,
            "offset_d": -0.30218996286930633,
            "phase_offset": -0.005127865937155156,
            "linear_covariance_sigma_d": 0.8608832557476004
          },
          {
            "kind": 1,
            "cycle": 45,
            "predicted_btjd": 3088.2627033011845,
            "offset_d": 19.009611823795694,
            "phase_offset": 0.3225743834249792,
            "linear_covariance_sigma_d": 1.0206825336492742
          }
        ]
      },
      {
        "sector": 101,
        "event_kind": "candidate",
        "observed_btjd": 4108.865352064356,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 63,
            "predicted_btjd": 4109.400495029437,
            "offset_d": -0.5351429650809223,
            "phase_offset": -0.00908084886768222,
            "linear_covariance_sigma_d": 1.1939717318122642
          },
          {
            "kind": 1,
            "cycle": 62,
            "predicted_btjd": 4090.0886932427716,
            "offset_d": 18.77665882158408,
            "phase_offset": 0.31862140049445214,
            "linear_covariance_sigma_d": 1.343435945725645
          }
        ]
      },
      {
        "sector": 103,
        "event_kind": "candidate",
        "observed_btjd": 4167.779650420944,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 64,
            "predicted_btjd": 4168.3314356142355,
            "offset_d": -0.5517851932918347,
            "phase_offset": -0.00936325108366187,
            "linear_covariance_sigma_d": 1.2136596916654971
          },
          {
            "kind": 1,
            "cycle": 63,
            "predicted_btjd": 4149.01963382757,
            "offset_d": 18.76001659337362,
            "phase_offset": 0.31833899827848017,
            "linear_covariance_sigma_d": 1.3626605533743341
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
