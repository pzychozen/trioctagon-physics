"""H6A Windows wheel/schema certification. No Historical scientific certification or attestation."""
import argparse
import base64
import csv
from email.parser import BytesParser
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile


def sha(raw):return hashlib.sha256(raw).hexdigest()
def save(path,value):path.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
def git(source,*args):return subprocess.check_output(['git','--no-optional-locks','-C',str(source),*args])
def run(log,args,cwd,env):
    result=subprocess.run([str(a) for a in args],cwd=cwd,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
    log.write_text(result.stdout+result.stderr,encoding='utf-8')
    if result.returncode:raise RuntimeError(log.name+' failed:\n'+(result.stdout+result.stderr)[-7000:])


def wheel_closure(wheel,copied):
    spec=importlib.util.spec_from_file_location('historical_source_audit',copied/'tools/check_imports.py')
    audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit)
    package=copied/'src/trioctagon_historical_protocol';audit.audit_package(package)
    stem='trioctagon_historical_protocol-0.1.0';meta=stem+'.dist-info/'
    expected={'trioctagon_historical_protocol/'+p.relative_to(package).as_posix():p for p in package.rglob('*') if p.is_file()}
    expected.update({meta+'licenses/'+name:copied/name for name in ('LICENSE','LICENSE_SCOPE.md')})
    generated={meta+name for name in ('METADATA','WHEEL','RECORD','top_level.txt')}
    with zipfile.ZipFile(wheel) as z:
        names=z.namelist();assert len(names)==len(set(names)) and set(names)==set(expected)|generated
        for name,path in expected.items():assert z.read(name)==path.read_bytes(),name
        m=BytesParser().parsebytes(z.read(meta+'METADATA'))
        assert (m['Name'],m['Version'])==('trioctagon-historical-protocol','0.1.0')
        assert m.get_all('Requires-Dist')==['trioctagon-analysis==0.1.1']
        assert set(m['Requires-Python'].split(','))=={'>=3.11','<3.12'}
        assert z.read(meta+'top_level.txt')==b'trioctagon_historical_protocol\n'
        rows=list(csv.reader(io.StringIO(z.read(meta+'RECORD').decode())))
        assert len(rows)==len(names) and {r[0] for r in rows}==set(names)
        for name,digest,size in rows:
            if name==meta+'RECORD':assert digest==size==''
            else:
                raw=z.read(name);assert int(size)==len(raw)
                assert digest=='sha256='+base64.urlsafe_b64encode(hashlib.sha256(raw).digest()).rstrip(b'=').decode()
        return [dict(path=name,bytes=len(z.read(name)),sha256=sha(z.read(name))) for name in sorted(names)]


