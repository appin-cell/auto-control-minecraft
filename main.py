import pyautogui as gui
import sys
import pyautogui
import time
import win32gui
app = win32gui.FindWindow(None,'Minecraft 1.19.3 - マルチプレイ（サードパーティーのサーバー）')
time.sleep(1)
win32gui.SetForegroundWindow(memoapp)

try:
    while True:
       x,y = gui.position()
       rgb = gui.pixel(x,y)
       if rgb = 
       

       
except KeyboardInterrupt:
    print('\n終了')
    sys.exit()
