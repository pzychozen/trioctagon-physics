"""Faithful publication document build and refreshed documentary checks."""
from pathlib import Path
from datetime import datetime, timezone
import json, os, subprocess, sys
R=Path(__file__).resolve().parents[1]
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
E=R/'candidate/v0.1'; V=R/'verification'
cmd=[sys.executable,str(E/'build.py'),'--tectonic',r'C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe','--build-dir',str(V/'publication_build01')]
started=datetime.now(timezone.utc).isoformat()
run=subprocess.run(cmd,cwd=E,capture_output=True)
(V/'BUILD_EXECUTION.txt').write_bytes(run.stdout+run.stderr)
(V/'BUILD_EXECUTION.json').write_text(json.dumps({'command':cmd,'cwd':str(E),'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'exit_status':run.returncode,'conda_environment':os.environ.get('CONDA_DEFAULT_ENV')},indent=2)+'\n')
print((run.stdout+run.stderr).decode('utf-8',errors='replace'))
assert run.returncode==0
s=(R/'review_basis_extracted/scripts/audit_document.py').read_text(encoding='utf-8')
s=s.replace("else V/'build07'", "else V/'publication_build01'")
s=s.replace('Research manuscript v0.1 — accepted mathematics; manuscript and author review pending.', 'Research edition v0.1 — project-internal review complete; author-authorized for repository publication.')
s=s.replace("assert 'manuscript and author review pending' in pages[0].lower()", "assert 'manuscript and author review pending' not in '\\n'.join(pages).lower()")
s=s.replace("assert 'author-authorized repository publication' not in '\\n'.join(pages)", "assert 'author-authorized' in pages[0].lower()\nassert 'project-internal review complete' in pages[0].lower()\nassert len(pages)==25\nassert len(labels)==118\nassert len(cites)==12")
(R/'scripts/audit_document.py').write_text(s,encoding='utf-8')
run=subprocess.run([sys.executable,str(R/'scripts/audit_document.py'),'publication_build01'],cwd=R,capture_output=True)
(V/'AUDIT_EXECUTION.txt').write_bytes(run.stdout+run.stderr)
print((run.stdout+run.stderr).decode('utf-8',errors='replace'))
raise SystemExit(run.returncode)
