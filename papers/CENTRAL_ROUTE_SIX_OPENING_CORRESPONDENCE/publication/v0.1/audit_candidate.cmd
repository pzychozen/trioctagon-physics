@echo off
setlocal
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
if errorlevel 1 exit /b %errorlevel%
set PYTHONUTF8=1
cd /d "%~dp0"
python verification\check_edition.py
exit /b %errorlevel%
