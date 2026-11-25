"""Measure a moving point in a TESS cutout and identify bodies from the spacecraft's position."""

import argparse

import csv

from concurrent.futures import ThreadPoolExecutor

import hashlib

import tempfile

import io

import json

from pathlib import Path

import re
import time



import astropy.units as u

from astropy.coordinates import SkyCoord

from astropy.io import fits

from astropy.time import Time

from astropy.wcs import WCS

import matplotlib.pyplot as plt

import numpy as np

import requests

from scipy.optimize import least_squares



from frames import HERE, rows, save





def service(url, params, receipt=None):

    urlfile = receipt.with_suffix(receipt.suffix + ".url.txt") if receipt else None

    if receipt and receipt.exists():

        return json.loads(receipt.read_bytes())

    response = requests.get(url, params=params, timeout=120)

    response.raise_for_status()

    if receipt:

        receipt.write_bytes(response.content)

        urlfile.write_text(response.url+"\n", encoding="utf-8")

    return response.json()





def positions(path, epoch):

    with fits.open(path) as h:

        d = h[1].data

        t, cube, quality = d["TIME"], d["FLUX"], d["QUALITY"]

        dt = t - epoch

        # When the entire event is flagged, retain the same flag for the diagnostic

        # movie and record it for every exposure. Thresholds below test actual motion.

        event_quality = int(quality[np.nanargmin(abs(dt))])

        usable = np.isfinite(dt) & np.isin(quality, [0, event_quality])

        reference = np.nanmedian(cube[usable & (abs(dt) > .25) & (abs(dt) < .7)], axis=0)

        wcs = WCS(h[2].header)

        yy, xx = np.indices(reference.shape)

        result, images = [], []

        for j in np.flatnonzero(usable & (abs(dt) < .135)):

            im = cube[j] - reference

            if not np.any(np.isfinite(im)):

                continue

            y, x = np.unravel_index(np.nanargmax(im), im.shape)

            if min(x, y, im.shape[0]-y-1, im.shape[1]-x-1) < 1:

                continue

            use = np.isfinite(im) & (np.hypot(xx-x, yy-y) < 3.5)

            def resid(p):

                amp, cx, cy, sigma, floor = p

                return (amp*np.exp(-((xx-cx)**2+(yy-cy)**2)/(2*sigma**2)) + floor - im)[use]

            fit = least_squares(resid, [max(1, im[y,x]), x, y, .8, 0],

                                bounds=([0,x-1.5,y-1.5,.3,-np.inf],[np.inf,x+1.5,y+1.5,2.5,np.inf]))

            amp, cx, cy, sigma, floor = fit.x

            mad = np.nanmedian(abs(im-np.nanmedian(im)))

            if amp < max(1, 6*mad):

                continue

            ra, dec = wcs.pixel_to_world_values(cx, cy)

            tm = Time(t[j]-d["TIMECORR"][j]+h[1].header["BJDREFI"]+h[1].header["BJDREFF"],

                      format="jd",scale="tdb").utc

            result.append(dict(utc=tm.isot,jd_utc=tm.jd,btjd=t[j],x=cx,y=cy,ra=float(ra),dec=float(dec),

                               width_px=sigma,amplitude=amp,quality=quality[j],ffi=d["FFI_FILE"][j]))

            images.append(im)

    return result,images





