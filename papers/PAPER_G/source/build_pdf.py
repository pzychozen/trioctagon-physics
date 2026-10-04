"""Offline multi-file LaTeX build, with all build scratch outside the repository.
Set PAPER_G_TECTONIC and PAPER_G_TEX_CACHE to installed tool and existing cache.
Output remains external until explicitly copied after review.
"""
from pathlib import Path
import argparse, hashlib, json, os, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--workspace',type=Path,required=True);a=p.parse_args();work=a.workspace.resolve()
 repo=next((p for p in ROOT.parents if (p/'.git').exists()),ROOT)
 if work==repo or repo in work.parents:raise ValueError('Use external build scratch')
 work.mkdir(parents=True,exist_ok=False)
 stage=work/'source';stage.mkdir();shutil.copyfile(ROOT/'source/paper_g.tex',stage/'paper_g.tex');shutil.copytree(ROOT/'figures',work/'figures')
 tool=Path(os.environ['PAPER_G_TECTONIC']).resolve();cache=Path(os.environ['PAPER_G_TEX_CACHE']).resolve()
 if cache==repo or repo in cache.parents:raise ValueError('Copy TeX cache outside repository first')
 fc=work/'fontconfig.xml';fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>'+os.environ.get('PAPER_G_FONTS','C:/Windows/Fonts')+'</dir><cachedir>'+(work/'font-cache').as_posix()+'</cachedir></fontconfig>')
 env=os.environ.copy();env.update(TECTONIC_CACHE_DIR=str(cache),FONTCONFIG_FILE=str(fc),SOURCE_DATE_EPOCH='1791072000')
 result=subprocess.run([str(tool),'-X','compile','--only-cached','--keep-logs','--keep-intermediates','--outdir',str(work),str(stage/'paper_g.tex')],cwd=stage,env=env,capture_output=True)
 (work/'console.log').write_bytes(result.stdout+result.stderr)
 if result.returncode:print((result.stdout+result.stderr).decode(errors='replace'));raise SystemExit(result.returncode)
 log=(work/'paper_g.log').read_text(errors='replace');warnings=[s for s in log.splitlines() if any(t in s for t in ('Warning','Overfull','Missing character'))]
 sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 record={'status':'BUILT_PENDING_VISUAL_REVIEW','pdf_sha256':sha(work/'paper_g.pdf'),'tex_sha256':sha(stage/'paper_g.tex'),'tectonic_sha256':sha(tool),'tectonic_version':subprocess.check_output([str(tool),'--version']).decode().strip(),'python':sys.version,'offline':True,'warnings':warnings,'figures':{p.name:sha(p) for p in (ROOT/'figures').glob('*.pdf')}}
 (work/'build_record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
if __name__=='__main__':main()
