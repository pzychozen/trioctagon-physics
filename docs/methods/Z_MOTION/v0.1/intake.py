from pathlib import Path,PurePosixPath
import json,hashlib,zipfile,sys,shutil,importlib.util,datetime
R=Path(__file__).resolve().parent;D=Path('C:/Users/Notandi/Downloads')
PACK=D/'NCM_Z_DOC_01_Codex_Packet_v0.1.zip';ORDER=D/'CODEX_NCM_Z_DOCUMENTATION_WORK_ORDER_v0.1.md'
def sha(b):return hashlib.sha256(b).hexdigest()
def meta(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
def dump(n,x):(R/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
with zipfile.ZipFile(PACK) as z:
 names=z.namelist();assert len(names)==len(set(names));assert z.testzip() is None
 for n in names:
  q=PurePosixPath(n);assert not q.is_absolute() and '..' not in q.parts and '\\' not in n and ':' not in n
  if n.endswith('/'):continue
  p=R/'packet'/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(n))
 print('\n'.join(names))
dump('SOURCE_MANIFEST_BEFORE.json',[meta(p) for p in [PACK,ORDER]])
dump('ENVIRONMENT.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.executable,'version':sys.version,'cwd':str(R),'shell':'cmd.exe','libraries':{m:bool(importlib.util.find_spec(m)) for m in ['reportlab','pypdf','pdfplumber','matplotlib','PIL','markdown_it','fitz']},'executables':{m:shutil.which(m) for m in ['pdftoppm','pdfinfo','pdflatex','xelatex','node']},'installed_anything':False})
print((R/'ENVIRONMENT.json').read_text())
