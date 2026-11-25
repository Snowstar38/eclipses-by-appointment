"""Refine the coherent short dips and measure their predicted epochs."""
from pathlib import Path

import numpy as np
from astropy.timeseries import LombScargle
from scipy.ndimage import median_filter

from review import ROOT, load, measure, write_csv

TARGETS = [(15,"37378337",.60029646,1523.958503,.12),
           (15,"307642177",.35888635,1792.371415,.06),
           (15,"258526967",.41504440,1711.695934,.088)]


def main():
    base = Path(__file__).resolve().parents[1]
    data = ROOT/"sky/data/qlp-sb-p20-60"
    batches = {}
    for batch,tic,guess,epoch,width in TARGETS:
        chunks = []
        for path in sorted(data.glob(f"{tic}_s*.fits")):
            sector,camera,t,flux,guard = load(path,{})
            size=max(3,(int(2/np.median(np.diff(t)))//2)*2+1)
            detrended=flux[:,1]-median_filter(flux[:,1],size=size)
            chunks.append((sector,camera,t,flux,guard,detrended))
        t=np.concatenate([row[2] for row in chunks])
        flux=np.concatenate([row[5] for row in chunks])
        model=LombScargle(t-epoch,flux,nterms=4)
        freq=np.linspace(.9998/guess,1.0002/guess,4001)
        score=model.power(freq,method="fastchi2")
        i=np.argmax(score)
        period=1/freq[i]
        p=np.linspace(-.20,.20,801)
        center=epoch+period*p[np.argmin(model.model(p*period,freq[i]))]
        p=np.linspace(.35,.65,601)
        secondary=epoch+period*p[np.argmin(model.model(p*period,freq[i]))]
        comparison_name = "secondary-window"
        if tic == "37378337":
            secondary = center + period/2
            comparison_name = "half-cycle comparison"
        summary=[]
        events=[]
        for label,pivot in (("primary",center),(comparison_name,secondary)):
            for sector,camera,t,flux,guard,_ in chunks:
                lo=int(np.ceil((t.min()-pivot)/period))
                hi=int(np.floor((t.max()-pivot)/period))
                rows=[]
                for cycle in range(lo,hi+1):
                    prediction=pivot+period*cycle
                    row=dict(tic=tic,sector=sector,camera=camera,signal=label,period_d=period,
                             epoch_btjd=pivot,width_d=width,cycle=cycle,center=prediction,
                             **measure(t,flux,guard,prediction,width))
                    events.append(row)
                    rows.append(row)
                q=[r for r in rows if r["fraction"]>=.65 and min(r["left_n"],r["right_n"])>=2]
                if q:
                    summary.append(dict(tic=tic,sector=sector,signal=label,period_d=period,
                                        epoch_btjd=pivot,width_d=width,total=len(rows),covered=len(q),
                                        sap_ppt=np.median([r["sap_ppt"] for r in q]),
                                        corrected_ppt=np.median([r["corrected_ppt"] for r in q])))
        write_csv(base/f"batch{batch}"/f"{tic}-timing.csv",events)
        batches.setdefault(batch,[]).extend(summary)
    for batch,summary in batches.items():
        write_csv(base/f"batch{batch}"/"coherent-dip-coverage.csv",summary)


if __name__=="__main__":
    main()
