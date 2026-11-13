from common import *
from validation import *
from dynamics_check import assess
cert=read(D/'CONNECTION_CERTIFICATE.json');nom=read(D/'NOMINAL_PLAN_128.json');node=nom['nodes'][-1];c=constants(True)
p=validate_box(node['x'],['0.00001','0.00001','0.00001','0.000002','0.000001'],node['inverse'],['4999/1000000','1/200'],c)
p['id']='endpoint_strip';parent=cert['patches'][-1]
p['inside_parent_patch_box']=all(F(parent['state_box'][i][0])<F(p['state_box'][i][0]) and F(p['state_box'][i][1])<F(parent['state_box'][i][1]) for i in range(5))
assert p['passed'] and p['inside_parent_patch_box']
s=assess(p,node,c,constants(False))
write(D/'ENDPOINT_STABILITY_STRIP.json',{'root_certificate':p,'parent_patch':127,'stability':s,'independent_scope':'This narrow interval only; no optimized threshold and no inference from failed broad bounds'})
print(json.dumps({'root_passed':p['passed'],'same_branch_by_parent_uniqueness':p['inside_parent_patch_box'],'mu':p['mu'],'norm_upper_display':s['norm_display'],'certified_attracting':s['certified_attracting']},indent=2))
