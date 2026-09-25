"""Bounded PDF structural QA and page renders; visual review is separately recorded."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument("render_dir",type=Path);p.add_argument("--poppler",required=True);args=p.parse_args()
dest=args.render_dir;dest.mkdir(parents=True,exist_ok=True)
pdf=ROOT/"PAPER_F_PUBLICATION_v0.2.pdf";reader=PdfReader(pdf)
texts=[p.extract_text() or "" for p in reader.pages];full="\n".join(texts)
(dest/"extracted_text.txt").write_text(full,encoding="utf-8")
fonts={}
def visit(res):
 if not res:return
 res=res.get_object()
 for f in res.get("/Font",{}).get_object().values() if "/Font" in res else []:
  f=f.get_object();name=str(f.get("/BaseFont"))
  desc=f.get("/FontDescriptor")
  if desc:desc=desc.get_object()
  sub=f.get("/DescendantFonts")
  if sub:desc=sub[0].get_object().get("/FontDescriptor").get_object()
  embedded=bool(desc and any(k in desc for k in ["/FontFile","/FontFile2","/FontFile3"]))
  fonts[name]={"subtype":str(f.get("/Subtype")),"embedded":embedded}
 for x in res.get("/XObject",{}).get_object().values() if "/XObject" in res else []:
  obj=x.get_object()
  if "/Resources" in obj:visit(obj["/Resources"])
for page in reader.pages:visit(page.get("/Resources"))
log=(ROOT/"records/latex_build.log").read_text(encoding="utf-8",errors="replace")
widths=[{"ordinal":i+1,"width_pt":float(w),"available_pt":float(a),"tag":tag.strip(),"scale":min(1,.93*float(a)/float(w))} for i,(w,a,tag) in enumerate(re.findall(r"PAPER-EQUATION-WIDTH: ([0-9.]+)pt; available ([0-9.]+)pt; tag ([^\n]*)",log))]
forbidden=[x for x in ["TODO","TBD","FIXME","0.244","GPT/Hilmir","ready for a publication build","C:\\","C:/","No staging","No publication PDF","NONZERO_LAMBDA"] if x in full]
missing=[tag for tag in [str(i) for i in range(1,62)]+["D1","D2","D3"] if "("+tag+")" not in full]
headings=[x for x in ["Theorem 4","Theorem 5","Theorem 7","Theorem 8","Appendix A.","Appendix B.","Appendix C.","Appendix D.","References","Supplementary reconstruction record"] if x not in full]
result={"pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),"page_count":len(reader.pages),"page_character_counts":[len(x) for x in texts],
 "all_pages_searchable":all(len(x)>150 for x in texts),"metadata":dict(reader.metadata),
 "fonts":fonts,"all_fonts_embedded":all(x["embedded"] for x in fonts.values()),"missing_numbered_equations":missing,
 "missing_required_headings":headings,"forbidden_prose_hits":forbidden,
 "overfull_boxes":re.findall(r"Overfull[^\n]*",log),"missing_glyphs":re.findall(r"Missing character[^\n]*",log),
 "equation_widths":widths,"minimum_display_scale":min(x["scale"] for x in widths),
 "figure_count":full.count("Figure 1:"),"qa_scope":"Structural checks, not a substitute for recorded page-by-page visual inspection."}
assert not forbidden and not missing and not headings
assert result["all_pages_searchable"] and result["all_fonts_embedded"]
assert not result["overfull_boxes"] and not result["missing_glyphs"]
(ROOT/"records/pdf_structural_qa.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
run=subprocess.run([args.poppler,"-r","110","-png",str(pdf),str(dest/"page")],capture_output=True)
assert run.returncode==0,run.stderr
pages=sorted(dest.glob("page-*.png"))
for i in range(0,len(pages),2):
 ims=[]
 for pp in pages[i:i+2]:
  im=Image.open(pp).convert("RGB")
  # 850px width: each complete page is inspected at approximately screen reading scale.
  im=im.resize((850,round(im.height*850/im.width)))
  im=ImageOps.expand(im,border=(5,28,5,5),fill="white");ImageDraw.Draw(im).text((10,6),pp.stem,fill="black")
  ims.append(im)
 sheet=Image.new("RGB",(sum(im.width for im in ims),max(im.height for im in ims)), "#ddd")
 x=0
 for im in ims:sheet.paste(im,(x,0));x+=im.width
 sheet.save(dest/("spread_%02d_%02d.png"%(i+1,min(i+2,len(pages)))))
print(json.dumps({"pages":len(pages),"minimum_display_scale":result["minimum_display_scale"],"fonts":len(fonts),"all_fonts_embedded":result["all_fonts_embedded"]}))
