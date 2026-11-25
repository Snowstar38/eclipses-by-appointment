"""Find camera-wide corrected-flux losses throughout sector 26, excluding the ten leads."""
import argparse
from pathlib import Path
import warnings

from astropy.io import fits
import numpy as np
import pandas as pd

HERE=Path(__file__).resolve().parent


def samples(row,cache):
    with fits.open(cache/row.filename) as h:
        d=h[1].data
        df=pd.DataFrame(dict(sap=d["SAP_FLUX"].astype(float),corrected=d["KSPSAP_FLUX"].astype(float)),
                        index=d["CADENCENO"].astype(int)).sort_index()
        good=pd.Series(d["QUALITY"]==0,index=d["CADENCENO"].astype(int))
        df=df.where(good & np.isfinite(df).all(axis=1)).reindex(range(df.index.min(),df.index.max()+1))
    sides=[]
    for sign in (-1,1):
        side=np.stack([df.shift(sign*i).to_numpy() for i in range(1,5)])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore",RuntimeWarning)
            median=np.nanmedian(side,axis=0)
        median[np.isfinite(side).sum(axis=0)<2]=np.nan
        sides.append(median)
    baseline=(sides[0]+sides[1])/2
    usable=(baseline>0).all(axis=1)&np.isfinite(df).all(axis=1).to_numpy()
    losses=1000*(1-df.to_numpy()[usable]/baseline[usable])
    return pd.DataFrame(dict(cadenceno=df.index[usable],camera=row.camera,ccd=row.ccd,
                             hit=(abs(losses[:,0])<10)&(losses[:,1]>50)))


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("cache",type=Path)
    args=p.parse_args()
    roster=pd.read_csv(HERE/"roster.csv")
    d=pd.concat([samples(r,args.cache) for r in roster[roster.role=="field"].itertuples()])
    chip=d.groupby(["cadenceno","camera","ccd"]).hit.agg(["count","sum"])
    chip["adequate_chips"]=(chip["count"]>=3).astype(int)
    out=chip.groupby(["cadenceno","camera"]).sum().rename(columns={"count":"measured","sum":"with_large_loss"})
    out["screen_flag"]=(out.measured>=12)&(out.adequate_chips>=2)&(out.with_large_loss>=.8*out.measured)
    out.to_csv(HERE/"exposure-scan.csv")
    flagged=out[out.screen_flag].reset_index().assign(sector=26, pipeline="QLP", flux_column="KSPSAP_FLUX")
    flagged.to_csv(HERE/"flagged-exposures.csv",index=False)
    print(out[out.screen_flag])
