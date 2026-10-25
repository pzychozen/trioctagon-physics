"""Read-only document audit for Volume III R1. Does not import research code.
Reads only supplied archives/text/PDF; writes audit records to a separate workspace.
"""
from __future__ import annotations
import argparse, collections, difflib, hashlib, io, json, re
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile
import fitz

BASE=Path('/mnt/data')
WORK=BASE/'SRG_VOLUME_III_R1_GPT_CLOSURE_WORK'
OLD=WORK/'prior'; NEW=WORK/'revised'; AUTH=WORK/'authority'
OUT=WORK/'audit'; OUT.mkdir(exist_ok=True)

def digest(b): return hashlib.sha256(b).hexdigest()
def ident(p):
 b=p.read_bytes(); return {'bytes':len(b),'sha256':digest(b)}
def same(p,q): return p.read_bytes()==q.read_bytes()
def write(name,x): (OUT/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def check_manifest(path):
 with ZipFile(path) as z:
  names=[i.filename for i in z.infolist() if not i.is_dir()]
  dup=[n for n,c in collections.Counter(names).items() if c>1]
  m=json.loads(z.read('MANIFEST.json'))
  rows=m['files']; expected={r['path'] for r in rows}
  errors=[]
  for r in rows:
   b=z.read(r['path'])
   if (len(b),digest(b))!=(r['bytes'],r['sha256']): errors.append(r['path'])
  return {'archive':path.name,**ident(path),'crc_failure_member':z.testzip(),
          'members':len(names),'payloads':len(rows),'payload_bytes':sum(r['bytes'] for r in rows),
          'missing':sorted(expected-set(names)),'extra':sorted(set(names)-expected-{'MANIFEST.json'}),
          'duplicates':dup,'manifest_duplicates':len(rows)-len(expected),'hash_errors':errors}

oldzip=BASE/'SRG_VOLUME_III_SIM06_SIM07_v0.1_CANDIDATE_REVIEW.zip'
newzip=BASE/'SRG_VOLUME_III_SIM06_SIM07_v0.1_R1_REVIEW.zip'
audit={'scope':'Document/source-diff/byte/PDF checks only. No scientific execution or new measurements.',
       'archives':{'old':check_manifest(oldzip),'new':check_manifest(newzip)}}
old_paths={p.relative_to(OLD).as_posix() for p in OLD.rglob('*') if p.is_file()}
new_paths={p.relative_to(NEW).as_posix() for p in NEW.rglob('*') if p.is_file()}
common=old_paths&new_paths
changed=sorted(n for n in common if not same(OLD/n,NEW/n))
audit['file_delta']={'changed':changed,'unchanged':sorted(common-set(changed)),'added':sorted(new_paths-old_paths),'removed':sorted(old_paths-new_paths)}
# Verify original baseline through the earlier actual archive, not solely a receipt.
bl=json.loads((NEW/'R1_INPUT_BASELINE.json').read_text())
rows=bl['prior_review_files']; errs=[]
with ZipFile(oldzip) as z:
 for r in rows:
  b=z.read(r['path'])
  if (len(b),digest(b))!=(r['bytes'],r['sha256']): errs.append(r['path'])
audit['baseline']={'recorded_rows':len(rows),'same_member_set':{r['path'] for r in rows}==old_paths,'errors':errs,
 'prior_zip_identity_matches':all(bl['prior_zip'][k]==ident(oldzip)[k] for k in ['bytes','sha256'])}
receipt=json.loads((NEW/'PRESERVATION_RECEIPT.json').read_text())
baselines=[]
for r in receipt['baseline_snapshots_unchanged']:
 baselines.append({'path':r['path'],'original_path':r['original_path'],'exact_prior_match':same(NEW/r['path'],OLD/r['original_path']),
                   'receipt_matches':all(ident(NEW/r['path'])[k]==r[k] for k in ['bytes','sha256'])})
audit['baseline_snapshots']={'count':len(baselines),'all_exact':all(x['exact_prior_match'] and x['receipt_matches'] for x in baselines)}
write('BASELINE_SNAPSHOT_CHECKS.json',baselines)
# Validate all selected copies with immutable parent archive bytes and prior uploads.
copy_manifest=json.loads((NEW/'EVIDENCE_COPY_MANIFEST.json').read_text())['copies']
archives={key:NEW/'handoff/inputs'/fn for key,fn in {
'S6':'SIM06_TOWER_II_GPT_REVIEW_AND_ACCEPTANCE.zip',
'S7C':'SIM07_UNIVERSE_GPT_REVIEW_AND_ACCEPTANCE.zip',
'S7R':'SIM07_UNIVERSE_REPLAY_GPT_REVIEW_AND_ACCEPTANCE.zip'}.items()}
parent_results=[]; copy_checks=[]
for k,p in archives.items():
 with ZipFile(p) as z:
  parent_results.append({'key':k,'file':str(p.relative_to(NEW)),**ident(p),'earlier_upload_exact':same(p,BASE/p.name),
                         'old_candidate_exact':same(p,OLD/p.relative_to(NEW)),'crc_failure_member':z.testzip(),'members':len(z.infolist())})
  for r in copy_manifest:
   if r['parent_key']!=k: continue
   b=(NEW/r['path']).read_bytes()
   copy_checks.append({'path':r['path'],'parent':k,'member':r['member'],'exact_parent_match':b==z.read(r['member']),
                       'exact_prior_match':b==(OLD/r['path']).read_bytes(),'manifest_match':(len(b),digest(b))==(r['bytes'],r['sha256'])})
audit['accepted_inputs']={'archives':parent_results,'evidence_copies':len(copy_checks),'all_copy_checks_pass':all(x['exact_parent_match'] and x['exact_prior_match'] and x['manifest_match'] for x in copy_checks)}
write('EVIDENCE_BYTE_COMPARISONS.json',copy_checks)
figrows=json.loads((NEW/'FIGURE_REGISTER.json').read_text())['figures']
figchecks=[]
for r in figrows:
 p=NEW/r['file']
 with ZipFile(archives[r['parent_key']]) as z:
  figchecks.append({'figure':r['figure'],'file':r['file'],'page':r['physical_pdf_page'],
                    'exact_prior_match':same(p,OLD/r['file']),'exact_parent_match':p.read_bytes()==z.read(r['member']),
                    'register_identity_match':all(ident(p)[k]==r[k] for k in ['bytes','sha256'])})
audit['figures']={'count':len(figchecks),'all_exact':all(x['exact_prior_match'] and x['exact_parent_match'] and x['register_identity_match'] for x in figchecks),'register_unchanged':same(NEW/'FIGURE_REGISTER.json',OLD/'FIGURE_REGISTER.json')}
write('FIGURE_PRESERVATION.json',figchecks)
# External attachments currently available.
audit['standalone_uploads']={
 'pdf_equals_archive':same(BASE/'manuscript(3).pdf',NEW/'manuscript.pdf'),
 'patch_equals_archive':same(BASE/'R1_EXACT_DIFF.patch',NEW/'R1_EXACT_DIFF.patch'),
 'preservation_equals_archive':same(BASE/'PRESERVATION_RECEIPT(1).json',NEW/'PRESERVATION_RECEIPT.json'),
 'prior_pdf_equals_prior_archive':same(BASE/'SRG_VOLUME_III_SIM06_SIM07_v0.1_CANDIDATE.pdf',OLD/'manuscript.pdf'),
 'actual_supplied_drafting_handoff_matches':ident(BASE/'SRG_SIM06_SIM07_MANUSCRIPT_CODEX_HANDOFF_20261025.zip')=={k:bl['external_inputs'][0][k] for k in ['bytes','sha256']},
 'source_readback_matches_prior_authority':same(NEW/'r1_input/SOURCE_READBACK_E01_E02.md',AUTH/'SOURCE_READBACK_E01_E02.md')}
# Actual diff, E01 block-only removal check and E02 single-entry correction.
files=['manuscript.tex','universe_sections.tex','closing_sections.tex','references.bib','CLAIM_EVIDENCE_MATRIX.md']
diffs={}
for n in files:
 a=(OLD/n).read_text(); b=(NEW/n).read_text()
 diffs[n]=''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='v0.1/'+n,tofile='v0.1-R1/'+n))
