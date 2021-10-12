import time
import pyautogui

print('Auto Mouse Mover Activated, press Ctrl-C to quit.')

try:
    while True:
        pyautogui.moveRel(10, 0, 0.5)
        pyautogui.moveRel(-10, 0, 0.5)
        time.sleep(3)
except KeyboardInterrupt:
    print('Auto Mouse Mover De-Activated.')
