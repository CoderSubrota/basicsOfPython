import pyautogui as py
import time 

time.sleep(5)
for i in range(10):
    py.write("I Love to Code !!\n", interval=0.1)
    py.press("enter")
    