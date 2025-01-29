@echo off

:: Setup Python ==============================================
:: Check and update Windows
:: No 'upgrade' available
:: Manually install python3...
:: No need to install pip (is default)
:: No need to install venv (is default)
py -m pip install --upgrade pip

:: Setup VENV ================================================
:: Set the virtual environment directory name
set VENV_DIR=.venv

:: Check if the virtual environment already exists and remove it
if exist %VENV_DIR% (
    echo Removing old virtual environment...
    rmdir %VENV_DIR% /s /q
)

:: Create a new virtual environment
echo Creating new virtual environment...
py -m venv %VENV_DIR%

:: Activate the virtual environment
call %VENV_DIR%\Scripts\activate

:: Update pip for venv
echo Upgrading pip...
py -m pip install --upgrade pip

:: Install MY package in normal mode (without -e)
py -m pip install -e ./build_automation_app

:: Deactivate the virtual environment
call %VENV_DIR%\Scripts\deactivate

:: END ======================================================
echo Script execution complete!
pause
