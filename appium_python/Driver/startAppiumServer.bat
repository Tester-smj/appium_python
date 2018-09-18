@echo off
title startAppiumServer
cmd /c ' "C:/Program Files/Appium/node.exe" "C:/Program Files/Appium/node_modules/appium/bin/appium.js" --address 127.0.0.1 -p 4723 --session-override '