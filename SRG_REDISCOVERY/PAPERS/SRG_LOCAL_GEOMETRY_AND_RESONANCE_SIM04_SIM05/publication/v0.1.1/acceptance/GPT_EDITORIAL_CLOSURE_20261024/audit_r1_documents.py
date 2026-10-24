#!/usr/bin/env python3
"""Read-only byte/text/document audit of Volume II R1. Never imports scientific source."""
from pathlib import Path
import collections, difflib, hashlib, json, re, urllib.parse, zipfile
import fitz

BASE = Path('/mnt/data')
WORK = BASE/'SRG_VOLUME_II_R1_CLOSURE_WORK'
OUT = BASE/'SRG_VOLUME_II_v0.1.1_GPT_EDITORIAL_CLOSURE'
OLD, NEW, AUTH = [WORK / n for n in ('v01','r1','authority')]

def digest(data): return hashlib.sha256(data).hexdigest()
def identity(p):
    b=p.read_bytes();return {'bytes':len(b),'sha256':digest(b)}
def readjson(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def text(p): return p.read_bytes().decode('utf-8-sig').replace('\r\n','\n')
def check(cond, msg):
    if not cond: raise AssertionError(msg)
def checked_manifest(root):
    manifest=readjson(root/'MANIFEST.json')
    rows=manifest['files']; names=[r['path'] for r in rows]
    check(len(names)==len(set(names)), 'Duplicate manifest path')
    files=sorted(str(p.relative_to(root)) for p in root.rglob('*') if p.is_file())
    check(set(files)==set(names)|{'MANIFEST.json'}, 'Unaccounted manifest members')
    errors=[]
    for row in rows:
        actual=identity(root/row['path'])
        if actual!={k:row[k] for k in ('bytes','sha256')}: errors.append(row['path'])
    check(not errors,'Manifest mismatches '+repr(errors))
    return {'files':len(files),'payloads':len(rows),'payload_bytes':sum(r['bytes'] for r in rows),'errors':errors}

def apply_unified(originals, patch):
    """Strict, context-checked unified patch on normalized document text in memory."""
    lines=patch.splitlines(keepends=True); result={}; i=0; counts={}
    while i<len(lines):
        if not lines[i].startswith('--- '): i+=1;continue
        oldname=lines[i][4:].strip().split('\t')[0].removeprefix('a/')
        i+=1; check(lines[i].startswith('+++ '),'Missing +++')
        newname=lines[i][4:].strip().split('\t')[0].removeprefix('b/')
        check(oldname==newname,'Unexpected rename')
        src=originals[oldname].splitlines(keepends=True); dst=[];cursor=0;count=0;i+=1
        while i<len(lines) and not lines[i].startswith('--- '):
            if not lines[i].startswith('@@'): i+=1;continue
            m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i]);check(m is not None,'Bad hunk')
            start=int(m[1])-1;oldlen=int(m[2] or 1);newlen=int(m[4] or 1)
            check(start>=cursor,'Overlapping hunk');dst+=src[cursor:start];cursor=start
            consumed=produced=0;count+=1;i+=1
            while i<len(lines) and not lines[i].startswith(('@@','--- ')):
                row=lines[i]
                if row.startswith('\\'): i+=1;continue
                if not row or row[0] not in ' +-':break
                sign,val=row[0],row[1:]
                if sign in ' -':
                    check(cursor<len(src) and src[cursor]==val,f'Context mismatch {oldname}:{cursor+1}')
                    cursor+=1;consumed+=1
                if sign in ' +':dst.append(val);produced+=1
                i+=1
            check(consumed==oldlen and produced==newlen,'Hunk length mismatch')
        dst+=src[cursor:];result[newname]=''.join(dst);counts[newname]=count
    return result,counts

report={'date':'2026-10-24','scope':'Document closure and immutable-byte checks only; no scientific execution.'}
report['archives']={n:identity(BASE/n) for n in [
 'SRG_VOLUME_II_SIM04_SIM05_CANDIDATE_v0.1.1_R1_REVIEW.zip',
 'SRG_VOLUME_II_SIM04_SIM05_CANDIDATE_v0.1_REVIEW.zip',
 'SRG_VOLUME_II_v0.1_GPT_REVIEW_AND_CODEX_R1.zip']}
