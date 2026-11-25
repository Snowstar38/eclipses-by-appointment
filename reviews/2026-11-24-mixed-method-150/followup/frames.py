"""Locate changes of light in 15-pixel TESS cutouts with independently fitted Gaia astrometry."""
import argparse
import csv
import hashlib
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from astropy.io import fits
from astropy.wcs import WCS
import matplotlib.pyplot as plt
import numpy as np
import requests

from scene import HERE, fit_scene, gaia_field, locate


def rows(f):
    with f.open(encoding='utf-8-sig',newline='') as s:return list(csv.DictReader(s))


def save(f,rs):
    with f.open('w',encoding='utf8',newline='') as s:
        w=csv.DictWriter(s,dict.fromkeys(k for r in rs for k in r),lineterminator='\n')
        w.writeheader()
        w.writerows(rs)


def retrieve(job):
    path,url,fmt=job
    if not path.exists():
        resp=requests.get(url,timeout=120)
        resp.raise_for_status()
        if fmt=='ZIP':
            with ZipFile(BytesIO(resp.content)) as archive:
                name,=[n for n in archive.namelist() if n.endswith('.fits')]
                data=archive.read(name)
            assert data.startswith(b'SIMPLE')
        else:
            data=resp.content
            assert data.startswith(b'source_id,')
        path.write_bytes(data)
    return dict(file=path.name,url=url,sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def jobs(stars,measurements,cache):
    output={}
    for row in measurements:
        tic,sector=row['tic'],row['sector']
        star=stars[tic]
        ra,dec=star['ra_deg'],star['dec_deg']
        url=requests.Request('GET','https://mast.stsci.edu/tesscut/api/v0.1/astrocut',
                             params=dict(ra=ra,dec=dec,sector=sector,x=15,y=15)).prepare().url
        path=cache/f'{tic}-{sector}.fits'
        output[path]=(path,url,'ZIP')
        q=("SELECT source_id,ra,dec,pmra,pmdec,ref_epoch,phot_g_mean_mag AS g,"
           "phot_rp_mean_mag AS rp FROM gaiadr3.gaia_source WHERE 1=CONTAINS("
           f"POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.066)) AND phot_g_mean_mag<20.5")
        url=requests.Request('GET','https://gea.esac.esa.int/tap-server/tap/sync',
                             params=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q,MAXREC=30000)).prepare().url
        path=HERE/f'gaia-{tic}.csv'
        output[path]=(path,url,'CSV')
    return list(output.values())


def measure(row,star,path):
    p,e,w=[float(row[k]) for k in ('period_d','epoch_btjd','width_d')]
    with fits.open(path) as h:
        assert h[0].header['SECTOR']==int(row['sector'])
        d=h[1].data
        t=d['TIME']
        good=(d['QUALITY']==0)&np.isfinite(t)
        cube=d['FLUX']
        dt=np.median(np.diff(t[good]))
        wcs=WCS(h[2].header)
        centers=[e] if not p else e+p*np.arange(np.ceil((min(t[good])-e)/p),np.floor((max(t[good])-e)/p)+1)
        frames=[]
        for c in centers:
            u=(t-c)/w
            masks=[good&(u>=-2)&(u<=-1),good&(abs(u)<.35),good&(u>=1)&(u<=2)]
            if any(m.sum()<max(2,.60*w*k/dt) for m,k in zip(masks,[1,.7,1])):continue
            l,i,r=[np.nanmedian(cube[m],axis=0) for m in masks]
            frames.append([(l+r)/2,l-i,r-i])
    if not frames:raise ValueError('No event with both shoulders and adequate core coverage')
    base,l,r=np.nanmedian(frames,axis=0)
    sign=1 if row['kind']=='dip' else -1
    l,r=l*sign,r*sign
    diff=(l+r)/2
    x,y,rel,ids,i=gaia_field(dict(**star,btjd=np.median(t[good])),wcs,diff.shape)
    sigma,dx,dy=fit_scene(base,x,y,rel)
    x,y=x+dx,y+dy
    cx,cy=locate(diff,sigma)
    scale=3600*np.sqrt(abs(np.linalg.det(wcs.pixel_scale_matrix)))
    dist=np.hypot(x-cx,y-cy)*scale
    other=np.flatnonzero((np.arange(len(ids))!=i)&(rel>.001)&(np.hypot(x-x[i],y-y[i])*scale<125))
    near=min(other,key=lambda j:dist[j]) if len(other) else None
    split=np.linalg.norm(locate(l,sigma)-locate(r,sigma))*scale
    yy,xx=np.indices(diff.shape)
    radius=np.hypot(xx-x[i],yy-y[i])
    ap=radius<1.65
    sky=(radius>3.5)&(radius<6)
    def apflux(im):return np.nansum(im[ap]-np.nanmedian(im[sky]))
    depth=1000*apflux(diff)/apflux(base)
    result=dict(**row,events=len(frames),target_offset_as=round(dist[i],3),
                closest_other_id=ids[near] if near is not None else '',
                closest_other_as=round(dist[near],3) if near is not None else '',
                flank_change_as=round(split,3),dx=round(dx,4),dy=round(dy,4),
                field_subtracted_target_change_ppt=round(depth,4))
    return result,(diff,(x[i],y[i]),(cx,cy),x[other],y[other])


