@echo off
call conda activate torment
if errorlevel 1 exit /b %errorlevel%
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
cd /d "%~dp0"
python -B %*
exit /b %errorlevel%
