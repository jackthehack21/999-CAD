@echo off
cd /d %~dp0

if exist start.py (
    set START=start.py
) else (
    echo "Couldn't find a valid entry point."
    pause
    exit 1
)

py %START% %*
pause