# Independent helper audit T091-T100

The batch queue was checked against queue-seal.json. The helper fetched one 9x9 TESSCut per target, recorded URL, archive and FITS SHA256 in each helper receipt, and produced difference images and a background-corrected 3x3 aperture extraction with helper_pixels.py. Sky pixels are positive, finite median pixels farther than three pixels from the target; zero detector edges do not enter the sky estimate. A positive target pixel and 51-54 usable sky pixels occur in every selected cutout. Quality-zero cadences only. This extraction uses the same TESS photons as QLP; it is an independent reduction, not a new observing occasion. Difference peak alone is not a calibrated localization.

|ID|Sector|3x3 depth ppt|Peak distance from WCS target, pixels|Source context|
|--|--:|--:|--:|--|
|T091|52|53.3|0.15|No Gaia neighbor with total G flux ratio exceeding measured aperture depth within 120 arcsec|
|T092|81|104.7|0.23|capable neighbors at 35.8 arcsec|
|T093|37|82.2|0.50|capable neighbors at 113.9 arcsec|
|T094|43|46.7|0.52|No Gaia neighbor with total G flux ratio exceeding measured aperture depth within 120 arcsec|
|T095|22|86.3|0.46|No Gaia neighbor with total G flux ratio exceeding measured aperture depth within 120 arcsec|
|T096|43|32.2|0.41|No Gaia neighbor with total G flux ratio exceeding measured aperture depth within 120 arcsec|
|T097|35|229.9|0.45|capable neighbors at 101.5 arcsec, 111.1 arcsec|
|T098|18|29.9|0.25|No Gaia neighbor with total G flux ratio exceeding measured aperture depth within 120 arcsec|
|T099|59|109.4|0.34|capable neighbors at 90.8 arcsec|
|T100|34|30.0|0.39|capable neighbors at 71.6 arcsec, 109.6 arcsec, 115.9 arcsec|

T092: the brighter G=10.731 neighbor at 35.81 arcsec lies at (4.633, 6.526), target at (4.826, 4.844), while positive residual moment is (4.808, 4.887), 0.047 pixel from target and 1.65 pixel from neighbor. T100: target (4.340, 4.201), residual moment (4.430, 4.400), nearest capable neighbor (7.515, 5.827). These moments are descriptive and not PRF fits; see helper-moments.json. G-band flux ratios are approximate, not exact TESS-band eclipse limits.

helper-geometry.json gives nominal conjunction checks using Gaia orbit with no uncertainty propagation; it is a screening comparison, not a constraint or a period measurement. T100's 0.679-d recurrence is far from the 58.827-d Gaia period and its frequent events can coincide accidentally with conjunction. Alias and classification decisions belong to the lead. Source hashes and numeric core/side coverage are in helper-pixel-audit.json; independent TESScut is same-photon evidence.

