import pyautogui
import time
from datetime import datetime


class AdvancedCompoundingBot:
    def __init__(self):
        self.timers = {
            "refresh_interval": ""
        }
    def compound(self):
        time.sleep(1)
        compound_button_location = pyautogui.locateOnScreen('compound-button.png', confidence=0.95)
        if compound_button_location != None:
            print("compound button found")
            compound_button_location_center = pyautogui.center(compound_button_location)
            pyautogui.click(compound_button_location_center.x, compound_button_location_center.y)
            time.sleep(2)
            mm_location = pyautogui.locateOnScreen('mm.png', confidence=0.50)
            if mm_location != None:
                mm_center = pyautogui.center(mm_location)
                print("mm position: ", mm_center.x, mm_center.y)
                pyautogui.click(mm_center.x, mm_center.y)
                time.sleep(1)
                pyautogui.scroll(-80)
                time.sleep(1)
                pyautogui.click(1820, 610)
                time.sleep(20)
                compound_success = self.check_if_compound_succes() 
                if compound_success == True:
                    return True
            else:
                return False
        print('compound button not found or not ready')
        return True

    def check_if_compound_succes(self):
        return pyautogui.locateOnScreen('mm.png', confidence=0.85) == None and pyautogui.locateOnScreen('ready.png', confidence=0.95) != None

    def cycle(self):
        while True:
            if not self.compound():
                print("breaking")
                break




x = AdvancedCompoundingBot()
x.cycle()
