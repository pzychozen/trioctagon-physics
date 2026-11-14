@echo off
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
if errorlevel 1 exit /b %errorlevel%
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
cd /d %~dp0
python -B %*
exit /b %errorlevel%
