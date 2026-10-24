"""R1 file intake and literal approved patch only; no science imports or execution."""
from pathlib import Path
import difflib, hashlib, json, re, shutil, zipfile
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'v0.1'
REVIEW=Path(r'C:\Users\Notandi\Downloads\SRG_VOLUME_II_v0.1_GPT_REVIEW_AND_CODEX_R1.zip')

def identity(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        while b:=f.read(1024*1024):h.update(b)
    return {'bytes':Path(p).stat().st_size,'sha256':h.hexdigest()}
def writej(name,x):
    (ROOT/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def put(name,b):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)

assert not (ROOT/'R1_STARTING_BASELINE.json').exists(), 'Do not overwrite an existing revision intake.'
expected={'manuscript.pdf':'1f625a35c76446769b473d01affc480c46f3a8738f9f43baef2b2e6313927f5d','manuscript.tex':'8a7c5747d77e4bfc62035381afbae236d0a1fbc9be29d5a22218bf07a717712c','SRG_VOLUME_II_SIM04_SIM05_CANDIDATE_v0.1_REVIEW.zip':'8eedae1f6b85519fed3053d592c1ca64d038135d4b9cf69fb1a8c2fbf52cc95c'}
for p,sha in expected.items():assert identity(OLD/p)['sha256']==sha,p
all_old=[{'path':p.relative_to(OLD).as_posix(),**identity(p)} for p in sorted(OLD.rglob('*')) if p.is_file()]
external=json.loads((OLD/'INPUT_BASELINE.json').read_text(encoding='utf-8'))+json.loads((OLD/'HANDOFF_BASELINE.json').read_text(encoding='utf-8'))
for row in external:
    got=identity(row['original_path'])
    assert all(got[k]==row[k] for k in ('bytes','sha256')),row['original_path']
writej('R1_STARTING_BASELINE.json',{'old_candidate_root':str(OLD),'old_candidate_all_files':all_old,'external_accepted_inputs':external,'r1_order_archive':{'path':str(REVIEW),**identity(REVIEW)},'expected_starting_identities':expected})

manifest=json.loads((OLD/'MANIFEST.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(OLD/'SRG_VOLUME_II_SIM04_SIM05_CANDIDATE_v0.1_REVIEW.zip') as z:
    assert z.testzip() is None
    assert set(z.namelist())=={r['path'] for r in manifest['files']}|{'MANIFEST.json'}
    for r in manifest['files']:
        b=z.read(r['path'])
        assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
        assert (OLD/r['path']).read_bytes()==b

regenerated={'manuscript.pdf','DOCUMENT_QA.json','PAGE_INSPECTION.json','FINAL_BUILD_RECEIPT.json','PRESERVATION_RECEIPT.json','finalize_package.py'}
legacy_tools={'prepare_manuscript.py','receive_review.py'}
for r in manifest['files']:
    rel=r['path'];b=(OLD/rel).read_bytes()
    if '/' not in rel:
        put('provenance/v0.1/'+rel,b) if rel!='manuscript.pdf' else None
    if rel not in regenerated|legacy_tools:
        put(rel,b)
put('provenance/v0.1/MANIFEST.json',(OLD/'MANIFEST.json').read_bytes())
put('provenance/v0.1/REVIEW_ZIP_IDENTITY.json',(OLD/'REVIEW_ZIP_IDENTITY.json').read_bytes())

with zipfile.ZipFile(REVIEW) as z:
    assert z.testzip() is None
    rm=json.loads(z.read('REVIEW_MANIFEST.json'))
    assert set(z.namelist())=={r['path'] for r in rm['files']}|{'REVIEW_MANIFEST.json'}
    for r in rm['files']:
        b=z.read(r['path'])
        assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'],r['path']
    for n in ['SRG_VOLUME_II_CODEX_EDITORIAL_R1.md','SRG_VOLUME_II_v0.1_GPT_MANUSCRIPT_REVIEW.md','SOURCE_READBACK_EXCERPTS.md','PROPOSED_E01_E03_SOURCE_CORRECTIONS.patch','GPT_REVIEW_RECEIPT.json','REVIEW_MANIFEST.json']:
        put('evidence/editorial/R1/'+n,z.read(n))
    patch=z.read('PROPOSED_E01_E03_SOURCE_CORRECTIONS.patch').decode('utf-8')
put('evidence/editorial/SRG_VOLUME_II_v0.1_GPT_REVIEW_AND_CODEX_R1.zip',REVIEW.read_bytes())

def apply_exact_patch(original,chunk):
    """Apply unified diff context literally, without Git or executable patch commands."""
    lines=original.splitlines(keepends=True);out=[];at=0
    h=re.compile(r'^@@ -(\d+)(?:,\d+)? \+\d+(?:,\d+)? @@.*$')
    for item in chunk.splitlines(keepends=True)[2:]:
        m=h.match(item.rstrip('\n'))
        if m:
            start=int(m[1])-1
            assert start>=at
            out.extend(lines[at:start]);at=start
        elif item.startswith(' '):
            assert lines[at]==item[1:],(at,item,lines[at]);out.append(lines[at]);at+=1
        elif item.startswith('-'):
            assert lines[at]==item[1:],(at,item,lines[at]);at+=1
        elif item.startswith('+'):out.append(item[1:])
        else:raise AssertionError(item)
    out.extend(lines[at:]);return ''.join(out)

chunks=re.split(r'(?=^--- a/)',patch,flags=re.M)
pure=[]
for chunk in chunks:
    if not chunk:continue
    name=chunk.splitlines()[0][6:]
    assert name in ('manuscript.tex','CLAIM_EVIDENCE_MATRIX.md'),name
    before=(OLD/name).read_text(encoding='utf-8')
    after=apply_exact_patch(before,chunk)
    put(name,after.encode('utf-8'))
    pure.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+name,tofile='b/'+name))
assert ''.join(pure)==patch, 'Source corrections must match the supplied patch exactly.'
put('SOURCE_CORRECTIONS_ONLY.patch',patch.encode('utf-8'))

tex=(ROOT/'manuscript.tex').read_text(encoding='utf-8')
replacements=[
 ('pdfsubject={Candidate v0.1 for scientific review; zero new simulations}', 'pdfsubject={Candidate v0.1.1 editorial R1, 24 October 2026, for scientific review; zero new simulations}'),
 ('\\fancyhead[R]{\\small\\sffamily Candidate v0.1}', '\\fancyhead[R]{\\small\\sffamily Candidate v0.1.1 / R1}'),
 ('\\textbf{Candidate manuscript v0.1 / 23 October 2026}', '\\textbf{Candidate manuscript v0.1.1 (editorial R1) / 24 October 2026}')]
for a,b in replacements:
    assert tex.count(a)==1,a
    tex=tex.replace(a,b)
put('manuscript.tex',tex.encode('utf-8'))
guide=(ROOT/'START_HERE.md').read_text(encoding='utf-8')
guide=guide.replace('**Candidate v0.1, dated 23 October 2026, for GPT and Hilmir review. Not publication accepted.**','**Candidate v0.1.1 (editorial R1), dated 24 October 2026, for GPT and Hilmir review. Not publication accepted.**')
guide += '\n## Editorial R1 only\n\nGPT accepted the v0.1 scientific core subject to E01–E03. This revision corrects the two mean/tensor descriptions and the three source ranges, with no changes to equations, numerical results, four propositions or ten figure assets. Final manuscript acceptance remains pending. The original v0.1 directory is preserved unchanged.\n\nSee [correction disposition](CORRECTION_DISPOSITION.md), [exact manuscript and claim-matrix diff](DIFF_FROM_v0.1.patch), [complete document diff](DOCUMENT_ONLY_DIFF_FROM_v0.1.patch), and [R1 order](evidence/editorial/R1/SRG_VOLUME_II_CODEX_EDITORIAL_R1.md). No new simulations, scientific checker executions, RNG draws, figures, Tower II investigation or Git/publication actions were performed. Stop for GPT and Hilmir review.\n'
put('START_HERE.md',guide.encode('utf-8'))
build=(ROOT/'build_document.py').read_text(encoding='utf-8')
build=build.replace("source = RESEARCH / 'PUBLICATION_PREPARATION_SIM04_SIM05_v0.1/cache/tectonic'","source = ROOT.parent / 'v0.1/cache/tectonic'")
put('build_document.py',build.encode('utf-8'))
writej('R1_INTAKE_RECEIPT.json',{'old_candidate_files_baselined':len(all_old),'old_payload_checked':len(manifest['files']),'old_manifest_and_zip_match':True,'r1_review_manifest_files_checked':len(rm['files']),'r1_review_crc':True,'source_patch_applied_exactly':True,'source_patch_sha256':identity(ROOT/'SOURCE_CORRECTIONS_ONLY.patch')['sha256'],'housekeeping_tex_replacements':replacements,'new_simulations':0,'scientific_runs':0,'rng_draws':0,'git_commands':0})
print(json.dumps({'prepared':str(ROOT),'preserved_v0_1_files':len(all_old),'exact_patch':True,'new_scientific_executions':0}))
