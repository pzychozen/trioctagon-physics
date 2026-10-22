"""Read-only, standard-library publication integrity checks. Never executes scientific code."""
from pathlib import Path
import hashlib,json,re,zipfile,urllib.parse,sys
ROOT=Path(__file__).resolve().parents[1]
PUB01_STATUS={
    'C07':{
        'support':'Volume I work order, Existing authority / Review status; ledger diff (historical SIM03 acceptance); provenance/editorial_closure/SRG_VOLUME_I_v0.1.1_GPT_EDITORIAL_CLOSURE.md (current manuscript status); instructions/PUBLICATION_WORK_ORDER.md (separate publication authority)',
        'limitation':'Scientific and editorial review is complete; provenance qualifications remain; publication requires separate authorization.'},
    'C102':{
        'claim':'Scientific/editorial review complete; wider SRG unfinished; publication and further experiments require separate authorization',
        'support':'Historical: User request; Volume I work order final stop; REVIEW_REPORT. Current: provenance/editorial_closure/SRG_VOLUME_I_v0.1.1_GPT_EDITORIAL_CLOSURE.md; instructions/PUBLICATION_WORK_ORDER.md',
        'limitation':'Publication and further experiments require separate authorization; no staging, commit, push, upload or new investigation.'}}
def digest(data):return hashlib.sha256(data).hexdigest()
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def check_file(p,row):
    assert p.is_file(),str(p)
    assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],str(p)
