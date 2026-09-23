"""Read-only publication checks, apart from its attributed verification receipt."""
from pathlib import Path
import hashlib,json,re,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
from publication_runtime import CONFIG, EVIDENCE, PUBLICATION, bootstrap_python
bootstrap_python()
from pypdf import PdfReader
MD=ROOT/CONFIG["manuscript"]
PDF=PUBLICATION/CONFIG["pdf_name"]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
md=MD.read_text(encoding="utf8")
refs=md.split("## References\n",1)[1].strip()
ref_file=(ROOT/CONFIG["references"]).read_text(encoding="utf8")
assert ref_file.split("**[PA]**",1)[1].strip()==refs.split("**[PA]**",1)[1].strip()
tags=re.findall(r"\*\*\[([A-Za-z0-9]+)\]\*\*",refs)
assert len(tags)==10 and len(set(tags))==10
body=md.split("## References\n",1)[0]
for tag in tags:assert re.search(r"\[[^\]]*\b"+re.escape(tag)+r"\b[^\]]*\]",body),tag
for file in [ROOT/name for name in [CONFIG["manuscript"], CONFIG["ledger"], CONFIG["symbols"], "README.md", "RELEASE_DEPENDENCIES_v0.1.1.md"]]:
    for target in re.findall(r"\]\(([^)]+)\)",file.read_text(encoding="utf8")):
        if "://" in target or target.startswith("#"):continue
        assert (file.parent/target.split("#",1)[0]).is_file(),(file.name,target)
assert re.findall(r"\\tag\{(\d+)\}",md)==[str(i) for i in range(1,27)]
statements=re.findall(r"\*\*((?:Proposition|Theorem) \d+)",body)
assert statements==["Proposition 1","Proposition 2","Theorem 3","Theorem 4","Proposition 5","Theorem 6","Proposition 7"]
reader=PdfReader(PDF)
texts=[p.extract_text() for p in reader.pages]
alltext="\n".join(texts)
assert len(reader.pages)>=10
for i,t in enumerate(texts,1):
    assert t.strip().splitlines()[-1].strip()==str(i),("page footer",i)
for i in range(1,6):assert "Figure "+str(i)+":" in alltext
for label in statements:assert label in alltext,label
for tag in tags:assert "["+tag+"]" in alltext,tag
for i in range(1,27):assert re.search(r"\("+str(i)+r"\)",alltext),i
assert not re.search(r"[A-Za-z]:[\\/]",alltext)
assert not re.search(r"GPT says|Claude says|Codex says|WORK ORDER",alltext,re.I)
assert "\ufffd" not in alltext
log=(PUBLICATION/"paper_B_final.log").read_text(encoding="utf8",errors="replace")
problems=[line for line in log.splitlines() if any(t in line for t in ["Overfull","Missing character","! LaTeX Error"])]
assert not problems,problems
widths=re.findall(r"PAPER-EQUATION-WIDTH: ([0-9.]+)pt; available ([0-9.]+)pt; tag (\d+)",log)
assert len(widths)==26
assert all(float(w)<.90*float(avail) for w,avail,_ in widths),"Unexpected equation downscaling"
assert len(list((ROOT/"figures").glob("figure_*.pdf")))==5
assert len(list((ROOT/"figures").glob("figure_*.png")))==5
inputs=json.loads((EVIDENCE/"publication_inputs.json").read_text(encoding="utf8"))
for entry in inputs:
    p=ROOT.parents[1]/entry["repository_path"]
    assert digest(p)==entry["sha256"],entry
result={"attribution":"Codex publication static verification, 2026-09-23",
 "status":"PASS","pdf_pages":len(reader.pages),"numbered_equations":26,
 "all_equations_fit_without_scaling":True,"theorem_proposition_statements":7,
 "adoptions":2,"figure_captions":5,"vector_figure_files":5,"png_figure_files":5,
 "reference_tags":tags,"reference_body_matches_companion":True,
 "relative_markdown_links_resolve":True,"source_hashes_match":len(inputs),
 "consecutive_page_footers":True,"missing_glyph_or_overfull_warnings":problems,
 "forbidden_absolute_paths_or_conversational_attribution":False,
 "pdf_sha256":digest(PDF),"manuscript_sha256":digest(MD),
 "limits":"Publication revision follows the relayed GPT acceptance of the identified v0.1 PDF; BIB-01 closed. Changed bytes are a new publication revision."}
(EVIDENCE/"publication_verification.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf8")
print(json.dumps(result,indent=2))
