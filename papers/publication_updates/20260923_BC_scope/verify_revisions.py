"""Bounded publication-content/layout checks. No algebra, kernels or figure generation.

Works in the actual checkout or in a minimal baseline-plus-proposal copy.
Writes only this packet's attributed verification receipt.
"""
from pathlib import Path
import hashlib,json,re,unicodedata
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
record=json.loads((ROOT/'evidence/five_approved_additions.json').read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def normalize(s):return re.sub(r'[\s‐‑–—-]','',unicodedata.normalize('NFKC',s))
specs={
'B':('papers/PAPER_B/publication/v0.1.2','PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md','PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.pdf','REFERENCES_v0.1.2.md',26,5),
'C':('papers/PAPER_C/publication/v1.0.1','PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md','PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_v1.0.1.pdf','REFERENCES_v1.0.1.md',28,0)}
dpath=REPO/'papers/PAPER_D/v0.1.1/publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf'
assert sha(dpath)==record['D_approved_sha256']=='7c4c52f8018765b21a7849d03ce7974824351e5af27c99356c5acb0b5dcaaaaf'
results={}
for name,(folder,mdname,pdfname,refname,math_count,fig_count) in specs.items():
    root=REPO/folder;md=(root/mdname).read_text(encoding='utf-8');restored=md
    original_path=REPO/record['baseline_'+name+'_source']['path'];original=original_path.read_text(encoding='utf-8')
    assert sha(original_path)==record['baseline_'+name+'_source']['sha256']
    insertions=[x for x in record['insertions'] if x['id'].startswith(name)]
    for item in insertions:
        assert md.count(item['inserted_prose'])==1,item['id']
        restored=restored.replace('\n\n'+item['inserted_prose'],'',1)
    restored=restored.rsplit('\n\n**[PD]**',1)[0].rstrip()+'\n'
    if name=='B':
        restored=restored.replace('Publication revision v0.1.2 - 23 September 2026','Publication revision v0.1.1 - 23 September 2026').replace('](../../figures/','](figures/')
    else:
        restored=restored.replace('The existing background references and their verification note remain in the companion [bibliography](../../PAPER_C_REFERENCES_v0.2.md). These references supply background and terminology, not a model-specific theorem of this paper. The added [PD] reference identifies the approved scaffold comparison and its separate construction.',
            'Full metadata (with DOIs and the verification note) is in the companion `PAPER_C_REFERENCES_v0.2.md`. All references are background / terminology; none supports a model-specific theorem of this paper.')
    assert restored.rstrip()==original.rstrip(),'Unexpected source change '+name
    assert re.findall(r'\$\$(.*?)\$\$',restored,re.S)==re.findall(r'\$\$(.*?)\$\$',original,re.S)
    refs=md.split('## References\n',1)[1].strip();companion=(root/refname).read_text(encoding='utf-8').split('\n\n',1)[1].strip()
    assert refs==companion
    links=[]
    for target in re.findall(r'\]\(([^)]+)\)',md):
        if '://' in target or target.startswith('#'):continue
        path=(root/target.split('#',1)[0]).resolve();assert path.is_file(),(name,target)
        assert path.is_relative_to(REPO.resolve());links.append(path.relative_to(REPO.resolve()).as_posix())
    reader=PdfReader(root/pdfname);pages=[p.extract_text() for p in reader.pages];text='\n'.join(pages)
    assert '\ufffd' not in text
    assert not re.search(r'[A-Za-z]:[\\/]',text)
    for i,p in enumerate(pages,1):assert p.strip().splitlines()[-1].strip()==str(i),(name,i,'footer')
    assert '[PD]' in text and 'revision v0.1.1' in text
    snippets={}
    for item in insertions:
        needle=normalize(item['inserted_prose'][:55]);hits=[i for i,p in enumerate(pages,1) if needle in normalize(p)]
        assert len(hits)==1,(name,item['id'],hits);snippets[item['id']]=hits[0]
    actions=[];Dlinks=[]
    for page in reader.pages:
        for ann in page.get('/Annots',[]):
            a=ann.get_object().get('/A')
            if not a:continue
            a=a.get_object();target=str(a.get('/F',a.get('/URI','')))
            if 'PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf' in target:
                assert (root/target).resolve()==dpath.resolve();assert (root/target).is_file();Dlinks.append(target)
            actions.append(str(a.get('/S')))
    assert Dlinks,(name,'missing resolvable D PDF annotation')
    log=(root/f'paper_{name}_final.log').read_text(encoding='utf-8',errors='replace')
    problems=[x for x in log.splitlines() if any(t in x for t in ['Overfull','Missing character','! LaTeX Error','undefined references'])];assert not problems,problems
    widths=re.findall(r'PAPER-EQUATION-WIDTH: ([\d.]+)pt; available ([\d.]+)pt; tag([^\r\n]*)',log)
    assert len(widths)==math_count,(name,len(widths))
    old_layout=json.loads((ROOT/'evidence/predecessor_equation_layout.json').read_text())[name]
    assert [list(x) for x in widths]==old_layout['width_records'],(name,'changed equation widths')
    inherited_scaled=[i+1 for i,(a,b,_) in enumerate(widths) if float(a)>.90*float(b)]
    assert inherited_scaled==old_layout['already_scaled_blocks']
    if name=='B':
        assert re.findall(r'\\tag\{(\d+)\}',md)==list(map(str,range(1,27)))
        statements=re.findall(r'\*\*((?:Proposition|Theorem) \d+)',md)
        assert len(statements)==7
        for label in statements:assert label in text
        for i in range(1,6):assert 'Figure '+str(i)+':' in text
    else:
        statements=re.findall(r'\*\*(Theorem \d+b?)',md)
        assert len(statements)==7,(name,statements)
        for label in statements:assert label in text
        assert len(reader.named_destinations)>=14
    results[name]={'PASS':True,'pages':len(pages),'pdf_sha256':sha(root/pdfname),'manuscript_sha256':sha(root/mdname),
       'approved_additions_at_pages':snippets,'original_content_exact_after_reversing_documented_changes':True,
       'original_display_math_blocks':math_count,'original_statement_labels':statements,'original_figure_count':fig_count,
       'equation_widths_unchanged_from_predecessor':True,'additional_equation_scaling':False,'inherited_scaled_display_blocks':inherited_scaled,'references_match_companion':True,'relative_links_resolve':links,
       'D_PDF_annotation_targets':Dlinks,'consecutive_page_footers':True,'overfull_or_missing_glyph_warnings':problems}
out={'attribution':'New Codex bounded B/C publication verification; distinct from GPT review','D_PDF_not_regenerated':True,
     'D_PDF_approved_sha256':sha(dpath),'new_scientific_execution':False,'papers':results}
(ROOT/'evidence/bounded_verification.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,ensure_ascii=False))
