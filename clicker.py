import pyautogui
import time

pyautogui.PAUSE = 1

positions = [[(443, 470), (505, 470), (578, 470)], [(443, 540), (505, 540), (578, 540)],
             [(443, 615), (505, 615), (578, 615)]]


def send_click(x, y):
    pyautogui.click(positions[x][y])


def restart_click():
    time.sleep(5)
    pyautogui.click()
