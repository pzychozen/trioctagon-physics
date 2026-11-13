"""Certificate checker: fresh shared-engine replay plus separately organized
exact-Fraction containment/norm/coverage/identification checks. Not a second
independent interval implementation. No nominal root solving or old suite run.
"""
from common import *
from validation import *
from dynamics_check import direct_quotient
import copy,time

def pair(x):return tuple(map(F,x))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    v=[a*b for a in x for b in y];return (min(v),max(v))
def scale(a,x):return mul((a,a),x)
def total(xs):
    ans=(F(0),F(0))
    for x in xs:ans=add(ans,x)
    return ans
def contains(x,y):return x[0]<=y[0] and y[1]<=x[1]
def strictly(x,y):return x[0]<y[0] and y[1]<x[1]
def absup(x):return max(map(abs,x))
def imat(x):return [[pair(v) for v in row] for row in x]
def imm(A,B):return [[total(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def pointmat(x):return [[(F(v),F(v)) for v in row] for row in x]
def semantic(cert):
    assert cert['mu_coverage']==['0','1/200'] and cert['zero_is_anchor_only'] is True
    pp=cert['patches'];jj=cert['joins'];assert len(pp)==128 and len(jj)==127
    for i,p in enumerate(pp):
        assert p['id']==i and list(map(F,p['mu']))==[F(i,25600),F(i+1,25600)],'False parameter coverage'
        assert F(p['state_box'][4][0])>0,'Host cannot replace the normalized branch'
    for i,j in enumerate(jj):
        assert j['left']==i and j['right']==i+1
        assert list(map(F,j['mu']))==[F(pp[i]['mu'][1])]*2
        for k in range(5):
            region=pair(j['state_box'][k])
            assert contains(region,pair(pp[i]['state_box'][k])) and contains(region,pair(pp[i+1]['state_box'][k])),'Broken shared-uniqueness join'
    assert cert['endpoint']['Up']==read(S/'m3_accepted_support.json')['values']['exact_receipts']['Up'],'Endpoint trap substituted'
    for z,up in zip(cert['endpoint']['quotient_enclosure'],cert['endpoint']['Up']):assert strictly(pair(up),pair(z)),'Invalid endpoint inclusion / substituted host'
    assert F(cert['endpoint']['quotient_enclosure'][4][0])>0
    for key,index,mu in [('onset',0,F(0)),('endpoint',127,F(1,200))]:
        row=cert[key];assert row['parent_patch']==index and list(map(F,row['mu']))==[mu,mu]
        for i in range(5):assert strictly(pair(pp[index]['state_box'][i]),pair(row['state_box'][i]))

def exact_patch(p,existence=True):
    center=list(map(F,p['center']));r=list(map(F,p['radii']));assert all(v>0 for v in r)
    exactbox=[(v-h,v+h) for v,h in zip(center,r)]
    assert all(contains(pair(b),e) for b,e in zip(p['state_box'],exactbox))
    A=pointmat(p['A']);J=imat(p['state_derivative']);AJ=imm(A,J)
    E=imat(p['defect_matrix'])
    for i in range(5):
        for j in range(5):assert contains(E[i][j],sub((F(i==j),F(i==j)),AJ[i][j]))
    qrows=[sum(absup(E[i][j])*r[j]/r[i] for j in range(5)) for i in range(5)]
    assert qrows==list(map(F,p['weighted_row_bounds']))
    assert max(qrows)<1,'No proved contraction / nonsingular preconditioner'
    a,b=map(F,p['mu']);m=(a+b)/2;delta=(a-m,b-m)
    residual=list(map(pair,p['center_residual']));param=list(map(pair,p['parameter_derivative']))
    for i in range(5):
        offset=neg(total(mul(A[i][j],residual[j]) for j in range(5)))
        offset=sub(offset,mul(total(mul(A[i][j],param[j]) for j in range(5)),delta))
        offset=add(offset,total(mul(E[i][j],(-r[j],r[j])) for j in range(5)))
        saved=pair(p['krawczyk_offset'][i]);assert contains(saved,offset)
        assert contains(pair(p['root_enclosure'][i]),add((center[i],center[i]),saved))
        if existence:assert absup(saved)<r[i],'No strict self-map'
    margins=p['regularity']
    for v in [margins['slice'],margins['gauge_modulus'],margins['gauge_real'],margins['nu'],*margins['prestage_reals'],*margins['prestage_radii']]:assert F(v[0])>0
    assert all(absup(pair(v))<=1 for v in margins['squared_kicks'])
    return float(max(qrows))

def replay_patch(p,c):
    new=validate_box(p['center'],p['radii'],p['A'],p['mu'],c)
    for key in ['state_box','center_residual','parameter_derivative','state_derivative','defect_matrix','krawczyk_offset','root_enclosure','weighted_row_bounds','regularity']:
        assert new[key]==p[key],('Replay mismatch',key,p.get('id',p.get('left','special')))

def exact_stability(s,replay,c):
    J=imat(s['D_Fhat']);M=[[scale(F(1 if i<3 else -1),v) for v in row] for i,row in enumerate(J)]
    P2=imat(s['P_two_step']);actual=imm(M,M)
    assert all(contains(P2[i][j],actual[i][j]) for i in range(5) for j in range(5))
    Q=pointmat(s['Q']);Rinv=pointmat(s['approximate_Q_inverse']);RQ=imm(Rinv,Q)
    eps=max(sum(absup(sub((F(i==j),F(i==j)),RQ[i][j])) for j in range(5)) for i in range(5))
    stored_eps=F(s['inverse_defect']);assert eps<=stored_eps<1
    sim=imat(s['transformed_matrix']);actual=imm(imm(Rinv,P2),Q)
    assert all(contains(sim[i][j],actual[i][j]) for i in range(5) for j in range(5))
    bound=max(sum(absup(v) for v in row) for row in sim)/(1-stored_eps)
    assert bound==F(s['norm_upper'])
    if s['certified_attracting']:assert bound<1
    for v in [s['direct_map_regularity']['gauge_modulus'],s['direct_map_regularity']['slice'],*s['direct_map_regularity']['prestage_radii']]:assert F(v[0])>0
    if replay:
        z=[IV.bounds(*pair(row)) for row in s['quotient_box']]
        out,margin=direct_quotient(z,IV.bounds(*map(F,s['mu'])),c)
        assert serial([r.d for r in out])==s['D_Fhat'] and serial(margin)==s['direct_map_regularity']
    return float(bound)

def main():
    tic=time.time();cert=read(D/'CONNECTION_CERTIFICATE.json');c=constants(True)
    ids=read(L/'INPUT_IDENTITIES.json')
    for row in ids['files']:
        b=(R/row['copied_path']).read_bytes();assert sha(b)==row['sha256'] and len(b)==row['bytes']
    for name in ['arithmetic.py','model.py','validation.py','generate_certificate.py']:
        assert sha((R/'scripts'/name).read_bytes())==cert['implementation_identities'][name],name
    assert serial(c)==cert['constants']
    host=read(S/'m2_accepted_certificate.json')['integer_interval_certificate']
    assert host['krawczyk_strict_inclusion'] is True
    for x,k in zip(host['host_box'],host['krawczyk_image']):
        b=lambda row:(F(int(row['lo_numerator']),2**row['denominator_power_of_two']),F(int(row['hi_numerator']),2**row['denominator_power_of_two']))
        assert strictly(b(x),b(k))
    semantic(cert)
    for index,p in enumerate(cert['patches']):
        exact_patch(p);replay_patch(p,c)
        if index%32==0:print('checked patch',index,flush=True)
    for p in cert['joins']:exact_patch(p,False);replay_patch(p,c)
    for key in ['onset','endpoint']:exact_patch(cert[key]);replay_patch(cert[key],c)
    endpoint=[IV.bounds(*pair(row)) for row in cert['endpoint']['root_enclosure']]
    assert serial(reconstruct(endpoint,IV.make(F(1,200)),c))==cert['endpoint']['quotient_enclosure']
    stability=read(D/'STABILITY_CERTIFICATE.json')
    for s in stability['rows']:exact_stability(s,True,c)
    strip=read(D/'ENDPOINT_STABILITY_STRIP.json');exact_patch(strip['root_certificate']);replay_patch(strip['root_certificate'],c)
    for a,b in zip(cert['patches'][127]['state_box'],strip['root_certificate']['state_box']):assert strictly(pair(a),pair(b))
    assert list(map(F,strip['root_certificate']['mu']))==[F(4999,1000000),F(1,200)]
    assert strip['stability']['mu']==strip['root_certificate']['mu']
    reconstructed=serial(reconstruct([IV.bounds(*pair(row)) for row in strip['root_certificate']['state_box']],IV.bounds(*map(F,strip['root_certificate']['mu'])),c))
    assert reconstructed==strip['stability']['quotient_box']
    exact_stability(strip['stability'],True,c);assert strip['stability']['certified_attracting']
    controls=[]
    for name in ['false_coverage','broken_join','substituted_host','invalid_endpoint_trap']:
        bad=copy.deepcopy(cert)
        if name=='false_coverage':bad['patches'][1]['mu'][0]='1/25000'
        elif name=='broken_join':bad['joins'][0]['state_box']=[['0','0']]*5
        elif name=='substituted_host':bad['endpoint']['quotient_enclosure']=[['0','0']]*5
        else:bad['endpoint']['Up']=[['-10','10']]*5
        try:semantic(bad)
        except AssertionError as e:controls.append({'control':name,'rejected':True,'reason':str(e)})
        else:raise AssertionError('Rejected control accepted: '+name)
    result={'status':'PASS','checked_utc':now(),'elapsed_seconds':time.time()-tic,'connection_coverage':['0','1/200'],'zero_is_anchor_only':True,'patches':128,'shared_uniqueness_joins':127,'onset_and_endpoint_refinements':2,'fresh_analytic_interval_replay':'PASS; shared new engine, not independent implementation','independent_fraction_containment_norm_and_coverage_audit':'PASS','exact_M3_Up_identification':'PASS; positive parity','stability_full_corridor':'UNRESOLVED by these broad bounds; no loss certified','stability_explicit_interval':['4999/1000000','1/200'],'stability_norm_upper_display':strip['stability']['norm_display'],'rejection_controls':controls,'historical_scientific_replays':0}
    write(D/'CERTIFICATE_CHECK.json',result)
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
