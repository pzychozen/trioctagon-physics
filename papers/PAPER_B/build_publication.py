"""Markdown -> Pandoc AST -> TeX -> Tectonic PDF; all writes inside Paper B."""
from pathlib import Path
import copy,datetime,hashlib,json,os,re,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent
BUILD=ROOT/".build";BUILD.mkdir(exist_ok=True)
from publication_runtime import CONFIG, EVIDENCE, PUBLICATION
PUB=PUBLICATION;PUB.mkdir(parents=True,exist_ok=True)
EVIDENCE.mkdir(parents=True,exist_ok=True)
def tool(name,variable):
    value=os.environ.get(variable) or shutil.which(name)
    if not value or not Path(value).is_file():
        raise RuntimeError("Provide existing "+name+" through PATH or "+variable)
    return Path(value).resolve()
PANDOC=tool("pandoc","PAPER_B_PANDOC")
TECTONIC=tool("tectonic","PAPER_B_TECTONIC")
cache_path=os.environ.get("PAPER_B_TEX_CACHE")
if not cache_path or not Path(cache_path).is_dir():
    raise RuntimeError("Set PAPER_B_TEX_CACHE to an existing populated Tectonic resource cache. No download or installation is performed.")
CACHE=Path(cache_path).resolve()
MD=ROOT/CONFIG["manuscript"]
PDF=PUB/CONFIG["pdf_name"]
def run(a,**kw):return subprocess.run([str(x) for x in a],check=True,capture_output=True,**kw)
def nodes(v,t):
    if isinstance(v,dict):
        if v.get("t")==t:yield v
        for x in v.values():yield from nodes(x,t)
    elif isinstance(v,list):
        for x in v:yield from nodes(x,t)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
fmt="markdown+tex_math_dollars+pipe_tables+raw_tex+lists_without_preceding_blankline-smart"
ast=json.loads(run([PANDOC,MD,"--from",fmt,"--to=json"]).stdout)
original=copy.deepcopy(ast)
maths=[n for n in nodes(ast,"Math") if n["c"][0]["t"]=="DisplayMath"]
equations=[]
for n in maths:
    raw=n["c"][1]
    tag=re.search(r"\\tag\{([^}]+)\}",raw)
    body=re.sub(r"\\tag\{[^}]+\}","",raw).strip()
    label=tag.group(1) if tag else ""
    equations.append({"label":label,"math":body})
    n.clear();n.update({"t":"RawInline","c":["latex",r"\paperdisplay["+label+"]{"+body+"}"]})
# Only display wrappers change. No prose, citations, tables or proof blocks are omitted.
ast_path=BUILD/"publication_ast.json"
ast_path.write_text(json.dumps(ast,ensure_ascii=False,indent=2),encoding="utf8")
TEX=ROOT/"paper_B_final.tex"
args=[PANDOC,ast_path,"--from=json","--to=latex","--standalone",
 "--include-in-header="+str(ROOT/"publication_style.tex"),"--variable=documentclass:article",
 "--variable=fontsize:11pt","--variable=papersize:a4","--variable=geometry:margin=24mm",
 "--variable=mainfont:texgyrepagella-regular.otf",
 "--variable=mainfontoptions:BoldFont=texgyrepagella-bold.otf,ItalicFont=texgyrepagella-italic.otf,BoldItalicFont=texgyrepagella-bolditalic.otf",
 "--variable=mathfont:texgyrepagella-math.otf","--variable=monofont:lmmono10-regular.otf",
 "--variable=monofontoptions:BoldFont=lmmonolt10-bold.otf","--variable=colorlinks:true",
 "--variable=linkcolor:MidnightBlue","--variable=urlcolor:MidnightBlue",
 "--wrap=preserve","--output="+str(TEX)]
run(args)
fontconfig=BUILD/"fontconfig.xml"
fontconfig.write_text('<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig><dir>C:/Windows/Fonts</dir><cachedir>'+str(BUILD/"fontconfig-cache").replace("\\","/")+'</cachedir></fontconfig>\n',encoding="utf8")
env=os.environ.copy()
env["TECTONIC_CACHE_DIR"]=str(CACHE);env["FONTCONFIG_FILE"]=str(fontconfig)
env["SOURCE_DATE_EPOCH"]=str(int(datetime.datetime(2026,9,23,tzinfo=datetime.timezone.utc).timestamp()))
with (PUB/"build_console.log").open("wb") as log:
    r=subprocess.run([str(TECTONIC),"-X","compile","--only-cached","--keep-logs",
       "--keep-intermediates","--outdir",str(BUILD),str(TEX)],cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT)
if r.returncode:
    print((PUB/"build_console.log").read_text(encoding="utf8",errors="replace")[-6000:])
    raise SystemExit(r.returncode)
shutil.copyfile(BUILD/"paper_B_final.pdf",PDF)
shutil.copyfile(BUILD/"paper_B_final.log",PUB/"paper_B_final.log")
version={"python":sys.version,"pandoc":run([PANDOC,"--version"]).stdout.decode().splitlines()[0],
 "tectonic":run([TECTONIC,"--version"]).stdout.decode().strip(),"pandoc_sha256":digest(PANDOC),
 "tectonic_sha256":digest(TECTONIC),"source_date_epoch":env["SOURCE_DATE_EPOCH"],
 "cache":"explicit pre-existing tool resource cache; --only-cached; no scientific archive fallback",
 "pdf_sha256":digest(PDF),"manuscript_sha256":digest(MD),"tex_sha256":digest(TEX)}
(PUB/"build_record.json").write_text(json.dumps(version,indent=2)+"\n",encoding="utf8")
fidelity={"display_equation_blocks":len(maths),"equation_labels":[x["label"] for x in equations],
 "figures":len(list(nodes(original,"Image"))),"omitted_scientific_nodes":0,
 "transformation":"Only display-math wrappers replaced by measured paperdisplay; original math body preserved.",
 "source_sha256":digest(MD)}
(EVIDENCE/"structural_fidelity.json").write_text(json.dumps(fidelity,indent=2)+"\n",encoding="utf8")
print(json.dumps({**version,**fidelity},indent=2))
