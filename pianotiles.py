from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#For mouse position
#pyautogui.displayMousePosition()
#Tile Position format: X:  581 Y:  400 RGB: ( 77,  80, 115)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(315, 698)[1] < 20:
        click(315, 700)
    if pyautogui.pixel(415, 698)[1] < 20:
        click(415, 700)
    if pyautogui.pixel(515, 698)[1] < 20:
        click(515, 700)
    if pyautogui.pixel(615, 698)[1] < 20:
        click(615, 700)
