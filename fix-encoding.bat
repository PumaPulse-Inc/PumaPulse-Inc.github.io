@echo off
echo Fixing broken encoding in all HTML files...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0fix-encoding.ps1"
pause
