"""Download TESScut 11x11 cutouts (zip) for given sectors. python -X utf8 tcut.py s1,s2,..."""
import sys, os, io, zipfile, urllib.request
O = '[local path omitted]'
for s in sys.argv[1].split(','):
    u = f'http[local path omitted]'
    try:
        b = urllib.request.urlopen(u, timeout=900).read(); z = zipfile.ZipFile(io.BytesIO(b))
        for n in z.namelist():
            open(os.path.join(O, os.path.basename(n)), 'wb').write(z.read(n)); print('got', s, n, len(z.read(n)))
    except Exception as e: print('fail', s, e)