actual=''.join(diffs[n] for n in files)
(OUT/'INDEPENDENT_EXACT_DIFF.patch').write_text(actual)
oldclosing=(OLD/'closing_sections.tex').read_bytes(); newclosing=(NEW/'closing_sections.tex').read_bytes()
a=oldclosing.index(b"Both sources' GRF observer is"); end=oldclosing.index(b'\\subsection{A large pooled spread')
b=newclosing.index(b'Both sources use the pointwise diagnostic'); endnew=newclosing.index(b'\\subsection{A large pooled spread')
oldbib=(OLD/'references.bib').read_bytes(); newbib=(NEW/'references.bib').read_bytes()
oldentry=next(x for x in oldbib.splitlines(keepends=True) if x.startswith(b'@misc{s7creview,'))
audit['source_changes']={
 'modified_manuscript_inputs':[n for n in files if diffs[n]],
 'delivered_diff_matches_recomputed_text':(NEW/'R1_EXACT_DIFF.patch').read_text()==actual,
 'actual_hunks':len(re.findall(r'^@@',actual,re.M)),
 'main_tex_byte_identical':same(OLD/'manuscript.tex',NEW/'manuscript.tex'),
 'universe_tex_byte_identical':same(OLD/'universe_sections.tex',NEW/'universe_sections.tex'),
 'closing_outside_GRF_block_byte_identical':oldclosing[:a]==newclosing[:b] and oldclosing[end:]==newclosing[endnew:],
 'bibliography_only_s7creview_date_changed':oldbib.replace(oldentry,oldentry.replace(b'24 October.',b'25 October.'))==newbib,
 'C34_generic_wording_unchanged':same(OLD/'CLAIM_EVIDENCE_MATRIX.md',NEW/'CLAIM_EVIDENCE_MATRIX.md'),
 'supplied_exact_proposed_patch_used':False,
 'GRF_equivalent_form': 'Two named averages of g_i in one equation instead of proposed general nonempty-G form. Independently reviewed as equivalent.',
 'version_label':'Delivered v0.1-R1; title/header remain Candidate v0.1. Not represented as a v0.1.1 edition.'}
