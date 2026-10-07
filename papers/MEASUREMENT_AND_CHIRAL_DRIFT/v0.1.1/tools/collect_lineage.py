"""Read-only primary-source excerpts; no historical script is executed."""
from pathlib import Path
from pypdf import PdfReader
import hashlib,json,shutil
BASE=Path('C:/TORMENT/TRIOCTAGON_new')
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'measurement/supplement/lineage'
sha=lambda b:hashlib.sha256(b).hexdigest()
records=[]
docs=[
('J1','research/top_to_recursive_bridge/sources/17253999/17253999/1.Symbolic Recursion and SRG Fusion.pdf',[1,2,3],'Symbolic Recursion and SRG Fusion: Emergent Lattice Fields from Glyph Memory Dynamics','July 15, 2025'),
('J2','research/top_to_recursive_bridge/sources/17253999/17253999/2.Symbolic Cosmogenesis Neutrino Collapse Recursive Memory and SRG Lattice Feedback.pdf',[1,2,3,5,6],'Symbolic Cosmogenesis: Neutrino Collapse, Recursive Memory, and SRG Lattice Feedback','July 15, 2025'),
('J3','research/top_to_recursive_bridge/sources/17253999/17253999/3.Symbolic Recursion and SRG Formation Full Method and Emergence.pdf',[1,2,3,5],'Symbolic Recursion and SRG Formation: Full Method and Emergence','July 14, 2025'),
('P21','pdfs_old/Recursive_Engines_Across_Scales__From_Vesica_Thermodynamics_to_QGS.pdf',[1,4,5,16,17,18],'Recursive Engines in Folded Tri-Octagon Geometry: From Symbolic Qubits to the Dual-Tetrahedral SRG Core','November 24, 2025'),
('P23','pdfs_old/Recursive_SRG_Evolution_qutrip_opperator_dual_core_geometry_computational_interpretation.pdf',[1,2,3,4,5,6,30],'Recursive SRG Evolution: A Qutrit-Qubit Operator, Dual-Core Geometry, and Computational Interpretation','November 24, 2025'),
]
for sid,rel,pages,title,date in docs:
    p=BASE/rel;b=p.read_bytes();reader=PdfReader(p)
    name=f'{sid}_primary_excerpts.txt'
    text=f'{sid}: {title}\nPrinted date: {date}\nProject-relative archival locator: {rel}\nOriginal PDF SHA-256: {sha(b)}\nPDF page numbers: {pages}\nExtracted with pypdf; extraction is not a facsimile. Historical claims are quoted source material, not adopted results.\n\n'
    for n in pages:text+=f'=== PDF PAGE {n} ===\n'+reader.pages[n-1].extract_text()+'\n\n'
    (DEST/name).write_text(text,encoding='utf-8')
    records.append({'id':sid,'title':title,'printed_date':date,'original_project_locator':rel,'original_sha256':sha(b),'original_bytes':len(b),'original_pages':len(reader.pages),'selected_pdf_pages':pages,'excerpt_path':'measurement/supplement/lineage/'+name,'excerpt_sha256':sha((DEST/name).read_bytes()),'disposition':'verbatim page-text extraction with explicit provenance header; historical assertions not validated or adopted'})
archive='trioctagon-physics/research_files/archive_members/Zenodo_research/17253999/Reading material.zip/Reading material/'
for sid,n in [('S1','RPCO.py'),('S2','TGMO.py'),('S3','REFU.py')]:
    rel=archive+n;b=(BASE/rel).read_bytes();name=n+'.txt';(DEST/name).write_bytes(b)
    records.append({'id':sid,'original_project_locator':rel,'original_sha256':sha(b),'original_bytes':len(b),'copy_path':'measurement/supplement/lineage/'+name,'copy_sha256':sha(b),'disposition':'unchanged script bytes with .txt suffix for source-only use; undated member; not executed'})
rel='trioctagon-physics/research_files/sources/Zenodo_research/17253999/recursive_field_evolve.py'
b=(BASE/rel).read_bytes();(DEST/'recursive_field_evolve.py.txt').write_bytes(b)
records.append({'id':'S4','original_project_locator':rel,'original_sha256':sha(b),'original_bytes':len(b),'copy_path':'measurement/supplement/lineage/recursive_field_evolve.py.txt','copy_sha256':sha(b),'disposition':'unchanged source-only bytes; contains random forcing, not executed'})
for n in ['geometry.py','srg.py','dynamics.py']:
    p=BASE/'trioctagon-physics/kernel_physics'/n;target=ROOT/'measurement/supplement/native/kernel_physics'/n
    assert p.read_bytes()==target.read_bytes()
    records.append({'id':'N-'+n,'original_project_locator':'trioctagon-physics/kernel_physics/'+n,'original_sha256':sha(p.read_bytes()),'copy_path':str(target.relative_to(ROOT)).replace('\\','/'),'copy_sha256':sha(target.read_bytes()),'disposition':'unchanged existing pinned native software copy; current HEAD has identical bytes'})
(ROOT/'provenance/lineage_sources.json').write_text(json.dumps(records,indent=2)+'\n')
print('Recorded 5 primary PDF excerpt sets, 4 unchanged historical script snapshots, and 3 unchanged native source identities.')
