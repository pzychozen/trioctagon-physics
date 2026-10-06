"""Inventory immutable inputs and assemble retained evidence; never run old writers."""
from pathlib import Path
import os,sys,json,hashlib,subprocess
sys.dont_write_bytecode=True
LANE=Path(__file__).resolve().parents[1]
REPO=LANE.parents[1]
RESEARCH=REPO.parent/'research'
NAMES={'GR0':'GR0_native_gravity_20261006','GR1':'GR1_unequal_response_20261006',
       'GR2':'GR2_spectral_response_20261006','CM0':'CM0_native_core_kinematics_20261006',
       'SA0':'SA0_native_state_shell_attachment_20261006'}
COUNTS=dict(GR0=45,GR1=38,GR2=42,CM0=78,SA0=226)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args],env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')).decode('utf-8')
def protected_state():
 files={};size=0
 for root,dirs,names in os.walk(REPO):
  dirs[:]=sorted(d for d in dirs if d!='.git' and Path(root)/d!=LANE)
  for name in sorted(names):
   p=Path(root)/name
   if p.is_file():files[p.relative_to(REPO).as_posix()]=sha(p);size+=p.stat().st_size
 return dict(head=git('rev-parse','HEAD').strip(),branch=git('branch','--show-current').strip(),
  status_excluding_lane='\n'.join(x for x in git('status','--short').splitlines() if 'papers/NATIVE_RESPONSE_GEOMETRY/' not in x),
  index_sha256=hashlib.sha256(git('ls-files','--stage','-z').encode()).hexdigest(),files=len(files),bytes=size,
  inventory_sha256=hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest())
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def assemble():
 for sub in ['manuscript','publication','figures','verification','provenance']: (LANE/sub).mkdir(exist_ok=True)
 baseline=LANE/'provenance/baseline.json'
 if not baseline.exists():save(baseline,protected_state())
 manifest={}; evidence={}; predicates={}
 for key,folder in NAMES.items():
  directory=RESEARCH/folder
  paths=sorted(directory.glob('*'))
  manifest[key]={'directory':str(directory),'artifacts':[{'name':p.name,'sha256':sha(p),'bytes':p.stat().st_size} for p in paths if p.is_file()]}
  result=next(directory.glob('*results.json'));v=json.loads(result.read_text(encoding='utf-8'))['verification']
  checks=v.get('symbolic_checks',v.get('exact_checks',v.get('exact_predicates')))
  if isinstance(checks,int):checks=v['exact_checks']
  names=[c['name'] if isinstance(c,dict) else c for c in checks]
  assert len(names)==COUNTS[key]
  predicates[key]=[{'ordinal':i+1,'name':n} for i,n in enumerate(names)]
  evidence[key]={'source_results':result.name,'source_sha256':sha(result),'retained_not_rerun':True,'verification':v}
 manifest['scientific_source_head']=git('rev-parse','HEAD').strip()
 manifest['native_sources']=[{'path':str(p.relative_to(REPO)),'sha256':sha(p)} for p in sorted((REPO/'kernel_physics').glob('*.py'))]
 save(LANE/'provenance/source_manifest.json',manifest)
 save(LANE/'verification/retained_evidence.json',evidence)
 save(LANE/'verification/retained_predicates.json',{'counts':COUNTS,'total':sum(COUNTS.values()),'qualification':'Heterogeneous retained symbolic/source checks, not 429 theorems; no predecessor scripts rerun.','predicates':predicates})
 print('Retained evidence assembled:',COUNTS,'total',sum(COUNTS.values()))
def seal():
 before=json.loads((LANE/'provenance/baseline.json').read_text(encoding='utf-8'));after=protected_state()
 manifest=json.loads((LANE/'provenance/source_manifest.json').read_text(encoding='utf-8'))
 changed=[]
 for key in NAMES:
  for a in manifest[key]['artifacts']:
   p=Path(manifest[key]['directory'])/a['name']
   if sha(p)!=a['sha256']:changed.append(str(p))
 result={'before':before,'after':after,'protected_checkout_unchanged':before==after,'changed_checkpoints':changed,'status':git('status','--short')}
 save(LANE/'provenance/preservation.json',result)
 assert before==after and not changed,result
 print('Protected checkout and all 15 checkpoint artifacts unchanged.')
if __name__=='__main__':{'assemble':assemble,'seal':seal}[sys.argv[1]]()
