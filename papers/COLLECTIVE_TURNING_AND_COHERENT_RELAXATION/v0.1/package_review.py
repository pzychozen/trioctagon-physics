"""Create the publication manifest/allowlist; never fabricate visual inspection.

The historical filename is retained. This edition does not generate transfer ZIPs.
"""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
def sha(data):return hashlib.sha256(data).hexdigest()
receipt=json.loads((ROOT/'verification/publication_verification.json').read_text())
assert receipt['status']=='PASS'
assert receipt['final_pdf_sha256']==sha((ROOT/'REVIEW.pdf').read_bytes())
visual=json.loads((ROOT/'verification/publication_visual_review.json').read_text())
assert visual['status']=='PASS' and visual['record_written_after_inspection']
assert not visual['packaging_script_generated_this_result']
assert visual['pdf_sha256']==receipt['final_pdf_sha256']
assert visual['pdf_pages']==receipt['pdf_pages']
assert visual['pages_inspected']==list(range(1,receipt['pdf_pages']+1))
reviewed=json.loads((ROOT/'verification/reviewed_manifest.json').read_text())
names={x['path'] for x in reviewed['files']}
names.update(['PUBLICATION_DISPOSITION.md','verify_publication.py','evidence/PUBLICATION_WORK_ORDER.txt','verification/README.md','verification/reviewed_manifest.json','verification/review_transfer_receipt.json','verification/publication_editorial_changes.json','verification/publication_build_record.json','verification/publication_visual_review.json','verification/publication_verification.json'])
files=[ROOT/name for name in sorted(names)]
for p in files:
 assert p.is_file() and p.resolve().is_relative_to(ROOT.resolve())
 if p.suffix=='.md':
  for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
   if not target.startswith(('http:','https:')):
    assert (p.parent/target.split('#')[0]).exists(),(p,target)
repo=ROOT.parents[2]
manifest={'edition':'Author-authorized repository research edition v0.1; GPT project-internal scientific review and author review complete','scientific_baseline':receipt['scientific_baseline'],'final_pdf_sha256':receipt['final_pdf_sha256'],'pdf_pages':receipt['pdf_pages'],'reviewed_inventory':'verification/reviewed_manifest.json','files':[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in files],'repository_index':{'path':'README.md','bytes':(repo/'README.md').stat().st_size,'sha256':sha((repo/'README.md').read_bytes()),'scope':'One compact appended edition entry; all pre-existing bytes preserved.'},'exclusions':['tmp/ compiler intermediates and page renders','publication_work/ local snapshots, status and staging records','verification/baseline.json','verification/inspect_inputs.py','prepare_review.py','publication_prepare.py','publication_status.py','publication_git.py','PACKAGE_RECEIPT.json (historical transfer archive receipt; archival copy is explicitly included)','COLLECTIVE_TURNING_AND_COHERENT_RELAXATION_v0.1_GPT_REVIEW.zip','other transfer archives and unrelated files'],'manifest_self_hash_excluded':True,'manifest_included_in_staging_allowlist':True}
man=ROOT/'PACKAGE_MANIFEST.json';man.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
files.append(man)
work=ROOT/'publication_work';work.mkdir(exist_ok=True)
allowlist=['README.md']+[p.relative_to(repo).as_posix() for p in files]
assert len(allowlist)==len(set(allowlist))
(work/'staging_allowlist.txt').write_text('\n'.join(allowlist)+'\n',encoding='utf-8',newline='\n')
(work/'commit_message.txt').write_text('Publish collective turning and coherent relaxation v0.1\n',encoding='utf-8')
print(json.dumps({'status':'PASS','edition_files_including_manifest':len(files),'total_outgoing_paths':len(allowlist),'pdf_sha256':receipt['final_pdf_sha256'],'pdf_pages':receipt['pdf_pages'],'visual_record_read_only':True,'transfer_zip_created':False,'allowlist':str(work/'staging_allowlist.txt')},indent=2))
