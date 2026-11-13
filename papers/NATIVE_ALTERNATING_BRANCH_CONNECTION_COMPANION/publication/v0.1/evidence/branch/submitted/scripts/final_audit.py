from common import *
from fractions import Fraction as F
import re
before=read(L/'OPERATOR_BEFORE.json');after={}
for key,args in [('head',['rev-parse','HEAD']),('branch',['symbolic-ref','--short','HEAD']),('status',['status','--porcelain=v1','-uall']),('staged',['diff','--cached','--binary']),('unstaged',['diff','--binary'])]:
    after[key]=git(args,'operator_after_'+key,USER).stdout.decode(errors='replace');assert after[key]==before[key],key
assert sha(Path(before['index_path']).read_bytes())==before['index_sha256']
identities=read(L/'INPUT_IDENTITIES.json')
for row in identities['files']:
    b=(R/row['copied_path']).read_bytes();assert sha(b)==row['sha256'] and len(b)==row['bytes'];assert b==Path(row['actual_origin']).read_bytes()
manifest=read(P/'PACKET_MANIFEST.json')
for row in manifest['files']:assert sha((P/row['path']).read_bytes())==row['sha256']
download=Path(r'C:\Users\Notandi\Downloads')
assert (R/'received/NATIVE_ALTERNATING_BRANCH_CONNECTION_01_CODEX_PACKET.zip').read_bytes()==(download/'NATIVE_ALTERNATING_BRANCH_CONNECTION_01_CODEX_PACKET.zip').read_bytes()
for outer,inner in [('NATIVE_ALTERNATING_BRANCH_CONNECTION_01_CODEX_WORK_ORDER.md','NATIVE_ALTERNATING_BRANCH_CONNECTION_01_CODEX_WORK_ORDER.md'),('NATIVE_ALTERNATING_BRANCH_CONNECTION_01_PRIOR_WORK_COMPARISON.md','PRIOR_WORK_COMPARISON.md')]:assert (download/outer).read_bytes()==(P/inner).read_bytes()
for row in read(L/'IMPLEMENTATION_ATTRIBUTION.json')['consulted_references']:
    b=(R/row['copy']).read_bytes();assert sha(b)==row['sha256'] and b==Path(row['origin']).read_bytes()
s=read(D/'EVIDENCE_SUMMARY.json');check=read(D/'CERTIFICATE_CHECK.json');alg=read(D/'ALGEBRA_AND_SOURCE_CHECKS.json');strip=read(D/'ENDPOINT_STABILITY_STRIP.json');cert=read(D/'CONNECTION_CERTIFICATE.json')
assert check['status']==alg['status']=='PASS' and all(x['rejected'] for x in check['rejection_controls'])
assert F(s['max_patch_q'])<F('0.614') and F(s['max_join_q'])<F('0.583')
assert F(s['minimum_slice'])>F('8.884') and F(s['minimum_prestage_real'])>F('1.504') and F(s['minimum_gauge_modulus'])>F('8.882')
assert F(s['maximum_squared_kick'])<F('0.0823') and F(s['nu_global'][0])>F('0.02209')
assert min(map(F,s['endpoint_Up_coordinate_margins']))>F('0.00001098')
assert F(strip['stability']['norm_upper'])<F('0.9601')
assert s['nominal_budget_used']['root_solves']<=600 and s['nominal_budget_used']['maximum_iterations_at_one_node']<=30
assert s['validation_budget_used']['full_certificate_passes_including_replay']<=4
for filename in ['PROOF_REPORT.md','README.md','RESULT_SUMMARY.md']:
    for link in re.findall(r'\]\(([^)]+)\)',(R/filename).read_text(encoding='utf-8')):
        if '://' not in link:assert (R/link.split('#')[0]).exists(),link
for name in ['arithmetic.py','model.py','validation.py','generate_certificate.py']:assert sha((R/'scripts'/name).read_bytes())==cert['implementation_identities'][name]
initial=[{'command':['run_python.cmd','scripts\\load_inputs.py'],'shell':'Windows Command Prompt','exit_status':0,'record_basis':'Observed tool completion; environment and identities were persisted by the run','outputs':['logs/ENVIRONMENT.json','logs/INPUT_IDENTITIES.json']},{'command':['run_python.cmd','scripts\\prior_search.py'],'shell':'Windows Command Prompt','exit_status':0,'record_basis':'Observed tool completion; child rg commands and complete outputs logged','outputs':['logs/PRIOR_SEARCH_RECORDS.json']},{'command':['run_python.cmd','scripts\\nominal.py'],'shell':'Windows Command Prompt','exit_status':0,'record_basis':'Observed tool completion; complete iteration histories and node results persisted','started_utc':read(D/'NOMINAL_PLAN_128.json')['started_utc'],'finished_utc':read(D/'NOMINAL_PLAN_128.json')['finished_utc'],'outputs':['data/NOMINAL_PLAN_128.json']}]
write(L/'INITIAL_EXECUTIONS.json',{'note':'These three top-level commands preceded the final execute.py logging wrapper. Their successful exits were observed directly; no replay was performed merely to manufacture logs.','records':initial})
inventory=[]
for root in [P,S,R/'received']:
    for path in sorted(root.rglob('*')):
        if path.is_file():inventory.append({'path':path.relative_to(R).as_posix(),'bytes':path.stat().st_size,'sha256':sha(path.read_bytes()),'role':'Supplied or copied immutable input'})
write(R/'SOURCE_INVENTORY.json',{'task':'NATIVE_ALTERNATING_BRANCH_CONNECTION_01','files':inventory,'origin_details':'logs/INPUT_IDENTITIES.json; logs/IMPLEMENTATION_ATTRIBUTION.json; packet/SOURCE_IDENTITIES.json'})
result={'status':'PASS','checked_utc':now(),'operator_HEAD_branch_status_index_and_tracked_diffs_unchanged':True,'source_worktree_required_files_unchanged':True,'original_received_packet_unchanged':True,'all_packet_manifest_entries_unchanged':len(manifest['files']),'standalone_order_and_prior_comparison_match_packet':True,'consulted_historical_script_bytes_unchanged':True,'claim_bounds_checked_as_exact_rationals':True,'implementation_bytes_match_checked_certificate':True,'required_inputs_authenticated':5,'repository_writes':0,'commits':0,'pushes':0,'historical_scientific_replays':0,'native_trajectory_runs':0,'scientific_outcome':'Full connection at the exact frozen family, returned for review','stability':'Explicit narrow endpoint interval plus inherited local scope; full corridor unresolved'}
write(L/'FINAL_PRESERVATION_AND_CLAIM_AUDIT.json',result)
print(json.dumps(result,indent=2))
