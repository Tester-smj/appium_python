#coding = utf-8
import os

def AppiumServer():
    '''通过命令行启动AppiumServer'''
    # start = 'cmd /c "appium -a 127.0.0.1 -p 4723 --session-override -log-no-color"'
    start = 'cmd /c " "D:/Program Files (x86)/Appium/node.exe" "D:/Program Files (x86)/Appium/node_modules/appium/bin/appium.js" --address 127.0.0.1 -p 4723 --session-override" '
    # start = 'cmd/c "D:/Program Files (x86)/Appium/node.exe lib/server/main.js" --address 127.0.0.1 --port 4723 --platform-name Android --platform-version 21 --automation-name Appium --device-name "" --log-no-color'
    return os.system(start)

AppiumServer()