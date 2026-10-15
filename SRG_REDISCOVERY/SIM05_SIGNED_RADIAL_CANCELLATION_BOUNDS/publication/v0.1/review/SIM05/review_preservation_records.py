"""File-only comparison of preservation receipts with supplied original artifacts."""
from pathlib import Path
import hashlib,json,zipfile
base=Path('/mnt/data');root=base/'sim05_submission';out=base/'SIM05_GPT_SCIENTIFIC_REVIEW_v0.1'
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
pmap=json.loads((root/'evidence/PRESERVATION_INPUTS.json').read_text())
with zipfile.ZipFile(base/'SIM04_GPT_REVIEW.zip') as z:
 for n,v in pmap['SIM04_files'].items():
  b=z.read(n) if n in z.namelist() else (base/n).read_bytes()
  assert ident(b)==v,n
for n,v in pmap['local_copies'].items():assert ident((root/n).read_bytes())==v,n
results={'recorded_protected_SIM04_identities_match_uploaded_authorities':len(pmap['SIM04_files']),
         'included_input_review_copies_match_preservation_map':len(pmap['local_copies']),
         'not_independent_Windows_access':True}
(out/'PRESERVATION_RECORD_REVIEW.json').write_text(json.dumps(results,indent=2)+'\n')
print(results)