def identify(row, prefix):

    t = Time(row["jd_utc"],format="jd",scale="utc")

    query = dict(COMMAND="'-95'", CENTER="'500@399'", EPHEM_TYPE="VECTORS", TLIST=f"'{t.tdb.jd:.9f}'",

                 REF_PLANE="FRAME", OUT_UNITS="KM-S", CSV_FORMAT="YES", VEC_TABLE="2",format="json")

    vector = service("https://ssd.jpl.nasa.gov/api/horizons.api",query,

                     HERE/f"{prefix}-spacecraft-response.json")["result"]

    (HERE/(prefix+"-spacecraft.txt")).write_text(vector,encoding="utf8")

    data = next(csv.reader([vector.split("$$SOE")[1].split("$$EOE")[0].strip()]))

    state = ",".join(str(float(k)) for k in data[2:8])

    sky=SkyCoord(row["ra"],row["dec"],unit="deg")

    params = {"xobs":state,"obs-time":t.isot[:19],"fov-ra-center":sky.ra.to_string(unit=u.hour,sep="-",precision=3,pad=True),

              "fov-dec-center":sky.dec.to_string(unit=u.deg,sep="-",precision=2,pad=True,alwayssign=True),

              "fov-ra-hwidth":.12,"fov-dec-hwidth":.12,"two-pass":"true","suppress-first-pass":"true",

              "req-elem":"false","vmag-lim":21,"mag-required":"true"}

    data = service("https://ssd-api.jpl.nasa.gov/sb_ident.api",params,

                   HERE/f"{prefix}-objects-response.json")

    (HERE/(prefix+"-objects.json")).write_text(json.dumps(dict(params=params,response=data),indent=1),encoding="utf8")

    return data





def compare(rec, obj, prefix):

    # Horizons accepts a maximum of 50 values in this URL; evenly sample the

    # measured series for the orbit comparison while retaining every measured position.

    subset=[dict(rec[i]) for i in np.unique(np.linspace(0,len(rec)-1,min(35,len(rec))).round().astype(int))]

    command = obj if obj.isdigit() else f"DES={obj}"

    slug = re.sub(r"[^A-Za-z0-9]+","-",obj)

    params=dict(format="json",COMMAND="'"+command+";'",CENTER="'500@-95'",EPHEM_TYPE="OBSERVER",QUANTITIES="'1,3,9'",

                CSV_FORMAT="YES",ANG_FORMAT="DEG",EXTRA_PREC="YES",CAL_FORMAT="BOTH",TIME_TYPE="UT",

                TLIST="'"+",".join(f"{r['jd_utc']:.8f}" for r in subset)+"'")

    raw=service("https://ssd.jpl.nasa.gov/api/horizons.api",params,

                HERE/f"{prefix}-horizons-{slug}-response.json")["result"]

    assert "$$SOE" in raw and "TESS" in raw

    (HERE/(prefix+"-horizons-"+slug+".txt")).write_bytes(raw.encode("utf-8"))

    header=next(l for l in raw.splitlines() if "Date__(UT)" in l and "R.A." in l).split(",")

    ri=next(i for i,v in enumerate(header) if v.strip().startswith("R.A."))

    di=next(i for i,v in enumerate(header) if v.strip().startswith("DEC"))

    eph=list(csv.reader(io.StringIO(raw.split("$$SOE")[1].split("$$EOE")[0].strip())))

    for r in subset:

        v=min(eph,key=lambda v:abs(float(v[1])-r["jd_utc"]))

        assert abs(float(v[1])-r["jd_utc"])<1e-6

        a,b=float(v[ri]),float(v[di])

        r.update(orbit=obj,pred_ra=a,pred_dec=b,residual_arcsec=SkyCoord(a,b,unit="deg").separation(SkyCoord(r["ra"],r["dec"],unit="deg")).arcsec)



    return subset



def motion_fit(rec):
    t=np.array([r["jd_utc"] for r in rec])
    t-=np.mean(t)
    xy=np.array([[r["x"],r["y"]] for r in rec])
    pred=np.column_stack([np.polyval(np.polyfit(t,coordinate,1),t) for coordinate in xy.T])
    return np.linalg.norm(pred[-1]-pred[0]), np.sqrt(np.mean(np.sum((xy-pred)**2,axis=1)))


def designation(name):
    match=re.match(r"(\d+)\b",name)
    return match.group(1) if match else name.strip("()")


def fetch_event(cache,row):
    tic,sector=row["tic"],row["sector"]
    prefix=f"motion-{tic}-s{sector}"
    epoch=float(row["epoch_btjd"])
    rec,ims=positions(cache/f"{tic}-{sector}.fits",epoch)
    if len(rec)<3:
        raise ValueError(f"{prefix} had fewer than 3 usable positions")
    save(HERE/f"{prefix}.csv",rec)
    center=min(rec,key=lambda r:abs(r["btjd"]-epoch))
    sb=identify(center,prefix)
    span,rms=motion_fit(rec)
    return row,prefix,rec,ims,sb,span,rms