def main(cache):
    measurements=rows(HERE/'clocks.csv')
    stars={r['tic']:r for r in rows(HERE.parent/'roster.csv')}
    cache.mkdir(parents=True,exist_ok=True)
    inputs=[]
    with ThreadPoolExecutor(5) as pool:
        tasks=[(j,pool.submit(retrieve,j)) for j in jobs(stars,measurements,cache)]
        for (path,url,_),f in tasks:
            try:inputs.append(f.result())
            except Exception as ex:inputs.append(dict(file=path.name,url=url,error=str(ex)))
    save(HERE/'inputs.csv',inputs)
    results=[]
    for tic in dict.fromkeys(r['tic'] for r in measurements):
        plots=[]
        for row in (r for r in measurements if r['tic']==tic):
            try:
                result,plot=measure(row,stars[tic],cache/f"{tic}-{row['sector']}.fits")
                plots.append((result,plot))
                results.append(result)
            except (ValueError,OSError) as ex:results.append(dict(**row,error=str(ex).split(':')[-1]))
        if not plots:continue
        cols=min(4,len(plots))
        nrows=(len(plots)+cols-1)//cols
        fig,axes=plt.subplots(nrows,cols,squeeze=False,figsize=(max(6,3.0*cols),3.2*nrows+.4),layout='constrained')
        for ax in axes.flat[len(plots):]:ax.set_visible(False)
        for ax,(rec,(im,target,center,x,y)) in zip(axes.flat,plots):
            lim=max(.001,np.nanpercentile(abs(im),99.5))
            ax.imshow(im,cmap='coolwarm',origin='lower',vmin=-lim,vmax=lim)
            ax.scatter(x,y,s=9,c='gray',marker='.')
            ax.scatter(*target,facecolors='none',edgecolors='yellow',s=100)
            ax.scatter(*center,c='black',marker='+',s=70)
            ax.set(xlim=(-.5,14.5),ylim=(-.5,14.5),xticks=[],yticks=[],
                   title=f"S{rec['sector']}   {rec['label']}   ({rec['events']})",
                   xlabel=f"{rec['target_offset_as']:.1f} arcsec from target")
        fig.suptitle(f"TIC {tic}   |   light change at predicted times\nTarget: yellow circle   /   fitted change: cross")
        fig.savefig(HERE/f'{tic}.png',dpi=140)
        plt.close(fig)
    save(HERE/'measurements.csv',results)
    print('Measurements:',len(results),'with measurements:',sum('events' in r for r in results))


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('cache',type=Path)
    main(ap.parse_args().cache)
