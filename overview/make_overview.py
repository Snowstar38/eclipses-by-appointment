"""Reproduce the overview: final paper first page, full included sky sample, real A98 light curve."""
import csv, json, re, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "DejaVu Sans"
from PIL import Image
from astropy.coordinates import SkyCoord
import astropy.units as u

import argparse, hashlib, io
from pathlib import Path
import pymupdf

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--paper', type=Path, default=Path('paper.pdf'))
parser.add_argument('--data', type=Path, default=Path('overview/systems.csv'))
parser.add_argument('--inset', type=Path, default=Path('overview/a98.json'))
parser.add_argument('--sky', type=Path, default=Path('overview/milkyway_2020_4k_print.jpg'))
parser.add_argument('--output', type=Path, default=Path('overview.png'))
args = parser.parse_args()
rows = list(csv.DictReader(args.data.open(encoding='utf-8')))
assert rows and len({r['review_id'] for r in rows}) == len(rows)
assert len({r['tic'] for r in rows if r['tic']}) == len(rows)
assert all(r['tier'] in ('confirmed', 'probable') for r in rows)
ra = np.array([float(r['ra_deg']) for r in rows])
dec = np.array([float(r['dec_deg']) for r in rows])
assert np.all(np.isfinite(ra)) and np.all((0 <= ra) & (ra < 360))
assert np.all(np.isfinite(dec)) and np.all(abs(dec) <= 90)
with pymupdf.open(args.paper) as pdf:
    page0 = pdf[0]
    headline = re.search(r"Eclipses by Appointment:\s*(\d+)\s+Eclipsing Systems", page0.get_text())
    assert headline, "Paper first-page system-count headline not found"
    assert int(headline.group(1)) == len(rows), "Paper headline and map sample count disagree"
    # Original image was rendered to a width of 1785 pixels before cropping.
    pix = page0.get_pixmap(matrix=pymupdf.Matrix(1785/page0.rect.width, 1785/page0.rect.width), alpha=False)
    paper_image = Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')

BG, GOLD, INK, DIM = "#0b1020", "#ffcf5c", "#eef2ff", "#9aa6c8"
fig = plt.figure(figsize=(20, 10.5), dpi=120, facecolor=BG)

# left: top of page 1, down to the end of the abstract
page = paper_image.crop((0, 90, 1785, 1870))
axp = fig.add_axes([0.02, 0.04, 0.40, 0.92]); axp.imshow(page); axp.axis("off")

def x_of(r): return -np.radians(((r + 180) % 360) - 180)   # RA increasing to the left, 0h at centre

ax = fig.add_axes([0.45, 0.20, 0.53, 0.62], projection="mollweide", facecolor="#141b33")
ax.grid(True, color="#2a3560", lw=0.6); ax.set_xticklabels([]); ax.set_yticklabels([])
for s in ax.spines.values(): s.set_edgecolor("#3a4778")
assert hashlib.sha256(args.sky.read_bytes()).hexdigest() == "1ebe95804f5f0e6e23f77488aaa33fdb4aaef3fd336821fb41b261ddeaee2df0", "Sky asset hash mismatch"
# NASA SVS 4851: ICRF/J2000 plate carree, RA=0 at centre,
# RA increases leftward, north at top. Thus image x matches our -RA longitude.
# Project every image cell through the same Mollweide transform as the targets.
# Source RGB is blended into the original navy background for readable points.
sky = np.asarray(Image.open(args.sky).convert("RGB"), dtype=float) / 255.0
h, w = sky.shape[:2]
lon_edges = np.linspace(-np.pi, np.pi, w + 1)
lat_edges = np.linspace(-np.pi/2, np.pi/2, h + 1)
navy = np.array([20, 27, 51]) / 255.0
rgb = 0.57 * sky[::-1] + 0.43 * navy
ax.pcolormesh(lon_edges, lat_edges, rgb, shading="flat", antialiased=False,
              rasterized=True, zorder=0)
ax.set_axisbelow(False)
fig.text(0.98, 0.224, "Sky: NASA/Goddard SVS; Gaia DR2: ESA/Gaia/DPAC", color=DIM,
         fontsize=7.5, ha="right")
x, y = x_of(ra), np.radians(dec)
ax.scatter(x, y, s=170, color=GOLD, alpha=0.18, lw=0, clip_on=False)
ax.scatter(x, y, s=34, color=GOLD, edgecolor="white", lw=0.5, zorder=3, clip_on=False)

fig.text(0.715, 0.915, f"{len(rows)} eclipsing systems across the sky", color=INK, fontsize=30, ha="center", weight="bold")
fig.text(0.715, 0.865, "confirmed and probable systems identified in public NASA TESS data", color=DIM, fontsize=17, ha="center")
fig.text(0.715, 0.835, "the whole sky, both hemispheres  \u00b7  each dot is one system", color=DIM, fontsize=13, ha="center")

# inset: the real dip of one of them
D = json.loads(args.inset.read_text(encoding="utf-8")); c, f = np.array(D["c"]), np.array(D["f"])
ai = fig.add_axes([0.53, 0.035, 0.37, 0.15], facecolor="#141b33")
ai.plot(np.r_[c, c + 1], np.r_[f, f], color=GOLD, lw=2)
ai.set_xlim(-0.25, 1.25); ai.set_xticks([]); ai.set_yticks([])
for s in ai.spines.values(): s.set_edgecolor("#3a4778")
i0 = np.argmin(f); ai.annotate("one star passes in front:\nlight drops by a quarter", (c[i0], f[i0]), (c[i0] + 0.12, f[i0] + 0.05),
                              color=INK, fontsize=11, va="center", arrowprops=dict(arrowstyle="-", color=DIM))
k = np.argmin(np.where(np.abs(c - 0.5) < 0.2, f, 9)); ai.annotate("the other passes behind:\nlight drops by a fifth", (c[k], f[k]), (c[k] + 0.05, f[k] + 0.02),
                              color=INK, fontsize=11, va="center", arrowprops=dict(arrowstyle="-", color=DIM))
fig.text(0.53, 0.195, "One of them, BD+45 2574 A: its archived TESS brightness over one 3.5-day orbit",
         color=DIM, fontsize=11.5)
fig.savefig(args.output, facecolor=BG, metadata={"Software": "Matplotlib"})
print(json.dumps({"systems": len(rows), "tiers": {t: sum(r["tier"] == t for r in rows) for t in ("confirmed", "probable")}, "sky_sha256": hashlib.sha256(args.sky.read_bytes()).hexdigest(), "paper_sha256": hashlib.sha256(args.paper.read_bytes()).hexdigest(), "data_sha256": hashlib.sha256(args.data.read_bytes()).hexdigest(), "inset_sha256": hashlib.sha256(args.inset.read_bytes()).hexdigest(), "output_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest()}, indent=2))
