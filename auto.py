from asyncio import constants
from time import time
from turtle import color
from pynput.mouse import Listener
import pyautogui
import os
from PIL import ImageGrab
import time

dir_path = r'./screenshotsauto'
count = 0
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)): count += 1

def loop(pos, color, count, x, y):
    while True:
        time.sleep(1)
        print('robie screena')
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f'./screenshotsauto/file{count}.png')
        count += 1
        while ImageGrab.grab().getpixel(pos) != color:
            print('kolor tła')
            time.sleep(5)
        print('kolor przycisku')
        pyautogui.click(x, y, clicks=2)
        print('kliknalem')




def on_click(x, y, button, pressed):
    global count
    if pressed:
        xval = (x/1440)*2880
        yval = (y/900)*1800
        position = (xval, yval)
        color = ImageGrab.grab().getpixel(position)
        print(f'zapisany kolor: {color}')
        loop(position, color, count, x, y)


with Listener( on_click=on_click ) as listener:
    listener.join()