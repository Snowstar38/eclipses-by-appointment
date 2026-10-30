import numpy as np
from scipy.optimize import least_squares
def trap(t,tc,dep,T14,T23):
    T23=min(abs(T23),abs(T14)); T14=abs(T14)
    x=np.abs(t-tc); y=np.zeros_like(t)
    full=x<=T23/2; y[full]=dep
    ing=(x>T23/2)&(x<T14/2)
    if T14>T23: y[ing]=dep*(T14/2-x[ing])/((T14-T23)/2)
    return 1-y
def model(p,t,texp,tref,nsub=11):
    tc,dep,T14,T23,a0,a1,a2=p
    off=(np.arange(nsub)-(nsub-1)/2)/nsub*texp
    tt=(t[:,None]+off[None,:]).ravel()
    m=trap(tt,tc,dep,T14,T23).reshape(len(t),nsub).mean(1)
    dt=t-tref
    return m*(a0+a1*dt+a2*dt*dt)
def fit_event(t,f,texp,tc0,dep0,T140,T230,fix_shape=False,quad=True):
    tref=tc0
    if fix_shape:
        def res(q):
            p=[q[0],q[1],T140,T230,q[2],q[3],q[4] if quad else 0.0]
            return f-model(p,t,texp,tref)
        q0=[tc0,dep0,1,0,0] if quad else [tc0,dep0,1,0]
        r=least_squares(res,q0,x_scale=[0.003,0.003,0.001,0.001,0.001][:len(q0)])
        J=r.jac; s=np.std(r.fun,ddof=len(q0))
        cov=np.linalg.pinv(J.T@J)*s*s; e=np.sqrt(np.diag(cov))
        p=[r.x[0],r.x[1],T140,T230]+list(r.x[2:])+([] if quad else [0.0])
        ep=[e[0],e[1],0,0]
    else:
        def res(q): return f-model(list(q) if quad else list(q)+[0.0],t,texp,tref)
        q0=[tc0,dep0,T140,T230,1,0,0] if quad else [tc0,dep0,T140,T230,1,0]
        lb=[tc0-0.05,0,0.01,0,0.5,-1,-1][:len(q0)]; ub=[tc0+0.05,0.5,0.5,0.5,1.5,1,1][:len(q0)]
        r=least_squares(res,q0,bounds=(lb,ub),x_scale=[0.003,0.003,0.01,0.01,0.001,0.001,0.001][:len(q0)])
        J=r.jac; s=np.std(r.fun,ddof=len(q0))
        cov=np.linalg.pinv(J.T@J)*s*s; e=np.sqrt(np.diag(cov))
        p=list(r.x)+([] if quad else [0.0]); ep=list(e[:4])
    resid=r.fun
    # red-noise beta: rms of binned residuals vs white expectation, bins ~ 30 min
    n=max(1,int(round((0.5/24)/np.median(np.diff(t)))))
    if n>1 and len(resid)>4*n:
        k=len(resid)//n; b=resid[:k*n].reshape(k,n).mean(1)
        beta=max(1.0,np.std(b)/(np.std(resid)/np.sqrt(n)))
    else: beta=1.0
    ep=[x*beta for x in ep]
    return p,ep,np.std(resid),beta
