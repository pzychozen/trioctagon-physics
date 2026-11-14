from common import *
from check_certificate import check
from geometry import *
import copy
original=read(D/'exact_certificate.json');original_bytes=(D/'exact_certificate.json').read_bytes();points,_,_,_=folded_family();records=[]
def control(name,mutate,expected):
    cert=copy.deepcopy(original);description=mutate(cert)
    try:check(cert)
    except (ValueError,AssertionError) as e:
        message=str(e);assert expected in message,(name,message)
        records.append({'name':name,'mutation':description,'expected_rejection_contains':expected,'observed_rejection':message,'result':'REJECTED_AS_REQUIRED','mutated_canonical_json_sha256':sha(json.dumps(cert,sort_keys=True).encode())});print(name,':',message,flush=True)
    else:raise AssertionError('False certificate accepted: '+name)
def false_parameter(c):c['transition']['parameter'][0]='-149/100';return 'Change rational part of x* from -3/2 to -149/100.'
def omit_facet(c):
    f=c['domains'][2]['faces'].pop();return 'Omit '+f['id']+' from C2, leaving a genuine hull edge without its second facet.'
def missing_zero(c):
    f=next(f for f in c['domains'][1]['faces'] if set(f['labels'])==set(['E05+','E09+','E17+','E21+','E10-','E16-']))
    removed='E21+';f['labels'].remove(removed);f['cycle'].remove(removed);work={k:constpoint(veval(v,T)) for k,v in points.items()};n,d=plane(work,f['cycle']);f['plane_basis']=f['cycle'][:3];f['normal_polynomials']=vdump(n);f['offset_polynomial']=pdump(d);f['residual_polynomials']={k:pdump(residual(n,d,p)) for k,p in work.items()}
    return 'Remove E21+ from both the six-point face declaration and cycle; rebuild its plane and every residual consistently so only the complete-zero-set test exposes the omission.'
def bad_endpoint(c):
    m=c['endpoints']['A']['vertex_mapping'];a,b=list(m)[:2];m[a]['labels'][0],m[b]['labels'][0]=m[b]['labels'][0],m[a]['labels'][0];return 'Swap one branch label between two distinct A endpoint positions.'
def gap(c):c['domains'][2]['lower']=(T+Q(F(1,1000))).dump();return 'Start C2 at x*+1/1000, leaving a coverage gap.'
def wrong_support(c):
    f=c['domains'][0]['faces'][0];f['cycle']=[f['cycle'][0],*reversed(f['cycle'][1:])];n,d=plane(points,f['cycle']);f['plane_basis']=f['cycle'][:3];f['normal_polynomials']=vdump(n);f['offset_polynomial']=pdump(d);f['residual_polynomials']={k:pdump(residual(n,d,p)) for k,p in points.items()}
    return 'Reverse an outward cycle and coherently rebuild the inward plane and residuals; stored formulas agree but the required support sign is false.'
for args in [('false_transition',false_parameter,'false transition parameter'),('wrong_support_sign',wrong_support,'face fails support'),('omitted_facet',omit_facet,'ridge closure'),('incomplete_zero_set',missing_zero,'incomplete or incorrect full zero set'),('broken_endpoint_label_mapping',bad_endpoint,'broken endpoint label mapping'),('coverage_gap',gap,'coverage gap')]:control(*args)
# Decisive arithmetic edge cases: a double interior root cannot hide behind no sign change.
mid=(A+T)/2;double=pmul(poly([-mid,1]),poly([-mid,1]));assert root_count_open(double,A,T)==1
try:uniform_sign(double,A,T)
except ValueError as e:records.append({'name':'even_multiplicity_hidden_root','mutation':'Use (x-(A+x*)/2)^2: positive on both sides but zero in the chamber.','result':'REJECTED_AS_REQUIRED','observed_rejection':str(e)})
else:raise AssertionError('Interior tangency root escaped Sturm check')
boundary=pmul(pmul(poly([-A,1]),poly([-A,1])),poly([-T,1]));assert root_count_open(boundary,A,T)==0 and uniform_sign(boundary,A,T)==-1
assert (D/'exact_certificate.json').read_bytes()==original_bytes
write(D/'NEGATIVE_CONTROL_RESULTS.json',{'status':'PASS','checked_utc':now(),'certificate_sha256':sha(original_bytes),'controls':records,'positive_endpoint_root_control':'PASS: (x-A)^2(x-x*) is strictly negative in (A,x*) while vanishing only at its endpoints.','original_certificate_unchanged':True,'scope':'New certificate/checker controls only, no historical scientific replay.'})
print('PASS all six certificate rejection controls and an even-multiplicity arithmetic control.')
