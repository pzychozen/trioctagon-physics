@echo off
call C:\Users\Notandi\miniconda3\condabin\conda.bat activate torment
if errorlevel 1 exit /b %errorlevel%
set PYTHONUTF8=1
set PYTHONDONTWRITEBYTECODE=1
cd /d C:\TORMENT\TRIOCTAGON_new\research\NATIVE_TURNING_CAPTURE_01\run_20261110_01
python %*
exit /b %errorlevel%
