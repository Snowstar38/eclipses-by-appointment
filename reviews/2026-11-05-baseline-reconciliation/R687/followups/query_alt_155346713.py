import json
import urllib.parse
import urllib.request
from pathlib import Path

here = Path(__file__).resolve().parent
tic = '155346713'
request = {'service': 'Mast.Caom.Filtered', 'format': 'json', 'pagesize': 5000, 'page': 1,
           'params': {'columns': 'target_name,sequence_number,dataURL,provenance_name',
                      'filters': [{'paramName': 'provenance_name', 'values': ['SPOC', 'TESS-SPOC', 'TARS', 'TGLC']},
                                  {'paramName': 'target_name', 'values': [tic]}]}}
body = urllib.parse.urlencode({'request': json.dumps(request)}).encode()
with urllib.request.urlopen(urllib.request.Request('https://mast.stsci.edu/api/v0/invoke', data=body), timeout=90) as response:
    raw = response.read()
(here / 'alternative-caom-155346713.json').write_bytes(raw)
data = json.loads(raw)
print(data.get('status'), len(data.get('data', [])))
print([(r['provenance_name'], r['sequence_number'], r['dataURL']) for r in data['data'] if r.get('dataURL', '').endswith('lc.fits')])
