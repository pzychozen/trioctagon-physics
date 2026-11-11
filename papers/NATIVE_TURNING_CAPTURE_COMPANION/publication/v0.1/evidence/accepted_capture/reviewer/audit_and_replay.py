"""GPT review: archive/identity audit and transparent replay of submitted checker.

Submitted files are never modified. The only execution adaptation removes the
Windows conda-name precondition; validate() and all arithmetic are unchanged.
No claim is made that this Linux reviewer runtime is the Windows torment env.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, platform, sys, zipfile, copy, time

ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT/'submitted'
OUT = ROOT/'reviewer'
def digest(data): return hashlib.sha256(data).hexdigest()
def load(path): return json.loads(path.read_text(encoding='utf-8'))
def record_file(path):
    data=path.read_bytes()
    return {'bytes':len(data),'sha256':digest(data)}
report={'reviewer_environment':{'python':sys.version,'executable':sys.executable,'platform':platform.platform()},'started_utc':datetime.now(timezone.utc).isoformat()}
archive=ROOT/'received/NATIVE_TURNING_CAPTURE_01_REVIEW.zip'
report['archive']=record_file(archive)
assert report['archive']['sha256']==archive.with_suffix('.zip.sha256').read_text().split()[0]
with zipfile.ZipFile(archive) as z:
    names=z.namelist()
    assert len(names)==len(set(names))==112 and z.testzip() is None
    assert all((SUB/n).read_bytes()==z.read(n) for n in names)
    report['archive']['members_verified']=len(names)
manifest=load(SUB/'REVIEW_MANIFEST.json')
entries=manifest['files']
assert {e['path'] for e in entries}==set(names)-{'REVIEW_MANIFEST.json'}
for e in entries:
    info=record_file(SUB/e['path'])
    assert info['bytes']==e['bytes'] and info['sha256']==e['sha256'],e['path']
report['manifest_entries_verified']=len(entries)
fa=load(ROOT/'received/NATIVE_TURNING_CAPTURE_01_FINAL_DELIVERY_AUDIT.json')
assert fa['archive_sha256']==report['archive']['sha256'] and fa['archive_bytes']==archive.stat().st_size
assert {e['path'] for e in fa['members']}==set(names)
for e in fa['members']:
    assert record_file(SUB/e['path'])=={'bytes':e['bytes'],'sha256':e['sha256']},e['path']
report['external_delivery_audit_entries_verified']=len(fa['members'])
sources=load(SUB/'SOURCE_IDENTITIES.json')['sources']
for e in sources:
    d=(SUB/e['path']).read_bytes()
    assert len(d)==e['bytes'] and digest(d)==e['sha256'],e['path']
    if 'git_blob_computed_without_git' in e:
        actual=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()
        assert actual==e['git_blob_computed_without_git'],e['path']
report['source_identity_entries_verified']=len(sources)
claims=load(SUB/'CLAIM_LEDGER.json')['claims']
locators=0
for claim in claims:
    for e in claim.get('locators',[]):
        p=SUB/e['path']
        assert digest(p.read_bytes())==e['sha256'],str(e)
        lines=p.read_text(encoding='utf-8').splitlines()
        assert e['locator'] in lines[e['line']-1],str(e)
        locators+=1
report['claim_entries']=len(claims);report['claim_locators_verified']=locators
original=ROOT/'received/NATIVE_TURNING_CAPTURE_01_CODEX_PACKET.zip'
assert original.read_bytes()==(SUB/'received'/original.name).read_bytes()
with zipfile.ZipFile(original) as z:
    assert z.testzip() is None
    for n in z.namelist():
        assert z.read(n)==(SUB/'packet'/n).read_bytes(),n
    report['original_packet_members_preserved']=len(z.namelist())
assert (SUB/'sources/dynamics.py').read_bytes()==(SUB/'packet/inputs/reference/dynamics.py').read_bytes()
report['frozen_implementation_reference_matched']=True
checker=SUB/'scripts/check_certificate.py'
code=checker.read_text(encoding='utf-8')
guard="assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'"
assert code.count(guard)==1
adapted=code.replace(guard,'assert not sys.flags.optimize  # Reviewer runtime; do not disable proof assertions.',1)
(OUT/'checker_environment_only_adaptation.diff').write_text('- '+guard+'\n+ assert not sys.flags.optimize  # Reviewer runtime; do not disable proof assertions.\n')
namespace={'__name__':'gpt_reviewer_import','__file__':str(checker)}
exec(compile(adapted,str(checker),'exec'),namespace)
cert=load(SUB/'data/CERTIFICATE.json')
t0=time.monotonic(); actual=namespace['validate'](cert); elapsed=time.monotonic()-t0
submitted=load(SUB/'data/CERTIFICATE_CHECK.json')
assert all(submitted[k]==v for k,v in actual.items()),'Replay differs from submitted scientific results'
report['checker_replay']={'checker_sha256':digest(checker.read_bytes()),'certificate_sha256':digest((SUB/'data/CERTIFICATE.json').read_bytes()),'adaptation': 'Only the conda-name guard replaced with an assertion that Python optimization is disabled; all scientific functions and assertions unchanged. The submitted __main__ writer was not executed.','elapsed_seconds':elapsed,'stable_result_values_match':True,'result':actual}
mutations=[('wrong exact initial state',lambda x:x['states'][0][0][0].__setitem__(0,str(int(x['states'][0][0][0][0])+1))),('zero prestage modulus',lambda x:x['steps'][0]['moduli'][0].__setitem__(0,'0')),('wrong kick sign',lambda x:x['steps'][0].__setitem__('kicks',[['0','0']]*3)),('broken trajectory linkage',lambda x:x['states'][1].__setitem__(0,[['0','0'],['0','0']])),('false terminal amplitude bound',lambda x:x['terminal'][0].__setitem__('amplitude_bounds',['1','10001/10000']))]
neg=[]
for name,mutation in mutations:
    bad=copy.deepcopy(cert);mutation(bad)
    try: namespace['validate'](bad)
    except (AssertionError,ValueError,ZeroDivisionError) as e: neg.append({'mutation':name,'rejected':True,'reason':str(e)})
    else: raise AssertionError('Accepted damaged certificate: '+name)
assert neg==load(SUB/'data/CHECKER_NEGATIVE_CONTROLS.json')['controls']
report['negative_controls_replayed']=neg
# Algebra of the time-shifted inherited convergence bound: exact rational coefficients.
from fractions import Fraction as Q
assert Q('1.07701')*Q(1,4)**2/8==Q(107701,12800000)
assert Q(11,10)*Q(1,4)==Q(11,40)
assert Q(121,100)*Q(1,4)==Q(121,400)
report['time_shifted_bound_rational_coefficients_checked']=True
# Recheck that no evidence file was written by the replay.
for e in entries: assert record_file(SUB/e['path'])=={'bytes':e['bytes'],'sha256':e['sha256']}
report['submitted_files_unchanged_after_replay']=True
report['finished_utc']=datetime.now(timezone.utc).isoformat();report['status']='PASS'
(OUT/'AUDIT_AND_REPLAY.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['checker_replay','negative_controls_replayed']},indent=2))
print('Replay:',actual['status'],'50 links, 150 prestages; seconds=',elapsed)
print('Damaged-certificate controls rejected:',len(neg))