report['crc']={n:zipfile.ZipFile(BASE/n).testzip() for n in report['archives']}
report['r1_manifest']=checked_manifest(NEW);report['v01_manifest']=checked_manifest(OLD)
report['standalone_uploads']={
 'pdf':(BASE/'manuscript(1).pdf').read_bytes()==(NEW/'manuscript.pdf').read_bytes(),
 'diff':(BASE/'DIFF_FROM_v0.1.patch').read_bytes()==(NEW/'DIFF_FROM_v0.1.patch').read_bytes(),
 'receipt':(BASE/'PRESERVATION_RECEIPT.json').read_bytes()==(NEW/'PRESERVATION_RECEIPT.json').read_bytes(),
 'old_pdf':(BASE/'manuscript.pdf').read_bytes()==(OLD/'manuscript.pdf').read_bytes(),
 'old_tex':(BASE/'manuscript(2).tex').read_bytes()==(OLD/'manuscript.tex').read_bytes()}
check(all(report['standalone_uploads'].values()),'Standalone mismatch')
oldtex,newtex=text(OLD/'manuscript.tex'),text(NEW/'manuscript.tex')
patchfile=AUTH/'PROPOSED_E01_E03_SOURCE_CORRECTIONS.patch'
check(patchfile.read_bytes()==(NEW/'SOURCE_CORRECTIONS_ONLY.patch').read_bytes(),'Authority patch changed')
expected,hunks=apply_unified({n:text(OLD/n) for n in ['manuscript.tex','CLAIM_EVIDENCE_MATRIX.md']}, text(patchfile))
replacements=[
 ('pdfsubject={Candidate v0.1 for scientific review; zero new simulations}', 'pdfsubject={Candidate v0.1.1 editorial R1, 24 October 2026, for scientific review; zero new simulations}'),
 (r'\fancyhead[R]{\small\sffamily Candidate v0.1}',r'\fancyhead[R]{\small\sffamily Candidate v0.1.1 / R1}'),
 (r'\textbf{Candidate manuscript v0.1 / 23 October 2026}',r'\textbf{Candidate manuscript v0.1.1 (editorial R1) / 24 October 2026}')]
for a,b in replacements:
    check(expected['manuscript.tex'].count(a)==1,'Unexpected housekeeping context')
    expected['manuscript.tex']=expected['manuscript.tex'].replace(a,b)
check(expected['manuscript.tex']==newtex,'Unapproved manuscript change')
check(expected['CLAIM_EVIDENCE_MATRIX.md']==text(NEW/'CLAIM_EVIDENCE_MATRIX.md'),'Unapproved matrix change')
actualdiff=''.join(''.join(difflib.unified_diff(text(OLD/n).splitlines(keepends=True),text(NEW/n).splitlines(keepends=True),fromfile='a/'+n,tofile='b/'+n)) for n in ['manuscript.tex','CLAIM_EVIDENCE_MATRIX.md'])
check(actualdiff==text(NEW/'DIFF_FROM_v0.1.patch'),'Delivered exact diff mismatch')
report['source_diff']={'approved_patch_sha256':identity(patchfile)['sha256'],'approved_patch_hunks':hunks,'additional_manuscript_changes':replacements,'exact_approved_result':True,'delivered_diff_matches_recomputation':True,'hunks_total':len(re.findall(r'^@@',actualdiff,re.M))}
(OUT/'INDEPENDENT_DIFF_FROM_v0.1.patch').write_text(actualdiff,encoding='utf-8')

# Check complete proof section and individual mathematical environments as literal source.
proof_start=r'\section{Four reviewed mathematical explanations}'
proof_end=r'\section{What the comparison establishes}'
oldproof=oldtex[oldtex.index(proof_start):oldtex.index(proof_end)]
newproof=newtex[newtex.index(proof_start):newtex.index(proof_end)]
check(oldproof==newproof,'Proof section changed')
math_pattern=r'\\begin\{(equation\*?|align\*?)\}.*?\\end\{\1\}'
oldmath=[m.group(0) for m in re.finditer(math_pattern,oldtex,re.S)]
newmath=[m.group(0) for m in re.finditer(math_pattern,newtex,re.S)]
check(oldmath==newmath,'Mathematical block changed')
oldraw,newraw=(OLD/'manuscript.tex').read_bytes(),(NEW/'manuscript.tex').read_bytes()
check(oldraw[oldraw.index(proof_start.encode()):oldraw.index(proof_end.encode())]==newraw[newraw.index(proof_start.encode()):newraw.index(proof_end.encode())], 'Raw proof bytes changed')
check([m.group(0) for m in re.finditer(math_pattern.encode(),oldraw,re.S)]==[m.group(0) for m in re.finditer(math_pattern.encode(),newraw,re.S)], 'Raw math bytes changed')
report['scientific_text_preservation']={'four_proposition_section_equal':True,'raw_proposition_and_math_block_bytes_equal':True,'propositions':newproof.count(r'\begin{proposition}'),'math_environments_equal':True,'math_environments':len(newmath),'proposition_section_sha256_LF_UTF8':digest(newproof.encode()),'bibliography_equal':(OLD/'references.tex').read_bytes()==(NEW/'references.tex').read_bytes()}

