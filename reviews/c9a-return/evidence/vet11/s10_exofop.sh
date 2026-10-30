#!/bin/bash
# ExoFOP-TESS: TOI / CTOI mentions on each target page (HTML grep).
for t in 372683900 13106408 372683622 319185391 62328710; do
  h=$(curl -sS --max-time 90 "https://exofop.ipac.caltech.edu/tess/target.php?id=$t")
  echo "TIC $t: bytes=${#h}; TOI matches: $(echo "$h" | grep -oE 'TOI[- ]?[0-9]+(\.[0-9]+)?' | sort -u | tr '\n' ' '); CTOI matches: $(echo "$h" | grep -oiE 'CTOI[^<]{0,30}' | sort -u | head -3 | tr '\n' ' ')"
done
# The target pages are JS grids, so also grep the full TOI and CTOI tables (CSV downloads).
D=/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet11
curl -sS --max-time 180 -o $D/toi.csv "https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv"
curl -sS --max-time 180 -o $D/ctoi.csv "https://exofop.ipac.caltech.edu/tess/download_ctoi.php?sort=ctoi&output=csv"
echo "TOI table rows: $(wc -l < $D/toi.csv); CTOI table rows: $(wc -l < $D/ctoi.csv)"
for t in 231663901 372683900 13106408 372683622 319185391 62328710; do
  echo "TIC $t: TOI rows=$(grep -cE "^$t," $D/toi.csv); CTOI rows=$(grep -cE "(^|,)$t(\.|,)" $D/ctoi.csv)"
done
