"""Final document/data verification. No scientific execution."""
from pathlib import Path
import json,re,hashlib,sys,zipfile,collections
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'packet/NCM_PAPER_01_Codex_Packet_v0.1'
sys.path.append(r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\site-packages')
from pypdf import PdfReader
findings=[]
def ok(name,condition):
    assert condition,name
    findings.append(name)
snap=json.loads((ROOT/'manuscript/content_snapshot.json').read_text())
tex=(ROOT/'manuscript/main.tex').read_text(encoding='utf-8')
refs={r[0] for r in snap['references']}
used=set(re.findall(r'\[@([A-Z0-9]+)\]',json.dumps(snap)))
ok('All citation IDs resolve',used<=refs and len(refs)==12)
index=(ROOT/'EVIDENCE_INDEX.md').read_text(encoding='utf-8')
ok('All evidence anchors exist',all(f'id="{r.lower()}"' in index for r in refs))
ok('All 30 equation blocks present in TeX',tex.count(r'\begin{equation}')==30)
ok('Seven table blocks',sum(b[0]=='table' for b in snap['blocks'])==7)
ok('Correct SRG product in final TeX',r'D=e^{-0.269}(0.382)^2' in tex)
ok('No erroneous grouped SRG exponent in final TeX',r'\exp[-0.269(0.382)^2]' not in tex)
ok('Sector review accepted', '**Disposition: ACCEPTED.**' in (ROOT/'proof_review/SECTOR_60_REVIEW.md').read_text(encoding='utf-8'))

analysis=json.loads((P/'context/NCM_DUAL_03_analysis_results.json').read_text(encoding='utf-8'))
ok('Historical outcome counts',analysis['stop_reasons']=={'max_iterations':1,'numerical_convergence':42,'line_search_failed':17})
ok('Historical trial counts',analysis['trial_reasons']=={'outside_B3':449,'nonpositive_fixed_gauge_pivot':273,'accepted':674,'insufficient_merit_decrease':1270})
ok('Historical iteration and call counts',all(analysis[k]==v for k,v in {
 'discovery_F_calls':8211,'iteration_passes':733,'newton_directions':691,
 'independent_regression_F_calls':126,'total_independent_regression_including_Stage_A':151,
 'lower_period_numerical_groups':7,'genuine_period_three_candidates':0}.items()))
groups=json.loads((ROOT/'evidence/RETAINED_GROUPS_EXTRACT.json').read_text())['groups']
members=[m['seed'] for g in groups for m in g['members']]
ok('Group memberships cover 42 distinct retained outcomes',len(members)==len(set(members))==42)
table4=next(b for b in snap['blocks'] if b[0]=='table' and b[1].startswith('Table 4.'))
expected=[[g['group'],g['representative_seed'],str(len(g['members'])),
           format(float(g['mu_three_angle_radians']),'.6g'),format(float(g['min_prestage_modulus']),'.6g'),
           format(float(g['max_H_separation']),'.3g')] for g in groups]
ok('All displayed Table 4 cells match retained records',table4[3]==expected)
sym=json.loads((ROOT/'proof_review/SYMBOLIC_RESULTS.json').read_text())
ok('29 supporting algebra checks passed',len(sym['checks'])==29 and all(c['passed'] for c in sym['checks']))
ok('Supporting checker records zero native calls',sym['native_F_evaluations']==0)

reader=PdfReader(str(ROOT/'manuscript/REVIEW.pdf'))
ok('Final PDF has 19 pages',len(reader.pages)==19)
ids={(p.indirect_reference.idnum,p.indirect_reference.generation) for p in reader.pages}
internal=external=0
for p in reader.pages:
    for ref in p.get('/Annots',[]):
        a=ref.get_object()
        if '/Dest' in a:
            target=a['/Dest'][0]
            okkey=(target.idnum,target.generation)
            assert okkey in ids
            internal+=1
        elif '/A' in a:
            uri=str(a['/A']['/URI'])
            path,fragment=uri.split('#')
            assert (ROOT/'manuscript'/path).resolve()==ROOT/'EVIDENCE_INDEX.md'
            assert f'id="{fragment}"' in index
            external+=1
ok('All 36 internal citations target PDF pages',internal==36)
ok('All 12 relative evidence links resolve locally',external==12)
renders=json.loads((ROOT/'qa/RENDER_FINAL.json').read_text())
ok('19 final page renders available',len(renders)==19)
ok('Final render images match recorded hashes',all(hashlib.sha256((ROOT/'qa'/name).read_bytes()).hexdigest()==sha for name,sha in renders.items()))
structure=json.loads((ROOT/'qa/PDF_STRUCTURE.json').read_text())
ok('Structural QA refers to final PDF',structure['pdf_sha256']==hashlib.sha256((ROOT/'manuscript/REVIEW.pdf').read_bytes()).hexdigest())

manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
ok('All bounded sources still unchanged',all(hashlib.sha256(Path(e['path']).read_bytes()).hexdigest()==e['before']['sha256'] for e in manifest['sources'].values()))
ok('All preserved packet members still unchanged',all(hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest()==e['before']['sha256'] for e in manifest['packet_members']))
required=['START_HERE.md','PLAIN_LANGUAGE_SUMMARY.md','CLAIM_SOURCE_MATRIX.md','NOVELTY_AND_PLACEMENT.md',
          'MANUSCRIPT_QA.md','CORRECTIONS_AND_DISPOSITION.md','EVIDENCE_INDEX.md','SOURCE_MANIFEST.json',
          'COMMANDS.txt','CLOSEOUT.txt','manuscript/main.tex','manuscript/references.bib','manuscript/REVIEW.pdf']
ok('Required pre-archive deliverables present',all((ROOT/n).is_file() for n in required))
out={'purpose':'Current document/data QA, not a scientific certificate','passed':findings,'failures':[],
     'native_F_evaluations':0,'old_scientific_scripts_executed':0}
(ROOT/'qa/REVIEW_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(f'{len(findings)} document/data/source checks passed; native calls 0; old scientific scripts 0.')
