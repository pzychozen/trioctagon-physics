from pathlib import Path,PurePosixPath
import json,hashlib,zipfile,datetime
R=Path(__file__).resolve().parent;P=R/'packet'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(n,x):(R/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
m=json.loads((P/'PACKET_MANIFEST.json').read_text());entries=m['entries']
for e in entries:
 b=(P/e['path']).read_bytes();assert len(b)==e['bytes'] and sha(b)==e['sha256'],e['path']
assert (P/'CODEX_NCM_Z_DOCUMENTATION_WORK_ORDER_v0.1.md').read_bytes()==Path('C:/Users/Notandi/Downloads/CODEX_NCM_Z_DOCUMENTATION_WORK_ORDER_v0.1.md').read_bytes()
select={
'Z01':['OBSERVATIONS.json','GAP_COMPARISON.json','INITIAL_STATE_LEDGER.json','inputs/retained.motion.json','inputs/parent_run_record.json','source_snapshots/observer.py','source_snapshots/z.py','source_snapshots/readouts.py','source_snapshots/motion.tex','source_snapshots/paperE.md','checks_results.json'],
'Z02':['OBSERVATIONS.json','GAP_COMPARISON.json','TRANSITIONS.json','ATTRIBUTION.json','inputs/SELECTED_HISTORY.json','ORIGINAL_TOKEN_LEDGER.json','ADMISSION_FREEZE_RECEIPT.json','accepted_sources/observer.py','accepted_sources/z.py','accepted_sources/central.tex','accepted_sources/host.tex','accepted_sources/attachment.tex','figures/01_top.png','figures/02_opposite_sides.png','checks_results.json'],
'Z03':['STATE_SNAPSHOTS.json','NATIVE_INTENSITY_BUDGET.json','NATIVE_CHIRAL_BUDGET.json','FROZEN_Z_SOURCE_BUDGET.json','RADIAL_TRANSVERSE_ACCOUNTING.json','SOURCE_EXCERPTS.txt','sources/kernel_physics/dynamics.py','sources/kernel_physics/readouts.py','sources/kernel_physics/axial_observables.py','sources/kernel_physics/z_diagnostics.py','sources/papers/PAPER_G/v0.1.1/source/paper_g.tex','figures/03_radial_balance.png']}
verification=[];extracted=[]
for s in json.loads((P/'SOURCE_INDEX.json').read_text())['sources']:
 archive=P/s['archive'];assert archive.stat().st_size==s['bytes'] and sha(archive.read_bytes())==s['sha256']
 with zipfile.ZipFile(archive) as z:
  names=z.namelist();assert len(names)==len(set(names))==s['archive_members'];assert z.testzip() is None
  for n in names:
   q=PurePosixPath(n);assert not q.is_absolute() and '..' not in q.parts and '\\' not in n and ':' not in n
  em=json.loads(z.read('OUTPUT_HASHES.json'))['entries'];assert set(names)=={e['path'] for e in em}|{'OUTPUT_HASHES.json'}
  for e in em:
   b=z.read(e['path']);assert len(b)==e['bytes'] and sha(b)==e['sha256']
  for e in s['convenience_copies']:assert z.read(e['archive_member'])==(P/e['packet_path']).read_bytes()
  for n in select[s['id']]:
   b=z.read(n);dest=R/'evidence'/s['id']/n;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
   extracted.append({'source':s['id'],'archive':str(archive.relative_to(R)).replace('\\','/'),'member':n,'extracted_path':str(dest.relative_to(R)).replace('\\','/'),'bytes':len(b),'sha256':sha(b)})
  verification.append({'id':s['id'],'members_verified':len(names),'payload_hashes_verified':len(em),'sha256':s['sha256'],'crc':True,'safe_unique_names':True,'convenience_copies_equal':True})
 # Reviewer evidence ZIPs remain intact; verify safety/CRC without extracting or execution.
 for e in s['review_materials']:
  b=(P/e['path']).read_bytes();assert len(b)==e['bytes'] and sha(b)==e['sha256']
  if e['path'].endswith('.zip'):
   with zipfile.ZipFile(P/e['path']) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
    for n in z.namelist():assert not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and ':' not in n and '\\' not in n
assert sha((R/'evidence/Z01/inputs/retained.motion.json').read_bytes())=='071f6f7dc74128d638b0e96e33897b1366b2f8bcb98ca741c11fe0af5ed0e1e7'
assert sha((R/'evidence/Z02/inputs/SELECTED_HISTORY.json').read_bytes())=='a294a4b0bf181adaa2054aa52379c1832a7833e3faa7614d0785aecd709ea09c'
with zipfile.ZipFile(P/'evidence/NCM_Z_03_v0.1_REVIEW.zip') as z:assert z.read('packet/NCM_Z_03_Packet_v0.1/inputs/SELECTED_HISTORY.json')==(R/'evidence/Z02/inputs/SELECTED_HISTORY.json').read_bytes()
dump('INPUT_VERIFICATION.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'packet_payloads_verified':len(entries),'archives':verification,'Z03_uses_identical_Z02_history':True,'two_state_bytes':27068,'five_state_bytes':8871,'historical_scripts_executed':0,'new_scientific_evaluations':0})
dump('EXTRACTION_MANIFEST.json',extracted)
print((R/'INPUT_VERIFICATION.json').read_text())
print('EXTRACTED',len(extracted))
for source,n in [('Z01','OBSERVATIONS.json'),('Z01','GAP_COMPARISON.json'),('Z02','TRANSITIONS.json')]:
 obj=json.loads((R/'evidence'/source/n).read_text());print('SCHEMA',source,n,str(obj)[:7000])
