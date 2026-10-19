"""Offline manuscript build using an existing compiler/cache; no installation."""
from pathlib import Path
import os,sys,subprocess,hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1];os.chdir(ROOT)
build=ROOT/'build';cache=ROOT/'cache';build.mkdir(exist_ok=True);cache.mkdir(exist_ok=True)
exe=os.environ.get('PAPER_II_TECTONIC') or shutil.which('tectonic')
if not exe:raise SystemExit('Set PAPER_II_TECTONIC to an existing compiler.')
source=os.environ.get('PAPER_II_TEX_CACHE');local=cache/'tectonic'
if source and Path(source).resolve()!=local.resolve():
 def long(p):return '\\\\?\\'+str(Path(p).resolve()) if os.name=='nt' else str(p)
 shutil.copytree(long(source),long(local),dirs_exist_ok=True)
if not local.exists():raise SystemExit('Set PAPER_II_TEX_CACHE to an existing populated offline cache.')
env=dict(os.environ,TECTONIC_CACHE_DIR=str(local),XDG_CACHE_HOME=str(cache),TEMP=str(cache),TMP=str(cache),SOURCE_DATE_EPOCH='1792368000')
if os.name=='nt':
 fc=cache/'fonts.conf';fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>'+Path(os.environ.get('WINDIR','C:/Windows')).as_posix()+'/Fonts</dir><cachedir>'+(cache/'fonts').as_posix()+'</cachedir></fontconfig>');env['FONTCONFIG_FILE']=str(fc)
n=len(list(build.glob('console_*.log')))+1
args=[str(exe),'--only-cached','--untrusted','--keep-logs','--keep-intermediates','--synctex','--outdir',str(build),'manuscript.tex']
r=subprocess.run(args,env=env,capture_output=True);(build/f'console_{n:03d}.log').write_bytes(r.stdout+r.stderr)
record={'command':args,'returncode':r.returncode,'python':sys.version,'compiler':subprocess.check_output([exe,'--version']).decode().strip(),'compiler_sha256':hashlib.sha256(Path(exe).read_bytes()).hexdigest(),'only_cached':True,'source_date_epoch':env['SOURCE_DATE_EPOCH']}
(build/f'build_record_{n:03d}.json').write_text(json.dumps(record,indent=2))
print((r.stdout+r.stderr).decode('utf8',errors='replace')[-7000:])
if r.returncode:raise SystemExit(r.returncode)
shutil.copyfile(build/'manuscript.pdf',ROOT/'PAPER_II_PAIRED_DRIVING_EXTERIOR_IDENTIFIABILITY_v0.1.pdf')
