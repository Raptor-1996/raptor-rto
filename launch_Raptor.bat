@echo off
title Raptor RTO Launcher
color 0A
echo ========================================
echo    🐺 RAPTOR RTO - Ghost Recon Tool 🐺
echo ========================================
echo.
echo [INFO] Starting Raptor Translator...
echo [INFO] Press Ctrl+Shift+L in game for translation
echo [INFO] Close the translation window to exit
echo.
cd /d "C:\Users\orion\Documents\000 Development\raptor_rto"
start /B python raptor_rto.py
echo.
echo [SUCCESS] Raptor is running!
echo [TIP] To close, click X on the translation window
echo.
pause > nul