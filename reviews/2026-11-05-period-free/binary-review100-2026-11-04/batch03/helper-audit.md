Independent helper audit

H021 TIC 299187993: Raw sector 38 is a complete flat-bottomed dip; sector 65 catches ingress before a long data gap, an additional observing occasion but not a precision center. Sector 100 shows an irregular dip on a changing baseline and requires caution. TESSCut sector 38 five-pixel-square extraction gives ~12.6 ppt, but difference-light centroid is 0.63 pixel from target toward Gaia DR3 5865636874832071424 (G 11.09; 35.7 arcsec), whose flux is capable of producing the signal. The event cannot confidently be attributed to the target by this inspection.

H022 TIC 294257329: sector 36 TESSCut aperture independently recovers a ~139.5 ppt event; difference centroid 0.04 pixel from target. No Gaia source within 60 arcsec has enough G-band flux alone under the approximate full-inclusion bound.

H023 TIC 224631871: sector 55 aperture recovers ~16.7 ppt; difference centroid 0.07 pixel from target. Capable Gaia neighbors are 13.5 and 19.4 arcsec away (G 14.38 and 13.92); centroid favors target but the proximity limits attribution.

H027 TIC 113645244: sector 67 aperture recovers ~10.3 ppt; difference centroid 0.16 pixel from target; two capable neighbors are 40 and 43 arcsec away. Triangular raw SAP fits yield centers 1676.36097, 2053.87179, 3144.45939, 3857.53608 BTJD. Integer cycles 0,9,35,52 give 41.94565 d; tested nearby aliases of 5-14 cycles disagree by days except 9. Gaia period 41.96173 +/- 0.02910 d is consistent marginally; covariance-aware orbital phase remains separate.

Source differences and apertures share photons with SAP, so they are independent reductions, not independent occasions. Difference centroids are simple positive-pixel moments, affected by crowding and noise; G-band flux bounds are approximate and assume full inclusion. More details, per-source WCS coordinates, source hashes and scripts are in helper-source-attribution.json, helper-timing.json and helper-pixels receipts.
