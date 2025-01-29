@echo off

:: Set the virtual environment directory name
set VENV_DIR=.venv

if not exist %VENV_DIR%\Scripts\activate (
    echo No virtual environment. Call 1_init.bat and try again...
    pause
    exit
)

:: Activate the virtual environment
call %VENV_DIR%\Scripts\activate

:: Run the Python script
echo Running CMake Build...
py ./build_automation_app ./data.json

:: Deactivate the virtual environment
call %VENV_DIR%\Scripts\deactivate

echo Script execution complete!
pause