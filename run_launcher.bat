@echo off
title Raptor RTO Manager
color 0A

:menu
cls
echo ========================================
echo    🐺 RAPTOR RTO - CONTROL CENTER 🐺
echo ========================================
echo.
echo  [1] ▶ Start Raptor (With GUI Launcher)
echo  [2] ▶ Start Raptor (Direct - No GUI)
echo  [3] ⏹ Stop Raptor
echo  [4] 🔄 Restart Raptor
echo  [5] 📊 Check Status
echo  [6] ❌ Exit
echo.
echo ========================================
set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto start_gui
if "%choice%"=="2" goto start_direct
if "%choice%"=="3" goto stop_raptor
if "%choice%"=="4" goto restart_raptor
if "%choice%"=="5" goto check_status
if "%choice%"=="6" goto exit
goto menu

:start_gui
cls
echo [INFO] Starting Graphical Launcher...
cd /d "C:\Users\orion\Documents\000 Development\raptor_rto"
start python raptor_launcher.py
echo [SUCCESS] Launcher started!
timeout /t 2 > nul
goto menu

:start_direct
cls
echo [INFO] Starting Raptor Translator directly...
cd /d "C:\Users\orion\Documents\000 Development\raptor_rto"
start /B python raptor_rto.py
echo [SUCCESS] Raptor is running!
echo [TIP] Press Ctrl+Shift+L in game
timeout /t 2 > nul
goto menu

:stop_raptor
cls
echo [INFO] Stopping Raptor...
taskkill /f /im python.exe > nul 2>&1
echo [SUCCESS] Raptor stopped!
timeout /t 2 > nul
goto menu

:restart_raptor
cls
echo [INFO] Restarting Raptor...
taskkill /f /im python.exe > nul 2>&1
timeout /t 1 > nul
cd /d "C:\Users\orion\Documents\000 Development\raptor_rto"
start /B python raptor_rto.py
echo [SUCCESS] Raptor restarted!
timeout /t 2 > nul
goto menu

:check_status
cls
tasklist /FI "IMAGENAME eq python.exe" 2>NUL | find /I /N "python.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [STATUS] ✅ Raptor is RUNNING
    echo [HOTKEY] Ctrl+Shift+L
) else (
    echo [STATUS] ❌ Raptor is NOT running
)
echo.
pause
goto menu

:exit
cls
echo [INFO] Goodbye Raptor! 🐺
timeout /t 1 > nul
exit