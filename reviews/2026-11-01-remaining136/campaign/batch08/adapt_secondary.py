from pathlib import Path
b=Path(__file__).parent
s=(b.parent/'batch07/secondary_check.py').read_text()
a=s.index(' if tic not in');z=s.index('  par,cov=',a)
s=s[:a]+' trlocal-source/omitted
s=s.replace(' ax.set_title(tic+'," except Exception as e:result=dict(status='Fit failed; secondary unresolved',guess_phase=guess,error=str(e))\n ax.set_title(tic+")
s=s.replace('xs=[];ys=[];ss=[]',"guess={'176048490':.369,'76177367':.58}.get(tic,guess);xs=[];ys=[];ss=[]")
s=s.replace('depth_ppt=par[2]*1000,','depth_ppt=par[2]*1000*min(1,par[4]/(2*par[5])),trapezoid_depth_parameter_ppt=par[2]*1000,fitted_ingress_days=par[5],')
(b/'secondary_check.py').write_text(s)
