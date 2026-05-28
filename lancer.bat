@echo off
cd /d %~dp0
call venv\Scripts\activate
python interface.py
pause