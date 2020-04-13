#Instagram bot for posting to stories

# Get the driver
from driver import driver

# Get the config
from config import config

#Simulate keyboard inputs
from pynput.keyboard import Key, Controller

#Send keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Time for sleep
import time

# Exception handling for when we don't find elements
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

# Success flag trickles down with execution of each element,
# if the last element was a success, we succeeded in uploading our story
SUCCESS = False

# Executes a DOM element,
# xPath = The xPath of the element to execute
# sleepTime = After each execution, sleep some time
# keys = pass in '0' to execute a click or the actual key to send ex: username, password
def executeElement(theDriver, xPath, sleepTime, keys):
    global SUCCESS
    try:
        if (keys != '0'):
            theDriver.find_element_by_xpath(xPath).send_keys(keys)
        else:
            theDriver.find_element_by_xpath(xPath).click()
        SUCCESS = True
        time.sleep(sleepTime)
    except NoSuchElementException:
        SUCCESS = False
        print("Couldn't find an element")

#Set up and save user data to avoid future logins
def instagramSetup():
    theDriver = driver(withHomeDir=True, headless=False)

    # Prompt login
    theDriver.get('http://instagram.com/accounts/login')

def postToStory():
    #Start up driver
    theDriver = driver(withHomeDir=True, headless=False)

    # Get Instagram
    theDriver.get('http://instagram.com/')
    time.sleep(4)

    # Click add story
    executeElement(theDriver, "//*[@id='react-root']/section/nav[1]/div/div/header/div/div[1]/button", 2, '0')

    # Click not now
    executeElement(theDriver, "/html/body/div[4]/div/div[2]/div/div[5]/button", 2, '0')

    # Activate keyboard
    keyboard = Controller()

    # Navigate to the home directory (MAC) or any other directory able to be reached by a shortcut
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press('h')
    keyboard.release('h')
    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)

    # Write down the file name
    for char in "screenshot.png":
        keyboard.press(char)
        keyboard.release(char)

    # Press enter to select the photo
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    # Open inspect element, this shortcut may change for windows
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press('c')
    keyboard.release('c')
    time.sleep(2)

    #Turn off element selector
    keyboard.press('c')
    keyboard.release('c')
    time.sleep(2)

    # Toggle device mode, this shortcut may change for windows
    keyboard.press('M')
    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)
    time.sleep(2)

    #Finally add to stories
    executeElement(theDriver, "//*[@id='react-root']/section/footer/div/div/button", 10, '0')

    theDriver.quit()

    #If the success flag trickled down to a true means story uploaded
    if SUCCESS:
        print('Tweet successfully pushed to Instagram stories')
        return True
    return False

