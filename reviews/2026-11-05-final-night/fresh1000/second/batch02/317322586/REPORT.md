# Z114 TIC 317322586

Lead verdict: C. Gaia DR3 2231760497013084672; actual G=11.891667. Association: consistent with Gaia-selected orbit. Catalogue status: NO_EXACT_EB_IDENTIFICATION_IN_FINAL_CENTRAL_SCOPE.

Deep same-kind raw events across S17/58/59/85/86 yield34.76826217d. Opposite conjunctions at1797.177,3466.062,3639.901 are kept separate. S78 broad background minima are unusable eclipse fits and excluded. Consecutive deep S58/59 and S85/86 events secure recurrence; covered divisors2..6 have nulls. Difference Gaussian0.125pixel from target; custom aperture93ppt. Gaia conjunction residuals0.315..1.136d fit covariance0.46..1.25d.

Limitations: Broad baseline variability and cadence-based timing floors; strongest representative eclipses used.

Next check: Fit additional eclipse profiles if precision characterization is required.

Bounded review follows paper Section2.7: representative quality0 raw SAP events, fitted same-kind timings, covered integer alternatives, alternate extraction, deciding pixels, Gaia neighbors and source-specific covariance. Independent reductions reuse the same TESS photons. Missing coverage is never a null. G flux is an approximate capability screen, not a TESS aperture-throughput model. Central sealed shared-catalogues supply dated catalogue scope; nonmatch is not exhaustive novelty proof. No queue replacement, ledger or public edits.

Numeric evidence: lead-context.json, lead-series.json, lead-timing.json, helper-localization.json/png, lead-neighbors.json, lead-capability-audit.json; batch-level clocks/aliases/Gaia-covariance/identity-audit and source hashes. See helper-independent-audit.md for independent source adjudication.

