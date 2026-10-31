"""Bounded packet/source intake. Never imports project code or old checkers."""
import datetime,hashlib,importlib.metadata,json,pathlib,platform,shutil,sys,zipfile
ROOT=pathlib.Path(__file__).resolve().parent
ZIP=pathlib.Path(r'C:\Users\Notandi\Downloads\NCM_PAPER_01_Codex_Packet_v0.1.zip')
ORDER=pathlib.Path(r'C:\Users\Notandi\Downloads\CODEX_NCM_COHERENCE_PAPER_WORK_ORDER_v0.1.txt')
REPO=ROOT.parent.parent/'trioctagon-physics'
FILES={'ORDER':ORDER,
 'DYNAMICS':REPO/'kernel_physics/dynamics.py',
 'OBSERVABLES':REPO/'papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex',
 'COHERENT':REPO/'papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex',
 'D1':REPO/'papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/manuscript.tex',
 'Z':REPO/'kernel_physics/z_manifold.py',
 'M3':REPO/'papers/PAPER_G/v0.1.1/source/paper_g.tex',
 'BRIDGE':REPO/'SRG_REDISCOVERY/FINAL_MATHEMATICAL_BRIDGE/publication/v0.1/SRG_FINAL_MATHEMATICAL_BRIDGE_v0.1.md'}
def fp(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def save(n,o):(ROOT/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def begin():
 assert not (ROOT/'SOURCE_MANIFEST.before.json').exists()
 for s in ('inputs','packet','evidence','logs','scratch','manuscript','proof_review','qa','mplconfig'):(ROOT/s).mkdir(exist_ok=True)
 vers={}
 for n in ('numpy','sympy','mpmath','reportlab','pymupdf','pypdf','matplotlib','Pillow'):
  try:vers[n]=importlib.metadata.version(n)
  except importlib.metadata.PackageNotFoundError:vers[n]=None
 data={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'environment':{'executable':sys.executable,'version':sys.version,'platform':platform.platform(),'packages':vers},
 'sources':{k:{'path':str(p),**fp(p.read_bytes())} for k,p in FILES.items()},
 'packet':{'path':str(ZIP),**fp(ZIP.read_bytes())},
 'tools':{n:shutil.which(n) for n in ('pdflatex','xelatex','lualatex','tectonic','latexmk','bibtex','pdftoppm','pdfinfo','node')}}
 save('SOURCE_MANIFEST.before.json',data)
 with (ROOT/'inputs'/ORDER.name).open('xb') as f:f.write(ORDER.read_bytes())
 members={}
 with zipfile.ZipFile(ZIP) as z:
  assert z.testzip() is None
  for info in z.infolist():
   name=pathlib.PurePosixPath(info.filename)
   assert not name.is_absolute() and '..' not in name.parts and ':' not in info.filename and '\\' not in info.filename
   assert (info.external_attr>>16)&0o170000!=0o120000
   target=ROOT/'packet'/name
   assert target.resolve().is_relative_to((ROOT/'packet').resolve())
   if info.is_dir():target.mkdir(parents=True,exist_ok=True);continue
   target.parent.mkdir(parents=True,exist_ok=True);b=z.read(info.filename)
   with target.open('xb') as f:f.write(b)
   members[info.filename]=fp(b)
 save('PACKET_MEMBERS.before.json',members)
 print(json.dumps({'environment':data['environment'],'tools':data['tools'],'packet':data['packet'],'members':list(members)},indent=2))
def read(key,start,end):
 p=FILES[key];lines=p.read_text(encoding='utf-8').splitlines()
 ledger=ROOT/'source_reads.json';rec=json.loads(ledger.read_text()) if ledger.exists() else []
 rec.append({'source':key,'first':start,'last':min(end,len(lines))});save(ledger.name,rec)
 for i in range(start-1,min(end,len(lines))):print(f'{i+1}: {lines[i]}')
if __name__=='__main__':
 if len(sys.argv)==1:begin()
 else:read(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
