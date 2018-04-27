@echo off
set my_dir=%~dp0%
call %my_dir%\CONFIG.bat
set my_script_name=%~n0%
%PYTHON% %my_dir%\..\bin\%my_script_name%.py %*
