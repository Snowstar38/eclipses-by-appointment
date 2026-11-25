# TESS difference-image localization

Six event-centered TESS-SPOC target-pixel fits favor the Gaia DR3 counterparts of their nominal TICs. Each fit uses one eclipse and its local baseline in a single sector.

| TIC | Sectors | Favored Gaia DR3 source | Source discrimination |
| --- | --- | --- | --- |
| 160193535 | 19, 60 | 1727862804856539264 | No catalogued alternative passed the model brightness screen in either sector. |
| 321912132 | 24, 78 | 2224073158388302976 | The alternatives 2224072574272754560 and 2224072986589617152 lie 59.3 and 68.0 arcsec from the nominal TIC position. Their fitted amplitudes have the opposite sign of an eclipse in both sectors. |
| 441584021 | 26, 47 | 1111840936992323456 | The two imaged deep dips favor the nominal counterpart over 1111840936992323328, 16.0 arcsec from the nominal position. Gaia DR3 1111840936990256384 is 6.7 arcsec away and fainter by 7.23 mag in G and 6.87 mag in RP, contributing under 0.2% of nominal source flux in either proxy. The shallow phase was outside this check. |

The fits use calibrated TESS-SPOC target-pixel data at quality zero with finite pixel cadences. The synthetic 1000 d period isolates each measured BTJD center. The full in-eclipse fit window equals the independently selected core width in the pilot's dips.csv. The difference image subtracts the average in-eclipse pixels from the average of bracketing out-of-eclipse pixels. Individual JSON files contain the TESS archive FITS URLs and SHA-256 hashes, the Gaia scene hashes, the event table hash, and the Gaussian position-fit diagnostics. The Gaia DR3 scene query used G < 20.5 within 230.4 arcsec of each aperture coordinate.

The model registers Gaia sources to an out-of-eclipse image using a Gaussian approximation to the TESS pixel response and compares candidate positions with a free difference-image position. The sub-arcsecond model residuals are internal offsets. The single-event model weights use a spatial MAD and do not support calibrated astrometric confidence intervals or formal significance from differences in chi-square. The brightness screen uses Gaia G as an estimate and the target stamp has finite coverage. Close or uncatalogued blends remain possible. These measurements constrain the position of the imaged flux loss without resolving the orbital clocks.
