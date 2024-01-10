import pyautogui
import time

import pyperclip


def click_ctrl_shift_i():
    # Delay to give time for focus to switch to the target window
    time.sleep(2)

    # Simulate pressing CTRL + SHIFT + I
    pyautogui.hotkey('ctrl', 'shift', 'i')
def zoom_out():
    # Delay to give time for focus to switch to the target window
    time.sleep(2)

    # Simulate pressing CTRL + SHIFT + I
    pyautogui.hotkey('ctrl', 'shift', '-')
def find_field():
    # Delay to give time for focus to switch to the target window
    time.sleep(2)
    # Simulate pressing CTRL + SHIFT + I
    pyautogui.hotkey('ctrl', 'f')
def find_all_types_of_truck():
    not_reached_duplicate = True
    all_availables_found = False
    all_not_availables_found = False
    trk_list = []
    while not_reached_duplicate:
        if not all_availables_found:
            all_found = find_types_of_truck(trk_list,"Availables")
            if all_found:
                all_availables_found = True
        if all_availables_found and not all_not_availables_found:
            all_found = find_types_of_truck(trk_list,"Not Availables")
            if all_found:
                all_availables_found = True
    



def send_string(text):
    # Optional delay to give time for the focus to switch to the target window
    time.sleep(2)

    # Simulate typing the string directly
    pyautogui.typewrite(text)
def find_types_of_truck(trk_list,type):
    if type == "Availables":
        return traverse_through_list(trk_list,"ModBk")
    if type == "Not Availables":
        return traverse_through_list(trk_list,"ModGy")

def traverse_through_list(trk_list,type):
    find_field()
    send_string(type)
    for i in range(len(trk_list) + 1):
        if i == len(trk_list):
            pyautogui.press('tab')
        time.sleep(0.15)
        pyautogui.press('enter')

    copied_content = collect_truck_details(trk_list)
    if copied_content not in trk_list:
        trk_list.append(copied_content)
        return True
    else:
        return False


def collect_truck_details(trk_list):

    pyautogui.hotkey('ctrl', 'c')
    copied_content = pyperclip.paste()
def press_enter_once():
    # Optional delay to give time for the focus to switch to the target window
    time.sleep(2)

    # Simulate pressing the Enter key once
    pyautogui.press('enter')

# Call the function to simulate the keypresses
click_ctrl_shift_i()