# Exposure guard provenance

The replay includes the three rows frozen by the Sector 26 QLP exposure-control review. It joins on sector, camera, flux column, and original CADENCENO. This leaves isolated features on other cameras eligible for measurement.

The calibration used a deterministic field draw with up to 12 stars per chip. A usable exposure required quality zero, finite raw and corrected flux, and at least two valid measurements per flank. A star passed when corrected flux dropped more than 5% while raw aperture flux changed less than 1%. The camera flag required at least 12 measured stars, at least two chips with three measured stars each, and a passing fraction of at least 80%. The two initial examples helped set the thresholds. The subsequent camera scan found the third exposure. The replay applies the frozen flags to KSPSAP_FLUX in Sector 26.
