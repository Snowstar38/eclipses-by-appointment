# T100 - TIC 95244521

Physical verdict: **PROBABLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Many narrow dips recur on the target-favored pixels across sectors 7, 34, 61 and 88. The raw SAP folded at 0.67918 d shows two near-equal dip trains separated by half a cycle, including sector-7 centers only 0.3336 d apart. Folding at 0.33959 d combines those trains. The supported photometric dip interval is about 0.3396 d; the orbital period could be that value or twice it (about 0.6792 d) because the two kinds are not securely distinguishable. Either clock is far from the selecting Gaia 58.8274-d SB1 orbit, so this is a separate short-period eclipsing signal or contaminant, not evidence that the Gaia spectroscopic orbit eclipses.

Gaia selection orbit: P=58.827422 d, SB1. Measured raw eclipse centers were compared against both edge-on Gaia conjunction kinds using the source-specific NSS covariance: nearest-conjunction absolute offsets span 1.51-15.46 propagated Gaia sigma across the selected events. Per-event measured times, predicted times, kinds, cycles and uncertainties are in lead-event-geometry.json. This conditional comparison alone cannot fix an unmeasured eclipse cycle count or source relationship.

## Source and reduction

TESScut sector 34: target WCS xy=(4.34,4.20), deficit peak xy=[4, 4], offset 0.39 pixel. A 3x3 sky-corrected custom aperture measures 30.0 ppt on the same observing occasion (5 core and 129 baseline cadences). There are 52 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 7 | 1493.0207 | 17.6 | 0.083 | 0.042 |
| 7 | 1513.3999 | 17.8 | 0.101 | 0.042 |
| 7 | 1514.0852 | 23.6 | 0.101 | 0.062 |
| 7 | 1514.4188 | 18.9 | 0.101 | 0.062 |
| 34 | 2231.2842 | 24.7 | 0.080 | 0.014 |
| 34 | 2236.0406 | 27.8 | 0.081 | 0.021 |
| 34 | 2237.3993 | 28.0 | 0.083 | 0.014 |
| 34 | 2248.2674 | 29.9 | 0.095 | 0.021 |
| 61 | 2965.4781 | 27.2 | 0.077 | 0.002 |
| 61 | 2977.0231 | 27.7 | 0.092 | 0.002 |
| 61 | 2979.0604 | 25.6 | 0.078 | 0.005 |
| 61 | 2981.0976 | 27.1 | 0.077 | 0.044 |
| 88 | 3703.7416 | 27.8 | 0.077 | 0.264 |
| 88 | 3706.4598 | 26.9 | 0.077 | 0.002 |
| 88 | 3713.2529 | 27.0 | 0.077 | 0.002 |
| 88 | 3716.6494 | 30.5 | 0.088 | 0.016 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Selected same-kind timing artifact: lead-timing.json, P=0.67917807 d with explicit cycles and residuals. Its formal error is conditional on those selections. This is not an adopted orbital period.
Current Tesscut footprint query returns sectors [7, 34, 61, 88]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue novelty gates remain unknown.
Limitation: Photometric recurrence is secure, but the orbital harmonic and physical relationship to the Gaia SB1 remain unresolved. The long-cycle formal timing error is inappropriate; no orbital period or error is adopted.
Next check: Resolve the orbital harmonic and source relation with spectroscopy or higher-resolution light curves.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T100); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.

The P versus P/2 raw fold and source hashes are in lead-t100-harmonic.json and lead-t100-harmonic.png. The selected 0.679178-d timing fit in lead-timing.json is a photometric double-period representation, not an adopted orbital ephemeris.