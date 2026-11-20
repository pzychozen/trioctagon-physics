from pathlib import Path
import hashlib, json, re, subprocess, shutil
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
(ROOT/"inspection").mkdir(exist_ok=True)
pdf=ROOT/"output/GM01_GM03_COMBINED_PAPER_v0.1.pdf"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
build=json.loads((ROOT/"BUILD_RECORD.json").read_text("utf-8"))
assert build["returncode"]==0 and build["pdf_sha256"]==sha(pdf)
for name,h in build["sources"].items(): assert sha(ROOT/name)==h, name
log=(ROOT/"build/tex/main.log").read_text("utf-8")
for bad in ["Overfull", "Underfull", "undefined", "Missing character", "multiply defined", "LaTeX Error"]:
    assert bad not in log, bad
alltex="\n".join(p.read_text("utf-8") for p in (ROOT/"manuscript").glob("*.tex"))
labels=re.findall(r"\\label\{([^}]+)\}",alltex)
refs=re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",alltex)
cites=[c for group in re.findall(r"\\cite\{([^}]+)\}",alltex) for c in group.split(",")]
bib=re.findall(r"\\bibitem\{([^}]+)\}",alltex)
assert len(labels)==len(set(labels))
assert set(refs)<=set(labels)
assert set(cites)<=set(bib) and len(bib)==len(set(bib))
aux=(ROOT/"build/tex/main.aux").read_text("utf-8")
assert all("\\newlabel{"+l+"}" in aux for l in labels)
assert all("\\bibcite{"+b+"}" in aux for b in bib)
reader=PdfReader(pdf)
fonts={}
for page in reader.pages:
    for name,obj in page["/Resources"].get("/Font",{}).items():
        font=obj.get_object()
        desc_fonts=font.get("/DescendantFonts",[font])
        for sub in desc_fonts:
            sub=sub.get_object()
            descriptor=sub.get("/FontDescriptor")
            assert descriptor, str(font)
            descriptor=descriptor.get_object()
            embedded=any(k in descriptor for k in ["/FontFile","/FontFile2","/FontFile3"])
            assert embedded
            fonts[str(sub["/BaseFont"])]=dict(subtype=str(sub["/Subtype"]),embedded=True)
texts=[page.extract_text() for page in reader.pages]
assert all(text.strip() for text in texts)
assert "??" not in "\n".join(texts)
(ROOT/"build/PDF_TEXT.txt").write_text("\n\n--- PAGE ---\n\n".join(texts),"utf-8")
links=[]
for n,page in enumerate(reader.pages,1):
    for annot in page.get("/Annots",[]):
        a=annot.get_object().get("/A")
        if a and a.get("/URI"): links.append({"page":n,"uri":str(a["/URI"])})
for link in links:
    u=link["uri"]
    if "github.com/" in u: assert "/ca22652dc000ca2b16419c1af4167918eab1ae94/" in u
for tool in ["pdfinfo","pdffonts"]:
    executable=shutil.which(tool)
    if not executable:
        (ROOT/f"build/{tool}.txt").write_text("CLI unavailable; metadata and all font embeddings checked directly with pypdf.\n","utf-8")
        continue
    p=subprocess.run([executable,str(pdf)],capture_output=True,text=True,encoding="utf-8",errors="replace",check=True)
    (ROOT/f"build/{tool}.txt").write_text(p.stdout,"utf-8")
render=[shutil.which("pdftoppm"),"-r","120","-png",str(pdf),str(ROOT/"inspection/page")]
run=subprocess.run(render,capture_output=True,text=True,check=True)
pages=sorted((ROOT/"inspection").glob("page-*.png"))
assert len(pages)==len(reader.pages)
record=dict(status="PASS",pdf_sha256=sha(pdf),page_count=len(reader.pages),
    labels=len(labels),references=len(refs),bibliography_entries=len(bib),citation_uses=len(cites),
    embedded_fonts=fonts,external_links=links,metadata={str(k):str(v) for k,v in reader.metadata.items()},
    final_tex_warnings=[],source_hashes_match_final_build=True,
    render_command=render,render_stderr=run.stderr,
    rendered_pages=[dict(page=i,path=p.relative_to(ROOT).as_posix(),sha256=sha(p)) for i,p in enumerate(pages,1)],
    visual_inspection="Pending separate human/assistant image inspection record.")
(ROOT/"DOCUMENT_VERIFICATION.json").write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n","utf-8")
print(json.dumps({"status":"PASS","pages":len(reader.pages),"labels":len(labels),"bibliography_entries":len(bib),"fonts":len(fonts),"pdf_sha256":sha(pdf)}))
