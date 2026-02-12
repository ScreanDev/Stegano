@echo off
echo --- Checking Python installation ---
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found
    pause
    exit /b
)

echo.
echo --- Creating virtual environment ---

if exist venv (
    echo Virtual environment already exists
) else (
    python -m venv venv
    echo Environment created
)

echo.
echo --- Activation ---
call venv\Scripts\activate.bat

echo.
echo --- Updating PIP ---
python -m pip install --upgrade pip

echo.
echo --- Installing dependencies ---

pip install cx_Freeze Pillow

echo.
echo --- Installation complete ---
echo TROUBLESHOOTING: If you keep having issues with unfound modules, ensure you use the Python interpreter of this virtual environment.
pause