@echo off
title Handover App
echo Opening the app, please wait...
start "" http://localhost:5000
echo Please refresh the web page now...
dist\app.exe
pause