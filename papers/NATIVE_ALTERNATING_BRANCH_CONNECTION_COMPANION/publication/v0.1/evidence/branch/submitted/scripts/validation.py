from common import *
from model import *
def serial(x):
    if isinstance(x,IV):return x.out()
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,list):return [serial(v) for v in x]
    return x
def intervals(x):return [IV.make(v) for v in x]
def enclose(center,radii):return [IV.bounds(F(v)-F(r),F(v)+F(r)) for v,r in zip(center,radii)]
def qbound(E,radii):
    return [sum(F(e.absup(),SCALE)*F(radii[j])/F(radii[i]) for j,e in enumerate(row)) for i,row in enumerate(E)]
def validate_box(center,radii,Astrings,mu_bounds,c):
    a,b=map(F,mu_bounds);mid=(a+b)/2;delta=IV.bounds(a-mid,b-mid)
    cx=intervals(center);box=enclose(center,radii);A=[intervals(row) for row in Astrings]
    rr,margins=regularized(box,IV.bounds(a,b),c)
    J=[r.d for r in rr];E=[[int(i==j)-v for j,v in enumerate(row)] for i,row in enumerate(mm(A,J))]
    rows=qbound(E,radii)
    fixed,_=regularized(cx,IV.make(mid),c)
    fixed=[r.v for r in fixed]
    param,_=regularized(cx,IV.bounds(a,b),c,parameter_derivative=True)
    pder=[r.d[5] for r in param]
    # Precondition before parameter interval multiplication to preserve cancellation.
    defect=mv(A,fixed);pdef=mv(A,pder)
    offset=[-defect[i]-pdef[i]*delta+sum(E[i][j]*IV.bounds(-F(radii[j]),F(radii[j])) for j in range(5)) for i in range(5)]
    K=[cx[i]+offset[i] for i in range(5)]
    inclusion=all(F(off.absup(),SCALE)<F(rad) for off,rad in zip(offset,radii))
    positive=all(x.lo>0 for x in [margins['slice'],margins['gauge_modulus'],margins['gauge_real'],margins['nu'],*margins['prestage_reals'],*margins['prestage_radii']])
    result={'mu':[str(a),str(b)],'center':center,'radii':radii,'A':Astrings,'state_box':serial(box),'center_residual':serial(fixed),'parameter_derivative':serial(pder),'state_derivative':serial(J),'defect_matrix':serial(E),'krawczyk_offset':serial(offset),'root_enclosure':serial(K),'weighted_row_bounds':list(map(str,rows)),'q_display':float(max(rows)),'strict_inclusion':inclusion,'regularity_positive':positive,'regularity':serial(margins),'passed':inclusion and max(rows)<1 and positive}
    return result
if __name__=='__main__':
    import time
    trial=sys.argv[1] if len(sys.argv)>1 else '01'
    tic=time.time();nom=read(D/'NOMINAL_PLAN_128.json');c=constants(True);radii=sys.argv[2:] if len(sys.argv)>2 else ['0.0005','0.0005','0.0006','0.0001','0.0001'];assert len(radii)==5
    N=nom['patch_count'];results=[]
    for i in [0,63,127]:
        row=nom['nodes'][i+1]
        result=validate_box(row['x'],radii,row['inverse'],[str(F(i,200*N)),str(F(i+1,200*N))],c)
        results.append(result)
        print(i,'pass',result['passed'],'q',result['q_display'],'inclusion',result['strict_inclusion'],'offset/radius',[float(max(abs(F(x)) for x in row)/F(rad)) for row,rad in zip(result['krawczyk_offset'],radii)],flush=True)
    write(D/('VALIDATION_TRIAL_'+trial+'.json'),{'purpose':'Three preliminary patch designs, not full continuation','elapsed_seconds':time.time()-tic,'attempts':results})
    print('elapsed',time.time()-tic)
