"""Document-only build using an existing cached Tectonic executable."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent;NAME='TRIOCTAGON_OUTER_ENVELOPE_COMPANION_v0.1.pdf'
p=argparse.ArgumentParser();p.add_argument('--tectonic',required=True);p.add_argument('--build-dir',required=True);args=p.parse_args()
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment' and not sys.flags.optimize
B=Path(args.build_dir).resolve();assert not B.is_relative_to(ROOT),'Use external intermediates';B.mkdir(parents=True,exist_ok=True)
for n in ['tmp','fontcache']:(B/n).mkdir(exist_ok=True)
epoch=str(int(datetime(2026,11,14,tzinfo=timezone.utc).timestamp()));env={**os.environ,'SOURCE_DATE_EPOCH':epoch,'TMP':str(B/'tmp'),'TEMP':str(B/'tmp')}
if os.name=='nt':
    fonts=Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts';(B/'fonts.conf').write_text('<?xml version="1.0"?><fontconfig><dir>'+fonts.as_posix()+'</dir><cachedir>'+(B/'fontcache').as_posix()+'</cachedir></fontconfig>',encoding='utf-8');env.update(FONTCONFIG_FILE=str(B/'fonts.conf'),FONTCONFIG_PATH=str(B))
cmd=[args.tectonic,'--only-cached','--untrusted','--keep-logs','--keep-intermediates','--outdir',str(B),'main.tex'];version=subprocess.run([args.tectonic,'--version'],capture_output=True,check=True).stdout.decode().strip();start=datetime.now(timezone.utc).isoformat()
q=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,timeout=240);(B/'compiler.stdout').write_bytes(q.stdout);(B/'compiler.stderr').write_bytes(q.stderr)
sources=[ROOT/'main.tex',ROOT/'references.tex',*sorted((ROOT/'tables').glob('*.tex')),*sorted((ROOT/'figures').glob('local_facet_transition.*'))]
rec={'started_utc':start,'finished_utc':datetime.now(timezone.utc).isoformat(),'client_date':datetime.now(timezone.utc).date().isoformat(),'status':'Project-internal manuscript review complete; author-authorized for repository publication.','command':cmd,'cwd':str(ROOT),'compiler_version':version,'exit_status':q.returncode,'source_date_epoch':epoch,'python':sys.executable,'python_version':sys.version,'conda_environment':os.environ['CONDA_DEFAULT_ENV'],'raw_source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},'build_helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'new_scientific_runs':0,'protection':'Existing cached compiler, --only-cached --untrusted, external intermediates; no package download or global configuration change.'}
if q.returncode==0:
    shutil.copyfile(B/'main.pdf',ROOT/NAME);rec.update(pdf_sha256=hashlib.sha256((ROOT/NAME).read_bytes()).hexdigest(),pdf_bytes=(ROOT/NAME).stat().st_size)
(B/'BUILD_RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8');print((q.stdout+q.stderr).decode(errors='replace'));sys.exit(q.returncode)
