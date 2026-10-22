"""Read/render the built PDF and inspect editorial structure; no scientific checks."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
POP=Path("C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin")
pdf=ROOT/"MANUSCRIPT/volume_i.pdf"
out=ROOT/"build/pdf_review";out.mkdir(parents=True,exist_ok=True)
info=subprocess.check_output([str(POP/"pdfinfo.exe"),str(pdf)],text=True,encoding="utf-8")
(out/"pdfinfo.txt").write_text(info,encoding="utf-8")
count=int(re.search(r"Pages:\s+(\d+)",info).group(1))
sys.path.append("C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/site-packages")
from pypdf import PdfReader
reader=PdfReader(pdf)
assert len(reader.pages)==count
page_text=[p.extract_text() for p in reader.pages]
text="\n\f\n".join(page_text)
(out/"text_layout.txt").write_text(text,encoding="utf-8")
report={"pages":count,"pdf_bytes":pdf.stat().st_size,"pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "extracted_words":len(text.split()),"replacement_characters":text.count("\ufffd"),
        "visible_question_mark_pairs":text.count("??")}
print(json.dumps(report,indent=2))
console=(ROOT/"build/typeset_console.txt").read_text(encoding="utf-8")
for filename,lineno in re.findall(r"warning: ([^:\n]+):(\d+): Overfull",console):
    p=ROOT/"MANUSCRIPT"/filename
    lines=p.read_text(encoding="utf-8").splitlines()
    n=int(lineno)
    print("\nOVERFULL CONTEXT",filename,n)
    for i in range(max(0,n-12),min(len(lines),n+1)):print(f"{i+1}: {lines[i]}")
(ROOT/"records/pdf_structure.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
if "--render" in sys.argv:
    subprocess.run([str(POP/"pdftoppm.exe"),"-r","110","-png",str(pdf),str(out/"page")],check=True)
    pages=sorted(out.glob("page-*.png"))
    assert len(pages)==count
    font=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",18)
    for start in range(0,count,6):
        canvas=Image.new("RGB",(3*420,2*620),"#d9dfe3")
        draw=ImageDraw.Draw(canvas)
        for j,p in enumerate(pages[start:start+6]):
            im=Image.open(p);im.thumbnail((410,580))
            x=j%3*420;y=j//3*620
            canvas.paste(im,(x+5,y+30))
            draw.text((x+8,y+5),f"PDF page {start+j+1}",font=font,fill="black")
        canvas.save(out/f"sheet_{start+1:02d}_{min(start+6,count):02d}.png")
    print("Rendered",count,"pages and contact sheets.")
