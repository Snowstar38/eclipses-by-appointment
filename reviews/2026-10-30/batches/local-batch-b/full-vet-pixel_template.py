import zipfile,pathlib,json,numpy as np,csv
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
r=pathlib.Path(__file__).parent
for tic,sec in [('295945076',34),('372376841',10)]:
 z=zipfile.ZipFile(r/'data'/f'{tic}_s{sec}_tesscut.zip');z.extractall(r/'data');fn=r/'data'/z.namelist()[0];h=fits.open(fn); a=h[1].data;wcs=WCS(h[2].header);t=np.array(a['TIME']);q=np.array(a['QUALITY']);flux=np.array(a['FLUX'],float);m=json.loads((r/f'{tic}_measurements.json').read_text());evt=[e for e in m['events'] if e['sector']==sec and e['coverage_ok']];maps=[]
 for e in evt:
  c=e['tc'];wid=e['T14_d'];f=e['T12_d']/wid;idx=(q==0)&np.isfinite(t)&(abs(t-c)<.7); x=t[idx]-c; F=flux[idx].reshape((-1,121));v=np.isfinite(F).all(axis=1);x=x[v];F=F[v];shape=np.clip((wid/2-abs(x))/(wid*f),0,1);A=np.column_stack([np.ones(len(x)),x,-shape]);coef=np.linalg.lstsq(A,F,rcond=None)[0];maps.append(coef[2])
 image=np.mean(maps,axis=0).reshape(11,11); yy,xx=np.indices((11,11)); nb=list(csv.DictReader(open(r/f'{tic}_ari_neighbours.txt'),skipinitialspace=True)) if False else []
 # ARI response has metadata lines; detect csv header
 lines=(r/f'{tic}_ari_neighbours.txt').read_text().splitlines();ix=next(i for i,x in enumerate(lines) if x.startswith('source_id,'));nb=list(csv.DictReader(lines[ix:])); positions=[]
 for n in nb:
  x,y=wcs.all_world2pix(float(n['ra']),float(n['dec']),0); positions.append((n['source_id'],float(x),float(y)))
 # Gaussian fixed template plus constant plane; width grid fits empirical PSF uncertainty.
 def test(x,y):
  best=None
  for sig in [.65,.8,1.,1.2,1.4]:
   g=np.exp(-((xx-x)**2+(yy-y)**2)/(2*sig**2));A=np.column_stack([g.ravel(),np.ones(121),xx.ravel(),yy.ravel()]); c=np.linalg.lstsq(A,image.ravel(),rcond=None)[0];rss=float(np.sum((image.ravel()-A@c)**2));
   if best is None or rss<best[0]:best=(rss,sig,float(c[0]))
  return best
 candidates=[{'source_id':n,'x':x,'y':y,'rss':test(x,y)[0],'sigma':test(x,y)[1],'amplitude':test(x,y)[2]} for n,x,y in positions];best=min(candidates,key=lambda a:a['rss']); tx,ty=positions[0][1:]; centers=[]
 for im in [image]+[a.reshape(11,11) for a in maps]:
  old=image; image=im; grid=[]
  for dx in np.arange(-.5,.501,.05):
   for dy in np.arange(-.5,.501,.05):
    score=test(tx+dx,ty+dy);grid.append((score[0],float(dx),float(dy),score[1]))
  b=min(grid);centers.append({'dx_pix':b[1],'dy_pix':b[2],'sigma_pix':b[3],'edge_of_grid':abs(b[1])>.49 or abs(b[2])>.49});image=old
 fig,ax=plt.subplots(figsize=(5,5));ax.imshow(image,origin='lower',cmap='magma');ax.scatter([x[1] for x in positions],[x[2] for x in positions],facecolors='none',edgecolors='cyan',s=75);ax.scatter([tx],[ty],marker='+',s=100,c='lime');ax.scatter([tx+centers[0]['dx_pix']],[ty+centers[0]['dy_pix']],marker='x',c='white');ax.set_title(f'TIC {tic}, sector {sec}: eclipse template map');fig.tight_layout();fig.savefig(r/f'{tic}_pixel_diagnostic.png',dpi=130);plt.close(fig)
 result={'free_psf_centers':centers,'sector':sec,'n_events':len(evt),'candidates':candidates,'best_source':best['source_id'],'caveat':'Uncalibrated catalogue WCS; Gaussian fixed-PSF + plane; RSS unweighted and no formal significance; PSF model/WCS systematics can dominate. No free centroid or WCS registration.'};(r/f'{tic}_pixel_template.json').write_text(json.dumps(result,indent=2));print(tic,'events',len(evt),'best',best,'target',candidates[0])
