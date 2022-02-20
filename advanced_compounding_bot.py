import pyautogui
import time
from datetime import datetime


class AdvancedCompoundingBot:
    def __init__(self):
        self.timers = {
            "refresh_interval": ""
        }

    def refresh_website(self):
        chrome_tab_location = pyautogui.locateOnScreen('chrome-tab.png', confidence=0.95)
        if chrome_tab_location == None:

            print("please open a browser with the theanimal.farm website")
        else:
            chrome_tab_location_center = pyautogui.center(chrome_tab_location)
            pyautogui.click(chrome_tab_location_center.x, chrome_tab_location_center.y)
            pyautogui.press('f5')
            time.sleep(4)

    def goto_garden_tab(self):
        garden_tab_location = pyautogui.locateOnScreen('drip-garden-tab.png', confidence=0.95)
        if garden_tab_location == None:
            print("could not find the drip garden tab")
        else:
            garden_tab_location_center = pyautogui.center(garden_tab_location)
            time.sleep(1)
            pyautogui.click(garden_tab_location_center.x, garden_tab_location_center.y)

    def adjust_position(self):
        time.sleep(1)
        garden_heading_location = pyautogui.locateOnScreen('garden-heading.png', confidence=0.95)
        plant_status_found = False
        compound_button_found = False
        if garden_heading_location != None:
            garden_heading_location_center = pyautogui.center(garden_heading_location)
            pyautogui.click(garden_heading_location_center.x, garden_heading_location_center.y)
        while(plant_status_found != True or compound_button_found != True):
            plant_status_found = pyautogui.locateOnScreen('plant-status.png', confidence=0.80) != None
            compound_button_found = pyautogui.locateOnScreen('compound-button.png', confidence=0.95) != None or pyautogui.locateOnScreen('compound-button-not-ready.png', confidence=0.95) != None
            if plant_status_found and compound_button_found:
                break
            pyautogui.scroll(-80)

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
                pyautogui.click(mm_center.x, mm_center.y)
                time.sleep(1)
                pyautogui.scroll(-80)
                time.sleep(1)
                pyautogui.click(1820, 610)
                time.sleep(10)
                return self.check_if_compound_succes()
            else:
                return True
        return True

    def check_if_compound_succes(self):
        return pyautogui.locateOnScreen('mm.png', confidence=0.85) == None and pyautogui.locateOnScreen('ready.png', confidence=0.95) != None

    def cycle(self):
        self.refresh_website()
        self.goto_garden_tab()
        self.adjust_position()
        while True:
            if not self.compound():
                print("breaking")
                break




x = AdvancedCompoundingBot()
x.cycle() 
