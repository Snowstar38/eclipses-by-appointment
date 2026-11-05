"""Step 1b: other pipelines for s9/s10 (TGLC, GSFC-ELEANOR-LITE, T16) and TESScut 21x21 cutouts for every sector.
Writes s1b_out.txt; files to %TEMP%/heartbeats/vet438089101 (tglc_s009.fits ... ; tesscut/s0009.zip etc.)."""
import os, urllib.request, zipfile
from lib import *

say = say_to(open(os.path.join(OUT, "s1b_out.txt"), "w"))
for line in open(os.path.join(OUT, "mast_inventory.txt")):
    c = line.rstrip("\n").split("\t")
    prov, s, typ, u = c[1], c[3], c[4], c[6]
    if typ != "timeseries" or prov not in ("TGLC", "GSFC-ELEANOR-LITE", "T16"): continue
    tag = {"TGLC": "tglc", "GSFC-ELEANOR-LITE": "eleanor", "T16": "t16"}[prov]
    p = os.path.join(DL, f"{tag}_s{int(s[1:]):03d}.fits")
    try:
        download(u, p); say("downloaded", tag, s)
    except Exception as ex:
        say("fail", tag, s, ex)

TC = os.path.join(DL, "tesscut"); os.makedirs(TC, exist_ok=True)
for sec in (9, 10, 35, 36, 37, 62, 63, 89, 90):
    z = os.path.join(TC, f"s{sec:04d}.zip")
    if not os.path.exists(z):
        u = (f"https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra={RA}&dec={DEC}&y=21&x=21&units=px&sector={sec}")
        try:
            urllib.request.urlretrieve(u, z + ".part"); os.replace(z + ".part", z)
        except Exception as ex:
            say("tesscut fail", sec, ex); continue
    with zipfile.ZipFile(z) as zf:
        names = zf.namelist(); zf.extractall(os.path.join(TC, f"s{sec:04d}"))
    say("tesscut", sec, names)
