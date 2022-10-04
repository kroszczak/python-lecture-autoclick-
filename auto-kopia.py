from asyncio import constants
from pynput.mouse import Listener
import pyautogui


def on_click(x, y, button, pressed):
    print(f'{x}, {y}')
    print(pyautogui.position())

with Listener( on_click=on_click ) as listener:
    listener.join()
