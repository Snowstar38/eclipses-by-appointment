"""Download a TESScut FFI cutout. python -X utf8 tesscut.py <ra> <dec> <sector> <outdir> [size]
Downloaded files are data only (never executed)."""
import io, os, sys, urllib.request, zipfile
ra, de, sec, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
size = int(sys.argv[5]) if len(sys.argv) > 5 else 15
os.makedirs(out, exist_ok=True)
dst = os.path.join(out, f'tesscut_s{sec:03d}.fits')
if os.path.exists(dst): print('have', dst); sys.exit()
u = f'http[local path omitted]'
b = urllib.request.urlopen(u, timeout=900).read()
z = zipfile.ZipFile(io.BytesIO(b))
names = [n for n in z.namelist() if n.endswith('.fits')]
print(names)
if len(names) != 1: print('WARNING: several cutouts (cameras/CCDs); keeping the first')
open(dst, 'wb').write(z.read(names[0])); print('wrote', dst, os.path.getsize(dst))
