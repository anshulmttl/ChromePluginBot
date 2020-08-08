import pyautogui
im = pyautogui.locateOnScreen(r'C:/Users/91702/Documents/Work/Fiverr/ChromePlugin/Capture.PNG')
pyautogui.click(x=im[0],y=im[1],clicks=1,interval=0.0,button="left")