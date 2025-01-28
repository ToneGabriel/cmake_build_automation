@echo off

:: Set the virtual environment directory name
set VENV_DIR=.venv

:: Activate the virtual environment
call %VENV_DIR%\Scripts\activate

:: Run the Python script
echo Running CMake Build...
py ./buildautomation

:: Deactivate the virtual environment
call %VENV_DIR%\Scripts\deactivate

echo Script execution complete!
pause