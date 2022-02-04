import pyautogui
import time

while True:
    ready_location = pyautogui.locateOnScreen('ready1.png', confidence=0.95)
    if ready_location != None:
        print(ready_location)
        time.sleep(60)
        button_location = pyautogui.locateOnScreen('compound_button.png', confidence=0.95)
        if button_location != None:
            button_center = pyautogui.center(button_location)
            pyautogui.click(button_center.x, button_center.y)
        else:
            print("no button found")