```json
{
  "clock": {
    "period_d": 34.76826217454243,
    "epoch_btjd": 1782.338842208302,
    "formal_period_error_d": 9.559680067465426e-05,
    "cycles": [
      0,
      32,
      33,
      53,
      54
    ],
    "times": [
      1782.3349392732725,
      2894.932549165534,
      2929.687320541165,
      3625.0601729058694,
      3659.8217007729227
    ],
    "residuals": [
      -0.0039029350293731113,
      0.00931737187465842,
      -0.00417342703713075,
      0.0034354468184574216,
      -0.003298860670383874
    ],
    "duration_d": 0.7196076655211604,
    "depth_ppt": 105.86525337618015,
    "max_residual_d": 0.00931737187465842,
    "gaia_period_d": 34.75540766600534,
    "note": "Trials inferred from eclipse intervals; integer-cycle selection requires covered-window audit. Timing error includes cadence/2 and .002d floors."
  },
  "gaia_geometry": {
    "source_id": "2231760497013084672",
    "gaia_nss_sha256": "1fc1b0641c78c28acaf587b5375dea37d7afe3b4f44810ca3c07da371bb20ec8",
    "gaia_period_d": 34.75540766600534,
    "gaia_period_error_d": 0.012773549,
    "eccentricity": 0.13095753484899142,
    "omega_deg": 202.73521008011144,
    "tp_btjd": 401.30241929829936,
    "mass_function_solar": 0.14106805287768023,
    "events": [
      {
        "sector": 17,
        "event_kind": "candidate",
        "observed_btjd": 1782.3349392732725,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 39,
            "predicted_btjd": 1782.0202225824885,
            "offset_d": 0.31471669078405284,
            "phase_offset": 0.00905518628377019,
            "linear_covariance_sigma_d": 0.4600637485845714
          },
          {
            "kind": 1,
            "cycle": 40,
            "predicted_btjd": 1796.7286089547547,
            "offset_d": -14.393669681482152,
            "phase_offset": -0.4141418745480797,
            "linear_covariance_sigma_d": 0.5855316475604869
          }
        ]
      },
      {
        "sector": 18,
        "event_kind": "candidate",
        "observed_btjd": 1797.177225939554,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 39,
            "predicted_btjd": 1782.0202225824885,
            "offset_d": 15.157003357065605,
            "phase_offset": 0.4361048934520438,
            "linear_covariance_sigma_d": 0.4600637485845714
          },
          {
            "kind": 1,
            "cycle": 40,
            "predicted_btjd": 1796.7286089547547,
            "offset_d": 0.4486169847994006,
            "phase_offset": 0.012907832620193892,
            "linear_covariance_sigma_d": 0.5855316475604869
          }
        ]
      },
      {
        "sector": 58,
        "event_kind": "candidate",
        "observed_btjd": 2894.932549165534,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 71,
            "predicted_btjd": 2894.1932678946596,
            "offset_d": 0.7392812708744714,
            "phase_offset": 0.021270971066685854,
            "linear_covariance_sigma_d": 0.8432384368230289
          },
          {
            "kind": 1,
            "cycle": 72,
            "predicted_btjd": 2908.9016542669256,
            "offset_d": -13.969105101391506,
            "phase_offset": -0.40192608976515753,
            "linear_covariance_sigma_d": 0.9829342289461652
          }
        ]
      },
      {
        "sector": 59,
        "event_kind": "candidate",
        "observed_btjd": 2929.687320541165,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 72,
            "predicted_btjd": 2928.948675560665,
            "offset_d": 0.7386449804998847,
            "phase_offset": 0.02125266340128019,
            "linear_covariance_sigma_d": 0.8555942206603648
          },
          {
            "kind": 1,
            "cycle": 73,
            "predicted_btjd": 2943.657061932931,
            "offset_d": -13.969741391766092,
            "phase_offset": -0.4019443974305632,
            "linear_covariance_sigma_d": 0.9955011836702805
          }
        ]
      },
      {
        "sector": 79,
        "event_kind": "candidate",
        "observed_btjd": 3466.0618706433916,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 87,
            "predicted_btjd": 3450.279790550745,
            "offset_d": 15.782080092646538,
            "phase_offset": 0.45408991441879043,
            "linear_covariance_sigma_d": 1.0421405253989002
          },
          {
            "kind": 1,
            "cycle": 88,
            "predicted_btjd": 3464.988176923011,
            "offset_d": 1.073693720380561,
            "phase_offset": 0.030892853586947076,
            "linear_covariance_sigma_d": 1.1845359855852657
          }
        ]
      },
      {
        "sector": 85,
        "event_kind": "candidate",
        "observed_btjd": 3625.0601729058694,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 92,
            "predicted_btjd": 3624.0568288807717,
            "offset_d": 1.0033440250977037,
            "phase_offset": 0.028868716912766525,
            "linear_covariance_sigma_d": 1.1047073676544865
          },
          {
            "kind": 1,
            "cycle": 93,
            "predicted_btjd": 3638.7652152530377,
            "offset_d": -13.705042347168273,
            "phase_offset": -0.39432834391907684,
            "linear_covariance_sigma_d": 1.2477217205021434
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3659.8217007729227,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 93,
            "predicted_btjd": 3658.812236546777,
            "offset_d": 1.0094642261456102,
            "phase_offset": 0.02904481040321615,
            "linear_covariance_sigma_d": 1.1172384016954175
          },
          {
            "kind": 1,
            "cycle": 94,
            "predicted_btjd": 3673.520622919043,
            "offset_d": -13.698922146120367,
            "phase_offset": -0.3941522504286272,
            "linear_covariance_sigma_d": 1.2603671167754733
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3639.900734513324,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 92,
            "predicted_btjd": 3624.0568288807717,
            "offset_d": 15.843905632552378,
            "phase_offset": 0.45586878982430934,
            "linear_covariance_sigma_d": 1.1047073676544865
          },
          {
            "kind": 1,
            "cycle": 93,
            "predicted_btjd": 3638.7652152530377,
            "offset_d": 1.1355192602864008,
            "phase_offset": 0.032671728992465975,
            "linear_covariance_sigma_d": 1.2477217205021434
          }
        ]
      },
      {
        "sector": 86,
        "event_kind": "candidate",
        "observed_btjd": 3653.7668451745485,
        "conjunctions": [
          {
            "kind": 0,
            "cycle": 93,
            "predicted_btjd": 3658.812236546777,
            "offset_d": -5.045391372228551,
            "phase_offset": -0.14516852803782548,
            "linear_covariance_sigma_d": 1.1172384016954175
          },
          {
            "kind": 1,
            "cycle": 93,
            "predicted_btjd": 3638.7652152530377,
            "offset_d": 15.001629921510812,
            "phase_offset": 0.43163441113033113,
            "linear_covariance_sigma_d": 1.2477217205021434
          }
        ]
      }
    ],
    "note": "Fixed-cycle local linear covariance; SB1 lower triangle P,gamma,K,e,omega,Tp; subindices0,3,4,5. Edge-on conjunction assumptions; no inclination measurement or full nonlinear posterior. This tests source-specific orbital consistency, not solely period matching."
  }
}
```