def main():
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--workspace',type=Path,required=True)
    p.add_argument('--precommit',action='store_true');args=p.parse_args()
    source=args.source.resolve();work=args.workspace.resolve()
    assert not work.is_relative_to(source),'build workspace must be outside checkout'
    assert not (os.environ.get('GITHUB_ACTIONS') and args.precommit),'CI requires a committed source'
    work.mkdir(parents=True,exist_ok=False);evidence=work/'evidence';evidence.mkdir()
    status=git(source,'status','--porcelain','--untracked-files=all')
    if not args.precommit:assert not git(source,'status','--porcelain','--untracked-files=no').strip()
    if os.environ.get('GITHUB_ACTIONS'):assert not status.strip()
    head=git(source,'rev-parse','HEAD').decode().strip()
    tracked=git(source,'ls-files','-z').decode().split('\0')[:-1]
    tracked_hashes={name:sha((source/name).read_bytes()) for name in tracked}
    inputs={p.relative_to(source/'historical_protocol').as_posix():sha(p.read_bytes()) for p in (source/'historical_protocol').rglob('*') if p.is_file()}
    assert not any('__pycache__' in name or '.egg-info/' in name for name in inputs)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1',PYTEST_DISABLE_PLUGIN_AUTOLOAD='1',PIP_DISABLE_PIP_VERSION_CHECK='1')
    env.pop('PYTHONPATH',None);env.pop('PYTHONHOME',None)
    core=work/'core';tool=source/'analysis/tools/certify_distribution.py'
    run(evidence/'core-acquire.log',[sys.executable,'-I','-B',tool,'--acquire','--source',source,'--workspace',core],work,env)
    command=[sys.executable,'-I','-B',tool,'--certify','--source',source,'--workspace',core]
    if args.precommit:command.append('--precommit')
    run(evidence/'core-certification.log',command,work,env)
    lane=core/('candidate' if args.precommit else 'certified')
    build_python=lane/'build/Scripts/python.exe';runtime_python=lane/'runtime/Scripts/python.exe'
    core_result=json.loads((lane/'evidence/installed-result.json').read_bytes());assert core_result['status']=='PASS'
    copied=work/'historical-source';shutil.copytree(source/'historical_protocol',copied)
    tests=work/'tests';shutil.copytree(copied/'tests',tests)
    empty=work/'empty';empty.mkdir()
    env.update(PIP_NO_INDEX='1',SOURCE_DATE_EPOCH=git(source,'show','-s','--format=%ct',head).decode().strip())
    runner=copied/'tools/run_tests.py'
    common=['--tests',tests,'--evidence',evidence,'--checkout',source,'--core-golden',lane/'analysis-source/tests/fixtures/golden_vectors.json']
    run(evidence/'source-imports.log',[runtime_python,'-I','-B',copied/'tools/check_imports.py','--source',copied/'src','--out',evidence/'source-imports.json'],empty,env)
    run(evidence/'source-tests.log',[runtime_python,'-I','-B',runner,*common,'--lane','source','--source',copied/'src'],empty,env)
    wheels=evidence/'wheel';wheels.mkdir()
    run(evidence/'build.log',[build_python,'-I','-B','-m','pip','wheel','--no-index','--no-deps','--no-build-isolation','--wheel-dir',wheels,copied],work,env)
    wheel=wheels/'trioctagon_historical_protocol-0.1.0-py3-none-any.whl'
    assert set(wheels.iterdir())=={wheel};members=wheel_closure(wheel,copied);save(evidence/'member-manifest.json',members)
    run(evidence/'install.log',[runtime_python,'-I','-B','-m','pip','install','--no-index','--no-deps','--no-compile',wheel],work,env)
    run(evidence/'pip-check.log',[runtime_python,'-I','-B','-m','pip','check'],work,env)
    run(evidence/'installed-imports.log',[runtime_python,'-I','-B',copied/'tools/check_imports.py','--out',evidence/'installed-imports.json'],empty,env)
    run(evidence/'installed-tests.log',[runtime_python,'-I','-B',runner,*common,'--lane','installed','--wheel',wheel],empty,env)
    assert git(source,'status','--porcelain','--untracked-files=all')==status
    assert {name:sha((source/name).read_bytes()) for name in tracked}==tracked_hashes
    assert {p.relative_to(source/'historical_protocol').as_posix():sha(p.read_bytes()) for p in (source/'historical_protocol').rglob('*') if p.is_file()}==inputs
    run(evidence/'diff-check.log',['git','--no-optional-locks','-C',source,'diff','--check'],work,env)
    run(evidence/'staged-diff-check.log',['git','--no-optional-locks','-C',source,'diff','--cached','--check'],work,env)
    result=dict(status='PASS',qualification='SCHEMA_PACKAGE_ONLY_NO_HISTORICAL_MATHEMATICS_NO_B2_ATTESTATION',
        precommit=args.precommit,source_head=head,source_tree=git(source,'rev-parse','HEAD^{tree}').decode().strip(),
        source_content_sha256=sha(json.dumps(inputs,sort_keys=True,separators=(',',':')).encode()),inputs=inputs,
        wheel=dict(filename=wheel.name,sha256=sha(wheel.read_bytes())),
        source_tests=json.loads((evidence/'source-result.json').read_bytes())['counts'],
        installed_tests=json.loads((evidence/'installed-result.json').read_bytes())['counts'],core_tests=core_result['counts'],
        core_certification_sha256=sha((lane/'evidence/certification.json').read_bytes()),
        source_preserved=True,scientific_imports=False,real_admission=False,issuer_present=False)
    save(evidence/'certification.json',result)
    print(json.dumps({key:value for key,value in result.items() if key!='inputs'},indent=2))

if __name__=='__main__':main()