oldfiles={str(p.relative_to(OLD)):p for p in OLD.rglob('*') if p.is_file()}
newfiles={str(p.relative_to(NEW)):p for p in NEW.rglob('*') if p.is_file()}
changed=[p for p in sorted(oldfiles.keys() & newfiles.keys()) if oldfiles[p].read_bytes()!=newfiles[p].read_bytes()]
added=sorted(newfiles.keys()-oldfiles.keys()); removed=sorted(oldfiles.keys()-newfiles.keys())
report['file_delta']={'changed':changed,'added':added,'removed':removed,'unchanged_count':len(oldfiles.keys() & newfiles.keys())-len(changed)}
scientific=[p for p in oldfiles if p.startswith(('evidence/','figures/'))]
check(all(p in newfiles and oldfiles[p].read_bytes()==newfiles[p].read_bytes() for p in scientific),'Scientific payload changed')
report['scientific_payload_preservation']={'unchanged_files':len(scientific),'figures':sum(p.startswith('figures/') for p in scientific),'scientific_evidence':sum(p.startswith('evidence/') for p in scientific),'paths':scientific}
inputs=['evidence/inputs/SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip','evidence/inputs/SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip']
for p in inputs:check((NEW/p).read_bytes()==(BASE/Path(p).name).read_bytes(),'Earlier immutable input mismatch '+p)
report['immutable_inputs_match_prior_uploads']={p:identity(NEW/p) for p in inputs}

baseline=readjson(NEW/'R1_STARTING_BASELINE.json'); receipt=readjson(NEW/'PRESERVATION_RECEIPT.json')
oldbase=baseline['old_candidate_all_files'];external=baseline['external_accepted_inputs']
check(len(oldbase)==665 and len({r['path'] for r in oldbase})==665,'Old baseline count')
check(sum(r['bytes'] for r in oldbase)==receipt['old_candidate_total_bytes'],'Baseline total mismatch')
base_by_name={r['path']:r for r in oldbase};supported=0
for p,f in oldfiles.items():
    row=base_by_name[p];check(identity(f)=={k:row[k] for k in ('bytes','sha256')},'Baseline old delivered mismatch '+p);supported+=1
old_zip='SRG_VOLUME_II_SIM04_SIM05_CANDIDATE_v0.1_REVIEW.zip'
row=base_by_name[old_zip];check(identity(BASE/old_zip)=={k:row[k] for k in ('bytes','sha256')},'Old zip baseline');supported+=1
external_checks=[]
# Some baselined inputs were not selected for direct copying; match exact bytes in
# existing uploaded input archives instead, without treating them as live paths.
available={}
for p in list(newfiles.values()) + [p for p in BASE.iterdir() if p.is_file()]:
    ident=identity(p);available[(ident['bytes'],ident['sha256'])]=str(p)
for zp in [BASE/'SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip',BASE/'SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip',BASE/'SRG_SIMULATION_STUDY_05_INFINITY_REVIEW.zip']:
    with zipfile.ZipFile(zp) as z:
        for info in z.infolist():
            if info.is_dir(): continue
            data=z.read(info);available[(len(data),digest(data))]=str(zp)+'!/'+info.filename
for row in external:
    cp=row.get('candidate_path')
    if cp and (NEW/cp).is_file():
        check(identity(NEW/cp)=={k:row[k] for k in ('bytes','sha256')},'External snapshot mismatch '+cp)
    match=available.get((row['bytes'],row['sha256']))
    external_checks.append({'original_path':row['original_path'],'matched_available_snapshot':match,'live_windows_path_accessed':False})
report['preservation_scope']={'codex_windows_baseline_file_count':len(oldbase),'baseline_total_bytes':sum(r['bytes'] for r in oldbase),'old_delivered_files_plus_archive_directly_matched':supported,'external_baseline_rows':len(external),'external_input_snapshots_matched':sum(r['matched_available_snapshot'] is not None for r in external_checks),'external_checks':external_checks,'qualification':'The live Windows directory and external paths were not accessed. The 665-file before/after preservation and absence of execution remain Codex attestations; delivered bytes, available input snapshots and baseline consistency were independently checked.'}

