"""Bounded Paper E artifact checks. No source execution or scientific regeneration."""
import runtime
from runtime import ROOT
import hashlib,json,re,sys
import numpy as np
from pypdf import PdfReader

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
checks={}
def check(name,value):
    checks[name]=bool(value)
    assert value,name

provenance=read('evidence/source_provenance.json')
for row in provenance['copies']:
    check('copy_'+row['copy'],sha(ROOT/row['copy'])==row['sha256'])
sym=read('evidence/symbolic_results.json')
check('66_symbolic_predicates',len(sym['predicates'])==66 and all(sym['predicates'].values()))
prior=read('evidence/accepted_reconstruction/verification_results.json')
check('63_prior_predicates_reused',len(prior['checks'])==63 and all(prior['checks'].values()))
data=np.load(ROOT/'evidence/plot_data.npz',allow_pickle=False)
results=read('evidence/plot_data_results.json')
check('frozen_data_identity',sha(ROOT/'evidence/plot_data.npz')==results['data_sha256'])
check('baseline_EMA_same_Omega',np.array_equal(data['baseline__Omega'],data['ema__Omega']))
observed={}
for name,token in [('subcritical','869bf44ed4'),('critical','37abc4f4f9')]:
    source=next((ROOT/'evidence/preserved_runs').glob('*'+token+'*_series.csv'))
    csv=np.genfromtxt(source,delimiter=',',names=True)
    z=np.column_stack([csv[k] for k in ['Zx','Zy','Zz']])
    for label,a,b in [('Z',z,data[name+'__Z_total']),('v',csv['v_rec'][1:],data[name+'__v']),('J',csv['J_eff'],data[name+'__J'])]:
        check(name+'_'+label+'_saved_array_equal',np.array_equal(a,b,equal_nan=True))
    v=data[name+'__v']; badz=np.flatnonzero(~np.isfinite(z).all(axis=1));badv=np.flatnonzero(~np.isfinite(v))
    observed[name]={'finite_events':int(np.sum(np.isfinite(v)&(v>=.8))),
      'first_nonfinite_Z':int(badz[0]) if len(badz) else None,
      'first_nonfinite_v_endpoint':int(badv[0])+1 if len(badv) else None}
check('saved_event_counts',observed['subcritical']['finite_events']==26 and observed['critical']['finite_events']==1277)
check('failure_alignment',observed['critical']['first_nonfinite_Z']==1279 and observed['critical']['first_nonfinite_v_endpoint']==1278)
check('subcritical_finite',observed['subcritical']['first_nonfinite_Z'] is None and observed['subcritical']['first_nonfinite_v_endpoint'] is None)
samples={}
for name,rows in [('subcritical',[8,501]),('critical',[1001,1276,1277])]:
    samples[name]={str(row):{k:float(data[name+'__'+k][row-1]) for k in ['v','dZ','dphi','dcorr','dkappa']} for row in rows}
pdf=ROOT/'publication/PAPER_E_Z_MANIFOLD_v0.1.pdf';reader=PdfReader(pdf)
check('28_PDF_pages',len(reader.pages)==28)
md=(ROOT/'PAPER_E_Z_MANIFOLD_v0.1.md').read_text(encoding='utf-8')
check('23_required_sections',[int(x) for x in re.findall(r'^## (\d+)\.',md,re.M)]==list(range(1,24)))
check('40_numbered_equations',[int(x) for x in re.findall(r'\\tag\{(\d+)\}',md)]==list(range(1,41)))
fidelity=read('evidence/structural_fidelity.json')
check('complete_equation_bodies',fidelity['all_equation_bodies_retained'] and fidelity['display_blocks']==40)
check('11_manuscript_figures',fidelity['figures']==11)
check('complete_figure_sets',all(len(list((ROOT/'figures').glob('*.'+ext)))==11 for ext in ['pdf','svg','png']))
figures=read('evidence/figure_manifest.json')
check('figure_data_identity',figures['data_sha256']==results['data_sha256'])
build=read('publication/build_record.json')
check('build_pdf_identity',sha(pdf)==build['pdf_sha256'])
check('build_manuscript_identity',sha(ROOT/'PAPER_E_Z_MANIFOLD_v0.1.md')==build['manuscript_sha256'])
check('build_TeX_identity',sha(ROOT/'paper_E_v0.1.tex')==build['tex_sha256'])
log=(ROOT/'publication/paper_E_v0.1.log').read_text(errors='replace')
check('no_overfull_or_missing_glyph',not re.search(r'Overfull|Missing character',log))
equations=re.findall(r'PAPER-EQUATION-WIDTH: ([\d.]+)pt; available ([\d.]+)pt; tag (\d+)',log)
check('all_math_natural_size',len(equations)==40 and all(float(w)<=.93*float(available) for w,available,_ in equations))
approved={
 'B':('PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.pdf','5555eb4f07b0974addced80339bf0f87bb7a5ab87d268926f321a3c586da35ad'),
 'D':('PAPER_D/v0.1.1/publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf','7c4c52f8018765b21a7849d03ce7974824351e5af27c99356c5acb0b5dcaaaaf')}
for key,(path,h) in approved.items():
    p=ROOT.parent/path
    # External originals are checked when present; portable copies retain their recorded identities.
    if p.exists():check('approved_'+key+'_PDF_unchanged',sha(p)==h)
record={'attribution':'New Codex bounded artifact inspection, no new source replay',
 'checks':checks,'passed':sum(checks.values()),'observed_runs':observed,'quoted_component_samples':samples,
 'pdf_pages':len(reader.pages),'pdf_sha256':sha(pdf),'python':sys.version,
 'visual_review':'Recorded separately in BUILD_AND_QA.md; not inferred by this script'}
(ROOT/'evidence/package_checks.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'pdf_pages':len(reader.pages),'runs':observed},indent=2))
