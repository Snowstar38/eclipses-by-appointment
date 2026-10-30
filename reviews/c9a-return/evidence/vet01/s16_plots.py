# s16: one 3-panel figure per star: out-of-eclipse TESScut image, stacked difference image (s8), raw QLP SAP fold (s5 profile)
import numpy as np, json, csv, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
for tic,sec in [('195865529','56'),('468181994','39')]:
    z=np.load(f'pix/img_{tic}_s{sec}.npz'); J=json.load(open(f'pix/pix_{tic}.json'))[sec]
    fold=np.loadtxt(f'fold_{tic}.txt')
    fig,ax=plt.subplots(1,3,figsize=(11,3.6))
    for a,im,tt in ((ax[0],z['O'],f's{sec} out-of-eclipse (e/s)'),(ax[1],z['D'],f's{sec} out minus in, {J["nev"]} primaries')):
        h=a.imshow(im,origin='lower',cmap='viridis'); plt.colorbar(h,ax=a,fraction=0.046)
        a.plot(z['xs'][1:],z['ys'][1:],'w+',ms=6); a.plot(z['xT'],z['yT'],'rx',ms=9,mew=2); a.set_title(tt,fontsize=9)
        a.contour(z['ap'],levels=[0.5],colors='r',linewidths=0.8)
    ax[2].plot(fold[:,0],(fold[:,1]-1)*1e3,'k.',ms=3); ax[2].set_xlabel('phase'); ax[2].set_ylabel('ppt (raw QLP SAP, local norm.)')
    ax[2].set_title(f'TIC {tic} fold, all QLP sectors',fontsize=9)
    fig.tight_layout(); fig.savefig(f'fig_{tic}.png',dpi=110); plt.close(fig)
print('ok')
