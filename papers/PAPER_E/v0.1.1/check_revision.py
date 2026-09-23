"""E-01/E-02 witness and bounded edition checks; no trajectory or GPT-checker run."""
import runtime
from runtime import ROOT
from pathlib import Path
import ast,argparse,hashlib,json,re,sys
import numpy as np
from pypdf import PdfReader

PARENT=ROOT.parent
SRC=PARENT/'evidence/source_snapshots/staged'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks={}
def check(name,value):
    checks[name]=bool(value)
    assert value,name
def function(path,name):
    tree=ast.parse(path.read_text(encoding='utf-8'))
    return next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name)
def isolated_body(path,name):
    node=function(path,name)
    namespace={'np':np}
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(path),'exec'),namespace)
    return namespace[name]

# Only these two previously inspected function bodies execute. Their modules,
# imports, GUI, model runner and all optional consumers are not executed.
phase_path=SRC/'phase_triad_sync.py';display_path=SRC/'toy_3d_triocta.py'
sync=isolated_body(phase_path,'apply_phase_triad_sync')
display=isolated_body(display_path,'embed_on_torus')
zeros=[complex(0.,0.),complex(-0.,0.),complex(0.,-0.),complex(-0.,-0.)]
angles=np.angle(np.array(zeros,dtype=np.complex128))
check('signed_zero_phases',np.array_equal(angles,np.array([0.,np.pi,-0.,-np.pi])))
check('negative_zero_phase_signbit',bool(np.signbit(angles[2])))
plus=np.array([zeros[0],np.exp(1j*np.pi/6),1.],dtype=np.complex128)
minus=np.array([zeros[1],np.exp(1j*np.pi/6),1.],dtype=np.complex128)
check('same_complex_state_different_zero_bits',np.array_equal(plus,minus) and not np.signbit(plus[0].real) and np.signbit(minus[0].real))
lam=.001;out_plus=sync(plus,lam);out_minus=sync(minus,lam)
distance=float(abs(out_plus[1]-out_minus[1]));expected=float(2*np.sin(lam))
check('zero_phase_changes_nonzero_neighbour',np.isclose(distance,expected,rtol=0,atol=1e-14))
check('magnitude_preserved_for_both_zero_choices',np.allclose(abs(out_plus),abs(plus),rtol=0,atol=1e-14) and np.allclose(abs(out_minus),abs(minus),rtol=0,atol=1e-14))
check('phase_off_identity_bypass',sync(plus,0.) is plus and sync(minus,0.) is minus)
xyzplus=display(plus[None,:]);xyzminus=display(minus[None,:])
pplus=np.array([c[0,0] for c in xyzplus]);pminus=np.array([c[0,0] for c in xyzminus])
check('display_zero_phase_point',np.allclose(pplus,[2.6,0,0],rtol=0,atol=1e-14))
check('display_signed_zero_alternative_point',np.allclose(pminus,[1.4,0,0],rtol=0,atol=1e-14))

def phi_divisor(path,name):
    node=function(path,name)
    assignment=next(n for n in node.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='phi' for t in n.targets))
    assert isinstance(assignment.value,ast.BinOp) and isinstance(assignment.value.op,ast.Div)
    return ast.unparse(assignment.value.right)
cyl3=phi_divisor(SRC/'geometry_3d.py','history_to_xyz')
cylalt=phi_divisor(SRC/'geometry_embeddings.py','history_to_xyz')
torusalt=phi_divisor(SRC/'geometry_embeddings.py','history_to_torus_xyz')
check('both_cylinders_literal_twelve',cyl3=='12.0' and cylalt=='12')
check('alternate_torus_config_n_sectors',torusalt=='config.n_sectors')
source_ids={p.name:sha(p) for p in [phase_path,display_path,SRC/'geometry_3d.py',SRC/'geometry_embeddings.py']}
provenance=json.loads((PARENT/'evidence/source_provenance.json').read_text())
for row in provenance['copies']:
    check('original_copy_'+row['copy'],sha(PARENT/row['copy'])==row['sha256'])