def verify(sealed=True):
    findings={'scope':'Static source, hash, archive and link checks only; no simulation or numerical scientific readback.'}
    baseline=ROOT/'provenance/accepted_editorial_v0.1.1.zip'
    assert sha(baseline)=='81fadcf432c9ecb6e9ed85ad65a30b17272a6039671eaec9d959b6aead1832d3'
    with zipfile.ZipFile(baseline) as z:
        ztext=lambda rel:z.read(rel).decode('utf-8').replace('\r\n','\n')
        assert z.testzip() is None
        accepted=json.loads(z.read('MANIFEST.json'))
        assert set(z.namelist())=={'MANIFEST.json'}|{r['path'] for r in accepted['package_files']}
        for r in accepted['package_files']:
            b=z.read(r['path']);assert len(b)==r['bytes'] and digest(b)==r['sha256']
        findings['accepted_archive_payloads']=len(accepted['package_files'])
        changed=[]
        for r in accepted['package_files']:
            rel=r['path']
            if rel.startswith('MANUSCRIPT/') and Path(rel).suffix in ['.tex','.png','.py']:
                if sha(ROOT/rel)!=r['sha256']:changed.append(rel)
        assert set(changed)=={'MANUSCRIPT/volume_i.tex','MANUSCRIPT/sections/01_scope.tex','MANUSCRIPT/sections/06_agenda.tex'},changed
        scope='MANUSCRIPT/sections/01_scope.tex'
        oldscope=ztext(scope);newscope=(ROOT/scope).read_text(encoding='utf-8')
        oldsentence='This manuscript itself\nis a draft awaiting review.'
        newsentence='Scientific and editorial\nreview is complete; publication requires separate authorization.'
        assert oldscope.count(oldsentence)==1
        assert newscope==oldscope.replace(oldsentence,newsentence),scope
        assert len(newscope.splitlines())==len(oldscope.splitlines())
        oldbytes=z.read(scope);newline=b'\r\n' if b'\r\n' in oldbytes else b'\n'
        before_bytes=oldsentence.encode('utf-8').replace(b'\n',newline)
        after_bytes=newsentence.encode('utf-8').replace(b'\n',newline)
        assert (ROOT/scope).read_bytes()==oldbytes.replace(before_bytes,after_bytes)
        chapter='MANUSCRIPT/sections/06_agenda.tex';old=ztext(chapter);new=(ROOT/chapter).read_text(encoding='utf-8')
        split='\\section{The review boundary}'
        assert old.split(split)[0]==new.split(split)[0]
        assert len(old.splitlines())==len(new.splitlines())
        assert new.split(split)[1].strip().endswith('\\claim{C102}')
        main='MANUSCRIPT/volume_i.tex'
        assert ztext(main).split('\\end{titlepage}',1)[1]==(ROOT/main).read_text(encoding='utf-8').split('\\end{titlepage}',1)[1]
        oldclaims=json.loads(z.read('records/claims.json'));newclaims=load(ROOT/'records/claims.json')
        assert len(oldclaims)==len(newclaims)==102
        for oldrow,newrow in zip(oldclaims,newclaims):
            assert newrow=={**oldrow,**PUB01_STATUS.get(oldrow['id'],{})},oldrow['id']
        assert {a['id'] for a,b in zip(oldclaims,newclaims) if a!=b}=={'C07','C102'}
        findings['PUB01_exact_status_records_verified']=['C07','C102']
        findings['other_claim_records_unchanged']=100
        for rel in ['records/figures.json','tools/build_pdf.py','tools/acquire_typesetter.py']:
            assert (ROOT/rel).read_bytes()==z.read(rel),rel
        math_count=0
        for p in (ROOT/'MANUSCRIPT/sections').glob('*.tex'):
            rel=p.relative_to(ROOT).as_posix();pat=r'\\begin\{(equation\*?|align\*?)\}(.*?)\\end\{\1\}'
            a=re.findall(pat,ztext(rel),re.S);b=re.findall(pat,p.read_text(encoding='utf-8'),re.S)
            assert a==b,rel;math_count+=len(a)
        assert math_count==16
        findings.update(changed_latex_files=changed,display_math_environments_unchanged=math_count)
    # Frozen pre-correction records provide a second comparison, against the reviewed publication.
    with zipfile.ZipFile(ROOT/'provenance/pre_PUB01/submitted_publication_records.zip') as z:
        assert z.testzip() is None
        assert digest(z.read('PUBLICATION_FILE_MANIFEST.json'))=='d7ff67b5b1383f8d8d38b17f6081ab7c5234f66b22ff70b9948eda7b08d9ccab'
        previous={r['path']:r for r in json.loads(z.read('PUBLICATION_FILE_MANIFEST.json'))['files']}
        for rel in z.namelist():
            if rel=='PUBLICATION_FILE_MANIFEST.json':continue
            data=z.read(rel);assert len(data)==previous[rel]['bytes'] and digest(data)==previous[rel]['sha256'],rel
        assert (ROOT/'MANUSCRIPT/sections/06_agenda.tex').read_bytes()==z.read('MANUSCRIPT/sections/06_agenda.tex')
        prior_matrix=z.read('CLAIM_EVIDENCE_MATRIX.md').decode('utf-8').replace('\r\n','\n')
        expected_matrix=prior_matrix
        for claim_id,fields in PUB01_STATUS.items():
            row=next(line for line in prior_matrix.splitlines() if line.startswith('| '+claim_id+' |'))
            cells=row.split(' | ')
            for field,index in [('claim',1),('support',3),('limitation',4)]:
                if field in fields:cells[index]=fields[field]
            expected_matrix=expected_matrix.replace(row,' | '.join(cells))
        assert (ROOT/'CLAIM_EVIDENCE_MATRIX.md').read_text(encoding='utf-8')==expected_matrix
        findings['PUB01_matrix_only_two_rows_changed']=True
        findings['section_6_6_unchanged_since_submission']=True
    closure=ROOT/'provenance/editorial_closure'
    for r in load(closure/'CLOSURE_MANIFEST.json')['files']:check_file(closure/r['path'],r)
    findings['editorial_closure_payloads']=4
    count=0;studies=[]
    for base in sorted((ROOT/'evidence/SRG_REDISCOVERY').glob('SRG_SIMULATION_*')):
        if not base.is_dir():continue
        m=load(base/'MANIFEST.json');rows=m.get('package_files',m.get('files'))
        for r in rows:check_file(base/r['path'],r)
        count+=len(rows);studies.append({'study':base.name,'verified_payloads':len(rows)})
    assert count==374 and len(studies)==4
    findings['study_payloads']=count;findings['studies']=studies
    for r in load(ROOT/'records/evidence_copy_manifest.json'):check_file(ROOT/r['publication_path'],r)
    external=load(ROOT/'records/external_evidence.json')
    for r in external:check_file(ROOT/r['path'],r)
    assert len(external)==66;findings['indexed_external_evidence_included']=len(external)
    claims=load(ROOT/'records/claims.json');assert len(claims)==102
    assert len({r['id'] for r in claims})==102
    for r in claims:
        for loc in r['manuscript_locations']:
            lines=(ROOT/loc['file']).read_text(encoding='utf-8').splitlines()
            assert '\\claim{'+r['id']+'}' in lines[loc['line']-1],r['id']
    figs=load(ROOT/'records/figures.json');assert len(figs)==17
    assets=0
    for f in figs:
        assert (ROOT/'MANUSCRIPT/figures'/f"{f['id']}.tex").is_file()
        for a in f['assets']:
            assert sha(ROOT/'MANUSCRIPT/figures'/a['asset'])==a['sha256']
            assert sha(ROOT/'evidence/SRG_REDISCOVERY'/a['source'])==a['source_sha256']
            assets+=1
    assert assets==35
    tex='\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'MANUSCRIPT').rglob('*.tex'))
    labels=re.findall(r'\\label\{([^}]+)\}',tex);refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',tex)
    assert len(labels)==len(set(labels))==63 and set(refs)<=set(labels)
    bib=re.findall(r'\\bibitem\{([^}]+)\}',tex);assert len(bib)==12
    cites=[key for group in re.findall(r'\\cite\{([^}]+)\}',tex) for key in group.split(',')]
    assert set(cites)<=set(bib)
    findings.update(claim_locations_verified=102,figures_verified=17,figure_assets_verified=35,unique_labels=63,resolved_label_references=len(refs),bibliography_entries=12)
    links=[];external_links=[]
    for p in ROOT.rglob('*.md'):
        text=p.read_text(encoding='utf-8-sig')
        for raw in re.findall(r'\]\(([^)]+)\)',text):
            raw=raw.strip().strip('<>');url=urllib.parse.urlparse(raw)
            if url.scheme or raw.startswith('//'):
                external_links.append({'file':p.relative_to(ROOT).as_posix(),'target':raw});continue
            path=urllib.parse.unquote(raw.split('#')[0]);q=(p.parent/path).resolve() if path else p
            assert q.is_relative_to(ROOT),('Link escapes payload',p,raw)
            assert q.exists(),('Missing link',p,raw)
            rel=q.relative_to(ROOT);cur=ROOT
            for part in rel.parts:
                assert part in {x.name for x in cur.iterdir()},('Case-sensitive link mismatch',p,raw)
                cur=cur/part
            if '#L' in raw:
                fragment=raw.split('#',1)[1];match=re.fullmatch(r'L(\d+)(?:-L(\d+))?',fragment)
                if match:assert max(int(x) for x in match.groups() if x)<=len(q.read_text(encoding='utf-8').splitlines())
            links.append({'document':p.relative_to(ROOT).as_posix(),'target':raw})
    findings['local_markdown_links_verified']=len(links);findings['link_targets']=links
    findings['external_links_not_live_tested']=external_links
    pdf=load(ROOT/'records/pdf_comparison.json')
    assert sha(ROOT/'MANUSCRIPT/volume_i.pdf')==pdf['pdf_sha256']
    assert pdf['physical_pages']==53 and pdf['numbered_figures_in_compiler_list']==17
    visual=load(ROOT/'records/visual_review.json');assert visual['pdf_sha256']==pdf['pdf_sha256'] and visual['result']=='PASS'
    findings['pdf_sha256']=pdf['pdf_sha256'];findings['pages']=53
    if sealed:
        manifest=load(ROOT/'PUBLICATION_FILE_MANIFEST.json');rows=manifest['files']
        actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
        assert actual=={r['path'] for r in rows}|{'PUBLICATION_FILE_MANIFEST.json'},('Manifest membership mismatch',actual^{r['path'] for r in rows})
        for r in rows:check_file(ROOT/r['path'],r)
        sums=(ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines()
        expected={r['path']:r['sha256'] for r in rows if r['path']!='SHA256SUMS.txt'}
        parsed={line[66:]:line[:64] for line in sums};assert parsed==expected
        findings['publication_manifest_payloads_verified']=len(rows)
        findings['publication_manifest_sha256']=sha(ROOT/'PUBLICATION_FILE_MANIFEST.json')
    findings['all_assertions_passed']=True
    return findings
if __name__=='__main__':
    result=verify(sealed='--unsealed' not in sys.argv)
    print(json.dumps({k:v for k,v in result.items() if k not in ['link_targets','external_links_not_live_tested']},indent=2))
