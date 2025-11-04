@echo off
title Instagram Account Creator

:: Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python n'est pas installe ou n'est pas dans le PATH
    echo.
    echo Pour installer Python:
    echo 1. Téléchargez Python depuis https://www.python.org/downloads/
    echo 2. Lors de l'installation, cochez "Add Python to PATH"
    echo 3. Redémarrez votre ordinateur
    echo.
    pause
    exit /b 1
)

:: Activer l'environnement virtuel .venv s'il existe
IF EXIST .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
) ELSE (
    echo WARNING: Environnement virtuel .venv non trouve
    echo Creation d'un nouvel environnement virtuel...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    pip install -r requirements.txt
)

:: Lancer le script principal
python creator.py

:: Pause pour voir les erreurs éventuelles
pause
