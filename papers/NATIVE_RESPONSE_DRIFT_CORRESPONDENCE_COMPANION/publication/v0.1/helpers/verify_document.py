"""Document-only PDF/source verification, crosswalk generation and page rendering.
Never imports or executes historical scientific checkers.
"""
from pathlib import Path
import os,sys,re,json,hashlib,subprocess,shutil,argparse
from pypdf import PdfReader
O=Path(__file__).resolve().parents[1];V=O/'verification';V.mkdir(exist_ok=True)
ap=argparse.ArgumentParser();ap.add_argument('--build-dir',required=True);args=ap.parse_args();B=Path(args.build_dir)
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
pdf=O/'NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_COMPANION_v0.1.pdf';reader=PdfReader(pdf)
tex=(O/'manuscript/main.tex').read_text(encoding='utf-8');bib=(O/'manuscript/references.tex').read_text(encoding='utf-8')
aux=(B/'main.aux').read_text(encoding='utf-8');log=(B/'main.log').read_text(encoding='utf-8');receipt=json.loads((B/'BUILD_RECEIPT.json').read_text())
assert receipt['exit_status']==0 and receipt['pdf_sha256']==sha(pdf)
for p,h in receipt['source_hashes'].items():assert sha(O/p)==h
assert not re.search(r'Overfull|Underfull|undefined|Missing character|Font Warning|LaTeX Warning|Package .+ Warning',log)
labels=re.findall(r'\\label\{([^}]+)\}',tex);assert len(labels)==len(set(labels))
labelmap={m[0]:dict(number=m[1],page=int(m[2])) for m in re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{(\d+)\}',aux)}
assert all(l in labelmap for l in labels)
for l in labels:labelmap[l]['source_line']=next(i for i,s in enumerate(tex.splitlines(),1) if '\\label{'+l+'}' in s)
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex);assert set(refs)<=set(labels)
keys=re.findall(r'\\bibitem\{([^}]+)\}',bib);assert len(keys)==len(set(keys))
cites={c for x in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',tex) for c in x.split(',')};assert cites==set(keys)
assert all('\\bibcite{'+k+'}' in aux for k in keys)
links=[]
for target in re.findall(r'\\href\{([^}]+)\}',tex+bib):
    p=(O/target).resolve();assert p.is_relative_to(O.resolve()) and p.is_file(),target
    links.append(dict(target=target,sha256=sha(p),exists=True))
fonts={};annotations=[];pages=[]
renderdir=V/'pages';renderdir.mkdir(exist_ok=True)
for n,page in enumerate(reader.pages,1):
    t=page.extract_text();assert len(t)>900 and '??' not in t and '\ufffd' not in t
    assert t.rstrip().endswith(str(n)),(n,t[-50:])
    (V/f'page-{n:02d}.txt').write_text(t,encoding='utf-8')
    pages.append(dict(page=n,text_characters=len(t),footer_verified=True,width=float(page.mediabox.width),height=float(page.mediabox.height)))
    for name,ref in page['/Resources'].get_object().get('/Font',{}).get_object().items():
        f=ref.get_object();base=str(f.get('/BaseFont'));desc=f.get('/FontDescriptor')
        if not desc and '/DescendantFonts' in f:desc=f['/DescendantFonts'][0].get_object().get('/FontDescriptor')
        assert desc,base
        desc=desc.get_object();embedded=any(k in desc for k in ['/FontFile','/FontFile2','/FontFile3']);assert embedded,base
        fonts[base]=dict(subtype=str(f['/Subtype']),embedded=embedded,to_unicode='/ToUnicode' in f)
    for ar in page.get('/Annots',[]):
        a=ar.get_object();action=a.get('/A',{}).get_object();uri=action.get('/URI')
        if uri:assert (O/str(uri)).is_file(),uri
        annotations.append(dict(page=n,subtype=str(a.get('/Subtype')),action=str(action.get('/S')),uri=str(uri) if uri else None))
assert reader.metadata.title=='Local Correspondence Between In-Phase Response Asymmetry and Chiral Common-Phase Drift in the Native Triad'
assert reader.metadata.author=='Hilmir Frímann Halldórsson (pzychozen)'
assert reader.metadata.subject=='Project-internal manuscript review complete; author-authorized repository research edition v0.1; 15 November 2026'
tool=shutil.which('pdftoppm');assert tool
cmd=[tool,'-r','130','-png',str(pdf),str(renderdir/'page')]
q=subprocess.run(cmd,capture_output=True,check=True,timeout=120)
images=sorted(renderdir.glob('page-*.png'));assert len(images)==len(reader.pages)
save(V/'RENDER_RECORD.json',dict(command=cmd,exit_status=q.returncode,pdf_sha256=sha(pdf),pages=[dict(path=p.relative_to(O).as_posix(),sha256=sha(p)) for p in images]))
proof=O/'evidence/accepted/submitted/PROOF_REPORT.md';pt=proof.read_text(encoding='utf-8')
eqmaps={1:['eq:pre','eq:post'],2:['eq:positive-factors'],3:['eq:fixed'],4:['prop:domain'],5:['eq:tangent'],6:['eq:gauge'],7:['eq:uniform'],8:['eq:cartesian','eq:pre-response','eq:B'],9:['eq:J'],10:['eq:orientation','eq:normalization'],11:['eq:cycle-factor','eq:Kh'],12:['eq:Dentries'],13:['eq:k-radius','eq:pair'],14:['eq:A','eq:minus'],15:['eq:SC'],16:['eq:aC'],17:['eq:cD','eq:quotient-taylor'],18:['sec:coefficients'],19:['eq:aCbound'],20:['eq:zeros'],21:['eq:ratio'],22:['eq:theta-leading'],23:['eq:generator-limit'],24:['eq:hzero-values'],25:['eq:C-scaling','eq:nu-scaling','eq:omega-scaling']}
equations=[]
for num,ls in eqmaps.items():
    line=next(i for i,s in enumerate(pt.splitlines(),1) if '\\tag{'+str(num)+'}' in s)
    places=[dict(label=l,**labelmap[l]) for l in ls]
    if num in [4,18]:
        marker='Its radius derivative' if num==4 else 'Along $\\xi='
        places[0]['source_line']=next(i for i,s in enumerate(tex.splitlines(),1) if marker in s)
    equations.append(dict(accepted_equation=num,accepted_source_line=line,manuscript=places,review='Manual comparison to preserved equation and surrounding hypotheses; documentary transcription, no algebra recomputation.'))
claimgroups={
'RD01':['sec:setting','eq:family','eq:pre','eq:post','eq:references','eq:relative','eq:gauge','sec:domain','prop:domain','eq:tangent','eq:fixed','eq:divided','eq:border','eq:uniform'],
'RD02':['sec:response','eq:cartesian','eq:pre-response','eq:B','eq:J','eq:orientation','eq:normalization','eq:cycle-factor','eq:Kh','eq:Dentries','sec:coefficients','eq:k-radius','eq:pair','eq:A','eq:minus','eq:SC','eq:aC','eq:cD','eq:quotient-taylor'],
'RD03':['thm:correspondence','eq:positive-factors','eq:zeros','eq:ratio','sec:division','sec:positivity','eq:aCbound','eq:bound-identity','eq:cDbound','eq:theta-leading','rem:radius'],
'RD04':['sec:limit','tab:generator','eq:generator-limit','eq:hzero-values','eq:C-scaling','eq:nu-scaling','eq:omega-scaling','eq:generator-state'],
'RD05':['sec:selection','eq:assigned','tab:states','eq:conditioned','sec:reconstruction-limit']}
ledger=json.loads((O/'evidence/accepted/submitted/CLAIM_LEDGER.json').read_text())
claims=[]
for c in ledger['claims']:
    ev=['evidence/accepted/submitted/'+p for p in c['evidence']]
    assert all((O/p).is_file() for p in ev)
    claims.append(dict(id=c['id'],title=c['title'],manuscript=[dict(label=l,**labelmap[l]) for l in claimgroups[c['id']]],proof_sections=c['report_sections'],proof_equations=c.get('report_equations',[]),inherited=c['inherited'],accepted_comparison_contribution=c['new'],hypotheses=c['hypotheses'],limitations=c['limitations'],evidence=ev,acceptance='evidence/accepted/NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_GPT_REVIEW.md'))
cross=dict(pdf_sha256=sha(pdf),main_tex_sha256=sha(O/'manuscript/main.tex'),proof_report_sha256=sha(proof),status='Scientific claims accepted; manuscript review complete; author-authorized repository publication',claims=claims,accepted_equation_transcription=equations,notation=[
dict(source='h / h_step',manuscript='h, called h_step in prose/code',meaning='Mathematical step; not geometric length or physical clock'),
dict(source='mathsf B_r, mathsf G_r',manuscript='bold B_r, bold G_r',meaning='Same matrices; font-only change'),
dict(source='assigned D_r',manuscript='calligraphic D_r',meaning='Scalar assigned diagnostic, distinct from matrix D_h and positive pair denominator D_ij'),
dict(source='increasing-pair Vandermonde',manuscript='-A',meaning='Orientation preserved'),
dict(source='nu and omega',manuscript='nu and omega=h nu',meaning='Extended rate versus actual per-update advance')])
save(O/'CLAIM_SOURCE_CROSSWALK.json',cross)
save(V/'LABELS.json',labelmap)
table_blocks=re.findall(r'\\begin\{table\}.*?\\end\{table\}',tex,re.S)
table_hashes=[dict(label=re.search(r'\\label\{([^}]+)\}',b)[1],sha256_utf8=hashlib.sha256(b.encode()).hexdigest()) for b in table_blocks]
save(V/'DOCUMENT_CHECKS.json',dict(status='PASS',pdf_sha256=sha(pdf),page_count=len(reader.pages),metadata=dict(reader.metadata),labels=len(labels),references=len(refs),bibliography_entries=len(keys),claim_locations=sum(len(c['manuscript']) for c in claims),accepted_equation_groups=len(equations),tables=len(table_blocks),table_source_hashes=table_hashes,fonts=fonts,relative_source_links=links,pdf_annotations=annotations,pages=pages,final_tex_warning_count=0,scientific_runs=0,limitations='Document checks do not constitute a new scientific or GPT manuscript acceptance. Separate visual record binds all rendered final pages.'))
out=O/'records/build';out.mkdir(parents=True,exist_ok=True)
for p in B.iterdir():
    if p.is_file() and p.name in ['BUILD_RECEIPT.json','compiler.stdout','compiler.stderr','main.log','main.aux']:shutil.copyfile(p,out/p.name)
print(json.dumps(dict(status='PASS',pages=len(reader.pages),labels=len(labels),fonts=len(fonts),citations=len(keys),source_links=len(links),claim_locations=sum(len(c['manuscript']) for c in claims))))
