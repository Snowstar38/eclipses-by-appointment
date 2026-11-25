"""Check nominated clocks in independent ground surveys without fitting a new phase."""
import argparse
import csv
import json
from pathlib import Path

from fetch import download
from sampling import HERE, assess, observations


def main(cache):
    donors=list(csv.DictReader((HERE/'donors.csv').open()))
    receipts=[download(r,cache) for r in donors]
    (HERE/'donor-ztf-receipts.json').write_text(json.dumps(receipts,indent=1)+'\n')
    tests=list(csv.DictReader((HERE/'tests.csv').open()))
    results=[]
    for tic in dict.fromkeys(r['tic'] for r in tests):
        series=list(observations(tic,cache))
        for row in (r for r in tests if r['tic']==tic):
            p,e,w=[float(row[k]) for k in ('period_d','epoch_btjd','width_d')]
            half=min(.04*p,.36*w)
            if not series:
                results.append(dict(**row,survey='no usable series'))
            for identity,t,y,err in series:
                levels=y if row['kind']=='dip' else -y
                vals=assess(t,levels,err,p,e,half)
                robust=vals['passes']
                if identity['survey']=='ASAS-SN' and robust:
                    robust=all(assess(t,levels,err,p,e+shift,half)['passes'] for shift in (-.008,.008))
                results.append(dict(**row,**identity,**vals,robust=robust))
    with (HERE/'fixed-windows.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,dict.fromkeys(k for row in results for k in row),lineterminator='\n')
        w.writeheader()
        w.writerows(results)


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('cache',type=Path)
    main(ap.parse_args().cache)
