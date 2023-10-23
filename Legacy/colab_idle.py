import pyautogui
import time


def write(text):
    pyautogui.write(text, interval=0.25)
    for _ in range(len(text)):
        pyautogui.press('backspace')


while (True):
    pyautogui.click(600, 600, duration=1)
    pyautogui.click(300, 300, duration=1)
    write('hello')
    pyautogui.press('pagedown')
    time.sleep(5)
    pyautogui.press('pageup')
    time.sleep(60 * 10)
