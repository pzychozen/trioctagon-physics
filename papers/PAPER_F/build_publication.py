"""Isolated Markdown->AST->TeX->PDF build. No scientific input is rewritten."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,re,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument("workspace",type=Path);args=p.parse_args()
WORK=args.workspace.resolve()
assert not WORK.exists(),"Use a fresh isolated build directory"
WORK.mkdir(parents=True);STAGE=WORK/"source";STAGE.mkdir()
for name in ["PAPER_F_PUBLICATION_v0.2.md","publication_style.tex"]:
 shutil.copyfile(ROOT/name,STAGE/name)
shutil.copytree(ROOT/"figures",STAGE/"figures")
PANDOC=Path(os.environ["PAPER_F_PANDOC"]).resolve();TECTONIC=Path(os.environ["PAPER_F_TECTONIC"]).resolve()
CACHE=Path(os.environ["PAPER_F_TEX_CACHE"]).resolve()
def run(a):return subprocess.run([str(x) for x in a],check=True,capture_output=True,cwd=STAGE)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(v,t):
 if isinstance(v,dict):
  if v.get("t")==t:yield v
  for x in v.values():yield from nodes(x,t)
 elif isinstance(v,list):
  for x in v:yield from nodes(x,t)
md=STAGE/"PAPER_F_PUBLICATION_v0.2.md"
fmt="markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables+raw_tex-smart"
ast=json.loads(run([PANDOC,md,"--from="+fmt,"--to=json"]).stdout)
maths=[n for n in nodes(ast,"Math") if n["c"][0]["t"]=="DisplayMath"]
assert len(maths)==106,len(maths)
mathmap=[]
for i,n in enumerate(maths):
 raw=n["c"][1];tag=re.search(r"\\tag\{([^}]+)\}",raw)
 body=re.sub(r"\\tag\{[^}]+\}","",raw).strip()
 rendered=body
 # Presentation-only line breaks, declared separately and token-audited below.
 layouts=json.loads((ROOT/"equation_layouts.json").read_text()) if (ROOT/"equation_layouts.json").exists() else {}
 if str(i+1) in layouts:
  item=layouts[str(i+1)];assert item["original"]==body
  rendered=item["rendered"]
 mathmap.append({"ordinal":i+1,"tag":tag.group(1) if tag else None,"body":body,"rendered_body":rendered,"layout_only":rendered!=body})
 n.clear();n.update({"t":"RawInline","c":["latex",r"\paperdisplay["+(tag.group(1) if tag else "")+"]{"+rendered+"}"]})
astpath=WORK/"manuscript_ast.json";astpath.write_text(json.dumps(ast,ensure_ascii=False),encoding="utf-8")
tex=STAGE/"paper_F_v0.2.tex"
run([PANDOC,astpath,"--from=json","--to=latex","--standalone","--shift-heading-level-by=-1",
 "--include-in-header="+str(STAGE/"publication_style.tex"),"--variable=documentclass:article","--variable=fontsize:11pt",
 "--variable=papersize:a4","--variable=geometry:margin=23mm",
 "--variable=mainfont:texgyrepagella-regular.otf","--variable=mainfontoptions:BoldFont=texgyrepagella-bold.otf,ItalicFont=texgyrepagella-italic.otf,BoldItalicFont=texgyrepagella-bolditalic.otf",
 "--variable=mathfont:texgyrepagella-math.otf","--variable=monofont:lmmono10-regular.otf",
 "--variable=colorlinks:true","--variable=linkcolor:MidnightBlue","--variable=urlcolor:MidnightBlue",
 "--wrap=preserve","--output="+str(tex)])
fc=WORK/"fontconfig.xml"
fontdir=os.environ.get("PAPER_F_SYSTEM_FONTS","C:/Windows/Fonts")
fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>'+fontdir+'</dir><cachedir>'+str(WORK/"fontconfig-cache").replace("\\","/")+'</cachedir></fontconfig>')
env=os.environ.copy();env["TECTONIC_CACHE_DIR"]=str(CACHE);env["FONTCONFIG_FILE"]=str(fc)
env["SOURCE_DATE_EPOCH"]=str(int(datetime.datetime(2026,9,25,tzinfo=datetime.timezone.utc).timestamp()))
buildargs=[str(TECTONIC),"-X","compile","--only-cached","--keep-logs","--keep-intermediates","--outdir",str(WORK),str(tex)]
result=subprocess.run(buildargs,cwd=STAGE,env=env,capture_output=True)
(ROOT/"records/build_console.log").write_bytes(result.stdout+result.stderr)
if result.returncode:print((result.stdout+result.stderr).decode(errors="replace")[-6000:]);raise SystemExit(result.returncode)
pdf=ROOT/"PAPER_F_PUBLICATION_v0.2.pdf"
shutil.copyfile(WORK/"paper_F_v0.2.pdf",pdf);shutil.copyfile(WORK/"paper_F_v0.2.log",ROOT/"records/latex_build.log");shutil.copyfile(tex,ROOT/tex.name)
record={"workspace":str(WORK),"isolated_build":True,"network_in_tex_build":False,"source_date_epoch":env["SOURCE_DATE_EPOCH"],
 "python":sys.version,"pandoc":run([PANDOC,"--version"]).stdout.decode().splitlines()[0],"tectonic":run([TECTONIC,"--version"]).stdout.decode().strip(),
 "pandoc_sha256":digest(PANDOC),"tectonic_sha256":digest(TECTONIC),"source_sha256":digest(md),"tex_sha256":digest(tex),"pdf_sha256":digest(pdf),
 "command":buildargs,"pandoc_reader":fmt,"exit_code":result.returncode,"display_blocks":len(maths),
 "inline_math_count":sum(n["c"][0]["t"]=="InlineMath" for n in nodes(ast,"Math")),"equation_conversion":mathmap}
(ROOT/"records/build_record.json").write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
assert all(x["rendered_body"] in tex.read_text(encoding="utf-8") for x in mathmap)
print(json.dumps({k:v for k,v in record.items() if k not in ("equation_conversion","command")},indent=2))