# Math environment comparison (raw bytes), including the only intended equation change.
blocks=[]
pattern=re.compile(rb'\\begin\{(equation\*?|align\*?|gather\*?)\}(.*?)\\end\{\1\}',re.S)
for n in ['manuscript.tex','universe_sections.tex','closing_sections.tex']:
 oldb=list(pattern.finditer((OLD/n).read_bytes())); newb=list(pattern.finditer((NEW/n).read_bytes()))
 if len(oldb)!=len(newb): raise ValueError('Math environments count changed')
 for i,(x,y) in enumerate(zip(oldb,newb)):
  labs=re.findall(rb'\\label\{([^}]+)\}',x.group(0))
  blocks.append({'source':n,'index':i,'labels':[v.decode() for v in labs],'equal':x.group(0)==y.group(0),
                 'before_sha256':digest(x.group(0)),'after_sha256':digest(y.group(0))})
audit['math_blocks']={'total':len(blocks),'unchanged':sum(x['equal'] for x in blocks),'changed':[x for x in blocks if not x['equal']]}
write('MATH_BLOCK_COMPARISONS.json',blocks)
# Document labels, citations, authored Markdown links, TeX inputs.
tex='\n'.join((NEW/n).read_text() for n in ['manuscript.tex','universe_sections.tex','closing_sections.tex'])
labels=re.findall(r'\\label\{([^}]+)\}',tex)
refs=re.findall(r'\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}',tex)
aux=(NEW/'qa/manuscript.aux').read_text()
compiled_labels=re.findall(r'\\newlabel\{([^}]+)\}',aux)
keys=re.findall(r'@\w+\{([^,]+),',(NEW/'references.bib').read_text())
cites=[k.strip() for match in re.findall(r'\\cite\w*\*?(?:\[[^]]*\])*\{([^}]+)\}',tex) for k in match.split(',')]
log=(NEW/'qa/manuscript.log').read_text(errors='replace')
warn=[line for line in log.splitlines() if ('undefined' in line.lower() or 'Missing character:' in line)]
links=[]
for p in sorted(NEW.glob('*.md')):
 for raw in re.findall(r'(?<!!)\[[^\]]*\]\(([^\n]+?)\)',p.read_text()):
  raw=raw.strip().strip('<>')
  # URLs and fragment-only entries are outside local target check.
  if raw.startswith(('http:','https:','mailto:','#')): continue
  target=unquote(raw.split('#',1)[0])
  links.append({'document':p.name,'target':target,'exists':(p.parent/target).exists()})
