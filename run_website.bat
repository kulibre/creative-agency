@echo off
echo Starting Local Framer Website...
echo --------------------------------
echo This script starts a custom Python web server.
echo Keep this window OPEN while browsing the site.
echo.

:: Open the browser first (it will wait/load until server is ready)
start "" "http://localhost:8000/index.html"

:: Start the custom server
python server.py

pause
