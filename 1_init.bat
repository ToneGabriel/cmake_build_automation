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

:: Check if the virtual environment already exists
echo Creating virtual environment...
if not exist %VENV_DIR% (
    py -m venv %VENV_DIR%
)

:: Activate the virtual environment
call %VENV_DIR%\Scripts\activate

:: Update pip for venv
echo Upgrading pip...
py -m pip install --upgrade pip

:: Install Req packages
echo Installing requirements...
py -m pip install -r requirements.txt

:: Install MY package in normal mode
py -m pip install ./buildautomation

:: Deactivate the virtual environment
call %VENV_DIR%\Scripts\deactivate

:: END ======================================================
echo Script execution complete!
pause
