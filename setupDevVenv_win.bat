@echo off
echo --- Verification de l'installation de Python ---
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found
    pause
    exit /b
)

echo.
echo --- Creation de l'environnement virtuel (venv) ---

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
pause