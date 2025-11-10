@echo off
REM Seg-NN CPU Implementation - Windows Installation Script
REM This script automates the environment setup process

echo ========================================
echo Seg-NN CPU Environment Setup
echo ========================================
echo.

REM Check if conda is available
where conda >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Conda not found. Please install Anaconda or Miniconda first.
    echo Download from: https://www.anaconda.com/download
    pause
    exit /b 1
)

echo [1/5] Creating Conda environment...
call conda create -n SegNN python=3.8 -y
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to create conda environment
    pause
    exit /b 1
)

echo.
echo [2/5] Activating environment...
call conda activate SegNN

echo.
echo [3/5] Installing PyTorch (CPU version)...
call conda install pytorch==1.12.0 torchvision==0.13.0 cpuonly -c pytorch -y
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install PyTorch
    pause
    exit /b 1
)

echo.
echo [4/5] Installing required packages...
call pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install required packages
    pause
    exit /b 1
)

echo.
echo [5/5] Installing dummy PointNet2 module...
cd pointnet2_dummy
call pip install -e .
cd ..

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Next steps:
echo   1. Activate the environment: conda activate SegNN
echo   2. Run tests: python scripts/test_environment.py
echo   3. Check README.md for more information
echo.
pause