def draw_montage(accepted):
    fig,axes=plt.subplots(len(accepted),7,figsize=(14,2.02*len(accepted)),squeeze=False,
                          gridspec_kw={"width_ratios":[1.9,1,1,1,1,1,1]},layout="constrained")
    fig.patch.set_facecolor("#101827")
    fig.suptitle("Five asteroid crossings in TESS difference images",fontsize=19,color="white")
    for (summary,rec,ims),axs in zip(accepted,axes):
        label=axs[0]
        label.axis("off")
        label.text(.02,.85,summary["body"],color="#f7bf7f",fontsize=11,fontweight="bold")
        label.text(.02,.66,f"TIC {summary['tic']}  |  Sector {summary['sector']}",
                   color="white",fontsize=9.5)
        date = rec[0]["utc"][:10]
        if date != rec[-1]["utc"][:10]:
            date += "/" + rec[-1]["utc"][8:10]
        label.text(.02,.47,date+" UTC",color="#cbd5e1",fontsize=9)
        label.text(.02,.30,f"{rec[0]['utc'][11:16]}–{rec[-1]['utc'][11:16]}  |  quality {summary['quality']}",
                   color="#cbd5e1",fontsize=9)
        label.text(.02,.13,f"{summary['median_residual_arcsec']:.1f} arcsec median residual",
                   color="#cbd5e1",fontsize=8)
        limit=max(1,np.nanpercentile([np.nanmax(im) for im in ims],90))
        for i,ax in zip(np.linspace(0,len(rec)-1,6).round().astype(int),axs[1:]):
            ax.imshow(ims[i],origin="lower",cmap="inferno",vmin=0,vmax=limit)
            ax.scatter(rec[i]["x"],rec[i]["y"],c="none",edgecolors="#8be9fd",s=90,lw=.8)
            ax.set(xticks=[],yticks=[],title=rec[i]["utc"][11:16]+" UTC")
            ax.title.set(color="#e2e8f0",fontsize=8)
            for spine in ax.spines.values():
                spine.set_color("#334155")
    fig.savefig(HERE/"pulse-sequences.jpg",dpi=140,facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_movie(accepted):
    from PIL import Image, ImageDraw, ImageFont
    from matplotlib.font_manager import findfont

    panels=[record for record in accepted if record[0]["tic"]=="186817099"]
    if len(panels)!=2:
        return
    font=lambda n:ImageFont.truetype(findfont("DejaVu Sans"),n)
    cmap=plt.get_cmap("inferno")
    frames=[]
    indices=[np.linspace(0,len(rec)-1,30).round().astype(int) for _,rec,_ in panels]
    limits=[max(1,np.nanpercentile([np.nanmax(im) for im in ims],90)) for _,_,ims in panels]
    for a in range(30):
        frame=Image.new("RGB",(602,356),"#101827")
        draw=ImageDraw.Draw(frame)
        draw.text((16,12),"Two asteroid crossings of the TIC 186817099 aperture",fill="white",font=font(19))
        for j,(summary,rec,ims) in enumerate(panels):
            i=indices[j][a]
            xy=rec[i]
            x0=20+300*j
            y0=79
            size=250
            m=ims[i][::-1]
            rgb=(cmap(np.clip(m/limits[j],0,1))[...,:3]*255).astype(np.uint8)
            im=Image.fromarray(rgb).resize((size,size),Image.Resampling.NEAREST)
            frame.paste(im,(x0,y0))
            scale=size/m.shape[0]
            x=x0+(xy["x"]+.5)*scale
            y=y0+(m.shape[0]-xy["y"]-.5)*scale
            draw.ellipse((x-17,y-17,x+17,y+17),outline="#8be9fd",width=2)
            draw.text((x0,46),summary["body"],fill="#f7bf7f",font=font(16))
            draw.text((x0,334),xy["utc"][:16].replace("T"," ")+" UTC",fill="#cbd5e1",font=font(13))
        frames.append(frame)
    frames[0].save(HERE/"motion-186817099-pair.gif",save_all=True,append_images=frames[1:],
                   duration=[125]*29+[700],loop=0,optimize=True)


def main(cache):
    events=[r for r in rows(HERE/"clocks.csv") if r["kind"]=="brightening"]
    with ThreadPoolExecutor(5) as pool:
        extracted=list(pool.map(lambda row: fetch_event(cache,row),events))
    candidates=[]
    fetched=[]
    with ThreadPoolExecutor(1) as pool:
        for row,prefix,rec,ims,sb,span,rms in extracted:
            for body in sb.get("data_second_pass",[]):
                obj=designation(body[0])
                fetched.append((prefix,body,obj,pool.submit(compare,rec,obj,prefix)))
        for prefix,body,obj,future in fetched:
            try:
                track=future.result()
            except (ValueError,KeyError,AssertionError,StopIteration,requests.RequestException) as exc:
                candidates.append(dict(event=prefix,body=body[0],designation=obj,status="comparison_failed",
                                       error=f"{type(exc).__name__}: {exc}"))
                continue
            resid=np.array([r["residual_arcsec"] for r in track])
            slug=re.sub(r"[^A-Za-z0-9]+","-",obj)
            save(HERE/f"{prefix}-track-{slug}.csv",track)
            candidates.append(dict(event=prefix,body=body[0],designation=obj,status="compared",
                                   samples=len(resid),median_residual_arcsec=np.median(resid),
                                   min_residual_arcsec=np.min(resid),max_residual_arcsec=np.max(resid),
                                   apparent_vmag=body[6],track=track))
    accepted,summary_rows=[],[]
    for row,prefix,rec,ims,sb,span,rms in extracted:
        matched=sorted([c for c in candidates if c["event"]==prefix and "track" in c],
                       key=lambda c:c["median_residual_arcsec"])
        good_track=span>=2 and rms<.35
        summary=dict(tic=row["tic"],sector=row["sector"],event_btjd=row["epoch_btjd"],
                     earliest_utc=rec[0]["utc"],latest_utc=rec[-1]["utc"],
                     quality=",".join(str(v) for v in sorted({r["quality"] for r in rec})),
                     measured_positions=len(rec),track_span_px=span,track_rms_px=rms)
        if not good_track:
            summary.update(disposition="no_coherent_moving_track")
        elif not matched or matched[0]["max_residual_arcsec"]>10:
            summary.update(disposition="moving_track_unidentified")
        else:
            hit=matched[0]
            hit["status"]="accepted"
            # Remove the MPC discovery alias from display while preserving it in the candidates table.
            body=hit["body"].split(" (")[0] if " (" in hit["body"] and not hit["body"].split(" (")[0].isdigit() else hit["body"]
            summary.update(disposition="identified",body=body,designation=hit["designation"],
                           orbit_samples=hit["samples"],
                           min_residual_arcsec=hit["min_residual_arcsec"],
                           median_residual_arcsec=hit["median_residual_arcsec"],
                           max_residual_arcsec=hit["max_residual_arcsec"],
                           track_table=f"{prefix}-track-{re.sub(r'[^A-Za-z0-9]+','-',hit['designation'])}.csv")
            accepted.append((summary,rec,ims))
        summary_rows.append(summary)
        print(summary,flush=True)
    save(HERE/"motion-orbits.csv",summary_rows)
    save(HERE/"motion-candidate-comparisons.csv",[{k:v for k,v in row.items() if k!="track"} for row in candidates])
    receipts=sorted(HERE.glob("motion-*-response.json"))
    save(HERE/"motion-receipts.csv",[dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                                           request_url=p.with_suffix(p.suffix+".url.txt").read_text().strip())
                                     for p in receipts])
    if accepted:
        draw_montage(accepted)
        draw_movie(accepted)


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cache",type=Path)
    main(ap.parse_args().cache)

