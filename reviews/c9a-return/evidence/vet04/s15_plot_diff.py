# two-panel plots (out-of-eclipse image, difference image in units of per-pixel noise) from the s13 stacks
import sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
for tag in sys.argv[1:]:
    z=np.load(f's13_diff_{tag}.npz'); XX=z['XX']; G=z['G']; sep=z['sep']
    fig,ax=plt.subplots(1,2,figsize=(7.4,3.6))
    ax[0].imshow(z['oot'],origin='lower',cmap='gray_r'); ax[0].set_title('out of eclipse')
    im=ax[1].imshow(z['diff']/z['sigp'],origin='lower',cmap='RdBu_r',vmin=-5,vmax=5); ax[1].set_title('(out - in) / sigma_pix')
    for a in ax:
        for i in range(len(G)):
            if sep[i]<90: a.plot(XX[i,0],XX[i,1],'x' if i else '+',color='lime' if i==0 else 'orange',ms=9 if i==0 else max(3,18-G[i]*0.9))
        a.plot(z['pf'][0],z['pf'][1],'o',mfc='none',mec='magenta',ms=10)
        a.set_xlim(-0.5,10.5); a.set_ylim(-0.5,10.5)
    plt.colorbar(im,ax=ax[1],fraction=0.046); fig.suptitle(tag+'  (+ target, x Gaia G<18 within 90", o fitted deficit)',fontsize=8)
    fig.tight_layout(); fig.savefig(f's15_diff_{tag}.png',dpi=100); plt.close(fig)
