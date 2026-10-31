from pathlib import Path
p=Path(__file__).parent/'review_measure.py';s=p.read_text().replace("min((1.15 if tic=='388152396' else 3)*dur,.35*p0)", 'min(3*dur,.35*p0)');s=s.replace('x=t[ix]-pred;y=f[ix];oot=np.abs(x)>dur',"x=t[ix]-pred;y=f[ix]\n   if tic=='388152396' and receipt['sector']==81 and cycle==67:\n    keep=~((x>.20)&(x<.45));x=x[keep];y=y[keep]\n   oot=np.abs(x)>dur")
p.write_text(s)
