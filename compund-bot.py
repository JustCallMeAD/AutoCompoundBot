import pyautogui
import time

while True:
    ready_location = pyautogui.locateOnScreen('ready1.png', confidence=0.95)
    if ready_location != None:
        print("ready found")
        time.sleep(5)
        button_location = pyautogui.locateOnScreen('compound_button.png', confidence=0.95)
        if button_location != None:
            print("comppound button found")
            button_center = pyautogui.center(button_location)
            pyautogui.click(button_center.x, button_center.y)
            time.sleep(5)
            mm_location = pyautogui.locateOnScreen('mm.png', confidence=0.50)
            if mm_location != None:
                print("mm found")
                mm_center = pyautogui.center(mm_location)
                pyautogui.click(mm_center.x, mm_center.y)
                time.sleep(5)
                pyautogui.scroll(-80)
                pyautogui.click(1820, 610)
                time.sleep(10)
                # mm_accept_location = pyautogui.locateOnScreen('test.png', confidence=0.95)
                # if mm_accept_location != None:
                #     print("mm button found")
                #     mm_accept_center = pyautogui.center(mm_accept_location)
                #     print(mm_accept_center.x, mm_accept_center.y)
                #     # pyautogui.click(mm_accept_center.x, mm_accept_center.y)
                #     time.sleep(3)
                # else:
                #     print("mm_accept not found")
                #     exit
        else:
            print("no button found")
