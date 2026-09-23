"""Read-only verification of the explicit combined publication proposal."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
allow=(ROOT/'COMBINED_PUBLICATION_ALLOWLIST.txt').read_text().splitlines()
assert len(allow)==len(set(allow))
manifest=ROOT/'SHA256SUMS.txt';entries=[]
for line in manifest.read_text().splitlines():
    expected,name=line.split('  ',1);p=(REPO/name).resolve()
    assert p.is_relative_to(REPO.resolve()) and p.is_file(),name
    assert sha(p)==expected,name
    entries.append(name)
assert set(allow)==set(entries+[manifest.relative_to(REPO).as_posix()])
classes=json.loads((ROOT/'PUBLICATION_CLASSES.json').read_text())
assert sorted(x for group in classes.values() for x in group)==sorted(allow)
old_D=(REPO/'papers/PAPER_D/v0.1.1/COMBINED_PUBLICATION_ALLOWLIST.txt').read_text().splitlines()
assert len(old_D)==136 and set(old_D)<=set(allow)
assert not any('/.build/' in p or '__pycache__' in p or p.endswith('.pyc') for p in allow)
assert sha(REPO/'papers/PAPER_D/v0.1.1/publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf')=='7c4c52f8018765b21a7849d03ce7974824351e5af27c99356c5acb0b5dcaaaaf'
print(json.dumps({'status':'PASS','allowlist_paths':len(allow),'checksum_entries':len(entries),'classes':{k:len(v) for k,v in classes.items()},'writes':0},indent=2))
