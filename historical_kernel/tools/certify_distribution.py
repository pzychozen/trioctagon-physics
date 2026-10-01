"""Exact-source Windows certification, independent environments and external admission evidence."""
import argparse,base64,csv,hashlib,io,json,os,shutil,subprocess,sys,zipfile
from email.parser import BytesParser
from pathlib import Path

H6A_SHA='734ae5d2734ce9b42301b851e23d57c4b9db37ac02b32b0fadff328d4724952f'
CORE_SHA='7fcba927068e8762b02fa7717c2bb30f8ba61ed9aa70b674f3006b10eee194d6'
ARTIFACT_SHA='6be5b7fc97bf3b3612a2d1dabfd7b813f829ff6b5e6888927082c69b2ae53d17'


def sha(raw):return hashlib.sha256(raw).hexdigest()
def save(path,value):path.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
def git(source,*args):return subprocess.check_output(['git','--no-optional-locks','-C',str(source),*args])
def run(log,command,cwd,env):
    result=subprocess.run([str(x) for x in command],cwd=cwd,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
    log.write_text(result.stdout+result.stderr,encoding='utf-8')
    if result.returncode:raise RuntimeError(log.name+' failed:\n'+(result.stdout+result.stderr)[-7000:])


def wheel_closure(wheel,copied):
    package=copied/'src/trioctagon_historical_kernel';stem='trioctagon_historical_kernel-0.1.0';meta=stem+'.dist-info/'
    expected={'trioctagon_historical_kernel/'+p.name:p for p in package.glob('*.py')}
    expected.update({meta+'licenses/'+n:copied/n for n in ('LICENSE','LICENSE_SCOPE.md')})
    generated={meta+n for n in ('METADATA','WHEEL','RECORD','top_level.txt')}
    with zipfile.ZipFile(wheel) as z:
        names=z.namelist();assert len(names)==len(set(names)) and set(names)==set(expected)|generated
        for name,path in expected.items():assert z.read(name)==path.read_bytes(),name
        m=BytesParser().parsebytes(z.read(meta+'METADATA'))
        assert (m['Name'],m['Version'])==('trioctagon-historical-kernel','0.1.0')
        assert m.get_all('Requires-Dist')==['numpy==2.4.4','trioctagon-historical-protocol==0.1.0']
        assert set(m['Requires-Python'].split(','))=={'>=3.11','<3.12'}
        assert z.read(meta+'top_level.txt')==b'trioctagon_historical_kernel\n'
        rows=list(csv.reader(io.StringIO(z.read(meta+'RECORD').decode())))
        assert len(rows)==len(names) and {r[0] for r in rows}==set(names)
        for name,digest,size in rows:
            if name==meta+'RECORD':assert digest==size==''
            else:
                raw=z.read(name);assert int(size)==len(raw)
                assert digest=='sha256='+base64.urlsafe_b64encode(hashlib.sha256(raw).digest()).rstrip(b'=').decode()
        return [dict(path=n,bytes=len(z.read(n)),sha256=sha(z.read(n))) for n in sorted(names)]


def main():
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--workspace',type=Path,required=True)
    p.add_argument('--precommit',action='store_true');a=p.parse_args();source=a.source.resolve();work=a.workspace.resolve()
    assert not work.is_relative_to(source) and not (os.environ.get('GITHUB_ACTIONS') and a.precommit)
    work.mkdir(parents=True,exist_ok=False);e=work/'evidence';e.mkdir();empty=work/'empty';empty.mkdir()
    head=git(source,'rev-parse','HEAD').decode().strip();status=git(source,'status','--porcelain','--untracked-files=all')
    if not a.precommit:assert not git(source,'status','--porcelain','--untracked-files=no').strip()
    if os.environ.get('GITHUB_ACTIONS'):assert not status.strip()
    tracked=git(source,'ls-files','-z').decode().split('\0')[:-1]
    tracked_hashes={n:sha((source/n).read_bytes()) for n in tracked}
    inputs={p.relative_to(source/'historical_kernel').as_posix():sha(p.read_bytes()) for p in (source/'historical_kernel').rglob('*') if p.is_file()}
    assert not any('__pycache__' in n or '.egg-info/' in n for n in inputs)
    save(e/'source-inputs.json',dict(head=head,revision=None if a.precommit else head,files=inputs))
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTEST_DISABLE_PLUGIN_AUTOLOAD='1',PIP_DISABLE_PIP_VERSION_CHECK='1')
    env.pop('PYTHONPATH',None);env.pop('PYTHONHOME',None)
    core=work/'core';tool=source/'analysis/tools/certify_distribution.py'
    run(e/'core-acquire.log',[sys.executable,'-I','-B',tool,'--acquire','--source',source,'--workspace',core],work,env)
    command=[sys.executable,'-I','-B',tool,'--certify','--source',source,'--workspace',core]
    if a.precommit:command.append('--precommit')
    run(e/'core-certification.log',command,work,env)
    lane=core/('candidate' if a.precommit else 'certified')
    core_result=json.loads((lane/'evidence/installed-result.json').read_bytes());assert core_result['status']=='PASS'
    acquired=work/'accepted';acquired.mkdir()
    raw=subprocess.check_output(['gh','api','repos/pzychozen/trioctagon-physics/actions/artifacts/11136252097/zip'])
    assert sha(raw)==ARTIFACT_SHA
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for path,digest in [('evidence/wheel/trioctagon_historical_protocol-0.1.0-py3-none-any.whl',H6A_SHA),
                            ('core/certified/evidence/wheel/trioctagon_analysis-0.1.1-py3-none-any.whl',CORE_SHA)]:
            data=z.read(path);assert sha(data)==digest;(acquired/Path(path).name).write_bytes(data)
    save(e/'accepted-dependencies.json',dict(h6a_wheel_sha256=H6A_SHA,analysis_wheel_sha256=CORE_SHA,artifact_zip_sha256=ARTIFACT_SHA))
    runtime=work/'historical-runtime';run(e/'venv.log',[sys.executable,'-I','-B','-m','venv',runtime],work,env)
    python=runtime/'Scripts/python.exe';env['PIP_NO_INDEX']='1'
    dependencies=[p for p in (core/'dependencies').glob('*.whl') if p.name.split('-')[0].lower() not in ('sympy','mpmath','setuptools','wheel')]
    run(e/'dependencies.log',[python,'-I','-B','-m','pip','install','--no-index','--no-deps','--no-compile',*dependencies,*acquired.glob('*.whl')],work,env)
    protocol=work/'protocol';shutil.copytree(source/'historical_protocol',protocol)
    protocol_e=e/'protocol';protocol_e.mkdir()
    run(e/'protocol-regressions.log',[python,'-I','-B',protocol/'tools/run_tests.py','--tests',protocol/'tests','--evidence',protocol_e,
        '--lane','installed','--checkout',source,'--wheel',acquired/'trioctagon_historical_protocol-0.1.0-py3-none-any.whl',
        '--core-golden',lane/'analysis-source/tests/fixtures/golden_vectors.json'],empty,env)
    copied=work/'historical-source';shutil.copytree(source/'historical_kernel',copied)
    tests=copied/'tests';runner=copied/'tools/run_tests.py'
    common=['--tests',tests,'--out',e,'--checkout',source]
    run(e/'source-tests.log',[python,'-I','-B',runner,*common,'--lane','source','--source',copied/'src'],empty,env)
    wheels=e/'wheel';wheels.mkdir();env['SOURCE_DATE_EPOCH']=git(source,'show','-s','--format=%ct',head).decode().strip()
    run(e/'build.log',[lane/'build/Scripts/python.exe','-I','-B','-m','pip','wheel','--no-index','--no-deps','--no-build-isolation',
        '--wheel-dir',wheels,copied],work,env)
    wheel=wheels/'trioctagon_historical_kernel-0.1.0-py3-none-any.whl';save(e/'wheel-members.json',wheel_closure(wheel,copied))
    run(e/'install.log',[python,'-I','-B','-m','pip','install','--no-index','--no-deps','--no-compile',wheel],work,env)
    run(e/'pip-check.log',[python,'-I','-B','-m','pip','check'],work,env)
    run(e/'installed-tests.log',[python,'-I','-B',runner,*common,'--lane','installed','--wheel',wheel],empty,env)
    run(e/'removal-control.log',[python,'-I','-B',copied/'tools/negative_control.py','--tests',tests,'--out',e],empty,env)
    fixture=tests/'fixtures/h2_applicable.json'
    run(e/'historical-export.log',[python,'-I','-B',copied/'tools/export_historical.py','--fixtures',fixture,'--out',e/'historical-export.json'],empty,env)
    run(e/'current-export.log',[lane/'runtime/Scripts/python.exe','-I','-B',copied/'tools/export_current.py','--fixtures',fixture,'--out',e/'current-export.json'],empty,env)
    with zipfile.ZipFile(core/'trioctagon_physics-0.1.0-py3-none-any.whl') as z:
        binding=[]
        for name in ('dynamics.py','z_manifold.py','readouts.py','_response_numeric.py'):
            raw=z.read('kernel_physics/'+name);assert raw==(source/'kernel_physics'/name).read_bytes()
            binding.append(dict(file=name,sha256=sha(raw)))
    save(e/'current-comparison-binding.json',dict(role='COMPARISON_REFERENCE_ONLY',source_head=head,scientific_members=binding))
    run(e/'comparison.log',[python,'-I','-B',copied/'tools/compare_exports.py','--historical',e/'historical-export.json',
        '--current',e/'current-export.json','--out',e/'external-comparison.json'],empty,env)
    run(e/'measurement.log',[python,'-I','-B',copied/'tools/measure.py','--tests',tests,'--wheel',wheel,'--out',e/'measurement'],empty,env)
    run(e/'admission.log',[python,'-I','-B',copied/'tools/admit.py','--evidence',e,'--source',copied,'--tests',tests,'--wheel',wheel],empty,env)
    assert git(source,'status','--porcelain','--untracked-files=all')==status
    assert {n:sha((source/n).read_bytes()) for n in tracked}==tracked_hashes
    assert {p.relative_to(source/'historical_kernel').as_posix():sha(p.read_bytes()) for p in (source/'historical_kernel').rglob('*') if p.is_file()}==inputs
    run(e/'diff-check.log',['git','--no-optional-locks','-C',source,'diff','--check'],work,env)
    result=dict(status='PASS',source_head=head,precommit=a.precommit,wheel=dict(filename=wheel.name,sha256=sha(wheel.read_bytes())),
        source_tests=json.loads((e/'source-result.json').read_bytes())['counts'],installed_tests=json.loads((e/'installed-result.json').read_bytes())['counts'],
        protocol_tests=json.loads((protocol_e/'installed-result.json').read_bytes())['counts'],core_tests=core_result['counts'],
        admission=json.loads((e/'local-admission-result.json').read_bytes()),source_preserved=True,
        windows_execution_binding='NOT_PROVEN',production_attestation_enabled=False)
    save(e/'certification.json',result);print(json.dumps(result,indent=2))

if __name__=='__main__':main()