old=(PARENT/'PAPER_E_Z_MANIFOLD_v0.1.md').read_text(encoding='utf-8')
new=(ROOT/'PAPER_E_Z_MANIFOLD_v0.1.1.md').read_text(encoding='utf-8')
equations=lambda s:re.findall(r'\$\$\s*(.*?)\s*\$\$',s,re.S)
check('40_display_equations_unchanged',len(equations(old))==40 and equations(old)==equations(new))
named=lambda s:re.findall(r'\*\*(?:Theorem|Proposition) \d+.*?(?=\n\n)',s,re.S)
check('13_named_statements_unchanged',len(named(old))==13 and named(old)==named(new))
check('11_figure_references_unchanged',re.findall(r'figures/[^)]+',old)==re.findall(r'figures/[^)]+',new) and len(re.findall(r'figures/[^)]+',new))==11)
check('E01_wording_present',all(x in new for x in ['signed-zero','arg0','lines 13-14','phase extraction at line 315']))
check('E02_wording_present','Only that module\'s alternate torus helper reads' in new and 'also hardcodes twelve sectors' in new)
check('E03_current_entries_correct',all('Example 3(iv)' not in (ROOT/f).read_text(encoding='utf-8') and 'Example 2(iv)' in (ROOT/f).read_text(encoding='utf-8') for f in ['PAPER_E_Z_MANIFOLD_v0.1.1.md','REFERENCE_LEDGER.md','references.bib']))
check('E04_scope_narrowed','That mechanism is proved possible by Section 9' not in new and 'attributing a recorded event to this mechanism requires the corresponding component data' in new)
check('reviewed_predecessor_pdf',sha(PARENT/'publication/PAPER_E_Z_MANIFOLD_v0.1.pdf')=='0d2a1e0b40d96f39c3929ad3c0a3c833b7eebebffc336b452ea9e1004f88880d')
check('reviewed_predecessor_allowlist',sha(PARENT/'PROPOSED_GIT_ALLOWLIST.txt')=='c6bf329d695a111da9e7f808e726df2d895f444cd8d07caaebc29b4ecec8260f')
for line in (PARENT/'SHA256SUMS.txt').read_text().splitlines():
    h,f=line.split('  ',1);assert sha(PARENT/f)==h,f
check('89_predecessor_manifest_entries',len((PARENT/'SHA256SUMS.txt').read_text().splitlines())==89)
for row in json.loads((ROOT/'evidence/review_input_identities.json').read_text())['review_evidence']:
    check('GPT_evidence_'+Path(row['copy']).name,sha(ROOT/row['copy'])==row['sha256'])
pdf=ROOT/'publication/PAPER_E_Z_MANIFOLD_v0.1.1.pdf';pages=len(PdfReader(pdf).pages)
build=json.loads((ROOT/'publication/build_record.json').read_text())
check('built_pdf_hash',sha(pdf)==build['pdf_sha256'])
check('built_manuscript_hash',sha(ROOT/'PAPER_E_Z_MANIFOLD_v0.1.1.md')==build['manuscript_sha256'])
check('built_TeX_hash',sha(ROOT/'paper_E_v0.1.1.tex')==build['tex_sha256'])
fidelity=json.loads((ROOT/'evidence/structural_fidelity.json').read_text())
check('full_equation_and_figure_fidelity',fidelity['all_equation_bodies_retained'] and fidelity['display_blocks']==40 and fidelity['figures']==11)
log=(ROOT/'publication/paper_E_v0.1.1.log').read_text(errors='replace')
check('no_overfull_or_missing_glyph',not re.search(r'Overfull|Missing character',log))
args=argparse.ArgumentParser();args.add_argument('--output',default=str(ROOT/'evidence/codex_revision_checks.json'));a=args.parse_args()
record={'attribution':'New Codex v0.1.1 bounded check; not execution of GPT checker or historical trajectories',
 'python':sys.version,'numpy':np.__version__,'checks':checks,'passed':sum(checks.values()),'pdf_pages':pages,
 'source_sha256':source_ids,'signed_zero_angles':angles.tolist(),'signed_zero_angle_signbits':np.signbit(angles).tolist(),
 'nonzero_neighbour_distance':distance,'expected_distance_2sin_lambda':expected,'lambda_phase':lam,
 'channel_zero_points':{'positive_zero':pplus.tolist(),'negative_real_zero':pminus.tolist()},
 'static_phi_divisors':{'geometry_3d_cylinder':cyl3,'alternate_cylinder':cylalt,'alternate_torus':torusalt},
 'numeric_tolerance':{'absolute':1e-14,'relative':0,'purpose':'ordinary rounding in a fixed analytic witness; no source, baseline or diagnostic tolerance changed'},
 'previous_evidence':'66 symbolic predicates and four source replays reused at v0.1 identities; GPT 27 groups/147 conditions supplied, not rerun'}
Path(a.output).write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':sum(checks.values()),'pdf_pages':pages,'neighbour_distance':distance,'static_divisors':record['static_phi_divisors']},indent=2))
