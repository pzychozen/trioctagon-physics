from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,shutil,subprocess,sys,zipfile
import pypdf,matplotlib,numpy
R=Path(__file__).resolve().parents[1]; P=R/'packet'; V=R/'verification'
REPO=Path(r'C:\TORMENT\TRIOCTAGON_new\trioctagon-physics')
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def git(*args):return subprocess.run(['git',*args],cwd=REPO,capture_output=True,check=True).stdout
archive=R/'received/NATIVE_SPATIAL_WORK_CAUSAL_TRANSPORT_PUBLISH_01_CODEX_PACKET.zip'
manifest=json.loads((P/'PACKET_MANIFEST.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    names=[x for x in z.namelist() if not x.endswith('/')]
    assert len(names)==len(set(names))
    assert set(names)=={x['path'] for x in manifest['files']}|{'PACKET_MANIFEST.json'}
    for row in manifest['files']:
        p=P/row['path'];assert p.resolve().is_relative_to(P.resolve())
        assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],row
        assert z.read(row['path'])==p.read_bytes()
A=json.loads((P/'GPT_ACCEPTANCE.json').read_text(encoding='utf-8'))
for row in A['corrected_edition_files']:
    assert sha(P/row['path'])==row['sha256'] and (P/row['path']).stat().st_size==row['bytes']
old=P/A['submitted_archive']['path'];assert sha(old)==A['submitted_archive']['sha256']
changes=json.loads((P/'CORRECTIONS.json').read_text(encoding='utf-8'))
assert len(changes)==16 and len({x['file'] for x in changes})==7
grouped={}
for c in changes:grouped.setdefault(c['file'],[]).append(c)
display=re.compile(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}|\\\[.*?\\\]',re.S)
display_count=0; environment_display_count=0; input_count=0; unchanged=[]
with zipfile.ZipFile(old) as z:
    om=json.loads(z.read('MANIFEST.json'))
    for row in om['files']:
        data=z.read(row['path']); assert hashlib.sha256(data).hexdigest()==row['sha256']
    for p in (P/'corrected_edition/v0.1').rglob('*'):
        if not p.is_file():continue
        rel=p.relative_to(P/'corrected_edition/v0.1').as_posix()
        if p.suffix=='.pdf' and p.parent.name=='v0.1':continue
        original=z.read('candidate/v0.1/'+rel)
        if rel in grouped:
            text=original.decode('utf-8')
            for c in grouped[rel]:
                assert text.count(c['old'])==1,(rel,c['id'])
                text=text.replace(c['old'],c['new'])
            assert text.encode()==p.read_bytes(),rel
        else:assert original==p.read_bytes(),rel
        if p.suffix=='.tex':
            oldblocks=[m.group() for m in display.finditer(original.decode('utf-8'))]
            newblocks=[m.group() for m in display.finditer(p.read_bytes().decode('utf-8'))]
            assert oldblocks==newblocks,rel
            display_count+=len(oldblocks)
            environment_display_count+=sum(x.startswith(r'\begin') for x in oldblocks)
        if rel.startswith('figures/'):unchanged.append(rel)
    for p in (P/'inputs').rglob('*'):
        if p.is_file():assert p.read_bytes()==z.read(p.relative_to(P).as_posix());input_count+=1
    # Extract the old submitted package separately as historical evidence/helper source.
    B=R/'review_basis_extracted'
    for name in z.namelist():
        if name.endswith('/'):continue
        target=B/name;assert target.resolve().is_relative_to(B.resolve())
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():assert target.read_bytes()==z.read(name)
        else:target.write_bytes(z.read(name))
assert environment_display_count==79 and display_count==81 and input_count==84,(environment_display_count,display_count,input_count)
sid=json.loads((P/'inputs/SOURCE_IDENTITIES.json').read_text(encoding='utf-8'))
for row in sid['sources']:assert sha(P/'inputs'/row['path'])==row['sha256']
dl=Path(r'C:\Users\Notandi\Downloads')
separate=[('NATIVE_SPATIAL_WORK_CAUSAL_TRANSPORT_PUBLISH_01_CODEX_WORK_ORDER.md','CODEX_FIX_AND_PUBLISH_WORK_ORDER.md'),
 ('NATIVE_SPATIAL_WORK_CAUSAL_TRANSPORT_PAPER_01_GPT_REVIEW.md','GPT_MANUSCRIPT_REVIEW.md'),
 ('SPATIAL_WORK_CAUSAL_TRANSPORT_v0.1_GPT_REVIEWED.pdf',A['corrected_pdf']['path'])]
for name,path in separate:
    assert (dl/name).read_bytes()==(P/path).read_bytes(),name
    shutil.copyfile(dl/name,R/'received'/name)
sidecar=dl/(archive.name+'.sha256')
if sidecar.exists():assert sidecar.read_text().split()[0].lower()==sha(archive)
dump(V/'INPUT_IDENTITIES.json',{'checked_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INTERNAL_AND_ACCEPTANCE_IDENTITIES',
 'packet_sha256':sha(archive),'packet_bytes':archive.stat().st_size,'packet_members':len(names),
 'manifest_entries':len(manifest['files']),'external_checksum_sidecar_present':sidecar.exists(),
 'external_checksum_status':'Not supplied/found in Downloads; no external checksum match claimed.',
 'corrected_files_verified':len(A['corrected_edition_files']),'exact_replacements_verified':16,'changed_source_files':7,
 'display_math_environments_unchanged':environment_display_count,'additional_bracket_displays_unchanged':display_count-environment_display_count,'figure_assets_unchanged':unchanged,'input_members_unchanged':input_count,
 'source_identities_unchanged':len(sid['sources']),'standalone_attachments_match_packet':True,
 'original_review_archive_sha256':sha(old),'reference_pdf_sha256':A['corrected_pdf']['sha256'],
 'scientific_suites_rerun':False})
status=git('status','--porcelain=v1','-z');(V/'ORIGINAL_CHECKOUT_STATUS.bin').write_bytes(status)
head=git('rev-parse','HEAD').decode().strip();remote=git('rev-parse','origin/main').decode().strip()
dirty={}
for line in git('diff','--name-only','-z').decode().split('\0'):
    if line:dirty[line]=sha(REPO/line)
assert not git('diff','--cached','--name-only')
assert not git('ls-tree','--name-only','origin/main','papers/SPATIAL_WORK_CAUSAL_TRANSPORT').strip()
dump(V/'REPOSITORY_PREFLIGHT.json',{'observed_utc':datetime.now(timezone.utc).isoformat(),'original_checkout':str(REPO),
 'branch':git('branch','--show-current').decode().strip(),'head':head,'origin_main':remote,
 'unrelated_dirty_tracked_hashes':dirty,'status_file':'ORIGINAL_CHECKOUT_STATUS.bin','status_sha256':sha(V/'ORIGINAL_CHECKOUT_STATUS.bin'),
 'publication_target_absent':True,'staged_files_before':[],'plan':'Isolated detached worktree based on fetched origin/main; preserve original dirty checkout.'})
env={'observed_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'executable':sys.executable,
 'conda':os.environ['CONDA_DEFAULT_ENV'],'pypdf':pypdf.__version__,'matplotlib':matplotlib.__version__,'numpy':numpy.__version__,'tools':{}}
paths={'tectonic':r'C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe',
 'pdftoppm':r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe',
 'pdfinfo':r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe'}
for name,path in paths.items():
    cmd=[path,'--version' if name=='tectonic' else '-v'];x=subprocess.run(cmd,capture_output=True,text=True,check=True)
    env['tools'][name]={'command':cmd,'version':(x.stdout+x.stderr).strip(),'exit_status':x.returncode}
dump(V/'ENVIRONMENT.json',env)
print(json.dumps({'packet_members':len(names),'manifest_entries':len(manifest['files']),'exact_edits':16,'unchanged_display_blocks':display_count,
 'unchanged_inputs':input_count,'source_identities':len(sid['sources']),'origin_main':remote,'external_checksum_present':sidecar.exists()},indent=2))