# Citation and navigation checks on current document only; inherited evidence retains historical links.
ref_text=text(NEW/'references.tex')
labels=[x for x in re.findall(r'\\label\{([^}]+)\}',newtex) if not x.startswith('#')]
labels += re.findall(r'\}\{(fig:[^}]+)\}\{\}',newtex)
refs=re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',newtex)
bib=re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',ref_text)
cites=[v.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',newtex) for v in group.split(',')]
check(len(labels)==len(set(labels)),'Duplicate label');check(not(set(refs)-set(labels)),'Unresolved labels');check(not(set(cites)-set(bib)),'Unresolved citations')
texlinks=re.findall(r'\\href\{([^}]+)\}',newtex+'\n'+ref_text)
def resolve_target(t):
    t=urllib.parse.unquote(t).removeprefix('run:').split('#',1)[0]
    if not t or t.startswith(('http:','https:','mailto:')): return None
    return (NEW/t).exists()
texlinkbad=[t for t in texlinks if resolve_target(t) is False]
check(not texlinkbad,'Missing TeX file targets')
rootdocs=['START_HERE.md','BUILD_INSTRUCTIONS.md','EDITORIAL_AND_VERIFICATION_NOTES.md','EVIDENCE_INDEX.md','CORRECTION_DISPOSITION.md','CLAIM_EVIDENCE_MATRIX.md']
mdlinks=[]
for name in rootdocs:
    for t in re.findall(r'\]\(([^\n)]+)\)',text(NEW/name)):
        mdlinks.append({'source':name,'target':t,'exists':resolve_target(t)})
mdmissing=[r for r in mdlinks if r['exists'] is False]
check(not mdmissing,'Missing root MD targets '+repr(mdmissing))
report['navigation']={'labels':len(labels),'reference_occurrences':len(refs),'bibliography_keys':len(bib),'unique_cited_keys':len(set(cites)),'tex_href_occurrences':len(texlinks),'md_link_occurrences':len(mdlinks),'missing_tex_targets':texlinkbad,'missing_md_targets':mdmissing,'claim_rows':len(re.findall(r'^\| C\d+ /',text(NEW/'CLAIM_EVIDENCE_MATRIX.md'),re.M))}

doc=fitz.open(NEW/'manuscript.pdf');olddoc=fitz.open(OLD/'manuscript.pdf')
pdftexts=[p.get_text() for p in doc]
fonts={};pdflinks=[]
for i,p in enumerate(doc):
    for f in p.get_fonts(full=True):
        if f[0] not in fonts:
            name,ext,typ,buf=doc.extract_font(f[0]);fonts[f[0]]={'name':name,'type':typ,'extension':ext,'embedded_bytes':len(buf)}
    for link in p.get_links():
        if link['kind'] in (fitz.LINK_GOTOR, fitz.LINK_LAUNCH):
            t=link.get('file','');pdflinks.append({'page':i+1,'target':t,'exists':resolve_target(t)})
        elif link['kind']==fitz.LINK_URI:
            t=link.get('uri','')
            if t.startswith('file:'):pdflinks.append({'page':i+1,'target':t,'exists':resolve_target(t.removeprefix('file:'))})
check(not any('??' in t for t in pdftexts),'PDF question mark placeholder')
check(not any('\ufffd' in t for t in pdftexts),'PDF replacement glyph')
check(all(f['embedded_bytes']>0 for f in fonts.values()),'Unembedded font')
check(not any(x['exists'] is False for x in pdflinks),'Missing PDF file target')
# Compare mathematical body content by extracted text page-to-page after removing headers, ignoring line wraps.
def body(p):
    t=p.get_text()
    t=re.sub(r'SRG Reconstruction\s*/\s*Volume II','',t)
    t=re.sub(r'Candidate v0\.1(?:\.1\s*/\s*R1)?','',t)
    return re.sub(r'\s+',' ',t).strip()
text_changed=[i+1 for i in range(len(doc)) if body(doc[i])!=body(olddoc[i])]
report['pdf']={'pages':len(doc),'identity':identity(NEW/'manuscript.pdf'),'metadata':doc.metadata,'embedded_font_count':len(fonts),'all_fonts_embedded':True,'pdf_file_links':len(pdflinks),'unique_pdf_file_targets':len({r['target'] for r in pdflinks}),'missing_pdf_file_links':[],'normalized_page_text_changed_excluding_running_headers':text_changed,'rotated_pages':[i+1 for i,p in enumerate(doc) if p.rotation],'visual_review':'Pending direct rendered-page inspection; see separate visual receipt.'}
(OUT/'DOCUMENT_AUDIT.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['file_delta','scientific_payload_preservation','archives']},indent=2,ensure_ascii=False))
print('\nFILE DELTA',json.dumps(report['file_delta'],indent=2))
