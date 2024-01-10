import time

import pyautogui
import pyperclip

# Start
# Will find Browser and Locate ESL
    # Refresher     #
# Will check ESL for Trucks / ESL Trucks checker
    # Will get all text and store it to a location
# Trucks Counter and details parser
    # Find each truck classification with selected image, later crop until the list ends
    # Record the number of trucks by darkness of the font which resembles availability
    #
# Organise data from the page
# Excel Spreedsheet Updater
# Repeat

# Flaws:
# Need to be logged in and one POS Tab should be open on chrome browser,

# screenshot = pyautogui.screenshot()
# screenshot.save('screens/screenshot.png')  # Save the screenshot

def locateChrome():
    icon = f'screens/icons/chrome_icon.png'
    icon_location = pyautogui.locateCenterOnScreen(icon)
    # Upload image to Gpt
    # Check if the Chrome icon was found
    if icon_location is not None:
        # Move the cursor to the icon's location
        pyautogui.moveTo(icon_location)

        # Click the icon to open Chrome
        pyautogui.click()
        return True
    else:
        print("Chrome icon not found on the screen.")
        return False
def locateESL():
    try:
        icon = f'screens/icons/UH_Icons/POS_icon.png'
        icon_location = pyautogui.locateCenterOnScreen(icon)
        # Upload image to Gpt
        # Check if the Chrome icon was found
        if icon_location is not None:
            # Move the cursor to the icon's location
            pyautogui.moveTo(icon_location)

            # Click the icon to open Chrome
            pyautogui.click()
            return True
        else:
            print("ESL not open on the chrome browser!")
            return False
    except Exception as e:
        print("POS is Selected?")
        try:
            icon = f'screens/icons/UH_Icons/selected_POS_icon.png'
            icon_location = pyautogui.locateCenterOnScreen(icon)
            if icon_location is not None:
                return True
        except Exception as e:
            print("ESL not loaded!")
            return False
def remove_back_up_contract_pop_up():
    print("Locating Close Icon")
    icon = f'screens/icons/UH_Icons/Pop_ups/close_pop_up.png'
    icon_location = pyautogui.locateCenterOnScreen(icon)
    # Upload image to Gpt
    # Check if the pop up shows up
    if icon_location is not None:
        print("Found Close Icon")
        # Move the cursor to the icon's location
        pyautogui.moveTo(icon_location)

        # Click the icon to open Chrome
        pyautogui.click()
        return True
    else:
        print("ESL not open on the chrome browser!")
        return False
def look_back_up_contract_pop_up():
    icon = f'screens/icons/UH_Icons/Pop_ups/backup_contract_pop_up.png'
    icon_location = pyautogui.locateCenterOnScreen(icon)
    # Upload image to Gpt
    # Check if the pop up shows up
    if icon_location is not None:
        print("Pop up found!")
        remove_back_up_contract_pop_up()
        return True
    else:
        print("ESL not open on the chrome browser!")
        return False
def refreshESL():
    print("Attempting to refresh")
    try:
        icon = f'screens/icons/UH_Icons/Refresh_icon.png'
        icon_location = pyautogui.locateCenterOnScreen(icon)
        # Move the cursor to the icon's location
        pyautogui.moveTo(icon_location)

        # Click the icon to open Chrome
        pyautogui.click()
        return True
        # Upload image to Gpt
    except Exception as e:
        print("searching for Back up contract pop up")
        try:
            look_back_up_contract_pop_up()
            refreshESL()
        except Exception as e:
            try:
                icon = f'screens/icons/UH_Icons/select_Refresh_icon.png'
                icon_location = pyautogui.locateCenterOnScreen(icon)
                pyautogui.locateOnScreen()
                # Move the cursor to the icon's location
                pyautogui.moveTo(icon_location)

                # Click the icon to open Chrome
                pyautogui.click()
                return True
            except Exception as e:
                print("Unknown error occurred while refreshing")
    # Check if the Chrome icon was found

def getESLPageDetails():
    # Perform the 'Select All' operation
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)  # Wait a bit for the operation to complete

    # Perform the 'Copy' operation
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait a bit for the operation to complete

    # Retrieve the text from the clipboard and store it in a variable
    allText = pyperclip.paste()

    print(allText)
    return allText

# Find the exact
start_time = time.time()
locateChrome()
time.sleep(5)
locateESL()
time.sleep(7)
refreshESL()
time.sleep(5)
getESLPageDetails()
end_time = time.time()

# Calculate the total time taken

time_taken = end_time - start_time

print("Time taken: ", time_taken, "seconds")
