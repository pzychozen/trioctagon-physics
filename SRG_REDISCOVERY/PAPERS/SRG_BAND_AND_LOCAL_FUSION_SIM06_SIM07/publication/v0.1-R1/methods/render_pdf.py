"""Render/extract the candidate PDF only; no scientific data processing."""
from pathlib import Path
import subprocess, json, hashlib, sys
sys.path.insert(0, str(Path('C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/site-packages')))
from pypdf import PdfReader
root=Path(__file__).resolve().parents[1]
bin=Path("C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin")
out=root/"build/pages"; out.mkdir(parents=True,exist_ok=True)
cmd=[str(bin/"pdftoppm.exe"),"-r","120","-png",str(root/"manuscript.pdf"),str(out/"page")]
if '--extract-only' not in sys.argv:
    subprocess.run(cmd,check=True)
reader=PdfReader(root/'manuscript.pdf')
(root/'build/manuscript.txt').write_text('\n\f\n'.join(p.extract_text() for p in reader.pages),encoding='utf-8')
info=subprocess.run([str(bin/"pdfinfo.exe"),"-f","1","-l",str(len(reader.pages)),str(root/"manuscript.pdf")],capture_output=True,text=True,check=True).stdout
(root/"build/pdfinfo.txt").write_text(info,encoding="utf-8")
print(info)
print('PDF has',len(reader.pages),'pages; old renders may remain locally after a shorter rebuild')

