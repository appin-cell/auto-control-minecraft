import pyautogui as gui
import sys
import pyautogui
import time
import win32gui
import pydirectinput as direct
app = win32gui.FindWindow(None,'Minecraft 1.19.3 - マルチプレイ（サードパーティーのサーバー）')
time.sleep(1)
win32gui.SetForegroundWindow(memoapp)

try:
    while True:
       pyautogui.move(0, 1, duration=0.001)
       x,y = gui.position()
       rgb = gui.pixel(x,y)
       if rgb = 92, 72, 40:
           direct.mousedown()
           time.sleep(0.8)
           pyautogui.move(0,-150,duration=0.1)
           time.sleep(0.8)
           pyautogui.move(0,300,duration=0.1)
           
           
           
           
       

       
except KeyboardInterrupt:
    print('\n終了')
    sys.exit()
