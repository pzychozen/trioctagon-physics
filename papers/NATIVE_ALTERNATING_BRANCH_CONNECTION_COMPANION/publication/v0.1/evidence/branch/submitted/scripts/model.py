"""New analytic divided quotient, sharing only basic arithmetic design with M2.
All physical parameters and host bounds are authenticated inputs, not floats.
"""
from common import *
from arithmetic import *
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mv(a,b):return [dot(r,b) for r in a]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[dot(r,c) for c in tr(b)] for r in a]
def constants(interval=False):
    accepted=read(S/'m2_accepted_certificate.json')['integer_interval_certificate']
    u=[]
    for row in accepted['krawczyk_image']:
        lo=F(int(row['lo_numerator']),2**row['denominator_power_of_two']);hi=F(int(row['hi_numerator']),2**row['denominator_power_of_two'])
        u.append(IV.bounds(lo,hi) if interval else float((lo+hi)/2))
    make=IV.make if interval else float;ep=make(1)/20;g=make(1)/5;k=list(map(make,['1','1.2208964704604097','6.35310346037241']))
    M=[[(1+ep*(k[i]-u[i]**2) if i==j else make(0))+g*(1-3*int(i==j)) for j in range(3)] for i in range(3)]
    JR=[[M[i][j]-(2*ep*u[i]**2 if i==j else 0) for j in range(3)] for i in range(3)]
    a=sqrt(u[0]**2+u[1]**2);r=sqrt(dot(u,u))
    V=tr([[u[1]/a,-u[0]/a,make(0)],[u[0]*u[2]/(a*r),u[1]*u[2]/(a*r),-(u[0]**2+u[1]**2)/(a*r)]])
    K=mm(mm(tr(V),M),V);disc=sqrt((K[0][0]-K[1][1])**2+4*K[0][1]**2)
    m1=(K[0][0]+K[1][1]+disc)/2;m2=(K[0][0]+K[1][1]-disc)/2
    e=[K[0][1],m1-K[0][0]];norm=sqrt(dot(e,e));e=[x/norm for x in e];perp=[-e[1],e[0]]
    return dict(u=u,ep=ep,g=g,k=k,M=M,JR=JR,V=V,K=K,m1=m1,m2=m2,e=e,perp=perp,ve=mv(V,e),vp=mv(V,perp),lc=(1+1/m1)/9,sigma=9*m1)
def regularized(x,mu,c,derivatives=True,parameter_derivative=False):
    """x=(X_A,X_B,X_C,y,nu), t=mu/nu. Returns R and chart margins."""
    if derivatives:
        n=6 if parameter_derivative else 5
        z=[AD(v,[v*0+int(i==j) for j in range(n)]) for i,v in enumerate(x)]
        if parameter_derivative:mu=AD(mu,[mu*0+int(j==5) for j in range(6)])
    else:z=x
    X=z[:3];y,nu=z[3:];t=mu/nu;zero=z[0]*0;one=zero+1
    T=DD(zero,one,t)
    b=[DD(c['ve'][i],y*c['vp'][i],t) for i in range(3)]
    bf=[v.full() for v in b];u=c['u'];ep=c['ep']
    # Exact host equation is used only to set the known constant prestage to u.
    pr=[DD(u[i],dot(c['JR'][i],X)-ep*(3*u[i]*t*X[i]**2+u[i]*bf[i]**2+t**2*X[i]**3+t*X[i]*bf[i]**2),t) for i in range(3)]
    pi=[dot(c['M'][i],b)-ep*(2*u[i]*T*X[i]*b[i]+T**2*X[i]**2*b[i]+T*b[i]**3) for i in range(3)]
    radii=[(pr[i]**2+T*pi[i]**2).sqrt() for i in range(3)]
    phase=[]
    for i in range(3):
        terms=[]
        for j in range(3):
            if i==j:continue
            real=pr[j]*pr[i]+T*pi[j]*pi[i]
            imag=pi[j]*pr[i]-pr[j]*pi[i]
            terms.append((3*real**2*imag-T*imag**3)/(radii[j]**3*radii[i]**3))
        phase.append(DD(c['lc'],nu,t)*sum(terms))
    outR=[];outI=[];squared_kicks=[]
    for i in range(3):
        d=phase[i];d2=d.full()**2;w=t*d2;squared_kicks.append(value(w))
        co=DD(one,d2*entire_tail(w,'C'),t)
        si=d*DD(one,d2*entire_tail(w,'S'),t)
        outR.append(pr[i]*co-T*pi[i]*si)
        outI.append(pr[i]*si+pi[i]*co)
    hr=dot(u,outR);hi=dot(u,outI);den=(hr**2+T*hi**2).sqrt()
    qr=[(outR[i]*hr+T*outI[i]*hi)/den for i in range(3)]
    qi=[(outI[i]*hr-outR[i]*hi)/den for i in range(3)]
    # qr(0)=u and V^T qi(0)=-e exactly; neither identity is replaced by a rounded residual.
    result=[qr[i].d-X[i] for i in range(3)]+[dot(v,[q.d for q in qi])+y*c['perp'][j] for j,v in enumerate(tr(c['V']))]
    margins={'slice':value(dot(u,[u[i]+t*X[i] for i in range(3)])),'prestage_reals':[value(p.full()) for p in pr],'prestage_radii':[value(r.full()) for r in radii],'gauge_modulus':value(den.full()),'gauge_real':value(hr.full()),'squared_kicks':squared_kicks,'nu':value(nu),'t':value(t)}
    return result,margins
def reconstruct(x,mu,c):
    t=mu/x[4];a=sqrt(t)
    return [t*v for v in x[:3]]+[a*(c['e'][j]+t*x[3]*c['perp'][j]) for j in range(2)]
