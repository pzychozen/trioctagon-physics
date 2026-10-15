from pathlib import Path,PurePosixPath
import zipfile,stat,hashlib,json,io
BASE=Path('/mnt/data'); OUT=BASE/'SIM05_GPT_SCIENTIFIC_REVIEW_v0.1'; EXT=BASE/'sim05_submission'
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def audit(z,manifest):
 infos=z.infolist(); names=[i.filename for i in infos]
 assert len(names)==len(set(names))==len({n.casefold() for n in names})
 for i in infos:
  p=PurePosixPath(i.filename)
  assert not p.is_absolute() and '..' not in p.parts and '\\' not in i.filename and ':' not in i.filename
  assert not stat.S_ISLNK(i.external_attr>>16) and not i.is_dir()
 assert z.testzip() is None
 m=json.loads(z.read(manifest)); rows=m.get('files',m.get('payload',{}))
 assert isinstance(rows,dict)
 assert set(rows)==set(names)-{manifest}, (set(rows)^ (set(names)-{manifest}))
 for n,v in rows.items():
  got=ident(z.read(n)); assert got['bytes']==v['bytes'] and got['sha256']==v['sha256'],n
 return {'members':len(names),'manifested_payloads':len(rows),'CRC_paths_names_no_symlinks_coverage_hashes':'PASS','uncompressed_bytes':sum(i.file_size for i in infos)}
current=BASE/'SIM05_GPT_REVIEW.zip'; seal=json.loads((BASE/'SIM05_TRANSPORT_SEAL.json').read_text())
assert ident(current.read_bytes())==seal['archive']
with zipfile.ZipFile(current) as z:
 result={'archive':ident(current.read_bytes()),'audit':audit(z,'MANIFEST.json')}
 assert ident(z.read('MANIFEST.json'))==seal['manifest']
 for n in ['SIM05_REPORT.md','SIM05_EXECUTION_RECEIPT.md']:assert (BASE/n).read_bytes()==z.read(n)
 with zipfile.ZipFile(BASE/'SIM04_GPT_REVIEW.zip') as old:
  assert ident((BASE/'SIM04_GPT_REVIEW.zip').read_bytes())=={'bytes':21653622,'sha256':'d3be3e9829181378f1e0e3af696d5cfe8de98c8a697ee59677c0edd5036e2987'}
  count=0
  for n in z.namelist():
   if n.startswith('inputs/'):
    assert z.read(n)==old.read(n.removeprefix('inputs/')), n; count+=1
  result['upstream_SIM04_files_byte_equal']=count
 with zipfile.ZipFile(BASE/'SRG_SIM05_CODEX_HANDOFF_v0.1_20261014.zip') as hand:
  count=0
  for n in z.namelist():
   if n.startswith('received/'):
    assert z.read(n)==hand.read(n.removeprefix('received/')),n; count+=1
  result['handoff_members_byte_equal']=count
 review_bytes=z.read('received/reference/SIM04_GPT_SCIENTIFIC_REVIEW_v0.1.zip')
 assert review_bytes==(BASE/'SIM04_GPT_SCIENTIFIC_REVIEW_v0.1.zip').read_bytes()
 with zipfile.ZipFile(io.BytesIO(review_bytes)) as rev:
  result['upstream_review_audit']=audit(rev,'REVIEW_MANIFEST.json')
  for n in rev.namelist():assert z.read('review/'+n)==rev.read(n),n
  result['upstream_review_members_byte_equal']=len(rev.namelist())
 EXT.mkdir(exist_ok=False)
 z.extractall(EXT)
 result['extracted_files_match']=all((EXT/i.filename).read_bytes()==z.read(i.filename) for i in z.infolist())
(OUT/'ARCHIVE_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
