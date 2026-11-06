import os, runpy, numpy as np
os.chdir(r'[workspace]/Fable 5\made\sb1-scale\teff438089101')
d=runpy.run_path('solve.py')
T=d['tgrid']; E=d['egrid']; obs=d['OBS']; slope=d['SLOPE']; intr=np.array([d['intrinsic'](t) for t in T]); mask=T<=10700
T=T[mask]; intr=intr[mask]
# band errors only; extra floor independent per color, as original
for sys in [0.02,0.04]:
 C=np.diag([.004**2, .001**2+.023**2, .031**2+.023**2, .023**2+.023**2])+np.eye(4)*sys**2
 C[1,2]=C[2,1]=C[1,3]=C[3,1]=C[2,3]=C[3,2]=.023**2
 D=obs[None,None,:]-intr[:,None,:]-E[None,:,None]*slope
 chi=np.einsum('tei,ij,tej->te',D,np.linalg.inv(C),D)
 i,j=np.unravel_index(np.argmin(chi),chi.shape); p=chi.min(axis=1); z=chi.min(axis=0); low,high=T[p<=chi[i,j]+1][[0,-1]]; el,eh=E[z<=chi[i,j]+1][[0,-1]]
 print(f'COV sys={sys}: T={T[i]:.0f} E={E[j]:.4f} chi2={chi[i,j]:.3f}; profile T={low:.0f}-{high:.0f}, E={el:.3f}-{eh:.3f}')
