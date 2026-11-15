@echo off
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
if errorlevel 1 exit /b %errorlevel%
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
set GIT_OPTIONAL_LOCKS=0
cd /d C:\TORMENT\NRD01\run_20261115_01
python -B %*
exit /b %errorlevel%
