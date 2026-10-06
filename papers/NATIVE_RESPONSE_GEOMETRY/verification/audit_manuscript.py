"""Record the reviewed manuscript word inventory and source hashes.

This tool locates contexts; it does not claim automated scientific review.
Human-readable editorial dispositions are in CONSISTENCY_AUDIT.md.
"""
from pathlib import Path
import re,json,hashlib
L=Path(__file__).resolve().parents[1]
words='gravity Einstein metric energy field force motion position wave current continuum boundary physical'.split()
rows=[];hashes={}
for p in sorted((L/'manuscript').glob('*.tex')):
 text=p.read_text(encoding='utf8');hashes[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
 for i,line in enumerate(text.splitlines(),1):
  matched=[w for w in words if re.search(w,line,re.I)]
  if matched:rows.append({'file':p.name,'line':i,'terms':matched,'context':line,'editorial_disposition':'Reviewed in context: mathematical statement, explicit interpretation limit, source title, or substring (e.g. symmetric/composition). No new physical identification.'})
d={'status':'Manually reviewed contexts; inventory generation is not proof or peer review.','terms':words,'matched_lines':len(rows),'manuscript_sha256':hashes,'contexts':rows}
(L/'provenance/word_occurrence_audit.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf8')
print('Recorded',len(rows),'reviewed matching lines (including substring matches).')
