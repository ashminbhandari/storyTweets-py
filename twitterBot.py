#Import driver
from driver import driver

#Config import
from config import config

#Time to sleep
import time

#To check if the screenshot exists
import os

#Start up driver and take tweet screenshot
def takeScreenshot(url):
    theDriver = driver(withHomeDir=False, headless=True)
    theDriver.get(url)
    time.sleep(4)  # Give it 4 seconds to load
    screenshotURL = config['save_path'] + '/screenshot.png'
    theDriver.save_screenshot(screenshotURL)
    theDriver.quit()
    time.sleep(1)
    if os.path.isfile(screenshotURL):
        print('Tweet snapped...')
    else:
        print('Failed to snap tweet')
        return False
    return True