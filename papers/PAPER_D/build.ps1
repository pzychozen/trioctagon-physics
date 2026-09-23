param(
  [Parameter(Mandatory=$true)][string]$Python,
  [Parameter(Mandatory=$true)][string]$Pandoc,
  [Parameter(Mandatory=$true)][string]$Tectonic,
  [Parameter(Mandatory=$true)][string]$TexCache,
  [string]$PythonLibraryPath = ''
)
$ErrorActionPreference = 'Stop'
$env:PAPER_D_PANDOC = $Pandoc
$env:PAPER_D_TECTONIC = $Tectonic
$env:PAPER_D_TEX_CACHE = $TexCache
$env:PAPER_D_PYTHON_PATH = $PythonLibraryPath
$env:PYTHONDONTWRITEBYTECODE = '1'
Push-Location $PSScriptRoot
try {
  & $Python generate_figures.py
  if ($LASTEXITCODE -ne 0) { throw 'Figure generation failed.' }
  & $Python -c "import pathlib,subprocess,sys; r=subprocess.run([sys.executable,'verify_manuscript.py'],capture_output=True); pathlib.Path('evidence/manuscript_checks_stdout.txt').write_bytes(r.stdout+r.stderr); print(r.stdout.decode()); sys.exit(r.returncode)"
  if ($LASTEXITCODE -ne 0) { throw 'Manuscript checks failed.' }
  & $Python build_publication.py
  if ($LASTEXITCODE -ne 0) { throw 'PDF build failed.' }
} finally { Pop-Location }
# Preserved predecessor checks are deliberately not executed.
# The supplied SHA256SUMS binds the delivered package, not a new rebuild.