audit['navigation']={'source_labels':len(labels),'compiled_labels':len(compiled_labels),'reference_occurrences':len(refs),
 'unresolved_source_references':sorted(set(refs)-set(compiled_labels)),'bibliography_keys':len(keys),'unique_cited_keys':len(set(cites)),
 'unresolved_citations':sorted(set(cites)-set(keys)),
 'source_label_sequence_unchanged':labels==re.findall(r'\\label\{([^}]+)\}','\n'.join((OLD/n).read_text() for n in ['manuscript.tex','universe_sections.tex','closing_sections.tex'])),
 'aux_unchanged':same(OLD/'qa/manuscript.aux',NEW/'qa/manuscript.aux'),
 'toc_unchanged':same(OLD/'qa/manuscript.toc',NEW/'qa/manuscript.toc'),
 'root_markdown_link_occurrences':len(links),'missing_local_targets':[l for l in links if not l['exists']],
 'undefined_or_missing_character_warnings':warn}
write('ROOT_LINK_CHECKS.json',links)
# PDF metadata/text/link checks; raster comparison separate below.
oldpdf=fitz.open(OLD/'manuscript.pdf'); newpdf=fitz.open(NEW/'manuscript.pdf')
text_changes=[]; page_meta=[]; pdf_bad_links=[]; ninternal=0
for i,(o,n) in enumerate(zip(oldpdf,newpdf)):
 if o.get_text()!=n.get_text(): text_changes.append(i+1)
 page_meta.append({'page':i+1,'size':list(n.rect),'rotation':n.rotation,'dimensions_and_rotation_equal':o.rect==n.rect and o.rotation==n.rotation})
 for l in n.get_links():
  if l['kind']==fitz.LINK_GOTO:
   ninternal+=1
   if not 0<=l.get('page',-1)<len(newpdf): pdf_bad_links.append({'page':i+1,'link':str(l)})
texts='\n'.join(p.get_text() for p in newpdf)
audit['pdf']={'current':ident(NEW/'manuscript.pdf'),'prior':ident(OLD/'manuscript.pdf'),'pages':len(newpdf),
 'changed_text_pages':text_changes,'unchanged_text_pages':len(newpdf)-len(text_changes),'rotated_pages':[p['page'] for p in page_meta if p['rotation']],
 'all_page_dimensions_and_rotations_equal':all(p['dimensions_and_rotation_equal'] for p in page_meta),
 'checked_internal_links':ninternal,'invalid_internal_links':pdf_bad_links,'replacement_glyph_count':texts.count('\ufffd'),
 'question_mark_placeholders':texts.count('??'),'metadata':newpdf.metadata}
write('PDF_PAGE_PROPERTIES.json',page_meta)
# Actual file identities for the closure and independent preservation checks.
audit['accepted_artifact_identities']={n:ident(NEW/n) for n in ['manuscript.pdf','manuscript.tex','universe_sections.tex','closing_sections.tex','references.bib','CLAIM_EVIDENCE_MATRIX.md','MANIFEST.json']}
write('DOCUMENT_AUDIT.json',audit)
print(json.dumps({k:audit[k] for k in ['archives','baseline','baseline_snapshots','standalone_uploads','source_changes','math_blocks','navigation','pdf','figures']},indent=2))
print('PARENT ARCHIVES:',json.dumps(parent_results,indent=2))
print('COPY CHECKS:',len(copy_checks),audit['accepted_inputs']['all_copy_checks_pass'])
