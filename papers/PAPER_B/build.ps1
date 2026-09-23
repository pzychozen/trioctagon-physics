param([string]$PythonExecutable = 'python')
$ErrorActionPreference = 'Stop'
& $PythonExecutable -B -X utf8 (Join-Path $PSScriptRoot 'check_manuscript_algebra.py')
if ($LASTEXITCODE -ne 0) { throw 'Algebra check failed' }
& $PythonExecutable -B -X utf8 (Join-Path $PSScriptRoot 'generate_figures.py')
if ($LASTEXITCODE -ne 0) { throw 'Figure generation failed' }
& $PythonExecutable -B -X utf8 (Join-Path $PSScriptRoot 'build_publication.py')
if ($LASTEXITCODE -ne 0) { throw 'PDF build failed' }
& $PythonExecutable -B -X utf8 (Join-Path $PSScriptRoot 'verify_publication.py')
if ($LASTEXITCODE -ne 0) { throw 'Publication verification failed' }
